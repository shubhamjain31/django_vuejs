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
                        <th scope="row">{{index+1}}</th>
                        <td>{{capitalize(item.username)}}</td>
                        <td>{{item.email}}</td>
                        <td>{{format_date(item.date_joined)}}</td>
                        <td>
                           <router-link :to="{ path: '/add-edit-user/'+item.id}"><i class="fa fa-edit text-info" style="font-size:20px; cursor: pointer;" title="Edit User"></i></router-link>&nbsp; &nbsp; 
                           <i class="fa fa-trash text-danger" @click="toggleModal" style="font-size:20px; cursor: pointer;" title="Delete User"></i>&nbsp; &nbsp; 
                            <div>
                              <div
                                ref="modal"
                                class="modal fade"
                                :class="{show, 'd-block': active}"
                                tabindex="-1"
                                role="dialog"
                              >
                                <div class="modal-dialog" role="document">
                                  <div class="modal-content">
                                    <div class="modal-header">
                                      <h5 class="modal-title">Delete User</h5>
                                      <button
                                        type="button"
                                        class="close"
                                        data-dismiss="modal"
                                        aria-label="Close"
                                        @click="toggleModal"
                                      >
                                        <span aria-hidden="true">&times;</span>
                                      </button>
                                    </div>
                                    <div class="modal-body">
                                      <p>Do you want to delete {{item.id}} this user?</p>
                                    </div>
                                    
                                    <div class="modal-footer">
                                      <button type="button" class="btn btn-secondary btn-sm"  @click="toggleModal">Close</button>
                                      <button type="button" class="btn btn-danger btn-sm" @click="delete(item.id)">Delete</button>
                                    </div>
                                  </div>
                                </div>
                              </div>
                              <div v-if="active" class="modal-backdrop fade show"></div>
                            </div>
                        </td>
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
     active: false,
      show: false,
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

    delete(id){
      console.log(id)
    },
    toggleModal() {
      const body = document.querySelector("body");
      this.active = !this.active;
      this.active
        ? body.classList.add("modal-open")
        : body.classList.remove("modal-open");
      setTimeout(() => (this.show = !this.show), 10);
    }
  },
};
</script>
<style></style>
