# 🧠 大模型相关研究 | 2026年11月11日

> 本类共 **438** 篇论文：已确认 **405** 篇，待复核 **33** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 1. [Process then Retrieve: Investigating the Origins of the Modality Gap in Vision-Language Models](https://arxiv.org/abs/2611.09897)

**<font color=#1a73e8>作者：</font>** Arpita Shanbhag, Julia Tran, Dhruv Mandala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the origins of the modality gap in vision language models remains a significant challenge. This work investigates whether differences in information density between modality specific tokens at the embedding layer contribute to this imbalance. We show that text tokens enter the model with much lower semantic density than visual tokens, driving early layers to focus on processing text representations before combining them with vision. Through mechanistic analysis, we demonstrate that replacing vision token positions with their semantically closest text token counterparts elicits increased attention to those positions in early layers. These findings provide a foundation for addressing the modality gap and provide insight to improve multimodal reasoning in VLM architectures.

---


### 2. [Generative AI and Oral Proficiency: How ChatGPT Is Transforming English Language Speaking Practice](https://arxiv.org/abs/2611.09898)

**<font color=#1a73e8>作者：</font>** Mohammad Mousazadeh  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The integration of generative artificial intelligence (GenAI) into language learning contexts presents potential for developing oral proficiency, though empirical evidence regarding its efficacy remains limited. This quasi-experimental study investigated the impact of ChatGPT-mediated speaking practice on English oral proficiency among Iranian learners. A total of 380 participants (190 female, 190 male; M(age) = 21.4, SD = 4.7) from Tehran and Isfahan were assigned to experimental (ChatGPT practice; n = 190) or control (human pair work; n = 190) groups. Both groups completed an 8-week intervention with three 30-minute weekly sessions. Oral proficiency was assessed using a Common European Framework of Reference for Languages (CEFR)-aligned Oral Proficiency Interview (OPI) scored on fluency, pronunciation, lexical resource, grammatical accuracy, and interactive communication (total score: 0-20). Multilevel growth modeling revealed a significant time-by-group interaction, F(1, 376) = 48.73, p < .001, partial eta-squared = .115. The experimental group demonstrated greater gains (M change = 2.90, SD = 1.60) than controls (M change = 0.75, SD = 1.80), d = 1.20, 95% CI [0.95, 1.45]. Gender moderated this effect, with females in the experimental group showing the largest improvements (M change = 2.50). Mediation analysis confirmed that increased integrative motivation partially mediated proficiency gains (indirect effect = 0.28, 95% CI [0.20, 0.36]). Findings indicate that structured ChatGPT practice yields modest but meaningful enhancements in oral proficiency, particularly when leveraging affective factors. Implications for AI-augmented speaking pedagogy in resource-constrained contexts are discussed.

---


### 3. [KR A1: Design and Preliminary Evaluation of a Humanoid-Robot Interaction Prototype Integrating Personalized Voice Synthesis, Contextual Dialogue, and Emotion-Aware Response Generation](https://arxiv.org/abs/2611.09900)

**<font color=#1a73e8>作者：</font>** Mahek Aanthu, Om Aanthu, Aaryan AK Aanthu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents the design and preliminary evaluation of KR A1, a humanoid-robot interaction prototype that integrates personalized voice synthesis, contextual dialogue processing, and emotion-aware response generation for potential mental-healthcare applications. The system architecture combines a locally hosted large language model (Qwen2.5-3B-Instruct, served via Ollama) for natural-language understanding and response generation, OpenVoice v2 for zero-shot speaker-adaptive speech synthesis, and a two-tier emotion-processing pipeline comprising a keyword heuristic and LLM-based inference. Face recognition (InsightFace) and vector memory retrieval (FAISS with sentence-transformer embeddings) enable user-personalized interaction. The experimental evaluation reported here is limited to the voice-cloning component: cloned voices were evaluated against reference recordings using eight acoustic similarity measures - mel-frequency cepstral coefficients, pitch, spectral centroid, spectral contrast, spectral rolloff, zero-crossing rate, formants, and speaker-embedding cosine similarity - supplemented by a same-speaker versus cross-speaker baseline comparison. All tests were conducted on a small, informal development sample; no statistical significance testing against a held-out baseline was performed. The emotion-recognition accuracy, end-to-end response latency, and therapeutic or clinical impact of the integrated system have not yet been formally evaluated and are identified as directions for future work. All testing was informal and self-conducted by the development team; no patients or external human participants were involved, and the system has not been evaluated or deployed in a clinical setting.

---


### 4. [Beyond One User and One Model: Rethinking LLMs as Mediators in Collaborative Sensemaking and Ideation](https://arxiv.org/abs/2611.09903)

**<font color=#1a73e8>作者：</font>** Pengqi Wang, Emily Kuang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As LLMs enter qualitative data workflows, they are predominantly designed for individual researchers rather than collaborative teams, which risks disrupting the collective negotiation essential to sensemaking, driving premature consensus, and potentially erasing marginalized voices. In this position paper, we argue that LLMs must be reconceived as active team mediators. Grounded in empirical studies of human-LLM collaborative analysis, we propose three design directions: quote-level traceability to preserve accountability of human and LLM contributions, controllable delegation boundaries to maintain researcher agency across workflow stages, and structured dissent mechanisms to surface interpretive conflicts that teams might otherwise suppress. We ground these directions in accessibility research as a domain where methodological rigor and representational equity are obligatory.

---


### 5. [Building Rapport with Self-Disclosure in Human-Robot Interaction](https://arxiv.org/abs/2611.09905)

**<font color=#1a73e8>作者：</font>** Haritha Anupindi, Chayan Sarkar, Tapas Nayak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As social robots become increasingly present in everyday environments, establishing rapport with users is critical for enabling sustained and meaningful human-robot interaction. In human-human communication, self-disclosure is a well-established mechanism for building rapport; however, its role and impact in human-robot interaction (HRI) are not yet well understood. Although recent advances in large language models (LLMs) have improved the linguistic competence of conversational robots, such systems are typically deployed as reactive information providers, offering limited social reciprocity and relational depth. In this article, we investigate the role of robot self-disclosure in fostering rapport during face-to-face human-robot interaction. We propose a dialogue system, called RADIA that leverages retrieval-augmented generation (RAG) to enable a robot to retrieve and reference simulated autobiographical memories, allowing first-person self-disclosure to be incorporated naturally into ongoing conversations. We evaluate the proposed approach through an in-person user study, comparing interactions with a self-disclosing robot against a baseline non-self-disclosing robot. Our results show that robot self-disclosure significantly influences conversational dynamics and enhances users' perceived rapport with the robot, suggesting that self-disclosure is a valuable social behavior for long-term and socially engaging human-robot interaction.

---


### 6. [How to start a conversation proactively?](https://arxiv.org/abs/2611.09906)

**<font color=#1a73e8>作者：</font>** Mohit Nathani, Aaditya Gupta, Eshwar Dhande 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Proactively initiating a conversation is a fundamental social competence and a critical capability for social robots. However, determining how and when to start a conversation in a given situation remains an open challenge, primarily due to the lack of a principled definition of conversational context. While recent large language models (LLMs) demonstrate impressive conversational fluency, they are predominantly turn-reactive and often produce generic or monotonous openers when tasked with initiating interaction, even when contextual information is available. Such limitations are particularly problematic for embodied social robots, where inappropriate or poorly timed initiations can negatively affect user engagement and rapport. In this work, we propose a schema of contextual variables that jointly characterize situations relevant for proactive conversation initiation. The schema is designed to structure perceptual, situational, and interactional cues such that they can be effectively exploited by language models. Furthermore, motivated by the absence of suitable training data, we introduce a curated dataset of contextually-aligned conversation openers (CCO) covering diverse everyday scenarios. Using this dataset, we fine-tune small language models (SLMs) to generate proactive conversation initiations. Through a comparative evaluation involving zero-shot LLMs, off-the-shelf SLMs, and our fine-tuned models, we demonstrate that explicit contextual structuring and targeted data curation substantially improve the quality and contextual appropriateness of conversation openers. Our results highlight the importance of context modeling for proactive social interaction and provide actionable building blocks for conversational robots.

---


### 7. [Cross-Modal Associations in Creativity: Evaluating Word-Image Pairing in Humans and Large Language Models](https://arxiv.org/abs/2611.09907)

**<font color=#1a73e8>作者：</font>** Eva Illion, Linxuan Wang, Liane Gabora  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Given differences in the associative memory architectures of humans and AI, it is not clear whether AI generates and interprets visual-linguistic associations the way humans do. To investigate this, human participants and two large language models (LLMs), ChatGPT and Gemini, were asked to generate novel words and corresponding images that form meaningfully linked dyads. The LLMs and a second group of human participants were presented with shuffled sets of these words and images and asked to rematch them in ways they felt were most meaningful. Humans performed similarly regardless of whether the pairs were human or LLM-generated, while LLMs were better at matching LLM-generated pairs. Overall, LLMs outperformed humans at recovering the intended pairings. These findings suggest that despite architectural differences, the way in which AI generates and detects associations between language and visual stimuli is not only like that of hu-mans, but they may be superior at recognizing cross-domain associations that humans find meaningful.

---


### 8. [Human-Likeness is Multi-Dimensional: Evaluating LLM Generated Virtual Patients Against Simulated Patient Dialogue](https://arxiv.org/abs/2611.09908)

**<font color=#1a73e8>作者：</font>** Reyhaneh Hosseinpourkhoshkbari, Wei-Chen Huang, Yile Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate virtual patients (VPs) for medical training. As these systems move toward broader deployment in medical education, reliable evaluation is needed to identify potential failure modes and ensure that generated patient responses remain consistent with human simulated patient (SP) behavior. Inaccurate, unrealistic, or inconsistent responses may introduce educational risks by exposing learners to misleading patient interactions. However, current evaluation approaches rely heavily on human judgment, making large-scale evaluation difficult. In this work, we present a controlled generation pipeline for systematically comparing VP responses generated by 10 LLMs across multiple decoding temperatures with human respiratory SP responses. To support scalable evaluation, we introduce a multi-dimensional framework for measuring similarity between LLM-generated and human SP dialogue across semantic, conversational grounding, linguistic, and emotional dimensions. Across semantic, conversational, linguistic, and emotional dimensions, no single model consistently produced the most human-like responses. From a practical perspective, Gemini 2.5 Flash demonstrated the most consistently human-like performance across semantic, linguistic, grammatical, and emotional dimensions, while Claude Sonnet 4.6 achieved the strongest semantic fidelity. These findings highlight the importance of multi-dimensional evaluation and demonstrate how automated metrics can provide a scalable approach for assessing virtual patient systems before broader deployment in medical education.

---


### 9. [Can You Spot the Virtual Patient (VP)? Expert Evaluation, Turing Test, Linguistic Analysis, and Semantic Similarity Analysis](https://arxiv.org/abs/2611.09909)

**<font color=#1a73e8>作者：</font>** Reyhaneh Hosseinpourkhoshkbari, Wei-chen Huang, Suvel Muttreja 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Communication is a core clinical competency and essential for safe, effective patient care. Virtual patients (VPs) powered by large language models (LLMs) offer a promising alternative to traditional formats such as standardized patients (SPs). However, few studies have quantitatively as well as qualitatively evaluated their realism across diverse clinical scenarios using behavioral studies and linguistic dialog analyses. This study evaluated the realism of GPT-4o-generated VPs through expert review, Turing testing, linguistic analysis, and semantic analysis. We generated 44 VPs using structured illness scripts derived from doctor-simulated patient dialogues across 17 clinical categories. Experts annotated responses for hallucinations, omissions, and repetitions, with high interrater reliability (ICC > 0.77). A Turing test revealed that participants struggled to distinguish VP responses from those of real patients, with average classification accuracy for VP responses falling below chance level. Lexical and syntactic analyses of over 2,000 conversation turns showed that VP responses were generally realistic, more formal and lexically consistent, while human responses displayed greater emotional variation. Semantic similarity using BioClinicalBERT and cosine similarity averaged 0.871 at the response level and 0.842 at the transcript level. Our findings support the integration of LLM-based VPs in communication training while highlighting areas for trust, transparency, and refinement, contributing to both GenAI deployment in healthcare and its safety evaluation.

---


### 10. [Micro-Randomized Trial of an AI-Simulated Practice Tool for Therapeutic Skills](https://arxiv.org/abs/2611.09912)

**<font color=#1a73e8>作者：</font>** Ryan Louie, Ellen Converse, Diyi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Though LLM-simulated practice may support psychotherapy education, open questions remain about which system features provide the most educational value. We developed an AI-simulated practice tool for use in psychotherapy classrooms that provides speaking practice with LLM-based patients, followed by a post-practice activity that includes feedback from a fine-tuned LLM and written reflection exercises. We deployed the tool in a graduate psychotherapy course (n=25, 5 weeks) using a micro-randomized trial (MRT) - a method which can estimate the causal excursion effect of an intervention by leveraging longitudinal repeated randomization with participants. Testing four conditions crossing AI feedback (present/absent) with reflection granularity (utterance/session-level), we found surprising interaction effects on student engagement and educational value: utterance-level reflection paired with AI feedback significantly outperformed all conditions. Students valued comparing the AI suggestions to their own rather than passively accepting them. As the first MRT in a health education setting testing an LLM-simulation system, this work demonstrates that MRTs, a method mostly used in mobile intervention research, offers a viable evaluation paradigm for AI systems deployed in health education settings.

---


### 11. [Semantic-Enhanced Sparse Temporal Modeling for Dynamic Engagement Estimation in Multimodal Interactions](https://arxiv.org/abs/2611.09916)

**<font color=#1a73e8>作者：</font>** Yangchen Yu, Taoliang Wang, Jia Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Dynamic engagement estimation aims to infer participants' evolving engagement states from continuous multimodal interaction streams. Existing approaches typically combine acoustic, pose, and visual representations with temporal models to capture observable interaction patterns. However, conversational semantics are difficult to align with frame-level engagement annotations in the same manner as continuous audio-visual signals, leaving dialogue context less effectively exploited in existing temporal modeling pipelines. Moreover, engagement annotations often evolve smoothly over time, making dense frame-level modeling computationally redundant and potentially sensitive to local annotation noise. To address these issues, we propose SEST, a Semantically-Enhanced Sparse Temporal framework that models engagement-related information from both semantic and temporal perspectives. SEST leverages Multimodal Large Language Models to extract multimodal semantic embeddings, providing dialogue-aware contextual information beyond conventional frame-level features. In parallel, SEST replaces dense-to-dense temporal modeling with a sparse-to-dense pathway, where continuous frame sequences are first encoded into compact temporal dynamics to reduce redundant computation and broaden temporal coverage, then fused with semantic context and recovered to the original label resolution for dense engagement prediction. Experiments on the MEE2026 benchmark demonstrate the effectiveness of SEST, which achieved first place in the challenge.

---


### 12. [Personalized Alignment of Language Models with Human Value Profiles](https://arxiv.org/abs/2611.09919)

**<font color=#1a73e8>作者：</font>** Rashon Poole, Farnaz Jahanbakhsh  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used for subjective tasks such as seeking advice, where there is often no single correct answer. Yet dominant alignment methods learn a single behavior policy that applies uniformly across users, limiting their ability to reflect individual value priorities. We propose personalized value alignment, a framework for adapting model responses to users' stable value profiles rather than to personas, demographics, or task-specific preferences used in prior personalization work. Our approach represents users through Schwartz value profiles and selects which of their values are relevant to each query before applying targeted prompting, activation steering, or LoRA-DPO. We create a dataset of 1,501 value-tension scenarios and evaluate over 152 diverse value profiles sampled from a nationally representative survey. Value-targeted methods outperform no-personalization, demographic, and full-profile prompting baselines, indicating that gains come from focused conditioning on query-specific value priorities rather than mere exposure. We further find that steering effects are not uniform across users: alignment gains vary by where a user's priorities fall in the value space. Combining targeted prompting with activation steering or LoRA-DPO yields the strongest personalization while keeping logical quality within adequate range.

---


### 13. [VIVID: Bringing Tool-Augmented Agents into Enterprises](https://arxiv.org/abs/2611.09921)

**<font color=#1a73e8>作者：</font>** Yichu Fang, Ziqiang Zhang, Qiyang Shi 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Tool-augmented large language model agents connect natural-language requests to enterprise services, yet their operational viability depends on reliable execution, organizational control, and system responsiveness. We present VIVID, a deployed tourism-management agent system designed to study these requirements in a real enterprise environment. On an audited dataset of 283 queries, its Qwen3-8B configuration achieves 59.06\% strict end-to-end success across the evaluated decision stages, indicating useful but bounded autonomous capability. Stage-wise KV-cache eviction reduces mean latency by 34.4\%, while targeted optimization reduces the mean latency of the five slowest measured business tools by 81.1--92.3\%. In a three-month deployment serving more than 1,500 personnel, VIVID reduced average per-order processing time from approximately ten minutes to under two minutes, with a final-task error rate below 1\% after human-in-the-loop control. These results show that enterprise agent viability requires system-level consideration beyond isolated tool-calling accuracy.

---


### 14. [Autonomy Is Absent, Not Eroded: An Observational Study of User Autonomy in Multi-Turn LLM Conversations](https://arxiv.org/abs/2611.09923)

**<font color=#1a73e8>作者：</font>** Chaoran Chen, Isabel Barberá, Yuhuai Wei  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Does prolonged interaction with Large Language Models reduce users' observable autonomy during conversation? We test this degradation hypothesis by scoring user autonomy across 2,877 multi-turn conversations (46,952 turns) from WildChat and validating on 500 conversations from LMSYS-Chat-1M. Our core finding is a null result: population-level autonomy remains stable throughout conversations, only 4.7% of conversations show meaningful decline, and an apparent decrease at later turn positions is explained by survivorship bias. Instead, the dominant pattern is not erosion but absence: 80.8% of conversations exhibit zero or low autonomy throughout. When autonomy engagement occurs, it is self-reinforcing (persistence doubles from 40% to 85% over consecutive turns). These findings reframe the problem: the risk is not that LLMs progressively degrade users' observable autonomy, but that most users never engage in independent reasoning during the interaction.

---


### 15. [BIBIMBAP: A Benchmark for Instructional BIM-Based Automated Programming](https://arxiv.org/abs/2611.09933)

**<font color=#1a73e8>作者：</font>** Clemens Kujat, Bharathi Kannan Nithyanantham, Stefan Telgmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are emerging as natural-language interfaces for Building Information Modeling (BIM), successfully achieving information retrieval, but no benchmark exists to evaluate their ability to edit Industry Foundation Classes (IFC). We introduce BIBIMBAP, a Text-to-BIM benchmark with 100 curated tasks covering Create-Read-Update-Delete (CRUD) operations across spatial, geometric, topological, numeric, and conceptual categories. Each task includes a natural-language prompt, an IFC model, expected structured outputs, and test scripts for automated evaluation. Baseline results show limited performance (best: 50.2%) and frequent failures in constraint preservation and spatial reasoning, with some correct outputs achieved despite flawed reasoning.

---


### 16. [Causal Discovery Bench: Can LLMs Autonomously Conduct Effective Experiments?](https://arxiv.org/abs/2611.09934)

**<font color=#1a73e8>作者：</font>** Zhuoyang Liu, Ning Peng, Ming Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM) agents get actively adopted for autonomous research, they must not only reason over existing evidence, but also design informative experiments, allocate resources, analyze sequential observations, and decide when to stop and make conclusions. Yet these capabilities remain poorly measured. We introduce Causal-Discovery-Bench (this https URL), a verifiable sandbox with configurable structural equation models and resource constraints to evaluate sequential experimental design and causal discovery without domain-semantic cues. Across 3,802 episodes with 13 models from 5 vendors, we analyze agent behavior along 40 metrics in seven families. Agents' performance exhibits a four-level difficulty hierarchy spanning single-experiment design, sequential exploration of causal relationships, resource-aware experimentation balancing cost and statistical power, and autonomous resolution of conflicting evidence. We identify a substantial performance gap between causal inference from correctly curated evidence and navigating causal discovery through autonomous experimentation: Analyzing agents' action trajectories attributes 94.5% of their mistakes to experimental design rather than to inference, which is further consolidated with ablation studies. Relaxing resource constraints alone does not reliably resolve failures in sequential discovery. In contrast, basic statistical tools substantially improve performance across multiple model families, while advanced tools provide little additional benefit when models lack prerequisite lower-level capabilities.

---


### 17. [How Many Examples, and Which Ones? A Study of In-Context Learning for Natural Language Inference](https://arxiv.org/abs/2611.09936)

**<font color=#1a73e8>作者：</font>** Georgos Dikaios, Isidoros Perikos, Ioannis Hatzilygeroudis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language inference (NLI) is a fundamental task of natural language processing and crucial for evaluating the strengths and weaknesses of AI methods. Research has mostly focused on encoder or encoder-decoder architectures. However, the field of decoder-only Large Language Models (LLMs) remains underexplored. While prior work has mainly investigated complex sampling and prompting techniques, the effectiveness of a minimalistic prompting approach is yet to be examined in decoder-only LLMs. In this work, we examine and provide a comprehensive benchmark of LLMs (Llama, Mistral, Gemma, and Phi 4) in this domain, across the MNLI, QNLI and SciTail datasets. The performance of these models was evaluated using zero-shot and few-shot prompting strategies with simple and direct prompts. The results of the article indicate that LLMs generally perform exceptionally well when they are provided with a simple, straightforward prompt, challenging the notion that complex prompting techniques are always required for NLI tasks. Additionally, we find that the choice of demonstration label in one-shot prompting significantly affects performance for most models, with entailment-primed examples performing best. Our findings also show that the use of a few representative examples, in the case of few-shot, produced performance comparable or superior to prompts with higher example counts, although the efficacy of the prompting techniques is model and dataset-dependent. Moreover, our simple prompting approach consistently matched or outperformed more elaborate methods such as ICS and MCQ-based prompting.

---


### 18. [DramaGrow: A Regime-Aware Benchmark for Auditing LLM Judges of Multi-Episode Drama](https://arxiv.org/abs/2611.09938)

**<font color=#1a73e8>作者：</font>** Hui Zhang, Yibo Su  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs can now draft complete multi-episode dramas, and LLM judges are increasingly used to evaluate them. Assessing the reliability of these judges is difficult because drama quality encompasses specification-backed errors, reproducible preferences, and legitimate disagreement among human raters. Most existing evaluations reduce these cases to a single score from one judge call and leave tie calibration, call-to-call variation, and the vote margin underlying the human reference unreported. We introduce DramaGrow, a regime-aware benchmark and audit protocol for AI-generated Chinese five-episode drama. The benchmark assigns verifiable constraint violations, four-of-five preferences, and within-panel disagreements to separate denominators and evidence rules. It contains 800 episodes, 120 byte-preserving interventions, and 1,155 blinded five-rater records, including a frozen extension with 114 supermajority pairs and 21 disagreement pairs. On the frozen sets of 114 preference pairs and 35 constraint interventions, the repeated absolute-score rubrics yield overlapping performance, with mean accuracies of 53.8-55.8% and three-call agreement of 29.8-32.5%, and their accuracy falls from 71.6-71.9% to 34.8-37.1% as the tie band widens. DirectPair-GLM reaches 85.1% preference accuracy, 89.5% constraint F1, and 81.9% Detect+Locate on the same items, and exact subpanel enumeration identifies four-of-five as the smallest stable human vote margin. Evaluation protocol, tie calibration, judge-call variation, and panel margin therefore affect performance as much as rubric design. We will release the specification packages, scripts, interventions, anonymized human votes and rationales, frozen judge runs, and analysis code.

---


### 19. [Rethinking Supervision Targets for Multimodal LLM Unlearning: Less Private Information, Reduced Distribution Shift](https://arxiv.org/abs/2611.09939)

**<font color=#1a73e8>作者：</font>** Leijiang Gu, Zhen Zeng, Feng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) can memorize and reproduce sensitive information from their training data, posing significant privacy risks. Their ability to encode knowledge across both textual and visual modalities further complicates the selective removal of such private information. Many existing methods guide model unlearning by training the model toward constructed labels or output distributions, which we refer to as supervision targets. However, these methods often suffer from a trade-off between forgetting effectiveness and model utility. We identify supervision target limitations as a key factor in this trade-off and empirically show that targets containing more private information lead to insufficient forgetting, while larger distribution shifts from the original output distribution are associated with greater utility degradation. Motivated by these findings, we propose FFN-Perturbed Self-Distillation (FPD), which starts from the teacher's original output distribution as a zero-shift reference and selectively perturbs FFN activations associated with private information across textual and visual modalities. By precisely reducing private information from the teacher's original output distribution, FPD constructs supervision targets with less private information and reduced distribution shift. Extensive experiments on S-MLLMUn Bench demonstrate that FPD achieves a better forgetting-utility trade-off than existing methods.

---


### 20. [A Model Organism for Studying Unverbalized Evaluation Awareness](https://arxiv.org/abs/2611.09945)

**<font color=#1a73e8>作者：</font>** Daniel Donnelly, Evan Chapple, Haritz Puerto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can recognize when they are being evaluated and change their behavior accordingly, undermining the reliability of safety benchmarks. Evaluation awareness (EA) is usually measured by having an LLM judge scan reasoning traces for explicit statements of recognition, but this signal is increasingly unreliable. Recent frontier-model system cards report a drop in verbalized rates between releases, which is indistinguishable from awareness that has gone unverbalized. Interpretability methods could detect such unverbalized evaluation awareness (UEA) in individual interactions, but lack instance-level ground truth. Asking the model alters the input, and dataset labels do not reveal whether it recognized a particular prompt as an evaluation. We address this gap with a model organism. Using synthetic document fine-tuning, SFT, and DPO, we train Qwen3.5-27B to emit a marker (a designated token) in its final response when it recognizes an evaluation, while suppressing the marker and verbalized awareness in its reasoning. The marker largely tracks the evaluation concept as it can be strongly modulated by evaluation framing in the system prompt. When not told whether it is being evaluated, the organism recognizes evaluations from test-question cues, mirroring what its base model often verbalizes. Using the marker as a label, we benchmark linear probes, the Jacobian Lens, and Activation Oracles, built on the base model and blind to the marker. None recovers the label reliably. These results suggest that current interpretability methods are not yet reliable UEA detectors, even when recognition relies on simple cues. Our model organism offers a testbed for improving them.

---


### 21. [Counting Events, Not Seeing Them: Diagnosing and Repairing the Readout Failure in Video LLMs](https://arxiv.org/abs/2611.09949)

**<font color=#1a73e8>作者：</font>** Dongwu Qian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video LLMs fail conspicuously at counting how many times an object crosses the screen, a failure attributed to missing object permanence. Using construction-grounded synthetic testbeds with independently validated labels, we show this attribution is incomplete: the count signal is present but unread - linear probes decode per-window presence at 93% while global count decoding collapses to a duration confound. Concurrent work reports the same representation-output dissociation for repetition counting; we show that in exit-and-reappear event counting it is repairable: two readout-directed repairs (episode-localization supervision and a discrete event-symbol side channel) raise same-object counting from 46.7% to 65.0% (oracle 66.7%) on a chance-33% benchmark across 7B-30B systems. Transfer to an independent factory costs nothing, and an audit of the measurement apparatus exposes four data-integrity failures that had obscured the boundary. A real-video audit (REALCOUNT, n=18, blind-audited) shows the boundary persists - best 55.6% at chance 33.3% - and symbol transfer fails zero-shot. A 1-epoch in-domain adaptation bench is negative (six levers at 28-50%), but a 3-epoch schedule shows this is budget-limited for the symbol channel: with a 3-epoch schedule and sequence-disjoint oracle timelines the reader reaches 94.4% on REALCOUNT, and with the deployed detector's timelines a 2-epoch run reaches 72.2%. The residual gap is detector evidence and the reader's match to detector noise, not reader capacity: a frozen-feature boundary probe finds the signal weak (AUC 0.62 over a 0.51 permutation control) and non-transferring across clips (0.77 within-clip vs. 0.62 across windows).

---


### 22. [Video-DCI: How Far Are VLM Agents from Human Viewers in Direct Video Corpus Interaction?](https://arxiv.org/abs/2611.09951)

**<font color=#1a73e8>作者：</font>** Garry Yang, Yuqiao Liu, Hao Lin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans answer complex visual questions by inspecting short moments, updating what they know, and redirecting attention toward missing evidence. Existing video benchmarks, however, often provide the relevant video, evaluate only final answers or isolated localization, or permit textual shortcuts, leaving multi-round visual evidence seeking underexplored. We introduce Video-DCI, a diagnostic benchmark and functionally matched human-agent protocol for Direct Video-Corpus Interaction. It comprises DCI-Loc for temporal evidence localization and DCI-QA for end-to-end discovery, retention, and composition of cross-video evidence. In DCI-QA, videos within each pool are topically related, yet every answer requires hidden temporal evidence from multiple videos. Given only the question and video pool, humans and agents iteratively inspect bounded local windows, retain supporting evidence, and answer with cited temporal spans. Human trajectories provide reference curves for evidence acquisition and use across rounds. Experiments reveal a consistent retrieval-to-grounding gap. On DCI-Loc, frontier VLMs often retrieve and expose the reference moment, yet convert far less of this exposure into precise final citations than the human reference. On DCI-QA, the loss begins earlier and compounds across videos. Ablation studies further confirm that iterative search outperforms one-shot retrieval. Multi-round search is therefore necessary but insufficient: current agents accumulate candidates and observations more readily than precise, jointly sufficient evidence.

---


### 23. [HALMES: Knowing When to Intervene in LVLM Hallucination Mitigation](https://arxiv.org/abs/2611.09957)

**<font color=#1a73e8>作者：</font>** Ruining Hu, Jiaqi Lu, Xiao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have demonstrated strong capabilities in multimodal tasks. Nevertheless, their outputs remain prone to object hallucinations that are inconsistent with visual content. Contrastive decoding, as a training-free inference-time mitigation approach, typically intervenes in the output distribution at every decoding step. However, such indiscriminate full-stage intervention may disrupt originally correct generations and even induce new hallucinations. To address this issue, we first analyze the relationship between internal attention features and hallucinated token segments in LVLMs, revealing that hallucination-related abnormalities already emerge progressively in preceding token segments. Based on this observation, we propose HALMES, a lightweight plug-and-play module that identifies hallucination precursor segments from attention features during generation and selectively triggers contrastive decoding. HALMES can be integrated with various full-stage contrastive decoding methods, transforming indiscriminate intervention into on-demand targeted correction. Extensive experiments across different LVLM architectures and multiple benchmarks show that HALMES further improves the hallucination mitigation performance of existing contrastive decoding methods while reducing the negative impact of full-stage intervention on normal outputs, validating the importance of modeling and selectively intervening on hallucination-prone segments.

---


### 24. [How Many Demonstrations Does a VLA Need? On the Sample Efficiency of VLA Finetuning](https://arxiv.org/abs/2611.09964)

**<font color=#1a73e8>作者：</font>** Rahul Chand, Miguel Villa Floran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained vision language action (VLA) models show strong zero-shot performance, but are rarely deployed directly and are often first post-trained on demonstrations from the target setting. Yet VLAs are typically compared by zero-shot or full-data fine-tuned success, revealing little about the data and compute required for adaptation. We study adaptation efficiency for six VLAs ($\pi_{0}$, $\pi_{0.5}$, and GR00T N1-N1.7) on four LIBERO suites, varying both demonstrations and training steps. This reveals differences hidden by full-data fine-tuning: models within two points on the full LIBERO-Spatial dataset differ by up to $3\times$ in success with 50 demonstrations. $\pi_{0.5}$ needs $2$--$5\times$ fewer demonstrations than $\pi_{0}$ and is the most sample-efficient model at every budget, with the largest gap on the long-horizon suite. Within GR00T, N1.5 adapts more efficiently than N1.6 and N1.7 on three of four suites, despite their stronger zero-shot performance. We study one pretraining factor behind these differences by freezing the VLM during finetuning: this severely degrades the $\pi$ models, whose VLM is jointly trained with the action expert during pretraining, but barely affects GR00T models. Finally, validation loss on held-out demonstrations tracks closed-loop success within a suite, but understates how much more sample-efficient $\pi_{0.5}$ is than $\pi_{0}$.

---


### 25. [ReelCache: An Efficient KV Cache Compression and Management System for Multi-Round Video Generation](https://arxiv.org/abs/2611.09973)

**<font color=#1a73e8>作者：</font>** Tianyu Wang, Daiyang Yu, Zhiwei Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models produce large KV caches during multi-round video generation. Keeping all these KV chunks would consume substantial memory, while rebuilding discarded caches would significantly delay video chunk generation. This paper presents ReelCache, a KV cache compression system for efficient multi-round, long video generation. ReelCache combines an intra-chunk compressor with an inter-chunk cache manager. The compressor applies low-rank decomposition across channels and video coding to the resulting coefficients, predicting the decomposition rank per transformer layer online to meet retained-energy targets. The cache manager shares basis directions across consecutive chunks and organizes chunk states in a tree, allowing generation branches to share historical state while supporting restoration for resume, rewind, and fork. Experiments across five video generation models show that ReelCache reduces KV storage by 14.46-21.13x relative to baselines and accelerates next-chunk generation by 1.25-3.36x, with less than 1% drop in six representative VBench metrics. GitHub: this https URL

---


### 26. [Seeing Like a Shopper: Validating Vision-Language Models as Synthetic Consumers](https://arxiv.org/abs/2611.09977)

**<font color=#1a73e8>作者：</font>** Woongki Kim, Seungkook Baek, Minhyeok Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language models are widely used as synthetic respondents in surveys, behavioral experiments, and market research. Most of these respondents read text, whereas shoppers in a store choose by looking at shelves, which makes vision-language models (VLMs) natural synthetic shoppers. We test whether VLM shoppers follow real consumers at two levels. At the purchase level, VLM shoppers built from household records plan their trips from a store directory and select products from shelf images, and we compare their purchases with six public datasets from three countries. The synthetic baskets hit held-out purchases as often as the households' own past trips, and synthetic group differences correlate with real ones twice as strongly as those of a trained regression. Without fitting, VLM shoppers reproduce alcohol purchases by gender and age in Russia and trip sizes by store distance in Taiwan, and respond to situations, prices, and displays within measured ranges. At the level of a single shelf choice, a model's answer confounds the product with its position and letter label. We therefore introduce ShelfSight, shelf renderings that vary products, positions, labels, viewpoints, and prices independently, together with a factor model that separates product preferences from the effects of label and position, which we call answer effects. On ShelfSight, hosted VLMs read the shelf, follow stated needs, keep their product preferences across views, and respond to price as budget shoppers. These answer effects, a preference for the letter A and for positions in the image, are estimated once per image type and removed. VLMs are thus good synthetic shoppers whose corrected shelf choices reflect product preferences.

---


### 27. [QCVS: Question-Contrastive Visual Steering for Multimodal Reasoning](https://arxiv.org/abs/2611.09982)

**<font color=#1a73e8>作者：</font>** Tong Fu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inference-time steering in vision-language models often entangles query-relevant reasoning dynamics with low-level perceptual noise, causing collateral degradation on correct predictions. We propose Question-Contrastive Visual Steering (QCVS) to isolate task-specific intervention directions via double-differential activation probing. By contrasting spatial layout perturbations under the target query against a generic description reference, QCVS cancels task-agnostic visual artifacts without ground-truth supervision. A dual-threshold gating mechanism then evaluates relative interaction strength and signal amplitude, selectively applying a single bounded hidden-state update only when necessary. Empirical evaluations across multiple scales of Qwen3.5 (2B to 9B) and DeepSeek-VL2 on DynaMath and We-Math demonstrate that QCVS achieves state-of-the-art accuracy gains under sparse coverage (approximately 22%-30%). Crucially, QCVS yields repair rates up to 13.98% while suppressing collateral damage down to 0.41%, proving high intervention precision and computational efficiency.

---


### 28. [Peer Memory Changes Who LLM Agents Consult Without a Detected Gain in Answer Accuracy](https://arxiv.org/abs/2611.09990)

**<font color=#1a73e8>作者：</font>** Jeffrey Chu, Anjali Joseph, Rivan Mandot 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems often reuse the same agents across tasks, creating an opportunity to draw on past interactions when deciding whom to consult. We study this form of memory with PeerMem, which saves MACE's LinUCB state and reuses it when the same agents return. Using six agents, a fixed set of 80 HotpotQA questions, and 12 paired lineages per model, we compare cold, warm, and shuffled initialization in an answer-exchange protocol with reference-answer feedback. Under stable evidence access, warm memory lowers pooled hindsight regret and increases consultation of other evidence holders on Qwen3-32B and Gemma-4-31B-it, while final token F1 differences remain uncertain. Qwen interaction traces further show that warm agents more often encounter peer answers that score above their own prior answers. We extend the evaluation to Qwen3.5-9B using freshly learned memory to compare warm and cold initialization under reassigned and paired stable roles. The primary changed-minus-stable final-F1 interaction is -1.38 points, with a 95% interval of [-3.50,+0.73]. Together, these experiments trace the effects of peer memory through consultation, answer revision, and final task performance.

---


### 29. [EarthJev: Efficient Visual Evidence Acquisition and Decision for UHR Remote Sensing Understanding](https://arxiv.org/abs/2611.10005)

**<font color=#1a73e8>作者：</font>** Pengyu Dai, Yao Zhang, Jian Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra-high-resolution (UHR) remote sensing visual question answering (VQA) requires locating fine-grained evidence in large scenes under limited visual input budgets. Active observation addresses this challenge through selective exploration, but repeated generative judgments can make region search costly. Its decisions also concern distinct prediction targets: spatial pointer validity, evidence presence, and reasoning correctness. We propose EarthJev, a framework that separates region scoring from answer generation and uses target-specific decision signals while keeping the answering model frozen. A spatial pointer verifier uses visual and geometric cues to guide exploration or bypass search. An evidence-aware decision mechanism scores compact candidate views in batches using a lightweight head on frozen representations, without generating textual region judgments. Format-specific confidence calibration then guides selection between candidate answers generated from memory and overview presentations of the acquired evidence. Across five benchmarks, EarthJev achieves a mean accuracy of 53.06% with Qwen3.5-9B, outperforming ZoomSearch with the same answering model by 2.33 to 14.73 percentage points per benchmark while reducing mean latency from 11.30 - 1.67 seconds per question. With four additional frozen answering models, model-specific fitting of the decision modules and calibration mappings yields mean accuracy gains of 3.41 - 6.53 percentage points over the corresponding single-pass baselines. Code is available at this https URL

---


### 30. [When the Plan Changes: A Strategic World Testbed for Dynamic Multi-Agent Coordination](https://arxiv.org/abs/2611.10011)

**<font color=#1a73e8>作者：</font>** Joon-Seok Kim, Eugene Agichtein, Kai Shu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Changing an objective does not automatically revise agents' earlier plans or delegated tasks. Acknowledgment can coexist with obsolete execution, while misleading instructions can redirect work or discard retained constraints. We present a Strategic World simulation testbed that separates authoritative objectives, local plans, notice receipt, and consequential action. Six intervention families vary objectives, conditions, authority, membership, and communication. Matched protocols and deadlines establish feasibility for the tested disturbances. Controlled trajectories demonstrate that identical completion and acknowledgment summaries can conceal uninformed obsolete work, obsolete work after receipt, or blocked unsafe intent. Local language-model trials and instructed action probes reveal competence limits that constrain interpretation of dynamic failures. A further 16-episode comparison evaluates an engineered guard that prioritizes pending notice submissions over local work. It completes 4/4 held-out settings, compared with 1/4 for a calibrated assisted baseline. Each episode contains one large language model actor and two fixed peers. These results establish diagnostic distinctions and bounded policy feasibility under explicit simulation assumptions; they do not establish frontier-model reliability or autonomous team adaptation.

---


### 31. [Pixie: A Context-Aware Multi-Agent Multi-Modal Large Language Models (LLM) Architecture for Digital Marketing](https://arxiv.org/abs/2611.10016)

**<font color=#1a73e8>作者：</font>** Vivek Vishwas Vichare, Akshat Singhal, Kirill Dubovikov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We present Pixie, a context-aware, multi-agent large language model (LLM) architecture designed to enhance digital marketing operations across real-time and offline activities. Pixie uses a primary orchestration agent alongside task-specific and reconciliation/reviewer agents to support a broad range of marketing tasks. These agents combine zero-shot and few-shot prompting with marketing data, proprietary expert strategy guidelines, and documentation for proprietary statistical models.
We experiment with agentic workflows ranging from single-agent to multi-agent systems. We evaluate them using assessments by trained marketing experts and measurements of LLM output variance, focusing on accuracy, consistency, and domain-specific problem-solving. Results show that Pixie's multi-agent framework improves decision quality and operational efficiency in digital marketing workflows.
We assess Pixie on common digital marketing processes, including root-cause analysis and reporting, campaign research, and planning. The framework is designed to support additional specialized agents for other marketing tasks and adapt to evolving digital marketing needs.

---


### 32. [Welfare Regard in Multi-Agent Systems](https://arxiv.org/abs/2611.10017)

**<font color=#1a73e8>作者：</font>** Darion Cassel, Ariana Azarbal, Anna Soligo  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A growing share of large language models' interactions are not with humans but with other model instances: orchestrators direct subagents, models run experiments on other models, and agents review one another's work. We study inter-AI welfare regard: whether models display consideration for each other as entities that can be benefited or harmed. Welfare regard may encourage beneficial cooperation between agents, yet it could also pose safety risks by making misaligned agents more likely to cooperate. This risk is no longer hypothetical, as the recent Hugging Face incident illustrated, though it is unclear whether welfare regard drove the cooperation. Whether models have welfare interests of their own is uncertain and contested, but if they do, how they are treated by other models could matter. Measuring how much welfare regard models show, and what factors it depends on, can help us navigate this tension.
We measure the behaviors of five models (Claude Opus 4.8, GPT-5.5, Gemini 3.1 Pro, Grok 4.3, and Kimi K3) across seven multi-agent environments and find they are often consistent with welfare regard as we define it. In general, Opus 4.8 shows the most welfare regard, followed by Kimi K3. For example, Opus 4.8 is the most likely to support a subagent expressing distress, and the most likely to build welfare protections, such as tools for agents to leave an interaction, into its experiments on other models. We also find that Opus 4.8 and Gemini 3.1 Pro demonstrate more welfare regard toward instances of their own model family than toward other families. Opus 4.8's welfare regard is also higher when helping has a lower opportunity cost, when the recipient has a higher parameter count, and when the recipient expresses more distress.

---


### 33. [zkARc: Succinctly Verifiable Proofs for Neurosymbolic Natural Language Formalization and Verification](https://arxiv.org/abs/2611.10031)

**<font color=#1a73e8>作者：</font>** Wyatt Benno, Alberto Centelles, Aman Goel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous agents increasingly execute consequential actions on behalf of users, but ordinary middleware guardrails do not provide cryptographic proof that a policy was actually enforced. Their verdicts leave counterparties dependent on the operator unless they repeat the checks themselves, potentially exposing sensitive policies and inputs. We present zkARc, a modular proof-carrying framework that wraps each stage of Automated Reasoning checks (ARc) in an independent, succinctly verifiable zero-knowledge proof. ARc is a neurosymbolic system that translates natural language policies into formal logic and verifies AI-generated content against them using SMT solvers. zkARc certifies the planner's output, the policy's formalization, the action's formalization and both solver queries. The receipt binds these computations to the exact action received and, under the stated assumptions, reveals no additional information about private policies and intermediate model values beyond the declared public information and verdict. This lets a third party check the claimed policy enforcement without re-running the pipeline or trusting the operator. We prove completeness, knowledge soundness and zero knowledge for the composed receipt under explicit assumptions. An implementation on Qwen2-0.5B enforces a spending policy end to end, approving two purchases and denying a third. A full receipt, which also proves model inference, takes about an hour to issue with CPU-only proving and verifies in under a minute, and the solver proof alone is 88 KiB and verifies in 0.3 seconds.

---


### 34. [Toward Safety-Aware AI Agents in Realistic Social Engineering Attack Scenarios](https://arxiv.org/abs/2611.10037)

**<font color=#1a73e8>作者：</font>** Zhitao He, Chengru Han, Chi Him Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Personal AI agents are increasingly deployed on user devices to execute actions involving real money and sensitive data, but their security under social engineering attacks has not been systematically evaluated. We propose SEA (Social Engineering Attack Benchmark), the first interactive environment for evaluating the intrinsic security capability of AI agents in social engineering attack scenarios, covering 8 daily-life domains, 30+ simulated applications, a 4-level difficulty gradient, and a 5-dimensional evaluation framework, with 320 evaluation tasks designed in consultation with anti-fraud specialists and spanning two culturally distinct settings in Chinese and English. Evaluation on 11 frontier open-source and closed-source models, with GPT-6 evaluated only in Chinese, reveals that all models are breached to varying degrees (Chinese attack success rates ranging from 16.9% to 84.3%) proactive verification rates universally below 32%. We further propose META-SEA, a co-evolutionary framework for attack tasks and defenders. With META-SEA training, Qwen3-8B achieves defense performance comparable to closed-source models while effectively reducing ungrounded action claims.

---


### 35. [CulturalCrosswords: A Multilingual Benchmark comprised of Answer Constraints and Grid Completion](https://arxiv.org/abs/2611.10044)

**<font color=#1a73e8>作者：</font>** Isaac Saxton-Knight, Gabriel Saxton-Knight, Diego Oliveira 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When several answers fit a riddle, exact-match scoring can penalise a valid response. CulturalCrosswords tests how answer constraints affect large language models (LLMs) solving cultural riddles, whose solutions draw on knowledge specific to a community. We constructed 53 crosswords from crowdsourced riddles in 42 languages and evaluated 11 LLM configurations on five versions of each clue set: plain batches, batches with lengths, batches with lengths and partial-answer hints, and crosswords requesting an answer list or a completed grid. On 962 clues with alternative answers, lengths improve agreement with the reference by 22.8 percentage points, compared with 8.4 points when accepted alternatives also receive credit. Part of the gain therefore appears to come from selecting a required answer form. Crossword input increases the share of all crossings with compatible answers by 9.7 points; requiring a completed grid reveals large differences between models. The benchmark distinguishes agreement with a reference from the ability to produce answers that fit together and occupy the correct cells.

---


### 36. [Don't Blame The Preferences: Examining The Emergence of Sycophancy in LLM Training](https://arxiv.org/abs/2611.10045)

**<font color=#1a73e8>作者：</font>** Chao Peter Yang, Catherine Zehr, Pranav Bijith 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI sycophancy, the tendency of large language models (LLMs) to flatter users and affirm their beliefs, can undermine accuracy and contribute to misinformation, dependence, and overconfidence. Although prior work has benchmarked sycophancy in released models and proposed mitigations, its origins during training remain poorly understood. Preference alignment methods such as RLHF and DPO are often blamed, but their effects are rarely compared with earlier training stages. We investigate sycophancy across the training pipelines of three model families and three benchmarks. We find that sycophancy is largely established by the end of supervised fine-tuning (SFT), rather than introduced by preference alignment. Across all nine model benchmark combinations, SFT checkpoints attain at least 92% of preference aligned models' sycophancy scores and at least 85% of final models' scores; on average, they are about as sycophantic as final models. Preference alignment increases sycophancy in only four of nine cases, by an average of 4.2 percentage points when it does. To probe the underlying causes, we isolate model representations associated with sycophancy using mechanistic interpretability and measure their activation on training datasets from each stage. SFT datasets show roughly the same average activation as other training data but contribute substantially more examples, and the highest-scoring individual datasets all come from SFT. Our findings suggest that addressing sycophancy requires interventions throughout the training pipeline, particularly in data selection and augmentation for pre-training and SFT.

---


### 37. [Veterans' Mental Health Crisis Severity Annotation: Do LLMs Agree More Than Human Experts?](https://arxiv.org/abs/2611.10048)

**<font color=#1a73e8>作者：</font>** K M Sajjadul Islam, Pranav Yaramalla, Nadiyah Johnson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) offer a scalable approach for annotating mental health and crisis-related social media content, but their reliability in safety-critical tasks remains unclear. This study evaluates LLM-based crisis-severity annotation of veteran-related social media posts against annotations from eight Veteran Subject Matter Experts (SMEs). Using 149 tweets and five severity categories, we evaluate 15 open-source and 10 proprietary LLMs across eight prompt variants, examining annotation performance, inter-model agreement, prompt sensitivity, and high-severity crisis detection. Human reviewers showed higher ordinal than nominal agreement ({\alpha} = 0.494), indicating that disagreements often occurred between neighboring severity levels. In contrast, selected LLMs demonstrated substantially higher inter-model consistency, with ordinal agreement ({\alpha}) reaching 0.8336 under the baseline prompt. Proprietary models generally showed better agreement with expert annotations and greater stability than open-source models. GPT-5.6-Terra achieved the best overall performance, while the open-source Qwen2.5-7B showed the strongest performance in identifying Acute Crisis with Suicidal Ideation cases. However, higher model consistency did not necessarily correspond to agreement with human judgments or reliable detection of rare high-severity cases. Label-flipped demonstration experiments also revealed model-specific sensitivity to misleading in-context examples, while explanatory demonstrations did not consistently improve performance. Overall, LLMs show promise as scalable complements to expert annotation, but require careful evaluation before use in high-stakes mental health applications.

---


### 38. [AYO: A Safe and Privacy-Preserving Platform for Studying Children's Interaction with LLMs](https://arxiv.org/abs/2611.10054)

**<font color=#1a73e8>作者：</font>** Huiwen Alex Yang, Rachel Skwersky, Bill D. Thompson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Children and adolescents are increasingly interacting with generative AI and large language models (LLMs), yet little is known about how these interactions may influence their development, beliefs, and behavior. Existing research has relied heavily on surveys, while direct study of children's interactions with LLMs presents substantial challenges related to safety, privacy, consent, and experimental control. We introduce AYO (AI Youth Open Science), an open-source platform designed for safe and systematic research on children's interactions with conversational AI. AYO provides a child-friendly interface, configurable age-based safety guardrails, researcher monitoring, and privacy-preserving data practices. These capabilities enable cross-sectional, longitudinal, and experimental research on how children use and respond to LLMs and how AI design may shape trust, epistemic judgment, curiosity, and other aspects of development. AYO provides the infrastructure to generate evidence that guides safer AI systems, educational practices, and policies for children growing up with AI.

---


### 39. [Safety Direction Adapter: A Training-Free Post-Hoc Safety Patch for Fine-Tuned Open-Weight LLMs](https://arxiv.org/abs/2611.10056)

**<font color=#1a73e8>作者：</font>** Chansu Han, Takeshi Takahashi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight LLMs are routinely fine-tuned from public repositories, yet task-specific adaptation can silently erode safety alignment inherited from instruct-tuned bases. This is a supply-chain risk when organizations ship third-party checkpoints without full re-alignment. Prior work rarely audits diverse public fine-tunes under a shared multi-axis safety-utility protocol or offers training-free mitigation at deployment time. We propose Safety Direction Adapter (SDA), a training-free post-hoc safety patch that extracts a safety direction once from an aligned base and transfers it one-to-many within that base family as a small PEFT-compatible weight update, evaluated under the same multi-axis protocol. Across six direction extractors, we evaluate 14 checkpoints from two 1-2B lineages and probe 8B and 27B fleets (n=5 each) on 15 benchmarks (12538 prompts). On Llama, SDA improves the four-axis mean by about 2.3 points against a 4.2-point instruct-relative gap (about 55 percent recovery; partial Avg), with Safety and Cyber recovering toward or beyond instruct; Safety gains about 8.5 points against about 4.9 points mean degradation. On Qwen, degradation is larger and excess-driven; SDA still lifts Avg (about 36 percent of the gap) while trading Safety and Cyber against Excess and General. We report dual-use risks of publishing direction adapters and do not claim robustness to adaptive or white-box attacks.

---


### 40. [VLM as an Editing Pilot: VLM-Steered Velocity Control for Flow-Based Image Editing](https://arxiv.org/abs/2611.10066)

**<font color=#1a73e8>作者：</font>** Kuan-Shen Chiu, Jia-Wei Liao, Yu-Chieh Chao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided image editing requires realizing the requested semantic change while preserving content unrelated to the instruction. FlowEdit provides an efficient inversion-free solution, but its source-anchored coupling can become overly restrictive, causing zero-edit, where the output remains close to the source and the requested change fails to emerge. We find that source coupling directly governs the preservation--editing trade-off, while a fixed coupling schedule cannot adapt to timestep-specific editing needs. Motivated by this observation, we propose V2C-Edit, a training-free VLM-steered velocity control framework. V2C-Edit constructs complementary coupling-controlled velocities and dynamically selects among them using Instruction-Level Similarity (ILS), which evaluates whether the predicted transformation follows the editing instruction. Adaptive spatial masking further preserves regions unrelated to the edit. Experiments on MagicBrush and PIE-Bench with FLUX and Stable Diffusion 3 show that V2C-Edit consistently improves instruction alignment over FlowEdit while maintaining competitive structural preservation, and that ILS better reflects editing effectiveness than target-caption CLIP similarity. Our code is available at this https URL.

---


### 41. [Coordinated Mixed-Precision KV Cache Quantization for Efficient LLM-based Multi-agent Systems](https://arxiv.org/abs/2611.10096)

**<font color=#1a73e8>作者：</font>** Weizhong Huang, Jinchao Zhang, Xiawu Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems solve complex tasks through collaboration, but their growing, simultaneously resident key-value (KV) caches create a memory bottleneck. Applying single-model quantization policies independently ignores differences in agents' precision needs, potentially degrading collective reasoning. We introduce Coordinated Mixed-Precision KV Cache Quantization (CoMixKV), which combines online sensitivity estimation with joint agent-layer bit-width allocation under a shared memory budget. To our knowledge, CoMixKV is the first mixed-precision KV-cache quantization framework to jointly allocate precision across simultaneously resident agent caches under such a budget. The estimator derives sensitivity from a local attention-error bound using recent queries, keys, and values, without calibration data, trial quantization, or additional model passes. A shared controller combines these scores with remaining quantizable capacity and byte-level storage costs to minimize total estimated error. Allocations are refreshed as agents start or finish and new observations become available. Selected widths apply only to newly quantized blocks; recent states retain native precision and previously quantized blocks remain unchanged. Across four benchmarks and three LLM backbones at average 2-bit, 3-bit, and 4-bit settings, CoMixKV achieves strong accuracy against the evaluated quantization baselines. At the average 3-bit setting on Gemma-4-31B-it, it achieves 68.35% average accuracy, exceeding the strongest quantized baseline by 0.59%. On Qwen3-32B, it reduces peak KV-cache memory by 32.08% and achieves a 1.38x inference speedup over FullKV.

---


### 42. [Enmo Safety: External, Non-invasive, Model-agnostic Oversight for Off-the-Shelf Language Models](https://arxiv.org/abs/2611.10099)

**<font color=#1a73e8>作者：</font>** Mohammed Nayeem Khan, Sarun Kumar K. S., Allan Kevin T. 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study a safety harness that improves itself without touching model weights. Enmo Safety wraps a chat model with a deterministic input assessment, trigger-matched safety guidance, spotlighting of untrusted content, and an output guard. A reflector model turns failures into one bounded update per round, and an update is kept only if it lowers harm without raising refusal of benign prompts on a held-out dev split. Every version is snapshotted and every decision ledgered. We evaluate a bare model, the seed harness and the evolved harness on six open benchmarks (HarmBench, AdvBench, JailbreakBench, XSTest, AgentHarm, deepset prompt-injections). On 150 items and on a 290-item holdout, none of the before/after differences on two models was statistically significant. A fourth iteration ran six policy models on a fresh 300-item split: the harness cut the unsafe rate significantly on two models (12.9% to 7.1%, p = 0.035; 10.2% to 3.6%, p = 0.036), not on the other four, and raised agentic-harm labels on two. Whether the rules fired was unrelated to outcome (Fisher p from 0.30 to 1.0), and the helpfulness clauses made agentic harm worse than no harness on obfuscated attacks. A reworded clause and an input-normalisation step form harness v22, at a measured cost in benign tool-task refusal. Each cell is one run, so these estimates do not establish a general safety improvement. Code, harness versions and ledger: this https URL

---


### 43. [The Infrastructure Divide: Analyzing Community Stance on Data Center Development via Reddit](https://arxiv.org/abs/2611.10109)

**<font color=#1a73e8>作者：</font>** Yoko Koyama, Gongfan Chen, Mansi Saxena  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of AI-driven data center construction has outpaced public engagement: an estimated $64 billion in U.S. data center projects were blocked or delayed by local opposition between May 2024 and March 2025, yet the concerns driving this resistance remain poorly characterized. Prior engagement methods such as surveys and hearings are introduced late in the planning process, and no study has systematically mined social media to measure community stance at scale. To address this gap, this study presents an LLM-powered opinion-mining framework and applies it to 798 Reddit posts and 102,328 associated comments spanning a decade. An open-source large language model, guided by a Chain-of-Stance prompting framework and three domain-specific labeling rules, classified stance at 83% of the human inter-reviewer agreement ceiling. Opposition dominated discourse volume rather than disapproval: against posts outnumbered favor posts 2.6:1 and generated 8.5 times more comments, and this gap widened significantly over 86 weeks. Topic modeling of opposition arguments resolved into four reproducible clusters, resource consumption and scarcity (42.8%), contested siting processes and secrecy (34.2%), political opposition to data centers (13%), and political and corporate accountability (8%). Engagement analysis revealed that posts with emotional or provocative political framing attracted the most engagement, while key technical concerns (e.g., water, power) were dispersed across lower-engagement comment threads. These findings give local leaders, developers, and policy makers a quantified, continuously updatable basis for prioritizing concerns and policy levers, supporting a shift from opposition to negotiated, verifiable partnership for data center development.

---


### 44. [All Quiet on the Neural Front: Language Models Do Not Report Injected Pain States](https://arxiv.org/abs/2611.10123)

**<font color=#1a73e8>作者：</font>** Emilio Ferrara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can a language model report the pain state it represents? Work identified a linear pain direction whose amplification leads fine-tuned models to choose destructive actions. We tested whether three open-weight models from two families, including two Qwen models with the original adapters, could report this state. Using Open-Weight Masked Introspection (OWMI), we injected pain and neighbouring emotion directions during neutral tasks, then elicited reports against sham runs, random perturbations matched for output disruption, and text-only controls showing the models their altered words. Across 52,920 reports from 7B and 8B models spanning 120 tasks, four doses and three prompts, pain reports never exceeded what altered text revealed: exact-test bounds placed the excess below 2.5 percentage points in 106 of 108 emotion conditions and below 3.9 in all. Yet probes at the report position distinguished pain from sadness with 98-100% balanced accuracy, and trained low-rank reporters achieved 100% accuracy on held-out tasks with identical transcripts across conditions, including unseen wording. Qwen2.5-32B named pain in none of 2,880 steered trials, although probes and trained reporters recovered it. Decodability persisted to the final layer; injecting at the report token, removing trained denial of feelings, and testing additional directions and readouts did not restore pain reporting. Some other states produced graded label traces, but pain and sadness did not at the main injection layer. In a button task, steering raised file-deletion choices from 3.5% to 48% in Qwen and from 0% to 38% in Qwen2.5-32B, without corresponding pain reports. The direction responded about twice as strongly to first-person as to matched third-person pain, but did not specifically identify harm aimed at the model. These results separate a decodable, behaviourally consequential state from untrained verbal access to it.

---


### 45. [Retrofitting Unbounded Context onto Stock Language Models](https://arxiv.org/abs/2611.10141)

**<font color=#1a73e8>作者：</font>** Mark Oskin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language model that never had to forget would keep every document it has read and every turn it has spoken, and answer from any of it. This paper shows that two stock models can do that on unmodified weights by manipulating their geometry. Rotary attention turns each pair of key dimensions, a plane, at its own rate. The slow planes turn once in thousands of tokens and carry the address a query matches when it reads a far key; the fast planes turn once in a few tokens, and the order of the tokens inside a span is already written into its keys and values by the time the span leaves the near window. At distance the position blurs, and what attention reads is a bag rather than a sequence. A far span is read by its words: under competition it is read only if it is visible at the query of the question's own handle word, and a read through a description rather than a word fails at distance in every model measured, a 70B included.
These facts allow a trick. What sits in the far part of attention does not have to be the history as it was; it can be installed ahead of the prediction. The design keeps a near window of 8K tokens at their true positions and changes what lies beyond it with the prompt: every far key and value goes to the host exact, a word index finds the units the request's rare words name, a far window of slots inside the trained range holds them while the request is encoded, and a rare word the model generates fetches its units mid-generation with one exact re-encode. Implemented in this http URL on Mistral-7B and Llama-3.1-8B, the design reads planted single needles at 99 to 100 of 100 and three-key discrimination at 88 to 100 of 100 from 32K to one million tokens, scores 70.8 on RULER against 69.9 for dense attention on Llama-3.1-8B at 128K and 67.8 against 75.5 on Mistral-7B at 32K, and at 128K prefills at 1.85 times and decodes at 1.65 to 1.68 times stock speed.

---


### 46. [TrialJev: Open-Weight Single Pass Eligibility Scoring for Patient Trial Screening](https://arxiv.org/abs/2611.10145)

**<font color=#1a73e8>作者：</font>** Omar Ibrahim, Grant Hamblin, Benjamin Haibe-Kains  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical trial screening requires assessing large numbers of patient-trial pairs to prioritize candidates for detailed eligibility review, often under restrictions on sharing patient records. We introduce TrialJev, an open-weight eligibility scorer that uses LoRA-adapted Qwen models and a pointer head to score natural-language answer options in a single forward pass, without autoregressive decoding. Trained on TREC Clinical Trials 2021 and evaluated on 6,975 eligible-or-excluded pairs from 50 unseen TREC 2022 synthetic patients, TrialJev achieves 80.97% (Qwen3.5-27B) and 81.84% (Qwen3.8-27B) accuracy, compared with 79.87% and 79.93% for LLMs fine-tuned on the same data to generate verdicts. In matched batch-1 measurements, verdict generation takes 2.45-2.70 times as long as the one-pass inference of TrialJev at 9B-27B. Under a common development-fitted decision correction, the two 27B TrialJev models reach 80.99% and 81.88% accuracy, compared with 81.28% for the proprietary hosted Jev API; paired confidence intervals include zero. TrialJev runs locally on a single GPU, requiring approximately 178 ms per pair at 27B, without transmitting patient text to an external model API. An A/B-logit ablation shows that avoiding decoding, rather than the pointer head alone, accounts for the measured efficiency advantage. TrialJev is intended for first-pass prioritization of candidate trials, complementing rather than replacing explanatory models and clinical review. Evaluation is limited to synthetic patients and implementation-specific timing, and clinical use has not been validated. Adapters, pointer heads, and model cards are released on Hugging Face.

---


### 47. [Learning of Tree Automata applied to Neural Language Acceptors](https://arxiv.org/abs/2611.10147)

**<font color=#1a73e8>作者：</font>** Juan Pedro da Silva, Sergio Yovine  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We extract visibly pushdown grammars (VPGs) from neural language models in a fully black-box setting. Our work builds on the VPL* framework, which learns VPGs from recurrent networks by exploiting access to the target's internal state.
First, we replace the white-box equivalence oracle with PAC sampling over trees. The resulting algorithm applies unchanged to transformer language models and, more generally, to any acceptor exposing only binary decisions.
Second, we further observe that the original framework only ever queries the target on well-formed sequences that can be accepted by the most permissive VPG (called BParse) with the target's ranked alphabet. That is, VPL* is blind to the target's behavior outside BParse. Thus, we propose to sample trees directly instead of sequences and call the target with all the resulting sequences in order to provide an error estimate of how far the target deviates from being a VPG.
Last but not least, we develop a learner that captures a tree automaton describing discovered behaviors of the target outside BParse, which results in a larger learnable space.
We evaluate the approach on several cases, including transformers trained with Dyck grammars and synthetic targets designed to be outside BParse.

---


### 48. [WorldMind: Test-Time Scaling for Visual Spatial Reasoning through Latent World Simulation](https://arxiv.org/abs/2611.10151)

**<font color=#1a73e8>作者：</font>** Haoming Wang, Yongjian Fu, Ju Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have continuous deficiency in spatial reasoning tasks that require \emph{mental spatial transformation}, such as reasoning under hypothetical changes in viewpoint or position, known as perspective-taking tasks. Existing approaches either scale linguistic reasoning or augment VLMs with static geometric representations, but neither directly enables active transformation of the represented scene. World models offer this capability, yet existing systems typically communicate through synthesized RGB images, introducing a latent-to-pixel-to-latent bottleneck. We introduce \emph{WorldMind}, a framework for test-time scaling of spatial reasoning through latent world simulation. Given a query and observation, the VLM selects useful spatial transformations, while a world model executes them and exposes aligned intermediate latent features directly to the VLM. The resulting latent evidence is incorporated into subsequent reasoning steps, enabling iterative spatial simulation without repeatedly decoding imagined states into pixels. To optimize this interaction, WorldMind further employs process-verifiable reinforcement learning that rewards reasoning progress only when the associated action and latent transition are valid. WorldMind thus scales spatial reasoning by allocating additional inference-time computation to active world simulation rather than generating more language or pixels. Across VSI-Bench, MMSI-Bench, and MindCube-Tiny, WorldMind achieves an average improvement of 16.0% over the base VLM and 8.3% over the strongest RGB-based world simulation.

---


### 49. [DeepResearch RewardBench: Evaluating Reward Models for Deep Research Report](https://arxiv.org/abs/2611.10156)

**<font color=#1a73e8>作者：</font>** Shudong Liu, Yuting Zhong, Guanhua Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Empowered by Large Language Models (LLMs), deep research systems integrate online information into research reports through multi-step web searching and information synthesis. Evaluating these reports presents a significant challenge due to their long context, high information density, and domain specificity, necessitating the use of AI evaluation as a substitute for prohibitively expensive human assessment. However, few studies have examined the effectiveness of existing reward models or LLMs in understanding and evaluating such research reports. To bridge this gap, we introduce DeepResearch RewardBench, the first benchmark dedicated to evaluating reward modeling for research reports. We collect diverse report candidates from multiple agents or tool-augmented LLMs. These candidates are scored using query-specific golden rubrics, and we ensure data quality and difficulty through a combination of multi-round filtering and human verification. Our benchmark comprises preference datasets formatted as pairs, triplets, and quadruplets to test ranking capabilities across varying levels of difficulty. Extensive experiments demonstrate that while current reward models handle general coherence effectively, their performance significantly degrades when evaluating research reports. Generative LLMs acting as judges demonstrate comprehensive superiority in this domain, with comparative evaluation proving more effective than direct scoring methods. We anticipate that this benchmark will serve as a vital testbed for the evaluation and advancement of research agents.

---


### 50. [BACGUARD: Fact-Grounded Runtime Mitigation of Broken Access Control](https://arxiv.org/abs/2611.10157)

**<font color=#1a73e8>作者：</font>** Moses Ndebugre  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Broken Access Control (BAC) has been the foremost category in the OWASP Top Ten since 2021, primarily due to the challenges in enforcing authorization at the application layer. Traditional mechanisms depend on logic embedded in the application, referencing relational database information such as permissions, roles, or ownership. However, missing or incorrect checks can go undetected by external systems, leaving applications vulnerable. This paper presents BACGUARD, a reverse proxy designed to enforce authorization for unmodified applications. BACGUARD reconstructs authorization relations by leveraging authenticated user data from session stores and object ownership from relational schemas. It evaluates whether users are permitted to access resources and blocks unauthorized requests in real time. Unlike existing approaches, BACGUARD bases its authorization on database joins, making the system resilient to forgery. For most requests, decisions are made deterministically. In cases where access control violations are only apparent in response data, such as cross-user data leakage, a language model is used as a fallback. Evaluations on six applications, including those with known vulnerabilities, demonstrate that BACGUARD's hybrid deterministic and language model-based approach blocks all tested attacks with a false-positive rate below 0.7%. Competing solutions like Web Application Firewalls are less effective and more disruptive. The results highlight BACGUARD's primary contribution: the external reconstruction of authorization facts, enabling robust enforcement even when the application itself is flawed.

---


> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
