<template>
  <div>
    <h2>Contact Form</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" v-model="formData.first_name" required>
      </div>
      <div>
        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" v-model="formData.last_name" required>
      </div>
      <div>
        <label for="phone_number">Phone Number:</label>
        <input type="text" id="phone_number" v-model="formData.phone_number" required>
      </div>
      <div>
        <label for="address">Address:</label>
        <input type="text" id="address" v-model="formData.address" required>
      </div>
      <div>
        <label for="comments">Comments:</label>
        <input type="text" id="comments" v-model="formData.comments" required>
      </div>
      <button type="submit">Submit</button>
    </form>

    <p v-if="successMessage">{{ successMessage }}</p>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>
 
<script>
export default {
  data() {
    return {
      formData: {
        first_name: '',
        last_name: '',
        phone_number: '',
        address: '',
        comments: ''
      },
      successMessage: '',
      errorMessage: ''
    };
  },

  methods: {
    async submitForm() {
      try {
        const response = await fetch('http://localhost:8000/api/contactsform/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.formData)
        });

        if (response.ok) {
          this.successMessage = 'Form submitted successfully!';
          this.formData = {first_name: '', last_name: '', phone_number: '', address: '', comments: ''}
        } else {
          this.errorMessage = 'Form submission failed.';
        }

      } catch (error) {
        this.errorMessage = 'Error submitting form.';
      }
    }
  }
};
</script>