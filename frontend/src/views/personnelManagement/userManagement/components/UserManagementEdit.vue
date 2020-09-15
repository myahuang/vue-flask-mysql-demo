<template>
  <el-dialog
    :title="title"
    :visible.sync="dialogFormVisible"
    width="500px"
    @close="close"
  >
    <el-form
      ref="form"
      :model="form"
      :rules="title === '添加' ? addRules : editRules"
      label-width="80px"
    >
      <el-form-item label="用户名" prop="username">
        <el-input
          v-model.trim="form.username"
          autocomplete="off"
          :disabled="title === '编辑'"
        ></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input
          v-model.trim="form.password"
          type="password"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input v-model.trim="form.email" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="权限" prop="permission">
        <!-- <el-checkbox-group v-model="form.permission">
          <el-checkbox label="superAdmin" v></el-checkbox>
          <el-checkbox label="admin"></el-checkbox>
          <el-checkbox label="guest"></el-checkbox>
          <el-checkbox label="user"></el-checkbox>
          <el-checkbox label="test"></el-checkbox>
        </el-checkbox-group> -->
        <el-radio v-model="form.permission" label="superAdmin"
          >超级管理员</el-radio
        >
        <el-radio v-model="form.permission" label="admin">管理员</el-radio>
        <!-- <el-radio v-model="form.permission" label="guest">游客</el-radio> -->
        <el-radio v-model="form.permission" label="user">普通用户</el-radio>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="close">取 消</el-button>
      <el-button type="primary" @click="save">确 定</el-button>
    </div>
  </el-dialog>
</template>

<script>
import { isPassword } from "@/utils/validate";
import { doEdit, doAdd } from "@/api/userManagement";
import { okCode, errorCode } from "@/config/settings";

export default {
  name: "UserManagementEdit",
  data() {
    const validateUserName = (rule, value, callback) => {
      if ("" == value) {
        callback(new Error("用户名不能为空"));
      } else {
        callback();
      }
    };
    const validatePassword = (rule, value, callback) => {
      if (!isPassword(value)) {
        callback(new Error("密码不能少于8位"));
      } else {
        callback();
      }
    };
    const validateEditPassword = (rule, value, callback) => {
      if (value && !isPassword(value)) {
        callback(new Error("密码不能少于8位"));
      } else {
        callback();
      }
    };
    const validateEmail = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请正确填写邮箱"));
      } else {
        if (value !== "") {
          var reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
          if (!reg.test(value)) {
            callback(new Error("请输入有效的邮箱"));
          }
        }
        callback();
      }
    };
    return {
      form: {
        username: "",
        password: "12345678",
        email: "",
        permission: "user",
      },
      addRules: {
        username: [
          { required: true, trigger: "blur", validator: validateUserName },
        ],
        password: [
          { required: true, trigger: "blur", validator: validatePassword },
        ],
        email: [{ required: true, trigger: "blur", validator: validateEmail }],
        permission: [
          { required: true, trigger: "blur", message: "请选择权限" },
        ],
      },
      editRules: {
        username: [
          { required: true, trigger: "blur", validator: validateUserName },
        ],
        password: [{ trigger: "blur", validator: validateEditPassword }],
        email: [{ required: true, trigger: "blur", validator: validateEmail }],
        permission: [
          { required: true, trigger: "blur", message: "请选择权限" },
        ],
      },
      title: "",
      dialogFormVisible: false,
    };
  },
  created() {},
  methods: {
    showEdit(row) {
      if (!row) {
        this.title = "添加";
      } else {
        this.title = "编辑";
        this.form = Object.assign({}, row);
      }
      this.dialogFormVisible = true;
    },
    close() {
      this.$refs["form"].resetFields();
      this.form = this.$options.data().form;
      this.dialogFormVisible = false;
    },
    save() {
      this.$refs["form"].validate((valid) => {
        if (valid) {
          if (this.title === "添加") {
            doAdd(this.form).then((res) => {
              const { code, msg, data } = res;
              if (code === okCode) {
                this.$baseMessage(res.msg || `添加用户信息成功！`, "success");
                this.$emit("fetchData");
                this.close();
              } else {
                this.$baseMessage(msg || `添加用户信息失败！`, "error");
              }
            });
          } else {
            doEdit(this.form).then((res) => {
              const { code, msg, data } = res;
              if (code === okCode) {
                this.$baseMessage(res.msg || `编辑用户信息成功！`, "success");
                this.$emit("fetchData");
                this.close();
              } else {
                this.$baseMessage(msg || `编辑用户信息失败！`, "error");
              }
            });
          }
        } else {
          return false;
        }
      });
    },
  },
};
</script>
