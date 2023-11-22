<template>
  <v-data-table :items="ContactsData"></v-data-table>
</template>

<script>
  export default {
    name: 'ContactsData',
    data(){
    return {
        contactsData: []
    }
},
async created(){
    var response = await fetch('http://localhost:8000/api/contacts/');
    this.contactsData = await response.json();
},}
</script>