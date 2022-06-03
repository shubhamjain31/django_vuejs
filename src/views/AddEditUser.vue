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
                    <h3 class="mb-0" v-if="!id">Add User</h3>
                    <h3 class="mb-0" v-if="id">Edit User</h3>
                  </div>
                  <div class="col-4 text-right">
                    <router-link :to="{ path: '/users/'}"><button class="btn btn-sm btn-primary">Back</button></router-link>
                  </div>
                </div>
              </div>
            </template>

            <form role="form" @submit.prevent="submitForm">
              <h6 class="heading-small text-muted mb-4">User information</h6>
              <div class="pl-lg-4">
                <div class="row">
                  <div class="col-lg-6">
                    <base-input
                      alternative=""
                      label="First Name*"
                      placeholder="First Name"
                      input-classes="form-control-alternative"
                      v-model="model.first_name"
                    />
                  </div>
                  <div class="col-lg-6">
                    <base-input
                      alternative=""
                      label="Last Name*"
                      placeholder="Last Name"
                      input-classes="form-control-alternative"
                      v-model="model.last_name"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col-lg-6">
                    <base-input
                      alternative=""
                      label="Username*"
                      placeholder="example123"
                      input-classes="form-control-alternative"
                      v-model="model.username"
                    />
                  </div>
                  <div class="col-lg-6">
                    <base-input
                      alternative=""
                      type="email"
                      label="Email address*"
                      placeholder="you@example.com"
                      input-classes="form-control-alternative"
                      v-model="model.email"
                    />
                  </div>
                </div>
                  <div class="row">
                  <div class="col-lg-6">
                    <base-input
                      alternative=""
                      type="password"
                      label="Password*"
                      placeholder="Password"
                      input-classes="form-control-alternative"
                      v-model="model.password"
                    />
                  </div>
                  <div class="col-lg-6">
                    <base-input
                      alternative=""
                      type="password"
                      label="Confirm Password*"
                      placeholder="Confirm Password"
                      input-classes="form-control-alternative"
                      v-model="model.confirm_password"
                    />
                  </div>
                </div>
                <div class="text-center">
                    <button class="input-group-text bg-primary text-white" >Add User</button>
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

export default {
  name: "add-edit-user",
  data() {
    if(this.$route.params.id){
      this.getuser(this.$route.params.id);
    }
    return {
      id: this.$route.params.id,
      model: {
        first_name: "",
        last_name: "",
        username: "",
        email: "",
        firstName: "",
        password: "",
        confirm_password: ""
      },
    };
  },
  methods: {
    getuser(id){
        axios.get('http://localhost:8000/api/get-user/'+id,{
            headers: {
            Authorization: 'Token ' + localStorage.getItem('token')
            }
          })
          .then(response =>{
            if(response["data"]["status"] === 200){
              this.model = response.data.data;
            }
          })
    },
    submitForm() {
        let self = this;

         if(this.model.first_name.trim().length===0){
          self.$toast.error(`Enter First Name`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.last_name.trim().length===0){
          self.$toast.error(`Enter Last Name`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.username.trim().length===0){
          self.$toast.error(`Enter Username`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.email.trim().length===0){
          self.$toast.error(`Enter Email`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.password.trim().length===0){
          self.$toast.error(`Enter Password`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.confirm_password.trim().length===0){
          self.$toast.error(`Enter Confirm Password`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.password.trim().length!=this.model.confirm_password.trim().length){
          self.$toast.error(`Password Do Not Match`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.$route.params.id){
          axios.put("http://localhost:8000/api/edit-user/"+this.$route.params.id, this.model
              )
            .then(function (response) {
              if(response["data"]["status"] === 200){
                self.$toast.success(response["data"]["message"], {"position": "top-right", "duration": 3000});
                self.reset();
              }

              if(response["data"]["status"] === 400){
                self.$toast.error(response["data"]["message"], {"position": "top-right", "duration": 3000});
              }
            })
            .catch(function (error) {
              console.log(error);
            });
          }
          else{
            axios.post("http://localhost:8000/api/add-user/", this.model
              )
            .then(function (response) {
              if(response["data"]["status"] === 200){
                self.$toast.success(response["data"]["message"], {"position": "top-right", "duration": 3000});
                self.reset();
              }

              if(response["data"]["status"] === 400){
                self.$toast.error(response["data"]["message"], {"position": "top-right", "duration": 3000});
              }
            })
            .catch(function (error) {
              console.log(error);
            });
          }
    },
    reset() {
      this.model.first_name = "";
      this.model.last_name = "";
      this.model.username = "";
      this.model.email = "";
      this.model.password = "";
      this.model.confirm_password = "";
    },
  },
};
</script>
<style></style>
