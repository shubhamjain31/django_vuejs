<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div class="card bg-secondary shadow border-0">
        <div class="card-header bg-transparent pb-5">
          <div class="text-muted text-center mt-2 mb-3">
            <small>Sign in with</small>
          </div>
          <div class="btn-wrapper text-center">
            <a href="#" class="btn btn-neutral btn-icon">
              <span class="btn-inner--icon"
                ><img src="img/icons/common/github.svg"
              /></span>
              <span class="btn-inner--text">Github</span>
            </a>
            <a href="#" class="btn btn-neutral btn-icon">
              <span class="btn-inner--icon"
                ><img src="img/icons/common/google.svg"
              /></span>
              <span class="btn-inner--text">Google</span>
            </a>
          </div>
        </div>
        <div class="card-body px-lg-5 py-lg-5">
          <div class="text-center text-muted mb-4">
            <small>Or sign in with credentials</small>
          </div>
          <form role="form" @submit.prevent="submitForm">
            <base-input
              formClasses="input-group-alternative mb-3"
              placeholder="Username"
              addon-left-icon="ni ni-hat-3"
              v-model="model.username"
            >
            </base-input>

            <base-input
              formClasses="input-group-alternative mb-3"
              placeholder="Password"
              type="password"
              addon-left-icon="ni ni-lock-circle-open"
              v-model="model.password"
            >
            </base-input>

            <base-checkbox class="custom-control-alternative">
              <span class="text-muted">Remember me</span>
            </base-checkbox>
            <div class="text-center">
              <button class="input-group-text bg-primary text-white text-center mx-auto">Sign in</button>
            </div>
          </form>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-6">
          <router-link to="/forget-password" class="text-light"
            ><small>Forgot password?</small>
          </router-link>
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
  name: "login",
  data() {
    return {
      model: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    
   submitForm() {
        let self = this;

         if(this.model.username.trim().length===0){
          self.$toast.error(`Enter Username`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.password.trim().length===0){
          self.$toast.error(`Enter Password`, {"position": "top-right", "duration": 3000});
          return;
        }

        axios.post("http://localhost:8000/api/login/", this.model
          )
        .then(function (response) {
          if(response["data"]["status"] === 200){
            localStorage.setItem("token", response["data"]["access"]);
            self.$router.push({name: "dashboard"});
          }

          if(response["data"]["status"] === 400){
            self.$toast.error(response["data"]["message"], {"position": "top-right", "duration": 3000});
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
