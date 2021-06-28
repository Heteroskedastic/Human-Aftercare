<style scoped>
  .page-bar {
    margin-top: -15px;
    margin-bottom: 15px;
  }
</style>
<template>
  <!--begin::Subheader-->
  <div class="subheader py-2 py-lg-4 subheader-solid" id="kt_subheader">
    <div class="container-fluid d-flex align-items-center justify-content-between flex-wrap flex-sm-nowrap">
      <div class="d-flex align-items-center flex-wrap mr-2">
        <slot name="pre-title"></slot>
        <slot name="title">
          <h5 class="text-dark font-weight-bold mt-2 mb-2 mr-5">
            <slot name="title-text">
              {{ $route.meta.pageInfo.title }}
            </slot>
          </h5>
        </slot>
        <slot name="post-title"></slot>
        <div class="subheader-separator subheader-separator-ver mt-2 mb-2 mr-4 bg-gray-200"></div>
        <ul class="breadcrumb breadcrumb-transparent breadcrumb-dot font-weight-bold p-0 my-2 font-size-sm">
          <slot name="breadcrumb-items">
            <li class="breadcrumb-item text-muted">
              <a is="router-link" :to="{name: homeRoute}" class="text-muted"><i class="fa fa-home"></i></a>
            </li>
            <li class="breadcrumb-item text-muted" v-if="$route.meta.pageInfo.back">
              <a is="router-link" :to="{name: $route.meta.pageInfo.back}" class="text-muted">
                {{$router.resolve({name: $route.meta.pageInfo.back}).resolved.meta.pageInfo.title}}
              </a>
            </li>
          </slot>
          <slot name="breadcrumb-title">
            <li class="breadcrumb-item text-muted">
              <slot name="breadcrumb-title-text">
                <span class="text-muted">{{$route.meta.pageInfo.title}}</span>
              </slot>
            </li>
          </slot>

        </ul>
      </div>
      <div class="d-flex align-items-center">
        <slot name="toolbar-items">
<!--          <a href="#" class="btn btn-clean btn-sm font-weight-bold font-size-base mr-1">Today</a>-->
        </slot>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  props: {
    isFixed: {
      type: Boolean,
      default: true
    },
    customHomeRoute: {
      type: String
    }
  },
  data: function() {
    return {
      homeRoute: this.customHomeRoute ||
                 this.$route.params.homeRoute ||
                 this.$route.meta.pageInfo.home ||
                 (this.$route.matched[0] || {}).meta.rootRoute ||
                 this.$rns.ROOT
    }
  }
};
</script>
