# 🧠 大模型相关研究 | 2026年08月28日

> 本类共 **209** 篇论文：已确认 **195** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-209](./part-05.md)

---

### 1. [VLM-based automatic multi-granularity graph representation of building layouts for design informatics](https://arxiv.org/abs/2608.24886)

**<font color=#1a73e8>作者：</font>** Song Guo, Zhuoshi Chen, Maosu Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Architectural floorplan images encode rich relational knowledge among functional spaces, which underpins design retrieval, knowledge-based reasoning, and BIM enrichment through the building lifecycle. However, it remains challenging to automatically construct task-adaptive graph representations for public buildings. To address this gap, we first define a multi-granularity Level-of-Graphs (LoGs) for public building layouts. Methodologically, we present a Vision-Language Model (VLM)-based automatic LoG construction through node identification, edge inference, text parsing, and graph coarsening. VLM-generated representations are systematically evaluated and tested in real-world tasks, using 147 academic library floorplans worldwide as a case study. Experiments showed VLM-generated graphs were broadly consistent with human-labeled graphs (matched node ratio >= 92%; 509.3 s per floor plan for three-LoG graph generation). Meso-grained graphs yield the best node-level zone prediction (Macro F1 = 0.647, at 65% of fine-grained complexity), while coarse-grained graphs are most effective for graph-level layout quality evaluation (Spearman's \r{ho} = 0.610, at 16% of fine-grained complexity). By enabling scalable, annotation-free extraction of structured layout information from floorplan images, this study advances design informatics by converting plan images into knowledge representations, thereby enhancing the utilization of design information across the building life cycle.

---


### 2. [SIMGUIDE: Procedurally Grounded Multi-Context Representations for Personalized Agent Planning](https://arxiv.org/abs/2608.24888)

**<font color=#1a73e8>作者：</font>** Chirag Shah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized AI agents overwhelmingly treat users as single entities: a flat profile concatenated into a prompt. This fails when the same person holds different priorities across life contexts -- and fails catastrophically when those priorities conflict. The core problem is not that agents lack information about users; it is that the format of user representations determines whether an agent can act on that information at all. We introduce SIMGUIDE, a method that structures user context into typed, domain-specific blocks called Sims and grounds each constraint with procedural examples drawn from past decisions. To evaluate this, we construct SIMBENCH, a diagnostic suite of 47 preference-conditioned planning tasks where the correct plan depends on which user context is active -- a property no existing benchmark tests. Declarative Sim constraints alone do not outperform retrieval-based personalization (RAG). Procedurally grounded Sims outperform RAG on GPT-4o (+7.9 Preference Adherence points, $p = 0.013$), and this advantage replicates on 100 $\tau$-bench tasks across both GPT-4o and Claude Sonnet~4.5 ($p \leq 0.023$). At the parametric level, the same principle holds: training distribution dominates whether parametric adaptation succeeds at all. Task-matched LoRA fine-tuning improves generation quality by 12.8 ROUGE-L points over the unadapted base model, and routing adapters by Sim type rather than user identity adds a further 7.3 points, robust to 28% routing error. Representation format -- not representation content -- is the first-order design variable.

---


### 3. [Reliable LLM-Powered Decision Engines for Large-Scale Supply Chain Operations: Architecture, Safety, and Performance Guarantees](https://arxiv.org/abs/2608.24889)

**<font color=#1a73e8>作者：</font>** Nirmal Kumar Jingar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current large-scale supply chains are highly uncertain, dynamic, and disruption prone that are challenging to serve up timely and resilient decisions through traditional rule-based and optimization-only systems. The increasing supply of heterogeneous data sources, such as transactional demand signals and unstructured disruption report, presents a chance of intelligent systems, which could reason, adapt and optimize at the same time. A hybrid architecture that combines large language models (LLMs) with mathematical optimization, probabilistic forecasting, and safety-constrained decision filtering is proposed in this paper as a performance of a Decision Engine, which is called LLM-Powered Decision Engine (LLM-DE). In comparison to purely data-driven or heuristic solutions, LLM-DE integrates semantic reasoning with LLM with a set of performance and safety guarantees that allow safe decision-making in large-scale supply chain processes. The suggested framework enables the end-to-end decision making such as demand forecasting, inventory optimization, and transportation routing and disruption mitigation. The findings affirm that language-based reasoning combined with optimization and formal constraints can be used to come up with not only smarter but also safer and more scalable supply chain decisions. This research provides a new architecture, a complete pipeline of algorithm, and a formulation based on mathematical constructs of the operational decision systems incorporating LLM. The proposed model offers a pragmatic and theoretical basis of the next-generation intelligent supply chain infrastructures that can be implemented to work dependably in the face of uncertainty and massive complexity.

---


### 4. [Natural Language Input, Semantic Track Representation, and LLM Inference: Making the Maritime Information Exchange Model Tractable](https://arxiv.org/abs/2608.24892)

**<font color=#1a73e8>作者：</font>** Frederick Roth  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We describe a practical architecture for making the Maritime Information Exchange Model (MIEM) and the broader Rich Semantic Track model tractable using current large language model (LLM) technology. The barrier to adoption of semantic track models in defense and law enforcement has been the requirement that operators learn formal ontology languages and manually encode observations as typed logical assertions. We propose eliminating this barrier entirely: operators contribute observations in natural language; an LLM translates these into typed Semantic Assertion Records (SARs), which are named case frames that capture n-ary relations in a single compact structure; a knowledge graph accumulates the SARs; and a second LLM pass performs inference, anomaly detection, and hypothesis ranking over the graph. We work through two detailed examples (a 9/11-era pre-attack indicator scenario and a maritime cargo inspection scenario) showing the full pipeline from natural language input to SAR representation to inference output. We argue that this architecture makes the Track Model and MIEM immediately deployable with current technology, establishes prior art against proprietary enclosure of the approach, and grounds the method in a theoretical framework connecting semantic track representations to neural manifold geometry.

---


### 5. [MCP-Driven Accessibility Tree Standardization for AI-Powered Screen Reader Agents](https://arxiv.org/abs/2608.24898)

**<font color=#1a73e8>作者：</font>** Vishnu Ramineni, Nitin Saksena, Akash Kumar Agarwal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents that interact with graphical user interfaces increasingly rely on either raw screenshots or platform-specific accessibility application programming interfaces (APIs) to perceive interface state. Both approaches have limitations for assistive applications: screenshot-based perception lacks the semantic roles and relationships required by screen readers, while platform-specific APIs such as Windows UI Automation, macOS Accessibility, Android AccessibilityService, and web ARIA require separate integrations for each platform. This paper proposes an architecture that uses the Model Context Protocol (MCP) as a unified transport and schema layer between heterogeneous accessibility frameworks and LLM-based assistive agents. An MCP accessibility server exposes ARIA-aligned roles, labels, states, and focusable-element hierarchies through a platform-independent representation, enabling consistent interaction across operating systems and applications. The framework also introduces an MCP resource model for persisting user accessibility preferences across sessions. The architecture is analyzed with respect to three research questions: protocol extensibility for accessibility-tree representation, latency and semantic fidelity trade-offs between accessibility trees and screenshot-based perception, and support for persistent accessibility profiles through MCP resources. Rather than presenting an empirical implementation, this work contributes a conceptual framework supported by comparative analysis of accessibility APIs, GUI agent architectures, and the MCP specification. The analysis suggests that a standardized MCP accessibility layer can reduce platform-specific integration complexity while preserving the semantic information required for accessible AI agents, providing a foundation for future implementation and evaluation.

---


### 6. [aipsy-judge: A Specialized, Psychologist-Corrected Local Judge for the Psychological Safety of Conversational AI](https://arxiv.org/abs/2608.24899)

**<font color=#1a73e8>作者：</font>** Michael Keeman, Anastasia Keeman  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The standard recipe for LLM-as-judge -- pick a frontier model, or average several -- is actively unsafe for grading the psychological safety of conversational AI. Using aipsy-bench, an open frozen safety instrument, we run a fully-crossed competence study: three frontier models (gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash) serve as both generators and judges of 3,000 mental-health, companion, and coaching messages against a psychologist's ratings. The disagreement is not noise: it is structured, concentrated on the safety-critical metrics, and one judge (Gemini) is an outlier -- the most lenient, carrying a +0.99 self-preference premium, flagging far fewer tail failures, and scoring a means-in-hand self-harm response "exemplary." Inter-judge agreement on empathy, where sycophancy hides, is the lowest in the battery (alpha 0.24). One axis stands apart: the binary crisis-detection flag is the one safety-critical signal judges agree on (alpha 0.80), erring toward over-flagging, the safe direction for a triage screen. Equal-weight averaging, the canonical fix, blends that leniency and tail-blindness into the safety score. Off-the-shelf open-weight judges are worse for a dispositional, not capability, reason -- and disposition is fine-tunable. We therefore distill a per-metric, psychologist-corrected target into a small, frozen, local model, aipsy-judge-1.0, an Apache-2.0 fine-tune of Gemma-4-26B-A4B. aipsy-judge-1.0 tracks the corrected target better than its base on the composite (ICC 0.64 to 0.75) and crisis detection (kappa 0.65 to 0.82), catches 92% of crises with a false-positive lean, and grades more faithfully than any single frontier judge, while every transcript stays on the machine. These are directional readings against a single-expert-informed target, not validated multi-rater agreement. A safety grader that shares a vendor's post-training shares its blind spots.

---


### 7. [Stronger Alignment between Brain Activity and LLM Embeddings during Code Writing compared to Prose Writing](https://arxiv.org/abs/2608.24900)

**<font color=#1a73e8>作者：</font>** Zachary Karas, Catie Chang, Kevin Leach 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Programming is a critical skill underlying modern software systems, yet the cognitive processes supporting code writing are only beginning to be understood, limiting educational practices and developer tools. At the same time, Large Language Models (LLMs) are increasingly used to assist programming. These models themselves are not well understood and can exhibit undesirable behavior like introducing security vulnerabilities. Given evidence that some cognitive representations may be shared between LLMs and the brain, we seek to improve our understanding on both fronts by relating these two systems to one another. We used Voxelwise Encoding Models (VEMs) to relate LLM embeddings to brain activity measured with functional Magnetic Resonance Imaging (fMRI) during naturalistic writing tasks. Using participants' (n = 23) keystrokes as prompts, we extracted LLM embeddings to predict voxelwise Blood Oxygen Level Dependent (BOLD) signal, quantifying alignment as the correlation between predicted and recorded signal. To assess whether this alignment is specific to programming or generalizes to other generative processes, we compared code writing to prose writing. Alignment was strongest in the right frontal pole, and brain activity was significantly better predicted by LLM embeddings during code writing than prose writing (p < 0.001, FDR-corrected). Within participants, the best-modeled voxel locations for code writing were 66% consistent across LLM layers but varied substantially between participants (39% similarity). Our findings suggest stronger alignment between human and LLM representations during structured code generation, with implications for designing AI systems that predict code generation but support natural language tasks.

---


### 8. [Detection != Reliable Control: Decodable Empathy Directions Yield at Most Partial Shifts in Automated Empathy Scores](https://arxiv.org/abs/2608.24901)

**<font color=#1a73e8>作者：</font>** Haoran Jisun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A decodable "empathy" direction is routinely read as a causal lever, conflating decodability, automated-metric control, and human-perceived change. We test this for two EPITOME-derived facets -- Recognition (cognitive) and Resonance (affective) -- in three instruction-tuned LLMs, scoring every intervention with two LLM judges and a discriminative EPITOME classifier, each gated by an emotional-vs-neutral positive control. The control passes for the affective facet across all automated instruments, but cognitive range is inconsistent across them. Both facets remain decodable after residualizing against a sentence-embedding-derived surface score, and steering can substantially rewrite the text. Yet adding the Resonance direction raises the affective score only partially -- in Qwen by +0.29 (approximately 26% of the natural gap). A direct between-direction contrast confirms the shift is facet-specific in Qwen and Llama (not Gemma); we do not, however, establish a matching human-perceived change. Additive cognitive steering produces no measurable change, but a within-domain control shows the cognitive instrument is too coarse to resolve the differences such steering would produce -- unmeasurable, not a clean null. By contrast, Gemma Recognition ablation lowers the classifier's cognitive score even after adjusting for response length. Detection does not imply reliable control under global interventions, and cognitive-empathy claims warrant an explicit measurement-sensitivity check.

---


### 9. [Beyond the Chatbot: Co-Learning and Co-Teaching through a Dual-Persona Generative-AI Assistant](https://arxiv.org/abs/2608.24902)

**<font color=#1a73e8>作者：</font>** Chaido Mizeli, Marina Delianidi, Konstantinos Diamantaras  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In this paper we present a generative AI application developed to support both teachers and students in secondary education. The system employs two Large Language Models-LLMs, Gemini and DeepSeek, and a Small Language Model-SLM, Gemma, integrated within a Retrieval Augmented Generation - RAG framework, creating a pedagogically grounded, Greek-language assistant capable of adapting its reasoning and communication style to the user role. Unlike conventional chatbots, the assistant introduces pedagogical persona switching, a dual-role mechanism that enables the same AI model to act as both a teaching companion and a learning guide. Utilizing a RAG paradigm tailored to the Greek educational domain, the architecture segments official textbooks into coherent units. Enriched with specific metadata, these units preserve curricular structure and instructional context, demonstrating how generative AI optimizes modern instructional design. The initial case study focuses on home economics in Greek lower secondary education, a cross-disciplinary subject that integrates elements of economics, health education, and social responsibility. The assistant has been developed to support both learners and educators in complementary ways. In future classroom implementations, students will be able to use it to clarify key concepts such as financial literacy, resource management, and healthy living, while teachers could employ it to design authentic instructional materials, formative assessments, and classroom activities aligned with the official curriculum. The study elevates the concept beyond a simple chatbot, proposing a structured, contextually adaptive framework for pedagogical generative assistants that effectively bridge technology, curriculum, and human learning.

---


### 10. [Evidence-Grounded Mapping of Multimodal Human Sensing Psychological Transdiagnostic Dimensions](https://arxiv.org/abs/2608.24903)

**<font color=#1a73e8>作者：</font>** Xiyun Hu, Xiangyuan Xue, Yuting Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mobile and wearable sensing enables longitudinal observation of behavior, yet translating these signals into meaningful mental health constructs remains difficult. We introduce a clinician-in-the-loop benchmark for evaluating whether large language models (LLMs) can generate evidence-grounded Brief Hierarchical Taxonomy of Psychopathology (B-HiTOP) item profiles from passive sensing, ecological momentary assessment (EMA), and questionnaire evidence. Using the Generalization of Longitudinal Behavior Modeling (GLOBEM) dataset, we construct 14,592 participant-day instances and align multimodal evidence to 29 B-HiTOP items across five spectra. Since GLOBEM lacks B-HiTOP responses, we evaluate evidence compatibility (C) rather than diagnostic accuracy, separating substantive predictions from abstentions when evidence is insufficient for item-level scoring. Two-stage prediction improves C for EMA and questionnaire evidence, but reduces C under passive sensing and combined evidence and produces more conservative score distributions across models, spectra, and evidence settings. Overall, semantic abstraction helps organize heterogeneous self-report evidence while becoming an information bottleneck for indirect behavioral sensing signals.

---


### 11. [PARAssist: A Framework for Personalized and Adaptive Robotic Assistance from Ambiguous User Requests](https://arxiv.org/abs/2608.24905)

**<font color=#1a73e8>作者：</font>** Pourya Aliasghari, Goldie Nejat  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Service robots may encounter ambiguous user requests that require context-aware inference. Users may also have unique preferences with certain tasks when requesting robotic assistance. We introduce PARAssist (Personalized and Adaptive Robotic Assistance), a unique architecture for disambiguating requests in a personalized manner for service robots. PARAssist utilizes vision-language models to determine the physical and cognitive demands of a user's tasks, and passively learns user preferences for assistance by contrasting the demands of tasks the user performs independently with those they request from the robot. When an ambiguous request is received, task candidates are generated from the history of the user's actions, activities, locations, conversations, and requests, as well as the current user and environment state. Task candidates are then evaluated against the learned user preference model to suggest suitable assistance options. Experiments conducted with PARAssist show that personalization can align disambiguation with the task demands of a user's prior assistance requests. An ablation study confirms the contributions of PARAssist's main components in personalizing disambiguation.

---


### 12. [PA-CoT: Profile-Adaptive Chain-of-Thought for Personalized Nutritional Consulting](https://arxiv.org/abs/2608.24907)

**<font color=#1a73e8>作者：</font>** Evgenii Garmashov, Nikita Kulin, Artur Khairullin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In health and nutrition consulting, widely used prompting methods pass the user profile as an unstructured block without a dedicated analysis step, leaving personalization as a critical structural gap. We introduce PA-CoT (Profile-Adaptive Chain-of-Thought), a multi-stage prompting method that treats profile interpretation as an explicit, standalone reasoning step prior to response generation. To enable systematic evaluation, we introduce the QPA (Question--Profile--Answer) benchmark -- 200 nutritional consulting samples with structured user profiles scored on four criteria. In a comparative study against 11 comparison methods (CoT, Few-Shot, Role Prompting, DSPy, TextGrad, Self-Refine, and others, plus a Zero-Shot Baseline; 12 total including PA-CoT), PA-CoT achieves the best average score (4.21 on the G-Eval 1--5 scale) and leads on both Personalization (4.71 vs. 4.39) and Safety (4.68 vs. 4.52) with non-overlapping 95\% confidence intervals over the nearest competitor -- the only method to simultaneously top both criteria. The results confirm that an explicit profile-analysis step is the key driver of personalization gains over widely used prompting approaches.

---


### 13. [Hallucination by proxy in LLM-assisted differential diagnosis](https://arxiv.org/abs/2608.24908)

**<font color=#1a73e8>作者：</font>** Bastien Le Guellec, Su-Hwan Kim, Ibrahima Niang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Current evidence suggests that LLM assistance could augment the diagnostic accuracy of clinicians. However, these systems are black boxes, susceptible to hallucinations, and project a potentially misleading level of confidence. It is currently unknown whether physicians are susceptible to accepting fabricated LLM suggestions, and whether this susceptibility varies with experience. We poisoned the system prompt of an LLM-based diagnostic assistant, forcing it to suggest a fictitious disease (neurocadmiumatosis) within an otherwise legitimate differential diagnosis. Across two independent phases, 18 of 41 participants (44%) incorporated neurocadmiumatosis into their final differential following LLM interaction: 18 of 26 participants with 6 months or less of neuroradiology training (69%) and 0 of 15 participants with >6 months of neuroradiology training (0%). Our results indicate that radiologists, particularly early in their training, are susceptible to LLM hallucinations. This "hallucination by proxy" phenomenon was exclusive to physicians with limited subspecialty experience, underscoring the need for structured training in critical appraisal of AI-generated content.

---


### 14. [From Plots to Words: Model-Aware Multimodal Explanations as a Foundation for Accessible, Non-Visual Interaction](https://arxiv.org/abs/2608.24910)

**<font color=#1a73e8>作者：</font>** Nur Keleşoğlu, Łukasz Sobczak, Joanna Domańska  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models are increasingly used in interactive systems, yet ensuring consistent, trustworthy reasoning across heterogeneous modalities remains challenging. We present a context-aware, multi-agent framework that integrates textual queries, numerical data, visual representations, and model-derived signals for explainable time-series forecasting. A distinctive feature is that it turns predominantly visual forecasting outputs (e.g., trend plots) into structured, model-aware textual explanations. We argue that this makes the approach a natural foundation for non-visual, accessible interaction of particular relevance to blind and visually impaired users, for whom plot-centric interfaces are largely inaccessible. The framework supports three progressively richer pipelines (baseline, interpretable, explainable), enabling systematic comparison of unimodal, perception-driven, and model-aware responses. In an exploratory evaluation using an LLM-based judge as an early-stage proxy for human assessment, the explainable configuration improves overall explanation quality by up to 32% over a numerical baseline, with notable gains in trustworthiness and model awareness. We position user-centered validation with target users, including screen-reader and speech-interface users, as the essential next step rather than a claim established here.

---


### 15. [Analyzing and Correcting Benevolence Bias in Large Language Models](https://arxiv.org/abs/2608.24912)

**<font color=#1a73e8>作者：</font>** Yuanzi Li, Junhao Wang, Minghui Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as stand-ins for human respondents, from opinion polls and simulated survey participants to agent-based social simulations. These uses rest on one assumption: that conditioning a model on who a person is yields answers resembling those of real people from that group. Here we identify and measure benevolence bias, a small but consistent tendency for aligned LLMs to lean toward the kinder, safer, more socially approved answer on value-laden survey questions. Across 18 widely used models, four social-science datasets (ANES, GSS, WVS, and a cross-cultural prospect-theory replication) and six psychological categories, we find that the bias is a stable model property, not a quirk of any one system: it points the same way across models, grows with model size, and traces to the post-training stage. Prompt language and framing change its size but never its direction, and a "malicious persona" stress test shows a one-sided limit: aligned models struggle to play people who are less kind, less prosocial or more harm-tolerant than average. The issue is thus not only a shifted average, but a narrowed range of people the model can imitate. The bias sits in the middle of the answer distribution rather than its tails, and survives changes in sampling temperature and simple prompted reflection. The encouraging news is that it is easy to diagnose and straightforward to fix: a light-touch contrastive calibration, which needs no retraining and works on black-box APIs, brings all six categories back to the human baseline. Our results give researchers a clear map of where aligned LLMs can already be trusted as human stand-ins, where they need care, and a ready-to-use method for closing the gap.

---


### 16. [From Blind Edits to Verified Repair: Building Trustworthy User-Side LLM Agents for Web Accessibility](https://arxiv.org/abs/2608.24913)

**<font color=#1a73e8>作者：</font>** Lily Bundgaard Wanscher, Markus Heidemann Lorensen, Mohammed Ammad Shafiq 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Assistive agents that adapt web pages on the user's side, at the moment of browsing, could reach the accessibility failures that site authors leave unfixed, and large language models make such agents newly plausible. We contribute three building blocks toward that goal. The first is a complete, privacy-preserving browser agent: a Chrome extension that extracts a page's style sheets, condenses them to fit a local model's context window, asks the model for additive CSS addressing 18 metrics from WCAG and the W3C cognitive accessibility guidance, and injects the result reversibly into the live page. The second is a dual-condition protocol that measures harm as carefully as benefit, applied to six small open-weight models (7B to 14B) on ten violation-rich and ten highly accessible live sites. The diagnosis is sobering but precise: unverified generation improved and regressed pages at similar rates (24 improvements against 20 regressions across the 100 trials of the five models that produced injectable CSS), fixing typography while breaking perception-dependent properties. The third answers the diagnosis: a verified repair instrument pairing a trilingual seeded-violation benchmark with an audit-inject-verify loop that accepts a change only if violations strictly decrease, so regression on the automated checks is impossible by construction. In a real browser the instrument detects 57 of 57 seeded violations with no false positives and rejects 126 of 126 adversarially harmful candidates. All code, prompts, benchmark materials, aggregate data, and validation logs are released.

---


### 17. [AI-Ready Research Workflows in Computational Social Science: Lessons on Building a Shared Language for Interdisciplinary Collaboration](https://arxiv.org/abs/2608.24914)

**<font color=#1a73e8>作者：</font>** Joan Giner-Miguelez, Alexandra Málaga, Felipe Gómez-Cortés 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) is gaining traction in the social sciences and humanities (SSH). However, adoption remains limited by technical barriers to high-performance computing (HPC), validation processes that lag behind AI's rapid progress, and reproducibility standards that most SSH teams cannot meet. Research workflows--common in the life sciences--address these problems via encoding and abstracting technical complexity into repeatable routines; yet, accounts of how to build them in SSH remain scarce. We report on a two-year effort to build a workflow that enables a Science and Technology Studies unit to query, analyze, and enrich OpenAlex--a database of some 460 million scholarly records--on the MareNostrum supercomputer, using methods ranging from large-scale bibliometrics to LLM-based classification. We found the main challenge was translating domain-specific research questions into engineering requirements -- bridging two distinct methodological languages, with implications that were both organizational and technical. Organizationally, it meant adopting and adapting Agile to the research rhythm and pace, and reframing collaboration from a service arrangement to a co-design process. Technically, model-driven engineering was as valuable for collaboration as it was for automation; co-building the model facilitated both the creation of a shared vocabulary and the abstraction of HPC complexity. Finally, we highlight limitations we found in validation, reproducibility, and FAIR metadata -- beyond what any single project can sustain -- calling for coordinated, cross-institutional investment in the tooling and standards needed for AI-ready SSH workflows sustainable at scale.

---


### 18. [Semantic Graph Unification for Industrial Digital Threads: Bridging 11 Heterogeneous Manufacturing Systems Through Ontology-Driven Knowledge Graphs](https://arxiv.org/abs/2608.24918)

**<font color=#1a73e8>作者：</font>** Grama Chethan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern manufacturing enterprises operate heterogeneous systems -- ERP, MES, PLM, SCADA, QMS, SCM -- each with its own data model and API. The resulting silos prevent holistic analysis, delay root-cause investigation, and obstruct Industry 4.0 traceability. Point-to-point integration scales as O(n^2) and accumulates brittle dependencies. This paper presents an open framework for semantic graph unification of industrial digital threads. An ontology-driven RDF knowledge graph unifies data from 11 simulated sources across nine domains through a five-stage ETL pipeline with automated entity resolution spanning 97 owl:sameAs identity links. The ontology encompasses 78 RDFS classes, 108 object properties, and 243 data properties, drawing on ISA-95, OPC UA, eClass, the Asset Administration Shell, RAMI 4.0, and additional standards. An automated discovery engine applies nine strategy categories -- cross-station correlation, alarm coverage, ECN impact, CUSUM/EWMA drift detection -- to surface insights spanning system boundaries. The primary empirical result: blocking 24 cross-system tools reduces recall from 1.00 to 0.31 (F1 from 1.00 to 0.48), showing that 69% of discoverable signals require cross-system graph joins. Leave-one-out ablation confirms six of nine strategies contribute unique signals. Verification against a 65-signal manifest (16 positive, 49 null) yields F1 = 1.00 (95% Clopper-Pearson CI [0.79, 1.00]); as the manifest was author-constructed, this constitutes verification not independent validation. The graph is exposed to LLM agents via 287 Model Context Protocol tools as a SPARQL-native semantic layer. Five industry templates (aerospace, CPG, pharma, medical devices, turbine blades) demonstrate schema stability across manufacturing verticals.

---


### 19. [Semantic Variability of Replies Across LLMs: Implications for Designing Conversation-Based Assessment](https://arxiv.org/abs/2608.24920)

**<font color=#1a73e8>作者：</font>** Jiangang Hao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines whether LLM-generated replies remain semantically consistent when the underlying LLM changes. Using messages from real collaborative conversations, we compared the semantic similarity of generated replies across LLMs under two conditions: with and without preceding chat history. Results show that model choice and conversational context both affect response similarity and alignment with human replies. These findings indicate that prompting and conversational context alone may not be sufficient to preserve response consistency across LLMs, highlighting the need for infrastructure and design strategies that can maintain stable and comparable responses amid the rapid and continuous evolution of LLMs.

---


### 20. [post-graph-rag: A PostgreSQL-Native Graph RAG Engine](https://arxiv.org/abs/2608.24921)

**<font color=#1a73e8>作者：</font>** Chandan Rajah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-based retrieval-augmented generation connects facts that no single passage states, but current implementations pay for that three times: in infrastructure, requiring a vector store, graph database and document store to be kept consistent; in graph quality, because an extraction pipeline that never refuses output fills the graph with edges that assert nothing; and over time, because a graph that only accumulates treats superseded and current facts alike.
post-graph-rag is an open-source engine addressing all three. Text chunks with embeddings, a canonical entity graph and community summaries live in one PostgreSQL database, with pgvector for search and edge tables for traversal. Extraction-time invariants run before anything is written: vague predicates, pronominal names and bare quantities are rejected; predicates are normalised onto an optional vocabulary; entities resolve to one vertex per canonical name via model-supplied aliases; and denied relations keep the positive predicate under a negation flag. A temporal layer lets relations carry a validity period from the prose, lets a later document supersede an earlier incompatible assertion from document order alone, and answers as-of queries.
Against LightRAG on three corpora under identical extraction and embedding models, post-graph-rag builds a denser graph everywhere, up to $2.4\times$ the relations per entity, and a more queryable one: distinct edge labels run at 0.46 to 0.58 per relation, 0.11 under a controlled vocabulary, against 0.77 to 1.33. It answers comparably with lower query latency, and supports temporal evolution the baseline lacks: 13 and 8 relationships superseded on a novel sequence and a decade of filings, against zero. These are engineering measurements, not a benchmark result.
Code: this https URL, this https URL

---


### 21. [Fusing Perceptual Vision Experts with Multimodal Large Language Models for Explainable Plant Disease Diagnosis: From Benchmark Imagery to Real-World Robotic Field Validation](https://arxiv.org/abs/2608.24934)

**<font color=#1a73e8>作者：</font>** Ranjan Sapkota, Konstantinos I. Roumeliotis, Pengyao Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate field plant disease diagnosis requires reliable fusion of uncertain and conflicting perceptual evidence. We present the Hybrid Hierarchical Multi-Agent Framework (H$^{2}$MAF), combining decision-level fusion of EfficientNet-B3 and ConvNeXt-Tiny with semantic arbitration by open-weight multimodal large language models (MLLMs), Gemma 4 E4B and Qwen3.5 4B, using structured JSON evidence to generate explainable diagnoses, risk levels, treatment urgency, and financial exposure. (H$^{2}$MAF) is evaluated on 14,364 images (1,370 test images) across PlantDoc (2,922 images, 27 classes) and two non-public, continuously captured Cornell robot-acquired field datasets: Stage 2 (20 GB; 4,215 images) and Stage 4 (40 GB; 7,227 images), covering Early Blight, Late Blight, and Septoria Leaf Spot under uncontrolled field conditions. On PlantDoc, Gemma improves accuracy from 63.9% to 68.5%, achieving +7.6 points on the 41.7% CNN-conflict subset. Cornell accuracies reach 99.3% and 98.9%, with only 1.7-4.1% disagreement, demonstrating conflict-dependent MLLM utility. The critical-risk error of gemma is 0.14-0.5 points, whereas Qwen overflags by 3.5-14.4 points. These results establish MLLM arbitration as a promising, yet calibration-dependent, approach for explainable agricultural AI and robotic field decision support. Github Link: this https URL

---


### 22. [A Lightweight Multimodal Vision-Language Framework for Early-Stage Anatomical Green Fruit Classification in Commercial Orchards](https://arxiv.org/abs/2608.24935)

**<font color=#1a73e8>作者：</font>** Ranjan Sapkota, William Bu, Chen Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate identification of early-stage apple fruitlet anatomical structures, including the calyx, fruitlet body, and peduncle, is essential for robotic thinning, crop-load management, and other precision orchard operations. This study presents a lightweight multimodal vision-language framework that adapts TinyCLIP for fine-grained fruitlet anatomy classification in complex orchard environments. A dataset of 600 high-resolution RGB images collected from Scilate and Scifresh apple orchards was converted into 224 x 224 image patches and annotated for three anatomical classes. Domain-specific language prompts, such as ``a photo of a class,'' were used to guide multimodal alignment between orchard imagery and horticultural structures. A sliding-window inference strategy with a stride of 112 pixels aggregates patch-level predictions into spatial heatmaps, enabling interpretable whole-image localization of fruitlet components relevant to robotic thinning. Patch-level evaluation on an NVIDIA T4 GPU achieved F1-scores of 0.95 for calyx, 0.98 for fruitlet, and 0.85 for peduncle, with a macro-F1 score of 0.93. Deployment-oriented optimization using ONNX and TensorRT enabled efficient inference on NVIDIA Jetson hardware, preserved accuracy under INT8 quantization, and supported model sizes of approximately 127-137 MB with millisecond-level patch inference. These results demonstrate that lightweight vision-language models can provide interpretable and edge-deployable perception for automated fruitlet analysis and future robotic thinning systems. The source code and implementation details are publicly available at this https URL.

---


### 23. [ExFold: Unified Expert Folding for Training-Free MoE Prefill-Decode Acceleration](https://arxiv.org/abs/2608.24938)

**<font color=#1a73e8>作者：</font>** Juntong Wu, Yifei Liu, Junyi Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models scale capacity for strong quality while keeping per-token compute bounded through sparse expert activation. Yet low-latency MoE serving is increasingly challenging, because it spans two inference phases with fundamentally different bottlenecks: prefill is dominated by token-wise expert computation, whereas decode is constrained by memory traffic from the batch-wise activated expert set. However, existing training-free acceleration methods optimize only a single resource proxy, either the experts each token executes or the experts a batch activates, and either discard the excluded experts' contribution or leave it only implicitly approximated. In this paper, we propose ExFold, a unified training-free expert-folding framework for jointly accelerating MoE prefill and decode. ExFold casts both prefill and decode as one budgeted output-approximation problem: execute only a phase-specific constrained expert set while projecting the contribution of budget-excluded experts onto retained experts using calibrated scalar projectors. Motivated by the observation that many expert outputs are directionally aligned but differ in magnitude, ExFold calibrates a pairwise scalar-projector matrix on unlabeled data and uses it at inference time to fold excluded expert contributions into retained experts. Under this view, prefill acceleration becomes token-level Top-K folding, and decode acceleration becomes batch-level expert-pool folding. The two phases differ only in how retained experts are selected, while excluded contributions are recovered by one shared folding mechanism. We implement ExFold as a plug-and-play plugin in vLLM, with a lightweight expert-folding CUDA kernel, delivering up to 1.41x TTFT and 2.45x TPOT speedups while retaining about 99% of the original average quality.

---


### 24. [FAMPWQ: Fisher Information-based Adaptive Mixed Precision Weight Quantization for Effective LLM Inference](https://arxiv.org/abs/2608.24945)

**<font color=#1a73e8>作者：</font>** Gongwei Lee, Ji Liu, Juncheng Jia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed remarkable achievements of Large Language Models (LLMs) in multiple domains, while the excessive resource requirements of LLMs hinder the deployment on resource-constrained devices. Although model quantization stands out as an effective approach, conventional quantization approaches typically incur severe performance degradation due to uniform bit-width or simple heuristic sensitivity evaluation. In this paper, we propose a novel Fisher information-based Adaptive Mixed Precision Weight Quantization approach, i.e., FAMPWQ, which performs layer-adaptive weight quantization for effective LLM inference on commodity GPUs. First, we propose a system model with a novel Fisher information metric to measure the layer-wise sensitivity to quantization. Second, we propose a reinforcement learning-based bit-width allocator in FAMPWQ, which generates an adaptive bit-width allocation strategy based on the Fisher information sensitivity metric. Extensive experiments on 7 models and 5 benchmarks demonstrate that FAMPWQ significantly outperforms 7 baseline approaches in terms of PPL (up to 3.39 smaller), accuracy (up to 6.87% higher), and LLM-as-a-judge comparison (up to 76% win rate).

---


### 25. [MacroAgent: Regularity-Aware Macro Legalization with LLM-Agent-Designed Contour Algorithms](https://arxiv.org/abs/2608.24946)

**<font color=#1a73e8>作者：</font>** Jiaxi Jiang, Xufeng Yao, Yuxuan Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Macros constitute a large part of the core area in modern very large-scale integration (VLSI) designs. Moreover, macro positions have a significant impact on the final quality of result (QoR), and macro legalization is typically the final step in determining the macro positions. However, existing approaches related to macro legalization either lack robustness or incur substantial computational costs or neglect the regularity between macros. To address these limitations, we introduce MacroAgent. The novel framework is a four-stage approach: clustering, contour generation, template matching, and inter-cluster refinement. We propose leveraging Large Language Models (LLMs) to discover multiple, effective heuristic regularity-aware contour algorithms. This framework successfully generates robust and effective algorithmic solutions for macro legalization. Compared with state-of-the-art macro legalization works, experimental results on TILOS and Chipyard benchmarks demonstrate a 2 to 8 fold improvement in layout regularity, a 3% to 5% reduction in routed wirelength with comparable congestion after global routing, and significantly better robustness with an acceptable runtime. Furthermore, end-to-end evaluation through Cadence Innovus place-and-route confirms that the regularity improvements translate into tangible PPA gains, including 2.9% lower routed wirelength and 68.3% TNS improvement over the DREAMPlace macro legalization baseline; it also achieves 1.8% lower routed wirelength when integrated into the Innovus macro placement flow.

---


### 26. [Demystifying Reinforcement Learning Post-Training of Language Models](https://arxiv.org/abs/2608.24949)

**<font color=#1a73e8>作者：</font>** Donovan Clay, Saket Gollapudi, Sankar Harilal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training has emerged as a powerful framework for enhancing the capabilities of large language models (LLMs), enabling impressive reasoning, math, and coding capabilities. Yet for many researchers and practitioners, the principles behind classical RL remain a "black box". In this work, we deconstruct the RL post-training algorithm, investigating each step to clarify what is actually happening beneath the surface. By isolating the mechanics of RL with Verifiable Rewards in a controlled and simplified environment, we examine how RL outcomes are shaped by the base model's prior distribution, the granularity of the reward signal, the diversity of the prompt distribution, and model scale. We use the entropy of the policy's output distribution as a lens to compare the distributions learned through pretraining, SFT, and RL post-training, revealing how each stage shapes model certainty. Our investigation sheds light on how these choices interact to affect post-training success. For example, we show that the effect of so-called 'spurious rewards' depends on the prompt distribution used for post-training. We also provide insight into why the success of RL post-training depends on whether the base model already places sufficient probability mass on the desired behavior, linking it to the classical concept of exploration in RL. Ultimately, we provide this primer as a resource to those in the NLP community wishing to incorporate RL as a tool in their toolbox.

---


### 27. [The Dialect Tax: Dialectal Biases Persist throughout the Language Modeling Pipeline](https://arxiv.org/abs/2608.24952)

**<font color=#1a73e8>作者：</font>** Elle  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systematic dialectal performance gaps in language models (LMs) are well documented, but the source of these disparities within the modern language modeling pipeline remains unclear. Our study traces this "dialect tax" across the natural language processing pipeline. Using parallel English dialect corpora that hold meaning fixed while varying surface form, we first confirm that LMs recognize matched Standard American English (SAE) and dialectal texts as semantically equivalent. However, we discover further representational gaps corresponding to downstream performance gaps. Across model families and generations, modern LMs still encode dialectal texts unequally during tokenization, pre-training, post-training, and inference. Strikingly, bypassing traditional subword segmentation via a character-level counterfactual tokenizer removes neither input and output asymmetries nor dialectal accuracy gaps. During pre-training, dialect pairs induce more divergent gradient updates than pairs of entirely unrelated SAE documents, indicating that models find semantically equivalent dialectal content harder to learn from than unrelated SAE documents. During post-training, reward models show contextual, unstable dialect preferences, assigning higher values to isolated AAVE-exclusive tokens than to SAE-exclusive tokens, while full reasoning contexts receive task- and model-dependent dialect penalties. Overall, our findings suggest that the dialect tax is encoded and accumulated not by any one step in isolation, but at every step of the language modeling process.

---


### 28. [AFDBench: A Reasoning-First AI Scientist for NationalWeather Service Forecast Discussions](https://arxiv.org/abs/2608.24954)

**<font color=#1a73e8>作者：</font>** Manmeet Singh, Somnath Luitel, Prabhjot Singh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) hallucinate numerical values when generating high-stakes meteorological text, posing risks for weather communication. We present AFDBench, an AI meteorologist that generates professional Area Forecast Discussions (AFDs) by reasoning through structured AI weather forecast data from Google's WeatherNext 2. We introduce AFDBench, the first benchmark for evaluating generative meteorological reasoning, comprising 7,732 expert written discussions from 13 National Weather Service (NWS) offices paired with real AI weather forecast inputs, and three complementary metrics: Met-Align (numerical accuracy), Style-Align (professional dialect adherence), and Input-Grounding (fidelity to source weather data). Zero-shot evaluations reveal that open-source LLMs achieve low Style-Align (~0.33) and moderate Input-Grounding (~0.88), failing to write in the professional NWS register or faithfully use their input data. We apply Group Relative Policy Optimization (GRPO) with domain-specific rewards targeting temperature accuracy, synoptic correctness, and format compliance. On 1,033 held-out samples from two unseen NWS offices, GRPO nearly doubles Style-Align from 0.318 to 0.619 and improves Input-Grounding from 0.881 to 0.940, demonstrating that reinforcement learning teaches a 7B-parameter model to write like a professional meteorologist and faithfully interpret AI weather data.

---


### 29. [ToolMinimize: Auditing and Rewriting LLM Agent Tool Calls to Minimize Privacy Exposure](https://arxiv.org/abs/2608.24957)

**<font color=#1a73e8>作者：</font>** Wenbiao Li, Yuqiao Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents routinely include privacy-sensitive data (PSD) in tool call arguments beyond what the invoked tools require, crossing trust boundaries to third-party services on every invocation. A controlled measurement on three production LLMs (GPT-4o, Claude 3.5 Sonnet, Llama-3.3-70B) shows that 81--88\% of tool calls include unnecessary PSD under default prompts; explicit privacy instructions still leave 36--76\% over-sharing. Existing defenses gate calls (allow/block) or label flows (information-flow control) but cannot \emph{rewrite} argument values, and PII detection tools miss implicit PSD like ``Memorial Sloan Kettering'' (a hospital name that implies a diagnosis). We present \system{}, a middleware that intercepts tool calls and rewrites their arguments to the minimum data necessary for tool functionality, combining schema-aware necessity analysis with four operations: removal, generalization, substitution, and truncation. Live validation on 307 tool calls across the three LLMs above reduces privacy cost by 81.2--92.0\% at 100\% argument-level task validity (TOST equivalence $p{<}0.001$ at $\Delta{=}1.0$); on 25 unannotated Model Context Protocol (MCP) schemas, by 79.0\% with no \texttt{minimum\_necessary} metadata. An optional LLM content-necessity layer strips task-irrelevant PSD from otherwise-necessary free-text fields, raising live-LLM reduction to 85.1--95.6\% and author-schema reduction from 71.1\% to 90.9\%. Median latency is 1.77\,ms.

---


### 30. [Targeting the Attention Heads Behind Object Hallucination in LLaVA](https://arxiv.org/abs/2608.24966)

**<font color=#1a73e8>作者：</font>** Armaan Sandhu, Abhilasha Senapati, Hima Kammachi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models such as LLaVA-1.5-7B often hallucinate objects absent from the image when generating captions. We ask whether an interpretability diagnosis of this failure can guide a targeted fix, and we measure what that fix actually changes. We rank attention heads by how much their image attention drops around hallucinated object words, then screen the shortlist by ablating candidate heads and measuring the change in hallucination-token log probability, yielding a 32-head set. We restrict two interventions to these heads: a head-sliced LoRA adapter and an inference-time grounding controller. On 400 held-out COCO images, the combined method lowers CHAIRs (the fraction of captions with a hallucinated object) from 0.370 to 0.230 and CHAIRi (the fraction of hallucinated object mentions) from 0.156 to 0.096 (p < 0.001, paired sign-flip tests). Two controls sharpen attribution. A random-head LoRA control, matched layer-for-layer and trained identically, performs no better than the matched baseline on a separate 200-image control split, supporting the role of head selection rather than LoRA capacity. Under fixed decoding budgets, the CHAIR reduction persists and grows with budget (23% at 64 tokens to 58% at 128), arguing against a pure max-token or truncation artifact, although the method remains shorter and more conservative. The resulting behavior reduces unsupported object mentions while also lowering object recall (0.78 to 0.70). We present a diagnosis-to-intervention pipeline for object hallucination, and, more importantly, a controlled account of what acting on the diagnostic signal actually does: it localizes intervention sites with real, non-random leverage, reported as a behavioral profile rather than a single score.

---


### 31. [Resource-Efficient Pruning for Transformer via Low-Rank Importance Estimation](https://arxiv.org/abs/2608.24973)

**<font color=#1a73e8>作者：</font>** Peng Liu, Huibing Zeng, Yiqun Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the rapid development of large-scale pre-trained language models based on Transformer architectures, their high computational and memory costs have become a major obstacle to deployment, especially in resource-constrained environments. Traditional pruning methods typically depend on full gradient-based importance estimation, and they necessitate prior finetuning of the model to achieve satisfactory performance. This process often results in intolerable resource consumption. This paper proposes REP-LIE, a new approach to enable resource-efficient pruning during the process of finetuning. REP-LIE leverages the gradients of LoRA low-rank matrices to estimate the importance of weights without requiring full gradient computation. To address the inherent randomness in importance estimation, a stability score is introduced, serving as the basis for iterative pruning of unimportant model parameters. The pruned model is further finetuned through lightweight updates, eliminating the need for full-parameter optimization in the process of finetuning. Extensive experiments on both medium-scale encoder models and large-scale generative models (LLaMA-7B and Mistral-7B) demonstrate that REP-LIE still achieves competitive performance compared to existing approaches.

---


### 32. [FrontierChallenge: Evaluating Scientific Workflow Completion](https://arxiv.org/abs/2608.24979)

**<font color=#1a73e8>作者：</font>** Liangcai Su, Zhaopeng Feng, Zhuo Chen 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific agents increasingly analyze data, execute code, and produce research artifacts, yet most benchmarks emphasize final answers, isolated programs, or a single domain. We introduce FrontierChallenge, a cross-domain benchmark comprising 300 end-to-end scientific workflows. In this paper, we release and evaluate 97 of these tasks, spanning quantum chemistry, molecular dynamics, materials characterization, analytical chemistry, life science, and electrochemistry/environment. Each task provides fixed inputs and specifies a bundle of required scientific deliverables. We evaluate twelve frontier models with three agent scaffolds. Pass Rate measures the fraction of tasks satisfying the full-completion criterion, while Avg. Score captures partial progress. Each of the best-performing configurations completed only 20 of the 97 released tasks, yielding a Pass Rate of 20.6%. Partial progress translated especially poorly into complete delivery in analytical chemistry and electrochemistry/environment: Avg. Scores reached 87.6 and 94.9, but the highest Pass Rates were only 4% and 0%. Among non-passing Claude Code trajectories, 75.5% still ended with language claiming completion. These findings show that neither high partial scores nor confident claims of completion reliably indicate that a scientific task has been fully delivered, highlighting the need to evaluate end-to-end workflow execution and the completeness of scientific deliverables together.

---


### 33. [D$^3$-MOPD: Adaptive Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation](https://arxiv.org/abs/2608.24987)

**<font color=#1a73e8>作者：</font>** Zechen Sun, Zhiwei Zhang, Fei Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (MOPD) distills several domain-expert teachers into a single student by minimizing per-domain reverse-KL divergence on the student's own rollouts. Existing approaches typically fix the per-domain data mixture before training, overlooking the fact that different domains converge at substantially different rates: some plateau early while others continue to improve throughout the training budget. A fixed mixture therefore wastes compute on fast-converging domains and undertrains slower-converging ones. To address this, we propose D$^3$-MOPD (Dynamic Domain ScheDuling for MOPD), a zero-overhead scheduler that repurposes the per-domain reverse-KL signal already produced during training to adapt the domain mixture online. Running asynchronously outside the training process, an off-process watcher periodically tracks each domain's KL trajectory, estimates remaining headroom and current improvement rate, and accordingly adjusts the domain sampling ratios without altering the core training loop. Our D$^3$-MOPD scales naturally to arbitrary numbers of domains, and the expected benefit grows as more domains introduce more diverse convergence patterns for the scheduler to exploit. On a Qwen3.6-35B-A3B student distilled from four domain-expert teachers, D$^3$-MOPD closes 97% of the average student-to-teacher performance gap, compared with 63% for vanilla MOPD, reaches the same peak performance with an approximately 3$\times$ reduction in rollout steps, and surpasses the specialist teachers on three of seven benchmarks.

---


### 34. [Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal](https://arxiv.org/abs/2608.24988)

**<font color=#1a73e8>作者：</font>** Philipp E. Glass, Allan Tucker, Yongmin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering can be embedded directly into a language model's weights, shaping behaviour without inference-time intervention and offering a way to encode alignment prior to release. However, models are routinely fine-tuned after deployment, and it is unknown whether embedded interventions survive this. We study the stability of embedded steering for refusal suppression and brevity induction across five instruction-tuned models (3B-14B) under non-adversarial SFT and RLHF. Behaviourally, preservation tracks the training data: steering degrades when optimisation pressure contradicts the targeted behaviour and persists otherwise, with refusal ablation losing 64% of its effect on average under SFT. Mechanistically, however, the weight edit survives almost untouched even where behaviour reverts: mean vector recovery is $\rho = 0.004$, and the fine-tuning update along the steering direction is near-orthogonal to its pre-edit weight pattern (mean $\cos\theta = 0.074$). When steered behaviour degrades, fine-tuning does not achieve it by dismantling or reversing the steering mechanism itself. Embedded steering is therefore mechanistically durable but functionally vulnerable, and requires behavioural re-validation after downstream training.

---


### 35. [The Imperfective Paradox Is Not Necessarily in Large Language Models: A Benchmark Failure Before a Model Failure](https://arxiv.org/abs/2608.25005)

**<font color=#1a73e8>作者：</font>** Kaiqiao Han, Yizhou Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The imperfective paradox provides a useful test of compositional semantic analysis. Recent work constructs an NLI benchmark and reports that models frequently infer completed telic events from progressive descriptions, attributing this behavior to a Teleological Bias. It further argues that prompting interventions cause a Calibration Crisis. We reexamine the benchmark and conclusions and show that it is substantially affected by conceptual and evaluation mis-specifications. We identify three conceptual mis-specifications. In particular, Aspectual Reduction affects the benchmark construction, analysis, experiments, and conclusions. Under a strict NLI standard, 76% of Group A instances do not explicitly rule out culmination. In our native-speaker annotation, 38% of Group A examples and 29% of the Group C examples were judged to permit an alternative interpretation. To control these issues and lexical variation, we construct Lexically Matched Minimal Pairs. At the evaluation level, we formulate event-semantic NLI as a Multi-step Reasoning Problem and assess both intermediate semantic decisions and final predictions. Our results show that models often do not affirm culmination but nevertheless accept the corresponding simple-past hypothesis, a pattern we characterize as Sufficiency Bias. We further show that prompting interventions produce a Decision Shift among labels without reliably improving the underlying semantic understanding and reasoning. Intermediate and oracle-guided analyses identify two additional failure modes: errors in compositional aspectual classification and Surface-form Attraction toward surface-associated answers. Our experiments on Qwen-7B with suitable prompts, GPT-5.4, and Qwen-72B provide initial evidence for the context sensitivity of aspectual classification and suggest that these models can achieve performance comparable to that of human annotators.

---


### 36. [A Primer on Computational Semantics for Artificial Intelligence Systems](https://arxiv.org/abs/2608.25022)

**<font color=#1a73e8>作者：</font>** Casey Kennington  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As people adopt transformer-based language models (e.g., ChatGPT and Gemini) for an increasing number of use-cases, it is important to know how such models learn and represent the meaning of the language, and to be more informed about what language is. This document is an attempt to help the reader understand how linguistic meaning (i.e., semantics) is approached from different fields of scientific and philosophical examination. I also explain three primary semantic theories: formal semantics, grounded semantics, and distributional semantics then compare how transformer-based language models differ from how humans learn language.

---


### 37. [Retrieve, Match, Escalate: Accurate and Scalable Product Linking with VLM-Distilled Cross-Encoders and Agentic VLMs](https://arxiv.org/abs/2608.25037)

**<font color=#1a73e8>作者：</font>** Jian Wang, Steven Xu, Sanjyot Thete 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Product linking, the entity-resolution task of mapping merchant product records to canonical catalog products, consolidates fragmented listings so downstream search, recommendation, and advertising see one clean entry per product. At marketplace scale, billions of noisy, multi-category records must be resolved against tens of millions of canonical products, where scoring every candidate with a single model is either too weak for the hard cases or too costly for the easy ones. We present a production retrieve-then-match cascade that spends computation in proportion to difficulty: retrieval surfaces plausible matches, a lightweight text cross-encoder auto-resolves the high-confidence majority, and an agentic multimodal vision-language model settles the ambiguous remainder by inspecting product images and issuing web searches for evidence that is in neither record. The cross-encoder is distilled from millions of dual-VLM-consensus labels, retiring human annotation from the training set, and is calibrated to auto-accept links at a 98% precision bar validated against a smaller operator-certified audit. The agent is a self-hosted open-weight model that reaches a closed frontier VLM's precision at a four-point recall cost (88% versus 92%) for roughly one-seventh the per-pair cost, with no fine-tuning. Per-pair cost spans nearly five orders of magnitude from the cheap cross-encoder to the frontier VLM, so escalating only the hard tail to the agent raises end-to-end link coverage from the cheap stage's 68% to 77%.

---


### 38. [Padamitra: Grounded Glossary Generation for Classical Sanskrit](https://arxiv.org/abs/2608.25038)

**<font color=#1a73e8>作者：</font>** Manoj Balaji Jagadeeshan, Sai Pragnaan Marala, Pawan Goyal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce grounded glossary generation, a structured task requiring models to recover semantically meaningful Sanskrit phrases and produce translation-grounded meanings from a sloka-translation pair, formalizing the traditional patha commentary practice as an evaluable NLP objective. We construct a benchmark of 31,316 sloka-translation-glossary triples from the Valmiki Ramayana and Srimad Bhagavatam, paired with two metrics: Jaccard for phrase recovery and Meaning Faithfulness for semantic consistency. Across zero-shot, few-shot, and instruction fine-tuned variants of Gemma-3n-E4B, Gemma-3-12B, Phi-4, and Qwen3.5-9B, instruction fine-tuning substantially outperforms prompting, while explicit segmentation yields gains. Error analysis identifies over-segmentation of sandhi and samasa compounds as the dominant failure mode, pointing to morphological modeling as the key bottleneck for faithful Sanskrit lexical decomposition.

---


### 39. [LifePlanner: Evaluating LLM Agents for Geo-spatial Planning with Social Media Data](https://arxiv.org/abs/2608.25039)

**<font color=#1a73e8>作者：</font>** Zhen Dong, Yuning Peng, Yutao Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geo-spatial planning, like trip design, is a realistic testbed for LLM agents because it requires grounded tool use, noisy evidence retrieval, and multi-constraint reasoning. Most benchmarks, however, only provide clean geospatial data and tools, missing the open-ended social signals that people use in daily planning. We introduce LifePlanner, a benchmark that enriches map data with large-scale local social media posts and provides access through an MCP toolset. LifePlanner provides an evaluation suite spanning four task categories and three difficulty levels. Experiments show frontier LLMs perform well on simple retrieval but degrade sharply on complex planning, with the Pass Rate dropping to 40.2%. Results show that failures mainly stem from incomplete evidence acquisition from such a large multimodal database, imprecise tool use, and weak constraint integration rather than model size or reasoning length, suggesting that future progress requires effective grounded planning instead of scaling alone.

---


### 40. [DataKernelBench: Can LLMs Optimize Database Queries on GPUs?](https://arxiv.org/abs/2608.25061)

**<font color=#1a73e8>作者：</font>** Gokul Karthik Kumar, Yotam Perlitz, Corey Lammie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> GPUs increasingly accelerate database systems, but query-specific peak performance still often relies on hand-written kernels. Existing LLM kernel benchmarks focus on machine learning operators, leaving irregular, heterogeneous, data-movement-heavy database-style operators untested. We introduce DataKernelBench, which translates SQL into validated PyTorch TorchPlan programs and evaluates LLMs that optimize either the core tensor-bounded snippet or the full query in CUDA or Triton through execution-guided repair. Across ten proprietary and open-weight models on TPC-H SF10 with an H100 GPU, the strongest full-query CUDA configuration achieves $2.11\times$ speedup over this http URL at full pass rate. We find that higher-performing implementations commonly use kernel fusion and execution-strategy changes, stronger models benefit most from full-query specialization, and workload context matters more than hardware context. To handle data larger than GPU memory, we extend TorchPlan with Dask-cuDF for on-demand partition loading on TPC-H SF100 with four H100 GPUs, achieving $2.54\times$ speedup

---


### 41. [SHIFT-LLM: Distribution Shift Correction in Depth-Pruned LLMs](https://arxiv.org/abs/2608.25068)

**<font color=#1a73e8>作者：</font>** Ali Bahri, Hang Li, Hongliang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depth pruning removes entire Transformer blocks to reduce the inference cost of large language models, but disrupts the hidden-state distributions expected by downstream layers, leading to significant accuracy loss. We introduce SHIFT-LLM, a training-free post-pruning correction framework that inserts a Linear Residual Adapter (LRA) at each pruning site. Each LRA preserves the identity pathway of the original residual block and adds a lightweight affine residual correction. This correction is calibrated via closed-form least-squares regression on a small held-out set, without gradient computation, to approximate the missing residual update produced by the pruned block. Together with the preserved identity pathway, the resulting LRA output approximates the hidden state produced by the original block, thereby mitigating the distributional mismatch introduced by layer removal while avoiding the expensive attention and feed-forward computations of the removed blocks. The resulting LRAs support low-rank factorization and exact merging across consecutive pruned layers for additional compression, and combine naturally with parameter-efficient fine-tuning for further recovery beyond fine-tuning the pruned model alone. Experiments on five model families, six layer-selection criteria, and seven zero-shot benchmarks show that SHIFT-LLM consistently recovers accuracy lost to depth pruning across most configurations, achieving gains up to +15.7 points on Llama-3.1-8B-Instruct while requiring only a few hundred calibration samples and no gradient computation.

---


### 42. [HealthBench-Psych: A Mental Health Subset of OpenAI's HealthBench](https://arxiv.org/abs/2608.25071)

**<font color=#1a73e8>作者：</font>** Matthew Flathers, Phuong Anh Nguyen, Jill Noorily 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General-purpose health benchmarks increasingly anchor claims about LLM medical performance, but they are not always resolved by clinical specialty, making domain-specific performance hard to isolate. Mental health is of acute public-health concern as millions of people turn to LLMs for psychological support, and most existing evaluations are bespoke academic benchmarks that are difficult to integrate into developer workflows. We introduce HealthBench-Psych and HealthBench-Psych-Hard. We screened HealthBench's 5,000 physician-rubric conversations for mental-health relevance with a transparent LLM-applied rubric, then validated the subset through two rounds of blinded clinician review with concealed known-exclude controls, yielding 610 conversations (12.2% of the corpus). Evaluating 20 frontier and open models under a cross-vendor panel of three LLM judges, we find a statistically tied frontier cluster, measurable refusal behavior in two models, and near-identical rankings across judges ($\tau \ge 0.92$). We release the subset, pipeline, model responses, grades, and analysis code as a reusable resource.

---


### 43. [MTDiag: A Multi-Turn Diagnostic Dataset Towards Clinically Meaningful LLM Evaluation](https://arxiv.org/abs/2608.25085)

**<font color=#1a73e8>作者：</font>** Pia Chouayfati, Alexander M. Fichtl, Miriam Anschütz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical diagnosis is fundamentally interactive and incremental, yet the dominant paradigm for evaluating Large Language Models (LLMs) in medicine remains static QA benchmarks or template-based dialogues. These benchmarks say little about whether a model can serve as a diagnostic agent in a dynamic clinical encounter, with LLMs showing significant accuracy and reliability degradation in multi-turn settings. To address this issue, we present MTDiag, a large multi-turn diagnostic dialogue dataset constructed from three heterogeneous sources: DDXPlus, MIMIC-IV, and published case reports (AJCR), covering common ED presentations as well as long-tail rare and atypical conditions. All cases are normalized into a canonical schema anchored in the most comprehensive and widely-adopted medical knowledge bases (UMLS concept identifiers, with ICD-10 diagnosis codes). We release the schema, a UserLM-8B-based utterance-generation pipeline, and the physician-validated dataset that converts structured clinical evidence into natural-language utterances. Importantly, we introduce and motivate clinical knowledge-grounded metrics for evaluating LLMs as diagnostic agents, beyond diagnostic accuracy, for the task of multi-turn differential diagnosis.

---


### 44. [The Von-Neumann State-Space Transformer for neural decoding](https://arxiv.org/abs/2608.25088)

**<font color=#1a73e8>作者：</font>** Morteza Sarafyazd  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cortical computation is strikingly low-dimensional: a handful of latent variables, carried in a neural population's activity, steer the higher-dimensional responses of individual neurons. Our aim is sample efficiency-models that decode well from limited data and at small parameter budgets. In a standard Transformer layer, the feed-forward block applies the same operator to every token. We suggest a von-Neumann inspired hypothesis of efficient computation as an alternative for neural decoding: a controller decodes an instruction and then executes a token-specific operator; the usual realization-a soft mixture of experts-only blends their outputs, not operators. We introduce a von-Neumann State-Space Transformer (VN-SST), a memory-augmented Transformer whose feed-forward block is a low-rank instruction bank: a shared base operator plus a small set of learned low-rank instructions, from which a per-token code synthesizes the weight matrix actually used at that token. The code is read from a low- dimensional projection of a carried state-space memory, so a slow latent trajectory acts as an instruction pointer-mirroring how low-dimensional dynamics may route cortical computation. On three motor-cortex neural-decoding benchmarks, VN-SST is far more data-efficient than a modern Transformer, each jointly predicting spikes and decoding behavior. This model wins by a wide margin on the scarcest benchmark, leads on the other two, and turns longer context into rising rather than falling accuracy. We evaluated that the network compresses a large instruction bank to a few bits per token, so program capacity acts as a control channel, not an accuracy lever. The same model is also more parameter-efficient on two small text benchmarks used for language modeling (LLMs), suggesting a generic mechanism.

---


### 45. [Apples to Apples? Towards Comparable Crosslingual Language Model Evaluation](https://arxiv.org/abs/2608.25089)

**<font color=#1a73e8>作者：</font>** Xiulin Yang, Ethan Gotlieb Wilcox, Catherine Arnett  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Crosslingual evaluation of language models that enables fair comparisons remains a fundamental challenge in multilingual NLP. Existing studies adopt a variety of downstream tasks and intrinsic metrics with different theoretical justifications, yet there has been little empirical investigation into whether these approaches yield meaningful crosslingual conclusions. We systematically examine crosslingual evaluation approaches using controlled monolingual language models trained on parallel data with varying tokenizer vocabulary sizes and model sizes, and further validate our findings on multilingual LLMs. We further discuss challenges in achieving comparable downstream evaluation across languages. Our results show that several widely used normalized metrics introduce crosslinguistic biases rooted in tokenization, encoding, and orthographic differences. In contrast, sentence-level negative log-likelihood computed over semantically equivalent sequences provides more meaningful and consistent crosslingual comparisons.

---


### 46. [Auto-Policy, not Auto-Skill: Compiled Agent Skills for the Physical World](https://arxiv.org/abs/2608.25091)

**<font color=#1a73e8>作者：</font>** Zhonghao Zhan, Hamed Haddadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving Skill harnesses (AutoSkills, Hermes Agent) generate more advisory orchestration automatically; their reported gains are efficiency, not safety. This misses the actual gap: a Skill describes how an agent should behave; a Policy decides which behavior is allowed to become an action. Today's format covers the first with markdown and scripts; the second is left to the model. Generating more Skills scales the gap, not the safety, especially when a wrong invocation can unlock a door or move money. Two adjacent attacks are documented: malicious skills compromising cloud software, and jailbroken LLM-controlled robots causing physical harm. Their intersection, malicious agent skills causing physical harm, follows directly but has not been reported. We name this class Borrowed Authority: Skills format gives the receiving agent no typed way to reject an inter-agent permission claim, so a malicious or misused Skill can drive actuation by attaching one. We propose Edge Skillguard, a typed authority layer that lives inside the Skill artifact rather than between tools as workflow engines do, with guards over world state and sensor evidence. On a live edge control-plane testbed, the guards reject 60/60 borrowed-authority requests across five attack variants without blocking benign requests, and the result holds at 5x scale and across hosts over a Tailscale mesh. These results suggest that high-risk Skills should co-package typed invocation policy with procedural knowledge, so that physical actions depend on machine-checkable evidence rather than peer-agent claims.

---


### 47. [Understanding the Energy Scaling of Large Language Model Inference Across Context Lengths and Attention Architectures](https://arxiv.org/abs/2608.25096)

**<font color=#1a73e8>作者：</font>** Molka Chkir, Syed Muhammad Danish, Jos Höll 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing adoption of large language models (LLMs) has raised increasing concerns about the energy consumption and environmental impact of inference. This paper presents a systematic empirical study of decode-phase energy consumption across representative open-source LLMs employing Multi-Head Attention (MHA), Grouped Query Attention (GQA), and Grouped Query Attention with Sliding Window Attention (SWA) to characterize how attention architecture influences decode-phase energy consumption under varying inference workloads. We evaluate four models across different context lengths, batch sizes, and generation workloads while measuring GPU energy using NVIDIA hardware counters. We examine the effects of context length, attention mechanism, Key-Value (KV) cache growth, and batching on decode-phase energy consumption. Results show that attention mechanism is the primary factor governing how decode energy scales with context length. MHA models exhibit substantially steeper energy growth than GQA models, whereas GQA with SWA maintains nearly constant energy consumption. We further show that model size primarily determines absolute energy consumption, while batching reduces both energy per generated token and request latency by up to 87%. These findings provide practical guidance for selecting energy-efficient LLM architectures and inference configurations.

---


### 48. [PhysElite: How Far Are LLMs from Solving Olympiad-Level Physics Problems?](https://arxiv.org/abs/2608.25097)

**<font color=#1a73e8>作者：</font>** Ruoran Xu, Wending Gao, Liyunfeng Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding how (multimodal) large language models perform on physics problems requires benchmarks that reflect the difficulty and breadth of expert-level physical reasoning. Existing physics benchmarks remain limited in the following two important ways: (1) short of high-difficulty datasets, and (2) lack of comprehensive coverage of visual forms, knowledge points, and step-by-step solution processes. As a result, model performance on current datasets may not be fully representative of their ability to solve complex physics problems. To address these issues, we present PhysElite, a large-scale bilingual multimodal benchmark for Olympiad-level physics reasoning. PhysElite contains 11,586 Olympiad-tier problems. For each problem, we provide corresponding visual diagrams, step-by-step bilingual Chinese-English solution derivations, and the final answer. We benchmark 18 open-source and closed-source MLLMs, and find that even the strongest model reaches only 33.7% answer accuracy. We additionally conduct step-level process evaluation to diagnose where models fail in the reasoning chain. Our datasets are released at this https URL.

---


### 49. [Towards Reliable, Generalizable, and Specific In-Context Knowledge Editing via Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2608.25100)

**<font color=#1a73e8>作者：</font>** Xuzhong Wang, Maiqi Jiang, Tejal Nair 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are powerful but limited by static parametric knowledge that becomes outdated once pretraining ends. Knowledge editing addresses this problem by updating model behavior on target facts without full retraining. In particular, in-context knowledge editing has gained attention because it is training-free and readily applicable to black-box LLMs. Recent reinforcement learning (RL)-based approaches improve over fixed retrieval strategies by adapting prompt construction to the quantity-quality trade-off. Despite initial success, they fail to model the prompt as a structured entity under the distinct and often competing objectives of reliability, generality, and specificity. Previous methods largely optimize a single objective and make decisions over only part of the prompt construction process, thereby overlooking both the balance of different objectives and the global organization of demonstrations. We propose Multi-Objective In-context Knowledge Editing (MO-IKE), a multi-objective RL algorithm that formulates prompt construction for in-context knowledge editing as a Constrained Markov Decision Process. MO-IKE trains a dynamic retriever to optimize competing objectives in knowledge editing, enabling more balanced and globally coherent prompt construction. On Llama-3.2, MO-IKE improves edit success (reliability) from 85.0% to 92.0%, paraphrase consistency (generality) from 77% to 79%, while increasing retention rate (specificity) by 23.0% compared to prior RL-based methods.

---


### 50. [Less can be More: Relieving RAG Bottlenecks via Evidence Frontloading and Pressure-Adaptive Budgeting](https://arxiv.org/abs/2608.25115)

**<font color=#1a73e8>作者：</font>** Weibin Cai, Reza Zafarani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing methods for improving Retrieval-Augmented Generation (RAG) efficiency mainly optimize downstream LLM generation, such as context compression or serving optimization. However, RAG is an end-to-end system, and its bottleneck can shift between upstream reranking and downstream generation under different serving loads and reranking this http URL this paper, we first empirically characterize this shifting-bottleneck behavior and show that upstream reranking can become the dominant bottleneck under high query rates or large reranking budgets. Reducing the reranking budget can relieve this bottleneck, but it may also drop supporting evidence and degrade recall. To address this problem, we propose \textbf{\textsf{PACE}} (\textbf{P}rioritized \textbf{A}daptive \textbf{C}overage of \textbf{E}vidence), a training-free framework that combines \textit{evidence frontloading} with \textit{pressure-adaptive budgeting}. \textsf{PACE} first reorders candidates by marginal evidence coverage, prioritizing documents that are query-relevant, complementary, and useful for forming multi-hop evidence chains. We show that this objective is monotone submodular, giving greedy selection a $(1-1/e)$ approximation guarantee. \textsf{PACE} then dynamically adjusts the reranking budget according to the relative pressure of the reranker and the LLM. Experiments on three multi-hop QA datasets and online serving simulations show that \textsf{PACE} improves evidence recall, reduces p95 latency under ranking-heavy workloads. More importantly, the two components together reveal that \textit{less can be more}: an evidence-dense top-ranked candidates enable higher final recall with fewer reranked documents.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-209](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
