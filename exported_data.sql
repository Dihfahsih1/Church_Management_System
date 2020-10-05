--
-- PostgreSQL database dump
--

-- Dumped from database version 11.8
-- Dumped by pg_dump version 11.8

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: background_task; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.background_task (
    id integer NOT NULL,
    task_name character varying(190) NOT NULL,
    task_params text NOT NULL,
    task_hash character varying(40) NOT NULL,
    verbose_name character varying(255),
    priority integer NOT NULL,
    run_at timestamp with time zone NOT NULL,
    repeat bigint NOT NULL,
    repeat_until timestamp with time zone,
    queue character varying(190),
    attempts integer NOT NULL,
    failed_at timestamp with time zone,
    last_error text NOT NULL,
    locked_by character varying(64),
    locked_at timestamp with time zone,
    creator_object_id integer,
    creator_content_type_id integer,
    CONSTRAINT background_task_creator_object_id_check CHECK ((creator_object_id >= 0))
);


ALTER TABLE public.background_task OWNER TO postgres;

--
-- Name: background_task_completedtask; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.background_task_completedtask (
    id integer NOT NULL,
    task_name character varying(190) NOT NULL,
    task_params text NOT NULL,
    task_hash character varying(40) NOT NULL,
    verbose_name character varying(255),
    priority integer NOT NULL,
    run_at timestamp with time zone NOT NULL,
    repeat bigint NOT NULL,
    repeat_until timestamp with time zone,
    queue character varying(190),
    attempts integer NOT NULL,
    failed_at timestamp with time zone,
    last_error text NOT NULL,
    locked_by character varying(64),
    locked_at timestamp with time zone,
    creator_object_id integer,
    creator_content_type_id integer,
    CONSTRAINT background_task_completedtask_creator_object_id_check CHECK ((creator_object_id >= 0))
);


ALTER TABLE public.background_task_completedtask OWNER TO postgres;

--
-- Name: background_task_completedtask_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.background_task_completedtask_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.background_task_completedtask_id_seq OWNER TO postgres;

--
-- Name: background_task_completedtask_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.background_task_completedtask_id_seq OWNED BY public.background_task_completedtask.id;


--
-- Name: background_task_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.background_task_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.background_task_id_seq OWNER TO postgres;

--
-- Name: background_task_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.background_task_id_seq OWNED BY public.background_task.id;


--
-- Name: corsheaders_corsmodel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.corsheaders_corsmodel (
    id integer NOT NULL,
    cors character varying(255) NOT NULL
);


ALTER TABLE public.corsheaders_corsmodel OWNER TO postgres;

--
-- Name: corsheaders_corsmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.corsheaders_corsmodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.corsheaders_corsmodel_id_seq OWNER TO postgres;

--
-- Name: corsheaders_corsmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.corsheaders_corsmodel_id_seq OWNED BY public.corsheaders_corsmodel.id;


--
-- Name: dashboard_about; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_about (
    id integer NOT NULL,
    about_image character varying(10000),
    about text,
    mission_description text,
    "Is_View_on_Web" character varying(20),
    vision_description text,
    about_title character varying(100),
    core_values text,
    church_details text
);


ALTER TABLE public.dashboard_about OWNER TO postgres;

--
-- Name: dashboard_about_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_about_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_about_id_seq OWNER TO postgres;

--
-- Name: dashboard_about_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_about_id_seq OWNED BY public.dashboard_about.id;


--
-- Name: dashboard_annualconference; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_annualconference (
    id integer NOT NULL,
    start_date date,
    end_date date,
    estimated_budget integer,
    conference_theme character varying(500),
    conference_report text
);


ALTER TABLE public.dashboard_annualconference OWNER TO postgres;

--
-- Name: dashboard_annualconference_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_annualconference_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_annualconference_id_seq OWNER TO postgres;

--
-- Name: dashboard_annualconference_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_annualconference_id_seq OWNED BY public.dashboard_annualconference.id;


--
-- Name: dashboard_cashfloat; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_cashfloat (
    id integer NOT NULL,
    "Date" date,
    "Amount" integer NOT NULL,
    "Notes" text
);


ALTER TABLE public.dashboard_cashfloat OWNER TO postgres;

--
-- Name: dashboard_cashfloat_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_cashfloat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_cashfloat_id_seq OWNER TO postgres;

--
-- Name: dashboard_cashfloat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_cashfloat_id_seq OWNED BY public.dashboard_cashfloat.id;


--
-- Name: dashboard_church; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_church (
    id integer NOT NULL,
    church_code character varying(130),
    church_name character varying(130) NOT NULL,
    address character varying(130) NOT NULL,
    phone character varying(130) NOT NULL,
    registration_date date,
    email_address character varying(120) NOT NULL,
    "Post_Office_Box" character varying(130),
    footer character varying(130),
    enable_frontend character varying(130) NOT NULL,
    latitude character varying(130),
    longitude character varying(130),
    facebook_url character varying(130),
    twitter_url character varying(130),
    "linkedIn_url" character varying(130),
    google_plus_url character varying(130),
    youtube_url character varying(130),
    instagram_url character varying(130),
    pinterest_url character varying(130),
    "Church_Logo" character varying(10000) NOT NULL,
    status character varying(130),
    maps_embedded_link character varying(1000),
    church_mission character varying(1000) NOT NULL,
    church_vision character varying(1000) NOT NULL
);


ALTER TABLE public.dashboard_church OWNER TO postgres;

--
-- Name: dashboard_church_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_church_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_church_id_seq OWNER TO postgres;

--
-- Name: dashboard_church_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_church_id_seq OWNED BY public.dashboard_church.id;


--
-- Name: dashboard_contact; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_contact (
    id integer NOT NULL,
    name character varying(1000),
    email character varying(130),
    phone character varying(130),
    subject character varying(130),
    message text,
    feedback text
);


ALTER TABLE public.dashboard_contact OWNER TO postgres;

--
-- Name: dashboard_contact_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_contact_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_contact_id_seq OWNER TO postgres;

--
-- Name: dashboard_contact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_contact_id_seq OWNED BY public.dashboard_contact.id;


--
-- Name: dashboard_event; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_event (
    id integer NOT NULL,
    event_title character varying(100),
    event_for character varying(20),
    event_place character varying(100) NOT NULL,
    from_date date,
    to_date date,
    image character varying(10000),
    note text NOT NULL,
    "Is_View_on_Web" character varying(20) NOT NULL,
    date date NOT NULL,
    "Activity_Type" character varying(20) NOT NULL,
    "Day" character varying(20),
    "End_Time" time without time zone,
    "Program_Name" character varying(100),
    "Start_Time" time without time zone
);


ALTER TABLE public.dashboard_event OWNER TO postgres;

--
-- Name: dashboard_event_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_event_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_event_id_seq OWNER TO postgres;

--
-- Name: dashboard_event_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_event_id_seq OWNED BY public.dashboard_event.id;


--
-- Name: dashboard_expenditures; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_expenditures (
    id integer NOT NULL,
    "Date" date,
    "Payment_Made_To" character varying(1000),
    "Amount" integer NOT NULL,
    "Reason_filtering" character varying(1000),
    "Other_Expenditure" character varying(1000),
    "Notes" character varying(1000),
    "Main_Expense_Reason" character varying(1000),
    "General_Expenses_Reason" character varying(1000),
    "Petty_Cash_Reason" character varying(1000),
    "Archived_Status" character varying(1000),
    "Member_Name_id" integer
);


ALTER TABLE public.dashboard_expenditures OWNER TO postgres;

--
-- Name: dashboard_expenditures_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_expenditures_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_expenditures_id_seq OWNER TO postgres;

--
-- Name: dashboard_expenditures_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_expenditures_id_seq OWNED BY public.dashboard_expenditures.id;


--
-- Name: dashboard_gallery; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_gallery (
    id integer NOT NULL,
    gallery_title character varying(100) NOT NULL,
    note text NOT NULL,
    "Is_View_on_Web" character varying(20) NOT NULL,
    date date NOT NULL
);


ALTER TABLE public.dashboard_gallery OWNER TO postgres;

--
-- Name: dashboard_gallery_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_gallery_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_gallery_id_seq OWNER TO postgres;

--
-- Name: dashboard_gallery_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_gallery_id_seq OWNED BY public.dashboard_gallery.id;


--
-- Name: dashboard_image; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_image (
    id integer NOT NULL,
    gallery_image character varying(10000),
    image_caption text NOT NULL,
    gallery_title_id integer,
    "Is_View_on_Web" character varying(20),
    date date NOT NULL
);


ALTER TABLE public.dashboard_image OWNER TO postgres;

--
-- Name: dashboard_image_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_image_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_image_id_seq OWNER TO postgres;

--
-- Name: dashboard_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_image_id_seq OWNED BY public.dashboard_image.id;


--
-- Name: dashboard_members; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_members (
    id integer NOT NULL,
    "First_Name" character varying(100),
    "Second_Name" character varying(100),
    "Home_Cell" character varying(100),
    "Residence" character varying(100),
    "Telephone" character varying(100),
    "Email" character varying(254) NOT NULL,
    "Photo" character varying(10000) NOT NULL,
    "Gender" character varying(100),
    "Marital_Status" character varying(100),
    "Marriage_Kind" character varying(100),
    "Education_Level" character varying(100),
    "Profession" character varying(100),
    "Type_of_Work" character varying(100),
    "Place_of_Work" character varying(100),
    "Country" character varying(100),
    "County" character varying(100),
    "Parish" character varying(100),
    "District" character varying(100),
    "Sub_County" character varying(100),
    "Village" character varying(100),
    "Date_Of_Salvation" date,
    "Date_Of_Birth" date,
    "Date_Of_Joining_UCC_Bwaise" date,
    "Ministry_Involved_In" character varying(100),
    "Name_Of_Next_Of_Kin" character varying(100),
    "Contact_Of_Next_Of_Kin" character varying(100),
    "Residence_Of_Next_Of_Kin" character varying(100),
    "Initials" character varying(100),
    "Is_View_on_Web" character varying(20),
    "Group" character varying(100),
    "More_Info" text,
    date timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    "Archived_Status" character varying(1000),
    "Full_Named" character varying(100)
);


ALTER TABLE public.dashboard_members OWNER TO postgres;

--
-- Name: dashboard_members_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_members_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_members_id_seq OWNER TO postgres;

--
-- Name: dashboard_members_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_members_id_seq OWNED BY public.dashboard_members.id;


--
-- Name: dashboard_ministry; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_ministry (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    details text,
    photos character varying(10000) NOT NULL,
    leader_id integer NOT NULL,
    "Is_View_on_Web" character varying(20)
);


ALTER TABLE public.dashboard_ministry OWNER TO postgres;

--
-- Name: dashboard_ministry_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_ministry_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_ministry_id_seq OWNER TO postgres;

--
-- Name: dashboard_ministry_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_ministry_id_seq OWNED BY public.dashboard_ministry.id;


--
-- Name: dashboard_newconvert; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_newconvert (
    id integer NOT NULL,
    is_church_member character varying(100),
    born_again_before character varying(100),
    "First_Name" character varying(100),
    "Second_Name" character varying(100),
    "Telephone" character varying(100),
    "Date_Of_Salvation" date,
    member_name_id integer
);


ALTER TABLE public.dashboard_newconvert OWNER TO postgres;

--
-- Name: dashboard_newconvert_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_newconvert_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_newconvert_id_seq OWNER TO postgres;

--
-- Name: dashboard_newconvert_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_newconvert_id_seq OWNED BY public.dashboard_newconvert.id;


--
-- Name: dashboard_news; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_news (
    id integer NOT NULL,
    news_title character varying(100) NOT NULL,
    date date NOT NULL,
    image character varying(10000),
    news text,
    "Is_View_on_Web" character varying(20) NOT NULL,
    author character varying(1003),
    audio_file character varying(10000)
);


ALTER TABLE public.dashboard_news OWNER TO postgres;

--
-- Name: dashboard_news_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_news_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_news_id_seq OWNER TO postgres;

--
-- Name: dashboard_news_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_news_id_seq OWNED BY public.dashboard_news.id;


--
-- Name: dashboard_page; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_page (
    id integer NOT NULL,
    page_location character varying(100) NOT NULL,
    page_title character varying(100) NOT NULL,
    page_description text NOT NULL,
    page_image character varying(10000)
);


ALTER TABLE public.dashboard_page OWNER TO postgres;

--
-- Name: dashboard_page_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_page_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_page_id_seq OWNER TO postgres;

--
-- Name: dashboard_page_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_page_id_seq OWNED BY public.dashboard_page.id;


--
-- Name: dashboard_pledgeitem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_pledgeitem (
    id integer NOT NULL,
    "Date" date,
    "Item_That_Needs_Pledges" character varying(100) NOT NULL,
    "Amount_Needed" integer,
    "Pledge_Deadline" date,
    "Archived_Status" character varying(100)
);


ALTER TABLE public.dashboard_pledgeitem OWNER TO postgres;

--
-- Name: dashboard_pledgeitem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_pledgeitem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_pledgeitem_id_seq OWNER TO postgres;

--
-- Name: dashboard_pledgeitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_pledgeitem_id_seq OWNED BY public.dashboard_pledgeitem.id;


--
-- Name: dashboard_pledges; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_pledges (
    id integer NOT NULL,
    "Status" character varying(100),
    "Date" date,
    "Amount_Pledged" integer,
    "Amount_Paid" integer,
    "Balance" integer,
    "Pledge_Made_By_id" integer,
    "Reason_id" integer,
    "Archived_Status" character varying(100),
    "PledgeItem" character varying(100),
    "Pledge_Made_By_Visitor_id" integer,
    is_church_member character varying(100),
    "AmountBeingPaid" integer,
    "DateOfPayment" date,
    "NameOfPledgee" character varying(100)
);


ALTER TABLE public.dashboard_pledges OWNER TO postgres;

--
-- Name: dashboard_pledges_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_pledges_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_pledges_id_seq OWNER TO postgres;

--
-- Name: dashboard_pledges_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_pledges_id_seq OWNED BY public.dashboard_pledges.id;


--
-- Name: dashboard_pledgescashedout; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_pledgescashedout (
    id integer NOT NULL,
    "Date" date,
    "Item_Id" character varying(100),
    "Amount_Needed" integer,
    "Amount_Cashed_Out" integer,
    "Item_That_Needs_Pledges" character varying(100)
);


ALTER TABLE public.dashboard_pledgescashedout OWNER TO postgres;

--
-- Name: dashboard_pledgescashedout_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_pledgescashedout_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_pledgescashedout_id_seq OWNER TO postgres;

--
-- Name: dashboard_pledgescashedout_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_pledgescashedout_id_seq OWNED BY public.dashboard_pledgescashedout.id;


--
-- Name: dashboard_project; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_project (
    id integer NOT NULL,
    project_title character varying(100) NOT NULL,
    start_date date,
    image character varying(10000),
    project_description text NOT NULL,
    "Is_View_on_Web" character varying(20) NOT NULL,
    project_leader_id integer
);


ALTER TABLE public.dashboard_project OWNER TO postgres;

--
-- Name: dashboard_project_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_project_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_project_id_seq OWNER TO postgres;

--
-- Name: dashboard_project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_project_id_seq OWNED BY public.dashboard_project.id;


--
-- Name: dashboard_revenues; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_revenues (
    id integer NOT NULL,
    "Date" date,
    "Service" character varying(100),
    "Amount" integer NOT NULL,
    "Archived_Status" character varying(100),
    "Revenue_filter" character varying(100),
    "Member_Name_id" integer,
    "Other_Sources" character varying(100),
    "Other_Notes" character varying(10000)
);


ALTER TABLE public.dashboard_revenues OWNER TO postgres;

--
-- Name: dashboard_revenues_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_revenues_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_revenues_id_seq OWNER TO postgres;

--
-- Name: dashboard_revenues_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_revenues_id_seq OWNED BY public.dashboard_revenues.id;


--
-- Name: dashboard_salariespaid; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_salariespaid (
    id integer NOT NULL,
    "Salary_Id" character varying(200),
    "Name" character varying(200),
    "Salary_Amount" integer NOT NULL,
    "Month_being_cleared" date,
    "Date_of_paying_salary" date,
    "Archived_Status" character varying(1000)
);


ALTER TABLE public.dashboard_salariespaid OWNER TO postgres;

--
-- Name: dashboard_salariespaid_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_salariespaid_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_salariespaid_id_seq OWNER TO postgres;

--
-- Name: dashboard_salariespaid_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_salariespaid_id_seq OWNED BY public.dashboard_salariespaid.id;


--
-- Name: dashboard_slider; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_slider (
    id integer NOT NULL,
    slider_image character varying(10000),
    image_title character varying(100) NOT NULL,
    modified timestamp with time zone NOT NULL
);


ALTER TABLE public.dashboard_slider OWNER TO postgres;

--
-- Name: dashboard_slider_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_slider_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_slider_id_seq OWNER TO postgres;

--
-- Name: dashboard_slider_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_slider_id_seq OWNED BY public.dashboard_slider.id;


--
-- Name: dashboard_staffdetails; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_staffdetails (
    id integer NOT NULL,
    "UCC_Bwaise_Member" character varying(100),
    "First_Name" character varying(100),
    "Second_Name" character varying(100),
    "Gender" character varying(100),
    "Date_Of_Birth" date,
    "Education_Level" character varying(100),
    "Residence" character varying(100),
    "Telephone" character varying(100),
    "Photo" character varying(10000),
    "Faith" character varying(100),
    "Date_of_paying_salary" date,
    "Month_being_cleared" date,
    "Salary_Amount" integer NOT NULL,
    "Role" character varying(200),
    "Date_of_employment" date,
    "End_of_contract" date,
    "Church_Member_id" integer,
    "Is_View_on_Web" character varying(20)
);


ALTER TABLE public.dashboard_staffdetails OWNER TO postgres;

--
-- Name: dashboard_staffdetails_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_staffdetails_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_staffdetails_id_seq OWNER TO postgres;

--
-- Name: dashboard_staffdetails_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_staffdetails_id_seq OWNED BY public.dashboard_staffdetails.id;


--
-- Name: dashboard_testing; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_testing (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    slug character varying(50) NOT NULL
);


ALTER TABLE public.dashboard_testing OWNER TO postgres;

--
-- Name: dashboard_testing_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_testing_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_testing_id_seq OWNER TO postgres;

--
-- Name: dashboard_testing_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_testing_id_seq OWNED BY public.dashboard_testing.id;


--
-- Name: dashboard_theme; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_theme (
    id integer NOT NULL,
    name character varying(40),
    colour character varying(40) NOT NULL,
    is_active character varying(10) NOT NULL
);


ALTER TABLE public.dashboard_theme OWNER TO postgres;

--
-- Name: dashboard_theme_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_theme_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_theme_id_seq OWNER TO postgres;

--
-- Name: dashboard_theme_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_theme_id_seq OWNED BY public.dashboard_theme.id;


--
-- Name: dashboard_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    email character varying(255),
    username character varying(30) NOT NULL,
    "Role" character varying(250),
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    is_superuser boolean NOT NULL,
    full_name_id integer,
    "Is_View_on_Web" character varying(20)
);


ALTER TABLE public.dashboard_user OWNER TO postgres;

--
-- Name: dashboard_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.dashboard_user_groups OWNER TO postgres;

--
-- Name: dashboard_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_user_groups_id_seq OWNER TO postgres;

--
-- Name: dashboard_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_user_groups_id_seq OWNED BY public.dashboard_user_groups.id;


--
-- Name: dashboard_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_user_id_seq OWNER TO postgres;

--
-- Name: dashboard_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_user_id_seq OWNED BY public.dashboard_user.id;


--
-- Name: dashboard_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.dashboard_user_user_permissions OWNER TO postgres;

--
-- Name: dashboard_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: dashboard_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_user_user_permissions_id_seq OWNED BY public.dashboard_user_user_permissions.id;


--
-- Name: dashboard_visitors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dashboard_visitors (
    id integer NOT NULL,
    "Photo" character varying(10000) NOT NULL,
    "First_Name" character varying(100),
    "Second_Name" character varying(100),
    "Address" character varying(100),
    "Telephone" character varying(100),
    "Church" character varying(100),
    "Date" date
);


ALTER TABLE public.dashboard_visitors OWNER TO postgres;

--
-- Name: dashboard_visitors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dashboard_visitors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_visitors_id_seq OWNER TO postgres;

--
-- Name: dashboard_visitors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dashboard_visitors_id_seq OWNED BY public.dashboard_visitors.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: oauth2_provider_accesstoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oauth2_provider_accesstoken (
    id bigint NOT NULL,
    token character varying(255) NOT NULL,
    expires timestamp with time zone NOT NULL,
    scope text NOT NULL,
    application_id bigint,
    user_id integer,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    source_refresh_token_id bigint
);


ALTER TABLE public.oauth2_provider_accesstoken OWNER TO postgres;

--
-- Name: oauth2_provider_accesstoken_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.oauth2_provider_accesstoken_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oauth2_provider_accesstoken_id_seq OWNER TO postgres;

--
-- Name: oauth2_provider_accesstoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.oauth2_provider_accesstoken_id_seq OWNED BY public.oauth2_provider_accesstoken.id;


--
-- Name: oauth2_provider_application; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oauth2_provider_application (
    id bigint NOT NULL,
    client_id character varying(100) NOT NULL,
    redirect_uris text NOT NULL,
    client_type character varying(32) NOT NULL,
    authorization_grant_type character varying(32) NOT NULL,
    client_secret character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    user_id integer,
    skip_authorization boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL
);


ALTER TABLE public.oauth2_provider_application OWNER TO postgres;

--
-- Name: oauth2_provider_application_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.oauth2_provider_application_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oauth2_provider_application_id_seq OWNER TO postgres;

--
-- Name: oauth2_provider_application_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.oauth2_provider_application_id_seq OWNED BY public.oauth2_provider_application.id;


--
-- Name: oauth2_provider_grant; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oauth2_provider_grant (
    id bigint NOT NULL,
    code character varying(255) NOT NULL,
    expires timestamp with time zone NOT NULL,
    redirect_uri character varying(255) NOT NULL,
    scope text NOT NULL,
    application_id bigint NOT NULL,
    user_id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    code_challenge character varying(128) NOT NULL,
    code_challenge_method character varying(10) NOT NULL
);


ALTER TABLE public.oauth2_provider_grant OWNER TO postgres;

--
-- Name: oauth2_provider_grant_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.oauth2_provider_grant_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oauth2_provider_grant_id_seq OWNER TO postgres;

--
-- Name: oauth2_provider_grant_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.oauth2_provider_grant_id_seq OWNED BY public.oauth2_provider_grant.id;


--
-- Name: oauth2_provider_refreshtoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.oauth2_provider_refreshtoken (
    id bigint NOT NULL,
    token character varying(255) NOT NULL,
    access_token_id bigint,
    application_id bigint NOT NULL,
    user_id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    revoked timestamp with time zone
);


ALTER TABLE public.oauth2_provider_refreshtoken OWNER TO postgres;

--
-- Name: oauth2_provider_refreshtoken_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.oauth2_provider_refreshtoken_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.oauth2_provider_refreshtoken_id_seq OWNER TO postgres;

--
-- Name: oauth2_provider_refreshtoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.oauth2_provider_refreshtoken_id_seq OWNED BY public.oauth2_provider_refreshtoken.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: background_task id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.background_task ALTER COLUMN id SET DEFAULT nextval('public.background_task_id_seq'::regclass);


--
-- Name: background_task_completedtask id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.background_task_completedtask ALTER COLUMN id SET DEFAULT nextval('public.background_task_completedtask_id_seq'::regclass);


--
-- Name: corsheaders_corsmodel id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.corsheaders_corsmodel ALTER COLUMN id SET DEFAULT nextval('public.corsheaders_corsmodel_id_seq'::regclass);


--
-- Name: dashboard_about id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_about ALTER COLUMN id SET DEFAULT nextval('public.dashboard_about_id_seq'::regclass);


--
-- Name: dashboard_annualconference id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_annualconference ALTER COLUMN id SET DEFAULT nextval('public.dashboard_annualconference_id_seq'::regclass);


--
-- Name: dashboard_cashfloat id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_cashfloat ALTER COLUMN id SET DEFAULT nextval('public.dashboard_cashfloat_id_seq'::regclass);


--
-- Name: dashboard_church id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_church ALTER COLUMN id SET DEFAULT nextval('public.dashboard_church_id_seq'::regclass);


--
-- Name: dashboard_contact id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_contact ALTER COLUMN id SET DEFAULT nextval('public.dashboard_contact_id_seq'::regclass);


--
-- Name: dashboard_event id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_event ALTER COLUMN id SET DEFAULT nextval('public.dashboard_event_id_seq'::regclass);


--
-- Name: dashboard_expenditures id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_expenditures ALTER COLUMN id SET DEFAULT nextval('public.dashboard_expenditures_id_seq'::regclass);


--
-- Name: dashboard_gallery id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_gallery ALTER COLUMN id SET DEFAULT nextval('public.dashboard_gallery_id_seq'::regclass);


--
-- Name: dashboard_image id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_image ALTER COLUMN id SET DEFAULT nextval('public.dashboard_image_id_seq'::regclass);


--
-- Name: dashboard_members id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_members ALTER COLUMN id SET DEFAULT nextval('public.dashboard_members_id_seq'::regclass);


--
-- Name: dashboard_ministry id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_ministry ALTER COLUMN id SET DEFAULT nextval('public.dashboard_ministry_id_seq'::regclass);


--
-- Name: dashboard_newconvert id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_newconvert ALTER COLUMN id SET DEFAULT nextval('public.dashboard_newconvert_id_seq'::regclass);


--
-- Name: dashboard_news id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_news ALTER COLUMN id SET DEFAULT nextval('public.dashboard_news_id_seq'::regclass);


--
-- Name: dashboard_page id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_page ALTER COLUMN id SET DEFAULT nextval('public.dashboard_page_id_seq'::regclass);


--
-- Name: dashboard_pledgeitem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_pledgeitem ALTER COLUMN id SET DEFAULT nextval('public.dashboard_pledgeitem_id_seq'::regclass);


--
-- Name: dashboard_pledges id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_pledges ALTER COLUMN id SET DEFAULT nextval('public.dashboard_pledges_id_seq'::regclass);


--
-- Name: dashboard_pledgescashedout id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_pledgescashedout ALTER COLUMN id SET DEFAULT nextval('public.dashboard_pledgescashedout_id_seq'::regclass);


--
-- Name: dashboard_project id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_project ALTER COLUMN id SET DEFAULT nextval('public.dashboard_project_id_seq'::regclass);


--
-- Name: dashboard_revenues id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_revenues ALTER COLUMN id SET DEFAULT nextval('public.dashboard_revenues_id_seq'::regclass);


--
-- Name: dashboard_salariespaid id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_salariespaid ALTER COLUMN id SET DEFAULT nextval('public.dashboard_salariespaid_id_seq'::regclass);


--
-- Name: dashboard_slider id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_slider ALTER COLUMN id SET DEFAULT nextval('public.dashboard_slider_id_seq'::regclass);


--
-- Name: dashboard_staffdetails id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_staffdetails ALTER COLUMN id SET DEFAULT nextval('public.dashboard_staffdetails_id_seq'::regclass);


--
-- Name: dashboard_testing id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_testing ALTER COLUMN id SET DEFAULT nextval('public.dashboard_testing_id_seq'::regclass);


--
-- Name: dashboard_theme id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_theme ALTER COLUMN id SET DEFAULT nextval('public.dashboard_theme_id_seq'::regclass);


--
-- Name: dashboard_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user ALTER COLUMN id SET DEFAULT nextval('public.dashboard_user_id_seq'::regclass);


--
-- Name: dashboard_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user_groups ALTER COLUMN id SET DEFAULT nextval('public.dashboard_user_groups_id_seq'::regclass);


--
-- Name: dashboard_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.dashboard_user_user_permissions_id_seq'::regclass);


--
-- Name: dashboard_visitors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_visitors ALTER COLUMN id SET DEFAULT nextval('public.dashboard_visitors_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: oauth2_provider_accesstoken id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken ALTER COLUMN id SET DEFAULT nextval('public.oauth2_provider_accesstoken_id_seq'::regclass);


--
-- Name: oauth2_provider_application id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_application ALTER COLUMN id SET DEFAULT nextval('public.oauth2_provider_application_id_seq'::regclass);


--
-- Name: oauth2_provider_grant id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_grant ALTER COLUMN id SET DEFAULT nextval('public.oauth2_provider_grant_id_seq'::regclass);


--
-- Name: oauth2_provider_refreshtoken id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken ALTER COLUMN id SET DEFAULT nextval('public.oauth2_provider_refreshtoken_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
1	Admins
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	1	6
7	1	7
8	1	8
9	1	9
10	1	10
11	1	11
12	1	12
13	1	13
14	1	14
15	1	15
16	1	16
17	1	17
18	1	18
19	1	19
20	1	20
21	1	21
22	1	22
23	1	23
24	1	24
25	1	25
26	1	26
27	1	27
28	1	28
29	1	29
30	1	30
31	1	31
32	1	32
33	1	33
34	1	34
35	1	35
36	1	36
37	1	37
38	1	38
39	1	39
40	1	40
41	1	41
42	1	42
43	1	43
44	1	44
45	1	45
46	1	46
47	1	47
48	1	48
49	1	49
50	1	50
51	1	51
52	1	52
53	1	53
54	1	54
55	1	55
56	1	56
57	1	57
58	1	58
59	1	59
60	1	60
61	1	61
62	1	62
63	1	63
64	1	64
65	1	65
66	1	66
67	1	67
68	1	68
69	1	69
70	1	70
71	1	71
72	1	72
73	1	73
74	1	74
75	1	75
76	1	76
77	1	77
78	1	78
79	1	79
80	1	80
81	1	81
82	1	82
83	1	83
84	1	84
85	1	85
86	1	86
87	1	87
88	1	88
89	1	89
90	1	90
91	1	91
92	1	92
93	1	93
94	1	94
95	1	95
96	1	96
97	1	97
98	1	98
99	1	99
100	1	100
101	1	101
102	1	102
103	1	103
104	1	104
105	1	105
106	1	106
107	1	107
108	1	108
109	1	109
110	1	110
111	1	111
112	1	112
113	1	113
114	1	114
115	1	115
116	1	116
117	1	117
118	1	118
119	1	119
120	1	120
121	1	121
122	1	122
123	1	123
124	1	124
125	1	125
126	1	126
127	1	127
128	1	128
129	1	129
130	1	130
131	1	131
132	1	132
133	1	133
134	1	134
135	1	135
136	1	136
137	1	137
138	1	138
139	1	139
140	1	140
141	1	141
142	1	142
143	1	143
144	1	144
145	1	145
146	1	146
147	1	147
148	1	148
149	1	149
150	1	150
151	1	151
152	1	152
153	1	153
154	1	154
155	1	155
156	1	156
157	1	157
158	1	158
159	1	159
160	1	160
161	1	161
162	1	162
163	1	163
164	1	164
165	1	165
166	1	166
167	1	167
168	1	168
169	1	169
170	1	170
171	1	171
172	1	172
173	1	173
174	1	174
175	1	175
176	1	176
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add allowance report archive	1	add_allowancereportarchive
2	Can change allowance report archive	1	change_allowancereportarchive
3	Can delete allowance report archive	1	delete_allowancereportarchive
4	Can view allowance report archive	1	view_allowancereportarchive
5	Can add donations	2	add_donations
6	Can change donations	2	change_donations
7	Can delete donations	2	delete_donations
8	Can view donations	2	view_donations
9	Can add donations report archive	3	add_donationsreportarchive
10	Can change donations report archive	3	change_donationsreportarchive
11	Can delete donations report archive	3	delete_donationsreportarchive
12	Can view donations report archive	3	view_donationsreportarchive
13	Can add expenses report archive	4	add_expensesreportarchive
14	Can change expenses report archive	4	change_expensesreportarchive
15	Can delete expenses report archive	4	delete_expensesreportarchive
16	Can view expenses report archive	4	view_expensesreportarchive
17	Can add general expenses	5	add_generalexpenses
18	Can change general expenses	5	change_generalexpenses
19	Can delete general expenses	5	delete_generalexpenses
20	Can view general expenses	5	view_generalexpenses
21	Can add general expenses report archive	6	add_generalexpensesreportarchive
22	Can change general expenses report archive	6	change_generalexpensesreportarchive
23	Can delete general expenses report archive	6	delete_generalexpensesreportarchive
24	Can view general expenses report archive	6	view_generalexpensesreportarchive
25	Can add members	7	add_members
26	Can change members	7	change_members
27	Can delete members	7	delete_members
28	Can view members	7	view_members
29	Can add offerings	8	add_offerings
30	Can change offerings	8	change_offerings
31	Can delete offerings	8	delete_offerings
32	Can view offerings	8	view_offerings
33	Can add offerings report archive	9	add_offeringsreportarchive
34	Can change offerings report archive	9	change_offeringsreportarchive
35	Can delete offerings report archive	9	delete_offeringsreportarchive
36	Can view offerings report archive	9	view_offeringsreportarchive
37	Can add pledge item	10	add_pledgeitem
38	Can change pledge item	10	change_pledgeitem
39	Can delete pledge item	10	delete_pledgeitem
40	Can view pledge item	10	view_pledgeitem
41	Can add salaries paid	11	add_salariespaid
42	Can change salaries paid	11	change_salariespaid
43	Can delete salaries paid	11	delete_salariespaid
44	Can view salaries paid	11	view_salariespaid
45	Can add salaries paid report archive	12	add_salariespaidreportarchive
46	Can change salaries paid report archive	12	change_salariespaidreportarchive
47	Can delete salaries paid report archive	12	delete_salariespaidreportarchive
48	Can view salaries paid report archive	12	view_salariespaidreportarchive
49	Can add spend	13	add_spend
50	Can change spend	13	change_spend
51	Can delete spend	13	delete_spend
52	Can view spend	13	view_spend
53	Can add sundry	14	add_sundry
54	Can change sundry	14	change_sundry
55	Can delete sundry	14	delete_sundry
56	Can view sundry	14	view_sundry
57	Can add sundry report archive	15	add_sundryreportarchive
58	Can change sundry report archive	15	change_sundryreportarchive
59	Can delete sundry report archive	15	delete_sundryreportarchive
60	Can view sundry report archive	15	view_sundryreportarchive
61	Can add visitors	16	add_visitors
62	Can change visitors	16	change_visitors
63	Can delete visitors	16	delete_visitors
64	Can view visitors	16	view_visitors
65	Can add tithes report archive	17	add_tithesreportarchive
66	Can change tithes report archive	17	change_tithesreportarchive
67	Can delete tithes report archive	17	delete_tithesreportarchive
68	Can view tithes report archive	17	view_tithesreportarchive
69	Can add tithes	18	add_tithes
70	Can change tithes	18	change_tithes
71	Can delete tithes	18	delete_tithes
72	Can view tithes	18	view_tithes
73	Can add thanks giving report archive	19	add_thanksgivingreportarchive
74	Can change thanks giving report archive	19	change_thanksgivingreportarchive
75	Can delete thanks giving report archive	19	delete_thanksgivingreportarchive
76	Can view thanks giving report archive	19	view_thanksgivingreportarchive
77	Can add thanks giving	20	add_thanksgiving
78	Can change thanks giving	20	change_thanksgiving
79	Can delete thanks giving	20	delete_thanksgiving
80	Can view thanks giving	20	view_thanksgiving
81	Can add staff details	21	add_staffdetails
82	Can change staff details	21	change_staffdetails
83	Can delete staff details	21	delete_staffdetails
84	Can view staff details	21	view_staffdetails
85	Can add seeds report archive	22	add_seedsreportarchive
86	Can change seeds report archive	22	change_seedsreportarchive
87	Can delete seeds report archive	22	delete_seedsreportarchive
88	Can view seeds report archive	22	view_seedsreportarchive
89	Can add seeds	23	add_seeds
90	Can change seeds	23	change_seeds
91	Can delete seeds	23	delete_seeds
92	Can view seeds	23	view_seeds
93	Can add pledges report archive	24	add_pledgesreportarchive
94	Can change pledges report archive	24	change_pledgesreportarchive
95	Can delete pledges report archive	24	delete_pledgesreportarchive
96	Can view pledges report archive	24	view_pledgesreportarchive
97	Can add pledges cashed out	25	add_pledgescashedout
98	Can change pledges cashed out	25	change_pledgescashedout
99	Can delete pledges cashed out	25	delete_pledgescashedout
100	Can view pledges cashed out	25	view_pledgescashedout
101	Can add pledges	26	add_pledges
102	Can change pledges	26	change_pledges
103	Can delete pledges	26	delete_pledges
104	Can view pledges	26	view_pledges
105	Can add paid pledges	27	add_paidpledges
106	Can change paid pledges	27	change_paidpledges
107	Can delete paid pledges	27	delete_paidpledges
108	Can view paid pledges	27	view_paidpledges
109	Can add allowance	28	add_allowance
110	Can change allowance	28	change_allowance
111	Can delete allowance	28	delete_allowance
112	Can view allowance	28	view_allowance
113	Can add user	29	add_user
114	Can change user	29	change_user
115	Can delete user	29	delete_user
116	Can view user	29	view_user
117	Can add posts	30	add_posts
118	Can change posts	30	change_posts
119	Can delete posts	30	delete_posts
120	Can view posts	30	view_posts
121	Can add log entry	31	add_logentry
122	Can change log entry	31	change_logentry
123	Can delete log entry	31	delete_logentry
124	Can view log entry	31	view_logentry
125	Can add permission	32	add_permission
126	Can change permission	32	change_permission
127	Can delete permission	32	delete_permission
128	Can view permission	32	view_permission
129	Can add group	33	add_group
130	Can change group	33	change_group
131	Can delete group	33	delete_group
132	Can view group	33	view_group
133	Can add content type	34	add_contenttype
134	Can change content type	34	change_contenttype
135	Can delete content type	34	delete_contenttype
136	Can view content type	34	view_contenttype
137	Can add session	35	add_session
138	Can change session	35	change_session
139	Can delete session	35	delete_session
140	Can view session	35	view_session
141	Can view slider	36	view_slider
142	Can add slider	36	add_slider
143	Can change slider	36	change_slider
144	Can delete slider	36	delete_slider
145	Can view About	37	view_about
146	Can add About	37	add_about
147	Can change About	37	change_about
148	Can delete About	37	delete_about
149	Can view page	38	view_page
150	Can add page	38	add_page
151	Can change page	38	change_page
152	Can delete page	38	delete_page
153	Can view Gallery	39	view_gallery
154	Can add Gallery	39	add_gallery
155	Can change Gallery	39	change_gallery
156	Can delete Gallery	39	delete_gallery
157	Can view image	40	view_image
158	Can add image	40	add_image
159	Can change image	40	change_image
160	Can delete image	40	delete_image
161	Can view News	41	view_news
162	Can add News	41	add_news
163	Can change News	41	change_news
164	Can delete News	41	delete_news
165	Can view event	42	view_event
166	Can add event	42	add_event
167	Can change event	42	change_event
168	Can delete event	42	delete_event
169	Can view church	43	view_church
170	Can add church	43	add_church
171	Can change church	43	change_church
172	Can delete church	43	delete_church
173	Can add contact	44	add_contact
174	Can change contact	44	change_contact
175	Can delete contact	44	delete_contact
176	Can view contact	44	view_contact
177	Can add building renovation	45	add_buildingrenovation
178	Can change building renovation	45	change_buildingrenovation
179	Can delete building renovation	45	delete_buildingrenovation
180	Can view building renovation	45	view_buildingrenovation
181	Can add expenditures	46	add_expenditures
182	Can change expenditures	46	change_expenditures
183	Can delete expenditures	46	delete_expenditures
184	Can view expenditures	46	view_expenditures
185	Can add revenues	47	add_revenues
186	Can change revenues	47	change_revenues
187	Can delete revenues	47	delete_revenues
188	Can view revenues	47	view_revenues
189	Can add archived members	48	add_archivedmembers
190	Can change archived members	48	change_archivedmembers
191	Can delete archived members	48	delete_archivedmembers
192	Can view archived members	48	view_archivedmembers
193	Can add cash float	49	add_cashfloat
194	Can change cash float	49	change_cashfloat
195	Can delete cash float	49	delete_cashfloat
196	Can view cash float	49	view_cashfloat
197	Can add application	50	add_application
198	Can change application	50	change_application
199	Can delete application	50	delete_application
200	Can view application	50	view_application
201	Can add access token	51	add_accesstoken
202	Can change access token	51	change_accesstoken
203	Can delete access token	51	delete_accesstoken
204	Can view access token	51	view_accesstoken
205	Can add grant	52	add_grant
206	Can change grant	52	change_grant
207	Can delete grant	52	delete_grant
208	Can view grant	52	view_grant
209	Can add refresh token	53	add_refreshtoken
210	Can change refresh token	53	change_refreshtoken
211	Can delete refresh token	53	delete_refreshtoken
212	Can view refresh token	53	view_refreshtoken
213	Can add cors model	54	add_corsmodel
214	Can change cors model	54	change_corsmodel
215	Can delete cors model	54	delete_corsmodel
216	Can view cors model	54	view_corsmodel
217	Can add ministry	55	add_ministry
218	Can change ministry	55	change_ministry
219	Can delete ministry	55	delete_ministry
220	Can view ministry	55	view_ministry
221	Can view Projects	56	view_project
222	Can add Projects	56	add_project
223	Can change Projects	56	change_project
224	Can delete Projects	56	delete_project
225	Can view theme	57	view_theme
226	Can add theme	57	add_theme
227	Can change theme	57	change_theme
228	Can delete theme	57	delete_theme
229	Can add completed task	58	add_completedtask
230	Can change completed task	58	change_completedtask
231	Can delete completed task	58	delete_completedtask
232	Can view completed task	58	view_completedtask
233	Can add task	59	add_task
234	Can change task	59	change_task
235	Can delete task	59	delete_task
236	Can view task	59	view_task
237	Can add testing	60	add_testing
238	Can change testing	60	change_testing
239	Can delete testing	60	delete_testing
240	Can view testing	60	view_testing
241	Can add annual conference	61	add_annualconference
242	Can change annual conference	61	change_annualconference
243	Can delete annual conference	61	delete_annualconference
244	Can view annual conference	61	view_annualconference
245	Can add new convert	62	add_newconvert
246	Can change new convert	62	change_newconvert
247	Can delete new convert	62	delete_newconvert
248	Can view new convert	62	view_newconvert
\.


--
-- Data for Name: background_task; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.background_task (id, task_name, task_params, task_hash, verbose_name, priority, run_at, repeat, repeat_until, queue, attempts, failed_at, last_error, locked_by, locked_at, creator_object_id, creator_content_type_id) FROM stdin;
\.


--
-- Data for Name: background_task_completedtask; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.background_task_completedtask (id, task_name, task_params, task_hash, verbose_name, priority, run_at, repeat, repeat_until, queue, attempts, failed_at, last_error, locked_by, locked_at, creator_object_id, creator_content_type_id) FROM stdin;
\.


--
-- Data for Name: corsheaders_corsmodel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.corsheaders_corsmodel (id, cors) FROM stdin;
\.


--
-- Data for Name: dashboard_about; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_about (id, about_image, about, mission_description, "Is_View_on_Web", vision_description, about_title, core_values, church_details) FROM stdin;
3	about/IMG_3486.JPG	United Christian Centre Bwaise (UCC BWAISE) is a born again Christian church in Kampala Uganda East Africa.\r\nThe church is located on Bwaise ΓÇô Nabweru road.\r\n The lead pastor is Pr. Joshua Zake ministering with a team of other associate pastors namely; Pr. Sande Posiano Zakumumpa, Pr. Henry Musubize, Pr. Sanyu Rebecca, Pr. Mukisa Kintu\r\nand other preachers of the word including the following\r\nMr. John Bosco Buyuki, Mr. Charles Bunjo, Mr. Kasirye Eddie and others.\r\n\r\nThe following are ministries at UCC-Bwaise\r\nWorship team\r\nChildrenΓÇÖs ministry\r\nYouth ministr\r\nWomenΓÇÖs ministry\r\nMenΓÇÖministry\r\nTeenΓÇÖs ministry\r\nEvangelism ministry\r\nUshers ministry\r\n\r\nVision: ΓÇ£Discovering and Doing GodΓÇÖs willΓÇ¥ \r\nThis is accomplished with the help of a Church Mission ΓÇô ΓÇ£Lwaki oli mulamuΓÇ¥ (why are you alive) Teach Me To do your will, for you are my God(Psalms 143:10).(John 18:37)\r\n\r\nMission: " Lwaki Oli Mulamu(Why are you alive)"\r\nThis mission is accomplished by broadcasting on Christian radio with a program running on Innerman fm every Sunday morning at 7 ΓÇô 8 am Uganda time .this frequency is also accessible online by app ΓÇô InnerMan2 fm\r\n\r\nThe church also has an outreach ministry of ΓÇÿLwaki oli mulamuΓÇÖ (why are you alive) missions with seminars almost every month both within and outside the country.\r\n\r\nPastor Joshua Zake has written several audio and video messages and Christian books for spiritual nourishments such as;\r\n1. The inner burning\r\n2. An upright heart\r\n3. What can a Christian do amidst the storm\r\n4. Why are you Alive	ΓÇÿΓÇÿWHY ARE YOU ALIVEΓÇÖΓÇÖ\r\nIntroduction \r\nThis is a very fundamental question in our lives. It deals with the reason why someone is in existence. It is important for each one of us to discover why they are alive. So many people have failed to discover the purpose of their lives and many have actually come to the end of their ΓÇÿjourneysΓÇÖ without getting the slightest idea of why they ever lived.\r\nThe scriptures teach us that the of spirit ΓÇ£mankindΓÇ¥ existed long before the creation of the world.\r\nThe creation of mankind happened in the eternity before God created any other thing in the physical world.\r\nWisdom  who is Christ , in Proverbs tell the story of what happened before the physical world was created - Prov 8:22  \r\nAs Christ tell the story he tells us of his moments with mankind in Spiritual world before the physical world was created \r\nVerse 31 ΓÇ£Rejoicing in the habitable part of his earth; and my delights were with the sons of menΓÇ¥.\r\n\r\nThe Psalmist through the prayer of Moses also reveals that spirit of mankind lived with God long before coming to the earth. \r\n\r\n ΓÇ£A Prayer of Moses the man of God. Lord, thou hast been our dwelling place in all generationsΓÇ¥. Psalms 90:1\r\n\r\nAnd that spirit existed before the body and even the days of mankind were known to God even before he was manifested on earth. ΓÇ£Your eyes saw my unformed Body. All the days ordained for me were written in your book before one of them came to be. Psalm 139:16.\r\nThis actually explains why manΓÇÖs spirit has got to return ΓÇ£to God, who gave it.ΓÇ¥ Ecclesiastes 12:7.\r\n\r\nGod predestined a lot of things about mankind. He knows each person and He selected them for His purpose. According to the Bible, even before one is born, they are known to God.\r\n  ΓÇ£I knew you before I formed you in your motherΓÇÖs womb.ΓÇ¥ Jeremiah 1: 5\r\n29ΓÇ¥For God knew his people in advance, and he chose them to become like his Son, so that his son would be the firstborn, with many brothers and sister. 30 And having chosen them, he called them to come to him. And he gave them right standing with himself, and he promised them his glory.ΓÇ¥ Romans 8:29-30\r\n\r\nItΓÇÖs God who chose when the spirit mankind should come on planet earth and definitely when it shall return to Him.  God determines birthdays and death days as the Bible states that ΓÇÿThe length of manΓÇÖs life is decided beforehand.ΓÇÖ Job 14:5\r\n\r\nThe best way you can get to know why you are alive is by getting to know your origin. The Bible states in Genesis 1:26 that ΓÇ£Then God said, ΓÇ£And now we will make human beings; they will be like us and resemble us. They will have power over the fish, the birds and all animals, domestic and wild, large and small. So God created human beings, making them to be like to him. He created them male and female. In his own image in the image of God created He him male and female.ΓÇ¥\r\nBeing in the image of God means that man is a spiritual being dwelling in the physical world walking a physical journey. Otherwise,   the citizenship of mankind is in heaven as stated by Paul in Philippians 3:20.  However, God determines sets the times for every mankind and the exact places where they should live. He brings one forth at a point in time to move them in His own direction. Man is GodΓÇÖs messenger, a person sent from Heaven with a peculiar mission on earth.\r\n ΓÇ£Iam the one who spoke and called him; I led him out and gave him success. Now come close to me and hear what I say. From the beginning I have spoken openly and have always made my words come true. The Holy God of Israel, the Lord who saves, says Iam the Lord your God, the one who wants to teach you for your own good and direct you in the way you should go.ΓÇ¥ Isaiah 48:15-17 \r\n\r\nThe Bible sometimes refers to human beings as ΓÇÿChristΓÇÖs AmbassadorsΓÇÖ 1 Corinthians 5:20 to show that man is a representative of the heavenly kingdom here on earth. As an ambassador, man is on a heavenly mission on earth. He is an instrument of transformation that is supposed to bring about change in places or systems wherever they go. Man is specifically designed and set apart for a particular purpose (Jeremiah 1:5) which purpose is ordained by God to be a fulfilment in lives of other people; families, nations and generally the entire creation. Man is a part of GodΓÇÖs original project and according to (Psalms 139:16) God scheduled every day of your life before you came to be.\r\n\r\nWHO ASKS WHY YOU ARE ALIVE?\r\n\r\nThe question ΓÇ£Why one is aliveΓÇ¥ can be asked by God, by fellow men or the individual Christian. \r\nIt is a very fundamental question which each one of should take time to meditate upon or else we abuse our stay on earth. T\r\n\r\nhis booklet is meant to help you to discover the reasons why you were created and why you are still on the face of the world. It will help you to know the reason and purpose for your being alive and how to set goals and ways of achieving a fulfilled life.\r\n\r\nWhen you are able to fully understand why you are alive, you will be able to make a difference during your time. This will enhance the quality of your life and set you on the road to success and fulfilment.\r\nBut this will take the spirit of the Lord; you will need to humble yourself before God to be able to know His will for your life. Whatever it is, the reason for your ΓÇÿbeingΓÇÖ has a lot to do with your ΓÇÿcreatorΓÇÖ. \r\nThe only possible reason why you appeared in a particular city, town or even family was for you to be released to your own generation to serve mankind and bring all things in your sphere of influence under the ruler ship of Christ. As it is stated in 1Corinthians 10:31 \r\n\r\n1.\tBY GOD\r\nThrough the word of God we come to learn about manΓÇÖs pre existence before coming into this world and therefore, there must be a reason why God decided to bring man on earth. There must have been a Godly plan which is called ΓÇÿGodΓÇÖs willΓÇÖ. \r\nGenerations after generations, God has been sending ΓÇÿlivesΓÇÖ on the planet earth for a specific period of time.  During the given number of days, months or years that one lives, God keeps checking on manΓÇÖs progress but sometimes He wonders why some people, are still alive since they donΓÇÖt seem to be doing what He sent them to do. This is very unfortunate and the Bible says that ΓÇ£The axe is already at the root of the trees, and every tree that does not produce good fruit will be cut down and thrown in fire.ΓÇ¥ Mathew 3:10\r\n\r\nMan is not an accident but a person appointed to be GodΓÇÖs servant even before he existed. According to Jeremiah 1:5, man has been set apart and appointed as GodΓÇÖs spokesperson. This means that each person has got what it takes to do GodΓÇÖs will. Whatever gifts God gives someone, He gives them so that one in turn gives them away in service to God. Everyone was created to share their life and talents with the community around them. When we become believers we also become GodΓÇÖs messengers. He wants to speak to the world through us and whatever we have gone through should be a message that God wants us to teach to others.	Yes	Whenever God calls you to serve him for a long time commission, itΓÇÖs very important to know what he has called you to and how to do it. Sometimes he may not give you the full details, but at least he always shows you the start and the end of that Commission. The vision is very important because it will be a guideline and a focus as you execute the commission.\r\n\r\nA vision being is a revelation of the full picture of GodΓÇÖs plan, will or purpose; itΓÇÖs the ultimate goal that one should target to get to\r\nAs Ucc Bwaise, God has given us a focus of what He wants us to follow and emphasise in this ministry ΓÇô Discovering and Doing GodΓÇÖs will.\r\n\r\nWe shall therefore divide this Vision in 3 segments\r\n1.\tGodΓÇÖs will\r\n\r\n2.\tDiscovering\r\n\r\n3.\tDoing GodΓÇÖs will \r\n\r\nIn this Church vision, the core value is GodΓÇÖs will and therefore we must well understand it before we dare to discover and then go on doing it\r\nGodΓÇÖs will is GodΓÇÖs heart, plan, choice, purpose, desire, and future over someone or something. This will is not obvious unto every one, it calls for discover after that you can then go on and do exactly that. \r\nGodΓÇÖs will either refers to what He wants or does not want at a particular moment.\r\n\r\nThe does and donΓÇÖts are two things that even make up the commandments of God and the word of God.\r\n\r\nTypes of GodΓÇÖs will\r\n\r\n-\tIndividual\r\n-\tGeneral\r\n-\tSeasonal\r\n-\tContributional / Personal\r\n\r\nI strongly believe that a lot of things happened before creation and basically before Mankind came on this planet Earth\r\nGod never does something for nothing!\r\nΓÇó\tWhy bring man on Earth\r\n-\tWhen the devil was thrown here the earth became hell of a place\r\n-\tNo barren Spirit- Messenger without message\r\n-\tProv. 8:22 Vs 31 - Wisdom (Christ tells the story of creation)\r\n-\tGen 1:26 -Let us make man.... so that....\r\n-\tJer 1:5, 1sh 49:1, \r\nΓÇó\tHow should man look like\r\n-\tEarthly  vessels for Spirit man Eccl 12:7( Male and Female)\r\n-\tSoul Spirit and Body\r\n-\tPs 139:14, 1 Jn 3:1, Jn 9:2\r\nΓÇó\tHow long should man live for ΓÇô Birth day and Death days set\r\nPs 39:4, Job 14:5, Ps 90:12\r\nΓÇó\tWhere should the Spirit called mankind be de1ivered / stay\r\n-\tLocation and Parents\r\n-\tActs 17:24 -27\r\n-\tIsh 51:1, Deut 32: 18, 1cor 10:4- drank from same spiritual rock Christ but we are all different in many ways.\r\n\r\n\r\nADAMIC FALL AWAY AND CONSEQUENCES \r\nThis brought a roundabout in the plan and mission of God on planet earth - it became a rescue mission\r\nΓÇó\tMankind was created upright ΓÇô Eccl 7:29\r\nΓÇó\tWhen sinned, he was Corrupted, Corroded Dis-figured \r\nNeed for Rescue; -\r\n-\t Revival\r\n-\t Restoration\r\n-\t Salvation \r\n-\tRomans 3:23  - For all have sinned, and come short of the glory of God;\r\n-\tRomans 5:12 - Wherefore, as by one man sin entered into the world, and death by sin; and so death passed upon all men, for that all have sinned:\r\n-\t\r\nΓÇó\tChrist came to seek and save the lost -  Luke 19:10\r\n\r\n∩ü╢\tIn this great rescue mission where there is reviving, restoring and saving mankind, a lot of work has to be done and Christ is the author of that great work -\r\n-\tHeb. 5:9 And being made perfect, he became the author of eternal salvation unto all them that obey him;\r\n-\tHeb. 12:2 Looking unto Jesus the author and finisher of our faith; who for the joy that was set before him endured the cross, despising the shame, and is set down at the right hand of the throne of God.\r\n-\tEphes. 4:8 Wherefore he saith, when he ascended up on high, he led captivity captive, and gave gifts unto men.\r\n∩ü╢\tNow that Christ started it, he gives us a great mission of reconciling mankind to God through different gifts and callings. Every one of us has a task therefore to discover oneself as in how did God prepare him or her to best serve his will \r\n-\t2Cor. 5:18 And all things are of God, who hath reconciled us to himself by Jesus Christ, and hath given to us the ministry of reconciliation;\r\nVs.19 To wit, that God was in Christ, reconciling the world unto himself, not imputing their trespasses unto them; and hath committed unto us the word of reconciliation. \r\n∩ü╢\tEvery one of us has a task of discovering and doing GodΓÇÖs will in the few years God gives you to live on this planet.\r\n\r\nHOW DO WE DISCOVER GODΓÇÖS WILL\r\n\r\nEach one of us was given a divine mission and God has a purpose for each one that is different from any other personΓÇÖs. However, many people are unable to walk according to GodΓÇÖs divine calendar. \r\nDiscovering GodΓÇÖs will is very vital because it enables us to know what He wants us to do and what He does not want us to do. The Bible states that ΓÇ£ItΓÇÖs GodΓÇÖs privilege to conceal things and the kingΓÇÖs privilege to discover them.ΓÇ¥Prov25:2\r\n\r\nItΓÇÖs a challenge for everyone who really wants to live for God and not for themselves to seek to discover GodΓÇÖs will. GodΓÇÖs will can be discovered in several ways including; \r\n∩âÿ\tNow that GodΓÇÖs will is not obvious to many people, there isnΓÇÖt any of us upon whom God doesnΓÇÖt have purpose! It leaves us with a challenge which we must solve ΓÇô why am I alive?\r\n∩âÿ\tOur God communicates to us in many ways now that our understanding and perception is also diverse; some easily understand by hearing once and several time while others do by seeing, yet others need both.  \r\n∩âÿ\tGod communicates to us in several ways as he shares with us his heart though many times we still do not understand but that doesnΓÇÖt stop his endeavours\r\n∩âÿ\tIt makes this communication easy if the one he is communicating to is very interested and therefore anxious or even attentive ΓÇô 1Sam 3:1-9\r\n∩âÿ\tWe can therefore know his will through some of the following ways;-	\N	1. Discipline\r\n\r\n2. Fear of God\r\n\r\n3. Humility and dignity\r\n\r\n4. Others before self.\r\n\r\n5. Respect for leaders	United Christian Centre Bwaise (UCC BWAISE) is a born again Christian church in Kampala Uganda East Africa.\r\nThe church is located on Bwaise ΓÇô Nabweru road.\r\nThe lead pastor is Pr. Joshua Zake ministering with a team of other associate pastors namely; Pr. Sande Posiano Zakumumpa, Pr. Henry Musubize, Pr. Sanyu Rebecca, Pr. Mukisa Kintu\r\nand other preachers of the word including the following\r\nMr. John Bosco Buyuki, Mr. Charles Bunjo, Mr. Kasirye Eddie and others.\r\nThe following are ministries at UCC-Bwaise\r\nWorship team\r\nChildrenΓÇÖs ministry\r\nYouth ministr\r\nWomenΓÇÖs ministry\r\nMenΓÇÖministry\r\nTeenΓÇÖs ministry\r\nEvangelism ministry\r\nUshers ministry\r\nVision: ΓÇ£Discovering and Doing GodΓÇÖs willΓÇ¥\r\nThis is accomplished with the help of a Church Mission ΓÇô ΓÇ£Lwaki oli mulamuΓÇ¥ (why are you alive) Teach Me To do your will, for you are my God(Psalms 143:10).(John 18:37)\r\nMission: " Lwaki Oli Mulamu(Why are you alive)"\r\nThis mission is accomplished by broadcasting on Christian radio with a program running on Innerman fm every Sunday morning at 7 ΓÇô 8 am Uganda time .this frequency is also accessible online by app ΓÇô InnerMan2 fm\r\nThe church also has an outreach ministry of ΓÇÿLwaki oli mulamuΓÇÖ (why are you alive) missions with seminars almost every month both within and outside the country.\r\nPastor Joshua Zake has written several audio and video messages and Christian books for spiritual nourishments such as;\r\n1. The inner burning\r\n2. An upright heart\r\n3. What can a Christian do amidst the storm\r\n4. Why are you Alive
\.


--
-- Data for Name: dashboard_annualconference; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_annualconference (id, start_date, end_date, estimated_budget, conference_theme, conference_report) FROM stdin;
1	2020-09-11	2020-10-02	13000	Loving God	
2	2020-09-11	2020-10-02	13000	Loving God	
3	2020-09-11	2020-10-02	13000	Loving God	
5	2020-09-17	2020-09-29	250000	Merciful God	
4	2020-04-09	2019-09-05	40000000	Ensigo Bwetagwa mutaka neffa, tebala bibala bingi	
\.


--
-- Data for Name: dashboard_cashfloat; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_cashfloat (id, "Date", "Amount", "Notes") FROM stdin;
10	2020-06-19	2000000	float
12	2020-07-04	900000	float for the second week of june
13	2020-07-23	1400000	
14	2020-08-01	100000	yfuuj vbiuv jbhvbjh jhvjhhj
11	2020-09-02	1250000	third week of June
15	2020-09-14	100000	cashfloat to be used
16	2020-09-28	1000000	for the first week of october
\.


--
-- Data for Name: dashboard_church; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_church (id, church_code, church_name, address, phone, registration_date, email_address, "Post_Office_Box", footer, enable_frontend, latitude, longitude, facebook_url, twitter_url, "linkedIn_url", google_plus_url, youtube_url, instagram_url, pinterest_url, "Church_Logo", status, maps_embedded_link, church_mission, church_vision) FROM stdin;
1	church1	UNITED CHRISTIAN CENTER - BWAISE	Kafunda Bwaise	0772 614086	2020-02-06	uccbwaise1@gmail.com	6589 Kampala, Uganda	All Rights Reserved @UCC Bwaise	Yes	\N	\N	https://web.facebook.com/uccbwaise1/	https://web.facebook.com/uccbwaise1/	https://web.facebook.com/uccbwaise1/	https://web.facebook.com/uccbwaise1/	https://www.youtube.com/channel/UCFMCB_zTwBQNunbpjBsPcSw/videos	https://web.facebook.com/uccbwaise1/	https://web.facebook.com/uccbwaise1/	logo/uccchurch_WNKhacV.jpg	Active	https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d7979.4856942634915!2d32.54923615200376!3d0.35241807093564126!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x3788a86d81fbe8f3!2sUNITED%20CHRISTIAN%20CENTER%20(UCC%20BWAISE)!5e0!3m2!1sen!2sug!4v1580995133401!5m2!1sen!2sug	Why Are You Alive?	Discovering and Doing God's Will
\.


--
-- Data for Name: dashboard_contact; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_contact (id, name, email, phone, subject, message, feedback) FROM stdin;
4	Ssempijja Jimmie	Jimmy@gmail.com	0847467783	\N		I just love UCC Bwaise
5	Bagyenda Steven	bagsteves@gmail.com	0784948989	\N		A very transforming church where lives never remain the same
7	Desire Namuganyi	\N	\N	\N		Am glad am part of this church
9	Zake Joshua	\N	\N	\N		We Serve the living God, the creator of the heavens and the earth
8	Ssempijja Jimmie	Jimmy@gmail.com	076557885768	Thank you	tfghujyvguk\r\nhhuuuygyu	Awesome Web Church System
10	Odeke Mable	\N	\N	\N		Being a UCC family member is such a thrilling feeling
43	Gitta K	\N	\N	\N		Glad to be part of this kingdom building family of God.
\.


--
-- Data for Name: dashboard_event; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_event (id, event_title, event_for, event_place, from_date, to_date, image, note, "Is_View_on_Web", date, "Activity_Type", "Day", "End_Time", "Program_Name", "Start_Time") FROM stdin;
1	Church's Vision and Mission	SuperAdmin	Church	2020-02-01	2020-03-01	images/FB_IMG_15614879910649330.jpg	Teaching all the members the church vision and mission so that everyone can explain it to other non church members	Yes	2020-02-06	Events	\N	\N	\N	\N
2	Church Outting	Members	Gaba Beach	2020-02-29	2020-02-05	images/uccchurch.jpg	Church members getting together to have fan	Yes	2020-02-06	Events	\N	\N	\N	\N
4	Baptism	Members	Church	2020-02-06	2020-02-06	images/inside1.jpg	baptising	Yes	2020-02-06	Events	\N	\N	\N	\N
7	Conference	SuperAdmin	UCC Bwaise	2020-02-28	2020-03-07	images/1_1.jpg	annual lwaki olimulamu	Yes	2020-02-22	Events	\N	\N	\N	\N
8	Computer Literacy	Members	UCC Bwaise	2020-02-25	2020-03-07	images/IMG_20191210_110351_741.JPG	Learning Computer Basics	Yes	2020-02-22	Events	\N	\N	\N	\N
5	Health Sensitization	Members	UCC Bwaise	2020-03-01	2020-03-01	images/front1.JPG	Blood checking, health tips and other advice	Yes	2020-02-13	Church_Program	Monday	04:00:00	\N	09:00:00
6	Bible Challenge	Members	UCC Bwaise	2020-02-22	2020-03-01	images/ps.jpg	Different Church Groups to participate	Yes	2020-02-13	Events	Monday	09:30:00	\N	07:00:00
9	Lwaki Olimulamu Annual Conerence 202	SuperAdmin	Kampala	2020-02-29	2020-03-07	images/1_KsAIZiZ.JPG	life	Yes	2020-02-29	Events	\N	\N	\N	\N
3	Women's Day	Members	UCC Bwaise	2020-02-06	2020-02-06	images/IMG_3563.JPG	Women of UCC Bwaise when they prepare to serve, they serve n mighty	No	2020-02-06	Events	\N	\N	\N	\N
10	Building	SuperAdmin	UCC Bwaise	2020-06-01	2020-06-27	images/IMG-20200428-WA0001_iTHHBOt.jpg	Floor levelling, Making finishing and other construction work	Yes	2020-06-03	Events	\N	\N	\N	\N
\.


--
-- Data for Name: dashboard_expenditures; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_expenditures (id, "Date", "Payment_Made_To", "Amount", "Reason_filtering", "Other_Expenditure", "Notes", "Main_Expense_Reason", "General_Expenses_Reason", "Petty_Cash_Reason", "Archived_Status", "Member_Name_id") FROM stdin;
1	2020-06-19	Mathew	20000	petty	help	\N	\N	\N	Other	ARCHIVED	\N
3	2020-06-19	Sam	30000	general	\N	\N	\N	Stationery	\N	ARCHIVED	\N
4	2020-06-27	Matayo	25000	main	\N	\N	Evangelism	\N	\N	ARCHIVED	\N
5	2020-07-04	Pr. Lwere	30000	petty	Thanks giving	\N	\N	\N	Other	ARCHIVED	\N
6	2020-07-21	Mathew	30000	petty	\N	\N	\N	\N	Upkeep	ARCHIVED	\N
7	2020-07-30	Sam	209039	main	\N	\N	Drinks	\N	\N	ARCHIVED	\N
8	2020-07-30	NEMA	30000	general	\N	\N	\N	Condolences	\N	ARCHIVED	\N
2	2020-08-03	\N	30000	allowance	\N	Appreciation	\N	\N	\N	ARCHIVED	7
9	2020-08-03	\N	100000	allowance	\N	Appreciation	\N	\N	\N	ARCHIVED	12
11	2020-09-08	Mr. James	100000	general	\N	\N	\N	Condolences	\N	ARCHIVED	\N
10	2020-09-02	Jonah	20000	general	\N	\N	\N	Repair	\N	ARCHIVED	\N
44	2020-09-28	Kenny	25000	main	\N	\N	Water Bills	\N	\N	NOT-ARCHIVED	\N
\.


--
-- Data for Name: dashboard_gallery; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_gallery (id, gallery_title, note, "Is_View_on_Web", date) FROM stdin;
2	Youths	It was December 9th, 2019. UCC Bwaise youth ministry held a getting together dinner which was attended by many of the youths even those who were off the grid could not miss such an opportunity.	Yes	2020-06-03
3	New Church Building	Construction Underway	Yes	2020-06-03
4	Women's Day	They Ministered the whole week and climaxed it on Sunday with Special lunch	Yes	2020-06-03
5	Men's Day	Every man needs godly men connecting him to the church.\r\nI cannot imagine going through life without having a purpose or mission.\r\nEvery man wants to be a part of something that is bigger than himself.\r\nWith new ministries, find a champion and resource them toward a specific mission.Ministering in m	Yes	2020-06-03
1	Conference 2020	Lwaki Oli Mulamu Lwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli MulamuLwaki Oli M	Yes	2020-06-03
6	Our Church Hall	Glory Glory Glory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGlory GloryGl	Yes	2020-06-05
\.


--
-- Data for Name: dashboard_image; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_image (id, gallery_image, image_caption, gallery_title_id, "Is_View_on_Web", date) FROM stdin;
1	images/IMG_3543.JPG	Pastor Joshua and  Mummy Joy Zakes	1	Yes	2020-06-03
2	images/IMG_3609.JPG	Awesomeness	2	Yes	2020-06-03
3	images/build2_Ju9BowA.jpg	Inspecting Church New Hall	3	Yes	2020-06-03
5	images/IMG_3487.JPG	Happiness	4	Yes	2020-06-03
6	images/IMG_3602.JPG	Food Session	4	Yes	2020-06-03
7	images/IMG_3485.JPG	Omukyala Mukama Yamutonda nag wanjawulo	4	Yes	2020-06-03
9	images/IMG_3495.JPG	Sermon Time	4	Yes	2020-06-03
10	images/IMG-20191224-WA0022.jpg	Get together dinner	2	Yes	2020-06-03
11	images/IMG-20191224-WA0007.jpg	Get together dinner	2	Yes	2020-06-03
12	images/IMG-20191224-WA0010.jpg	Get together dinner	2	Yes	2020-06-03
13	images/IMG-20191224-WA0012.jpg	Get together dinner	2	Yes	2020-06-03
14	images/IMG-20191224-WA0017.jpg	Get together dinner	2	Yes	2020-06-03
15	images/IMG-20191224-WA0018.jpg	Get together dinner	2	Yes	2020-06-03
16	images/IMG-20191224-WA0014_818pWHb.jpg	Get together dinner	2	Yes	2020-06-03
17	images/1.jpg	Ministering in mighty	5	Yes	2020-06-03
18	images/2.jpg	Ministering in mighty	5	Yes	2020-06-03
20	images/men.jpg	Ministering in mighty	5	Yes	2020-06-03
22	images/IMG-20200323-WA0008.jpg	finishing up	3	Yes	2020-06-03
23	images/IMG-20200428-WA0000.jpg	Levelling the floor	3	Yes	2020-06-03
4	images/2_wm6fyXk_54nS3wN.jpg	Construction underway	3	Yes	2020-06-03
19	images/3.jpg	Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty	5	Yes	2020-06-03
25	images/IMG-20200323-WA0008_tRFXPIP.jpg	Hallelujah\r\n\r\n Hallelujah\r\nHallelujah\r\n\r\nHallelujah\r\n\r\nHallelujah\r\nMinistering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in mighty Ministering in	6	Yes	2020-06-05
24	images/IMG-20200428-WA0001_FEYzD8q.jpg	Levelling the floor	3	Yes	2020-06-03
26	images/contact.jpg	utyewu	6	Yes	2020-08-20
\.


--
-- Data for Name: dashboard_members; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_members (id, "First_Name", "Second_Name", "Home_Cell", "Residence", "Telephone", "Email", "Photo", "Gender", "Marital_Status", "Marriage_Kind", "Education_Level", "Profession", "Type_of_Work", "Place_of_Work", "Country", "County", "Parish", "District", "Sub_County", "Village", "Date_Of_Salvation", "Date_Of_Birth", "Date_Of_Joining_UCC_Bwaise", "Ministry_Involved_In", "Name_Of_Next_Of_Kin", "Contact_Of_Next_Of_Kin", "Residence_Of_Next_Of_Kin", "Initials", "Is_View_on_Web", "Group", "More_Info", date, is_active, "Archived_Status", "Full_Named") FROM stdin;
15	Upendo	Flistar	Kafunda Zone	Nabweru	02389004	email@email.com	avatars/upendo.jpg	Female	Single	Cohabiting	Degree	Unemployed	\N	\N	Uganda	Kyandondo	Maganjo	Wakiso	Nabweru	Nabweru South	\N	\N	\N	Youth Leadership	\N	\N	\N	Ms.	Yes	Victors		2020-10-05 11:52:48.569134+03	t	NOT-ARCHIVED	Upendo Flistar
12	Henry	Musubize	Lugoba Zone	Lugoba	07536277884	email@email.com	avatars/pr_henry.JPG	Male	Single	\N	Certificate	Employed	Motor	Kampala	\N	\N	\N	\N	\N	\N	\N	\N	\N	Pastoral	\N	\N	\N	Pr.	Yes	Overcomers	Vision: ΓÇ£Discovering and Doing GodΓÇÖs willΓÇ¥ which is accomplished with the help of a Church Mission ΓÇô ΓÇ£Lwaki oli mulamuΓÇ¥ (why are you alive) Teach Me To do your will, for you are my God(Psalms 143:10).(John 18:37)\r\nMission: " Lwaki Oli Mulamu(Why are you alive)"\r\nThis mission is accomplished by broadcasting on Christian radio with a program running on Innerman fm every Sunday morning at 7 ΓÇô 8 am Uganda time .this frequency is also accessible online by app ΓÇô InnerMan2 fm	2020-10-05 11:52:48.575364+03	t	NOT-ARCHIVED	Henry Musubize
100	Jimmy	Ssembirige	Kafunda Zone	Nabweru	0772194309	uccbwaise1@gmail.com	avatars/maxresdefault.jpg	Male	Married	Church_Marriage	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2020-02-03	\N	Discipleship	\N	\N	\N	Mr.	Yes	Victors		2020-10-05 09:38:19.912131+03	t	NOT-ARCHIVED	Jimmy Ssembirige
98	Cate	Byekwaso	Gombolola Zone	Nabweru	076348778599	dihfahsihm@gmail.com	avatars/cover.png	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2020-07-18	\N	Discipleship	\N	\N	\N	Mrs.	Yes	God is Able		2020-10-05 09:38:19.936068+03	t	NOT-ARCHIVED	Cate Byekwaso
90	Mayanja	Mayanja	Church Zone	Nabweru	08945879589	mayanja@gmail.com	avatars/mayanja.jpg	Male	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2020-06-19	\N	Discipleship	\N	\N	\N	Mr.	Yes	Winners		2020-10-05 09:38:19.955063+03	t	NOT-ARCHIVED	Mayanja Mayanja
42	Sophie	Kaaya	Katooke Zone	Katooke	0784973839	kaaya@gmail.com	avatars/sophie.jpg	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2020-06-18	\N	Discipleship	\N	\N	\N	Mrs.	Yes	Overcomers		2020-10-05 09:38:19.96104+03	t	NOT-ARCHIVED	Sophie Kaaya
39	Innocent	Tusingwire	Church Zone	Nansana	07847658959	innocent@gmail.com	avatars/budject.jpg	Male	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2020-06-10	\N	Discipleship	\N	\N	\N	\N	Yes	Biyinzika		2020-10-05 09:38:19.973071+03	t	NOT-ARCHIVED	Innocent Tusingwire
99	Susan	Nsubuga	Kafunda Zone	Kafunda	07648747487	dihfahsihm@gmail.com	avatars/IMG_3514.JPG	Female	Married	Church_Marriage	\N	Employed	Business	Kampala	\N	\N	\N	\N	\N	\N	\N	2020-07-04	\N	Discipleship	\N	\N	\N	Mrs.	Yes	Biyinzika		2020-10-05 09:38:19.917119+03	t	NOT-ARCHIVED	Susan Nsubuga
20	Kintu	Jenipher	Kafunda Zone	Kafunda	07856357674	m@gmail.com	avatars/Mrs_kintu.jpg	Female	Married	Church_Marriage	Degree	Employed	Self	Wakiso	Uganda	Kyandondo	Nabweru	Wakiso	Nabweru	Nabweru South	2019-12-04	2020-02-03	2019-12-30	Discipleship	\N	\N	\N	Mrs.	Yes	God is Able		2020-10-05 11:52:48.560155+03	t	NOT-ARCHIVED	Kintu Jenipher
19	Gitta	K	Lugoba Zone	Lugoba	0772194309	gitta@yahoo.com	avatars/mr_gitta_S2YUQxZ.jpg	Male	Married	Church_Marriage	Degree	Employed	Self Employed	Wakiso	Uganda	Kyadondo	Nabweru	Wakiso	Nabweru	Lugoba	2002-01-25	2020-01-27	2010-01-24	Discipleship	Mrs Edith Gitta	084794940	Lugoba	Mr.	Yes	Biyinzika	All provided	2020-10-05 11:52:48.562152+03	t	NOT-ARCHIVED	Gitta K
91	Grace	Kikansira	Bombo Rd Zone	Namalere	0772194309	kikansira@gmail.com	avatars/kikansira_grace.jpg	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Mrs.	Yes	Issachar		2020-10-05 09:38:19.951027+03	t	NOT-ARCHIVED	Grace Kikansira
43	Rose	Mukisa	Kazo Zone	Kazo	0843989490	mukisa@gmail.com	avatars/rose_mukisa.jpg	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Mrs.	Yes	Overcomers		2020-10-05 09:38:19.958009+03	t	NOT-ARCHIVED	Rose Mukisa
40	Patrick	Bbosa	Gombolola Zone	Nabweru	0857785555	bbosa@big.com	avatars/download.jpg	Male	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2020-06-10	\N	Discipleship	\N	\N	\N	Mr.	Yes	Winners		2020-10-05 09:38:19.969004+03	t	NOT-ARCHIVED	Patrick Bbosa
38	Mubiru	Tracey	Kafunda Zone	Nabweru	08958995	email@email.com	avatars/AI.jpg	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Ms.	Yes	Winners		2020-10-05 09:38:19.976204+03	t	NOT-ARCHIVED	Mubiru Tracey
33	Brian	Muwanguzi	Gombolola Zone	Nabweru	078398989r9	email@email.com	avatars/brian.jpg	Male	Married	Cohabiting	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Mr.	Yes	Victors		2020-10-05 09:38:19.990925+03	t	NOT-ARCHIVED	Brian Muwanguzi
17	Herbert	Byekwaso	Gombolola Zone	Nabweru	0778648949	byekwaso@gmail.com	avatars/mr_byekwaso.jpg	Male	Married	Church_Marriage	Degree	Employed	Software Development	Andela	Uganda	Kyandondo	Nabweru	Wakiso	Nabweru	Nabweru North	2020-01-27	2020-02-03	2004-01-25	Ushering	Cate Byekwaso	0783948489	USA	Eng.	Yes	God is Able	All info provided	2020-10-05 11:52:48.565144+03	t	NOT-ARCHIVED	Herbert Byekwaso
16	Kawombe	Harriet	Kazo Zone	Kazo	0783939393	kawombe@gmail.com	avatars/Mrs_Kawombe.jpg	Female	Married	Customary	Certificate	Employed	Self	Kampala	Uganda	Kyadondo	Maganjo	Wakiso	Nabweru	Kazo	2020-12-04	2020-12-04	2020-12-04	Discipleship	Nakato	07489848959	Kampala	Mrs.	Yes	God is Able	no more	2020-10-05 11:52:48.567139+03	t	NOT-ARCHIVED	Kawombe Harriet
7	Mukisa	Ivan	Lugoba Zone	Lugoba	074783489898489	email@email.com	avatars/w11.JPG	Male	Married	Church_Marriage	Certificate	Employed	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Orchestra	\N	\N	\N	Mr.	Yes	Winners		2020-10-05 11:52:48.582557+03	t	NOT-ARCHIVED	Mukisa Ivan
4	Nusurah	Ayebare	Katooke Zone	Lugoba	0747885989	nusu@gmail.com	avatars/Nusurah.jpg	Female	Single	Church_Marriage	Diploma	Employed	Saloon	Katooke	Uganda	Kyandondo	Nabweru	Nabweru	Nabweru	Katooke	2019-12-04	2020-01-27	2020-01-26	Worship Team	Sumayiyah	09774789	Katooke	Ms.	Yes	Overcomers		2020-10-05 11:52:48.583559+03	t	NOT-ARCHIVED	Nusurah Ayebare
2	Nabachwa	Teddy	Kafunda Zone	Nabweru	235467777777777789	email@email.com	avatars/IMG-20191224-WA0015.jpg	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Ms.	Yes	Biyinzika		2020-10-05 11:52:48.586549+03	t	NOT-ARCHIVED	Nabachwa Teddy
32	Dihfahsih	Mugoya	Kafunda Zone	Nabweru	+256751612792	dihfahsihm@gmail.com	avatars/IMG_20191210_112652.jpg	Male	Single	\N	Degree	Employed	IT	Mengo	Uganda	Central	\N	\N	\N	\N	\N	2020-06-15	\N	Discipleship	\N	\N	\N	Mr.	Yes	God is Able		2020-10-05 09:38:19.993917+03	t	NOT-ARCHIVED	Dihfahsih Mugoya
31	Brenda	Lubwama	Church Zone	Nansana	078958899	brendam@gmail.com	avatars/IMG_20200416_181015.jpg	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Mrs.	Yes	Biyinzika		2020-10-05 09:38:19.996904+03	t	NOT-ARCHIVED	Brenda Lubwama
30	Geofrey	Lubwama	Church Zone	Nansana	0376489589	email@email.com	avatars/FB_IMG_15798747303394626.jpg	Male	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Orchestra	\N	\N	\N	Mr.	Yes	Biyinzika		2020-10-05 11:52:48.540371+03	t	NOT-ARCHIVED	Geofrey Lubwama
14	Desire	Namuganyi	Kabira Zone	Nabweru	0754236758	email@email.com	avatars/desire.jpeg	Female	Married	Church_Marriage	Diploma	Unemployed	Flight Attendant	Entebbe	Uganda	Kyandondo	Nabweru	Wakiso	Nabweru	Nabweru South	1996-12-04	1996-12-04	2004-01-25	Discipleship	\N	\N	\N	Ms.	Yes	God is Able	All Provided	2020-10-05 11:52:48.571861+03	t	NOT-ARCHIVED	Desire Namuganyi
10	Yusuf	Lule	Kazo Zone	Kazo	0847887484	lule@gmail.com	avatars/26167418_570496569960970_5368404521942502125_n.jpg	Male	Married	Church_Marriage	Degree	Employed	Business	Kampala	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Mr.	Yes	Overcomers		2020-10-05 11:52:48.579353+03	t	NOT-ARCHIVED	Yusuf Lule
29	Sempijja	Jimmy	Lugoba Zone	Lugoba	07348485	email@email.com	avatars/jimmy_ZJQuQWC.jpg	Male	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Mr.	Yes	Winners		2020-10-05 11:52:48.543552+03	t	NOT-ARCHIVED	Sempijja Jimmy
9	Odeke	Mable	Lugoba Zone	Lugoba	0893478784	mable@uccbwaise.com	avatars/48967418_108314770240104_1882345597306929152_n.jpg	Female	Married	Church_Marriage	Degree	Employed	Secretary	Church	\N	\N	\N	\N	\N	\N	\N	\N	\N	Worship Team	\N	\N	\N	Mrs.	Yes	God is Able		2020-10-05 11:52:48.58035+03	t	NOT-ARCHIVED	Odeke Mable
1	Zake	Joshua	Lugoba Zone	Lugoba	07848894	uccbwaise1@gmail.com	avatars/pr_josh.jpg	Male	Married	Church_Marriage	Degree	Employed	Pastoral	Church	\N	\N	\N	\N	\N	\N	2020-02-03	2020-02-03	2020-02-03	Pastoral	\N	\N	\N	Pr.	Yes	Winners	Pr. Joshua Zake is the lead pastor of UCC Bwaise , He is married to a beautiful wife Joy Zake. He is a father of 2 girls and 2 boys.\r\n\r\nHe is also  an author of 4 Christian books, founder and vision bearer of Why Are You Alive (Lwaki Oli Mulamu)\r\nA Member of A Uganda Wit hout Orphans (AUWO)\r\n\r\nHe hosts Lwaki Oli Mulamu Radio Program on InnerMan FM 107.5 from 7:00am to 8:00am Ugandan Time every sunday.\r\n\r\nHe leads a team of dedicated  ministers at UCC Bwaise in missions of preaching why are you alive in different parts of the country.	2020-10-05 11:52:48.588545+03	t	NOT-ARCHIVED	Zake Joshua
28	Maama	Tracy	Church Zone	Nabweru	0886587958905	email@email.com	avatars/maama_tracy.jpg	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Mrs.	Yes	Victors		2020-10-05 11:52:48.54555+03	t	NOT-ARCHIVED	Maama Tracy
27	Muwanguzi	Frank	Kawaala Zone	Masanafu	0984900	email@email.com	avatars/Frank.jpg	Male	Married	Church_Marriage	\N	Employed	Furniture	Bwaise	\N	\N	\N	\N	\N	\N	\N	\N	\N	Youth Leadership	\N	\N	\N	Mr.	Yes	Winners		2020-10-05 11:52:48.546549+03	t	NOT-ARCHIVED	Muwanguzi Frank
26	Peninah	Mubulire	Kabira Zone	Nabweru	078888877	email@email.com	avatars/Mrs_peninah.jpg	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Mrs.	Yes	Biyinzika		2020-10-05 11:52:48.548542+03	t	NOT-ARCHIVED	Peninah Mubulire
41	Kayiwa	Richard	Lugoba Zone	Lugoba	0847859599	rkayiwaicea@gmail.com	avatars/de.jpg	Male	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2020-06-10	\N	Discipleship	\N	\N	\N	Mr.	Yes	Biyinzika		2020-10-05 09:38:19.965033+03	t	NOT-ARCHIVED	Kayiwa Richard
25	Mama Nabulya	Haddija	Church Zone	Nabweru	047895805	email@email.com	avatars/Maama_Nabulya.jpg	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Mrs.	Yes	God is Able		2020-10-05 11:52:48.550493+03	t	NOT-ARCHIVED	Mama Nabulya Haddija
37	Stephen	Bagyenda	Kazo Zone	Kazo	7843980493	email@email.com	avatars/tech_ug.jpg	Male	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Mr.	Yes	Biyinzika		2020-10-05 09:38:19.979954+03	t	NOT-ARCHIVED	Stephen Bagyenda
36	Sam	Kwagala	Church Zone	Nabweru	078995895	email@email.com	avatars/kwagala_sam.jpg	Male	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2020-06-09	\N	Discipleship	\N	\N	\N	Mr.	Yes	Winners		2020-10-05 09:38:19.983979+03	t	NOT-ARCHIVED	Sam Kwagala
35	Sharon	Nalubega	Kabira Zone	Nabweru	067484848	email@email.com	avatars/1_Q6NYHcg.jpg	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Ms.	Yes	Overcomers		2020-10-05 09:38:19.987929+03	t	NOT-ARCHIVED	Sharon Nalubega
24	Susan	Namyalo	Gombolola Zone	Nabweru	076365654764	susann@gmail.com	avatars/Susan.jpg	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Ms.	Yes	Victors	Am a simple lady	2020-10-05 11:52:48.552359+03	t	NOT-ARCHIVED	Susan Namyalo
23	John Bosco	Buyuki	Katooke Zone	Katooke	0847950	email@email.com	avatars/mr_buyuki.jpg	Male	Married	Church_Marriage	Degree	Employed	Business	Kampala	Uganda	Kyandondo	\N	\N	\N	\N	\N	2020-02-03	\N	Discipleship	\N	\N	\N	Mr.	Yes	Issachar		2020-10-05 11:52:48.554356+03	t	NOT-ARCHIVED	John Bosco Buyuki
22	Joshua	Mubulire	Kabira Zone	Nabweru	07347959	email@email.com	avatars/Mt_Joshua.jpg	Male	Married	Church_Marriage	Masters	Employed	Business	Kampala	Uganda	Kyandondo	Lugoba	Wakiso	Nabweru	Nabweru South	2020-01-27	2020-01-27	2019-12-30	Discipleship	Mr.Peninah	0748850	Nabweru	Mr.	Yes	Winners	Nothing More	2020-10-05 11:52:48.556349+03	t	NOT-ARCHIVED	Joshua Mubulire
21	Nalongo	Joan	Gombolola Zone	Nabweru	478947484993	email@email.com	avatars/Nalongo_Joan.jpg	Female	Single	\N	Degree	Employed	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Discipleship	\N	\N	\N	Ms.	Yes	Winners		2020-10-05 11:52:48.558343+03	t	NOT-ARCHIVED	Nalongo Joan
11	Posiano	Zakumumpa	Church Zone	Mukono	0745367889	email@email.com	avatars/pr.posian.JPG	Male	Married	Church_Marriage	Certificate	Employed	Business	Mukono	\N	\N	\N	\N	\N	\N	\N	\N	\N	Pastoral	\N	\N	\N	Pr.	Yes	Issachar	Vision: ΓÇ£Discovering and Doing GodΓÇÖs willΓÇ¥ which is accomplished with the help of a Church Mission ΓÇô ΓÇ£Lwaki oli mulamuΓÇ¥ (why are you alive) Teach Me To do your will, for you are my God(Psalms 143:10).(John 18:37)\r\n\r\nUnited Christian Centre Bwaise (UCC BWAISE) is a born again Christian church in Kampala Uganda East Africa.\r\nThe church is located on Bwaise ΓÇô Nabweru road The lead pastor isPr. Joshua Zake ministering with a team of other associate pastors namely;\r\nPr. Sande Posiano Zakumumpa\r\nPr. Henry Musubize\r\nPr. Sanyu Rebecca\r\nand other preachers of the word including the following\r\nMr. Mukisa Kintu\r\nMr. John Bosco Buyuki\r\nMr. Charles Bunjo\r\nMr. Kasirye Eddie	2020-10-05 11:52:48.577359+03	t	NOT-ARCHIVED	Posiano Zakumumpa
92	Joy	Zake	Lugoba Zone	Lugoba	0789499589	joy@gmail.com	avatars/joy_zake.jpg	Female	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2020-06-19	\N	Discipleship	\N	\N	\N	Mrs.	Yes	God is Able		2020-10-05 09:38:19.947078+03	t	NOT-ARCHIVED	Joy Zake
96	Wataka	Andrew	Kafunda Zone	Kafunda	0784948474	dihfahsihm@gmail.com	avatars/wataka_andrew.jpg	Male	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2020-06-19	\N	Discipleship	\N	\N	\N	Mr.	Yes	God is Able		2020-10-05 09:38:19.943053+03	t	NOT-ARCHIVED	Wataka Andrew
97	Ssembirige	Esther	Church Zone	Nabweru	0748983	dihfahsihm@gmail.com	avatars/mirembe.jpg	Female	Married	Church_Marriage	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2020-06-19	\N	Discipleship	\N	\N	\N	Mrs.	Yes	God is Able		2020-10-05 09:38:19.94006+03	t	NOT-ARCHIVED	Ssembirige Esther
18	Ronald	Mukisa	Kafunda Zone	Kafunda	089795498	email@email.com	avatars/mr_kintu.jpg	Male	Married	Church_Marriage	Degree	Employed	Teaching	Wakiso	Uganda	Kyandondo	Nabweru	Wakiso	Nabweru	Nabweru South	2019-12-04	2020-01-27	2020-01-27	Pastoral	Mrs Kintu	08347875490	Nabweru	Pr.	Yes	Issachar	Vision: ΓÇ£Discovering and Doing GodΓÇÖs willΓÇ¥ which is accomplished with the help of a Church Mission ΓÇô ΓÇ£Lwaki oli mulamuΓÇ¥ (why are you alive) Teach Me To do your will, for you are my God(Psalms 143:10).(John 18:37)\r\nMission: " Lwaki Oli Mulamu(Why are you alive)"\r\nThis mission is accomplished by broadcasting on Christian radio with a program running on Innerman fm every Sunday morning at 7 ΓÇô 8 am Uganda time .this frequency is also accessible online by app ΓÇô InnerMan2 fm\r\n\r\nUnited Christian Centre Bwaise (UCC BWAISE) is a born again Christian church in Kampala Uganda East Africa.\r\nThe church is located on Bwaise ΓÇô Nabweru road The lead pastor isPr. Joshua Zake ministering with a team of other associate pastors namely;\r\nPr. Sande Posiano Zakumumpa\r\nPr. Henry Musubize\r\nPr. Sanyu Rebecca\r\nand other preachers of the word including the following\r\nMr. Mukisa Kintu\r\nMr. John Bosco Buyuki\r\nMr. Charles Bunjo\r\nMr. Kasirye Eddie	2020-10-05 11:52:48.564148+03	t	NOT-ARCHIVED	Ronald Mukisa
13	Rebecca	Sanyu Mirembe	Church Zone	Kasubi	0752678794	email@email.com	avatars/pr_sanyu.JPG	Female	Single	\N	Certificate	Unemployed	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	Pastoral	\N	\N	\N	Pr.	Yes	Victors	Vision: ΓÇ£Discovering and Doing GodΓÇÖs willΓÇ¥ which is accomplished with the help of a Church Mission ΓÇô ΓÇ£Lwaki oli mulamuΓÇ¥ (why are you alive) Teach Me To do your will, for you are my God(Psalms 143:10).(John 18:37)\r\nMission: " Lwaki Oli Mulamu(Why are you alive)"\r\nThis mission is accomplished by broadcasting on Christian radio with a program running on Innerman fm every Sunday morning at 7 ΓÇô 8 am Uganda time .this frequency is also accessible online by app ΓÇô InnerMan2 fm\r\n\r\nUnited Christian Centre Bwaise (UCC BWAISE) is a born again Christian church in Kampala Uganda East Africa.\r\nThe church is located on Bwaise ΓÇô Nabweru road The lead pastor isPr. Joshua Zake ministering with a team of other associate pastors namely;\r\nPr. Sande Posiano Zakumumpa\r\nPr. Henry Musubize\r\nPr. Sanyu Rebecca\r\nand other preachers of the word including the following\r\nMr. Mukisa Kintu\r\nMr. John Bosco Buyuki\r\nMr. Charles Bunjo\r\nMr. Kasirye Eddie	2020-10-05 11:52:48.573365+03	t	NOT-ARCHIVED	Rebecca Sanyu Mirembe
\.


--
-- Data for Name: dashboard_ministry; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_ministry (id, name, details, photos, leader_id, "Is_View_on_Web") FROM stdin;
2	Building Ministry	more details	avatars/IMG-20200428-WA0000.jpg	22	Yes
1	Youth Ministry	Youths of UCC Bwaise of ages between\r\n18 and 45	avatars/IMG-20191224-WA0007_YzrDmcX.jpg	2	Yes
3	Sunday School Ministry	Children Ministry	avatars/sunday_school.jpg	21	Yes
4	Teens Ministry	All children below twelve years of age	avatars/teens.jpg	38	Yes
5	Ochestra Ministry	Church Musical instruments	avatars/ochestra.jpg	7	Yes
6	Member's Welfare	Okulabula ba members ba UCC Bwaise okumanya nga bwe bali.	avatars/maxresdefault_KbRfE2m.jpg	41	Yes
\.


--
-- Data for Name: dashboard_newconvert; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_newconvert (id, is_church_member, born_again_before, "First_Name", "Second_Name", "Telephone", "Date_Of_Salvation", member_name_id) FROM stdin;
2	No	No	James	Seth	0772194309	2020-09-24	\N
1	Yes	No	\N	\N	\N	2020-09-23	100
3	No	No	John	Teddy	+256751612792	2020-09-28	\N
\.


--
-- Data for Name: dashboard_news; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_news (id, news_title, date, image, news, "Is_View_on_Web", author, audio_file) FROM stdin;
1	Women's Day	2020-02-05	images/w17.JPG	Enjoying great taste of food	Yes	2	\N
2	Foot Ball Team	2020-02-05	images/football_xnTRfPN.jpg	Ready for sports activities	Yes	2	\N
3	Inspecting New Church Building	2020-02-05	images/build2.jpg	The saints led by the building committee chairman, inspected the new church structure	Yes	2	\N
4	CHURCH MISSION  ΓÇÿΓÇÿWHY ARE YOU ALIVEΓÇÖΓÇÖ	2020-02-06	images/IMG_3487_37EkVRQ.JPG	Introduction \r\nThis is a very fundamental question in our lives. It deals with the reason why someone is in existence. It is important for each one of us to discover why they are alive. So many people have failed to discover the purpose of their lives and many have actually come to the end of their ΓÇÿjourneysΓÇÖ without getting the slightest idea of why they ever lived.\r\nThe scriptures teach us that the of spirit ΓÇ£mankindΓÇ¥ existed long before the creation of the world.\r\nThe creation of mankind happened in the eternity before God created any other thing in the physical world.\r\nWisdom  who is Christ , in Proverbs tell the story of what happened before the physical world was created - Prov 8:22  \r\nAs Christ tell the story he tells us of his moments with mankind in Spiritual world before the physical world was created \r\nVerse 31 ΓÇ£Rejoicing in the habitable part of his earth; and my delights were with the sons of menΓÇ¥.\r\n\r\nThe Psalmist through the prayer of Moses also reveals that spirit of mankind lived with God long before coming to the earth. \r\n\r\n ΓÇ£A Prayer of Moses the man of God. Lord, thou hast been our dwelling place in all generationsΓÇ¥. Psalms 90:1	Yes	1	\N
5	HOW DO WE DISCOVER GODΓÇÖS WILL	2020-02-13	images/IMG_3528.JPG	Each one of us was given a divine mission and God has a purpose for each one that is different from any other personΓÇÖs. However, many people are unable to walk according to GodΓÇÖs divine calendar. \r\nDiscovering GodΓÇÖs will is very vital because it enables us to know what He wants us to do and what He does not want us to do. The Bible states that ΓÇ£ItΓÇÖs GodΓÇÖs privilege to conceal things and the kingΓÇÖs privilege to discover them.ΓÇ¥Prov25:2\r\nItΓÇÖs a challenge for everyone who really wants to live for God and not for themselves to seek to discover GodΓÇÖs will. GodΓÇÖs will can be discovered in several ways including; \r\n∩âÿ\tNow that GodΓÇÖs will is not obvious to many people, there isnΓÇÖt any of us upon whom God doesnΓÇÖt have purpose! It leaves us with a challenge which we must solve ΓÇô why am I alive?\r\n∩âÿ\tOur God communicates to us in many ways now that our understanding and perception is also diverse; some easily understand by hearing once and several time while others do by seeing, yet others need both.  \r\n∩âÿ\tGod communicates to us in several ways as he shares with us his heart though many times we still do not understand but that doesnΓÇÖt stop his endeavours\r\n∩âÿ\tIt makes this communication easy if the one he is communicating to is very interested and therefore anxious or even attentive ΓÇô 1Sam 3:1-9\r\n∩âÿ\tWe can therefore know his will through some of the following ways;-	Yes	Admin	\N
6	WAYS OF DISCOVERING GOD'S WILL	2020-02-13	images/IMG_3489.JPG	∩ü╢\tPrayer; \r\n-\tTo us prayer is all about letting God know what we need, well some of the scriptures about prayer when read will give you this view. However when you read one that says before we pray he already knows what we need (Mat.6:7- 8), a question comes to mind why then pray?\r\n-\tPrayer times before God could be a moment when God gets our attention with an attitude we are going to let God know what we need, yet he is also ready to share his will with us now that in such times we are focused and attentive \r\n-\tMat.17:1 ΓÇô mountain of transfiguration they was a two way communication\r\n-\tExod.3:3 - Moses by the burning bushΓÇªI will go over and seeΓÇªΓÇ¥\r\n-\tPrayer is ΓÇ£two way trafficΓÇ¥. During prayer God speaks back and reveals His will to someone in a particular area of their concern. . \r\n∩ü╢\tRevelation; \r\n-\tThis is to disclose, to enlighten or illuminate\r\n-\tGod sometimes uses dreams when revealing to us his will\r\n-\tMany times God communicates to mankind through visions and dreams as he reveals his heart. Examples of people that God spoke to in dreams and visions include Joseph, Paul, Jeremiah, David, Peter e.t.c. \r\n-\tEph.1: 17 -18 -  That the God of our Lord Jesus Christ, the Father of glory, may give unto you the spirit of wisdom and revelation in the knowledge of him:\r\n18 The eyes of your understanding being enlightened; that ye may know what is the hope of his calling, and what the riches of the glory of his inheritance in the saints,\r\n-\tRoms 11:8-10 -   (According as it is written, God hath given them the spirit of slumber, eyes that they should not see, and ears that they should not hear;) unto this day.\r\n9 And David saith, Let their table be made a snare, and a trap, and a stumblingblock, and a recompence unto them:\r\n10 Let their eyes be darkened, that they may not see, and bow down their back alway.\r\n-\tLuk.24:16, 31 -   But their eyes were holden that they should not know him\r\nVs.31 -  And their eyes were opened, and they knew him; and he vanished out of their sight.\r\n-\tProv.25:2 -  It is the glory of God to conceal a thing: but the honour of kings is to search out a matter\r\n∩ü╢\tDeut.29:29 -  The secret things belong unto the LORD our God: but those things which are revealed belong unto us and to our children for ever, that we may do all the words of this law \r\n\r\n∩ü╢\tConviction of the heart.- This is one of the most common ways by which God makes his will known to mankind. Conviction is easy because it involves ones heart yet some of the other ways are somehow difficult because one has to be concentrated in order to know GodΓÇÖs will. It becomes even easier if one has got a heart of flesh and not aΓÇ¥ strong heartΓÇ¥. ΓÇ£I will give you a new heart and put a new spirit in you: I will remove from you your heart of stone and give you a heart of fresh. And I will put my spirit in you and move you to follow my decree and be care free to keep my laws. ΓÇ£Ezekiel 36:26-27\r\n\r\nA heart of flesh is one that easily melts when God moves it which is unlike for a strong one.\r\nGod can put it upon ones heart to do something as the case was for Nehemiah ΓÇ£ I went to Jerusalem, and after staying there three days I set out during the night with a few men. I had not told anyone what my God had put in my heart to do for Jerusalem. There were no mounts with me except the one I was riding on.ΓÇ¥ Nehemiah: 2:11-12  \r\n∩ü╢\tGodΓÇÖs Word; \r\n∩éº\tThrough GodΓÇÖs written word or ΓÇ£LOGOSΓÇ¥; \r\n∩éº\t2Timothy 3:16 - All scripture [is] given by inspiration of God, and [is] profitable for doctrine, for reproof, for correction, for instruction in righteousness:\r\n \r\n-\tEven when Christ came into this world, he did GodΓÇÖs will by living according to scriptures\r\n-\tLuke 4:21 And he began to say unto them, This day is this scripture fulfilled in your ears.\r\n-\tJohn 19:28 After this, Jesus knowing that all things were now accomplished, that the scripture might be fulfilled, saith, I thirst.\r\n\r\n-\tJohn 19:36 For these things were done, that the scripture should be fulfilled, A bone of him shall not be broken.\r\n\r\n-\tJohn 19:37 And again another scripture saith, They shall look on him whom they pierced.\r\n\r\n-\tJohn 20:9 For as yet they knew not the scripture, that he must rise again from the dead.\r\n-\t\r\n∩éº\tThrough GodΓÇÖs spoken word or ΓÇ£RHEMAΓÇ¥; \r\n∩éº\tThrough prophesies; \r\n∩éº\tThrough Word of knowledge (according to Isaiah 34:16 the word of God has every detail Ezekiel 3:1- eats the scroll and Jeremiah 15:16 - also ate GodΓÇÖs word.\r\n∩éº\tThrough leaders; God puts us under someone for a purpose and He expects us to submit under that authority. He uses such leaders to groom us into the people that He wants us to be. So God can communicate to people through their leaders. For example God used Moses and Joshua to communicate to the Israelites as He used Paul to speak to Timothy. Deuteronomy 34:9 and 1Timothy 4:14 respectively. \r\n\r\n\r\n∩ü╢\tTendencies and repeated challenges facing you\r\n-\tThere are things in life that one feels a concern and such a unique care about which is not the same case with other people.\r\n-\tOne may even try to draw the attention of other people to the same concern when for them they do not realise anything as related to issue of concern.\r\n-\t This personal concern many times is a message from God making the specific person notice that need so as to do something about it and so obey the heart of God by doing his will.\r\n-\tSometimes the attraction may even be annoying yet itΓÇÖs what God wants you to correct or do something about.\r\n-\tSome of these concerns are seasonal yet others are part of oneΓÇÖs life ΓÇô itΓÇÖs a sign that one is wired accordingly.\r\n-\tThis tendency is like putting a responsibility upon yourself when everyone else is mindless or silent about something ΓÇô no one chooses you but you choose yourself.\r\n-\tPeter always did this probably little did he know he was later to be a leader , a man of responsibility\r\n∩âÿ\tMat.16:18 ΓÇô Simon peter answers ΓÇ£ you are the ChristΓÇ¥\r\n∩âÿ\tMatthew 14:28 And Peter answered him and said, Lord, if it be thou, bid me come unto thee on the water.\r\n∩âÿ\tMatthew 19:27 Then answered Peter and said unto him, Behold, we have forsaken all, and followed thee; what shall we have therefore?\r\n∩âÿ\tMatthew 26:58 But Peter followed him afar off unto the high priest's palace, and went in, and sat with the servants, to see the end.\r\n∩âÿ\tMatthew 16:22 Then Peter took him, and began to rebuke him, saying, Be it far from thee, Lord: this shall not be unto thee.\r\n∩âÿ\tMark 9:5 And Peter answered and said to Jesus, Master, it is good for us to be here: and let us make three tabernacles; one for thee, and one for Moses, and one for Elias.\r\n\r\nAs  we endeavour to discover and do GodΓÇÖs will, when one asks oneself this question ΓÇ£why are you aliveΓÇ¥  it helps very much in refocusing back to roots which is the heart of God where we find the blue print of every oneΓÇÖs divine purpose of creation on this planet.	Yes	PR. Joshua Zake	\N
7	Testing	2020-06-11	images/1_ZKdQ3gZ.jpg	it worked	Yes	Pastor Tester	audios/Mp3jaja.com_Music_Butamanya_-_Coopy_Bly.mp3
8	Test2	2020-06-11	images/tithes.JPG	Testing mode	Yes	Test Again	audios/Abatarina_mukama_-_Bugembe.mp3
\.


--
-- Data for Name: dashboard_page; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_page (id, page_location, page_title, page_description, page_image) FROM stdin;
1	Header	Sports	UCC BwaiseFootball Team	images/football.jpg
2	Footer	About	Footer Info	images/2_wm6fyXk.jpg
\.


--
-- Data for Name: dashboard_pledgeitem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_pledgeitem (id, "Date", "Item_That_Needs_Pledges", "Amount_Needed", "Pledge_Deadline", "Archived_Status") FROM stdin;
25	2020-07-20	Renovaton	200000	2020-07-29	Archived
26	2020-10-06	Helping the needy	100000	2020-10-30	NOT-ARCHIVED
\.


--
-- Data for Name: dashboard_pledges; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_pledges (id, "Status", "Date", "Amount_Pledged", "Amount_Paid", "Balance", "Pledge_Made_By_id", "Reason_id", "Archived_Status", "PledgeItem", "Pledge_Made_By_Visitor_id", is_church_member, "AmountBeingPaid", "DateOfPayment", "NameOfPledgee") FROM stdin;
124	UNPAID	2020-10-04	20000	0	20000	29	26	NOT-ARCHIVED	\N	\N	YES	0	\N	\N
118	PARTIAL	2020-07-20	100000	64000	36000	9	25	NOT-ARCHIVED	\N	\N	YES	0	\N	\N
117	PAID	2020-07-20	100000	100000	0	\N	25	NOT-ARCHIVED	\N	1	NO	0	\N	\N
116	PAID	2020-07-20	10000	10000	0	10	25	ARCHIVED	\N	\N	YES	0	\N	\N
123	\N	\N	0	0	\N	\N	\N	NOT-ARCHIVED	Helping the needy	\N	YES	5000	2020-10-11	Susan Namyalo
119	\N	\N	0	0	\N	\N	\N	NOT-ARCHIVED	\N	\N	YES	0	\N	\N
120	\N	\N	0	0	\N	\N	\N	NOT-ARCHIVED	\N	\N	YES	10000	2020-07-21	Odeke Mable
121	\N	\N	0	0	\N	\N	\N	NOT-ARCHIVED	Renovaton	\N	YES	4000	2020-07-22	Odeke Mable
122	PARTIAL	2020-10-04	10000	5000	5000	24	26	NOT-ARCHIVED	\N	\N	YES	0	\N	\N
\.


--
-- Data for Name: dashboard_pledgescashedout; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_pledgescashedout (id, "Date", "Item_Id", "Amount_Needed", "Amount_Cashed_Out", "Item_That_Needs_Pledges") FROM stdin;
14	2020-07-22	25	200000	20000	Renovaton
15	2020-10-05	26	100000	1000	Helping the needy
\.


--
-- Data for Name: dashboard_project; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_project (id, project_title, start_date, image, project_description, "Is_View_on_Web", project_leader_id) FROM stdin;
1	Church Hall	2020-05-04	images/IMG-20200428-WA0000_xU5vwHs.jpg	iuiwufihojieroj owvoinonoevpp	Yes	19
2	Church Cathedral	2020-06-06	images/build3_q2o3hwC.jpg	Church cathedral details	Yes	29
\.


--
-- Data for Name: dashboard_revenues; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_revenues (id, "Date", "Service", "Amount", "Archived_Status", "Revenue_filter", "Member_Name_id", "Other_Sources", "Other_Notes") FROM stdin;
85	2020-07-04	Unspecified Service	120000	ARCHIVED	tithes	20	\N	\N
84	2020-07-03	Unspecified Service	100000	ARCHIVED	tithes	9	\N	\N
83	2020-06-24	Unspecified Service	100	ARCHIVED	tithes	14	\N	\N
82	2020-06-23	Unspecified Service	100000	ARCHIVED	tithes	14	\N	\N
81	2020-06-19	\N	1200000	ARCHIVED	others	\N	donation	\N
79	2020-06-17	Youth Service	200000	ARCHIVED	tithes	29	\N	\N
78	2020-06-18	Unspecified Service	23000	ARCHIVED	build	\N	\N	Church Hall
77	2020-06-08	Wednesday Service	1000	ARCHIVED	build	\N	\N	Church Hall
76	2020-06-08	Youth Service	12000	ARCHIVED	tithes	7	\N	\N
112	2020-09-28	Sunday First Service	36000	NOT-ARCHIVED	tithes	100	\N	\N
113	2020-10-09	Home Cell Service	200000	NOT-ARCHIVED	build	\N	\N	New Church
111	2020-09-28	Sunday First Service	200000	ARCHIVED	tithes	32	\N	\N
110	2020-02-20	Friday Overnight	10000	ARCHIVED	tithes	92	\N	\N
109	2020-07-30	Sunday First Service	500000	ARCHIVED	tithes	14	\N	\N
108	2020-08-10	\N	23450	ARCHIVED	others	\N	<script>alert('hello')</script>	\N
107	2020-08-10	\N	10000	ARCHIVED	others	\N	Hello, <script>alert('hello')</script>	\N
106	2020-08-10	Home Cell Service	230000	ARCHIVED	tithes	17	\N	\N
105	2020-08-03	Sunday First Service	200000	ARCHIVED	tithes	100	\N	\N
104	2020-08-08	Home Cell Service	10000	ARCHIVED	tithes	27	\N	\N
103	2020-07-30	Friday Overnight	75000	ARCHIVED	build	\N	\N	church renovation
102	2020-07-30	Friday Overnight	100000	ARCHIVED	thanks	17	\N	\N
101	2020-07-30	\N	100000	ARCHIVED	others	\N	Ivan and the wife Baptism and thanks giving	\N
100	2020-07-30	Sunday Second Service	180000	ARCHIVED	seeds	20	\N	\N
99	2020-07-30	Sunday First Service	500000	ARCHIVED	tithes	14	\N	\N
98	2020-07-30	Wednesday Service	100000	ARCHIVED	offering	\N	\N	\N
92	2020-02-20	Unspecified Service	100000	ARCHIVED	build	\N	\N	for construction
91	2020-07-20	Bible Study Service	17400	ARCHIVED	tithes	98	\N	\N
90	2020-02-20	Youth Service	10000	ARCHIVED	tithes	35	\N	\N
89	2020-07-13	Youth Service	10000	ARCHIVED	build	\N	\N	New Church
88	2020-07-13	Youth Service	10000	ARCHIVED	build	\N	\N	New Church
87	2020-07-04	Sunday Third Service	20000	ARCHIVED	tithes	99	\N	\N
86	2020-07-04	Home Cell Service	200000	ARCHIVED	build	\N	\N	for building new cathedral
\.


--
-- Data for Name: dashboard_salariespaid; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_salariespaid (id, "Salary_Id", "Name", "Salary_Amount", "Month_being_cleared", "Date_of_paying_salary", "Archived_Status") FROM stdin;
7	7	Mukisa Ivan	5000	2020-06-01	2020-06-08	NOT-ARCHIVED
8	3	Good Man	50000	2020-06-01	2020-06-16	NOT-ARCHIVED
9	3	Good Man	50000	2020-06-01	2020-06-23	NOT-ARCHIVED
10	15	Upendo Flistar	60000	2020-06-01	2020-06-23	NOT-ARCHIVED
13	7	Mukisa Ivan	50000	2020-06-01	2020-07-04	ARCHIVED
14	3	Good Man	50000	2020-07-01	2020-07-04	NOT-ARCHIVED
15	3	Good Man	50000	2020-06-01	2020-01-07	NOT-ARCHIVED
16	3	Good Man	50000	2020-01-07	2020-01-07	NOT-ARCHIVED
17	15	Upendo Flistar	60000	2020-07-09	2020-07-09	NOT-ARCHIVED
18	3	Good Man	50000	2020-07-01	2020-07-30	NOT-ARCHIVED
19	7	Mukisa Ivan	50000	2020-08-01	2020-08-03	NOT-ARCHIVED
\.


--
-- Data for Name: dashboard_slider; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_slider (id, slider_image, image_title, modified) FROM stdin;
1	sliders/w7.JPG	When daddy and mummy are hugging - Wow	2020-02-13 14:15:45.176+03
11	sliders/IMG_3526.JPG	What a warm hug from the Admin to his wife.	2020-02-08 13:51:42.915+03
12	sliders/IMG_3523.JPG	What a smile from this Couple	2020-02-05 21:07:06.688+03
13	sliders/IMG_3517.JPG	Ivan and His wonderful Wife	2020-02-05 21:08:14.447+03
14	sliders/IMG_3514.JPG	Hugging has never been this passionate	2020-02-05 21:09:11.555+03
15	sliders/w10.JPG	It seems it was an awhile hug, so passionate	2020-02-13 14:16:59.879+03
16	sliders/w20.JPG	Kanzu are not for only burial and kwanjula, So smart	2020-02-13 14:18:24.998+03
18	sliders/IMG_3520.JPG	My husband is the most handsome guy, she says	2020-02-13 14:21:02.178+03
19	sliders/w8.JPG	He never expected it!, that was incredible	2020-02-13 14:30:02.744+03
21	sliders/w14.JPG	Perfect Joy, When you see couples hugging each other!	2020-02-22 02:34:07.533761+03
20	sliders/IMG_3478.JPG	Enjoying the goodness of the Lord	2020-09-02 16:21:41.95242+03
22	sliders/women1.JPG	Pure joy and happiness	2020-09-02 16:28:31.979562+03
17	sliders/w21.JPG	God refurbishes us	2020-09-02 16:33:26.981597+03
\.


--
-- Data for Name: dashboard_staffdetails; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_staffdetails (id, "UCC_Bwaise_Member", "First_Name", "Second_Name", "Gender", "Date_Of_Birth", "Education_Level", "Residence", "Telephone", "Photo", "Faith", "Date_of_paying_salary", "Month_being_cleared", "Salary_Amount", "Role", "Date_of_employment", "End_of_contract", "Church_Member_id", "Is_View_on_Web") FROM stdin;
1	Yes	\N	\N	\N	\N	\N	\N	\N		\N	\N	\N	50000	Security	2020-02-08	2020-02-09	7	Yes
2	Yes	\N	\N	\N	\N	\N	\N	\N		\N	\N	\N	60000	Church-Welfare	2020-03-09	2020-04-10	15	Yes
3	No	Good	Man	Male	2020-06-16	Certificate	Nabweru	0772194309	avatars/django.png	Others	\N	\N	100000	Security	2020-06-17	2020-07-11	\N	Yes
\.


--
-- Data for Name: dashboard_testing; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_testing (id, name, slug) FROM stdin;
\.


--
-- Data for Name: dashboard_theme; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_theme (id, name, colour, is_active) FROM stdin;
1	red	#e80000	No
5	deep-pink	#FF1493	No
8	light-sea-green	#20B2AA	No
2	navy-blue	#001f67	No
11	medium-purple	#9370DB	No
13	rebecca-purple	#663399	No
9	lime-green	#32CD32	No
15	trinidad	#CC4F26	No
6	dodger-blue	#1E90FF	No
16	umber	#745D0B	No
4	black	#23282d	No
7	jazzberry-jam	#9F134E	No
14	slate-gray	#2A3F54	Yes
10	maroon	#800000	No
12	radical-red	#FB2E50	No
3	dark-orange	#FF8C00	No
\.


--
-- Data for Name: dashboard_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_user (id, password, last_login, email, username, "Role", is_active, is_staff, is_superuser, full_name_id, "Is_View_on_Web") FROM stdin;
20	pbkdf2_sha256$150000$eGLURjVsHcGS$Bu74VoXCwO5FQC/r2bV9V1iaCnw9kYH7GT/QV4VzbW8=	\N	dihfahsihm@gmail.com	itsupport	SuperAdmin	t	f	f	32	Yes
22	pbkdf2_sha256$150000$unc6pMf9z1Pb$MkF1Q8TbR0bgUjTJDheAdQU4XfPau1X004djjqX9YUA=	\N	gitta@yahoo.com	assadmin	Assistant_Admin	t	f	f	19	Yes
23	pbkdf2_sha256$150000$a946qFnbi9cC$dPwL1d9f+3XH3Co0V557ntysk2yimJwy315xB7T0ez4=	2020-10-04 21:25:27.679691+03	susann@gmail.com	secretary	Secretary	t	f	f	24	Yes
21	pbkdf2_sha256$150000$5ghcPuVlar7g$rbqGGmWTiUqh/BqtiTabJr7wRyrAv3A6xTx7qRSqIhU=	\N	lule@gmail.com	uccadmin	Admin	t	f	f	10	Yes
2	pbkdf2_sha256$150000$8BT7zmbSWbni$CN5XAM/aPMp7QstZsTt4eFLvBMpvtJY3lMKAFAPd92w=	2020-09-28 16:19:22.070824+03	uccbwaise1@gmail.com	superadmin	SuperAdmin	t	t	t	1	Yes
24	pbkdf2_sha256$150000$wgvE3eJ6mFv6$3awXPqnK7gHbFBGWfaN+6wxeHDuuFNtoF0wixs2Lc/c=	2020-10-04 21:55:34.095374+03	email@email.com	desire	Ordinary	t	f	f	14	Yes
\.


--
-- Data for Name: dashboard_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: dashboard_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: dashboard_visitors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dashboard_visitors (id, "Photo", "First_Name", "Second_Name", "Address", "Telephone", "Church", "Date") FROM stdin;
1		Christoper	Ssemakula	Mukono	076347784	UCC Mukono	2020-02-20
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
5	2020-02-07 09:40:03.814+03	1	Contact object (1)	3		44	2
10	2020-02-18 21:06:53.126268+03	6	hhdfj	2	[{"changed": {"fields": ["Date"]}}]	45	2
11	2020-02-18 21:07:24.978349+03	5	fr	2	[{"changed": {"fields": ["Date"]}}]	45	2
12	2020-02-18 21:33:21.766577+03	4	dfghjkl	2	[{"changed": {"fields": ["archivedyear"]}}]	45	2
13	2020-02-18 21:34:12.826938+03	1	Building the house of God	2	[]	45	2
14	2020-02-19 13:16:55.977248+03	1	Jonah Kisaktye	2	[{"changed": {"fields": ["Archived_Status"]}}]	46	2
15	2020-02-19 13:31:58.168691+03	2	UNSWC	2	[{"changed": {"fields": ["Archived_Status"]}}]	46	2
16	2020-02-19 16:56:37.303506+03	9	Jonah	2	[{"changed": {"fields": ["Reason_filtering"]}}]	46	2
17	2020-02-19 16:56:55.01013+03	8	Sam	2	[{"changed": {"fields": ["Reason_filtering"]}}]	46	2
18	2020-02-19 23:12:53.105696+03	2	2020-03-03	2	[{"changed": {"fields": ["Archived_Status"]}}]	47	2
19	2020-02-20 10:23:53.108814+03	6	2020-02-20	2	[{"changed": {"fields": ["Archived_Status"]}}]	47	2
20	2020-02-20 10:23:59.611417+03	5	2020-02-20	2	[{"changed": {"fields": ["Archived_Status"]}}]	47	2
21	2020-02-20 10:25:20.862059+03	6	2020-02-20	2	[{"changed": {"fields": ["Archived_Status"]}}]	47	2
22	2020-02-20 11:20:50.59744+03	6	2020-02-20	2	[{"changed": {"fields": ["Archived_Status"]}}]	47	2
23	2020-02-20 11:21:24.094848+03	6	2020-02-20	2	[]	47	2
24	2020-02-20 12:39:02.593822+03	12	2020-02-20	2	[{"changed": {"fields": ["Archived_Status"]}}]	47	2
25	2020-02-20 13:59:43.016199+03	13	2020-02-17	2	[{"changed": {"fields": ["Archived_Status"]}}]	47	2
26	2020-02-20 22:23:04.081287+03	17	allowance	2	[{"changed": {"fields": ["Archived_Status"]}}]	46	2
27	2020-02-21 00:17:16.251717+03	17	allowance	2	[{"changed": {"fields": ["Archived_Status"]}}]	46	2
28	2020-02-21 13:34:13.285776+03	6	main	2	[{"changed": {"fields": ["Archived_Status"]}}]	46	2
29	2020-02-21 13:34:26.422242+03	5	main	2	[{"changed": {"fields": ["Archived_Status"]}}]	46	2
30	2020-03-03 23:32:50.450792+03	12	Building2	3		10	2
31	2020-03-03 23:32:50.503209+03	11	Radio Program	3		10	2
32	2020-03-03 23:32:50.508198+03	10	Orphans	3		10	2
33	2020-03-03 23:32:50.512183+03	6	Building	3		10	2
34	2020-03-04 00:36:00.038443+03	25	NOT-ARCHIVED	2	[{"changed": {"fields": ["Archived_Status"]}}]	26	2
35	2020-03-04 00:36:40.413968+03	21	ARCHIVED	3		26	2
36	2020-03-04 00:37:16.889033+03	24	ARCHIVED	3		26	2
37	2020-03-04 00:37:16.902205+03	23	ARCHIVED	3		26	2
38	2020-03-04 00:37:16.905006+03	22	ARCHIVED	3		26	2
39	2020-03-04 00:37:16.907937+03	20	ARCHIVED	3		26	2
40	2020-03-04 00:37:16.910928+03	19	ARCHIVED	3		26	2
41	2020-03-04 00:37:16.915919+03	18	ARCHIVED	3		26	2
42	2020-03-04 00:37:16.919908+03	17	ARCHIVED	3		26	2
43	2020-03-04 00:37:16.922978+03	14	ARCHIVED	3		26	2
44	2020-03-04 00:37:16.9259+03	13	ARCHIVED	3		26	2
45	2020-03-04 00:37:16.928491+03	12	ARCHIVED	3		26	2
46	2020-03-04 00:37:16.93148+03	11	ARCHIVED	3		26	2
47	2020-03-04 00:37:16.93547+03	10	ARCHIVED	3		26	2
48	2020-03-04 00:37:16.938461+03	9	ARCHIVED	3		26	2
49	2020-03-04 00:37:16.941488+03	8	ARCHIVED	3		26	2
50	2020-03-04 00:37:16.943548+03	7	ARCHIVED	3		26	2
51	2020-03-04 00:37:16.946437+03	6	ARCHIVED	3		26	2
52	2020-03-04 00:37:16.94943+03	5	ARCHIVED	3		26	2
53	2020-03-04 21:23:32.140657+03	13	Building	2	[{"changed": {"fields": ["Archived_Status"]}}]	10	2
54	2020-03-06 18:39:30.264314+03	9	PaidPledges object (9)	3		27	2
55	2020-03-06 18:39:53.137162+03	23	PaidPledges object (23)	3		27	2
56	2020-03-06 18:39:53.147133+03	22	PaidPledges object (22)	3		27	2
57	2020-03-06 18:39:53.150125+03	21	PaidPledges object (21)	3		27	2
58	2020-03-06 18:39:53.152223+03	20	PaidPledges object (20)	3		27	2
59	2020-03-06 18:39:53.155161+03	19	PaidPledges object (19)	3		27	2
60	2020-03-06 18:39:53.157195+03	18	PaidPledges object (18)	3		27	2
61	2020-03-06 18:39:53.160099+03	17	PaidPledges object (17)	3		27	2
62	2020-03-06 18:39:53.162093+03	16	PaidPledges object (16)	3		27	2
63	2020-03-06 18:39:53.164195+03	15	PaidPledges object (15)	3		27	2
64	2020-03-06 18:39:53.166296+03	13	PaidPledges object (13)	3		27	2
65	2020-03-06 18:39:53.168123+03	12	PaidPledges object (12)	3		27	2
66	2020-03-06 18:39:53.170168+03	10	PaidPledges object (10)	3		27	2
67	2020-03-13 14:45:08.255128+03	3	CashFloat object (3)	2	[{"changed": {"fields": ["Date"]}}]	49	2
68	2020-04-26 14:07:18.885482+03	3	Contact object (3)	2	[{"changed": {"fields": ["feedback"]}}]	44	2
69	2020-04-26 14:08:23.362776+03	8	Contact object (8)	2	[{"changed": {"fields": ["feedback"]}}]	44	2
70	2020-05-26 09:54:07.692124+03	36	tithes	2	[{"changed": {"fields": ["Member Name"]}}]	47	2
71	2020-05-26 09:54:37.062272+03	36	tithes	2	[{"changed": {"fields": ["Amount"]}}]	47	2
72	2020-05-26 09:56:16.558544+03	22	tithes	2	[{"changed": {"fields": ["Archived Status"]}}]	47	2
73	2020-05-26 09:56:28.612286+03	57	tithes	2	[]	47	2
74	2020-05-26 09:56:39.389892+03	28	tithes	2	[{"changed": {"fields": ["Archived Status"]}}]	47	2
75	2020-05-26 09:56:46.606021+03	27	tithes	2	[]	47	2
76	2020-05-26 09:56:57.088055+03	40	tithes	2	[{"changed": {"fields": ["Archived Status"]}}]	47	2
77	2020-05-26 16:22:39.030533+03	65	Nalongo Joan	2	[{"changed": {"fields": ["Archived Status"]}}]	47	2
78	2020-05-26 16:23:09.349691+03	36	Maama Tracy	2	[{"changed": {"fields": ["Date"]}}]	47	2
79	2020-05-29 23:20:13.265663+03	9	Secretary	2	[{"changed": {"fields": ["User permissions"]}}]	29	2
80	2020-05-29 23:26:38.123593+03	9	Secretary	2	[{"changed": {"fields": ["User permissions"]}}]	29	2
81	2020-05-31 17:28:43.730277+03	1	red	1	[{"added": {}}]	57	2
82	2020-05-31 17:30:05.844805+03	1	red	2	[{"changed": {"fields": ["is_active"]}}]	57	2
83	2020-05-31 17:30:50.80908+03	2	navy-blue	1	[{"added": {}}]	57	2
84	2020-05-31 19:23:03.144358+03	3	dark-orange	1	[{"added": {}}]	57	2
85	2020-05-31 20:44:13.306006+03	4	black	1	[{"added": {}}]	57	2
86	2020-05-31 20:44:35.133608+03	5	deep-pink	1	[{"added": {}}]	57	2
87	2020-05-31 20:44:54.369205+03	6	dodger-blue	1	[{"added": {}}]	57	2
88	2020-05-31 20:45:10.90396+03	7	jazzberry-jam	1	[{"added": {}}]	57	2
89	2020-05-31 20:45:23.994957+03	8	light-sea-green	1	[{"added": {}}]	57	2
90	2020-05-31 20:45:38.979889+03	9	lime-green	1	[{"added": {}}]	57	2
91	2020-05-31 20:45:54.026654+03	10	maroon	1	[{"added": {}}]	57	2
92	2020-05-31 20:46:20.371212+03	11	medium-purple	1	[{"added": {}}]	57	2
93	2020-05-31 20:46:38.890691+03	12	radical-red	1	[{"added": {}}]	57	2
94	2020-05-31 20:46:55.644892+03	13	rebecca-purple	1	[{"added": {}}]	57	2
95	2020-05-31 20:47:16.29368+03	14	slate-gray	1	[{"added": {}}]	57	2
96	2020-05-31 20:47:36.666208+03	15	trinidad	1	[{"added": {}}]	57	2
205	2020-06-08 17:25:44.745119+03	12	petty	3		46	2
97	2020-05-31 20:47:53.592944+03	16	umber	1	[{"added": {}}]	57	2
98	2020-05-31 20:51:16.531302+03	15	trinidad	2	[{"changed": {"fields": ["colour"]}}]	57	2
99	2020-05-31 20:51:21.132001+03	15	trinidad	2	[]	57	2
100	2020-05-31 20:51:43.396468+03	14	slate-gray	2	[{"changed": {"fields": ["colour"]}}]	57	2
101	2020-05-31 20:52:16.254606+03	8	light-sea-green	2	[{"changed": {"fields": ["colour"]}}]	57	2
102	2020-05-31 20:55:52.478563+03	13	rebecca-purple	2	[{"changed": {"fields": ["colour"]}}]	57	2
103	2020-05-31 20:56:23.965372+03	12	radical-red	2	[{"changed": {"fields": ["colour"]}}]	57	2
104	2020-05-31 20:56:49.861127+03	16	umber	2	[{"changed": {"fields": ["colour"]}}]	57	2
105	2020-05-31 20:57:40.81488+03	11	medium-purple	2	[{"changed": {"fields": ["colour"]}}]	57	2
106	2020-05-31 20:58:01.08169+03	10	maroon	2	[{"changed": {"fields": ["colour"]}}]	57	2
107	2020-05-31 20:58:26.492769+03	9	lime-green	2	[{"changed": {"fields": ["colour"]}}]	57	2
108	2020-05-31 20:58:37.317795+03	8	light-sea-green	2	[]	57	2
109	2020-05-31 20:59:00.25945+03	7	jazzberry-jam	2	[{"changed": {"fields": ["colour"]}}]	57	2
110	2020-05-31 20:59:24.001998+03	6	dodger-blue	2	[{"changed": {"fields": ["colour"]}}]	57	2
111	2020-05-31 20:59:57.679913+03	5	deep-pink	2	[{"changed": {"fields": ["colour"]}}]	57	2
112	2020-05-31 21:00:26.504838+03	4	black	2	[{"changed": {"fields": ["colour"]}}]	57	2
113	2020-05-31 21:00:34.960229+03	3	dark-orange	2	[]	57	2
114	2020-05-31 21:00:42.637699+03	2	navy-blue	2	[]	57	2
115	2020-06-06 10:20:24.157878+03	44	Dihfahsih Mugoya	3		44	2
116	2020-06-06 10:20:41.123601+03	3	Kim Jane	3		44	2
117	2020-06-06 10:20:41.135449+03	2	Dihfahsih Mugoya	3		44	2
118	2020-06-06 10:48:45.844313+03	6	Ziwa Kiweewa	3		44	2
119	2020-06-07 16:22:26.18306+03	73	ARCHIVED	3		26	2
120	2020-06-07 16:22:26.188015+03	72	ARCHIVED	3		26	2
121	2020-06-07 16:22:26.190012+03	71	ARCHIVED	3		26	2
122	2020-06-07 16:22:26.191008+03	70	ARCHIVED	3		26	2
123	2020-06-07 16:22:26.193002+03	67	ARCHIVED	3		26	2
124	2020-06-07 16:22:26.193999+03	65	ARCHIVED	3		26	2
125	2020-06-07 16:22:26.195994+03	64	ARCHIVED	3		26	2
126	2020-06-07 16:22:26.197989+03	61	ARCHIVED	3		26	2
127	2020-06-07 16:22:26.199983+03	60	ARCHIVED	3		26	2
128	2020-06-07 16:22:26.200983+03	59	ARCHIVED	3		26	2
129	2020-06-07 16:22:26.203008+03	58	ARCHIVED	3		26	2
130	2020-06-07 16:22:26.203974+03	57	ARCHIVED	3		26	2
131	2020-06-07 16:22:26.20602+03	56	ARCHIVED	3		26	2
132	2020-06-07 16:22:26.207+03	55	ARCHIVED	3		26	2
133	2020-06-07 16:22:26.20896+03	54	ARCHIVED	3		26	2
134	2020-06-07 16:22:26.209957+03	53	ARCHIVED	3		26	2
135	2020-06-07 16:22:26.211985+03	52	ARCHIVED	3		26	2
136	2020-06-07 16:22:26.212949+03	51	ARCHIVED	3		26	2
137	2020-06-07 16:22:26.214943+03	50	ARCHIVED	3		26	2
138	2020-06-07 16:22:26.215941+03	49	ARCHIVED	3		26	2
139	2020-06-07 16:22:26.216937+03	48	ARCHIVED	3		26	2
140	2020-06-07 16:22:26.218979+03	47	ARCHIVED	3		26	2
141	2020-06-07 16:22:26.220929+03	46	ARCHIVED	3		26	2
142	2020-06-07 16:22:26.221925+03	45	ARCHIVED	3		26	2
143	2020-06-07 16:22:26.222921+03	44	ARCHIVED	3		26	2
144	2020-06-07 16:22:26.224944+03	43	ARCHIVED	3		26	2
145	2020-06-07 16:22:26.234889+03	42	ARCHIVED	3		26	2
146	2020-06-07 16:22:26.23592+03	41	ARCHIVED	3		26	2
147	2020-06-07 16:22:26.237881+03	40	ARCHIVED	3		26	2
148	2020-06-07 16:22:26.23888+03	39	ARCHIVED	3		26	2
149	2020-06-07 16:22:26.239877+03	38	ARCHIVED	3		26	2
150	2020-06-07 16:22:26.240873+03	37	ARCHIVED	3		26	2
151	2020-06-07 16:22:26.242886+03	36	ARCHIVED	3		26	2
152	2020-06-07 16:22:26.243867+03	35	ARCHIVED	3		26	2
153	2020-06-07 16:22:26.245861+03	34	ARCHIVED	3		26	2
154	2020-06-07 16:22:26.246859+03	33	ARCHIVED	3		26	2
155	2020-06-07 16:22:26.247855+03	32	ARCHIVED	3		26	2
156	2020-06-07 16:22:26.24985+03	31	ARCHIVED	3		26	2
157	2020-06-07 16:22:26.25086+03	30	ARCHIVED	3		26	2
158	2020-06-07 16:22:26.251844+03	29	ARCHIVED	3		26	2
159	2020-06-07 16:22:26.253839+03	28	ARCHIVED	3		26	2
160	2020-06-07 16:22:26.254837+03	27	ARCHIVED	3		26	2
161	2020-06-07 16:22:26.255834+03	26	ARCHIVED	3		26	2
162	2020-06-07 16:22:26.25683+03	25	ARCHIVED	3		26	2
163	2020-06-08 17:23:59.396464+03	9	CashFloat object (9)	3		49	2
164	2020-06-08 17:23:59.510162+03	8	CashFloat object (8)	3		49	2
165	2020-06-08 17:23:59.513152+03	7	CashFloat object (7)	3		49	2
166	2020-06-08 17:23:59.516166+03	6	CashFloat object (6)	3		49	2
167	2020-06-08 17:23:59.522361+03	5	CashFloat object (5)	3		49	2
168	2020-06-08 17:23:59.553046+03	4	CashFloat object (4)	3		49	2
169	2020-06-08 17:23:59.587954+03	3	CashFloat object (3)	3		49	2
170	2020-06-08 17:23:59.590313+03	2	CashFloat object (2)	3		49	2
171	2020-06-08 17:23:59.59294+03	1	CashFloat object (1)	3		49	2
172	2020-06-08 17:24:43.440655+03	43	allowance	3		46	2
173	2020-06-08 17:25:44.663791+03	45	petty	3		46	2
174	2020-06-08 17:25:44.693712+03	44	petty	3		46	2
175	2020-06-08 17:25:44.696409+03	42	petty	3		46	2
176	2020-06-08 17:25:44.698036+03	41	petty	3		46	2
177	2020-06-08 17:25:44.700708+03	40	general	3		46	2
178	2020-06-08 17:25:44.702687+03	39	general	3		46	2
179	2020-06-08 17:25:44.704681+03	38	main	3		46	2
180	2020-06-08 17:25:44.706064+03	37	main	3		46	2
181	2020-06-08 17:25:44.707955+03	36	allowance	3		46	2
182	2020-06-08 17:25:44.709668+03	35	allowance	3		46	2
183	2020-06-08 17:25:44.710665+03	34	allowance	3		46	2
184	2020-06-08 17:25:44.71266+03	33	main	3		46	2
185	2020-06-08 17:25:44.713699+03	32	general	3		46	2
186	2020-06-08 17:25:44.714656+03	31	petty	3		46	2
187	2020-06-08 17:25:44.717647+03	30	petty	3		46	2
188	2020-06-08 17:25:44.718739+03	29	petty	3		46	2
189	2020-06-08 17:25:44.721055+03	28	main	3		46	2
190	2020-06-08 17:25:44.722708+03	27	general	3		46	2
191	2020-06-08 17:25:44.724002+03	26	general	3		46	2
192	2020-06-08 17:25:44.725625+03	25	general	3		46	2
193	2020-06-08 17:25:44.726661+03	24	main	3		46	2
194	2020-06-08 17:25:44.728617+03	23	main	3		46	2
195	2020-06-08 17:25:44.729752+03	22	petty	3		46	2
196	2020-06-08 17:25:44.731608+03	21	petty	3		46	2
197	2020-06-08 17:25:44.733604+03	20	main	3		46	2
198	2020-06-08 17:25:44.735599+03	19	petty	3		46	2
199	2020-06-08 17:25:44.736643+03	18	allowance	3		46	2
200	2020-06-08 17:25:44.73831+03	17	allowance	3		46	2
201	2020-06-08 17:25:44.739587+03	16	petty	3		46	2
202	2020-06-08 17:25:44.74067+03	15	petty	3		46	2
203	2020-06-08 17:25:44.742579+03	14	petty	3		46	2
204	2020-06-08 17:25:44.743602+03	13	petty	3		46	2
206	2020-06-08 17:25:44.75754+03	11	petty	3		46	2
207	2020-06-08 17:25:44.759534+03	10	petty	3		46	2
208	2020-06-08 17:25:44.760532+03	9	general	3		46	2
209	2020-06-08 17:25:44.762627+03	8	general	3		46	2
210	2020-06-08 17:25:44.764522+03	7	general	3		46	2
211	2020-06-08 17:25:44.765616+03	6	main	3		46	2
212	2020-06-08 17:25:44.767513+03	5	main	3		46	2
213	2020-06-08 17:25:44.76851+03	4	general	3		46	2
214	2020-06-08 17:25:44.770112+03	1	general	3		46	2
215	2020-06-08 17:26:25.83762+03	18	Lwaki Oli Mulamu Conference 2020	3		10	2
216	2020-06-08 17:26:25.910427+03	17	Conference	3		10	2
217	2020-06-08 17:26:44.564822+03	13	Conference	3		25	2
218	2020-06-08 17:26:44.570492+03	12	Lwaki Oli Mulamu Conference	3		25	2
219	2020-06-08 17:26:44.572487+03	11	Lwaki Oli Mulamu Conference	3		25	2
220	2020-06-08 17:26:44.574547+03	10	Lwaki Oli Mulamu Conference	3		25	2
221	2020-06-08 17:26:44.576781+03	9	Building	3		25	2
222	2020-06-08 17:26:44.579468+03	8	Building2	3		25	2
223	2020-06-08 17:26:44.581463+03	7	Building2	3		25	2
224	2020-06-08 17:26:44.583458+03	6	Building2	3		25	2
225	2020-06-08 17:26:44.585452+03	5	Orphans	3		25	2
226	2020-06-08 17:26:44.587564+03	4	Radio Program	3		25	2
227	2020-06-08 17:26:44.589746+03	3	Building	3		25	2
228	2020-06-08 17:26:44.591436+03	2	Buying Machines	3		25	2
229	2020-06-08 17:26:44.593432+03	1	Building	3		25	2
230	2020-06-08 17:27:17.270993+03	22	None	3		47	2
231	2020-06-08 17:27:17.280965+03	75	Yusuf Lule	3		47	2
232	2020-06-08 17:27:17.282961+03	73	None	3		47	2
233	2020-06-08 17:27:17.284954+03	74	None	3		47	2
234	2020-06-08 17:27:17.28695+03	72	None	3		47	2
235	2020-06-08 17:27:17.288952+03	71	Mukisa Ivan	3		47	2
236	2020-06-08 17:27:17.290471+03	70	Desire Namuganyi	3		47	2
237	2020-06-08 17:27:17.291935+03	69	Desire Namuganyi	3		47	2
238	2020-06-08 17:27:17.29393+03	56	None	3		47	2
239	2020-06-08 17:27:17.295926+03	62	Geofrey Lubwama	3		47	2
240	2020-06-08 17:27:17.296924+03	60	Brenda Lubwama	3		47	2
241	2020-06-08 17:27:17.298917+03	68	Geofrey Lubwama	3		47	2
242	2020-06-08 17:27:17.299917+03	66	Mukisa Ivan	3		47	2
243	2020-06-08 17:27:17.301952+03	64	Desire Namuganyi	3		47	2
244	2020-06-08 17:27:17.303903+03	63	Gitta K	3		47	2
245	2020-06-08 17:27:17.30495+03	61	Geofrey Lubwama	3		47	2
246	2020-06-08 17:27:17.306972+03	59	Brenda Lubwama	3		47	2
247	2020-06-08 17:27:17.308432+03	57	Maama Tracy	3		47	2
248	2020-06-08 17:27:17.309889+03	58	Rebecca Sanyu Mirembe	3		47	2
249	2020-06-08 17:27:17.311886+03	28	Yusuf Lule	3		47	2
250	2020-06-08 17:27:17.313172+03	27	Yusuf Lule	3		47	2
251	2020-06-08 17:27:17.314874+03	54	None	3		47	2
252	2020-06-08 17:27:17.316869+03	41	Yusuf Lule	3		47	2
253	2020-06-08 17:27:17.317867+03	40	Mukisa Ivan	3		47	2
254	2020-06-08 17:27:17.319861+03	23	Yusuf Lule	3		47	2
255	2020-06-08 17:27:17.320902+03	53	Yusuf Lule	3		47	2
256	2020-06-08 17:27:17.322854+03	52	None	3		47	2
257	2020-06-08 17:27:17.323852+03	50	None	3		47	2
258	2020-06-08 17:27:17.325846+03	49	Upendo Flistar	3		47	2
259	2020-06-08 17:27:17.326842+03	48	None	3		47	2
260	2020-06-08 17:27:17.328838+03	51	Desire Namuganyi	3		47	2
261	2020-06-08 17:27:17.329863+03	45	Nabachwa Teddy	3		47	2
262	2020-06-08 17:27:17.331829+03	47	Upendo Flistar	3		47	2
263	2020-06-08 17:27:17.333272+03	46	None	3		47	2
264	2020-06-08 17:27:17.334855+03	44	None	3		47	2
265	2020-06-08 17:27:17.336816+03	43	None	3		47	2
266	2020-06-08 17:27:17.337857+03	42	Zake Joshua	3		47	2
267	2020-06-08 17:27:17.339809+03	2	None	3		47	2
268	2020-06-08 17:27:17.340806+03	38	Mukisa Ivan	3		47	2
269	2020-06-08 17:27:17.34212+03	31	None	3		47	2
270	2020-06-08 17:27:17.343798+03	29	Odeke Mable	3		47	2
271	2020-06-08 17:27:17.344796+03	21	None	3		47	2
272	2020-06-08 17:27:17.346789+03	20	None	3		47	2
273	2020-06-08 17:27:17.347787+03	35	None	3		47	2
274	2020-06-08 17:27:17.34978+03	32	None	3		47	2
275	2020-06-08 17:27:17.350901+03	25	None	3		47	2
276	2020-06-08 17:27:17.351777+03	19	None	3		47	2
277	2020-06-08 17:27:17.35377+03	18	Nabachwa Teddy	3		47	2
278	2020-06-08 17:27:17.354854+03	15	Yusuf Lule	3		47	2
279	2020-06-08 17:27:17.356762+03	10	Yusuf Lule	3		47	2
280	2020-06-08 17:27:17.35806+03	8	None	3		47	2
281	2020-06-08 17:27:17.359755+03	67	None	3		47	2
282	2020-06-08 17:27:17.361749+03	55	None	3		47	2
283	2020-06-08 17:27:17.362845+03	39	None	3		47	2
284	2020-06-08 17:27:17.364741+03	37	Mukisa Ivan	3		47	2
285	2020-06-08 17:27:17.366009+03	33	None	3		47	2
286	2020-06-08 17:27:17.367733+03	17	None	3		47	2
287	2020-06-08 17:27:17.368756+03	16	None	3		47	2
288	2020-06-08 17:27:17.369772+03	14	Odeke Mable	3		47	2
289	2020-06-08 17:27:17.371769+03	12	None	3		47	2
290	2020-06-08 17:27:17.373716+03	11	Zake Joshua	3		47	2
291	2020-06-08 17:27:17.374818+03	9	Posiano Zakumumpa	3		47	2
292	2020-06-08 17:27:17.37671+03	7	None	3		47	2
293	2020-06-08 17:27:17.378704+03	6	Mukisa Ivan	3		47	2
294	2020-06-08 17:27:17.381734+03	5	Nabachwa Teddy	3		47	2
295	2020-06-08 17:27:17.384688+03	4	None	3		47	2
296	2020-06-08 17:27:17.388678+03	3	Zake Joshua	3		47	2
297	2020-06-08 17:27:17.392787+03	30	None	3		47	2
298	2020-06-08 17:27:17.639007+03	1	None	3		47	2
299	2020-06-08 17:27:17.642002+03	24	Nusurah Ayebare	3		47	2
300	2020-06-08 17:27:17.694861+03	13	Desire Namuganyi	3		47	2
301	2020-06-08 17:27:17.729767+03	34	None	3		47	2
302	2020-06-08 17:27:17.732758+03	26	Yusuf Lule	3		47	2
303	2020-06-08 17:27:17.734752+03	65	Nalongo Joan	3		47	2
304	2020-06-08 17:27:17.737344+03	36	Maama Tracy	3		47	2
305	2020-06-08 17:27:33.899498+03	6	SalariesPaid object (6)	3		11	2
306	2020-06-08 17:27:33.920762+03	5	SalariesPaid object (5)	3		11	2
307	2020-06-08 17:27:33.923434+03	4	SalariesPaid object (4)	3		11	2
308	2020-06-08 17:27:33.926426+03	3	SalariesPaid object (3)	3		11	2
309	2020-06-08 17:27:33.92871+03	2	SalariesPaid object (2)	3		11	2
310	2020-06-08 17:27:33.931413+03	1	SalariesPaid object (1)	3		11	2
311	2020-06-10 10:08:01.826784+03	19	Brenda Lubwama	3		29	2
312	2020-06-10 10:08:02.002605+03	18	Geofrey Lubwama	3		29	2
313	2020-06-10 10:08:02.006576+03	17	Sempijja Jimmy	3		29	2
314	2020-06-10 10:08:02.011552+03	16	Joshua Mubulire	3		29	2
315	2020-06-10 10:08:02.016566+03	15	Nalongo Joan	3		29	2
316	2020-06-10 10:08:02.020555+03	14	Kawombe Harriet	3		29	2
317	2020-06-10 10:08:02.023686+03	13	Desire Namuganyi	3		29	2
318	2020-06-10 10:08:02.027537+03	11	Mukisa Ivan	3		29	2
319	2020-06-10 10:08:02.03262+03	10	Gitta K	3		29	2
320	2020-06-10 10:08:02.036614+03	9	Odeke Mable	3		29	2
321	2020-06-10 10:08:02.039563+03	4	Yusuf Lule	3		29	2
322	2020-07-03 09:57:08.314075+03	22	Pure joy and happiness	2	[{"changed": {"fields": ["slider_image"]}}]	36	2
323	2020-07-04 10:53:02.937189+03	19	Radio Program	2	[{"changed": {"fields": ["Archived_Status"]}}]	10	2
324	2020-07-04 12:18:36.87685+03	20	Radio Program2020	3		10	2
325	2020-07-04 12:18:36.879999+03	19	Radio Program	3		10	2
326	2020-07-04 12:59:55.745945+03	21	Radio Program	2	[{"changed": {"fields": ["Amount_Needed"]}}]	10	2
327	2020-07-21 00:00:31.481803+03	22	Lwaki Olimulamu 2020 Conference	3		10	2
328	2020-07-21 00:00:31.537007+03	21	Radio Program	3		10	2
329	2020-07-21 00:03:54.444854+03	23	Radio Program	1	[{"added": {}}]	10	2
330	2020-07-21 00:20:46.816501+03	23	Radio Program	3		10	2
331	2020-07-21 00:29:40.902848+03	111	NOT-ARCHIVED	3		26	2
332	2020-07-21 00:29:40.906837+03	110	NOT-ARCHIVED	3		26	2
333	2020-07-21 00:29:40.907871+03	109	NOT-ARCHIVED	3		26	2
334	2020-07-21 00:29:40.909226+03	108	NOT-ARCHIVED	3		26	2
335	2020-07-21 00:29:40.910824+03	107	NOT-ARCHIVED	3		26	2
336	2020-07-21 00:29:40.912821+03	106	NOT-ARCHIVED	3		26	2
337	2020-07-21 00:29:40.914163+03	105	NOT-ARCHIVED	3		26	2
338	2020-07-21 00:29:40.915811+03	104	NOT-ARCHIVED	3		26	2
339	2020-07-21 01:28:39.296102+03	24	Youths	3		10	2
340	2020-07-21 01:29:40.960365+03	115	NOT-ARCHIVED	3		26	2
341	2020-07-21 01:29:40.970887+03	114	NOT-ARCHIVED	3		26	2
342	2020-07-21 01:29:40.975868+03	113	NOT-ARCHIVED	3		26	2
343	2020-07-21 01:29:40.9799+03	112	NOT-ARCHIVED	3		26	2
344	2020-07-27 23:41:50.98908+03	93	offering	3		47	2
345	2020-07-27 23:41:51.102071+03	80	offering	3		47	2
346	2020-07-27 23:41:51.10433+03	96	offering	3		47	2
347	2020-07-27 23:41:51.106907+03	94	offering	3		47	2
348	2020-07-27 23:41:51.126855+03	97	offering	3		47	2
349	2020-07-27 23:41:51.130106+03	95	offering	3		47	2
377	2020-09-02 16:02:58.793275+03	3	United Christian Centre Bwaise (UCC BWAISE) is a born again Christian church in Kampala Uganda East Africa.\r\nThe church is located on Bwaise ΓÇô Nabweru road.\r\n\r\n The lead pastor is Pr. Joshua Zake mini	2	[{"changed": {"fields": ["about"]}}]	37	2
378	2020-09-02 16:04:27.477602+03	3	United Christian Centre Bwaise (UCC BWAISE) is a born again Christian church in Kampala Uganda East Africa.\r\nThe church is located on Bwaise ΓÇô Nabweru road.\r\n The lead pastor is Pr. Joshua Zake minist	2	[{"changed": {"fields": ["about"]}}]	37	2
379	2020-09-02 16:05:37.425128+03	3	United Christian Centre Bwaise (UCC BWAISE) is a born again Christian church in Kampala Uganda East Africa.\r\nThe church is located on Bwaise ΓÇô Nabweru road.\r\n The lead pastor is Pr. Joshua Zake minist	2	[{"changed": {"fields": ["about"]}}]	37	2
380	2020-09-02 16:19:26.946158+03	3	United Christian Centre Bwaise (UCC BWAISE) is a born again Christian church in Kampala Uganda East Africa.\r\nThe church is located on Bwaise ΓÇô Nabweru road.\r\n The lead pastor is Pr. Joshua Zake minist	2	[{"changed": {"fields": ["about"]}}]	37	2
381	2020-09-08 13:52:37.531781+03	11	general	2	[{"changed": {"fields": ["Archived_Status"]}}]	46	2
382	2020-09-08 13:52:46.558648+03	10	general	2	[{"changed": {"fields": ["Archived_Status"]}}]	46	2
414	2020-09-15 15:07:30.191976+03	4		2	[{"changed": {"fields": ["about_title", "vision_description"]}}]	37	2
415	2020-09-15 15:08:49.842253+03	5		2	[{"changed": {"fields": ["about_title", "vision_description", "mission_description"]}}]	37	2
416	2020-09-23 08:09:47.024976+03	6		1	[{"added": {}}]	37	2
417	2020-09-23 09:59:36.060007+03	3	Whenever God calls you to serve him for a long time commission, itΓÇÖs very important to know what he has called you to and how to do it. Sometimes he may not give you the full details, but at least he 	2	[{"changed": {"fields": ["about_title", "core_values", "church_details", "vision_description", "mission_description"]}}]	37	2
418	2020-09-23 10:00:11.62308+03	6	1. Discipline\r\n\r\n2. Fear of God\r\n\r\n3. Humility and dignity\r\n\r\n4. Others before self.\r\n\r\n5. Respect for leaders	3		37	2
419	2020-09-23 10:00:11.631364+03	5	HOW DO WE DISCOVER GODΓÇÖS WILL\r\n\r\nEach one of us was given a divine mission and God has a purpose for each one that is different from any other personΓÇÖs. However, many people are unable to walk accordi	3		37	2
420	2020-09-23 10:00:11.634099+03	4	Types of GodΓÇÖs will\r\n\r\n-\tIndividual\r\n-\tGeneral\r\n-\tSeasonal\r\n-\tContributional / Personal\r\n\r\nI strongly believe that a lot of things happened before creation and basically before Mankind came on this pl	3		37	2
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	dashboard	allowancereportarchive
2	dashboard	donations
3	dashboard	donationsreportarchive
4	dashboard	expensesreportarchive
5	dashboard	generalexpenses
6	dashboard	generalexpensesreportarchive
7	dashboard	members
8	dashboard	offerings
9	dashboard	offeringsreportarchive
10	dashboard	pledgeitem
11	dashboard	salariespaid
12	dashboard	salariespaidreportarchive
13	dashboard	spend
14	dashboard	sundry
15	dashboard	sundryreportarchive
16	dashboard	visitors
17	dashboard	tithesreportarchive
18	dashboard	tithes
19	dashboard	thanksgivingreportarchive
20	dashboard	thanksgiving
21	dashboard	staffdetails
22	dashboard	seedsreportarchive
23	dashboard	seeds
24	dashboard	pledgesreportarchive
25	dashboard	pledgescashedout
26	dashboard	pledges
27	dashboard	paidpledges
28	dashboard	allowance
29	dashboard	user
30	blog	posts
31	admin	logentry
32	auth	permission
33	auth	group
34	contenttypes	contenttype
35	sessions	session
36	dashboard	slider
37	dashboard	about
38	dashboard	page
39	dashboard	gallery
40	dashboard	image
41	dashboard	news
42	dashboard	event
43	dashboard	church
44	dashboard	contact
45	dashboard	buildingrenovation
46	dashboard	expenditures
47	dashboard	revenues
48	dashboard	archivedmembers
49	dashboard	cashfloat
50	oauth2_provider	application
51	oauth2_provider	accesstoken
52	oauth2_provider	grant
53	oauth2_provider	refreshtoken
54	corsheaders	corsmodel
55	dashboard	ministry
56	dashboard	project
57	dashboard	theme
58	background_task	completedtask
59	background_task	task
60	dashboard	testing
61	dashboard	annualconference
62	dashboard	newconvert
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2020-02-14 20:35:40.569673+03
2	contenttypes	0002_remove_content_type_name	2020-02-14 20:35:40.688709+03
3	auth	0001_initial	2020-02-14 20:35:40.916106+03
4	auth	0002_alter_permission_name_max_length	2020-02-14 20:35:41.235252+03
5	auth	0003_alter_user_email_max_length	2020-02-14 20:35:41.270171+03
6	auth	0004_alter_user_username_opts	2020-02-14 20:35:41.314001+03
7	auth	0005_alter_user_last_login_null	2020-02-14 20:35:41.347036+03
8	auth	0006_require_contenttypes_0002	2020-02-14 20:35:41.354002+03
9	auth	0007_alter_validators_add_error_messages	2020-02-14 20:35:41.384615+03
10	auth	0008_alter_user_username_max_length	2020-02-14 20:35:41.411322+03
11	auth	0009_alter_user_last_name_max_length	2020-02-14 20:35:41.440546+03
12	auth	0010_alter_group_name_max_length	2020-02-14 20:35:41.473396+03
13	auth	0011_update_proxy_permissions	2020-02-14 20:35:41.502003+03
14	dashboard	0001_initial	2020-02-14 20:35:43.953249+03
15	admin	0001_initial	2020-02-14 20:35:45.258248+03
16	admin	0002_logentry_remove_auto_add	2020-02-14 20:35:45.407286+03
17	admin	0003_logentry_add_action_flag_choices	2020-02-14 20:35:45.458354+03
18	dashboard	0002_auto_20200203_1346	2020-02-14 20:35:45.562117+03
19	dashboard	0003_auto_20200203_1356	2020-02-14 20:35:45.783275+03
20	dashboard	0004_members_initials	2020-02-14 20:35:46.070849+03
21	dashboard	0005_auto_20200205_1215	2020-02-14 20:35:46.149302+03
22	dashboard	0006_slider	2020-02-14 20:35:46.20708+03
23	dashboard	0007_about	2020-02-14 20:35:46.320132+03
24	dashboard	0008_gallery_image_page	2020-02-14 20:35:46.614349+03
25	dashboard	0009_news	2020-02-14 20:35:46.817105+03
26	dashboard	0010_event	2020-02-14 20:35:46.956246+03
27	dashboard	0011_auto_20200205_2303	2020-02-14 20:35:46.981224+03
28	dashboard	0012_church	2020-02-14 20:35:47.113235+03
29	dashboard	0013_image_is_view_on_web	2020-02-14 20:35:47.148818+03
30	dashboard	0014_auto_20200206_1528	2020-02-14 20:35:47.189023+03
31	dashboard	0015_auto_20200206_2154	2020-02-14 20:35:47.423208+03
32	dashboard	0016_church_maps_embedded_link	2020-02-14 20:35:47.457297+03
33	dashboard	0017_contact	2020-02-14 20:35:47.562852+03
34	dashboard	0018_auto_20200207_0910	2020-02-14 20:35:47.621407+03
35	dashboard	0019_contact_feedback	2020-02-14 20:35:47.64523+03
36	dashboard	0020_auto_20200207_0923	2020-02-14 20:35:47.674269+03
37	dashboard	0021_members_group	2020-02-14 20:35:47.712239+03
38	dashboard	0022_auto_20200212_2145	2020-02-14 20:35:47.878451+03
39	dashboard	0023_auto_20200212_2252	2020-02-14 20:35:47.90037+03
40	dashboard	0024_auto_20200212_2259	2020-02-14 20:35:47.927547+03
41	dashboard	0025_auto_20200213_0004	2020-02-14 20:35:47.950139+03
42	dashboard	0026_auto_20200213_1043	2020-02-14 20:35:48.065167+03
43	dashboard	0027_auto_20200213_1153	2020-02-14 20:35:48.114063+03
44	dashboard	0028_auto_20200213_1154	2020-02-14 20:35:48.158974+03
45	dashboard	0029_auto_20200213_1211	2020-02-14 20:35:48.204088+03
46	dashboard	0030_about_about_title	2020-02-14 20:35:48.22761+03
47	dashboard	0031_auto_20200213_1338	2020-02-14 20:35:48.551256+03
48	dashboard	0032_auto_20200213_1513	2020-02-14 20:35:48.612692+03
49	dashboard	0033_auto_20200213_1602	2020-02-14 20:35:48.696944+03
50	dashboard	0034_auto_20200213_1846	2020-02-14 20:35:48.74363+03
51	dashboard	0035_members_more_info	2020-02-14 20:35:48.784141+03
52	dashboard	0036_auto_20200214_0019	2020-02-14 20:35:48.825595+03
53	sessions	0001_initial	2020-02-14 20:35:48.924016+03
54	dashboard	0037_tithesreportarchive_service	2020-02-15 18:50:04.107922+03
55	dashboard	0038_auto_20200215_1851	2020-02-15 18:51:46.853256+03
56	dashboard	0039_auto_20200217_0044	2020-02-17 00:45:07.290663+03
57	dashboard	0040_members_date	2020-02-17 17:11:14.106342+03
58	dashboard	0041_auto_20200217_1715	2020-02-17 17:15:08.536498+03
59	dashboard	0042_auto_20200218_1213	2020-02-18 12:13:38.612054+03
60	dashboard	0043_auto_20200218_1239	2020-02-18 12:39:17.463967+03
61	dashboard	0044_buildingrenovation	2020-02-18 15:16:07.94181+03
62	dashboard	0045_auto_20200218_1533	2020-02-18 15:33:53.189925+03
63	dashboard	0046_buildingrenovation_archived_status	2020-02-18 16:21:54.143707+03
64	dashboard	0047_auto_20200218_1628	2020-02-18 16:28:52.113526+03
65	dashboard	0048_auto_20200218_1820	2020-02-18 18:20:25.106086+03
66	dashboard	0049_auto_20200218_1840	2020-02-18 18:41:03.697091+03
67	dashboard	0050_auto_20200218_1924	2020-02-18 19:25:00.820204+03
68	dashboard	0051_auto_20200218_2050	2020-02-18 20:50:10.103898+03
69	dashboard	0052_auto_20200218_2234	2020-02-18 22:34:47.450409+03
70	dashboard	0053_auto_20200219_1112	2020-02-19 11:12:23.450894+03
71	dashboard	0054_expenditures_archived_status	2020-02-19 11:21:11.119055+03
72	dashboard	0055_expenditures_reason_filtering	2020-02-19 15:01:58.160987+03
73	dashboard	0056_auto_20200219_2203	2020-02-19 22:03:50.658515+03
74	dashboard	0057_revenues_other_sources	2020-02-20 14:55:55.056893+03
75	dashboard	0058_auto_20200220_1558	2020-02-20 15:58:54.126542+03
76	dashboard	0059_expenditures_member_name	2020-02-20 20:40:30.618995+03
77	dashboard	0060_expenditures_notes	2020-02-20 21:30:14.831289+03
78	dashboard	0061_auto_20200220_2219	2020-02-20 22:19:24.491885+03
79	dashboard	0062_auto_20200221_0921	2020-02-21 09:22:12.734212+03
80	dashboard	0063_auto_20200221_1006	2020-02-21 10:06:48.694668+03
81	dashboard	0064_auto_20200221_1013	2020-02-21 10:13:16.12747+03
82	dashboard	0065_auto_20200221_2159	2020-02-21 21:59:24.592581+03
83	dashboard	0066_members_archived_status	2020-02-27 09:50:36.015031+03
84	dashboard	0067_auto_20200227_1134	2020-02-27 11:35:07.212305+03
85	dashboard	0068_pledges_archived_status	2020-03-02 19:03:18.75683+03
86	dashboard	0069_pledges_pledge_id	2020-03-03 00:01:42.094986+03
87	dashboard	0070_auto_20200303_0037	2020-03-03 00:37:46.952925+03
88	dashboard	0071_auto_20200303_0044	2020-03-03 00:44:55.955467+03
89	dashboard	0072_auto_20200303_2146	2020-03-03 21:46:37.714217+03
90	dashboard	0073_cashfloat	2020-03-06 21:06:58.86301+03
91	dashboard	0074_auto_20200309_1703	2020-03-09 17:03:55.73246+03
92	dashboard	0075_auto_20200309_1724	2020-03-09 17:24:51.060121+03
93	oauth2_provider	0001_initial	2020-04-27 11:19:50.413073+03
94	oauth2_provider	0002_auto_20190406_1805	2020-04-27 11:19:51.323906+03
95	corsheaders	0001_initial	2020-04-27 12:40:56.020526+03
96	dashboard	0076_auto_20200427_2046	2020-04-27 20:47:00.647718+03
97	dashboard	0077_auto_20200430_2052	2020-04-30 20:52:36.830823+03
98	dashboard	0078_auto_20200501_0001	2020-05-01 00:01:12.668396+03
99	dashboard	0079_ministry	2020-05-06 10:55:54.399657+03
100	dashboard	0080_ministry_is_view_on_web	2020-05-06 11:50:24.000004+03
101	dashboard	0081_members_is_active	2020-05-25 12:28:59.138716+03
102	dashboard	0082_auto_20200530_1226	2020-05-30 12:27:10.752381+03
103	dashboard	0083_project_project_leader	2020-05-30 12:46:14.646027+03
104	dashboard	0084_theme	2020-05-31 10:27:54.720602+03
105	dashboard	0085_remove_theme_theme_image	2020-05-31 20:39:38.999234+03
106	dashboard	0086_auto_20200603_1905	2020-06-03 19:05:14.044138+03
107	dashboard	0087_gallery_date	2020-06-03 19:06:52.975601+03
108	dashboard	0088_auto_20200603_2000	2020-06-03 20:01:05.645727+03
109	dashboard	0089_auto_20200603_2002	2020-06-03 20:02:48.37402+03
110	dashboard	0090_visitors_date	2020-06-06 15:22:03.005274+03
111	dashboard	0091_auto_20200607_1058	2020-06-07 10:58:13.75141+03
112	dashboard	0092_auto_20200607_1125	2020-06-07 11:25:34.279675+03
113	dashboard	0093_auto_20200607_1152	2020-06-07 11:52:43.694895+03
114	dashboard	0094_auto_20200607_1227	2020-06-07 12:28:02.22281+03
115	dashboard	0095_auto_20200607_1349	2020-06-07 13:49:35.199011+03
116	dashboard	0096_delete_paidpledges	2020-06-07 16:33:25.014471+03
117	dashboard	0097_auto_20200608_0932	2020-06-08 09:33:07.451912+03
118	dashboard	0098_auto_20200608_1814	2020-06-08 18:15:00.547022+03
119	dashboard	0099_expenditures_otheramount	2020-06-08 18:23:17.043194+03
120	dashboard	0098_auto_20200608_1840	2020-06-08 18:40:38.403024+03
121	dashboard	0099_auto_20200608_1842	2020-06-08 18:42:28.670969+03
122	dashboard	0100_delete_expenditures	2020-06-08 20:55:53.910384+03
123	dashboard	0101_expenditures	2020-06-08 20:56:55.28815+03
124	dashboard	0102_auto_20200609_0908	2020-06-09 09:09:02.461369+03
125	dashboard	0103_members_archived_status	2020-06-09 10:18:20.726763+03
126	dashboard	0104_members_full_named	2020-06-09 22:32:06.080668+03
127	dashboard	0105_auto_20200610_1145	2020-06-10 11:45:29.245499+03
128	dashboard	0106_auto_20200611_1004	2020-06-11 10:05:07.199414+03
129	dashboard	0107_auto_20200616_0835	2020-06-16 08:35:29.721462+03
130	dashboard	0108_auto_20200703_0953	2020-07-03 09:53:34.014223+03
131	dashboard	0108_auto_20200704_1152	2020-07-04 11:52:44.023606+03
132	dashboard	0108_auto_20200704_1158	2020-07-04 11:58:12.901799+03
133	dashboard	0109_auto_20200704_1216	2020-07-04 12:16:28.576125+03
134	dashboard	0110_auto_20200704_1254	2020-07-04 12:54:14.958648+03
135	dashboard	0111_salariespaid_archived_status	2020-07-04 15:50:01.990569+03
136	dashboard	0112_delete_salariespaidreportarchive	2020-07-04 20:50:19.219708+03
137	dashboard	0113_auto_20200705_1119	2020-07-05 11:20:08.252273+03
138	dashboard	0114_auto_20200721_0231	2020-07-21 02:31:47.694029+03
139	dashboard	0115_pledges_nameofpledgee	2020-07-21 02:55:20.993412+03
140	dashboard	0116_auto_20200721_0305	2020-07-21 03:05:54.579079+03
141	dashboard	0117_auto_20200820_0859	2020-08-20 08:59:30.068585+03
142	background_task	0001_initial	2020-08-27 16:10:21.935857+03
143	background_task	0002_auto_20170927_1109	2020-08-27 16:10:23.368332+03
144	dashboard	0118_testing	2020-09-02 11:14:28.077002+03
145	dashboard	0119_annualconference	2020-09-11 10:54:56.762345+03
146	dashboard	0120_auto_20200911_1208	2020-09-11 12:08:56.529285+03
147	dashboard	0121_newconvert	2020-09-15 00:23:14.687388+03
148	dashboard	0122_auto_20200915_0755	2020-09-15 07:56:00.368406+03
149	dashboard	0123_about_core_values	2020-09-23 08:06:51.035795+03
150	dashboard	0124_auto_20200923_0903	2020-09-23 09:03:20.024569+03
151	dashboard	0125_auto_20200928_1359	2020-09-28 13:59:38.318117+03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
32iydxjil4bqip7pl0ppkgrk4777915j	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-02-18 19:59:01.734+03
64rll1o4ystz00tzb82lhq03vc50extv	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-02-21 14:59:07.23+03
90khtxhhivs4nx0j2fkhf5o8pl14uvbn	ZDM5ZTY2ZDMwYTcwMTc5ODY3NDk5MzdmMTYwYWZmZGZjZWZiYjBmMDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWQxZTQyODFmZmU5YzQwY2VmNmEwOGZkZDA2YmYzMzhiMzFlOWRlIn0=	2020-02-26 20:52:57.328+03
cx8huj20lhstxeblw517udeuwctrt6hu	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-02-23 01:55:17.338+03
d3pcq4dnslcaf8eewlc2c68h2dyhcvw7	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-02-23 16:58:20.039+03
df00tgc91pf8x1eib3kc5x7ke847ily1	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-02-23 15:59:00.812+03
div43f28m4v3j2d9mwjyw2wstxzju459	ZjkxMmQyYzZjOGZkZTk1NGU1MDQyMTU2NDJlYWUyNzRhYjMxMjc0OTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxZjc1YTVjZDQ1ZDQwMTMyYzNkMGZlZTgzNDI2ODA2YmJlYjEwY2U3In0=	2020-02-20 01:36:31.253+03
0g50yexaz73hmtcdg787co9rtpmoivgr	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-03-14 17:00:13.50229+03
eyyk9csqhokr7f6ttzn7tdytm22k8zjb	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-02-19 12:46:12.728+03
lmu3ylfo62dq98w8hxnys1s5dszhlf0f	ZDM5ZTY2ZDMwYTcwMTc5ODY3NDk5MzdmMTYwYWZmZGZjZWZiYjBmMDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWQxZTQyODFmZmU5YzQwY2VmNmEwOGZkZDA2YmYzMzhiMzFlOWRlIn0=	2020-02-26 22:58:07.088+03
loe9ugk4xtzl385qspnsu5w9x9soxaxs	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-02-20 19:51:37.398+03
m0llct13bacqrfn94aoz0w8vhnbksyyv	NjcwY2RlMDQ0OTRjNmYyMjRmMzUzZjA1Y2Q1MTAzNjNjMTgxMTEyYzp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwMGU2ZDY5YmM3NGExZTliNWY1ZTY0OTNmM2JkMDAyMDRkYmRmMDM2In0=	2020-02-17 14:28:19.125+03
oj8gy8xky4qfksseir0a50usq35qsbgb	MTg2MTE3ZTYzYTM3MDk3N2MzZDExNGY3NmZlYWY1ZDJiNjQ2NmM2YTp7fQ==	2020-02-24 18:24:20.538+03
vgagczwmepjxrma3m0gflvvyjmc589og	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-02-22 20:38:20.859+03
xu3c0mz0ph7xdyexexwwuz7g4rnvoqiv	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-02-21 10:05:47.586+03
djz6de31tw467xtcqlq4prfx7270z9ln	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-02-28 21:52:50.272745+03
73nb4mgnu070pgt3oopfwfm1dhgp82al	ZDM5ZTY2ZDMwYTcwMTc5ODY3NDk5MzdmMTYwYWZmZGZjZWZiYjBmMDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWQxZTQyODFmZmU5YzQwY2VmNmEwOGZkZDA2YmYzMzhiMzFlOWRlIn0=	2020-03-07 21:13:19.588218+03
859l1l8gwv6awlbtzx0f8wkeo4ypk55r	NmRmMTlhMDY0NzJjNDRmMGIzMWYxMzMzYzM4Mjc4Yjk4OTIyZDgzZDp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmQwNjBjZWFiNWE5N2FhMzBkNmEwMGViYWNkMjkwOWFiN2MyNmFlMSJ9	2020-05-22 17:10:46.235024+03
7wnbhxyhf1vyk7tie3vy9fpctq9sn03x	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-03-08 21:44:28.516154+03
x5334thfoclcmzxsp7qsk2pn8if8tmx9	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-03-06 16:31:47.708157+03
zjknoquc9ojqkq551nc8sw2hxre2a9uj	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-02-29 21:30:53.475029+03
vfj0bm6ybeioyteituuj8bg83abj6qgy	ZDY0ZTBhMDY1MzZkYmI5MDlkZWM5NzBjYWI4NDNhMzFjN2Q4NTAzNjp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0NDczZGE0YjEyNmM4MGI4ZWI3ZjU5ZWM5N2UxNWJiNTkzMDQ5YWJiIn0=	2020-03-07 01:11:39.568906+03
ep7cszow9qtsil0fmxb1gyoorewzzgsq	ZDM5ZTY2ZDMwYTcwMTc5ODY3NDk5MzdmMTYwYWZmZGZjZWZiYjBmMDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWQxZTQyODFmZmU5YzQwY2VmNmEwOGZkZDA2YmYzMzhiMzFlOWRlIn0=	2020-03-07 01:13:00.997033+03
pxguhs9sep5skez610mnjar9ntnf8sqg	ZDM5ZTY2ZDMwYTcwMTc5ODY3NDk5MzdmMTYwYWZmZGZjZWZiYjBmMDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZWQxZTQyODFmZmU5YzQwY2VmNmEwOGZkZDA2YmYzMzhiMzFlOWRlIn0=	2020-03-03 00:27:44.034595+03
1nl2c2g3gdg5fxd8ctqewmkpqffhvg9k	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-03-16 19:04:16.979084+03
snj3ol8ne3jtrvgwizefn5yhjcfn1qsa	OTM4ZjE0ZWRkOWI4NjY4MjBlYzRkYjgxZGJjNDdiNDJmNTk2MDZjMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYTNiMmVlYTc3MTk3M2JlYTdlY2QxOTlhNjA4NWQzYjNiOTk4ODM0In0=	2020-07-09 15:57:21.589265+03
cd16z9fqnprw519ytohj0d607ih5zux5	MTI1NjlhMjE5MmRlN2QxNDI3ZDZiMjFiZDhhOTQ3ZGE5OWRlOGZlYjp7Il9hdXRoX3VzZXJfaWQiOiI5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0YTE1ZTIyYzU2OTBkYWE3YjZhNzk1MzExN2YwYmQyN2I4ZDNmYjA4In0=	2020-03-24 21:22:31.404975+03
1m6v8e12m4dux31f8uyp4iogjqy85yl0	YmUwM2E3MGQ1NzQ1NjI5NzNmMWI2MWM5OGVjNDM5MDJiZTg4YTQ4OTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZDU3MDY3MDZjYjY0MzdkNzZmZmUwMGY4MGQxYjc1NzFmYzQ3MDhiIn0=	2020-06-14 17:30:51.037094+03
847gregs6njl5jjuy37nvqa411s5zb7f	YTk4MmZlNTgxNDBmNWI4OTQ5YjYwZThhODFjYjkxZDVjMGUyNWVlOTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NWFkNWYyZmQ5NzQxMjhkYjcyNzNhZjQ1YWVlYjAxOTQ1YzE5NGNkIn0=	2020-05-23 20:09:16.549898+03
jjyueju9yjc81mkng0odocwdziqt3fxs	NmRmMTlhMDY0NzJjNDRmMGIzMWYxMzMzYzM4Mjc4Yjk4OTIyZDgzZDp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmQwNjBjZWFiNWE5N2FhMzBkNmEwMGViYWNkMjkwOWFiN2MyNmFlMSJ9	2020-05-27 19:46:10.393783+03
43ggczjfutc3qbhmifguwjipw2pjwy60	YmUwM2E3MGQ1NzQ1NjI5NzNmMWI2MWM5OGVjNDM5MDJiZTg4YTQ4OTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZDU3MDY3MDZjYjY0MzdkNzZmZmUwMGY4MGQxYjc1NzFmYzQ3MDhiIn0=	2020-06-16 14:36:16.924821+03
si6r1aw7id0233fgqc6ftcfg2przjfvo	OWI5Y2NlNzRiYWI1ZTk3ZmJkNzExZDkyNmE2YTI5YTc0MDBkYTI5ZTp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNDU5ZjA4OWQyM2Y4YmU0ZTg2ODVmZjE3MDc3NGYyNzUyMmUxNmVhYSJ9	2020-06-20 08:41:04.603066+03
uzi4mnbx995oybimf20fcl5rgjzfztsv	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-07-18 21:22:44.668105+03
e8m1rpkony66n02sz2bprdb78m906ao7	NzMzZTgwNmM2OTE0NWU3N2I3N2ZhOTQ2MWVlNDgzZDk0MDJmNWViZDp7Il9hdXRoX3VzZXJfaWQiOiIyNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODFkNDlkYWYwN2I3M2UyOTI0ZGY0MjI4MDJmZDI2MDZkYTI4MjJkMyJ9	2020-08-15 23:38:43.879264+03
ft25pbbu2smp9djwmusg5f29zw5htjqw	MTg2MTE3ZTYzYTM3MDk3N2MzZDExNGY3NmZlYWY1ZDJiNjQ2NmM2YTp7fQ==	2020-08-19 11:37:10.271003+03
k9pr2wqqh06x85ycnwn45ivtz6mim24r	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-09-02 22:57:38.906297+03
jo9j7e6r55f107lwfegumdd03kx0aiad	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-09-07 14:03:36.98226+03
89ymvedqosfqrcxkyogifz3kebyyf43u	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-09-09 11:58:01.888558+03
4eomnt04q32g1lu89htjjskuzgikdo7g	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-04-01 14:37:33.292233+03
vj6kzwxvffnd7sghleegty07j17pr7z2	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-04-04 06:06:49.444515+03
g154x9sc4buw03zz6yuj5wnaeq4ds5hg	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-05-10 20:00:39.169634+03
j6s7e9uzmbfwy3nwcf7wfmqjgrv7m5hh	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-09-25 23:15:35.657453+03
w38l22anwyp1rsan9ysj516tareygnsz	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-09-29 08:51:43.313918+03
2c1pjocidoohqgqxoonssn4sarhueq1g	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-10-01 17:23:08.105599+03
wmezs4mvyjk4wuvlnfldjbd2j0mf2q9l	NWRhMTlkYzg0ZGE2ODk1OWFjOGI1ZWUyYTA0NGM3NjY3MWZhNDlhNjp7Il9tZXNzYWdlcyI6IltbXCJfX2pzb25fbWVzc2FnZVwiLDAsMjUsXCJZb3UgaGF2ZSBiZWVuIGxvZ2dlZCBvdXQsIFlvdSBjYW4gbG9nIGluIGFnYWluXCJdXSJ9	2020-05-11 13:54:30.335958+03
w5ppubzby1aeyvi2mrdsi2ch7vp1phzo	YmUwM2E3MGQ1NzQ1NjI5NzNmMWI2MWM5OGVjNDM5MDJiZTg4YTQ4OTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZDU3MDY3MDZjYjY0MzdkNzZmZmUwMGY4MGQxYjc1NzFmYzQ3MDhiIn0=	2020-06-14 18:32:52.709778+03
buck47kmoql50saeqkpteguu12m1ars2	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-04-07 14:40:51.825962+03
dvegkycvgux1xymspov662ooonh1l53y	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-05-12 14:16:05.529024+03
li9w1favww3mgtzvezu466n7jvijv6y0	ZGU1OTc5NjliODg0ZWU3ZDhmODIxNmYzYjRmOTVkMTQ0NzYxMmU3MDp7Il9hdXRoX3VzZXJfaWQiOiI5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0MWFiYWZmZDZhMzQ4YmYxNjk2ZTFlZjAwN2Y1ZDc5YTZkOTRiN2RiIn0=	2020-06-21 21:51:39.065786+03
6yqrnxedtzu919ho0u2k6lo0srwtwiho	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-05-13 15:50:58.263421+03
dhj78d6fyfw6mlqmpkded5x2ott4uret	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-04-18 21:52:26.665054+03
jvb3y8mwj6v7rsm7y3fu8c96vcv9dbxf	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-03-24 21:35:02.434352+03
572dme1ggqvk9n768eaobz6uzsezhb78	NWRhMTlkYzg0ZGE2ODk1OWFjOGI1ZWUyYTA0NGM3NjY3MWZhNDlhNjp7Il9tZXNzYWdlcyI6IltbXCJfX2pzb25fbWVzc2FnZVwiLDAsMjUsXCJZb3UgaGF2ZSBiZWVuIGxvZ2dlZCBvdXQsIFlvdSBjYW4gbG9nIGluIGFnYWluXCJdXSJ9	2020-05-16 10:50:00.775399+03
5l7vpi2yrljq84nohy5b7v2xai80n3jp	OTM4ZjE0ZWRkOWI4NjY4MjBlYzRkYjgxZGJjNDdiNDJmNTk2MDZjMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYTNiMmVlYTc3MTk3M2JlYTdlY2QxOTlhNjA4NWQzYjNiOTk4ODM0In0=	2020-07-07 17:02:07.508813+03
ux736od88zcvemgjdqvho0dwg9qtip3z	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-04-20 22:13:08.908562+03
u4tjzxv56kwuf26z6lhp7xah2fgqelms	Nzg3ODE0YjUzNDQ1MTJhNzYzZmVhYjEzZTgzODc1YWZkMzIxMzEyMDp7Il9hdXRoX3VzZXJfaWQiOiI5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMGViMWNmODEyYmRmYmNiZDhhNmEyYmUyMmNiZmU0OTQxNTRiZjU4In0=	2020-06-06 17:36:09.055874+03
9glgun8qpdvdnbbor55vdxvxw25x9vhs	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-04-30 20:58:52.479222+03
hl3hnklo73vk20r8n42my9c00ghgcd6w	OTM4ZjE0ZWRkOWI4NjY4MjBlYzRkYjgxZGJjNDdiNDJmNTk2MDZjMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYTNiMmVlYTc3MTk3M2JlYTdlY2QxOTlhNjA4NWQzYjNiOTk4ODM0In0=	2020-07-10 19:47:58.567504+03
zwsinwcywg9ahr1q6a3dg2ppbv1rh2i2	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-05-01 13:22:20.768225+03
46oqh3lv28wgucx22wm693ahgyek7ltw	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-05-04 21:31:29.674865+03
ww9wour7e4gug0wl9i8x6zkf5eyd2x7t	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-03-18 00:51:53.47057+03
no34dckcyjreobow3j2yolua52t9zg8h	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-05-08 13:35:21.460285+03
d9sewm9py8pjbf93s99ix25i4st94hlv	OTM4ZjE0ZWRkOWI4NjY4MjBlYzRkYjgxZGJjNDdiNDJmNTk2MDZjMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYTNiMmVlYTc3MTk3M2JlYTdlY2QxOTlhNjA4NWQzYjNiOTk4ODM0In0=	2020-07-13 09:46:17.284344+03
mlc2js1udxqghotp3ua0petc1p3554vy	OTM4ZjE0ZWRkOWI4NjY4MjBlYzRkYjgxZGJjNDdiNDJmNTk2MDZjMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYTNiMmVlYTc3MTk3M2JlYTdlY2QxOTlhNjA4NWQzYjNiOTk4ODM0In0=	2020-07-17 09:57:08.832272+03
kdqn18fgtbtm6fx9oi4p3ory8grazafp	ZTg2ZTdhMDBlOTZhNjI1YmJhMTNiNmI1MjUwMzRjZWNlZmNlMjA2Mjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1NjYxZDliZTg4OGNlMTQ2OTViYzI5YmEwOGJlNzYzMmJhZjgyMzlmIn0=	2020-06-10 15:42:10.191308+03
xdeqy9lzc05xnin2c6v0zzhr3pb7bvap	YmUwM2E3MGQ1NzQ1NjI5NzNmMWI2MWM5OGVjNDM5MDJiZTg4YTQ4OTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZDU3MDY3MDZjYjY0MzdkNzZmZmUwMGY4MGQxYjc1NzFmYzQ3MDhiIn0=	2020-06-14 15:29:54.183998+03
ve3mtwxiegy69ytb7cz22saowm9xwchc	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-05-08 23:49:08.424011+03
dqnzr5yfvanh9unh8pkzupqfy3utbxz4	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-03-18 21:23:32.475918+03
ou4mqzotkflis9jvp4nwaxrg8gv9c4wu	NzMzZTgwNmM2OTE0NWU3N2I3N2ZhOTQ2MWVlNDgzZDk0MDJmNWViZDp7Il9hdXRoX3VzZXJfaWQiOiIyNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODFkNDlkYWYwN2I3M2UyOTI0ZGY0MjI4MDJmZDI2MDZkYTI4MjJkMyJ9	2020-07-07 10:51:12.512652+03
41v6pjhpak40iq73l4b0wxlbg70jzz6c	YmUwM2E3MGQ1NzQ1NjI5NzNmMWI2MWM5OGVjNDM5MDJiZTg4YTQ4OTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZDU3MDY3MDZjYjY0MzdkNzZmZmUwMGY4MGQxYjc1NzFmYzQ3MDhiIn0=	2020-06-14 19:23:03.342406+03
djxaj3yhhilg7pmcefmfx2oqh7t7uzwk	MTg2MTE3ZTYzYTM3MDk3N2MzZDExNGY3NmZlYWY1ZDJiNjQ2NmM2YTp7fQ==	2020-07-11 18:08:36.127605+03
o6k61kjvtnzijdx3ajtam7yh1ceyqbxb	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-03-21 17:44:22.161281+03
he4maxacma5f4vwe62comqs7bwwj0ck7	OTM4ZjE0ZWRkOWI4NjY4MjBlYzRkYjgxZGJjNDdiNDJmNTk2MDZjMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYTNiMmVlYTc3MTk3M2JlYTdlY2QxOTlhNjA4NWQzYjNiOTk4ODM0In0=	2020-07-17 09:26:34.855586+03
43kz7hprzqywlp56fcomk0lrokvc9awv	OTM4ZjE0ZWRkOWI4NjY4MjBlYzRkYjgxZGJjNDdiNDJmNTk2MDZjMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYTNiMmVlYTc3MTk3M2JlYTdlY2QxOTlhNjA4NWQzYjNiOTk4ODM0In0=	2020-06-27 19:55:04.408491+03
y99xuvtoelr302iy1ouudq0m9oi9o85h	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-03-23 23:51:17.529098+03
htb0saeggjftyrthxhsn34pq4pehir4x	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-05-13 17:55:47.006186+03
fqdsxfqnta5oz3euayt1jv2xw2h86z07	OTM4ZjE0ZWRkOWI4NjY4MjBlYzRkYjgxZGJjNDdiNDJmNTk2MDZjMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYTNiMmVlYTc3MTk3M2JlYTdlY2QxOTlhNjA4NWQzYjNiOTk4ODM0In0=	2020-07-18 10:50:09.774741+03
iq2vd6v3ksc4z4i8rq72hxa58p8lyhyh	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-07-22 23:36:36.739915+03
gwz1rqxm8375djpxsvdsynaos1t2tamj	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-07-23 21:17:24.111422+03
262uyf0522sntu9a3ezc5tgahs2wom6e	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-02 20:56:20.975091+03
rx963fd9tp6vnik94oauoi40z1fbdpcq	YmUwM2E3MGQ1NzQ1NjI5NzNmMWI2MWM5OGVjNDM5MDJiZTg4YTQ4OTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZDU3MDY3MDZjYjY0MzdkNzZmZmUwMGY4MGQxYjc1NzFmYzQ3MDhiIn0=	2020-06-22 22:44:54.883516+03
z37l4orwpj6ozh8qdyoin9hhxvc1i832	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-04 02:09:34.262938+03
sbnprl16nefuk0mnmbpqqr7dtevl5z5n	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-05 22:32:58.29612+03
mzb9td2kkt6xonvveqmy2mm37m39n2xm	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-09 20:53:27.697844+03
ujarvk4d3bgf7zo8jkv9oy049id5jig9	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-10 23:41:51.43234+03
etbn022xuiys10voz7apxeb2r46faoys	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-13 19:17:06.24032+03
78jncid2jzkex5p1vcsv9n5663528spe	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-17 22:35:43.097616+03
azufao1aea1riuzadrad5kdzoytd8nnm	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-18 17:42:36.713449+03
3hhm4wkltph4y9vgy1af4og4f5r2n26u	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-20 22:19:10.576987+03
psr4iwft16qi9zssyisoxjlfyp73hzay	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-28 23:52:50.675245+03
uj3o87vsw9ovc51e4ec840pjzno1s5fs	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-05-09 16:21:58.421629+03
rhs1k9cim6kv8x056au7xp7ibo0y09tp	ZDNjYzJiNDYyYjVhNWYxODIwZDYzYWM1NzcxNzE1OTc0OTg0ZWI4NDp7Il9hdXRoX3VzZXJfaWQiOiIyNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNDBkODQ4MjQ5YzNlZjJhN2YzY2E0OTI5NjkzYTI5ZWZjZDE1M2MyZCJ9	2020-10-18 21:55:34.408018+03
m3imlsds8mct1udd6qr47fhu1hpdgkm1	MTg2MTE3ZTYzYTM3MDk3N2MzZDExNGY3NmZlYWY1ZDJiNjQ2NmM2YTp7fQ==	2020-05-10 14:54:03.544196+03
8nlo84tb4tx02f5raj1f50jo1ewyf9t3	NmRmMTlhMDY0NzJjNDRmMGIzMWYxMzMzYzM4Mjc4Yjk4OTIyZDgzZDp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmQwNjBjZWFiNWE5N2FhMzBkNmEwMGViYWNkMjkwOWFiN2MyNmFlMSJ9	2020-05-19 21:28:53.664877+03
m787nb4q7ynslmulso8i9ji4dzr8x3go	OTM4ZjE0ZWRkOWI4NjY4MjBlYzRkYjgxZGJjNDdiNDJmNTk2MDZjMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxYTNiMmVlYTc3MTk3M2JlYTdlY2QxOTlhNjA4NWQzYjNiOTk4ODM0In0=	2020-07-08 10:47:56.352227+03
yaw4wi6ccl58to9i5zjcx2yf6e46nq7o	MTg2MTE3ZTYzYTM3MDk3N2MzZDExNGY3NmZlYWY1ZDJiNjQ2NmM2YTp7fQ==	2020-05-16 10:50:01.605562+03
qz0w7wlgisv2yvxkme1fuoafrstgqiie	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-07-18 14:36:09.109711+03
pxjd75z2jdjhb8gbchdujq8iivq0ucl6	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-04 20:18:14.819712+03
wpjfzssar3o1nmzo0cm68hrg0i4jc1j5	OWUwNWNkODIwNTNjY2M0YmJmOGRjZTI4ODhkYWRkYTdhN2Q2ZGJkMTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYWE5MGQxMjRkODk2Y2IwYmMwMDlhMDBmMTMwNTg2MTNlMmEyOTcwIn0=	2020-03-24 22:51:52.085789+03
0n2145g2ot6reqjsnea3soz527tigh2o	MTg2MTE3ZTYzYTM3MDk3N2MzZDExNGY3NmZlYWY1ZDJiNjQ2NmM2YTp7fQ==	2020-08-06 23:04:03.670197+03
qfgc8v8m15ym54q4jom5iqyzgu8a512s	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-10 23:15:06.369905+03
9jn3hp7onwol6cwykzzcz0penn2x5x54	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-24 20:46:47.904415+03
i3el9gr7rprumnjkqc327lk9ial7fhk7	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-08-29 23:41:11.451714+03
2spf20f5wg88j2sgj1x8zof7kha943vx	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-09-10 10:58:59.225963+03
5tua8zi78y0wvbzze75aotm5ppcoi58h	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-09-16 16:35:47.349462+03
33snm0yszrwcu9ayr2f7h6jc0895ce41	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-09-29 11:32:16.017744+03
jbvt8fesotevi6nu5r1owilsgdou4d8y	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-10-11 21:07:57.123125+03
ih0so28t3th1amzey7umweg7nhm1lqnq	NTJkYjRkYzQ3ZWEwYzUwOTM4MDQyNTQ0ZWM3MzE5M2U1ZjhjNzU5Zjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2ZDQ2ZDcyNWZjZmU3MWE0ZWNjY2Y4MDI4MmYxYmQ0ZjA2ZGI4NTlmIn0=	2020-10-12 10:27:32.771679+03
bil6vuny8vzx7bd8ddypv1obru3zrwp8	ZjgzZTU0NTZmNDk3M2FlYTkxYmFjMGRjMDNmM2ZmMTJiMjhiNjE2Nzp7Il9hdXRoX3VzZXJfaWQiOiIyMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNDcwYjE2NTI0YWQ3Y2U1OGEzZWE5ZmUyOTIyNTEwNjg0YjliZjljZiJ9	2020-10-12 16:20:20.047673+03
\.


--
-- Data for Name: oauth2_provider_accesstoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.oauth2_provider_accesstoken (id, token, expires, scope, application_id, user_id, created, updated, source_refresh_token_id) FROM stdin;
\.


--
-- Data for Name: oauth2_provider_application; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.oauth2_provider_application (id, client_id, redirect_uris, client_type, authorization_grant_type, client_secret, name, user_id, skip_authorization, created, updated) FROM stdin;
1	IiTWFk8QlhPI6pGClFUpkc2D6cc57dA6Fvco84ML	http://django-oauth-toolkit.herokuapp.com/consumer/exchange/	confidential	authorization-code	JXj3LXOhdiWMweDbdLML81yedzcWDT8PHAHv0mMkXGWORfo1o72LYC2SCV51kNaZw2mKBgPUMEBEeFZqQ5xTAzaqgEXKw1FfmReWcHUNEFOLVup17ZYA04dgqSbnV9MW	ucc-bwaise	2	f	2020-04-27 11:46:53.198667+03	2020-04-27 11:57:16.83371+03
\.


--
-- Data for Name: oauth2_provider_grant; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.oauth2_provider_grant (id, code, expires, redirect_uri, scope, application_id, user_id, created, updated, code_challenge, code_challenge_method) FROM stdin;
\.


--
-- Data for Name: oauth2_provider_refreshtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.oauth2_provider_refreshtoken (id, token, access_token_id, application_id, user_id, created, updated, revoked) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 176, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 248, true);


--
-- Name: background_task_completedtask_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.background_task_completedtask_id_seq', 1, false);


--
-- Name: background_task_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.background_task_id_seq', 1, false);


--
-- Name: corsheaders_corsmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.corsheaders_corsmodel_id_seq', 1, false);


--
-- Name: dashboard_about_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_about_id_seq', 6, true);


--
-- Name: dashboard_annualconference_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_annualconference_id_seq', 5, true);


--
-- Name: dashboard_cashfloat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_cashfloat_id_seq', 16, true);


--
-- Name: dashboard_church_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_church_id_seq', 1, true);


--
-- Name: dashboard_contact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_contact_id_seq', 44, true);


--
-- Name: dashboard_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_event_id_seq', 10, true);


--
-- Name: dashboard_expenditures_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_expenditures_id_seq', 44, true);


--
-- Name: dashboard_gallery_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_gallery_id_seq', 6, true);


--
-- Name: dashboard_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_image_id_seq', 26, true);


--
-- Name: dashboard_members_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_members_id_seq', 100, true);


--
-- Name: dashboard_ministry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_ministry_id_seq', 6, true);


--
-- Name: dashboard_newconvert_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_newconvert_id_seq', 3, true);


--
-- Name: dashboard_news_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_news_id_seq', 8, true);


--
-- Name: dashboard_page_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_page_id_seq', 2, true);


--
-- Name: dashboard_pledgeitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_pledgeitem_id_seq', 26, true);


--
-- Name: dashboard_pledges_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_pledges_id_seq', 124, true);


--
-- Name: dashboard_pledgescashedout_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_pledgescashedout_id_seq', 15, true);


--
-- Name: dashboard_project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_project_id_seq', 2, true);


--
-- Name: dashboard_revenues_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_revenues_id_seq', 113, true);


--
-- Name: dashboard_salariespaid_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_salariespaid_id_seq', 19, true);


--
-- Name: dashboard_slider_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_slider_id_seq', 22, true);


--
-- Name: dashboard_staffdetails_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_staffdetails_id_seq', 3, true);


--
-- Name: dashboard_testing_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_testing_id_seq', 1, false);


--
-- Name: dashboard_theme_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_theme_id_seq', 16, true);


--
-- Name: dashboard_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_user_groups_id_seq', 1, false);


--
-- Name: dashboard_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_user_id_seq', 24, true);


--
-- Name: dashboard_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_user_user_permissions_id_seq', 56, true);


--
-- Name: dashboard_visitors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dashboard_visitors_id_seq', 1, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 420, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 62, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 151, true);


--
-- Name: oauth2_provider_accesstoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.oauth2_provider_accesstoken_id_seq', 1, false);


--
-- Name: oauth2_provider_application_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.oauth2_provider_application_id_seq', 1, true);


--
-- Name: oauth2_provider_grant_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.oauth2_provider_grant_id_seq', 1, false);


--
-- Name: oauth2_provider_refreshtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.oauth2_provider_refreshtoken_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: background_task_completedtask background_task_completedtask_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.background_task_completedtask
    ADD CONSTRAINT background_task_completedtask_pkey PRIMARY KEY (id);


--
-- Name: background_task background_task_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.background_task
    ADD CONSTRAINT background_task_pkey PRIMARY KEY (id);


--
-- Name: corsheaders_corsmodel corsheaders_corsmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.corsheaders_corsmodel
    ADD CONSTRAINT corsheaders_corsmodel_pkey PRIMARY KEY (id);


--
-- Name: dashboard_about dashboard_about_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_about
    ADD CONSTRAINT dashboard_about_pkey PRIMARY KEY (id);


--
-- Name: dashboard_annualconference dashboard_annualconference_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_annualconference
    ADD CONSTRAINT dashboard_annualconference_pkey PRIMARY KEY (id);


--
-- Name: dashboard_cashfloat dashboard_cashfloat_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_cashfloat
    ADD CONSTRAINT dashboard_cashfloat_pkey PRIMARY KEY (id);


--
-- Name: dashboard_church dashboard_church_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_church
    ADD CONSTRAINT dashboard_church_pkey PRIMARY KEY (id);


--
-- Name: dashboard_contact dashboard_contact_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_contact
    ADD CONSTRAINT dashboard_contact_pkey PRIMARY KEY (id);


--
-- Name: dashboard_event dashboard_event_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_event
    ADD CONSTRAINT dashboard_event_pkey PRIMARY KEY (id);


--
-- Name: dashboard_expenditures dashboard_expenditures_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_expenditures
    ADD CONSTRAINT dashboard_expenditures_pkey PRIMARY KEY (id);


--
-- Name: dashboard_gallery dashboard_gallery_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_gallery
    ADD CONSTRAINT dashboard_gallery_pkey PRIMARY KEY (id);


--
-- Name: dashboard_image dashboard_image_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_image
    ADD CONSTRAINT dashboard_image_pkey PRIMARY KEY (id);


--
-- Name: dashboard_members dashboard_members_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_members
    ADD CONSTRAINT dashboard_members_pkey PRIMARY KEY (id);


--
-- Name: dashboard_ministry dashboard_ministry_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_ministry
    ADD CONSTRAINT dashboard_ministry_name_key UNIQUE (name);


--
-- Name: dashboard_ministry dashboard_ministry_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_ministry
    ADD CONSTRAINT dashboard_ministry_pkey PRIMARY KEY (id);


--
-- Name: dashboard_newconvert dashboard_newconvert_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_newconvert
    ADD CONSTRAINT dashboard_newconvert_pkey PRIMARY KEY (id);


--
-- Name: dashboard_news dashboard_news_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_news
    ADD CONSTRAINT dashboard_news_pkey PRIMARY KEY (id);


--
-- Name: dashboard_page dashboard_page_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_page
    ADD CONSTRAINT dashboard_page_pkey PRIMARY KEY (id);


--
-- Name: dashboard_pledgeitem dashboard_pledgeitem_Item_That_Needs_Pledges_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_pledgeitem
    ADD CONSTRAINT "dashboard_pledgeitem_Item_That_Needs_Pledges_key" UNIQUE ("Item_That_Needs_Pledges");


--
-- Name: dashboard_pledgeitem dashboard_pledgeitem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_pledgeitem
    ADD CONSTRAINT dashboard_pledgeitem_pkey PRIMARY KEY (id);


--
-- Name: dashboard_pledges dashboard_pledges_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_pledges
    ADD CONSTRAINT dashboard_pledges_pkey PRIMARY KEY (id);


--
-- Name: dashboard_pledgescashedout dashboard_pledgescashedout_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_pledgescashedout
    ADD CONSTRAINT dashboard_pledgescashedout_pkey PRIMARY KEY (id);


--
-- Name: dashboard_project dashboard_project_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_project
    ADD CONSTRAINT dashboard_project_pkey PRIMARY KEY (id);


--
-- Name: dashboard_revenues dashboard_revenues_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_revenues
    ADD CONSTRAINT dashboard_revenues_pkey PRIMARY KEY (id);


--
-- Name: dashboard_salariespaid dashboard_salariespaid_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_salariespaid
    ADD CONSTRAINT dashboard_salariespaid_pkey PRIMARY KEY (id);


--
-- Name: dashboard_slider dashboard_slider_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_slider
    ADD CONSTRAINT dashboard_slider_pkey PRIMARY KEY (id);


--
-- Name: dashboard_staffdetails dashboard_staffdetails_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_staffdetails
    ADD CONSTRAINT dashboard_staffdetails_pkey PRIMARY KEY (id);


--
-- Name: dashboard_testing dashboard_testing_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_testing
    ADD CONSTRAINT dashboard_testing_name_key UNIQUE (name);


--
-- Name: dashboard_testing dashboard_testing_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_testing
    ADD CONSTRAINT dashboard_testing_pkey PRIMARY KEY (id);


--
-- Name: dashboard_testing dashboard_testing_slug_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_testing
    ADD CONSTRAINT dashboard_testing_slug_key UNIQUE (slug);


--
-- Name: dashboard_theme dashboard_theme_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_theme
    ADD CONSTRAINT dashboard_theme_pkey PRIMARY KEY (id);


--
-- Name: dashboard_user_groups dashboard_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user_groups
    ADD CONSTRAINT dashboard_user_groups_pkey PRIMARY KEY (id);


--
-- Name: dashboard_user_groups dashboard_user_groups_user_id_group_id_2c570fca_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user_groups
    ADD CONSTRAINT dashboard_user_groups_user_id_group_id_2c570fca_uniq UNIQUE (user_id, group_id);


--
-- Name: dashboard_user dashboard_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user
    ADD CONSTRAINT dashboard_user_pkey PRIMARY KEY (id);


--
-- Name: dashboard_user_user_permissions dashboard_user_user_perm_user_id_permission_id_550d0c70_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user_user_permissions
    ADD CONSTRAINT dashboard_user_user_perm_user_id_permission_id_550d0c70_uniq UNIQUE (user_id, permission_id);


--
-- Name: dashboard_user_user_permissions dashboard_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user_user_permissions
    ADD CONSTRAINT dashboard_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: dashboard_user dashboard_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user
    ADD CONSTRAINT dashboard_user_username_key UNIQUE (username);


--
-- Name: dashboard_visitors dashboard_visitors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_visitors
    ADD CONSTRAINT dashboard_visitors_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: oauth2_provider_accesstoken oauth2_provider_accesstoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_accesstoken_pkey PRIMARY KEY (id);


--
-- Name: oauth2_provider_accesstoken oauth2_provider_accesstoken_source_refresh_token_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_accesstoken_source_refresh_token_id_key UNIQUE (source_refresh_token_id);


--
-- Name: oauth2_provider_accesstoken oauth2_provider_accesstoken_token_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_accesstoken_token_key UNIQUE (token);


--
-- Name: oauth2_provider_application oauth2_provider_application_client_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_application
    ADD CONSTRAINT oauth2_provider_application_client_id_key UNIQUE (client_id);


--
-- Name: oauth2_provider_application oauth2_provider_application_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_application
    ADD CONSTRAINT oauth2_provider_application_pkey PRIMARY KEY (id);


--
-- Name: oauth2_provider_grant oauth2_provider_grant_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_grant
    ADD CONSTRAINT oauth2_provider_grant_code_key UNIQUE (code);


--
-- Name: oauth2_provider_grant oauth2_provider_grant_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_grant
    ADD CONSTRAINT oauth2_provider_grant_pkey PRIMARY KEY (id);


--
-- Name: oauth2_provider_refreshtoken oauth2_provider_refreshtoken_access_token_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refreshtoken_access_token_id_key UNIQUE (access_token_id);


--
-- Name: oauth2_provider_refreshtoken oauth2_provider_refreshtoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refreshtoken_pkey PRIMARY KEY (id);


--
-- Name: oauth2_provider_refreshtoken oauth2_provider_refreshtoken_token_revoked_af8a5134_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refreshtoken_token_revoked_af8a5134_uniq UNIQUE (token, revoked);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: background_task_attempts_a9ade23d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_attempts_a9ade23d ON public.background_task USING btree (attempts);


--
-- Name: background_task_completedtask_attempts_772a6783; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_attempts_772a6783 ON public.background_task_completedtask USING btree (attempts);


--
-- Name: background_task_completedtask_creator_content_type_id_21d6a741; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_creator_content_type_id_21d6a741 ON public.background_task_completedtask USING btree (creator_content_type_id);


--
-- Name: background_task_completedtask_failed_at_3de56618; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_failed_at_3de56618 ON public.background_task_completedtask USING btree (failed_at);


--
-- Name: background_task_completedtask_locked_at_29c62708; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_locked_at_29c62708 ON public.background_task_completedtask USING btree (locked_at);


--
-- Name: background_task_completedtask_locked_by_edc8a213; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_locked_by_edc8a213 ON public.background_task_completedtask USING btree (locked_by);


--
-- Name: background_task_completedtask_locked_by_edc8a213_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_locked_by_edc8a213_like ON public.background_task_completedtask USING btree (locked_by varchar_pattern_ops);


--
-- Name: background_task_completedtask_priority_9080692e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_priority_9080692e ON public.background_task_completedtask USING btree (priority);


--
-- Name: background_task_completedtask_queue_61fb0415; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_queue_61fb0415 ON public.background_task_completedtask USING btree (queue);


--
-- Name: background_task_completedtask_queue_61fb0415_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_queue_61fb0415_like ON public.background_task_completedtask USING btree (queue varchar_pattern_ops);


--
-- Name: background_task_completedtask_run_at_77c80f34; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_run_at_77c80f34 ON public.background_task_completedtask USING btree (run_at);


--
-- Name: background_task_completedtask_task_hash_91187576; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_task_hash_91187576 ON public.background_task_completedtask USING btree (task_hash);


--
-- Name: background_task_completedtask_task_hash_91187576_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_task_hash_91187576_like ON public.background_task_completedtask USING btree (task_hash varchar_pattern_ops);


--
-- Name: background_task_completedtask_task_name_388dabc2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_task_name_388dabc2 ON public.background_task_completedtask USING btree (task_name);


--
-- Name: background_task_completedtask_task_name_388dabc2_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_completedtask_task_name_388dabc2_like ON public.background_task_completedtask USING btree (task_name varchar_pattern_ops);


--
-- Name: background_task_creator_content_type_id_61cc9af3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_creator_content_type_id_61cc9af3 ON public.background_task USING btree (creator_content_type_id);


--
-- Name: background_task_failed_at_b81bba14; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_failed_at_b81bba14 ON public.background_task USING btree (failed_at);


--
-- Name: background_task_locked_at_0fb0f225; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_locked_at_0fb0f225 ON public.background_task USING btree (locked_at);


--
-- Name: background_task_locked_by_db7779e3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_locked_by_db7779e3 ON public.background_task USING btree (locked_by);


--
-- Name: background_task_locked_by_db7779e3_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_locked_by_db7779e3_like ON public.background_task USING btree (locked_by varchar_pattern_ops);


--
-- Name: background_task_priority_88bdbce9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_priority_88bdbce9 ON public.background_task USING btree (priority);


--
-- Name: background_task_queue_1d5f3a40; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_queue_1d5f3a40 ON public.background_task USING btree (queue);


--
-- Name: background_task_queue_1d5f3a40_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_queue_1d5f3a40_like ON public.background_task USING btree (queue varchar_pattern_ops);


--
-- Name: background_task_run_at_7baca3aa; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_run_at_7baca3aa ON public.background_task USING btree (run_at);


--
-- Name: background_task_task_hash_d8f233bd; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_task_hash_d8f233bd ON public.background_task USING btree (task_hash);


--
-- Name: background_task_task_hash_d8f233bd_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_task_hash_d8f233bd_like ON public.background_task USING btree (task_hash varchar_pattern_ops);


--
-- Name: background_task_task_name_4562d56a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_task_name_4562d56a ON public.background_task USING btree (task_name);


--
-- Name: background_task_task_name_4562d56a_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX background_task_task_name_4562d56a_like ON public.background_task USING btree (task_name varchar_pattern_ops);


--
-- Name: dashboard_expenditures_Member_Name_id_7bc96d06; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "dashboard_expenditures_Member_Name_id_7bc96d06" ON public.dashboard_expenditures USING btree ("Member_Name_id");


--
-- Name: dashboard_image_gallery_title_id_9676d8f3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_image_gallery_title_id_9676d8f3 ON public.dashboard_image USING btree (gallery_title_id);


--
-- Name: dashboard_ministry_leader_id_0375a831; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_ministry_leader_id_0375a831 ON public.dashboard_ministry USING btree (leader_id);


--
-- Name: dashboard_ministry_name_8f0d9dad_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_ministry_name_8f0d9dad_like ON public.dashboard_ministry USING btree (name varchar_pattern_ops);


--
-- Name: dashboard_newconvert_member_name_id_4386bbd2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_newconvert_member_name_id_4386bbd2 ON public.dashboard_newconvert USING btree (member_name_id);


--
-- Name: dashboard_pledgeitem_Item_That_Needs_Pledges_59dec05b_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "dashboard_pledgeitem_Item_That_Needs_Pledges_59dec05b_like" ON public.dashboard_pledgeitem USING btree ("Item_That_Needs_Pledges" varchar_pattern_ops);


--
-- Name: dashboard_pledges_Pledge_Made_By_Visitor_id_29b9481e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "dashboard_pledges_Pledge_Made_By_Visitor_id_29b9481e" ON public.dashboard_pledges USING btree ("Pledge_Made_By_Visitor_id");


--
-- Name: dashboard_pledges_Pledge_Made_By_id_e0f3dcfb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "dashboard_pledges_Pledge_Made_By_id_e0f3dcfb" ON public.dashboard_pledges USING btree ("Pledge_Made_By_id");


--
-- Name: dashboard_pledges_Reason_id_dff79f38; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "dashboard_pledges_Reason_id_dff79f38" ON public.dashboard_pledges USING btree ("Reason_id");


--
-- Name: dashboard_project_project_leader_id_6663714f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_project_project_leader_id_6663714f ON public.dashboard_project USING btree (project_leader_id);


--
-- Name: dashboard_revenues_Member_Name_id_7c5d9a45; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "dashboard_revenues_Member_Name_id_7c5d9a45" ON public.dashboard_revenues USING btree ("Member_Name_id");


--
-- Name: dashboard_staffdetails_Church_Member_id_f0684c0b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "dashboard_staffdetails_Church_Member_id_f0684c0b" ON public.dashboard_staffdetails USING btree ("Church_Member_id");


--
-- Name: dashboard_testing_name_7e84a135_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_testing_name_7e84a135_like ON public.dashboard_testing USING btree (name varchar_pattern_ops);


--
-- Name: dashboard_testing_slug_2766831f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_testing_slug_2766831f_like ON public.dashboard_testing USING btree (slug varchar_pattern_ops);


--
-- Name: dashboard_user_full_name_id_7c7af222; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_user_full_name_id_7c7af222 ON public.dashboard_user USING btree (full_name_id);


--
-- Name: dashboard_user_groups_group_id_54086039; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_user_groups_group_id_54086039 ON public.dashboard_user_groups USING btree (group_id);


--
-- Name: dashboard_user_groups_user_id_a915c7fc; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_user_groups_user_id_a915c7fc ON public.dashboard_user_groups USING btree (user_id);


--
-- Name: dashboard_user_user_permissions_permission_id_70269958; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_user_user_permissions_permission_id_70269958 ON public.dashboard_user_user_permissions USING btree (permission_id);


--
-- Name: dashboard_user_user_permissions_user_id_ea9b20c2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_user_user_permissions_user_id_ea9b20c2 ON public.dashboard_user_user_permissions USING btree (user_id);


--
-- Name: dashboard_user_username_f9d39e85_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX dashboard_user_username_f9d39e85_like ON public.dashboard_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: oauth2_provider_accesstoken_application_id_b22886e1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_accesstoken_application_id_b22886e1 ON public.oauth2_provider_accesstoken USING btree (application_id);


--
-- Name: oauth2_provider_accesstoken_token_8af090f8_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_accesstoken_token_8af090f8_like ON public.oauth2_provider_accesstoken USING btree (token varchar_pattern_ops);


--
-- Name: oauth2_provider_accesstoken_user_id_6e4c9a65; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_accesstoken_user_id_6e4c9a65 ON public.oauth2_provider_accesstoken USING btree (user_id);


--
-- Name: oauth2_provider_application_client_id_03f0cc84_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_application_client_id_03f0cc84_like ON public.oauth2_provider_application USING btree (client_id varchar_pattern_ops);


--
-- Name: oauth2_provider_application_client_secret_53133678; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_application_client_secret_53133678 ON public.oauth2_provider_application USING btree (client_secret);


--
-- Name: oauth2_provider_application_client_secret_53133678_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_application_client_secret_53133678_like ON public.oauth2_provider_application USING btree (client_secret varchar_pattern_ops);


--
-- Name: oauth2_provider_application_user_id_79829054; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_application_user_id_79829054 ON public.oauth2_provider_application USING btree (user_id);


--
-- Name: oauth2_provider_grant_application_id_81923564; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_grant_application_id_81923564 ON public.oauth2_provider_grant USING btree (application_id);


--
-- Name: oauth2_provider_grant_code_49ab4ddf_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_grant_code_49ab4ddf_like ON public.oauth2_provider_grant USING btree (code varchar_pattern_ops);


--
-- Name: oauth2_provider_grant_user_id_e8f62af8; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_grant_user_id_e8f62af8 ON public.oauth2_provider_grant USING btree (user_id);


--
-- Name: oauth2_provider_refreshtoken_application_id_2d1c311b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_refreshtoken_application_id_2d1c311b ON public.oauth2_provider_refreshtoken USING btree (application_id);


--
-- Name: oauth2_provider_refreshtoken_user_id_da837fce; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX oauth2_provider_refreshtoken_user_id_da837fce ON public.oauth2_provider_refreshtoken USING btree (user_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: background_task_completedtask background_task_comp_creator_content_type_21d6a741_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.background_task_completedtask
    ADD CONSTRAINT background_task_comp_creator_content_type_21d6a741_fk_django_co FOREIGN KEY (creator_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: background_task background_task_creator_content_type_61cc9af3_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.background_task
    ADD CONSTRAINT background_task_creator_content_type_61cc9af3_fk_django_co FOREIGN KEY (creator_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_expenditures dashboard_expenditur_Member_Name_id_7bc96d06_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_expenditures
    ADD CONSTRAINT "dashboard_expenditur_Member_Name_id_7bc96d06_fk_dashboard" FOREIGN KEY ("Member_Name_id") REFERENCES public.dashboard_members(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_image dashboard_image_gallery_title_id_9676d8f3_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_image
    ADD CONSTRAINT dashboard_image_gallery_title_id_9676d8f3_fk_dashboard FOREIGN KEY (gallery_title_id) REFERENCES public.dashboard_gallery(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_ministry dashboard_ministry_leader_id_0375a831_fk_dashboard_members_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_ministry
    ADD CONSTRAINT dashboard_ministry_leader_id_0375a831_fk_dashboard_members_id FOREIGN KEY (leader_id) REFERENCES public.dashboard_members(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_newconvert dashboard_newconvert_member_name_id_4386bbd2_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_newconvert
    ADD CONSTRAINT dashboard_newconvert_member_name_id_4386bbd2_fk_dashboard FOREIGN KEY (member_name_id) REFERENCES public.dashboard_members(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_pledges dashboard_pledges_Pledge_Made_By_Visit_29b9481e_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_pledges
    ADD CONSTRAINT "dashboard_pledges_Pledge_Made_By_Visit_29b9481e_fk_dashboard" FOREIGN KEY ("Pledge_Made_By_Visitor_id") REFERENCES public.dashboard_visitors(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_pledges dashboard_pledges_Pledge_Made_By_id_e0f3dcfb_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_pledges
    ADD CONSTRAINT "dashboard_pledges_Pledge_Made_By_id_e0f3dcfb_fk_dashboard" FOREIGN KEY ("Pledge_Made_By_id") REFERENCES public.dashboard_members(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_pledges dashboard_pledges_Reason_id_dff79f38_fk_dashboard_pledgeitem_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_pledges
    ADD CONSTRAINT "dashboard_pledges_Reason_id_dff79f38_fk_dashboard_pledgeitem_id" FOREIGN KEY ("Reason_id") REFERENCES public.dashboard_pledgeitem(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_project dashboard_project_project_leader_id_6663714f_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_project
    ADD CONSTRAINT dashboard_project_project_leader_id_6663714f_fk_dashboard FOREIGN KEY (project_leader_id) REFERENCES public.dashboard_members(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_revenues dashboard_revenues_Member_Name_id_7c5d9a45_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_revenues
    ADD CONSTRAINT "dashboard_revenues_Member_Name_id_7c5d9a45_fk_dashboard" FOREIGN KEY ("Member_Name_id") REFERENCES public.dashboard_members(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_staffdetails dashboard_staffdetai_Church_Member_id_f0684c0b_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_staffdetails
    ADD CONSTRAINT "dashboard_staffdetai_Church_Member_id_f0684c0b_fk_dashboard" FOREIGN KEY ("Church_Member_id") REFERENCES public.dashboard_members(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_user dashboard_user_full_name_id_7c7af222_fk_dashboard_members_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user
    ADD CONSTRAINT dashboard_user_full_name_id_7c7af222_fk_dashboard_members_id FOREIGN KEY (full_name_id) REFERENCES public.dashboard_members(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_user_groups dashboard_user_groups_group_id_54086039_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user_groups
    ADD CONSTRAINT dashboard_user_groups_group_id_54086039_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_user_groups dashboard_user_groups_user_id_a915c7fc_fk_dashboard_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user_groups
    ADD CONSTRAINT dashboard_user_groups_user_id_a915c7fc_fk_dashboard_user_id FOREIGN KEY (user_id) REFERENCES public.dashboard_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_user_user_permissions dashboard_user_user__permission_id_70269958_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user_user_permissions
    ADD CONSTRAINT dashboard_user_user__permission_id_70269958_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: dashboard_user_user_permissions dashboard_user_user__user_id_ea9b20c2_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dashboard_user_user_permissions
    ADD CONSTRAINT dashboard_user_user__user_id_ea9b20c2_fk_dashboard FOREIGN KEY (user_id) REFERENCES public.dashboard_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_dashboard_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_dashboard_user_id FOREIGN KEY (user_id) REFERENCES public.dashboard_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_accesstoken oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr FOREIGN KEY (application_id) REFERENCES public.oauth2_provider_application(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_accesstoken oauth2_provider_acce_source_refresh_token_e66fbc72_fk_oauth2_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_acce_source_refresh_token_e66fbc72_fk_oauth2_pr FOREIGN KEY (source_refresh_token_id) REFERENCES public.oauth2_provider_refreshtoken(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_accesstoken oauth2_provider_acce_user_id_6e4c9a65_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_acce_user_id_6e4c9a65_fk_dashboard FOREIGN KEY (user_id) REFERENCES public.dashboard_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_application oauth2_provider_appl_user_id_79829054_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_application
    ADD CONSTRAINT oauth2_provider_appl_user_id_79829054_fk_dashboard FOREIGN KEY (user_id) REFERENCES public.dashboard_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_grant oauth2_provider_gran_application_id_81923564_fk_oauth2_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_grant
    ADD CONSTRAINT oauth2_provider_gran_application_id_81923564_fk_oauth2_pr FOREIGN KEY (application_id) REFERENCES public.oauth2_provider_application(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_grant oauth2_provider_grant_user_id_e8f62af8_fk_dashboard_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_grant
    ADD CONSTRAINT oauth2_provider_grant_user_id_e8f62af8_fk_dashboard_user_id FOREIGN KEY (user_id) REFERENCES public.dashboard_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_refreshtoken oauth2_provider_refr_access_token_id_775e84e8_fk_oauth2_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refr_access_token_id_775e84e8_fk_oauth2_pr FOREIGN KEY (access_token_id) REFERENCES public.oauth2_provider_accesstoken(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_refreshtoken oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr FOREIGN KEY (application_id) REFERENCES public.oauth2_provider_application(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: oauth2_provider_refreshtoken oauth2_provider_refr_user_id_da837fce_fk_dashboard; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refr_user_id_da837fce_fk_dashboard FOREIGN KEY (user_id) REFERENCES public.dashboard_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

