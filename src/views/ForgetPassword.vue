<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div class="card bg-secondary shadow border-0">
        <div class="card-header bg-transparent pb-5">
          <div class="text-muted text-center mt-2 mb-3">
            <small>Forget Password</small>
          </div>
        </div>
        <div class="card-body px-lg-5 py-lg-5">
          <form role="form" @submit.prevent="submitForm">
            <base-input
              formClasses="input-group-alternative mb-3"
              placeholder="Email"
              addon-left-icon="ni ni-hat-3"
              v-model="model.email"
            >
            </base-input>

            <div class="text-center">
              <button class="input-group-text bg-primary text-white text-center mx-auto">Submit</button>
            </div>
          </form>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-6">
          <router-link to="/login" class="text-light"
            ><small>Login</small></router-link
          >
        </div>
        <div class="col-6 text-right">
          <router-link to="/register" class="text-light"
            ><small>Create new account</small></router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "forget-password",
  data() {
    return {
      model: {
        email: "",
      },
    };
  },
  methods: {
    
   submitForm() {
        let self = this;

         if(this.model.email.trim().length===0){
          self.$toast.error(`Enter Email`, {"position": "top-right", "duration": 3000});
          return;
        }

        axios.post("http://localhost:8000/api/forget-password/", this.model
          )
        .then(function (response) {
          if(response['data']['status'] === 200){
            self.$toast.success(`Reset Link Sent to `+self.model.email, {"position": "top-right", "duration": 3000});
            self.model.email = "";
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
<style></style>
