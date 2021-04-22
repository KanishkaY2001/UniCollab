import createPersistedState from 'vuex-persistedstate'

export const plugins = [createPersistedState()]

export const state = () =>({
  userId: 0,
  user: "",
  defPhoto: "/img/spaceman.png",
  currentGroup: 0,
})

export const mutations = {
  SAVE_USER(state, info) {
    if (!info) return;
    state.user = info;
    state.userId = info.id;
    console.log(state.user.name)
  },
  SAVE_GROUP(state, id) {
    if(!id) return
    state.currentGroup = id
  }
}

export const getters = {
  userId(state) {
    return state.userId
  },
  groupId(state) {
    return state.currentGroup
  }
}