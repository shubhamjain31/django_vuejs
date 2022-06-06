<template>
  <div class="wrapper" :class="{ 'nav-open': $sidebar.showSidebar }">
    <side-bar
      :background-color="sidebarBackground"
      short-title="HRM"
      title="HRM"
    >
      <template v-slot:links>
        <sidebar-item
          :link="{
            name: 'Dashboard',
            icon: 'ni ni-tv-2 text-primary',
            path: '/dashboard',
          }"
        />

        <sidebar-item
          :link="{
            name: 'Home',
            icon: 'ni ni-send text-blue',
            path: '/icons',
          }"
        />
        <sidebar-item
          :link="{
            name: 'Users',
            icon: 'ni ni-circle-08 text-warning',
            path: '/users',
          }"
        />
        <sidebar-item
          :link="{
            name: 'User Profile',
            icon: 'ni ni-paper-diploma text-orange',
            path: '/maps',
          }"
        />
        <sidebar-item
          :link="{
            name: 'Employees',
            icon: 'ni ni-single-02 text-yellow',
            path: '/employees',
          }"
        />
        <sidebar-item
          :link="{
            name: 'Leave',
            icon: 'ni ni-calendar-grid-58',
            path: '/tables',
          }"
        />
         <sidebar-item
          :link="{
            name: 'Birthday',
            icon: 'ni ni-box-2 text-success',
            path: '/tables',
          }"
        />
         <sidebar-item
          :link="{
            name: 'Logout',
            icon: 'ni ni-user-run text-red',
            path: '/logout',
          }"
        />
      </template>
    </side-bar>
    <div class="main-content" :data="sidebarBackground">
      <dashboard-navbar></dashboard-navbar>

      <div @click="toggleSidebar">
        <!-- your content here -->
        <router-view></router-view>
        <content-footer v-if="!$route.meta.hideFooter"></content-footer>
      </div>
    </div>
  </div>
</template>
<script>
import DashboardNavbar from "./DashboardNavbar.vue";
import ContentFooter from "./ContentFooter.vue";

export default {
  components: {
    DashboardNavbar,
    ContentFooter,
  },
  data() {
    return {
      sidebarBackground: "vue", //vue|blue|orange|green|red|primary
    };
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    },
  },
};
</script>
<style lang="scss"></style>
