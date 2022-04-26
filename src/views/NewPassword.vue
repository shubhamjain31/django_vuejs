<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div class="card bg-secondary shadow border-0">
        <div class="card-header bg-transparent pb-5">
          <div class="text-muted text-center mt-2 mb-3">
            <small>Reset Password</small>
          </div>
          
        </div>
        <div class="card-body px-lg-5 py-lg-5">
          <div class="text-center text-muted mb-4">
            <small>Reset Password</small>
          </div>
          <form role="form" @submit.prevent="submitForm">
            <base-input
              formClasses="input-group-alternative mb-3"
              placeholder="Password"
              type="password"
              addon-left-icon="ni ni-lock-circle-open"
              v-model="model.password"
            >
            </base-input>

            <base-input
              formClasses="input-group-alternative mb-3"
              placeholder="Re-Password"
              type="password"
              addon-left-icon="ni ni-lock-circle-open"
              v-model="model.repassword"
            >
            </base-input>

            <div class="text-center">
              <button class="input-group-text bg-primary text-white text-center mx-auto">Reset</button>
            </div>
          </form>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-6">
          <router-link to="/login" class="text-light">
            <small>Login</small>
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
  name: "new-password",
  data() {
    return {
      model: {
        password: "",
        repassword: "",
      },
    };
  },
  methods: {
    
   submitForm() {
        let self = this;
        this.model['reset_link'] = self.$route.params.id;

         if(this.model.password.trim().length===0){
          self.$toast.error(`Enter Password`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.repassword.trim().length===0){
          self.$toast.error(`Enter Re-Password`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.password.length<8 || this.model.repassword.length<8){
          self.$toast.error(`Password Length Must Be 8 Characters!`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.password!=this.model.repassword){
          self.$toast.error(`Password Not Matching!`, {"position": "top-right", "duration": 3000});
          return;
        }

        axios.patch("http://localhost:8000/api/forget-password/", this.model
          )
        .then(function (response) {
          if(response["data"]["status"] === 200){
            self.$router.push({name: "login"});
            self.$toast.success(response["data"]["message"], {"position": "top-right", "duration": 3000});
          }

          if(response["data"]["status"] ===400){
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
