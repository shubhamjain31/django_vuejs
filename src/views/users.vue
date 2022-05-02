<template>
  <div>
    <base-header
      class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center"
    >
      <span class="mask bg-gradient-success opacity-8"></span>
      </base-header>

    <div class="container-fluid mt--7">
      <div class="row">
        
        <div class="col-xl-12 order-xl-1">
          <card shadow type="secondary">
            <template v-slot:header>
              <div class="bg-white border-0">
                <div class="row align-items-center">
                  <div class="col-8">
                    <h3 class="mb-0">All Users</h3>
                  </div>
                  <div class="col-4 text-right">
                    <router-link to="/add-edit-user"><button class="btn btn-sm btn-primary">Add</button></router-link>
                  </div>
                </div>
              </div>
            </template>

            <form>
              <h6 class="heading-small text-muted mb-4">User information</h6>
              <div class="pl-lg-4">
                <div class="row">
                 <table class="table">
                    <thead class="text-center">
                      <tr>
                        <th scope="col">Sr No.</th>
                        <th scope="col">Username</th>
                        <th scope="col">Email</th>
                        <th scope="col">Added At</th>
                        <th scope="col">Action</th>
                      </tr>
                    </thead>
                    <tbody class="text-center">
                      <tr v-if="all_users.length==0">
                        <td></td>
                        <td></td>
                        <td class="text-center font-weight-bold">No User</td>
                        <td></td>
                        <td></td>
                      </tr>
                      <tr v-for="(item, index) in all_users.data" :key="item.id">
                        <th scope="row">{{index}}</th>
                        <td>{{capitalize(item.username)}}</td>
                        <td>{{item.email}}</td>
                        <td>{{format_date(item.date_joined)}}</td>
                        <td></td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              
            </form>
          </card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import moment from 'moment'
// this.all_users = [];

export default {
  name: "users",
  data() {
    this.getItems();
  return{
    all_users : {},
  }
  },
  methods: {
    format_date(value){
         if (value) {
           return moment(String(value)).format('DD-MM-YYYY')
          }
      },
      
    capitalize(value) {
      const [firstLetter, ...rest] = value.split('');
      const upperCaseLetter = firstLetter.toUpperCase();
      
      if (firstLetter != upperCaseLetter) {
        return firstLetter.toUpperCase() + rest.join('');
      }
    },

    getItems(){
        axios.get('http://localhost:8000/api/users',{
            headers: {
            Authorization: 'Token ' + localStorage.getItem('token')
            }
          })
          .then(response =>{
            if(response["data"]["status"] === 200){
              this.all_users = response.data;
            }
          })
    },
  }
};
</script>
<style></style>
