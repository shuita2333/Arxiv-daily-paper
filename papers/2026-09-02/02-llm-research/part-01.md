# 🧠 大模型相关研究 | 2026年09月02日

> 本类共 **452** 篇论文：已确认 **431** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

---

### 1. [A collective capability boundary in frontier large language models on guideline-conformant and case-specific oncology decision-making](https://arxiv.org/abs/2608.28592)

**<font color=#1a73e8>作者：</font>** Zhang Sheng, Jinming Li, Wangyang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve high scores on medical knowledge examinations, yet real-world oncology is not a knowledge test--it is a sequence of guideline-pathway choices, escalation judgments, and commitments under uncertainty. Existing benchmarks largely measure factual recall, leaving open whether frontier LLMs share decision-path blind spots that combining models cannot fix. We built the Oncology Decision Boundary Benchmark (ODBB)--2,005 oncology decision points across NCCN guidelines and colorectal cancer cases--and evaluated nine frontier LLMs (four closed-source, five open-weight families) released between June 2025 and April 2026. A fully deterministic scorer (zero LLM inference) classified outputs into 14 failure types, independently validated by two oncologists (Cohen's weighted $\kappa$ = 0.939 and 0.790) on a 225-item stratified sample. Treating the nine as a pooled super-model, 42.1% (Wilson 95% CI 40.0--44.3%) of all items--35.7% of the 1,586 NCCN items and 66.4% of the 419 colorectal-cancer cases--were answered correctly by none, with failures concentrated in choosing between guideline pathways before reasoning within any: a consistent blind spot in clinical meta-judgment that likely requires architectural intervention rather than more training data. Two models tuned for decisiveness (GPT-5.5, Gemini 3.1 Pro Preview) made unsafe commitments three to five times more often than the seven cautious models without scoring higher. In 3--9% of items, models stated the correct next clinical step yet did not commit to it--failures of decision, not knowledge. Model quality is no longer the primary bottleneck for clinical LLM deployment; the binding constraint is the assumption that any single model can be the sole basis for a clinical decision. Progress requires architectures that detect when a model reaches its competence boundary and route the decision to a clinician.

---


### 2. [Statutory AI: Aligning Large Language Models With Legal Norms](https://arxiv.org/abs/2608.28593)

**<font color=#1a73e8>作者：</font>** Cindy Delage, Stéphane Canu, Marc Décombas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the increasing development of AI regulatory frameworks, ensuring that artificial intelligence systems, particularly generative models, operate in accordance with legal and ethical standards has become a critical priority. Existing proposals for AI alignment and value-guided behavior, however, face some limitations. Approaches such as Constitutional AI depend on human supervision, while broad normative frameworks like the Good-for-Humanity (GfH) principle may be overly general and ambiguous to provide actionable governance guidance. To overcome these limitations, we propose a hybrid approach called Statutory AI that employs pre-existing human-authored principles drawn from specific themes within a legal corpus. Specifically, Statutory AI uses legal texts as a constitutional framework, enabling AI systems to autonomously critique and revise their outputs according to established norms. It operates in two stages, both using Chain-of-Thought prompting. The first stage classifies the user prompt into one of the identified themes, while the second stage analyzes it in conjunction with relevant articles selected from the legal corpus of that theme. To illustrate the potential of our approach, we conducted an experiment involving 1,000 red-teaming prompts and five penal themes: discrimination, disclosure of confidential information, violence, fraud, and abuse of vulnerable persons. Statutory AI reduced harmful content by 52 to 59 percentage points across tested models, approximately 10 percentage points higher than standard Constitutional AI, while cutting computation time by over 50%.

---


### 3. [Paper Pilot: A Human-in-the-Loop Expert System for Evidence-Traceable Scientific Manuscript Generation in Applied Sciences](https://arxiv.org/abs/2608.28596)

**<font color=#1a73e8>作者：</font>** Nidhi Jha, Siddharth Chaudhary, Ajinkya Kulkarni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly embedded in scientific workflows for literature analysis, drafting, and review. Existing systems advance autonomous discovery and manuscript generation, but do not resolve the governance problem that arises when ideas, methods, results, and claims propagate through AI-assisted workflows without mandatory human approval or artifact-level traceability. This paper proposes Paper Pilot, a human-in-the-loop expert system for evidence-traceable scientific manuscript generation in applied sciences. It adapts the Collaborative Agent Reasoning Engineering (CARE) methodology to manuscript development through manuscript-owner approval gates, explicit no-pass criteria, claim classification, audit logging, advisory LLM review, and evidence-locked revision control. The framework defines eight approval gates across the idea-to-claim pipeline and distinguishes literature-grounded from artifact-grounded claims, requiring reported numbers and interpretations to remain traceable to approved evidence; its system prompt is openly released for deployment in ChatGPT, Gemini, Claude, or institutional LLM environments. As a first empirical validation, we evaluate the citation-grounding layer with a controlled, mechanically scored benchmark (two commercial LLMs, real arXiv papers, no LLM judge): under coverage pressure ungated drafters fabricated up to 25% of their citations and never flagged an evidence gap, whereas the same models under Paper Pilot's evidence-locked rules produced zero fabricated citations and surfaced the planted gaps as explicit placeholders. Preliminary results for result grounding, revision, and adversarial robustness point the same way; full evaluation is left to future work. Paper Pilot positions LLM-assisted writing as a controlled human-AI decision-support process rather than a fully autonomous authorship pipeline.

---


### 4. [The Race between Agentic AI Capabilities and Data Quality Control in Online Surveys](https://arxiv.org/abs/2608.28597)

**<font color=#1a73e8>作者：</font>** Sourav Panda, Hillmer Chona, Rupak Kumar Das 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online surveys are a foundational data collection instrument in a variety of fields, with attention checks serving as critical guardians of response quality. However, the rapid emergence of agentic AI (goal directed systems powered by a large language model (LLM) brain and/or a multimodal processing unit with tool-augmented capabilities) raises new questions about the robustness of these safeguards. We investigate how well agentic AI architectures can complete web-based surveys and pass standard attention checks. We evaluate a single-agent architecture capable of multimodal input processing and tool-based web interaction on a controlled survey sandbox. We analyze the problem from two perspectives. From an attack perspective, we demonstrate how structural vulnerabilities such as exposed DOM metadata and predictable option encoding allow agents to resolve attention checks through structured parsing only. From a defense perspective, we implement a mitigation strategy of DOM metadata obfuscation to remove semantic cues in text-based questions. We evaluate multiple open-source language and multimodal models to study capability and orchestration effectiveness. Based on our evaluations, we offer perspectives on how to simultaneously meet the needs of empiricists and agentic AI researchers.

---


### 5. [CDPR: Counterfactual Advantage-based Credit Assignment for Cost-Aware Sequential Medical Diagnosis](https://arxiv.org/abs/2608.28599)

**<font color=#1a73e8>作者：</font>** Qi Peng, Yi Cai, Changmeng Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical diagnosis is a step-by-step, cost-aware process: a physician orders examinations one at a time, observes the results, and updates the diagnosis before reaching a final conclusion. Most medical language models instead treat diagnosis as a one-pass classification task and ignore the trade-off between a test's value and its cost. We model diagnosis as a cost-aware sequential decision process and train the policy with reinforcement learning. The main difficulty is credit assignment: the only reliable signal comes once at the end of a long trajectory, so it scores a wasteful workup the same as an efficient one. We propose CDPR (Counterfactual Diagnostic Process Reward), which needs no expert labels and no learned critic. CDPR first finds the states where the policy hesitates, using the uncertainty of its action distribution, and then scores the chosen action by its advantage over the alternatives the policy itself would consider, estimated with short rollouts under a utility that balances correctness against test count, cost, and infeasible requests. A rollout cache reuses within-batch trajectories to keep the cost low. We integrate CDPR into GRPO and test it on one in-domain (MIMIC-IV) and two out-of-domain (ClinicalBench and a private hospital dataset) benchmarks. CDPR improves diagnostic accuracy while clearly reducing the number and cost of examinations.

---


### 6. [SHAPE of Chain-of-Thought in Math Reasoning](https://arxiv.org/abs/2608.28600)

**<font color=#1a73e8>作者：</font>** Jonghyun Song, Sangjun Song, Minjae Oh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong performance on mathematical reasoning benchmarks, yet the mathematically meaningful skills underlying their reasoning remain underexplored. We introduce \texttt{SHAPE}, a framework that analyzes Chain-of-Thought (CoT) trajectories through two lenses developed in mathematics education: (1) semantic spaces: the model's evolving mathematical interpretations of a problem (e.g., algebraic, geometric), and (2) heuristics: the specific mathematical actions taken within those spaces (e.g., simplifying the problem, working backward). We first use \texttt{SHAPE} to analyze the reasoning patterns of various models. Our findings reveal that the mathematical heuristics employed by a model better explain final answer correctness than traditional CoT features. Furthermore, models are likely to reach correct solutions by concentrating their reasoning effort within a few semantic spaces rather than exploring many disparate ones -- a pattern consistent with human behavior. Next, we utilize the \texttt{SHAPE} lens to evaluate whether post-training truly enhances mathematical proficiency. We find that reinforcement learning induces mode-seeking in heuristic usage. Lastly, we post-train LLMs by promoting diverse heuristics and demonstrate its effectiveness in improving accuracy. Overall, \texttt{SHAPE} provides a theoretically-grounded diagnostic framework for decoding LLM reasoning and offers a new path toward post-training LLMs for math reasoning. The code for our model is available at this https URL

---


### 7. [Leveraging Generative AI to Design Accessible Interactive Visualizations for Undergraduate Mathematics: A Six-Phase Workflow](https://arxiv.org/abs/2608.28601)

**<font color=#1a73e8>作者：</font>** Mahesh Sunkula, Kuan-Hua Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive visualizations support conceptual understanding in undergraduate mathematics, but building them has required programming expertise most instructors lack. Using a design-based research approach, we develop, deploy, and evaluate a six-phase workflow (Foundation, Customization, Mathematical Depth, Application, Accessibility, Pedagogical Control) that uses generative AI to build WCAG~2.2 Level~AA compliant visualizations without programming. The six phases structure every prompt, scaffold the AI's code generation, and define where human verification is applied. We ask whether the structure reliably yields correct and accessible tools, whether it runs both backward (reverse-engineering prompts from a finished tool) and forward (generating a tool from a plain-language idea), and what verification each phase requires. Across four deployed tools spanning calculus, multivariable calculus, and differential equations, we evaluate mathematical correctness against closed forms, accessibility through automated and manual screen-reader testing, and the errors that recurred. The structure produces structurally complete first-pass tools, but human verification remains mandatory at every phase: each output must be checked for mathematical correctness, accessibility, and pedagogical fit before the next phase begins. The workflow is platform-independent and serves both instructors and students.

---


### 8. [RegDivergence-101: An LLM Benchmark for Cross-Jurisdiction Regulatory Contradiction Detection in Life Sciences](https://arxiv.org/abs/2608.28607)

**<font color=#1a73e8>作者：</font>** Chuchu Wu, Zhiyin Zhou, Jingzhuo Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pharmaceutical sponsors developing a drug for both the United States and the European Union must reconcile guidance issued independently by the FDA and the EMA. Where the two agencies require substantively the same thing, a sponsor can file once; where they diverge, a single trial design risks rejection in one region; where one agency is silent on a point the other regulates, the sponsor must infer obligations. Today this reconciliation is performed manually by regulatory-affairs experts. We introduce cross-jurisdiction regulatory divergence detection: given an FDA requirement and an EMA requirement on the same topic, classify their relationship as AGREE, DIVERGE, or SILENT. SILENT is inherently directional (SILENT_FDA vs. SILENT_EMA); we record direction per pair and report per-direction F1 alongside the collapsed label. We release RegDivergence-101, a 101-pair expert-grounded pilot evaluation benchmark (labels grounded in three peer-reviewed FDA/EMA comparison studies and primary FDA/EMA/ICH guidance text; dual-annotation inter-annotator kappa = 0.85), and systematically characterise a four-method baseline hierarchy: lexical heuristic (0.511 macro-F1, 95% CI [0.411-0.605]), NLI cross-encoder (0.233), obligation-level Graph-RAG (0.663 [0.570-0.747]), and flat LLM judge / Claude Haiku (0.830 [0.747-0.908]). Three directional observations emerge at pilot scale (n = 101): SILENT is semantically detectable but invisible to entailment-only formulations; pair-level obligation graphs improve over lexical methods but trail flat-LLM context (CIs partially overlapping); and corpus-level graph construction is the indicated architectural target for large-scale silent-detection. RegDivergence-101 is a pilot release establishing the task formulation and baseline hierarchy; four unrepresented regulatory domains and an expansion roadmap are described in Section 7.

---


### 9. [Parametric Multimodal User Memory: Storing What Captions Cannot Carry](https://arxiv.org/abs/2608.28609)

**<font color=#1a73e8>作者：</font>** Bojie Li, Noah Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A personalized agent needs a user memory: a persistent model of who its user is. Today it is almost always text -- transcripts and captions retrieved by similarity. This serves the captionable half of a person ("my cat is named Bibi"), but discards the perceptual half no caption can hold: how a voice sounds, how a face reads across age and lighting, how tired someone sounds. We measure this loss across five modalities: a strong caption-based re-identifier recovers as little as 0.11 of a dedicated encoder's recall, collapsing toward chance on non-nameable signals.
We instead ground perceptual memory in the model, decomposing recall into two subproblems: a vision-language model grounds the referent in context (what and where), and a dedicated encoder extracts an identity key (who), stored as one inline token read by attention at generation with no external round-trip. Neither suffices alone -- the VLM identifies cross-age faces at only 0.54 recall where a face encoder reaches 0.81, and an ungrounded encoder recognizes a two-person-scene referent at 0.05 -- yet together they reach correct-region oracle (0.96), generalizing to multi-speaker audio and video. The recognition core is training-free: it reproduces the encoder's recall on any frozen model at O(1) registration cost. On PerceptMem (12 domains, 1,080 tasks) perceptual identity is capacity-limited while exact facts are binding-limited: identity belongs in a parametric bank, facts in a text store. The two memories compose cleanly: an agent with both can remember not only what its user said, but also what they are like.

---


### 10. [TPvG: A Moral Decision Framework for Large Language Models from One-Shot to Sequential Feedback](https://arxiv.org/abs/2608.28610)

**<font color=#1a73e8>作者：</font>** Fangyuan Zhang, Dong Yu, Pengyuan Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing LLM moral evaluations typically present models with isolated moral vignettes and elicit a single-shot decision, neglecting a factor known to profoundly influence human moral behavior: consequence feedback. We introduce TPvG (Text-based Pain-versus-Gain), adapted from a human moral paradigm, which embeds consequence feedback into an everyday moral dilemma of not harming others versus maximising self-gain. TPvG comprises five moral decision tasks, progressing from minimal-context one-shot choices to sequential decisions with explicit consequence feedback. Our results show that LLM moral decisions were strongly affected by decision format (one-shot versus sequential), and explicit receiver feedback produced heterogeneous effects across models. Furthermore, LLM responses to explicit receiver feedback diverged from the human reference pattern, suggesting potentially different decision processes. These findings highlight the need to evaluate whether LLM moral behavior remains stable in high-stakes interactive settings.

---


### 11. [Gurukul AI: An Interactive AI-Driven Educational Platform for Indian Education System](https://arxiv.org/abs/2608.28611)

**<font color=#1a73e8>作者：</font>** Isha Narang, Sneh Gosai, Mayank Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) like ChatGPT and LLaMA have transformed AI-driven education, but these systems are predominantly trained on Western-centric data, making them ill-suited for regional curricula like India's. The Indian education system is linguistically diverse, exam-oriented, and structured around standardized syllabi, not addressed by existing datasets or tools. In this work, we curate a syllabus-aligned QA dataset based on NCERT (National Council of Educational Research and Training) textbooks for classes 9-12, capturing the content, context, and teaching style of Indian curricula. The final dataset, comprising 18,720 question-answer pairs across five subjects, is publicly available at this https URL. We fine-tune the LLaMA 3.1 8B model using this dataset and deploy it in a Retrieval-Augmented Generation (RAG) framework tailored to educational needs. We introduce GurukulAI, an open-access platform that enables Indian students to chat with the model, get doubts cleared, practice exam-style questions, receive contextual answers, and interact in both English and Hindi. By localizing AI for Indian classrooms, our work bridges the gap between global LLM capabilities and regional educational demands. The code is available at this https URL.

---


### 12. [InternReviewer & InternAdvocate: Objective Reward and Evaluation for Agentic Reinforcement Learning in Peer Review and Rebuttal](https://arxiv.org/abs/2608.28612)

**<font color=#1a73e8>作者：</font>** Xuerui Su, Liya Guo, Qizhi Pei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating professional scholarly content, such as peer reviews and rebuttals, requires an intricate synergy between domain reasoning and factual grounding. This work presents a comprehensive framework for the development and evaluation of specialized scholarly agents, InternReviewer and InternAdvocate. We first establish a large-scale, high-quality scholarly dataset and integrate a high-efficiency arXiv retrieval tool to enable active evidence gathering. To optimize these agents, we implement an agentic Reinforcement Learning (RL) paradigm driven by a unified objective metric and reward system. This system avoids the biases of subjective model-based judging by employing multi-dimensional criteria, including reference-anchored semantic alignment, structural compliance, and a strict verification mechanism that cross-checks citations against real-time interaction logs to eliminate hallucinations. Experimental results demonstrate that agents trained within this closed-loop framework exhibit significant improvements in reasoning depth and citation accuracy.

---


### 13. [From GenAI Virtual Patient Dialogue Logs to Teacher-Interpretable Process Evidence: A Learning Analytics Study in Higher Education](https://arxiv.org/abs/2608.28619)

**<font color=#1a73e8>作者：</font>** Xinyu Li, Zijian Li, Mengyu Xia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical history taking is a dialogue-based clinical reasoning task in which learners must gather, organise, and integrate patient information while the consultation unfolds. Generative AI-powered virtual patients (GenAI VPs) make repeated history taking practice scalable and preserve full turn by turn dialogue. However, these logs are educationally difficult to use directly. Complete transcripts are too detailed for routine teacher review, whereas final scores obscure whether learners followed up patient cues, checked uncertainty, or used summaries to guide later questioning. This study examined whether coded GenAI VP dialogues can provide teacher-interpretable process evidence of clinical reasoning. We analysed 1{,}030 GenAI VP dialogues from 210 second-year medical learners across five weeks chest-pain cases. Each consultation was teacher-scored using a rubric assessing the full history taking dialogue, and consultations were classified within each week as high- or low-rated using the weekly median score. To explain how rated performance was reflected in the dialogue process, we applied three analytic layers to the same coded dialogue data: behavioural prevalence, local co-occurrence using Epistemic Network Analysis, and sequential transition using Transition Network Analysis. High-rated consultations involved more history taking activity, but differences were not simply about volume. High rated consultations more often connected information gathering and symptom exploration with communication, checking, organisation, and synthesis. Summarising and organising moves more often led to verification or mechanism-oriented follow-up. These findings show how layered analysis of GenAI VP dialogue logs can reveal process patterns associated with high rated history taking and support process-focused feedback in medical education.

---


### 14. [Looking Again: Measuring Sycophancy in the Reasoning Chains of Multimodal Models Under Pressure](https://arxiv.org/abs/2608.28623)

**<font color=#1a73e8>作者：</font>** Mahir Numayeer Islam, Gakuto Okuyama, Nikolaus Siauw 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large multimodal reasoning models (LMRMs) are getting increasingly capable, primarily through generating explicit chain-of-thought reasoning before answering. In language models it has been observed that this performance often comes with sycophancy, the tendency of a model to agree with the user over the evidence. However, for LMRMs no reliable method to measure sycophancy yet exists. We bridge this gap by introducing a benchmark and dataset for evaluating LMRM sycophancy when confronted with a wrong answer from a user. Our benchmark pairs four visually grounded datasets spanning mathematical, clinical, temporal, and demographic reasoning with five pressure conditions in single-turn and multi-turn settings. We evaluate sycophancy in the final answer as well as its emergence within the reasoning chain. We find that sycophancy is prevalent under pressure, with Statement pressure eliciting the highest rates and Conviction the lowest for all models except Mistral-Small-4, and under multi-turn pressure reasoning-level sycophancy intensifies sharply in clinical visual judgement, reaching 95.7% for the most affected model. We further introduce a failure taxonomy separating reasoning-chain from answer-level sycophancy, and a complementary sentence-level taxonomy locating where in the chain drift first emerges. Our results show that sycophancy can corrupt the reasoning chain independently of the final answer, so answer-level evaluation alone is insufficient.

---


### 15. [MA-RAG: Multi-Agent Retrieval-Augmented Generation for Query-Driven Summarization of Longitudinal Parkinson's Disease Assessments](https://arxiv.org/abs/2608.28624)

**<font color=#1a73e8>作者：</font>** Sana Alamgeera, Denise Goberta, Muhammad Irshad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurate interpretation of single-visit and longitudinal clinical assessments for Parkinson's disease is time-consuming and often depends on specialist expertise. Although large language models (LLMs) can generate natural language summaries, they frequently lack domain-specific clinical grounding and struggle to produce factually correct and temporally consistent responses for structured longitudinal assessment data. To address these limitations, we propose MA-RAG, a query-driven multi-agent retrieval-augmented generation framework that decomposes clinical reasoning into domain-specialized agents, combines structured fact extraction, and synthesizes clinically grounded summaries through a final verification stage. The framework supports four clinical analysis tasks: single-session, trajectory, comparison, and cohort summarization. We evaluate MA-RAG using objective metrics, namely Fact Precision, Hallucination Rate, Temporal Fidelity, and Semantic Similarity, together with subjective evaluations conducted by clinical experts. Compared to Traditional, RAG-only, and Single-agent RAG baselines, MA-RAG substantially improves factual correctness, achieving up to a 122% relative increase in Fact Precision (from 0.436 to 0.990) and reducing the Hallucination Rate by up to 98% (from 0.564 to 0.010), while consistently receiving top ratings from clinical experts for organization and clinical usefulness. These results demonstrate that domain-specialized multi-agent reasoning enables reliable query-driven summarization of structured longitudinal clinical assessment data.

---


### 16. [Do large language models scrutinise what they review? A multimodal audit of scoring calibration, error detection, and author-identity effects](https://arxiv.org/abs/2608.28626)

**<font color=#1a73e8>作者：</font>** Emad Alharbi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate peer reviews, prompting examination of their capacity for critical evaluation. This study evaluates two multimodal LLMs, Qwen2.5-VL-72B and Pixtral-Large-124B, as reviewers across 165 submissions to the 2026 International Conference on Learning Representations, a venue that postdates both models' training cutoffs. Manuscripts were presented to both models with author identities blinded, replaced with high-prestige affiliations, or replaced with low-prestige affiliations, and in either text-only or text-with-figure format. Additionally, 145 verifiably detectable errors were inserted into 55 manuscripts to assess error identification under natural and verification-oriented prompts. Across all manuscript groups, including rejected submissions, LLM scores ranged from 7.0 to 8.1, whereas human mean scores ranged from 3.4 to 6.8. The models detected 12.1\% of the verified errors under natural prompting, and a one-sentence verification instruction increased detection to 22.2\%; however, 78\% of the errors remained undetected. Providing figures reduced error detection while increasing review scores. No visual error was reliably verified against its corresponding figure, and half of the text-only reviews described figures that were not provided. Author identity did not influence either review scores or error detection. LLM editorial decisions exactly matched those produced by simple score averaging.

---


### 17. [CDEP Agent: Connecting Meteorologically Detected Temporal Compound Events to Real-World Documentary Evidence](https://arxiv.org/abs/2608.28628)

**<font color=#1a73e8>作者：</font>** Zhuoran Li, Weiyi Kong, Boer Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compound drought-to-extreme-precipitation (CDEP) events are recognized in climate science as a growing driver of extreme impact, but whether this recognition carries over into real-world early warning and post-event documentation is unknown, so a meteorologically real CDEP event may pass with neither advance warning nor any later record. Here we present CDEP Agent, an auditable LLM-agent framework that tests this mismatch directly by linking CDEP candidates detected from meteorological reanalysis to real-world hazard and impact evidence across sources with different spatial scales, temporal resolutions, and reporting conventions. Using California as a case study, we identify 408 candidate CDEP events from ERA5 observations during 2021-2025 and evaluate each against the U.S. Drought Monitor, NOAA Storm Events, and public webpages along five dimensions: antecedent drought, extreme rainfall, local impact, hazard-impact attribution, and explicit drought-to-rainfall linkage. Only 34.3% of candidates are corroborated on both hazard components, and just 1.5% are ever explicitly linked to their antecedent drought, indicating that most meteorologically detected CDEP events go undocumented and their compound nature almost never enters the record at all. Our framework gives climate scientists a way to test physical event definitions against what actually gets documented, and gives social scientists, economists, and disaster-response agencies a provenance-linked evidence base for compound events that current warning and reporting systems largely fail to capture.

---


### 18. [Intelligent Identification and Repair of Design Defects in BIM via Domain-Specific Large Language Models](https://arxiv.org/abs/2608.28629)

**<font color=#1a73e8>作者：</font>** Jia-Rui Lin, Yun-Hong Cai, Xiang-Rui Ni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing methods lack a generalized approach to efficiently identify and resolve the diversity of design defects in BIM. Therefore, this study proposes an integrated framework to identify and repair various defects in BIM via domain-specific LLMs. Firstly, a BIM-to-Text method with component-balanced chunking is introduced to bridge BIM data with LLMs. Then, prompt learning with rule injection, few-shot prompting and RAG is proposed to identify defects and generate repair suggestions. Meanwhile, a hallucination control strategy combining key identifier validation and token-length thresholds is introduced to ensure reliability. Experiments show capability expansion yields 85% identification accuracy versus 70% for traditional rule checking, achieving a 94% rate of reasonable repair suggestions. Moreover, the proposed hallucination control further increased accuracy from 64% to 85%, eliminating 92.5% of hallucinations in a single intervention round. This study establishes an end-to-end prototype from raw BIM data input, through defect identification, to repair suggestion generation.

---


### 19. [Enabling Proactive Spoken Turns via a Generalized Style-Aware Full-Duplex Framework](https://arxiv.org/abs/2608.28630)

**<font color=#1a73e8>作者：</font>** Tianrui Pan, Qinglin Zhang, Chong Deng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Compared with half-duplex dialogue systems where the system waits for user turn completion before it responds, natural full-duplex dialogue systems require agents to act proactively in real time, including timely interruptions and backchannels. This creates a key challenge: improving turn timing without sacrificing response quality. To address limitations in realistic proactive turn-taking, we build a generalized style-aware full-duplex framework with three key components. Firstly, we propose LPS-TC, a Lightweight Proactive Speech Turn Controller for plug-and-play integration. It features a fine-grained action space covering both reactive and proactive turn behaviors, enabling half-duplex models with full-duplex capabilities and enhancing existing full-duplex models with superior timing control. Secondly, we construct WildTurn, a large-scale, real-world English dataset containing approximately 2,981 hours of filtered multi-turn stereo conversations from face-to-face and telephone conversations, annotated with five turn-taking and five backchanneling styles. Trained on WildTurn, LPS-TC exhibits rich spoken dynamics that are not captured by existing static full-duplex benchmarks. Thirdly, we introduce a two-tier evaluation scheme that assesses both chunk-level timing precision and turn-level interaction quality under realistic streaming constraints. Our experiments, integrating LPS-TC with half-duplex models like Qwen2.5-Omni and full-duplex models like Freeze-Omni, showcase its superior performance in timing appropriateness and response quality. Our framework also demonstrates fine-grained style controllability and strong generalizability, enabling more natural and human-like spoken interactions.

---


### 20. [AutoScientist-Quant: Self-Evolving Coding Agents for Automatic Research in Quantitative Investment](https://arxiv.org/abs/2608.28632)

**<font color=#1a73e8>作者：</font>** Zongqian Li, Yaoyiran Li, Yaohui Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents can discover alphas, yet current methods have three weaknesses. The search cannot adapt during the run, automation usually ends at alpha generation while library selection and model choice stay manual, and alpha discovery can read the test window through loop feedback or code problems. We present AutoScientist-Quant, a self evolving search process that regards quantitative research as one budgeted search problem. A single controller conditions every decision on the remaining budget, choosing at each round whether to improve, combine, pivot, or stop, which node to expand, how many alphas to generate, and how to retrieve past trajectories from the shared memory. The same core then selects from the library and tunes the model, closing the loop from hypothesis to deployable strategy. We also review the evaluation pipeline reused from prior work, fix two lookahead problems, and keep the feedback window disjoint from the held out test window, so every comparison tests true generalization. On CSI universes, the framework attains the best value of nearly every metric in every setting, and these conclusions hold across several backbones and markets.

---


### 21. [PAUSE: Editable Strategy Artifacts for Long-Form Cultural Story Adaptation](https://arxiv.org/abs/2608.28633)

**<font color=#1a73e8>作者：</font>** Taaha Kazi, Vasu Sharma, Mohammad Saifullah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative AI systems increasingly mediate cultural adaptation, but their cultural decisions are often hidden inside prompts, transient model plans, or final prose. We study PAUSE (Pause-And-Update Strategy Editing), an intervention that exposes an editable adaptation strategy as a human control surface for cultural decisions in long-form story adaptation. The strategy is a structured artifact that can be inspected, edited, and then projected through downstream character, entity, and chapter-localization stages. In two Chinese-source serialized novels, we test whether human edits to this strategy propagate into chapter-level prose. Across 9 edited-vs-control chapter comparisons, judges select the edited-strategy output in all 9; a marker audit shows target markers in 8/9 edited outputs and 0/9 controls, with forbidden markers absent from edited outputs and present in all controls. We frame these results as a smoke-scale edit-adherence study, not a claim that the outputs are culturally authoritative or literary-quality improvements. PAUSE offers one practical way to make AI-mediated cultural adaptation more inspectable and contestable before decisions propagate through long-form generation.

---


### 22. [Do MLLMs Really Understand Low-Resource Khmer Documents? A Pilot Study on Khmer Document VQA](https://arxiv.org/abs/2608.28635)

**<font color=#1a73e8>作者：</font>** Nimol Thuon, Panhapin Theang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) have advanced document understanding, visual question answering, and text extraction. However, their reliability in low-resource, non-Latin settings remains uncertain. Khmer form documents present particular challenges because they contain complex script forms, mixed Khmer-English fields, and monetary values in both Cambodian Riel and US Dollars. Available resources for Khmer Document VQA are also limited. This paper presents a pilot diagnostic evaluation of open MLLMs on Khmer document images. We construct an evaluation subset from the previously introduced KH-FUNSD collection, covering invoices, receipts, quotations, and other business forms. The subset includes questions in English and Khmer, with answers retained in their original English, Khmer, mixed-script, or numeric forms. Rather than introducing a full public benchmark, this study examines the capabilities and failure modes of existing models. We evaluate representative open Qwen-VL models using direct image-based prompting and compare parser-assisted and external OCR-assisted configurations with Qwen3-VL-8B. Direct Qwen3-VL-8B outperforms smaller models, achieving 51.9% overall accuracy, although performance remains limited for Khmer-script and mixed-script answers. External OCR produces the strongest results, reaching 61.9% with Tesseract and 61.6% with PaddleOCR. Nevertheless, Khmer-script answers remain substantially more difficult than English and numeric fields. The results indicate that current MLLMs can process visually clear English and structured numeric content, but reliable native Khmer document understanding remains an open challenge.

---


### 23. [Self-Evolving Skills via Surrogate-Guided Solve-and-Reproduce](https://arxiv.org/abs/2608.28638)

**<font color=#1a73e8>作者：</font>** Jiale Liu, Pinze Ren, Yuqi Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills are portable packages of instructions and resources an agent consults at deployment. Self-evolving them fails in two ways today. First, skills evolved from scratch underperform human-curated ones and, on a weak model, using no skill at all. Second, an evolution-time pass records one lucky trajectory that a fresh stochastic agent often fails to reproduce at deployment. We present reSolve, a per-task, oracle-in-the-loop framework built on three components. It decouples interactive solving from a self-contained deliverable that is independently re-executed in a fresh container, a protocol we call solve-and-reproduce. It enhances the sparse reward signal with a surrogate verifier that cannot access hidden tests or reference answers. It then runs verifier-guided beam search over a solution-construction graph. Within a fixed harness, a cheap model self-evolves skills that reach $74.9\%$ mean-of-3, $+14.8$ points over the $60.1\%$ human-curated baseline, exceeding the strongest official curated-skill result ($67.3\%$, GPT-5.5/OpenHands). We also report observed failure cases and domain-level results, including performance on the 14 Natural Science tasks, to clarify when the approach does and does not help.

---


### 24. [Reward-Oracle MCTS for Formal Theorem Proving: Sample-Efficient Search and the Need for Kernel-Level Proof Auditing](https://arxiv.org/abs/2608.28639)

**<font color=#1a73e8>作者：</font>** Bodla Krishna Vamshi, Haizhao Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formal theorem proving with large language models remains challenging due to the difficulty of navigating large proof search spaces efficiently. Existing tree search approaches either feed verbose compiler error messages directly into the generation context, increasing context usage during search, or employ non-standard evaluation protocols that prevent direct comparison with established baselines. We propose a three-role Monte Carlo Tree Search (MCTS) framework that treats the Lean 4 compiler purely as a reward oracle using compiler output as a scalar signal for UCB-guided tree updates without feeding error content into the generation context. Our framework decomposes proof search into three roles: a generator for proof attempts, a decomposer for subgoal decomposition, and a critic for subgoal quality evaluation. We evaluate across 4 benchmarks spanning competition mathematics and physics (MiniF2F, PutnamBench, LeanPhysBench, PhysLeandata) with three prover models at standard proof attempt budgets (PAB@16 to PAB@256). Our method achieves 87.1\% on MiniF2F with Goedel-Prover-V2-8B at PAB@256 and solves 26/659 PutnamBench problems at PAB@32 surpassing base sampling 18/659 at same proof attempt budget. Through an exhaustive axiom-level audit of every compiled proof, we further identify reward hacking in search-based theorem proving: DeepSeek-Prover-V2-7B produces proofs on PutnamBench that pass compilation and the standard sorry-token scan while depending on sorryAx. The audit removes 4 and 8 such proofs from whole-proof sampling at PAB@32 and PAB@128, and 11 and 19 from MCTS. We do not attribute these counts to the search procedure; we report them to establish that kernel-level auditing is necessary for compiler-verified evaluation.

---


### 25. [Terminal-Bench-LILT: Multilingual Agentic Coding Benchmark Grounded in Language, Region, and Culture](https://arxiv.org/abs/2608.28641)

**<font color=#1a73e8>作者：</font>** Yunsu Kim, Kaden Uhlig, Ashwin Purohit 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most evaluations for coding agents are conducted exclusively in English, which does not reflect real-world multilingual deployment. We present Terminal-Bench-LILT, a suite of 300 authentic coding tasks in ten languages: Arabic, Czech, German, Spanish, Hindi, Japanese, Korean, Serbian, Turkish, and Chinese. Each task targets issues specific to non-English software development that have no direct English equivalent, e.g., internationalization, encoding, text normalization, and cultural conventions. All tasks are authored by native-speaker programmers and validated through a multi-stage quality control pipeline. Evaluation of six frontier models reveals that even the strongest model reaches only 63.1\% pass rate, with many tasks unsolved by any model. Performance varies substantially by language and does not track general coding benchmark rankings, highlighting that multilingual coding competence is a distinct and underexplored capability axis. Sample tasks are available at this https URL

---


### 26. [Cross Lingual Transfer in Tulu Legal Comprehension: Script-Dependent Improvement and RAG-Induced Knowledge Conflict](https://arxiv.org/abs/2608.28645)

**<font color=#1a73e8>作者：</font>** Sindhu Shetty, Spurthi Setty, Natan Vidra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-resource languages without an adequate training corpus often use a related, higher-resource language as a scaffold for comprehension. Still, there is a need to develop rigorous evaluation methods to identify when models fail in cross lingual low-resource environments. Using the legal domain as a backdrop, three models (Llama3, Hex-1, Sarvam) were tested on the ability to classify legal complaints written in a low resource Dravidian language (Tulu). Transliterating queries across Dravidian scripts allowed models to gain a preliminary understanding of speakers' complaints without the use of wide scale training, though the level of comprehension was heavily script dependent (with Kannada - another relatively low-resource language - producing the strongest positive trend). Retrieving from a corpus of Kannada legal papers across a RAG framework caused mixed results. Some models had a weak positive trend in comprehension under certain conditions, but when models failed, it was often across two axes: fact substitution (fixating on specific passage excerpts that skewed reasoning) and confabulation (hallucination that had no basis in either query or corpus). Within low resource domains, results identify the model's parsing of information and subsequent reasoning as the source of reasoning failure, rather than corpus contents. Script-dependent comprehension and RAG robustness also seem to travel together. This is further supported by the reasoning-trace analysis and a statistical-honesty framework deployed - techniques that are more broadly applicable to low-resource multilingual RAG evaluation.

---


### 27. [Self-Specialized Teachers for Domain Post-Training](https://arxiv.org/abs/2608.28647)

**<font color=#1a73e8>作者：</font>** Yifei Li, Rongman Xu, Lingling Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Target-only post-training can improve performance in a specialized domain while degrading behaviors that a general-purpose base model acquired before adaptation. We study this problem when target-domain data are available but a representative replay corpus is not. We propose self-specialized teacher distillation (SSTD), a two-stage procedure that first trains a copy of the base model into a domain teacher, then distills its token distribution to a student on prefixes sampled from the student itself. Teacher training combines standard target supervision with base-aware key-token weighting and distribution alignment to the frozen base model; on-policy distillation then places domain feedback on states the student can encounter at inference time. On financial numerical reasoning, medical question answering, and legal holding identification, SSTD retains much of the target improvement of direct fine-tuning while improving the mean score on the evaluated general suite by 4.8--5.0 points at the reported operating point. The pattern persists across Qwen3 sizes and on Gemma backbones. SSTD requires neither an external teacher nor general replay data.

---


### 28. [How Language Models Choose Sides: Internal Representations of Instruction Hierarchy](https://arxiv.org/abs/2608.28648)

**<font color=#1a73e8>作者：</font>** Enrique Balp-Straffon, Chih-Hao Hsu, Rushiraj Gadhvi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how instruction-tuned LLMs arbitrate direct conflicts between system and user instructions. We introduce a benchmark of 41 paired constraints with deterministic verifiers and evaluate eight models under matched baseline, conflict, and same-channel control conditions. Behaviourally, the models split into three regimes by System Authority Delta: hierarchy-respecting models use the system channel as an authority signal, anti-hierarchy models follow the system less often than their same-channel baseline predicts, and no-effect models show little channel sensitivity. Llama-3.1-8B is the strongest anti-hierarchy case in our suite, following the system in only 0.10 of conflict trials. We use this behavioural failure case to ask whether user-preferring arbitration reflects the absence of an internal conflictresolution signal. It does not: on Llama-3.1-8B, the conflict outcome is linearly decodable from residual-stream activations at 0.97 balanced accuracy, 17 percentage points above a metadata-only baseline, with analogous signals on Qwen2.5-7B and gpt-oss-20b. Steering with a layer-12 mean of four per-conflict logistic-regression directions raises genuine system compliance from 0.132 to 0.530, while directions selected mainly for pooled separability steer poorly. User-preferring conflict resolution can therefore coexist with a readable internal arbitration signal, and successful intervention depends on the geometry of the readout rather than probe accuracy alone

---


### 29. [Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?](https://arxiv.org/abs/2608.28649)

**<font color=#1a73e8>作者：</font>** Jinqi Wu, Sishuo Chen, Zhangming Chan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Touchpoint selection in conversion attribution, namely identifying meaningful touchpoints contributing to conversions, is essential for e-commerce recommendation and online advertising. Current selection methods rely heavily on collaborative-filtering-based heuristics, which fail to align with user-perceived semantic intent. Through human annotation, we reveal a significant semantic gap: many implicitly-related, semantically relevant touchpoints remain undetected by existing rules. Therefore, we systematically evaluate the capability of Large Language Models (LLMs) in identifying these hidden associations. Our evaluation shows that while LLMs effectively uncover a substantial portion of implicitly-related touchpoints, significant room for improvement remains in their selection performance. Furthermore, we analyze the impact of different prompting strategies and foundation model choices on identification performance, providing valuable insights into their reasoning patterns and effectiveness. These insights offer a new roadmap for transitioning conversion attribution from mechanical rule-matching to human-aligned semantic reasoning. Moreover, we leverage the LLM-attributed conversion labels for enhancing industrial CVR model training and achieve significant offline performance gains, showing the potential of LLMs in conversion attribution.

---


### 30. [A Generalized Optimization Engine (GOE) for Edge AI Inference Acceleration](https://arxiv.org/abs/2608.28652)

**<font color=#1a73e8>作者：</font>** Venkat R. Dasari, Jakob A. Adams, Vinod K. Mishra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) models have demonstrated remarkable capabilities across various domains, yet their widespread deployment is impeded by significant computational costs, particularly on resource-constrained devices. This paper explores the theoretical underpinnings of various AI model optimization techniques, algorithms, and abstractions, discussing their potential to reduce computational complexity, memory footprint, latency, and power consumption. Furthermore, we propose a comprehensive hardware (HW) and model-agnostic generalized optimization architecture that integrates these techniques for improved efficiency. Our study underscores the critical role of such a generalized optimization system in preparing model deployment over resource-constrained heterogeneous hardware in a tactical environment. As a concrete demonstration, we show that GOE-compressed language models deploy and run on a GPU-less edge CPU, and that the choice of compression method, not merely its nominal bit-width, determines whether task accuracy survives deployment.

---


### 31. [Test-Time Scaling for Scientific Equation Discovery](https://arxiv.org/abs/2608.28660)

**<font color=#1a73e8>作者：</font>** Haowei Lin, Hubert Lim, Xiangyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling (TTS) improves language model reasoning by allocating additional test-time compute, but prior work mainly studies closed-ended tasks such as math and coding. We study TTS for automated equation discovery, an open-ended setting where models search over candidate equations and rely on observed datapoints for feedback. We formulate LLM-driven equation discovery as an iterative search process that unifies Best-of-N, sequential refinement, tree search, and evolution-style methods under a common compute-allocation view. To isolate allocation effects from prompt engineering and other heuristics, we compare minimal parallel controllers under fixed budgets. On LLM-SRBench equation-discovery tasks, we find that search width is the dominant allocation parameter: the best width in our sweep generally increases with the compute budget, while the population--branching split and controller choice matter less. Appropriate width selection also improves wall-clock efficiency by increasing parallelism. These results suggest that, given an informative verifier, controlling exploration and exploitation is central to scaling LLM-based equation discovery.

---


### 32. [FRAC-MAS: A Safe and Explainable Multi-Agent System for Fracture Diagnosis](https://arxiv.org/abs/2608.28662)

**<font color=#1a73e8>作者：</font>** Hardik Iyer, Tirath Bhathawala, Mihir Panchal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fracture detection and its clinical interpretability see notable improvements when deep vision models are integrated with agentic AI architectures. While deep learning models achieve high diagnostic performance, their black-box nature limits clinical adoption. We propose FRAC-MAS, an agentic AI system for automated, explainable, and safe bone fracture detection. The framework combines a stacked ensemble of four vision models with conformal prediction to produce statistically grounded differential diagnoses, while a multi-agent workflow performs independent verification, retrieves clinical guidelines, and generates patient-friendly reports. A pipeline-depth ablation study confirms that our multi-agent critic triages 86.6% of cases into a high-confidence auto-confirmed cohort while escalating uncertain cases, outperforming a single-agent baseline. Patient preference studies against Llama, MedGemma, and Gemini further demonstrate significantly more comprehensible clinical reports. These results suggest that integrating multi-agent critics with conformal guarantees enables safer radiology triage while preserving clinician oversight. More broadly, FRAC-MAS demonstrates how cooperative agentic architectures can serve as auditable, human-in-the-loop decision support systems for safety-critical healthcare. Our code is available at this https URL, and the website is available at this https URL.

---


### 33. [Improving Spatial-Temporal Reasoning in Video-Language Models with Structured Video Prompting](https://arxiv.org/abs/2608.28666)

**<font color=#1a73e8>作者：</font>** Sadegh Mohammadian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-language models (VLMs) remain brittle on tasks that require tracking events over time and grounding answers in specific spatial regions. We propose that part of this limitation can be addressed through better organization of visual evidence at inference time. We introduce structured video prompting, a training-free inference-time method that augments the input video with lightweight spatial structure and temporal structure, providing explicit anchors for organizing evidence across space and time without changing model weights or decoding and without altering the question prompt in the main comparison. We evaluate this approach on two complementary video benchmarks and two open video-language models. Across these settings, structured inputs improve performance in several cases, with gains varying by model and task. Our findings suggest that some failures of VLMs arise not only from reasoning capacity, but also from how video evidence is presented at inference time. These results highlight structured video prompting as a simple and practical direction for improving video understanding.

---


### 34. [GreenBench: Benchmarking Energy Efficiency and Carbon Footprint of Open-Source LLM Inference on Apple Silicon](https://arxiv.org/abs/2608.28667)

**<font color=#1a73e8>作者：</font>** Rajeswari Kannan, Raj Firke, Shreya Bengle 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of Large Language Models (LLMs) has raised concerns about their environmental impact during inference. While Green AI research has focused on datacenter GPUs and embedded platforms, the energy profile of LLM inference on Apple Silicon, with its unified memory architecture, remains unstudied. This paper presents GreenBench, a benchmarking framework that evaluates the energy efficiency, throughput, and carbon footprint of five open-source LLMs (3-9B parameters) across three NLP tasks on an Apple M4 Pro with 48 GB unified memory. Using macOS powermetrics for direct power measurement and Ollama's nanosecond-precision timing, we find that the M4 Pro draws only 0.47 W of CPU+GPU package power during sustained inference, with total system power of 8-12 W, achieving 30-40x better energy efficiency per token than datacenter GPUs in single-user deployment. Smaller models (3-3.8B) deliver 2.6-4.2x higher throughput and up to 62% less energy per token than larger models (7-9B). Pareto analysis identifies Qwen 2.5 (7B) as the optimal accuracy-efficiency trade-off at 57% MMLU and 59 tokens/s, while Llama 3.2 (3B) suits latency-critical applications at 175 tokens/s. We provide per-token energy at package and system levels with CO2 estimates for India and US grids.

---


### 35. [Automated pipeline for herbarium label digitization](https://arxiv.org/abs/2608.28676)

**<font color=#1a73e8>作者：</font>** Hiba Abbad, Hanane Ariouat, Eva Perez Pimpare 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digitized herbarium collections, now comprising over 100 million freely accessible specimen images, have become a critical resource for addressing fundamental questions in ecology and evolutionary biology. Yet the rich metadata encoded in herbarium labels (collector identities, geographic localities, collection dates, and ecological observations) remains largely inaccessible at scale, constraining both biodiversity informatics and the construction of specimen-specific image-text corpora for multimodal AI. We present HERBIOME, a modular end-to-end pipeline for automated herbarium label digitization, integrating YOLOv8-based component detection, CRAFT Hezar word-level text localization, fine-tuned TrOCR for recognition of mixed handwritten and printed text, and GPT-4o Mini for semantic metadata structuring into standardized fields. TrOCR was trained on a multi-source dataset combining general transcription corpora (CREMMA-AN, PictoCatalogs) with herbarium-specific data (RéColNat), achieving a Character Error Rate of 4.05-4.10%. End-to-end evaluation on 450 French herbarium specimens, using a dual-metric framework of Maximum Window Similarity (MWS: 0.614-0.618) and Semantic Metadata Accuracy (SMA: 0.440-0.445), reveals that hybrid training strategies improve semantic fidelity while random sampling maximizes surface similarity, with taxonomic fields remaining the principal bottleneck. By automating the extraction of structured metadata from complex, heterogeneous labels, HERBIOME reduces transcription burden, enables the construction of paired image-text datasets that faithfully capture specimen individuality, which is a prerequisite for next-generation multimodal biodiversity AI systems.

---


### 36. [Evaluating Constrained Iterative Refinement for Scalable Vector Graphics Generation with Off-the-Shelf VLMs](https://arxiv.org/abs/2608.28678)

**<font color=#1a73e8>作者：</font>** Matthew Perlman, James Beetham, Niels Da Vitoria Lobo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scalable Vector Graphics (SVGs) power much of the modern visual ecosystem, yet state-of-the-art generative models focus almost entirely on rasterized images. We explore whether inference-time methods can unlock SVG generation capabilities in off-the-shelf vision-language models (VLMs). We systematically evaluate a constrained iterative refinement harness that combines visual feedback, structured editing, and constrained decoding to characterize the capabilities and limitations of current VLMs for SVG generation. Across multiple VLMs and generation settings, we find that constrained decoding improves compilation success rates, while iterative refinement reveals a deficit in visual reasoning and self-correction. Our results highlight both the promise and current limitations of using inference-time methods to adapt general-purpose VLMs for SVG generation.

---


### 37. [FLM: Frequency-Aware Language Models for Generative Image Compression](https://arxiv.org/abs/2608.28687)

**<font color=#1a73e8>作者：</font>** Jiarun Chen, Kejun Wu, Li Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models have significantly improved the performance ceiling of image lossy compression at low bitrates by exploiting learned priors. However, the generated textures and semantic details may deviate from the source content, thereby affecting the fidelity of image reconstruction. To solve these challenges, we propose FLM, a frequency-aware language model that improves compression efficiency through frequency-domain probabilistic modeling while retaining deterministic reconstruction. At the encoder, the input image is transformed into quantized DCT coefficients, which are organized into discrete sequences using macroblock-based coefficient tokenization. FLM then performs next-coefficient prediction to autoregressively estimate token-wise conditional probability distributions for arithmetic coding, thereby generating a compact bitstream. At the decoder, the LLM and arithmetic decoder jointly recover the frequency-domain data, followed by inverse transformations for image reconstruction. A task-specific frequency-domain dataset and a two-stage fine-tuning strategy are further developed to enable the model to operate across multiple bitrate settings. FLM is a versatile compressor that is compatible with both lossy compression and lossless JPEG recompression frameworks. Experiments show that FLM exceeds conventional and generative lossy compression methods in rate-distortion performance. FLM achieves BD-PSNR gains of 3.30 dB, 3.83 dB, and 3.80 dB than JPEG baseline on Kodak, Tecnick, and CLIC2020, respectively. Better qualitative quality of FLM can be achieved in improving semantically high fidelity and suppressing blocking artifacts. FLM is also validated to be applicable to the lossless recompression task with competitive performance.

---


### 38. [Defending Wearable VLMs Against Private Attribute Inference](https://arxiv.org/abs/2608.28691)

**<font color=#1a73e8>作者：</font>** Zhimin Li, Pan Wang, Jingxian Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wearable VLM pipelines promise continuous multimodal assistance from egocentric visual capture: a user asks a task-driven question about the surrounding scene, and the system uses compact visual tokens to support language reasoning. The challenge motivating this work is that the same egocentric evidence needed for useful assistance can also reveal private attributes about the wearer or nearby bystanders. We investigate this as a joint privacy-utility problem for split VLM inference, where visual encoding occurs within a trusted device boundary but intermediate visual tokens may be transmitted to downstream reasoning components. This exposes an understudied leakage surface: even when final textual responses are benign, external attackers or untrusted downstream components can recover private attributes from transmitted visual tokens. To evaluate this tension, we construct a paired privacy-utility benchmark with 3,221 image-question records, each paired with a utility question and privacy labels covering location, income, sex, and interests. We further propose Token-Guided Attribute Privacy (TGAP), a pre-LLM token disentangler that learns a residual transformation of visual tokens before they leave the trusted boundary. TGAP combines utility preservation, identity regularization, semantic privacy suppression, and image-driven representation suppression, avoiding the utility loss caused by coarse hard or attention masking. On the benchmark used for source-model evaluation, TGAP reduces privacy accuracy from 56.7\% to 7.4\%, a 49.3\% absolute drop, while maintaining relaxed utility at 74.4\%. These results suggest that securing the compact token interface is a practical path toward privacy-preserving wearable multimodal AI.

---


### 39. [Weaving Visual Narratives: Agentic Image Bundle Composition Beyond Atomic Visual Matching](https://arxiv.org/abs/2608.28695)

**<font color=#1a73e8>作者：</font>** Rong Shan, Tianyi Xu, Congmin Zheng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image retrieval has traditionally been formulated as a point-wise matching problem, where each candidate image is scored in isolation. However, this atomic paradigm fails to capture the complexity of human search intent within personal photo collections, where users often seek compact visual stories bound by structural relations rather than isolated snapshots. To address this limitation, we introduce **Image Bundle Composition (IBC)**, a novel paradigm that shifts the objective from ranking individual images to dynamically composing cohesive image bundles from a massive, unstructured photo pool. Since target bundles are not predefined, IBC presents a severe combinatorial explosion challenge and demands modeling non-decomposable joint relevance. To establish this paradigm, we construct **IBCBench**, the first IBC benchmark dataset containing 109,467 images and 667 verified queries, built via a semi-automated verification pipeline. Furthermore, we propose **BundleWeaver**, an agentic framework that reformulates IBC as query-conditioned incremental hyperedge discovery. By employing a Large Language Model to adaptively search for missing relational roles and utilizing a Vision-Language Model for whole-bundle verification, BundleWeaver effectively navigates the combinatorial space. Extensive experiments demonstrate that while state-of-the-art embedding models and static decompose-and-rerank paradigms suffer from relational blindness, BundleWeaver achieves substantial performance gains, highlighting the necessity of shifting from atomic scoring to dynamic relational composition. Our dataset and code are available.

---


### 40. [Instruction Distillation: Text Instructions as Visual Examples](https://arxiv.org/abs/2608.28696)

**<font color=#1a73e8>作者：</font>** Hardik Jindal, Soumyabrata Pal, Sayak Ray Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual in-context learning (ICL) with multimodal large language models (MLLMs) is effective for fine-grained visual classification, but each retrieved image example consumes several hundred context tokens, making large-$K$ settings prohibitively expensive at inference scale. We propose Instruction Distillation: an offline procedure in which the MLLM itself generates, for each individual training image, a structured identification instruction encoding general appearance cues, features that differentiate the class from visually similar ones, and a common confusion point. Unlike prior work that produces a single description per class, our instructions are generated per training image, preserving the intra-class visual diversity that per-class descriptions collapse. At inference time, we study five configurations sharing a single CLIP retrieval index: zero-shot, image ICL, instruction-only ICL, and two hybrid variants in which retrieved neighbors are split between images and instructions. Across seven fine-grained benchmarks and two MLLM backbones, instruction based pipelines match, or exceeds image ICL at $K{=}1$ and reduces per-query tokens by $2.9\times$ and inference latency by $3.3\times$ at $K{=}5$. Hybrid configurations further show that visual and textual ICL signals are complementary, images give visual patterns to learn and see, while instructions give explicit rules and logic. When both of these are provided, the quality of context improves, which is noticeable in the performance.

---


### 41. [State-Conditioned Visual Evidence Retrieval for Fine-Grained Perception in Document Vision-Language Models](https://arxiv.org/abs/2608.28698)

**<font color=#1a73e8>作者：</font>** Mingxu Chai, Chenyu Liu, Ziyu Shen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compared with typical vision-language tasks, document parsing places stronger demands on fine-grained visual perception. Existing vision-language model (VLM)-based parsing approaches rely on globally compressed visual tokens, where fine-grained details are entangled within a single representation and repeatedly accessed during decoding. However, we observe that the visual evidence for each prediction is typically localized and conditioned on the current decoding state, whereas such representations must be accessed in full at every decoding step, resulting in inefficient computation. To address this mismatch, we formulate perception as state-conditioned visual evidence retrieval (SCVER) during autoregressive decoding. The model operates on a compact global representation for coarse structure and retrieves a small set of relevant high-resolution regions conditioned on the current token state. This coarse-to-fine design enables on-demand access to fine-grained visual cues, relieving globally shared representations from encoding all fine-grained details. We further find that learning such state-conditioned retrieval in VLMs is challenging and unstable. To stabilize this process, we introduce a Spatially-Guided Learning Objective (SGLO) to guide the retrieval process. Experiments on document parsing benchmarks show that SCVER improves robustness under reduced input resolution and achieves a better accuracy-efficiency trade-off, demonstrating the effectiveness of on-demand visual evidence retrieval for fine-grained perception.

---


### 42. [Beyond Visual Boundaries: Rethinking Scene Segmentation for Movie RAG](https://arxiv.org/abs/2608.28699)

**<font color=#1a73e8>作者：</font>** Dong-Hee Kim, Seonwoo Choi, Changbeen Kim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding long-form video remains a fundamental challenge for multimodal large language models (MLLMs). Sparse frame sampling fails to capture fine-grained visual details, while dense sampling quickly exceeds context length limits. Retrieval-augmented generation (RAG) offers a promising middle ground by selectively retrieving relevant video segments for grounded generation, yet its effectiveness critically depends on the quality of the video segments used as retrieval units. In this paper, we investigate RAG for movie understanding, which demands story-level reasoning over characters, events, and narrative arcs spanning hours of content. Scene segmentation, a long-studied problem that partitions movies into semantically coherent units, is a natural candidate for defining such retrieval units. We reexamine whether existing methods actually serve this role through comprehensive evaluation on downstream movie understanding tasks, and find that they consistently fail to outperform naive uniform temporal chunking. Our audit of the most standard scene segmentation benchmarks reveals why: current annotations prioritize visually salient transitions over narrative event structure. Motivated by this mismatch, we introduce NarraScene, a narrative-centric scene segmentation dataset annotated with a three-level cognitive taxonomy spanning physical, character, and narrative change, where every valid boundary requires a narrative-level shift. When used as retrieval units, these narrative-grounded segments outperform uniform chunking on downstream movie understanding tasks, suggesting that the central challenge for scene segmentation in movie RAG is not detecting boundaries, but identifying the narrative event units that matter for movie understanding.

---


### 43. [TopoAgent: A Structure-Aware Perception-to-Reasoning Framework for Diagram-to-Graph Topology Extraction with Large Vision-Language Models](https://arxiv.org/abs/2608.28701)

**<font color=#1a73e8>作者：</font>** Bangwei Guo, Xujiang Zhao, Yanchi Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diagram-to-graph topology extraction aims to extract a graph of entities and their connections from a structural diagram. This task remains challenging for current vision-language models because it requires both fine-grained perceptual grounding and topology-aware reasoning with global consistency. We present TopoBench-180, a human-verified benchmark for diagram-to-graph topology extraction, and TopoAgent, a structure-aware perception-to-reasoning framework for reliable topology extraction using large vision-language models. TopoBench-180 contains 180 structural diagrams spanning Web-style and Network-style categories, paired with canonical graph annotations. TopoAgent progressively extracts the target graph by combining grounded perception, global structural priors, canonical node inventory construction, node-centric local-to-global relation reasoning, and topological consistency enforcement. Experiments on TopoBench-180 show that TopoAgent outperforms strong vision-language model baselines and recent visual reasoning frameworks, especially on edge extraction. More broadly, this work fills an important gap in multimodal structured understanding by establishing a benchmark and framework for diagram-to-graph topology extraction. The benchmark and associated resources will be publicly released at this https URL.

---


### 44. [ReVA: A Region-Aware Visual Assistant for Visually Grounded Question Answering](https://arxiv.org/abs/2608.28707)

**<font color=#1a73e8>作者：</font>** Anoop Senthil  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable progress in Visual Question Answering (VQA), yet they continue to struggle with questions requiring precise spatial reasoning and fine-grained visual understanding. These limitations often manifest as object, attribute, and spatial hallucinations, where models generate confident but visually unsupported responses due to insufficient region-level and fine-grained visual grounding. To address this challenge, we propose ReVA, a region-aware VQA model that employs a frozen CLIP ViT-L/14 Vision Transformer (ViT) and a Qwen2.5-7B-Instruct large language model (LLM) connected through a dual bridge that aligns both whole-image and region-level representations with the LLM's embedding space. The image bridge maps final transformer block features into image tokens. The region bridge maps cropped features from enriched intermediate features across ViT blocks so early texture and later object cues are more evident, into K region tokens for every bounding box. ReVA uses a detector stack that supplies automatic zero-shot bounding boxes that are both question-agnostic and question-dependent, using RAM++ (Recognize Anything Model), spaCy, and Grounding DINO. The image tokens and region tokens are concatenated as an LLM prompt prefix to jointly encode scene-level context and fine-grained regional evidence when answering questions. Evaluated on VQAv2, MMBench, POPE, and SEED-Bench, ReVA achieves 82.85% mean F1 on POPE, compared with 81.14% for an image-token baseline without region tokens. These results demonstrate that explicit region-aware visual representations reduce object hallucination and improve the factual grounding of MLLMs.

---


### 45. [Beyond the Answer Key: Robustness Evaluation of Large Language Models for Step-Level Mathematical Verification](https://arxiv.org/abs/2608.28725)

**<font color=#1a73e8>作者：</font>** Fateme Mazdarani, Carlos Toxtli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as graders, verifiers, and process auditors, but most mathematical evaluations still emphasize final-answer accuracy. This can obscure whether a model can verify a non-canonical but valid solution trace. We introduce a controlled linear-equation benchmark for evaluating LLMs in the evaluator role. Each instance asks the model to judge final-answer correctness, step-level trace correctness, and the first incorrect step. Our evaluation of state-of-the-art open LLMs reveals a significant robustness gap: models that accurately evaluate canonical solutions often fail when presented with perturbed but logically equivalent variants. Across GPT-OSS 20B, Qwen3-14B, and Phi-4-Reasoning, base models perform well on canonical traces but degrade substantially on perturbed traces, especially for error localization. On valid perturbed traces, base-model false-rejection rates reach 75.6-85.3%, showing strong sensitivity to canonical solution form. Supervised fine-tuning, distillation, and test-time compute improve robustness in some settings, but gains are model dependent and can trade off against canonical performance. The results show that reliable process-level verification remains challenging, and evaluator robustness should be measured separately from solver accuracy, even in a simple algebraic domain with exact ground truth.

---


### 46. [Pro-Router: Token-Aware Progressive Model Routing with Adaptive Edge-Cloud Collaboration for Efficient Multimodal LLM Inference](https://arxiv.org/abs/2608.28726)

**<font color=#1a73e8>作者：</font>** Xinyuan Gui, Shaowen Wang, Sheng Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The remarkable performance of multimodal large language models (MLLMs) comes at the cost of substantial computational overhead, posing significant challenges to real-time deployment and cost effectiveness. Existing model routing approaches either decide from coarse request-level features alone or spend one or several extra language model passes to inspect the generated response, leaving the token-level uncertainty signals that emerge during generation unused. To address these limitations, we propose Pro-Router, a token-aware progressive model routing method with adaptive edge-cloud collaboration for efficient multimodal LLM inference. Pro-Router employs a two-stage progressive decision mechanism. First, a lightweight prompt pre-scorer module performs rapid pre-screening before token generation begins, guiding apparently simple requests to small models. Second, a token-aware verifier reads the sampling probability distribution of each token the small model generates, estimating the model's confidence in its own output to determine, per request, whether the answer ships or escalates to the cloud-based high-precision model. Furthermore, we design an adaptive edge-cloud serving pipeline that sizes every dispatch to each device's measured service rate, so both the edge and the cloud tiers stay fully utilized without manual parameter tuning and are not impacted by the network latency. Extensive experiments on multiple multimodal benchmark datasets and models demonstrate the effectiveness of Pro-Router. Compared to other methods, it achieves the highest routing accuracy and improves routing speed by more than 10x. Its serving pipeline also reaches more than 75% higher end-to-end throughput than the existing model routing pipeline. Our code is available at this https URL.

---


### 47. [PermitGPT: A Unified Generative-AI Pipeline for Construction Hazard Forecasting, Permit Prediction, and Community Impact](https://arxiv.org/abs/2608.28728)

**<font color=#1a73e8>作者：</font>** Mohd Ruhul Ameen, Farjana Aktar, Akif Islam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban construction governance requires early decisions that connect workplace safety, permitting requirements, and community impact, yet the relevant evidence is often scattered across separate municipal and regulatory data sources. This paper presents PermitGPT, a unified generative artificial intelligence framework for converting unstructured construction permit descriptions into structured decision-support outputs across three domains: safety hazard identification, permit requirement specification, and community impact assessment. To address data fragmentation, we spatially and temporally align records from the New York City Department of Buildings, Occupational Safety and Health Administration, and NYC 311 service requests, producing 90,000 structured prompt-response pairs derived through rule-based alignment and domain-informed spot checking. We fine-tune three open-weight language models using parameter-efficient adaptation and evaluate them on 2,833 held-out test cases. The results show complementary model behavior: Gemma-3-1B provides the most efficient inference at 3.07 samples per second with low memory usage, Llama-3.2-3B gives the highest lexical overlap for regulatory-style outputs with a BLEU score of 0.0091, and 4-bit Mistral-7B-Instruct-v0.3 achieves the strongest semantic alignment with a BERTScore-F1 of 0.7747. Because the task involves open-ended structured generation, low BLEU values are interpreted alongside semantic metrics and qualitative output structure rather than as standalone indicators of utility. Overall, PermitGPT provides an initial step toward AI-assisted construction governance while identifying directions for stronger task-level evaluation and real-world validation.

---


### 48. [Inter-3D VQA: A Roadside Multimodal Benchmark for 3D Spatiotemporally Grounded Visual Question Answering](https://arxiv.org/abs/2608.28762)

**<font color=#1a73e8>作者：</font>** Shaozu Ding, Linan Song, Dajiang Suo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in visual question answering (VQA) and multimodal large language models (MLLMs) have enabled natural-language reasoning over traffic scenes. However, existing benchmarks are largely built from ego-vehicle views or 2D roadside videos, limiting their ability to evaluate 3D-grounded reasoning over real-world distances, trajectories, infrastructure topology, and safety-critical interactions. We introduce Inter-3D VQA, a large-scale roadside multimodal benchmark for 3D spatiotemporally grounded VQA at intersections. Built from synchronized point clouds and multi-view images, Inter-3D VQA contains 407K QA pairs covering lane-level positions, object relationships, motion patterns, and near-miss-oriented interaction reasoning. We further propose Inter-Geo, an MLLM baseline that integrates object- and scene-level aligned LiDAR representations, and Inter-Metrics, a unified evaluation framework for textual consistency, numerical accuracy, and semantic correctness. Experiments show that Inter-Geo outperforms image-based VLMs, especially on grounded spatial and temporal reasoning tasks. Our benchmark and codes are available at this https URL .

---


### 49. [ERR+: Sequential Entropy Resolution for Efficient and Decisive LLM Reasoning](https://arxiv.org/abs/2608.28771)

**<font color=#1a73e8>作者：</font>** Xin Jiang, Minhao Wang, Wen Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large reasoning models achieve strong performance on complex tasks by generating extended chain-of-thought (CoT) traces via reinforcement learning with verifiable rewards (RLVR). While current RLVR methods have achieved strong results with correctness-based reward signals, they provide limited guidance on the quality of the reasoning process itself, leaving the internal reasoning structure largely unoptimized. Through empirical analysis across multiple model families, we identify a consistent pattern: correct reasoning trac es exhibit more frequent and larger token-level entropy drops within the thinking phase than incorrect ones. We propose ERR+, a two-phase RLVR framework grounded in this observation. The first phase trains with the Entropy Relief Reward (ERR), a bonus proportional to cumulative token-level entropy drops in the thinking phase, log-normalized by response length. Unlike prior methods that suppress entropy, ERR rewards the resolution of uncertainty while leaving exploratory high-entropy states unconstrained. The second phase introduces the Robust Relative Efficiency Reward, which scores each response's length against co-generated peers via a $\tanh$-transformed within-group $z$-score. We provide a formal analysis showing that joint optimization of the two objectives induces gradient conflict in early training, motivating the sequential design . Experiments on five datasets demonstrate consistent improvements in both accuracy and response conciseness across model backbones. Our code is available at this https URL

---


### 50. [ClearText-Video: A Large-Scale Text-Centric Video Dataset Bridging Video Restoration and Scene-Text Enhancement](https://arxiv.org/abs/2608.28784)

**<font color=#1a73e8>作者：</font>** Jinlong Li, Jiaming Ding, Dingfu Lu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have recently made strong progress in visual--linguistic understanding. However, their performance on text-centric video reasoning remains highly sensitive to input quality. Real-world user-provided videos often contain motion blur, compression artifacts, noise, and low-resolution text, which impair reliable text reading and downstream reasoning. Whether MLLMs can robustly read and reason about real-world scene text under diverse quality conditions remains a fundamental open question. We introduce ClearText-Video (CTVid), a large-scale, scene-text-aware benchmark for studying text-centric video understanding under controlled quality variation. CTVid contains 4,639 real-world text-rich egocentric videos, 550K+ frames, 1.6M human-verified scene-text annotations, and 220K+ spatial/temporal question--answer pairs in Chinese and English. For each high-quality video, CTVid provides content-matched Degraded-Quality and Restored-Quality variants, supporting two task families: Text-Centric Video Restoration and Multi-Quality VideoQA. We evaluate 18 representative restoration methods and 16 state-of-the-art MLLMs on CTVid. The results show that visual enhancement does not guarantee textual fidelity or downstream reasoning gains: blur is more damaging than low resolution, restored videos can alter the textual evidence used by MLLMs, and OCR-only pipelines remain far below direct multimodal reasoning. CTVid exposes the gap between video restoration and text-grounded understanding, providing a rigorous foundation for restoration-aware, quality-robust text-centric video systems.

---


> [!TIP]
> 当前位于：**1-50**（第 1/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
