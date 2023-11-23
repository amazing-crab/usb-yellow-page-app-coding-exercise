<script setup lang="ts">
import ContactsTable from '../components/ContactsTable.vue'
import ContactsForm from '../components/ContactsForm.vue'
</script>

<template>
  <main>
    <ContactsTable :contactsData="contactsData" />
    <ContactsForm/>
  </main>
</template>
