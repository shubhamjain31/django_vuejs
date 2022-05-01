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
                    <thead>
                      <tr>
                        <th scope="col">#</th>
                        <th scope="col">First</th>
                        <th scope="col">Last</th>
                        <th scope="col">Handle</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td></td>
                        <td class="text-center font-weight-bold" v-if="login">No User</td>
                        <td></td>
                      </tr>
                      <tr v-if="!login">
                        <th scope="row">1</th>
                        <td></td>
                        <td></td>
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
export default {
  name: "users",
  data() {
    // return {
    //   model: {
    //     username: "",
    //     email: "",
    //     firstName: "",
    //     lastName: "",
    //     address: "",
    //     city: "",
    //     country: "",
    //     zipCode: "",
    //     about: "",
    //   },
    // };
  return{
    login: true,
  }
  },
};
</script>
<style></style>
