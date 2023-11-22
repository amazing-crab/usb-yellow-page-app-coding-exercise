<script setup lang="ts">
import ContactsTable from '../components/ContactsTable.vue'
</script>

<template>
  <main>
    <ContactsTable :contactsData="contactsData"/>
  </main>
</template>
