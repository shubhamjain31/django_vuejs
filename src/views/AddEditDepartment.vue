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
                    <h3 class="mb-0" v-if="!id">Add Department</h3>
                    <h3 class="mb-0" v-if="id">Edit Department</h3>
                  </div>
                  <div class="col-4 text-right">
                    <router-link :to="{ path: '/departments/'}"><button class="btn btn-sm btn-primary">Back</button></router-link>
                  </div>
                </div>
              </div>
            </template>

            <form role="form" @submit.prevent="submitForm">
              <h6 class="heading-small text-muted mb-4">Department information</h6>
              <div class="pl-lg-4">
                <div class="row">
                  <div class="col-lg-6">
                    <base-input
                      alternative=""
                      label="Name*"
                      placeholder="Name"
                      input-classes="form-control-alternative"
                      v-model="model.name"
                    />
                  </div>
                  <div class="col-lg-6">
                    <base-input
                      alternative=""
                      label="Description*"
                      placeholder="Description"
                      input-classes="form-control-alternative"
                      v-model="model.description"
                    />
                  </div>
                </div>

                <div class="text-center">
                    <button class="input-group-text bg-primary text-white"  v-if="!id">Add Department</button>
                    <button class="input-group-text bg-primary text-white"  v-if="id">Edit Department</button>
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
  name: "add-edit-department",
  data() {
    if(this.$route.params.id){
      this.getDepartment(this.$route.params.id);
    }
    return {
      id: this.$route.params.id,
      model: {
        name: "",
        description: ""
      },
    };
  },
  methods: {
    getDepartment(id){
        axios.get('http://localhost:8000/api/get-department/'+id,{
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

         if(this.model.name.trim().length===0){
          self.$toast.error(`Enter Name`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.description.trim().length===0){
          self.$toast.error(`Enter Description`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.$route.params.id){
          axios.put("http://localhost:8000/api/edit-department/"+this.$route.params.id, this.model
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
            axios.post("http://localhost:8000/api/add-department/", this.model
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
      this.model.name = "";
      this.model.description = "";
    },
  },
};
</script>
<style></style>
