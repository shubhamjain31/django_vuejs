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
                    <h3 class="mb-0" v-if="!id">Add Employee</h3>
                    <h3 class="mb-0" v-if="id">Edit Employee</h3>
                  </div>
                  <div class="col-4 text-right">
                    <router-link :to="{ path: '/employees/'}"><button class="btn btn-sm btn-primary">Back</button></router-link>
                  </div>
                </div>
              </div>
            </template>

            <form role="form" @submit.prevent="submitForm">
              <h6 class="heading-small text-muted mb-4">Employee information</h6>
              <div class="pl-lg-4">
                <div class="row">
                  <div class="col-lg-3">
                    <label for="exampleFormControlSelect1" class="font-weight-bold">Title*</label>
                    <select class="form-control" v-model="model.title">
                        <option value="Mr">Mr</option>
                        <option value="Mrs">Mrs</option>
                        <option value="MSS">Mss</option>
                        <option value="Mss">Dr</option>
                        <option value="Sir">Sir</option>
                        <option value="Madam">Madam</option>
                    </select>
                  </div>
                   <div class="col-lg-3">
                   <label for="exampleFormControlSelect1" class="font-weight-bold">Roles*</label>
                    <select class="form-control"  v-model="model.user_set">
                        <option value="">----Select----</option>
                        <option v-for="item in roles" :value="item.id"  :key="item.id">{{item.name}}</option>
                    </select>
                  </div>
                  <div class="col-lg-3" v-if="id">
                    <label for="exampleFormControlSelect1" class="font-weight-bold">Profile*</label>
                    <input type="file" class="form-control-file" id="exampleFormControlFile1" @change="uploadImage($event)">
                  </div>
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="First Name*"
                      placeholder="First Name"
                      input-classes="form-control-alternative"
                      v-model="model.firstname"
                    />
                  </div>
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Last Name*"
                      placeholder="Last Name"
                      input-classes="form-control-alternative"
                      v-model="model.lastname"
                    />
                  </div>
                </div>

                 <div class="row">
                  <div class="col-lg-3">
                    <label for="exampleFormControlSelect1" class="font-weight-bold">Sex*</label>
                    <select class="form-control" v-model="model.sex">
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Other">Other</option>
                        <option value=">Not Known">Not Known</option>
                    </select>
                  </div>
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Bio*"
                      placeholder="Bio"
                      input-classes="form-control-alternative"
                      v-model="model.bio"
                    />
                  </div>
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Other Name*"
                      placeholder="Other Name"
                      input-classes="form-control-alternative"
                      v-model="model.othername"
                    />
                  </div>
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Birthday*"
                      placeholder="Birthday"
                      input-classes="form-control-alternative"
                      v-model="model.birthday"
                      type="date"
                    />
                  </div>
                </div>

                 <div class="row">
                   <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Religion*"
                      placeholder="Religion"
                      input-classes="form-control-alternative"
                      v-model="model.religion"
                    />
                  </div>
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Nationality*"
                      placeholder="Nationality"
                      input-classes="form-control-alternative"
                      v-model="model.nationality"
                    />
                  </div>
                  <div class="col-lg-3">
                   <label for="exampleFormControlSelect1" class="font-weight-bold">Departments*</label>
                    <select class="form-control"  v-model="model.department_set">
                        <option value="">----Select----</option>
                        <option v-for="item in departments" :value="item.id" :key="item.id">{{item.name}}</option>
                    </select>
                  </div>
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Home Town*"
                      placeholder="Home Town"
                      input-classes="form-control-alternative"
                      v-model="model.hometown"
                    />
                  </div>
                </div>

                <div class="row">
                   <div class="col-lg-3">
                    <label for="exampleFormControlSelect1" class="font-weight-bold">Region*</label>
                    <select class="form-control" v-model="model.region">
                        <option value="Ahafo">Ahafo</option>
                        <option value="Ashanti">Ashanti</option>
                        <option value="Bono East">Bono East</option>
                        <option value="Bono">Bono</option>
                        <option value="Central">Central</option>
                        <option value="Eastern">Eastern</option>
                        <option value="Greater">Greater Accra</option>
                        <option value="Northen East">Northen East</option>
                        <option value="Northen">Northen</option>
                        <option value="Oti">Oti</option>
                        <option value="Savannah">Savannah</option>
                        <option value="Upper East">Upper East</option>
                        <option value="Upper West">Upper West</option>
                        <option value="Volta">Volta</option>
                        <option value="Western North">Western North</option>
                        <option value="Western">Western</option>
                    </select>
                  </div>
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Residence*"
                      placeholder="Residence"
                      input-classes="form-control-alternative"
                      v-model="model.residence"
                    />
                  </div>
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Address*"
                      placeholder="Address"
                      input-classes="form-control-alternative"
                      v-model="model.address"
                    />
                  </div>
                  <div class="col-lg-3">
                    <label for="exampleFormControlSelect1" class="font-weight-bold">Education*</label>
                    <select class="form-control" v-model="model.education">
                        <option value="Senior High School">Senior High School</option>
                        <option value="Junior High School">Junior High School</option>
                        <option value="Primary School">Primary School</option>
                        <option value="Tertiary/University/Polytechnic">Tertiary/University/Polytechnic</option>
                        <option value="OLevel">OLevel</option>
                        <option value="Other">Other</option>
                    </select>
                  </div>
                </div>

                <div class="row">
                   <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Last Work*"
                      placeholder="Last Work"
                      input-classes="form-control-alternative"
                      v-model="model.lastwork"
                    />
                  </div>
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Position*"
                      placeholder="Position"
                      input-classes="form-control-alternative"
                      v-model="model.position"
                    />
                  </div>
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="SSN Number*"
                      placeholder="SSN Number"
                      input-classes="form-control-alternative"
                      v-model="model.ssnitnumber"
                    />
                  </div>
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Tin Number*"
                      placeholder="Tin Number"
                      input-classes="form-control-alternative"
                      v-model="model.tinnumber"
                    />
                  </div>
                </div>

                <div class="row">
                   <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Start Date*"
                      placeholder="Start Date"
                      input-classes="form-control-alternative"
                      v-model="model.startdate"
                      type="date"
                    />
                  </div>
                  <div class="col-lg-3">
                    <label for="exampleFormControlSelect1" class="font-weight-bold">Employee Type*</label>
                    <select class="form-control" v-model="model.employeetype">
                        <option value="Full-Time">Full-Time</option>
                        <option value="Part-Time">Part-Time</option>
                        <option value="Contract">Contract</option>
                        <option value="Intern">Intern</option>
                    </select>
                  </div>
                  <!-- <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="SSNIT Number*"
                      placeholder="SSNIT Number"
                      input-classes="form-control-alternative"
                      v-model="model.ssnitnumber"
                    />
                  </div> -->
                  <div class="col-lg-3">
                    <base-input
                      alternative=""
                      label="Date Issued*"
                      placeholder="Date Issued"
                      input-classes="form-control-alternative"
                      v-model="model.dateissued"
                      type="date"
                    />
                  </div>
                </div>

                <div class="text-center">
                    <button class="input-group-text bg-primary text-white"  v-if="!id">Add Employee</button>
                    <button class="input-group-text bg-primary text-white"  v-if="id">Edit Employee</button>
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
  name: "add-edit-role",
  data() {
    if(this.$route.params.id){
      this.getuser(this.$route.params.id);
    }
    else{
      this.getdata();
    }
    return {
      id: this.$route.params.id,
      model: {
        title: "Mr",
        user_set: "",
        firstname: "",
        lastname: "",
        sex: '>Not Known',
        bio: "",
        othername: "",
        birthday: "",
        religion: "",
        nationality: "",
        department_set: "",
        hometown: "",
        region: "Ahafo",
        residence: "",
        address: "",
        education: "Senior High School",
        lastwork: "",
        position: "",
        ssnitnumber: "",
        tinnumber: "",
        startdate: "",
        employeetype: "Full-Time",
        dateissued: "",
      },
      roles: [],
      departments: [],
    };
  },
  methods: {
    getuser(id){
        axios.get('http://localhost:8000/api/get-employee/'+id,{
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
    getdata(){
        axios.get('http://localhost:8000/api/employees/',{
            headers: {
            Authorization: 'Token ' + localStorage.getItem('token')
            }
          })
          .then(response =>{
            if(response["data"]["status"] === 200){
              this.roles = response.data.data2;
              this.departments = response.data.data1;
              console.log(this.departments,this.roles)
            }
          })
    },
    uploadImage(event) {
    let data = new FormData();
    data.append('name', 'profile');
    data.append('file', event.target.files[0]); 
    },
    submitForm() {
        let self = this;

         if(this.model.title.trim().length===0){
          self.$toast.error(`Enter Name`, {"position": "top-right", "duration": 3000});
          return;
        }

        // if(this.model.description.trim().length===0){
        //   self.$toast.error(`Enter Description`, {"position": "top-right", "duration": 3000});
        //   return;
        // }

        if(this.model.firstname.trim().length===0){
          self.$toast.error(`Enter First Name`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.lastname.trim().length===0){
          self.$toast.error(`Enter Last Name`, {"position": "top-right", "duration": 3000});
          return;
        }
        
        if(this.model.bio.trim().length===0){
          self.$toast.error(`Enter Bio`, {"position": "top-right", "duration": 3000});
          return;
        }
        
        if(this.model.othername.trim().length===0){
          self.$toast.error(`Enter Other Name`, {"position": "top-right", "duration": 3000});
          return;
        }
        
        if(this.model.birthday.trim().length===0){
          self.$toast.error(`Enter Birthday`, {"position": "top-right", "duration": 3000});
          return;
        }
        
        if(this.model.religion.trim().length===0){
          self.$toast.error(`Enter Religion`, {"position": "top-right", "duration": 3000});
          return;
        }
        
        if(this.model.nationality.trim().length===0){
          self.$toast.error(`Enter Nationality`, {"position": "top-right", "duration": 3000});
          return;
        }
        
        if(this.model.hometown.trim().length===0){
          self.$toast.error(`Enter Hometown`, {"position": "top-right", "duration": 3000});
          return;
        }
        
        if(this.model.residence.trim().length===0){
          self.$toast.error(`Enter Residence`, {"position": "top-right", "duration": 3000});
          return;
        }
        
        if(this.model.address.trim().length===0){
          self.$toast.error(`Enter Address`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.lastwork.trim().length===0){
          self.$toast.error(`Enter Lastwork`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.position.trim().length===0){
          self.$toast.error(`Enter Position`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.ssnitnumber.trim().length===0){
          self.$toast.error(`Enter Ssnit Number`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.tinnumber.trim().length===0){
          self.$toast.error(`Enter Tin Number`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.startdate.trim().length===0){
          self.$toast.error(`Enter Start Date`, {"position": "top-right", "duration": 3000});
          return;
        }

        if(this.model.dateissued.trim().length===0){
          self.$toast.error(`Enter Date Issued`, {"position": "top-right", "duration": 3000});
          return;
        }
        console.log(this.model);
        

        if(this.$route.params.id){
          axios.put("http://localhost:8000/api/edit-employee/"+this.$route.params.id, this.model,{
            headers: {
            Authorization: 'Token ' + localStorage.getItem('token')
            }
          })
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
            axios.post("http://localhost:8000/api/add-employee/", this.model,{
            headers: {
            Authorization: 'Token ' + localStorage.getItem('token')
            }
          })
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
    },
  },
};
</script>
<style></style>
