import { createRouter, createWebHashHistory } from "vue-router";

import DashboardLayout from "@/layout/DashboardLayout";
import AuthLayout from "@/layout/AuthLayout";

import Dashboard from "../views/Dashboard.vue";
import Icons from "../views/Icons.vue";
import Maps from "../views/Maps.vue";
import Profile from "../views/UserProfile.vue";
import Tables from "../views/Tables.vue";

import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import ForgetPassword from "../views/ForgetPassword.vue";
import NewPassword from "../views/NewPassword.vue";
import Users from "../views/users.vue";
import AddEditUser from "../views/AddEditUser.vue";
import Employees from "../views/employees.vue";
import Roles from "../views/Roles.vue";
import AddEditRole from "../views/AddEditRole.vue";
import Departments from "../views/Departments.vue";
import AddEditEmployee from "../views/AddEditEmployee.vue";
import AddEditDepartment from "../views/AddEditDepartment.vue";

function authGuard(to, from, next)
{
 var isAuthenticated= false;
if(localStorage.getItem('token'))
  isAuthenticated = true;
 else
  isAuthenticated= false;

 if(isAuthenticated) 
 {
  next(); // allow to enter route
 } 
 else
 {
  next('/login'); // go to '/login';
 }
}

function loginGuard(to, from, next)
{
 var isAuthenticated= false;
if(localStorage.getItem('token'))
  isAuthenticated = true;
 else
  isAuthenticated= false;

 if(isAuthenticated) 
 {
  next('/dashboard'); // go to '/dashboard';
 } 
 else
 {
  next(); // allow to enter route;
 }
}


const routes = [
  {
    path: "/",
    redirect: "/dashboard",
    beforeEnter : authGuard,
    component: DashboardLayout,
    children: [
      {
        path: "/dashboard",
        name: "dashboard",
        beforeEnter : authGuard,
        components: { default: Dashboard },
      },
      {
        path: "/icons",
        name: "icons",
        components: { default: Icons },
      },
      {
        path: "/maps",
        name: "maps",
        components: { default: Maps },
      },
      {
        path: "/profile",
        name: "profile",
        components: { default: Profile },
      },
      {
        path: "/tables",
        name: "tables",
        components: { default: Tables },
      },
      {
        path: "/users",
        name: "users",
        components: { default: Users },
      },
      {
        path: "/add-edit-user/:id",
        // name: "add-edit-user",
        components: { default: AddEditUser },
      },
      {
        path: "/add-edit-user",
        name: "add-edit-user",
        components: { default: AddEditUser },
      },
      {
        path: "/employees",
        name: "employees",
        components: { default: Employees },
      },
      {
        path: "/add-edit-employee",
        name: "add-edit-employee",
        components: { default: AddEditEmployee },
      },
      {
        path: "/roles",
        name: "roles",
        components: { default: Roles },
      },
      {
        path: "/add-edit-role",
        name: "add-edit-role",
        components: { default: AddEditRole },
      },
      {
        path: "/add-edit-role/:id",
        components: { default: AddEditRole },
      },
      {
        path: "/departments",
        name: "departments",
        components: { default: Departments },
      },
      {
        path: "/add-edit-department",
        name: "add-edit-department",
        components: { default: AddEditDepartment },
      },
      {
        path: "/add-edit-department/:id",
        components: { default: AddEditDepartment },
      },
    ],
  },
  {
    path: "/",
    redirect: "login",
    component: AuthLayout,
    children: [
      {
        path: "/login",
        name: "login",
        beforeEnter : loginGuard,
        components: { default: Login },
      },
      {
        path: "/register",
        name: "register",
        beforeEnter : loginGuard,
        components: { default: Register },
      },
      {
        path: "/forget-password",
        name: "forget-password",
        beforeEnter : loginGuard,
        components: { default: ForgetPassword },
      },
      {
        path: "/new-password/:id",
        name: "new-password",
        beforeEnter : loginGuard,
        components: { default: NewPassword },
      },
    ],
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  linkActiveClass: "active",
  routes,
});

export default router;
