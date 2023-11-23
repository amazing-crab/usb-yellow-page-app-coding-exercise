<template>
  <v-data-table :items="contactsData" :items-per-page="5" :headers="headers">
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Contacts</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ props }">
            <v-btn color="primary" dark class="mb-2" v-bind="props"> New Item </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.first_name" label="First Name"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.last_name" label="Last Name"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.phone_number"
                      label="Phone Number"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.address" label="Address"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="editedItem.comments" label="Comments"></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue-darken-1" variant="text" @click="close"> Cancel </v-btn>
              <v-btn color="blue-darken-1" variant="text" @click="save"> Save </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue-darken-1" variant="text" @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue-darken-1" variant="text" @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <div class="d-flex">
        <v-icon icon="mdi-pencil" @click="editItem(item)"></v-icon>
        <v-icon icon="mdi-delete" @click="deleteItem(item)"></v-icon>
      </div>
    </template>
  </v-data-table>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'ContactsData',
  data() {
    return {
      contactsData: [] as {
        first_name: string
        last_name: string
        phone_number: string
        address: string
        comments: string
      }[],
      dialog: false,
      dialogDelete: false,
      headers: [
        { title: 'First Name', key: 'first_name' },
        { title: 'Last Name', key: 'last_name' },
        { title: 'Phone number', key: 'phone_number' },
        { title: 'Address', key: 'address' },
        { title: 'Comments', key: 'comments' },
        { title: 'Actions', key: 'actions', sortable: false }
      ],
      editedIndex: -1,
      editedItem: {
        first_name: '',
        last_name: '',
        phone_number: '',
        address: '',
        comments: ''
      } as {
        first_name: string
        last_name: string
        phone_number: string
        address: string
        comments: string
      },
      defaultItem: {
        first_name: '',
        last_name: '',
        phone_number: '',
        address: '',
        comments: ''
      } as {
        first_name: string
        last_name: string
        phone_number: string
        address: string
        comments: string
      }
    }
  },
  async created() {
    var response = await fetch('http://localhost:8000/api/contacts/')
    this.contactsData = await response.json()
  },

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    }
  },

  watch: {
    dialog(val) {
      val || this.close()
    },
    dialogDelete(val) {
      val || this.closeDelete()
    }
  },

  methods: {
    editItem(item: any): void {
      this.editedIndex = this.contactsData.findIndex((contact: any) => contact === item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem(item: any) {
      this.editedIndex = this.contactsData.findIndex((contact: any) => contact === item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm() {
      this.contactsData.splice(this.editedIndex, 1)
      this.closeDelete()
    },

    close() {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    closeDelete() {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    async save() {
      try {
        const response = await fetch('http://localhost:8000/api/contactsform/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.editedItem)
        })

        if (response.ok) {
          this.close()
        } else {
          console.error('Error:', response)
        }
      } catch (error) {
        console.error('Error:', error)
      }
    }
  }
})
</script>
