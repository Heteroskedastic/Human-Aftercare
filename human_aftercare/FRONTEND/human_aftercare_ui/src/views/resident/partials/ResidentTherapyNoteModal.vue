<style>
#residentTherapyNoteModal .modal-body {
  padding: 0;
}
</style>

<template>
  <b-modal
    ref="modalRef"
    id="residentTherapyNoteModal"
    hide-footer
    @show="onShowModal"
    :title="record && record.id? 'Edit Therapy Note': 'Add Therapy Note'"
    size="lg"
    body-class=""
  >
    <form class="modal-form" @submit.prevent="saveRecord">
      <div class="modal-form-content">
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right">Resident</label>
          <div class="col-lg-9 col-xl-6">
            <span class="form-control form-control-lg form-control-solid">{{displayUser(resident)}}</span>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right">Date/Time</label>
          <div class="col-lg-9 col-xl-6">
            <div class="input-group input-group-lg input-group-solid">
              <div class="input-group-prepend datetime-picker cursor-pointer">
                <span class="input-group-text">
                  <i class="la la-calendar"></i>
                </span>
              </div>
              <vue-datetimepicker
                  v-model="record.datetime"
                  placeholder=""
                  name="datetime"
                  :wrap="true"
                  iconRef=".datetime-picker"
                  class="form-control form-control-lg form-control-solid"
                  :config="{format: 'YYYY-MM-DD HH:mm', formatTime:'h:mm A', mask: true, step: 5, scrollInput: false}">
              </vue-datetimepicker>
            </div>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right">Duration</label>
          <div class="col-lg-9 col-xl-6">
            <div class="input-group input-group-solid">
              <input v-model="record.duration_minutes" class="form-control form-control-lg form-control-solid"
                   min="1" step="1" type="number" required/>
              <div class="input-group-append">
                <span class="input-group-text">
                  Minutes
                </span>
              </div>
            </div>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right">Note</label>
          <div class="col-lg-9 col-xl-6">
            <textarea v-model="record.note" rows="5" class="form-control form-control-lg form-control-solid" required></textarea>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <span
          ref="deleteConfirm"
          v-if="record.id"
          @confirmed="deleteRecord"
          is="inline-confirm"
          btn-class="btn btn-light-danger font-weight-bold"
          sure-class="text-danger"
          yes-class="btn-danger"
          no-class="btn-secondary"
          confirming-icon-class="fa fa-spin fa-spinner"
          class="inline mr-auto"
          :confirming="deleting"
          :disabled="$cannot('delete', 'therapynote')"
        >
          <i class="far fa-trash-alt"></i> Delete
        </span>
        <button type="button" class="btn btn-light-primary font-weight-bold" @click="hide">
          Close
        </button>
        <button
          v-if="record.id"
          type="submit"
          class="btn btn-warning"
          :disabled="saving || $cannot('change', 'therapynote')"
        >
          <i :class="saving? 'fa fa-spin la-spinner':'fa fa-edit'"></i>
          <span v-show="!saving">Update</span>
          <span v-show="saving">Updating</span>
        </button>
        <button v-else type="submit" class="btn btn-success" :disabled="saving">
          <i :class="saving? 'fa fa-spin la-spinner':'fa fa-plus'"></i>
          <span v-show="!saving">Add</span>
          <span v-show="saving">Adding</span>
        </button>
      </div>
    </form>
  </b-modal>
</template>

<script>
import moment from "moment";

import UtilMixin from "@/components/mixins/UtilMixin";
import InlineConfirm from "@/components/libs/InlineConfirm";
import VueDatetimepicker from "@/components/libs/VueDatetimepicker";

export default {
  mixins: [UtilMixin],
  components: {VueDatetimepicker, InlineConfirm},
  props: {
    resident: {
      type: Object
    }
  },
  data: function() {
    return {
      saving: false,
      deleting: false,
      record: {}
    };
  },
  methods: {
    show: function(record) {
      if (record !== undefined) {
        this.record = Object.assign({}, record);
      } else {
        this.record = {};
      }
      this.$refs.modalRef.show();
    },
    hide: function() {
      this.$refs.modalRef.hide();
    },
    onShowModal: function() {
      this.saving = false;
    },
    deleteRecord: function() {
      this.deleting = true;
      this.$http.delete(`therapy_note/${this.record.id}`).then(
        (response) => {
          this.showSuccess("Therapy Note deleted successfully", 5000);
          this.deleting = false;
          this.hide();
          this.$emit("saved-success");
        },
        (error) => {
          this.deleting = false;
          this.showDefaultServerError(error);
        }
      );
    },
    saveRecord: function() {
      this.saving = true;
      var url = "therapy_note",
          httpFunc = this.$http.post,
          successMessage = "Therapy Note added successfully";
      if (this.record.id) {
        url = `therapy_note/${this.record.id}/`;
        httpFunc = this.$http.patch;
        successMessage = "Therapy Note updated successfully";
      }
      var postData = Object.assign({}, this.record);
      if (postData.datetime) {
        postData.datetime = moment(postData.datetime).utc().format("YYYY-MM-DDTHH:mm:ss\\Z");
      }
      postData.resident = this.resident.id;
      httpFunc(url, postData).then((response) => {
        this.saving = false;
        this.showSuccess(successMessage, 5000);
        this.hide();
        this.saving = false;
        this.$emit("saved-success");
      },
      (error) => {
        this.saving = false;
        this.showDefaultServerError(error);
      });
    }
  }
};
</script>
