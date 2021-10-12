
--
-- Create model Doctor
--
CREATE TABLE `doctors_doctor` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `praticing_from` date NOT NULL, `professional_statement` longtext NOT NULL, `sex` varchar(10) NOT NULL, `photo` varchar(100) NOT NULL, `phone` varchar(20) NOT NULL, `created` datetime(6) NOT NULL);
--
-- Create model HospitalAffiliation
--
CREATE TABLE `doctors_hospitalaffiliation` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `hospital_name` varchar(100) NOT NULL, `city` varchar(50) NOT NULL, `country` varchar(50) NOT NULL, `start_date` date NOT NULL, `end_date` date NOT NULL, `doctor_id` bigint NOT NULL);
--
-- Create model Office
--
CREATE TABLE `doctors_office` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `time_slot_per_client_in_min` integer NOT NULL, `first_consultation_fee` integer NOT NULL, `followup_consultation_fee` integer NOT NULL, `street_address` varchar(500) NOT NULL, `city` varchar(100) NOT NULL, `state` varchar(100) NOT NULL, `country` varchar(100) NOT NULL, `zip` varchar(50) NOT NULL, `doctor_id` bigint NOT NULL, `hospital_id` bigint NOT NULL);
--
-- Create model Specialization
--
CREATE TABLE `doctors_specialization` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `specialization_name` varchar(100) NOT NULL);
--
-- Create model Qualification
--
CREATE TABLE `doctors_qualification` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `qualification_name` varchar(200) NOT NULL, `institute_name` varchar(200) NOT NULL, `procurement_year` date NOT NULL, `doctor_id` bigint NOT NULL);
--
-- Create model OfficeDoctorAvailabiliy
--
CREATE TABLE `doctors_officedoctoravailabiliy` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `day_of_week` varchar(10) NOT NULL, `start_time` datetime(6) NOT NULL, `end_time` datetime(6) NOT NULL, `is_available` bool NOT NULL, `reason_of_unavailabiliy` longtext NOT NULL, `office_id` bigint NOT NULL);
--
-- Create model NetworkInsurance
--
CREATE TABLE `doctors_networkinsurance` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `insurance_name` varchar(200) NOT NULL, `office_id` bigint NOT NULL);
--
-- Add field specializations to doctor
--
CREATE TABLE `doctors_doctor_specializations` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `doctor_id` bigint NOT NULL, `specialization_id` bigint NOT NULL);
--
-- Add field user to doctor
--
ALTER TABLE `doctors_doctor` ADD COLUMN `user_id` integer NOT NULL UNIQUE , ADD CONSTRAINT `doctors_doctor_user_id_c371de6c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user`(`id`);
ALTER TABLE `doctors_hospitalaffiliation` ADD CONSTRAINT `doctors_hospitalaffi_doctor_id_f3e00b14_fk_doctors_d` FOREIGN KEY (`doctor_id`) REFERENCES `doctors_doctor` (`id`);
ALTER TABLE `doctors_office` ADD CONSTRAINT `doctors_office_doctor_id_a1b6c3e1_fk_doctors_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `doctors_doctor` (`id`);
ALTER TABLE `doctors_office` ADD CONSTRAINT `doctors_office_hospital_id_8db653c2_fk_doctors_h` FOREIGN KEY (`hospital_id`) REFERENCES `doctors_hospitalaffiliation` (`id`);
ALTER TABLE `doctors_qualification` ADD CONSTRAINT `doctors_qualification_doctor_id_da273d58_fk_doctors_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `doctors_doctor` (`id`);
ALTER TABLE `doctors_officedoctoravailabiliy` ADD CONSTRAINT `doctors_officedoctor_office_id_a5ecaa95_fk_doctors_o` FOREIGN KEY (`office_id`) REFERENCES `doctors_office` (`id`);
ALTER TABLE `doctors_networkinsurance` ADD CONSTRAINT `doctors_networkinsurance_office_id_2b30317a_fk_doctors_office_id` FOREIGN KEY (`office_id`) REFERENCES `doctors_office` (`id`);
ALTER TABLE `doctors_doctor_specializations` ADD CONSTRAINT `doctors_doctor_specializ_doctor_id_specialization_86617eed_uniq` UNIQUE (`doctor_id`, `specialization_id`);
ALTER TABLE `doctors_doctor_specializations` ADD CONSTRAINT `doctors_doctor_speci_doctor_id_f5fc5de3_fk_doctors_d` FOREIGN KEY (`doctor_id`) REFERENCES `doctors_doctor` (`id`);
ALTER TABLE `doctors_doctor_specializations` ADD CONSTRAINT `doctors_doctor_speci_specialization_id_788722a6_fk_doctors_s` FOREIGN KEY (`specialization_id`) REFERENCES `doctors_specialization` (`id`);

--
-- Create model Patient
--
CREATE TABLE `patients_patient` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `first_name` varchar(50) NOT NULL, `last_name` varchar(50) NOT NULL, `phone` varchar(50) NOT NULL, `email` varchar(150) NOT NULL, `photo` varchar(100) NOT NULL);
--
-- Create model ClientReview
--
CREATE TABLE `patients_clientreview` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `is_review_anonymous` bool NOT NULL, `wait_time_rating` integer NOT NULL, `bedside_manner_rating` integer NOT NULL, `overall_rating` integer NOT NULL, `review` longtext NOT NULL, `is_doctor_recommended` bool NOT NULL, `review_date` datetime(6) NOT NULL, `doctor_id` bigint NOT NULL, `patient_id` bigint NOT NULL);
ALTER TABLE `patients_clientreview` ADD CONSTRAINT `patients_clientreview_doctor_id_ea8411aa_fk_doctors_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `doctors_doctor` (`id`);
ALTER TABLE `patients_clientreview` ADD CONSTRAINT `patients_clientreview_patient_id_52f26823_fk_patients_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `patients_patient` (`id`);

--
-- Create model AppBookingChannel
--
CREATE TABLE `pages_appbookingchannel` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `app_booking_channel_name` varchar(50) NOT NULL);
--
-- Create model AppointStatus
--
CREATE TABLE `pages_appointstatus` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `status` varchar(10) NOT NULL);
--
-- Create model Appointment
--
CREATE TABLE `pages_appointment` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `probable_start_time` datetime(6) NOT NULL, `actual_end_time` datetime(6) NOT NULL, `appointment_taken_date` date NOT NULL, `channel_name_id` bigint NOT NULL, `office_id` bigint NOT NULL, `patient_id` bigint NOT NULL, `status_id` bigint NOT NULL);
ALTER TABLE `pages_appointment` ADD CONSTRAINT `pages_appointment_channel_name_id_0b2165e1_fk_pages_app` FOREIGN KEY (`channel_name_id`) REFERENCES `pages_appbookingchannel` (`id`);
ALTER TABLE `pages_appointment` ADD CONSTRAINT `pages_appointment_office_id_6bf65efc_fk_doctors_office_id` FOREIGN KEY (`office_id`) REFERENCES `doctors_office` (`id`);
ALTER TABLE `pages_appointment` ADD CONSTRAINT `pages_appointment_patient_id_ceb940c7_fk_patients_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `patients_patient` (`id`);
ALTER TABLE `pages_appointment` ADD CONSTRAINT `pages_appointment_status_id_3cb6cd07_fk_pages_appointstatus_id` FOREIGN KEY (`status_id`) REFERENCES `pages_appointstatus` (`id`);