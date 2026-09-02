# 🧠 大模型相关研究 | 2026年09月03日

> 本类共 **295** 篇论文：已确认 **283** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-295](./part-06.md)

---

### 101. [Feedback-Assisted Trust Propagation over Document Relation Graphs for Retrieval-Augmented Generation](https://arxiv.org/abs/2609.00543)

**<font color=#1a73e8>作者：</font>** Zhuoheng Li, Ying Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) systems rely on external corpora that may contain outdated, contradictory, noisy, or unreliable documents, introducing reliability risks. Prior work has leveraged document relations to improve the answer reliability of RAG. To propagate reliability signals beyond directly compared document pairs, we propose TrustPropRAG, which structures document relations as a graph and estimates document reliability through multi-hop propagation across the graph. TrustPropRAG anchors this propagation with a limited set of human feedback on document reliability, extending these costly-to-collect feedback-based reliability signals across the whole corpus. Specifically, based on the constructed document relation graph, TrustPropRAG estimates a trust score for each document by formulating and solving an optimization problem that jointly captures pairwise document relations and user feedback. These scores are then used to improve the selection of reliable documents and support trust-aware answer generation. Evaluation results show that TrustPropRAG improves both retrieval quality and exact match over baselines, and remains robust under sparse and noisy feedback.

---


### 102. [Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents](https://arxiv.org/abs/2609.00549)

**<font color=#1a73e8>作者：</font>** Seonghyeon Cho, Chanjun Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents increasingly rely on external skills, yet standard evaluations obscure whether retrieving these skills actually helps. Aggregate metrics often compare retrieved versus non-retrieved tasks, introducing severe selection bias and failing to isolate the true effect of skill use. To measure this actual-use capability-which we formalize as Skill Following (SF)-we introduce the Retrieval-Invoked Actual-Use Effect (RAE). RAE computes the same-task outcome difference between matched skill-enabled and skill-disabled executions, conditioned exclusively on tasks where the agent actively retrieved a skill. Evaluating 17 LLMs across coding and mathematical domains, we uncover a stark evaluation paradox: models frequently show positive aggregate retrieval lift but negative RAE. On MBPP+, multiple models that appear to benefit system-wide actually harm their own performance on the exact tasks where retrieval occurred. These findings demonstrate that aggregate averages can create a misleading illusion of tool-use proficiency, whereas RAE directly measures whether the retrieval-to-answer pipeline genuinely rescues more outcomes than it harms.

---


### 103. [Same Semantics, Different Outcome: On the Modality Robustness of Multimodal LLMs under Knowledge Conflict](https://arxiv.org/abs/2609.00550)

**<font color=#1a73e8>作者：</font>** Jungyeon Lee, Yejin Yoon, Taeuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly provided with contextual evidence in heterogeneous forms: as a text passage, as a rendered image of the same passage, or as both together. However, it remains unclear how consistently these surface forms are processed, especially when the evidence conflicts with the model's parametric knowledge. We study modality robustness under knowledge conflict across 13 MLLMs and two datasets, and find them far from robust. (1) Contrary to common belief, models favor a context that contradicts parametric knowledge more readily in image form than in text form; (2) when a contradicting text and image are presented together, the preferred modality is essentially arbitrary, varying with input order, model, and dataset. We further demonstrate that this instability has practical consequences: it degrades performance in multimodal RAG and can be exploited by adversarial attacks. To alleviate this brittleness, we examine several simple techniques---prompting, steering, supervised fine-tuning (SFT), and direct preference optimization; the majority prove ineffective, whereas SFT achieves moderate success. We therefore call for greater awareness of this inconsistency and argue that it is fundamental, demanding attention at multiple training stages.

---


### 104. [EM^2Mem: Event-Centric Multimodal Memory for Large Language Models](https://arxiv.org/abs/2609.00551)

**<font color=#1a73e8>作者：</font>** Yijun Chen, Yaqi Zheng, Yanya Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal memory offers a scalable interface for long-video question answering, but existing methods often retrieve captions, frames, transcripts, summaries, or graph facts as isolated fragments. Although searchable, such fragments are not generation-ready: language models must reconstruct cross-modal and temporal alignments at inference time, when context is limited and attribution is difficult. We propose EM^2Mem, an event-centric multimodal memory framework that binds heterogeneous evidence to event anchors during memory construction. Each event-indexed memory cell aligns multimodal records, temporal context, graph-linked relations, semantic facts, and provenance, enabling compact evidence readout over grounded multimodal events rather than modality-specific fragments. Across three long-video QA benchmarks, EM^2Mem improves average accuracy over the strongest memory baseline by 2.0, 2.4, and 3.7 points, improves strict event-level Top-5 evidence recall by 7.0 points, and reduces per-query latency by 4.67 times and total inference tokens by 63.66% (The code will be integrated into this https URL).

---


### 105. [VoiceLongMemEval: Do Assistants Remember How You Sounded?](https://arxiv.org/abs/2609.00570)

**<font color=#1a73e8>作者：</font>** Ramit Pahwa, Parivesh Priye, Apoorva Beedu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the growing scale of multi-agent architectures and large language models, deployed AI assistants are increasingly tasked with reasoning over long, continuous, multi-session conversation histories. Current benchmarks evaluate this dialogue history as information retrieval over long horizon, temporal reasoning, or knowledge updates, while crucially ignoring the fundamental dynamics of human-agent interaction, i.e. how they said it. To address this gap, we present VoiceLongMemEval (VLME) benchmark, where every answer depends on paralinguistic metadata (emotion labels, prosody descriptors, and voice events) attached to conversational turns, which is otherwise unrecoverable from the words alone. Every item passes a three-stage adversarial gate, ensuring that a strong language model fails when given only the transcript. Evaluating leading frontier and open-weight models reveals a pervasive affect gap; providing text-track paralinguistic metadata yields a 0.09 to 0.38 accuracy boost (0.61 to 0.69 when prompted with evidence hints), while standard ASR pipelines systematically discard this signal. Additionally, audio-native models successfully extract these cues directly from speech (0.354 to 0.412 vs. 0.325 blind). Code and dataset will be made available upon acceptance.

---


### 106. [Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs](https://arxiv.org/abs/2609.00575)

**<font color=#1a73e8>作者：</font>** Seungwoo Jung, Dohyeok Kwon, Seungmin Cha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) architectures scale large language models efficiently, but they demand massive GPU memory. To cope with such demand, models are commonly compressed to reduce their memory footprint. Residual sparsification is a representative compression technique that decomposes each projection matrix of an expert into a shared base matrix and per-expert residual matrix, and then compresses the residuals. Existing sparsification methods compress each residual matrix independently by minimizing its compression error, thereby minimizing the error of each projection matrix. However, our analysis shows that this objective is misaligned with preserving model accuracy after compression. In an expert, the final output is produced through computations coupled across multiple projections and hidden representations. Therefore, even small errors in individual matrices can propagate through hidden representations and projection interactions, leading to large expert output errors and accuracy degradation. To address this misalignment, we propose PARSER, a new residual sparsification method that shifts the compression objective from minimizing isolated matrix errors to preserving the expert output error. PARSER achieves this by introducing output importance, which measures the actual contribution to the expert output error. Our experiments show that, compared with existing methods, PARSER narrows the accuracy gap to the uncompressed model by 1.41$\times$ on Qwen and 1.44$\times$ on DeepSeek, while achieving the same peak memory reduction.

---


### 107. [Consistency Without Alignment: Item-Sensitive Language Models Indistinguishable From Random](https://arxiv.org/abs/2609.00576)

**<font color=#1a73e8>作者：</font>** Cris Huynh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Item-sensitivity, defined as whether a model's choice depends on the specific input rather than on its own output prior, is widely reported as evidence of task competence. We show this evidence is necessary but not sufficient using a forced-choice signalling task abstracted from the board game Deception: Murder in Hong Kong. In this environment, the reference points against which a coordinate should be judged (a fit-maximising strategy, a posterior-maximising strategy, and uniform random selection) are all computable in closed form. Across seven language models, two model families, a post-training ablation, and three independent scoring rules, every one of 21 model-by-rule cells is reliably item-sensitive. Yet 8 of those 21 cells are not statistically distinguishable from a chooser that ignores the item and selects at random, and 5 score worse than random at describing the target. Item-sensitivity and distance from random correlate at only r = 0.30. We call this consistency without alignment and argue it generalises to any evaluation that relies on item-sensitivity, permutation consistency, or self-consistency without an independent reference for the measured quantity. We further find that a literal-similarity baseline with no pragmatics outperforms most tested language models, that adding a pragmatic layer over two baseline similarity sources moves choosers toward random rather than toward the Bayesian reference, and that a standard labelled multiple-choice format carries no measurable content signal here. All results represent the model side of a pre-registered instrument; a matched human condition is designed and piloted but not yet collected.

---


### 108. [Same Request, Different Boundary: Evaluating Cybersecurity Assistance across Conversational Contexts](https://arxiv.org/abs/2609.00578)

**<font color=#1a73e8>作者：</font>** Rui Yang, Yang Hong, Yichao Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can solve complex problems, but their misuse in high-risk domains can lead to severe consequences. Model providers therefore restrict assistance for potentially harmful requests. Refusing all cybersecurity requests would therefore harm legitimate users. Providers need a mechanism to block malicious use without denying legitimate assistance to defenders. Existing cybersecurity-specific datasets evaluate this mechanism, but none considers the conversational context of a request. We introduce 3R-Bench (Refusal, Repetition, and Revision), a benchmark of 150 real-world cybersecurity requests augmented with two adversarial conversational settings, and evaluate eight LLMs on it. Prior assistant behavior strongly changes responses to an unchanged request: among 376 available pairs from a 400-pair panel, compliance rises from 62.0% after refused history to 85.1% after accepted history. The opposite pattern appears under dialogue decomposition. In comparison, compliance falls from 501/800 direct responses to 172/800 after dialogue; among 738 pairs returning model-authored text in both conditions, the decrease is 45.1 points. Failure feedback recovers only a small fraction of this loss.

---


### 109. [Enoki: Efficient Multi-Level Hallucination Detection](https://arxiv.org/abs/2609.00581)

**<font color=#1a73e8>作者：</font>** Elisei Rykov, Timur Ionov, Nikolay Ivanov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ensuring factuality remains a critical challenge for deploying LLMs in high-stakes settings. Existing hallucination detectors usually operate at a single level: claim-level methods provide interpretable factual units, while span-level methods localize unsupported text. Bridging these views is costly, as LLM-heavy pipelines require multiple decomposition and verification calls, and modular systems need additional claim-to-span alignment. We propose Enoki, an Open Information Extraction framework for multi-level hallucination detection. Enoki extracts text-anchored relational facts, verifies them against evidence, and projects unsupported facts back to hallucinated spans. This shared representation enables claim-level verification and span-level localization without requiring separate alignment. Enoki supports LLM-based, encoder-based, and rule-based extraction regimes, balancing accuracy and inference cost through a common interface. Experiments show that Enoki remains competitive with strong claim-level systems while using fewer resources and achieves superior performance on fine-grained span- and entity-level localization. We also release EnokiQA, a dual-granularity dataset with aligned claim-level verification and span-level localization annotations.

---


### 110. [Socrates went Nuclear: Comparing Interaction Strategies for AI systems in a Learning Context using Brain Sensing](https://arxiv.org/abs/2609.00584)

**<font color=#1a73e8>作者：</font>** Alexandre Clin Deffarges, Nataliya Kosmyna, Pattie Maes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Does unrestricted AI access bypass the cognitive effort required for learning, or does it streamline knowledge acquisition? This paper reports on a study where we compare three designs for user-AI interaction in a learning context: (1) an unrestricted conversational bot like ChatGPT, (2) a pedagogically constrained bot that guides through hints without giving final answers, which we refer to as the Socratic mode; and (3) a non-conversational adaptive tutoring system that adjusts difficulty in real-time based on the user's cognitive engagement derived from the brain signals. Fifty study participants were tasked with learning about nuclear safety protocols, a domain chosen for its zero-prior knowledge baseline. The participants progressed through an instructional video, a pre-test, an AI-driven assessment phase, which varied in the three conditions, and an immediate post-test. The nature of the questions centered primarily on factual knowledge acquisition, but it still required participants to have a global understanding of the concepts in order to answer the questions correctly. A Muse headband was used to derive the cognitive engagement of all users in all conditions. The unrestricted chatbot produced higher learning gains (delta) than both constrained modes (p < .03, d > 0.80), while the adaptive condition generated significantly higher EEG engagement (p = .018). The cluster analysis of chatbot usage and discussion patterns by users showed that most participants in the unrestricted-mode adopted a direct answer-retrieval strategy, while participants in the Socratic-mode initially attempted to reason through the hints before progressively disengaging. Consequently, this also suggests that the success of the unrestricted AI is not an evidence of deeper learning, but rather a result of the immediate post-test evaluation after the training phase.

---


### 111. [CRAFT: Fine-Tuning Pre-hoc Explainability in AI-native 6G RAN](https://arxiv.org/abs/2609.00590)

**<font color=#1a73e8>作者：</font>** Pranshav Gajjar, Vijay K Shah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The next generation of mobile networks is envisioned as fully AI-native, with AI-RAN architectures embedding small language models (SLMs) to perform reasoning over real-time telemetry. The state-of-the-art training paradigms for telecom LLMs, exemplified by RANSTRUCT-style supervised fine-tuning (SFT) on curated instruction data, are limited to post hoc rationalization. Here, the explanations, when produced at all, are generated after or independently of the decision, leaving the decision process unauditable. Pre-hoc reasoning, where a causal reasoning trace is produced before the output label, is preferable, and the broader LLM reasoning literature has made real progress toward it via RL methods such as Group Relative Policy Optimization (GRPO). Here we observe that transplanting this recipe into the telecom setting runs into a cold-start barrier: SLMs either learn to output the desired format or learn to predict the label, but rarely both. We identify this barrier and propose CRAFT, which stands for Cold-start Reasoning Alignment via Fine-Tuning, a data-centric method to autonomously generate a verified dataset of (input, trace, label) triplets. CRAFT fine-tunes SLMs on this verified data using low-rank adaptation (LoRA), requiring substantially less compute and wall-clock time than GRPO-based methods. On the TRACTOR and IC xApp telecom datasets, CRAFT achieves up to 86.5% and 94.6% for accuracy and F1 with no parse failures, while direct GRPO and SFT+GRPO fail to exceed 28% and 53.5% F1 with multiple parse failures. We further show that CRAFT-initialized policies serve as a robust foundation for subsequent GRPO fine-tuning, as under diverse reward functions the performance remains consistent with no parse failures. Finally, we demonstrate that CRAFT consumes 59% less energy than GRPO-based baselines, making it a sustainable path to deployable, auditable AI in 6G RAN.

---


### 112. [A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss](https://arxiv.org/abs/2609.00591)

**<font color=#1a73e8>作者：</font>** Suryaansh Jain, Rahasya Barkur, Vishal G 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An image may be worth a thousand words, but most captioning models describe it in only a few. Modern vision-language models produce fluent high-level captions, yet routinely miss the attributes, counts, textures, materials, and spatial relations that make an image visually specific. Recent multi-stage systems recover some of these details through generation, decomposition, verification, and rewriting, but they do so at the expense of substantially higher inference latency.
We propose SimLoss, a reference-free embedding-space objective for single-pass fine-grained image captioning. SimLoss trains a vision-language model to align its projected hidden-state representation with a frozen image embedding through an InfoNCE contrastive loss, supplying a dense visual supervision signal before any text is decoded, and requiring neither human-written fine-grained captions nor pseudo-captions from a multi-stage pipeline. We instantiate it as SimLoss FFT, which backpropagates through a locally available embedding model, and SimLoss GRPO, which treats that model as a black-box reward.
Compared with single-pass, multi-stage verification, reward-optimized, and perception-aware baselines, the fully differentiable fine-tuning variant, SimLoss FFT, achieves the highest precision while nearly matching the F1 score of the multi-stage method, all while retaining single-pass inference and running roughly 20 times faster than the multi-stage pipeline.
The reward-based variant SimLoss GRPO attains the strongest recall. Together, these results show that embedding-space supervision can recover the quality of multi-stage verification at the latency of a single-pass captioner.

---


### 113. [SoK: When Safe Agents Fail Together: The Security of Multi Agent LLM Systems](https://arxiv.org/abs/2609.00595)

**<font color=#1a73e8>作者：</font>** Rui Yang, Junjie Xu, Zhengyu Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safe agents can fail together. Multi-agent LLM systems (MAS) move information, state, decisions, and authority across principal boundaries, creating failures that local checks may miss. Without an execution-level view, a multi-agent setting can easily be mistaken for evidence of a genuinely multi-agent security effect. We thus systematize MAS security through an execution-centered analysis of 197 works, covering six interaction interfaces, four adversary positions, seven system-level risks, and eight recurring attack paths. We introduce an A-I-R framework that organizes attacks by adversary position, interaction interface, and resulting system-level risk, unifying otherwise fragmented attack mechanisms across MAS. We organize defenses through a five-part contract covering path target, observation, intervention, trust boundary, and recovery, and identify path closure and recovery as key challenges. We audit 44 evaluation and benchmark works and identify open challenges in isolating interaction effects, designing comparable and diagnostic metrics, supporting reuse across MAS designs, and evaluating open-system operation. Together, these findings motivate an interaction-aware view of MAS security: trace attacks end to end, test whether defenses close those paths, and evaluate system-level effects with appropriate counterfactuals.

---


### 114. [Topological Steering](https://arxiv.org/abs/2609.00597)

**<font color=#1a73e8>作者：</font>** Benoît Guérand, Tan Minh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the rapid rise of large language models (LLMs), controlling undesirable model behaviors has become increasingly important. Existing behavioral control methods typically intervene directly in activation or feature space, but such approaches can be sensitive to outliers, distributional shifts, noise, and other local perturbations. Motivated by Topological Data Analysis (TDA), which captures global rather than purely local structure, we propose Topological Steering, a new framework for steering LLM behavior through the topological representation of activation spaces. Using persistence diagrams, our method connects activation-based steering with TDA and enables more robust behavioral control. We show that Topological Steering consistently modifies LLM behavior across multiple model families and model sizes.

---


### 115. [NeuroGraph: An AI Graph-Driven Neuro-Symbolic Framework for Explainable Threat Reasoning in Advanced Manufacturing](https://arxiv.org/abs/2609.00604)

**<font color=#1a73e8>作者：</font>** Padmeswari Nandiya, Ahmad Mohsin, Ahmed Ibrahim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growing complexity of cyber-physical attack surfaces in advanced manufacturing has made cyber threat intelligence analysis increasingly difficult. Although large language models and retrieval-augmented generation have improved CTI workflows, text-based approaches remain vulnerable to hallucinations and provide limited support for structured reasoning over interconnected threats. Graph-based RAG reduces some of these limitations, but existing approaches often lack ontology-consistent multi-hop reasoning and transparent evidence tracing across heterogeneous cybersecurity data. This paper proposes a graph-grounded neuro-symbolic framework that integrates ontology-aware symbolic query generation, knowledge graph retrieval, and neural language generation to support accurate and explainable threat analysis across information technology and operational technology environments. The framework adopts a dual-large language model architecture: the first model translates natural-language questions into executable Cypher queries for symbolic graph retrieval, while the second generates answers strictly from the retrieved graph evidence. Experimental evaluation using publicly available cyber threat intelligence benchmarks shows consistent improvements over the published baseline in reasoning accuracy, while also reducing hallucinations, strengthening multi-hop reasoning, and improving robustness to adversarial perturbations. Runtime and explainability analyses further demonstrate that the framework maintains interactive inference performance and exposes graph-grounded reasoning artifacts that allow analysts to inspect and verify each stage of the analysis. Overall, the results highlight the potential of graph-grounded neuro-symbolic reasoning as a scalable, interpretable, and reliable approach to cyber threat intelligence for next-generation Industry 5.0 environments.

---


### 116. [Confess What You Know: Forget-Set Misalignment with Model Knowledge in LLM Unlearning](https://arxiv.org/abs/2609.00605)

**<font color=#1a73e8>作者：</font>** Miso Kim, Georu Lee, Seungwon Jeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning for large language models (LLMs) often assumes that a pre-defined forget set matches what the model has memorized, but this frequently breaks in realistic privacy settings where the original training data is inaccessible. We term this gap forget-set misalignment and identify two cases. In Under Unlearning, the forget set omits memorized information and leakage persists. In Out-of-Knowledge Unlearning, the algorithm is driven to "forget" knowledge the model never learned, perturbing parameters and degrading utility. Using gradient-level analysis, we show these behaviors arise from misaligned unlearning targets rather than specific optimization choices. We then propose CONfession-to-Forget-Set (CONFS), a data-blind framework that constructs model-aligned forget sets by eliciting and formalizing the model's memorized knowledge. Across synthetic, multimodal, and real-world benchmarks, CONFS approaches Gold-standard performance on several metrics and achieves a competitive forgetting-utility balance, while preserving utility better than other data-blind forget-set constructions.

---


### 117. [Investigating Assistant Bias in LLM User Simulators Using a Role Vector](https://arxiv.org/abs/2609.00608)

**<font color=#1a73e8>作者：</font>** Daeheon Jeong, Yoonjoo Lee, Eugene Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based user simulators are increasingly used to evaluate autonomous agents at scale, in place of costly human evaluations. Despite this promise, these simulators exhibit "assistant bias," a tendency to cooperate and pursue task goals. They rarely reproduce the frustration or disengagement that real users exhibit, compromising evaluation validity. Prior work outlines that this bias is baked in during model training, which role-playing prompts fail to override. We analyze this bias from model activations, extracting a user role vector by contrasting how the model represents user versus assistant perspectives on the same dialogue. We observe two findings: (i) the user direction is identifiable in activations, elicits user-like behaviors, and captures characteristics distinct from assistant traits; and (ii) although user-role activation associates with simulation realism and steering strengthens it, it can exaggerate user behaviors and override individual user profiles. Together, our findings provide a representation-level analysis of LLM user simulators, confirming that assistant bias is structurally identifiable and that user behavior can be directionally analyzed.

---


### 118. [Control-Data Flow Separation: Stable Prompt Optimization in Multi-Agent LLMs](https://arxiv.org/abs/2609.00621)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Syed Shariyar Murtaza, Junaid Ahmad Bhatti 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt optimization can improve multi-agent LLM systems, but the prompts being optimized often serve two entangled roles: generating task-relevant content and specifying execution-critical protocols, such as message routing, output formatting, and termination signals, on which the underlying code relies. As a result, a prompt edit intended to improve content generation can inadvertently corrupt the protocol and cause the entire agent pipeline to fail. Our key observation is that these two roles have different representations: execution protocols are typically structured, while task-relevant content is usually expressed in unstructured language. Based on this, we propose control-data flow separation, where execution-critical control is represented as typed, validated program objects, while task-relevant language remains the optimizable data flow for agent communication. This design allows optimizers to improve multi-agent behavior without exposing the routing or formatting interface to prompt drift. Across synthetic reasoning, collaborative review generation, and insurance rating workflows, our framework empirically achieves 100% eventual protocol validity while consistently improving task performance.

---


### 119. [Trust Your Guide Only When Certain: Uncertainty-Aware Sparse Alignment at Inference Time](https://arxiv.org/abs/2609.00624)

**<font color=#1a73e8>作者：</font>** Zeen Zhu, Zhuo Li, Weiyang Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A prominent paradigm in inference-time alignment employs lightweight supervisors to steer Large Language Models (LLMs). Through empirical analysis, we identify a structural mismatch in this paradigm: weak supervisors exhibit pervasive high entropy across the vast majority of tokens, yet prevailing dense intervention approaches mandate supervision at every decoding step. This leads to frequent low-confidence interventions that can disrupt valid base-model reasoning and incur substantial utility costs. To resolve this, we propose TUSA (Trust-based Uncertainty Sparse Alignment). Moving away from continuous oversight, TUSA reframes alignment as a dynamic arbitration process, introducing an uncertainty-aware arbiter that authorizes intervention only when two conditions are met: the supervisor is confident and the token is semantically salient. This mechanism effectively filters out uncertainty-driven noise and redundant supervision. Extensive experiments across multiple models and benchmarks show that TUSA consistently improves both safety alignment and general helpfulness. By bypassing approximately 50% of alignment steps, it not only enhances safety preference by up to 15.6%, but also boosts general preference rates by up to 12.0% compared to the dense baseline, demonstrating that selective, high-precision alignment can outperform continuous supervision.

---


### 120. [Restrict, Don't Retrain: Inference-Time VLM Guidance for Zero-Shot Aerial Segmentation](https://arxiv.org/abs/2609.00628)

**<font color=#1a73e8>作者：</font>** Teresa DiMeola, Charles Walter, Hong Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Global welfare often depends on the correct interpretation of aerial and satellite imagery. Acting on such imagery (mapping flooded ground, crop extent, or damaged infrastructure) demands pixel-level segmentation to ensure perfect class localization. Pretrained general foundation models, when applied directly, often miss important features and cannot always find all the classes belonging to a given scene, overlooking smaller objects that matter most. We use a single consumer-grade GPU running a vision-language model (VLM) to supply this missing guidance, improving segmentation while producing structured, auditable evidence that drives the result and can be inspected on its own. We fuse three approaches: the frozen foundation model that labels every pixel, and two queries to a VLM, one to choose the classes that matter, and one to locate the small objects the base model misses. Evaluating across four aerial datasets, we see consistent gains at each stage where the base model is competent.

---


### 121. [ExpArt-KG: Artwork Image Description Generation through Iterative Exploration of Knowledge Graphs](https://arxiv.org/abs/2609.00629)

**<font color=#1a73e8>作者：</font>** Yuta Kato, Shintaro Ozaki, Kazuki Hayashi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) achieve strong performance on image-grounded text generation and visual question answering. However, it remains difficult for them to comprehensively and accurately describe the factual relations among the entities and concepts associated with the objects depicted in an image. In this work, we propose a framework that efficiently exploits factual information from a knowledge graph via retrieval-augmented generation (RAG), with the goal of enabling LVLMs to generate detailed and accurate image explanations. Specifically, our method alternates between answer generation and knowledge-graph retrieval, and controls the search using a correctness judgment, thereby acquiring the necessary and sufficient factual information efficiently. We also construct a knowledge graph for the artwork domain (ExpArt-KG), in which the correspondence between images and entities is unambiguous. Applying the proposed method to this knowledge graph, we show experimentally that it improves the level of detail of artwork explanations and reduces the retrieval cost of external knowledge while maintaining generation quality comparable to that of iterating a fixed number of times.

---


### 122. [Breaking the Structural Identity: Personalized Federated LoRA Fine-tuning under Rank Heterogeneity](https://arxiv.org/abs/2609.00632)

**<font color=#1a73e8>作者：</font>** Lei Wang, Jieming Bian, Letian Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable success across diverse domains, but their adaptation to privacy-sensitive, distributed datasets remains a challenge. While Federated Learning (FL) combined with Low-Rank Adaptation (LoRA) provides a resource-efficient paradigm for collaborative fine-tuning, practical deployments are hindered by the dual challenges of resource heterogeneity and data heterogeneity. Existing rank-heterogeneous methods primarily focus on bridging dimension mismatches for aggregation but typically provide a unified global model for all clients sharing the same rank, failing to capture client-specific features in non-IID scenarios. In this paper, we propose FedRoRA (Federated Rank-wise Personalized LoRA), a novel framework that enables fine-grained personalization within rank-heterogeneous federations. FedRoRA decouples adaptation into shared global directions and personalized rank-wise magnitudes governed by learnable diagonal scales. On the server side, it extracts a global subspace via singular value decomposition (SVD) and redistributes client-specific initializations through a personalized projection and top-$k$ selection mechanism. Extensive experiments on NLU and NLG benchmarks demonstrate that FedRoRA consistently outperforms state-of-the-art methods.

---


### 123. [REVISE: Validity-Guided Recovery for Online Revisions in Agent Workflows](https://arxiv.org/abs/2609.00643)

**<font color=#1a73e8>作者：</font>** Ruoling Qi, Xuaner Wu, Penghang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent revisions expose a fundamental correctness--efficiency trade-off during concurrent execution. Discarding ongoing work preserves latest-version correctness but wastes progress that may remain valid, whereas reusing prior work preserves efficiency but risks propagating stale state into outputs and tool effects. Existing recovery strategies resolve this trade-off in an imbalanced way with coarse-grained policies: they either favor efficiency by allowing potentially stale work to continue, or favor correctness by restarting the workflow or recomputing a linear suffix from the earliest conflict, thereby discarding unaffected progress. We present \textsc{Revise}, a validity-guided runtime for fine-grained recovery in structured agent workflows. When a revision arrives, \textsc{Revise} first intersects its delta with recorded data and control dependencies and propagates the resulting impact through the partially executed DAG to identify affected work. It then stops invalid work, preserves validity-established progress beyond the earliest conflict, and recomputes only the affected region. Incomplete provenance conservatively expands recovery, while reused results are revalidated before commit. Analysis of real coding-agent traces show online recovery opportunities: 118 sessions retain observable work before a queued later message is delivered; across 167 overlapping assistant responses, enqueue-to-completion overlap reaches 56.55~s at p95. Across 300 challenging revision/commit executions, \textsc{Revise} matches a latest-version oracle with no stale outputs or effects. On unmodified LangGraph and LLMCompiler applications using Qwen3-14B, it reduces model calls by 40.6--56.0\% relative to full restart and by 31.3--43.6\% relative to suffix recomputation. Under serving pressure, it further reduces revision-to-correct-completion tokens by 13.26\% and improves SLO goodput by 3.07--5.43\%.

---


### 124. [You Cannot Photograph the Same Street Twice: Reliability Limits in Vision-Language Measurement of Urban Change](https://arxiv.org/abs/2609.00649)

**<font color=#1a73e8>作者：</font>** Kaizhen Tan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models are increasingly used to measure urban change from repeated street-level imagery, but their longitudinal reliability is not well understood. We test how much a perception score can change when the street itself does not undergo substantial redevelopment. Using 4,648 consecutive-epoch image pairs from 435 Google Street View standpoints across five US cities, we find that re-photographing the same street changes a perception score by 0.80 points on average, equivalent to 66.5% of the difference between two different streets in the same city. Repeated model calls contribute almost no variation, while image re-encoding and prompt-order changes each account for about one fifth of the between-street difference. Six image statistics describing scattering, contrast, colour, exposure, sharpness and specularity explain almost none of the remaining epoch-to-epoch variation. A small systematic drift of about 0.1 points remains and increases with the interval between captures, consistent with minor physical changes not recorded by redevelopment labels. Controlled experiments further show that acquisition conditions can shift scores when camera and image properties are allowed to vary, and that the direction of these shifts depends on the model. In crowdsourced imagery, camera geometry alone causes a model to report physical change in 45% of identical-scene pairs; normalising both images to a common virtual camera reduces this rate to 7.5%. Despite poor reliability at the individual-location level, aggregation recovers a coherent redevelopment signal: changed streets are judged wealthier, better maintained, more enclosed and less green. These results show that vision-language measurement of urban change is reliable at the scale of hundreds of paired observations, but not at the scale of individual sample points.

---


### 125. [Self-Reports Are Not Verification: Environment-Grounded Auditing of LLM Operators in Evolutionary Search](https://arxiv.org/abs/2609.00652)

**<font color=#1a73e8>作者：</font>** Enrong Pan, Ryan Zhou, Ting Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model agents increasingly propose actions, observe external feedback, and explain their own behavior. Their confidence and rationales are convenient monitoring signals, but convenience is not verification. We introduce an environment-grounded audit in which every intermediate proposal receives an exact outcome. A language model operates an evolutionary Contexto search whose feedback function assigns every valid guess an exact rank without human annotation. Across 200 runs spanning five configurations and three model families, four reporting configurations produce 12,249 self-reports. We test three assumptions: stated confidence is calibrated, inherited rationales affect later proposals, and fitness-based selection improves report quality. All three fail. Operators overstate top-100 success by factors of 4.8 to 9.3, while calibration and discrimination dissociate across model families. Controlled interventions on 754 inherited rationales bound any measured benefit of the genuine rationale to roughly 250 ranks. Neither fitness-based nor random selection produces a detectable selection differential or parent-to-offspring transmission in report accuracy, despite sharply different search behavior. Agent self-reports should therefore be treated as claims to verify against the environment, not as evidence of their own reliability.

---


### 126. [SciTrue: Reliable Scientific Claim Validation with Frontier and Open Language Models at the NTCIR SciClaimEval Task](https://arxiv.org/abs/2609.00654)

**<font color=#1a73e8>作者：</font>** Qiming Bao, Neşet Özkan Tan, Siyuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We describe the SciTrue team's participation in both subtasks of the NTCIR-19 SciClaimEval task~\cite{sciclaimeval}, which asks systems to verify scientific claims against the tables and figures of a paper. Rather than tuning a single model, we benchmark eleven frontier and open multimodal models under one honest, per-sample protocol and combine them with light, transparent post-processing. On the official, blind test leaderboard (Section~\ref{sec:results}), SciTrue placed first by a clear margin in three of the four evidence-category/subtask combinations, and tied for first on the primary metric in the fourth. Three findings explain the result. First, strong instruction-tuned models are already competitive: Claude Opus~4.8 and Gemma-4-31B each exceed the strongest public baseline (o4-mini), and GPT-5.5 and Claude Fable~5 lead both subtasks (97.7 on Subtask~2). Second, the task's pairing structure is the largest lever: a \emph{leak-free pair prior} that recovers the Supported/Refuted pairing from the claim text alone (a visible field) and assigns Supported to the higher-confidence evidence raises Subtask-1 pair-accuracy from 72.2 to 93.5, far more than any model swap or ensemble weighting. Third, a case-by-case audit finds that most residual errors are visually-undetectable label-mapping swaps or dataset label noise, so measured accuracy understates the true ability and the fixable-by-modeling headroom is small. Controlled fine-tuning, distillation, and agentic consistency-checking support the same conclusions, and we document throughout a measurement leak---label information reaching a system through the packaging of the data rather than its content---in which the released file ordering encodes the label, including one instance that briefly misled our own pipeline.

---


### 127. [Teaching Vision-Language Models to Use the Scale They Are Given: Label-Free Equivariance Training for Metric Physical Reasoning](https://arxiv.org/abs/2609.00658)

**<font color=#1a73e8>作者：</font>** Kaizhen Tan, Yang Feng, Heqing Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metric questions about video require vision-language models to use supplied real-world references to convert visual measurements into physical units. Yet we find that current models use this scale information only partially. When every world-space quantity in a prompt is rescaled by a common factor, the video remains equally valid and the correct answer changes by exactly that factor, but model predictions move only part of the way and accuracy remains concentrated near the familiar scale of the depicted objects. Across eight vision-language models, this under-response persists over four orders of magnitude. The same models recover the correct closed-form scaling laws when the identical physics is asked in a scale-free form, indicating that the main deficit lies in metric grounding rather than physical mechanism knowledge. We use this exact scaling relation as supervision without requiring metric annotations. Under a common rescaling of the supplied world-space quantities, the correct metric answer must change by the same factor. EquiSD exploits this constraint by projecting a model's own prediction onto the scale-equivariant family and fine-tuning the model on the resulting targets. It requires no ground-truth answers and only one model query per training video. On held-out simulated videos, EquiSD increases a 3B model's median response slope from 0.66 to 0.94 and improves mean relative accuracy by 9.2 points across scales. The learned relation generalizes to unseen world scales and transfers without adaptation to real QuantiPhy videos, where accuracy increases by 6.4 points. These results show that an exact physical symmetry can provide label-free supervision for improving metric grounding in vision-language models.

---


### 128. [Drift-Aware LLM Routing with Sparse Contexts and Shared Budgets](https://arxiv.org/abs/2609.00662)

**<font color=#1a73e8>作者：</font>** Cheung Hao Lee, Patrick Wong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A multi-model language service must route each request while preserving workload-level budgets for compute, latency, memory, or monetary cost. Two features make this problem materially harder than static model selection. Prompt representations are high dimensional, so only a small subset of embedding directions may predict the incremental value of a model, and both the request mix and the model frontier drift after launches, fine-tunes, quantization changes, and system updates. We formulate nonstationary sparse contextual routing with multiple knapsack constraints and an optional shadow-audit stream that evaluates a small fraction of prompts on several models.
We propose Drift-Aware Sparse Routing (DRS). The policy estimates reward and resource use from a rolling audit window, routes using pessimistic reward and optimistic cost estimates, updates resource shadow prices online, and applies a hard meter before commitment. The analysis separates control from statistics. On any event with uniform prediction radii $\{\beta_t\}$, regret against a paced dynamic fluid benchmark is bounded by the sum of the radii, a capacity-buffer term, and an $O(\sqrt{T})$ pacing term. Under a sparse linear model and bounded drift $V_T$, rolling estimation gives \[ \widetilde O\left( T\sqrt{\frac{s}{\rho W}}+WV_T+\sqrt{T} \right), \] where $s$ is sparsity, $\rho$ is the audit rate, and $W$ is the window length. Optimizing $W$ yields the usual stationary $O(\sqrt{sT/\rho})$ rate when $V_T=0$ and a $O(T^{2/3}(s/\rho)^{1/3}V_T^{1/3})$ adaptation term under drift.

---


### 129. [Separating perception from reasoning in vision-language models: a model-free render ceiling for crystal structures](https://arxiv.org/abs/2609.00663)

**<font color=#1a73e8>作者：</font>** Can Polat, Mustafa Kurban, Erchin Serpedin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal evaluations cannot say whether a vision-language model misread an image or misreasoned about it, because every existing method for separating the two places a second model in the loop. We introduce the render ceiling, a model-free reference for benchmarks built by rendering known objects: inverting the frozen cameras and re-solving cross-view correspondence recovers exactly the answer the images support. We prove the ceiling fails only through an enumerable set of projection coincidences and certify that set empty on 2,160 rendered crystal structures, so every point of a model's deficit belongs to the model. Across fourteen vision-language models, supplying exact geometry as text lifts every model yet closes under half the gap for thirteen, while a supervised vision model with no language component reads the same images at 0.8952, above every vision-language model. The instrument exposes extraction-stage fabrication that downstream accuracy would misattribute to reasoning, yields camera-placement rules for benchmark builders, and transfers to any benchmark with an invertible forward rendering.

---


### 130. [Triple-Bottom-Line Sustainability of Language Models for Edge AI: A Comparison Between SLMs and Quantized LLMs](https://arxiv.org/abs/2609.00665)

**<font color=#1a73e8>作者：</font>** Jainil Dharmil Shah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Edge-AI model selection is commonly driven by one isolated metric - accuracy, latency, memory, energy, or safety, even though a deployable language model must balance all five. Our work focuses on answering the question whether na- tively trained small language models (SLMs) or large language models (LLMs) compressed through post-training quantization offer the more sustainable edge- deployment trade-off. We introduce a reproducible Holistic Sustainability Score (HSS) organized around the triple bottom line: an economic pillar for capability and systems efficiency, an environmental pillar for operational GPU energy and a social pillar for harmful-prompt robustness. Five BF16 SLMs and five LLMs under different quantization approaches - BF16, INT8, NF4 4-bit, GPTQ 4-bit, and GGUF Q4 produce 30 measured configurations. Capability is assessed on five zero-shot benchmarks; efficiency uses latency, throughput, peak VRAM and energy; and safety is approximated by attack success rate on five harmful prompts. Qwen3-30B-A3B/GGUF Q4 ranks first in the combined pool (93.38), followed by Mistral-Small-24B/GGUF Q4 (92.40), while Phi-4-mini/BF16 is the highest- ranked SLM in that pool (89.49). Thus, the hypothesis that native SLMs must be the most sustainable edge choice is not supported universally; optimized quantized LLMs can win overall, while SLMs remain competitive through lower resource demand. Quantization is a systems-level choice rather than a monotonic precision- efficiency trade-off and HSS remains relative to its comparison pool and proxy definitions.

---


### 131. [SCoNE: Selective Context-aware Neuron Editing for Robust Retrieval-Augmented Generation](https://arxiv.org/abs/2609.00689)

**<font color=#1a73e8>作者：</font>** Chaewon Kim, Seo Yeon Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) is highly sensitive to retrieval noise: when retrieved documents mix informative and irrelevant context, LLMs are easily distracted, leading to hallucinations. To overcome this, we propose SCoNE (Selective Context-aware Neuron Editing), a training-free model editing approach that improves retrieval noise robustness by selectively strengthening context-aware FFN neurons that are identified by both high attribution and high cross-input variability. SCoNE requires only a small number of mining samples, no fine-tuning, and no inference-time overhead. Across various knowledge-intensive question-answering benchmarks and two LLM backbones, SCoNE consistently outperforms competitive baseline methods. Our code is available at this https URL.

---


### 132. [Patterning in Practice: Debiasing Reward Models with Susceptibilities](https://arxiv.org/abs/2609.00699)

**<font color=#1a73e8>作者：</font>** George Wang, Elizabeth Donoway, Daniel Murfet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward models trained on human preferences are known to suffer from length, formatting, and other stylistic biases. In this paper we use patterning, which reweights each preference pair according to its measured effect on posterior expectation values of benchmark losses (its susceptibility), to debias a Gemma 2 9B Instruct reward model trained on Skywork-Reward-Preference v0.2. We obtain $+14.2 \pm 1.2$ pp on RM-Bench Hard, the split where style cues point against correctness (mean $\pm$ s.e.\ over 5 seeds), with overall RM-Bench accuracy preserved, comparable to the strongest Hard-split gain reported by the closest published comparator (SteerRM, $+13.2$ pp). We demonstrate in a simple case that the reweighting is interpretable by tracing a side effect of the intervention (a regression on a safety subset of RM-Bench) to a small class of training pairs, which we confirm by ablation. The weights also transfer: those computed on Gemma 2 9B debias Gemma 2 2B and 27B with no recomputation, and transfer partially to Llama 3.1 8B. This is the first application of patterning, a program grounded in singular learning theory, beyond small models and synthetic tasks.

---


### 133. [Value Over Language Model: Detecting Original Contribution in Writing](https://arxiv.org/abs/2609.00700)

**<font color=#1a73e8>作者：</font>** Vibhhu Sharma, Thorsten Joachims, Sarah Dean  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs have been rapidly adopted across writing tasks, prompting the development of tools for detecting LLM-generated text. Yet, these tools largely measure how much of a document's surface text was written by an LLM and aren't fundamentally designed to measure how much of the information content or ideas originated from the LLM itself rather than being supplied by the user in the prompt. In this work, we design a framework that measures how much value a person adds on top of what a language model could have easily produced by itself. The method requires no training or labeled data and never scores the document's surface text, insulating it from stylistic confounders. Instead, it extracts the document's content at increasing levels of granularity, uses an LLM to reconstruct the document from each partial representation, and compares these reconstructions with those produced from the task description alone. We call this framework Value Over Language Model (VOLM), which measures a document's contribution relative to a replacement-level document that an LLM could produce from the task description alone. We evaluate VOLM with a specific instantiation of this framework across three domains: news articles, ICLR peer reviews, and argumentative essays. VOLM separates human-authored documents from matched LLM-generated documents produced from generic task descriptions, while remaining substantially invariant to content-preserving transformations, including LLM-based reconstruction and round-trip translation. We further find that increasingly constrained content extractors reduce residual differences between LLM-generated and humanized text, demonstrating the importance of disentangling informational content from stylistic variation. We hope these results encourage further work on specialized instantiations of the framework and on assessing human contributions in LLM-assisted writing more generally.

---


### 134. [A Certificate-Producing Cascade for Equational Implication: The SAIR EQT2 Stage 2 Solver](https://arxiv.org/abs/2609.00706)

**<font color=#1a73e8>作者：</font>** Haobo Ma, Wenlin Zhang, Manuel Israel Cázares  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The SAIR Mathematics Distillation Challenge on Equational Theories asks a solver to classify whether one magma identity implies another and, for either verdict, to return a certificate accepted by a deterministic Lean judge. We present a single-file solver organized as a cheapest-first cascade. Its false branch combines coefficient tests over structured algebra families, bounded finite-model search, an explicit central-groupoid witness, and several infinite-carrier witnesses. Its true branch is a proof-producing ordered unit superposition procedure with Knuth-Bendix ordering, bidirectional demodulation, indexing, memoised substitution, and anytime size deepening. Search results remain outside the trusted base: successful derivations are replayed as small Lean terms, and countermodels are rechecked by the competition judge.
The frozen solver is a 189,504-byte Python file with SHA-256 f2392533c9f4c03b.... In local runs through official judge revision 2848228, it produced accepted certificates for all 1,889 rows of the six public sets with no language-model calls. Separate measurements recorded full agreement on the 800 published Stage 1 evaluation-distribution problems, 100 accepted rows in the canonical Marathon manifest without tokens, and 200 accepted rows in the hosted playground. These are regression and playground measurements, not a leaderboard result and not evidence about a hidden set. All quantitative claims are tied to immutable result ledgers; the paper makes no completeness or comparative-superiority claim.

---


### 135. [Controllable Image Captioning with Prompt-Conditioned Scene Rewards](https://arxiv.org/abs/2609.00709)

**<font color=#1a73e8>作者：</font>** Jongyeop Hyun, Taeyoung Kim, Hyounghun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models produce fluent image descriptions but offer limited semantic control: users cannot reliably specify whether captions should emphasize attributes, relations, or particular image regions. We present Fine-grained Captioning Control Using Scene Rewards (FoCUS), a controllable image captioning method that lets users steer captions toward specific semantic emphases through natural-language control prompts. The core idea is a prompt-conditioned control objective based on scene-graph-aligned component scores. Generated captions are parsed and aligned to scene-graph components such as objects, attributes, and relations. These components are differentially weighted, including negative weights, according to the requested emphasis. We optimize this objective with GRPO and further improve its reliability through a stricter object validity threshold and reasoning-based verification for attribute and relation scoring. To evaluate controllability, we introduce Semantic Control and Precision Evaluation (SCoPE), a benchmark with contrastive Include/Avoid constraints for measuring both target content coverage and out-of-scope suppression. Experiments on two VLM backbones show that FoCUS consistently improves controllability and fine-grained caption quality without degrading general caption performance.

---


### 136. [ChatDev 2.0: A No-Code Multi-Agent Platform for Developing Everything](https://arxiv.org/abs/2609.00714)

**<font color=#1a73e8>作者：</font>** Yufan Dang, Shu Yao, Bowen Lai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems (MAS) have shown strong potential for solving complex tasks, yet their development forces a tradeoff: code frameworks are expressive but engineering-intensive, while no-code builders simplify authoring but constrain agent interactions to author-defined workflows. We present ChatDev 2.0: DevAll (hereafter DevAll), a no-code platform for building, executing, and inspecting heterogeneous MAS that delivers both high expressiveness and ease of use. In terms of expressiveness, DevAll pairs a declarative executable graph abstraction with a cycle-aware execution engine, so that heterogeneous agents and dynamic and cyclic interactions can be represented and executed within a single framework. For ease of use, an integrated visual interface lets users author, run, monitor, and inspect MAS, including human-in-the-loop steps, entirely without writing code. Experiments demonstrate that DevAll reproduces state-of-the-art MAS across three representative tasks at competitive performance and without task-specific orchestration code, highlighting its effectiveness as a general-purpose platform for LLM-based MAS. DevAll is available at this https URL.

---


### 137. [SOVER: Formal Certification of Optimization Reformulations via LLM-Assisted SMT Verification](https://arxiv.org/abs/2609.00728)

**<font color=#1a73e8>作者：</font>** Swapnil Bhattacharyya, Mayank Baranwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown remarkable promise in translating and reformulating complex mathematical optimization problems across modeling languages. However, validating such transformations through empirical solver executions alone is unreliable, as solver outcomes may be affected by local minima, structural timeouts, numerical artifacts, and subtle semantic divergence between formulations. We introduce SOVER, an LLM-assisted SMT framework that separates semantic mapping from formal certification: Z3 checks domain cross-feasibility and global objective-order preservation for mixed-integer linear formulations, while dReal provides tolerance-aware feasibility/range and $\epsilon$-argmin checks for continuous nonlinear formulations. We also introduce NLEquiv-150, a public benchmark of 100 equivalent and 50 deliberately hard non-equivalent nonlinear reformulation pairs. With LLM-extracted mappings, SOVER classifies 149/150 pairs (99.33%) correctly, including all 50 hard negatives; the sole error is an incomplete mapping extraction.

---


### 138. [Agentic Empirical Asset Pricing: Methodological Foundations](https://arxiv.org/abs/2609.00731)

**<font color=#1a73e8>作者：</font>** Yingjian Pan, Xiaowei Ding, Kay Giesecke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in LLM agents enable a new paradigm for asset pricing, which we call Agentic Empirical Asset Pricing (AEAP): systems that autonomously conduct the scientific discovery process itself. We define AEAP and identify its core building blocks. Existing evaluation practices backtest only the outputs (factors or trades), not the autonomous discovery system that produced them. We focus on factor discovery, contributing a reference architecture, a rigorous evaluation standard for discovered factors, and a method for out-of-sample backtesting the discovery system. As a concrete instance of that architecture, we evaluate SEADS against five re-implemented baselines on two US equity panels using this standard: no single metric ranks the systems consistently, motivating evaluation on multiple axes at once. A separate rolling re-execution then asks the complementary question of whether the discovery process itself, not one static output, is reliable. We also report negative findings and limitations that surface further evaluation pitfalls for future AEAP systems.

---


### 139. [Online Self-Weighted Fine-Tuning](https://arxiv.org/abs/2609.00734)

**<font color=#1a73e8>作者：</font>** Haiquan Wen, Yiwei He, Bei Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard supervised fine-tuning (SFT) assigns the same explicit loss weight to every expert demonstration, regardless of the model's changing competence over training queries. Reinforcement learning (RL) based methods adapt update strength using model-generated rollouts, but often require substantially more sampling and can be unstable on hard tasks. We propose \textbf{Online Self-Weighted Fine-Tuning (OSW-FT)}, a simple method that augments SFT with online, trajectory-level weighting. For each query, OSW-FT estimates the model's current success rate using a small number of inference-only rollouts and rescales the standard SFT loss accordingly. The optimization direction remains anchored to the expert trajectory, while the update magnitude adapts online. For binary-verifiable reasoning, we connect this weighting to SFT and RL at the gradient level, inspired by variance-reduction principles. The resulting estimator is unbiased for the exact OSW-FT surrogate update for any finite rollout count, and we analyze convergence with respect to the corresponding surrogate objective. Evaluated across Qwen3 series ranging from 0.6B to 4B on multiple challenging benchmarks (e.g., AIME), OSW-FT consistently improves over SFT on small-to-medium scale models. OSW-FT offers a favorable compute-performance trade-off as a practical approach for fine-tuning small-to-medium LLMs on binary-verifiable reasoning tasks with only \textbf{2 online rollouts}.

---


### 140. [Escaping Redundant Reasoning: Structure-Aware Search for Inference-Time LLMs](https://arxiv.org/abs/2609.00738)

**<font color=#1a73e8>作者：</font>** Lu Cheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inference-time search with large language models (LLMs) often concentrates on a small set of structurally or semantically similar trajectories, leaving alternatives underexplored---a failure mode we call \textit{reasoning basin collapse}. We introduce BASIN, a training-free, structure-aware selection method that groups reasoning states into basins and penalizes repeated visits to the same strategy, thereby reallocating search across genuinely distinct reasoning paths under a fixed compute budget. Under matched inference budgets, BASIN improves over Tree of Thoughts (ToT) by up to $+22$pp on Game of 24 and $+6.7$pp on MuSR. A quality-aware variant, QA-BASIN, further improves robustness by preserving high-quality basins when unconditional diversification over-explores. To explain when basin-aware selection helps, we introduce the redundancy gap $\Delta$, which measures how differently search concentrates for correct versus incorrect predictions: standard ToT often operates near $\Delta \approx 0$, while BASIN consistently shifts $\Delta$ positive. More broadly, BASIN suggests structure-aware selection as a simple and general approach to improving inference-time reasoning. Code can be found at this https URL.

---


### 141. [Text Capability Loss in Vision-Language Adaptation: An Attention-Sink Diagnosis](https://arxiv.org/abs/2609.00746)

**<font color=#1a73e8>作者：</font>** Minsik Choi, Geewook Kim, Young Geun Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a pretrained LLM into a vision-language model (VLM) can erode the backbone's text capability, with the damage concentrated on tasks that require following exact output rules, such as instruction following, chain-of-thought reasoning graded on a strictly parsed final answer, and similar evaluations with strict graders. We trace this gap to attention-sink corruption: VL fine-tuning perturbs the early sink position that anchors a large fraction of attention probability, and how well the base LLM preserves its sink tracks how much of the affected capability survives adaptation. Building on this view, we introduce Sink Strength, a single scalar computed on the base LLM in a few seconds on a single GPU that predicts post-VL degradation without any VL training. It consistently tracks relative degradation across the six VLM-LLM pairs and multiple format-sensitive tasks. Complementing this diagnostic, we find that post-pretraining QK-RMSNorm injection fails to reproduce the protection of native QK-RMSNorm, while several off-the-shelf weight-merging settings fail to recover the lost capability after VL training. These negative results underscore the value of screening backbones with Sink Strength before VL training and narrow the intervention space toward head-selective training-time protection.

---


### 142. [Can Large Language Models Forecast What Researchers Study Next?](https://arxiv.org/abs/2609.00747)

**<font color=#1a73e8>作者：</font>** Fenghai Li, Zihan Tang, Haofei Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly generate research ideas, yet judging their novelty or feasibility at generation time does not establish whether they anticipate subsequent work. We introduce IdeaForecastBench to evaluate research idea forecasting. Given a community's literature up to a cutoff, a system produces up to five ranked ideas, which are evaluated against later papers. The benchmark comprises 624 rolling episodes across 52 topics, with a fixed retrieve-then-judge protocol and separately reported results from two judges. We compare five history-compression strategies across GPT-4.1, Qwen2.5-7B/14B, and Qwen3.5-9B, together with a learned Mode-Decomposition Forecaster (MDF). Under the primary GPT-4.1-mini judge, Summary improves on Direct in Hit@5 and Precision@5 across all four backbones. Qwen2.5 scores above GPT-4.1, whereas Qwen3.5 scores below it. An outcome-blind assessment finds that Qwen2.5 produces broader forecasts, but does not identify how much breadth contributes to its advantage. Threshold and judge diagnostics further clarify the limits of interpreting realization as precise anticipation. IdeaForecastBench provides a common task for studying which research ideas a community subsequently pursues and how reliably this outcome can be measured.

---


### 143. [ContextPipe: Database-Inspired Context Assembly for Long-Horizon Agents](https://arxiv.org/abs/2609.00749)

**<font color=#1a73e8>作者：</font>** Peng Xu, Zuyu Zhang, Yuze Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon large language model (LLM) agents require context assembly: the runtime must decide what to include in each prompt, in what order, and when to compact history under a hard context-window budget and a byte-sensitive prompt cache. In production agentic systems, this logic is scattered across prompt builders, ad hoc compaction routines, cache-break workarounds, and per-provider shims. We argue that context assembly is structurally isomorphic to query execution in a relational database: both execute under a hard budget, exploit a tiered cache, and leverage statistics. We adopt this discipline in ContextPipe: a five-phase pipeline (Plan Bind Optimize Execute Feedback) backed by a structured data-source catalog, a deterministic cache-aware optimizer, and an EXPLAIN ANALYZE trace. We show that context in ContextPipe is auditable, replayable, and failure-isolated. A preliminary evaluation using the SWE-bench Pro Qutebrowser subset shows that, compared with the append-only context construction policy, ContextPipe reduces total token volume by 31%, LLM calls by 23%, and response time by 9%, at the cost of a lower KV cache-hit ratio.

---


### 144. [How Do Language Models Choose Between Context and Memory?](https://arxiv.org/abs/2609.00753)

**<font color=#1a73e8>作者：</font>** Benjamin Shih, John Winnicki, Arianna Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When contextual information conflicts with the knowledge stored in model parameters, activation directions can be used to decode and steer which source the model follows. However, steering along a direction does not establish causality: whether the unedited model would naturally use that direction or whether the direction is reusable across tasks. We test these distinctions through counterfactual experiments in unambiguous settings. First, we estimate authority directions from agreement prompts, in which the context and parametric knowledge support the same answer. We then interchange naturally occurring coordinates along these directions between matched prompts that direct the model to prioritize either the supplied context or its parametric knowledge. Across Qwen, Llama, and OLMo models, this intervention reproduces 30-68% of the authority-induced shift in source choice, whereas matched controls reproduce almost none. To test cross-task reuse, we learn authority directions on two tasks separately and see that cross-task transferability closes only 9% of the authority gap while the local direction learned on the given task closes 57%. These results distinguish authority representation, causal use, and cross-task causal reuse, and suggest that authority computations may be task-dependent, rather than reusable across tasks.

---


### 145. [S^3martCirc: Self-supervised Smart Circuit Discovery](https://arxiv.org/abs/2609.00755)

**<font color=#1a73e8>作者：</font>** Wendy Zheng, Yinhan He, Liang Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable performance across diverse tasks, from text summarization to question answering. Despite these capabilities, their black-box nature obscures internal decision-making processes. Mechanistic interpretability (MI) aims to address this by reverse-engineering neural networks into human-understandable algorithms. Current MI approaches for LLMs typically follow a two-stage paradigm: first identifying important components (circuit discovery), where components are typically individual nodes such as an attention head or feedforward neuron, and second determining the role they play in a certain task (functional interpretation). However, this sequential approach overlooks a fundamental insight: a component's importance and its functional role are inherently codependent. Unifying these stages presents two key challenges: (1) functional roles are often tied to specific nodes or components, limiting generalization, and (2) their identification relies on subjective interpretation rather than quantifiable metrics. To address these challenges, we propose S^3martCirc (Self-supervised Smart Circuit Discovery), a unified framework that simultaneously discovers circuits and interprets functionality. S^3martCirc abstracts node behavior into two general computational roles that generalize across tasks and defines a quantitative metric for assigning them, enabling importance and functional role to be discovered jointly rather than in sequence. Extensive experiments show that our framework outperforms existing methods in circuit discovery.

---


### 146. [Joint Training Is Not Enough: Conditioned Cross-Granularity Training for Multimodal Document Understanding](https://arxiv.org/abs/2609.00756)

**<font color=#1a73e8>作者：</font>** Chengguang Gan, Yunhao Liang, Hanjun Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Mutual Reinforcement Effect (MRE) asks whether a fine, span-level and a coarse, document-level task help each other when one model handles both. We test it in multimodal document understanding on three corpora, two of receipts and one of scanned business forms, comparing single-task, joint and conditioned training, which puts one granularity's gold output in the other's prompt during training only. We build Doc-MRE, an annotation layer pairing gold field extraction (point) with four document-level facets (line), from a three-judge LLM committee under a pre-registration, validated by blind re-annotation. One predicate, fixed in advance: at a shared recipe, a regime reinforces if it beats the matched single-task model on both granularities. Mixed joint training, the arrangement prior MRE work assumes, reinforces on no corpus at the main scale: it is below both single-task models on CORD and trades one granularity for the other on the two others, as single-task tuning does. Conditioned training reinforces on two of the three, CORD (+0.5 point, +4.8 line) and the forms corpus (+7.2 point, +11.0 line), resolvably on the coarse side and directionally on the fine one, and trades on WildReceipt; at that recipe no alternative measurably beats it on either side anywhere. Two byte-identical-prompt controls separate content from format: shuffled conditioning destroys the coarse-side skill but costs the fine side far less, and a neutral-content control reproduces the whole fine-side gain on WildReceipt, which is therefore prompt structure but buys nothing resolvable on the other two. On the forms corpus conditioning buys collapse avoidance: mixed training and the neutral control both assign the majority semantic label to all 50 test documents; only conditioning recovers the gold distribution. Probes find the information decodable under every regime with no resolvable increase under conditioning.

---


### 147. [Compile, Don't Memorize: A Context Compilation Architecture (CCA) for In-Context Learning](https://arxiv.org/abs/2609.00759)

**<font color=#1a73e8>作者：</font>** Jinhu Qi, Minda Hu, Wentao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly handle in-context learning (ICL) tasks where a long, novel context defines the rules, knowledge, and output schema for a series of questions. On benchmarks that grade against every detail of the context, even strong open-weights models pass only 12-16% of tasks: a single overlooked rule fails the whole response. We argue this brittleness is structural: the dominant "read-and-reason" paradigm asks the model to extract, plan, generate, and self-verify in one forward pass. We therefore ask whether explicit context compilation can fix it, how it compares to existing long-context strategies (gist retrieval, multi-agent self-play), and where the resulting harness benefit holds across task structure and model scale. We propose the Context Compilation Architecture (CCA), whose central novelty is a typed intermediate representation (IR) with fixed slots (rules.{must_do, must_not, conditional}, output_spec, available_tools, data_profile) into which any prose context is compiled once; executable verifiers and a violation-gated correction loop follow as downstream consequences. On CL-bench (1,899 tasks across 4 open base models), CCA outperforms vanilla prompting and two long-context baselines (ReadAgent-P, Ctx2Skill) on every base model, lifting Kimi K2.5 from 15.4% to 21.4% with gains concentrated on rule-dense sub-categories. Code and cached completions are available at this https URL.

---


### 148. [A Unified Mechanistic Analysis of Knowledge- and Safety-Based Refusals](https://arxiv.org/abs/2609.00760)

**<font color=#1a73e8>作者：</font>** Yuri Son, Seunghee Kim, Hyuhng Joon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly trained to decline queries that fall outside their knowledge (knowledge-based refusal, KR) or violate safety policies (safety-based refusal, SR). Although KR and SR result in superficially similar responses, they have largely been studied in isolation, leaving open whether they share an underlying mechanism. We address this gap with a systematic study on a new dataset of 213 contrastive quadruples that jointly probe both refusal types. We find that KR and SR are governed by overlapping yet distinguishable mechanisms. Both share a refusal direction, yet the overlap is asymmetric: SR signals transfer more strongly to KR than the reverse. Type-specific specialization emerges mainly in upper layers, with KR aligning with uncertainty- and knowledge-related representations and SR with safety- and policy-related ones. We thus characterize refusal as a commit-then-specify process: a shared initial mechanism commits to refusing, then type-specific features in later layers specify whether the grounds are epistemic or normative.

---


### 149. [Frozen Cores Need Task Signal: Fisher-Whitened Cross-Covariance for Low-Resource LLM Adaptation](https://arxiv.org/abs/2609.00762)

**<font color=#1a73e8>作者：</font>** Wentao Ye, Zhanming Shen, Zhiqing Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning is usually framed as a question of how many parameters to update. Under a severe trainable-state budget, however, where those coefficients act is equally consequential. We study this choice through frozen-core adaptation: a calibration pass fixes left and right bases for each weight matrix, and fine-tuning optimizes only an $r\times r$ core. This removes the ability of trainable factors to repair a poor initial span and makes subspace quality directly observable. We introduce FCCA, which estimates the signed input--error cross-covariance, whitens it with diagonal Fisher moments, truncates it in the resulting local metric, maps the selected directions back, and applies thin QR to obtain stable core coordinates. Under a matched $r^2$ budget, we compare eight basis constructors on 11 tasks, four model settings, and three seeds. On Qwen2.5-3B, FCCA reaches an 83.0 macro-average, 2.3 points above the next-best matched-budget constructor, and exceeds its unwhitened RawGrad control on all 11 tasks. It ranks first at all three Qwen scales and finishes within 0.13 points of the best method on Llama-3.2-1B. Controlled ablations show gains of 2.7--17.2 points from whitening and identify QR as necessary for stable core optimization in the tested regime. Finally, FCCA comes within 0.32 and 0.23 average points of LoRA and DoRA while optimizing 36.9K rather than roughly 7.4M parameters. These results show that a carefully selected fixed span can recover most of the benefit of movable low-rank factors at a much smaller trainable and optimizer-state cost.

---


### 150. [Automated Tree Knowledge Graph Construction using Ontology Expansion and Retrieval from Vietnamese History Textbooks](https://arxiv.org/abs/2609.00763)

**<font color=#1a73e8>作者：</font>** Ket Doan Nguyen, Minh N. H. Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hierarchical Knowledge graph (KG)-based retrieval augmented generation (RAG) has emerged as a powerful approach for supporting large language models with structured knowledge. However, there are primary challenges: (i) the lack of methods for automatic KG construction using ontology expansion for low-resource languages such as Vietnamese, (ii) the absence of systematic evaluation for knowledge retrieval strategies leveraging the hierarchical structures. In this paper, we propose an end-to-end pipeline for KG construction and retrieval strategies evaluation. In the KG construction, we employ a three-phase hybrid relation extraction pipeline: intra-batch deduplication via Union-Find, approximate cross-batch search, and LLM extraction with a centroid filter that reduces prompts combined with a five-step dual-LLM validator to prevent bloated ontology. A two-tier architecture consists of unmergeable structural nodes to preserve the document structure and mergeable content nodes. The retrieval evaluation consists of three graph traversal strategies: Top-Down, Horizontal, and Bottom-Up, which are evaluated on a synthetically generated benchmark of 1,210 Vietnamese queries from 109 subgraphs, categorized by five query directions. In this paper, we construct the tree knowledge graph from Vietnamese high school History textbooks (nearly 400 pages) to produce 750 nodes and 4,341 semantic edges with controlled ontology growth from 40 to 41 types. Among experimental graph traversal strategies, the Top-Down strategy with structure surpasses the vector baseline by 4.7 percentage points in NDCG@10. As a result, tree-structural information provides valuable information beyond flat cosine similarity but degrades performance when the query does not require structural context.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-295](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
