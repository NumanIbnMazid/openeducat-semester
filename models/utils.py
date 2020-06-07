def create_or_update_course(self, values, record):
    course_id_values = values.get('course_id')
    course_id_self = self.course_id.id
    id_self = self.id
    # course_id = None
    # semester_id = None
    if not course_id_values == None:
        course_id = course_id_values
    else:
        course_id = course_id_self
    if not id_self == False:
        semester_id = id_self
    else:
        semester_id = record.id
    course = self.env['op.course'].search([('id', '=', course_id)])
    if course:
        # Subject Create or Update
        self.env.cr.execute(
            "SELECT ocr.op_subject_id FROM op_course_op_subject_rel AS ocr WHERE ocr.op_course_id= %d" % (
                course_id)
        )
        subject_result = self.env.cr.fetchall()
        course_sub_ids = []
        for i, (course_sub_id) in enumerate(subject_result):
            course_sub_ids.append(course_sub_id[0])
        if not values.get('subject_ids') == None:
            subject_ids_val = values.get('subject_ids')[0][2]
            for sub_id in subject_ids_val:
                course_sub_ids.append(sub_id)
            course_sub_ids = list(set(course_sub_ids))
            course['subject_ids'] = course_sub_ids
        # Semester Create or Update
        self.env.cr.execute(
            "SELECT os.id FROM op_semester AS os WHERE os.course_id= %d" % (
                course_id)
        )
        semester_result = self.env.cr.fetchall()
        course_semester_ids = []
        for i, (course_sem_id) in enumerate(semester_result):
            course_semester_ids.append(course_sem_id[0])
        course_semester_ids.append(semester_id)
        course_semester_ids = list(set(course_semester_ids))
        course['semester_ids'] = course_semester_ids
