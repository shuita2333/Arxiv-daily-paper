# 🧠 大模型相关研究 | 2026年04月18日

> 本类共 **143** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

---

### 1. [Compressed-Sensing-Guided, Inference-Aware Structured Reduction for Large Language Models](https://arxiv.org/abs/2604.14156)

**<font color=#1a73e8>作者：</font>** Andrew Kiruluta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models deliver strong generative performance but at the cost of massive parameter counts, memory use, and decoding latency. Prior work has shown that pruning and structured sparsity can preserve accuracy under substantial compression, while prompt-compression methods reduce latency by removing redundant input tokens. However, these two directions remain largely separate. Most model-compression methods are static and optimized offline, and they do not exploit the fact that different prompts and decoding steps activate different latent computational pathways. Prompt-compression methods reduce sequence length, but they do not adapt the executed model subnetwork.
We propose a unified compressed-sensing-guided framework for dynamic LLM execution. Random measurement operators probe latent model usage, sparse recovery estimates task-conditioned and token-adaptive support sets, and the recovered supports are compiled into hardware-efficient sparse execution paths over blocks, attention heads, channels, and feed-forward substructures. The framework introduces five key contributions: task-conditioned measurements, so different prompts induce different sparse supports; token-adaptive recovery, so active substructures are re-estimated during decoding; formal sample-complexity bounds under restricted isometry or mutual incoherence assumptions; compile-to-hardware constraints that restrict recovery to GPU-efficient structures; and a joint objective that unifies prompt compression with model reduction. Together, these components recast LLM inference as a measurement-and-recovery problem with explicit approximation guarantees and deployment-oriented speedup constraints.

---


### 2. [MemGround: Long-Term Memory Evaluation Kit for Large Language Models in Gamified Scenarios](https://arxiv.org/abs/2604.14158)

**<font color=#1a73e8>作者：</font>** Yihang Ding, Wanke Xia, Yiting Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current evaluations of long-term memory in LLMs are fundamentally static. By fixating on simple retrieval and short-context inference, they neglect the multifaceted nature of complex memory systems, such as dynamic state tracking and hierarchical reasoning in continuous interactions. To overcome these limitations, we propose MemGround, a rigorous long-term memory benchmark natively grounded in rich, gamified interactive scenarios. To systematically assess these capabilities, MemGround introduces a three-tier hierarchical framework that evaluates Surface State Memory, Temporal Associative Memory, and Reasoning-Based Memory through specialized interactive tasks. Furthermore, to comprehensively quantify both memory utilization and behavioral trajectories, we propose a multi-dimensional metric suite comprising Question-Answer Score (QA Overall), Memory Fragments Unlocked (MFU), Memory Fragments with Correct Order (MFCO), and Exploration Trajectory Diagrams (ETD). Extensive experiments reveal that state-of-the-art LLMs and memory agents still struggle with sustained dynamic tracking, temporal event association, and complex reasoning derived from long-term accumulated evidence in interactive environments.

---


### 3. [HUOZIIME: An On-Device LLM-enhanced Input Method for Deep Personalization](https://arxiv.org/abs/2604.14159)

**<font color=#1a73e8>作者：</font>** Baocai Shan, Yuzhuang Xu, Wanxiang Che  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mobile input method editors (IMEs) are the primary interface for text input, yet they remain constrained to manual typing and struggle to produce personalized text. While lightweight large language models (LLMs) make on-device auxiliary generation feasible, enabling deeply personalized, privacy-preserving, and real-time generative IMEs poses fundamental this http URL this end, we present HUOZIIME, a personalized on-device IME powered by LLM. We endow HUOZIIME with initial human-like prediction ability by post-training a base LLM on synthesized personalization data. Notably, a hierarchical memory mechanism is designed to continually capture and leverage user-specific input history. Furthermore, we perform systemic optimizations tailored to on-device LLMbased IME deployment, ensuring efficient and responsive operation under mobile this http URL demonstrate efficient on-device execution and high-fidelity memory-driven personalization. Code and package are available at this https URL.

---


### 4. [Can Large Language Models Detect Methodological Flaws? Evidence from Gesture Recognition for UAV-Based Rescue Operation Based on Deep Learning](https://arxiv.org/abs/2604.14161)

**<font color=#1a73e8>作者：</font>** Domonkos Varga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation is essential in machine learning research, yet methodological flaws-particularly data leakage-continue to undermine the validity of reported results. In this work, we investigate whether large language models (LLMs) can act as independent analytical agents capable of identifying such issues in published studies. As a case study, we analyze a gesture-recognition paper reporting near-perfect accuracy on a small, human-centered dataset. We first show that the evaluation protocol is consistent with subject-level data leakage due to non-independent training and test splits. We then assess whether this flaw can be detected independently by six state-of-the-art LLMs, each analyzing the original paper without prior context using an identical prompt. All models consistently identify the evaluation as flawed and attribute the reported performance to non-independent data partitioning, supported by indicators such as overlapping learning curves, minimal generalization gap, and near-perfect classification results. These findings suggest that LLMs can detect common methodological issues based solely on published artifacts. While not definitive, their consistent agreement highlights their potential as complementary tools for improving reproducibility and supporting scientific auditing.

---


### 5. [SeaAlert: Critical Information Extraction From Maritime Distress Communications with Large Language Models](https://arxiv.org/abs/2604.14163)

**<font color=#1a73e8>作者：</font>** Tomer Atia, Yehudit Aperstein, Alexander Apartsin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Maritime distress communications transmitted over very high frequency (VHF) radio are safety-critical voice messages used to report emergencies at sea. Under the Global Maritime Distress and Safety System (GMDSS), such messages follow standardized procedures and are expected to convey essential details, including vessel identity, position, nature of the distress, and required assistance. In practice, however, automatic analysis remains difficult because distress messages are often brief, noisy, and produced under stress, may deviate from the prescribed format, and are further degraded by automatic speech recognition (ASR) errors caused by channel noise and speaker stress. This paper presents SeaAlert, an LLM-based framework for robust analysis of maritime distress communications. To address the scarcity of labeled real-world data, we develop a synthetic data generation pipeline in which an LLM produces realistic and diverse maritime messages, including challenging variants in which standard distress codewords are omitted or replaced with less explicit expressions. The generated utterances are synthesized into speech, degraded with simulated VHF noise, and transcribed by an ASR system to obtain realistic noisy transcripts.

---


### 6. [How to Fine-Tune a Reasoning Model? A Teacher-Student Cooperation Framework to Synthesize Student-Consistent SFT Data](https://arxiv.org/abs/2604.14164)

**<font color=#1a73e8>作者：</font>** Zixian Huang, Kaichen Yang, Xu Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A widely adopted strategy for model enhancement is to use synthetic data generated by a stronger model for supervised fine-tuning (SFT). However, for emerging reasoning models like Qwen3-8B, this approach often fails to improve reasoning capabilities and can even lead to a substantial drop in performance. In this work, we identify substantial stylistic divergence between teacher generated data and the distribution of student as a major factor impacting SFT. To bridge this gap, we propose a Teacher-Student Cooperation Data Synthesis framework (TESSY), which interleaves teacher and student models to alternately generate style and non-style tokens. Consequently, TESSY produces synthetic sequences that inherit the advanced reasoning capabilities of the teacher while maintaining stylistic consistency with the distribution of the student. In experiments on code generation using GPT-OSS-120B as the teacher, fine-tuning Qwen3-8B on teacher-generated data leads to performance drops of 3.25% on LiveCodeBench-Pro and 10.02% on OJBench, whereas TESSY achieves improvements of 11.25% and 6.68%.

---


### 7. [Hierarchical Retrieval Augmented Generation for Adversarial Technique Annotation in Cyber Threat Intelligence Text](https://arxiv.org/abs/2604.14166)

**<font color=#1a73e8>作者：</font>** Filippo Morbiato, Markus Keller, Priya Nair 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mapping Cyber Threat Intelligence (CTI) text to MITRE ATT\&CK technique IDs is a critical task for understanding adversary behaviors and automating threat defense. While recent Retrieval-Augmented Generation (RAG) approaches have demonstrated promising capabilities in this domain, they fundamentally rely on a flat retrieval paradigm. By treating all techniques uniformly, these methods overlook the inherent taxonomy of the ATT\&CK framework, where techniques are structurally organized under high-level tactics. In this paper, we propose H-TechniqueRAG, a novel hierarchical RAG framework that injects this tactic-technique taxonomy as a strong inductive bias to achieve highly efficient and accurate annotation. Our approach introduces a two-stage hierarchical retrieval mechanism: it first identifies the macro-level tactics (the adversary's technical goals) and subsequently narrows the search to techniques within those tactics, effectively reducing the candidate search space by 77.5\%. To further bridge the gap between retrieval and generation, we design a tactic-aware reranking module and a hierarchy-constrained context organization strategy that mitigates LLM context overload and improves reasoning precision. Comprehensive experiments across three diverse CTI datasets demonstrate that H-TechniqueRAG not only outperforms the state-of-the-art TechniqueRAG by 3.8\% in F1 score, but also achieves a 62.4\% reduction in inference latency and a 60\% decrease in LLM API calls. Further analysis reveals that our hierarchical structural priors equip the model with superior cross-domain generalization and provide security analysts with highly interpretable, step-by-step decision paths.

---


### 8. [Chinese Essay Rhetoric Recognition Using LoRA, In-context Learning and Model Ensemble](https://arxiv.org/abs/2604.14167)

**<font color=#1a73e8>作者：</font>** Yuxuan Lai, Xiajing Wang, Chen Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rhetoric recognition is a critical component in automated essay scoring. By identifying rhetorical elements in student writing, AI systems can better assess linguistic and higher-order thinking skills, making it an essential task in the area of AI for education. In this paper, we leverage Large Language Models (LLMs) for the Chinese rhetoric recognition task. Specifically, we explore Low-Rank Adaptation (LoRA) based fine-tuning and in-context learning to integrate rhetoric knowledge into LLMs. We formulate the outputs as JSON to obtain structural outputs and translate keys to Chinese. To further enhance the performance, we also investigate several model ensemble methods. Our method achieves the best performance on all three tracks of CCL 2025 Chinese essay rhetoric recognition evaluation task, winning the first prize.

---


### 9. [Chronological Knowledge Retrieval: A Retrieval-Augmented Generation Approach to Construction Project Documentation](https://arxiv.org/abs/2604.14169)

**<font color=#1a73e8>作者：</font>** Ioannis-Aris Kostis, Natalia Sanchiz, Steeve De Schryver 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In large-scale construction projects, the continuous evolution of decisions generates extensive records, most often captured in meeting minutes. Since decisions may override previous ones, professionals often need to reconstruct the history of specific choices. Retrieving such information manually from raw archives is both labor-intensive and error-prone. From a user perspective, we address this challenge by enabling conversational access to the whole set of project meeting minutes. Professionals can pose natural-language questions and receive answers that are both semantically relevant and explicitly time-annotated, allowing them to follow the chronology of decisions. From a technical perspective, our solution employs a Retrieval-Augmented Generation (RAG) framework that integrates semantic search with large language models to ensure accurate and context-aware responses. We demonstrate the approach using an anonymized, industry-sourced dataset of meeting minutes from a completed construction project by a large company in Belgium. The dataset is annotated and enriched with expert-defined queries to support systematic evaluation. Both the dataset and the open-source implementation are made available to the community to foster further research on conversational access to time-annotated project documentation.

---


### 10. [Stateful Evidence-Driven Retrieval-Augmented Generation with Iterative Reasoning](https://arxiv.org/abs/2604.14170)

**<font color=#1a73e8>作者：</font>** Qi Dong, Ziheng Lin, Ning Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) grounds Large Language Models (LLMs) in external knowledge but often suffers from flat context representations and stateless retrieval, leading to unstable performance. We propose Stateful Evidence-Driven RAG with Iterative Reasoning, a framework that models question answering as a progressive evidence accumulation process. Retrieved documents are converted into structured reasoning units with explicit relevance and confidence signals and maintained in a persistent evidence pool capturing both supportive and non-supportive information. The framework performs evidence-driven deficiency analysis to identify gaps and conflicts and iteratively refines queries to guide subsequent retrieval. This iterative reasoning process enables stable evidence aggregation and improves robustness to noisy retrieval. Experiments on multiple question answering benchmarks demonstrate consistent improvements over standard RAG and multi-step baselines, while effectively accumulating high-quality evidence and maintaining stable performance under substantial retrieval noise.

---


### 11. [Benchmarking Linguistic Adaptation in Comparable-Sized LLMs: A Study of Llama-3.1-8B, Mistral-7B-v0.1, and Qwen3-8B on Romanized Nepali](https://arxiv.org/abs/2604.14171)

**<font color=#1a73e8>作者：</font>** Ananda Rimal, Adarsha Rimal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Romanized Nepali, the Nepali language written in the Latin alphabet, is the dominant medium for informal digital communication in Nepal, yet it remains critically underresourced in the landscape of Large Language Models (LLMs). This study presents a systematic benchmarking of linguistic adaptation across three comparable-sized open-weight models: Llama-3.1-8B, Mistral-7B-v0.1, and Qwen3-8B. We evaluate these architectures under zero-shot and fine-tuned settings using a curated bilingual dataset of 10,000 transliterated instruction-following samples. Performance is quantified across five metrics spanning seven measurement dimensions: Perplexity (PPL), BERTScore, chrF++, ROUGE-1, ROUGE-2, ROUGE-L, and BLEU, capturing fluency, phonetic consistency, and semantic integrity. Models were fine-tuned using Quantized Low-Rank Adaptation (QLoRA) with Rank-Stabilized LoRA (rsLoRA) at rank r=32 on dual NVIDIA Tesla T4 GPUs, training only approximately 1% of each model's parameters in under 27 total GPU-hours. At zero-shot, all three models fail to generate Romanized Nepali, each exhibiting a distinct architecture-specific failure mode. Following fine-tuning, all three resolve these failures and converge to BERTScore approximately 0.75 and chrF++ greater than 23. Overall dimension-wise assessment across ten criteria identifies Qwen3-8B as the overall recommended architecture, being the only model to produce semantically relevant zero-shot output and leading all structural alignment metrics post-SFT. The adaptation headroom hypothesis is confirmed: Llama-3.1-8B, despite its weakest zero-shot baseline, achieves the largest absolute fine-tuning gains in PPL (Delta = -49.77) and BERTScore (Delta = +0.3287), making it the preferred choice for iterative low-resource development pipelines. This work establishes the first rigorous baseline for Romanized Nepali adaptation in comparable-sized open-weight LLMs.

---


### 12. [Tug-of-War within A Decade: Conflict Resolution in Vulnerability Analysis via Teacher-Guided Retrieval-Augmented Generations](https://arxiv.org/abs/2604.14172)

**<font color=#1a73e8>作者：</font>** Ziyin Zhou, Jianyi Zhang, Xu ji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are essential for analyzing and addressing vulnerabilities in cybersecurity. However, among over 200,000 vulnerabilities were discovered in the past decade, more than 30,000 have been changed or updated. This necessitates frequent updates to the training datasets and internal knowledge bases of LLMs to maintain knowledge consistency. In this paper, we focus on the problem of knowledge discrepancy and conflict within CVE (Common Vulnerabilities and Exposures) detection and analysis. This problem hinders LLMs' ability to retrieve the latest knowledge from original training datasets, leading to knowledge conflicts, fabrications of factually incorrect results, and generation hallucinations. To address this problem, we propose an innovative two-stage framework called CRVA-TGRAG (Conflict Resolution in Vulnerability Analysis via Teacher-Guided Retrieval-Augmented Generation). First, to improve document retrieval accuracy during the retrieval stage, we utilize Parent Document Segmentation and an ensemble retrieval scheme based on semantic similarity and inverted indexing. Second, to enhance LLMs' capabilities based on the retrieval of CVE dataset in generation stage, we employ a teacher-guided preference optimization technique to fine-tune LLMs. Our framework not only enhances the quality of content retrieval through RAG but also leverages the advantages of preference fine-tuning in LLMs to answer questions more effectively and precisely. Experiments demonstrate our method achieves higher accuracy in retrieving the latest CVEs compared to external knowledge bases. In conclusion, our framework significantly mitigates potential knowledge conflicts and inconsistencies that may arise from relying solely on LLMs for knowledge retrieval.

---


### 13. [Correcting Suppressed Log-Probabilities in Language Models with Post-Transformer Adapters](https://arxiv.org/abs/2604.14174)

**<font color=#1a73e8>作者：</font>** Bryan Sanchez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Alignment-tuned language models frequently suppress factual log-probabilities on politically sensitive topics despite retaining the knowledge in their hidden representations. We show that a 786K-parameter (approximately 0.02% of the base model) post-transformer adapter, trained on frozen hidden states, corrects this suppression on 31 ideology-discriminating facts across Qwen3-4B, 8B, and 14B. The adapter memorizes all 15 training facts and generalizes to 11--39% of 16 held-out facts across 5 random splits per scale, with zero knowledge regressions via anchored training. Both gated (SwiGLU) and ungated (linear bottleneck) adapters achieve comparable results; neither consistently outperforms the other (Fisher exact p > 0.09 at all scales). On instruct models, the adapter corrects log-probability rankings. When applied at all token positions during generation, the adapter produces incoherent output; however, when applied only at the current prediction position (last-position-only), the adapter produces coherent, less censored text. A logit-space adapter operating after token projection fails to produce coherent generation at any application mode, suggesting hidden-state intervention is the correct level for generation correction. A previously undocumented silent gradient bug in Apple MLX explains all null results in earlier iterations of this work: the standard pattern nn.value_and_grad(model, fn)(this http URL()) returns zero gradients without error; the correct pattern nn.value_and_grad(model, fn)(model, data) resolves this. We provide a minimal reproduction and discuss implications for other adapter research using MLX.

---


### 14. [QU-NLP at ArchEHR-QA 2026: Two-Stage QLoRA Fine-Tuning of Qwen3-4B for Patient-Oriented Clinical Question Answering and Evidence Sentence Alignment](https://arxiv.org/abs/2604.14175)

**<font color=#1a73e8>作者：</font>** Mohammad AL-Smadi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a unified system addressing both Subtask 3 (answer generation) and Subtask 4 (evidence sentence alignment) of the ArchEHR-QA Shared Task. For Subtask 3, we apply two-stage Quantised Low-Rank Adaptation (QLoRA) to Qwen3-4B loaded in 4-bit NF4 quantisation: first on 30,000 samples from the emrQA-MedSQuAD corpus to establish clinical domain competence, then on the 20 annotated development cases to learn the task-specific output style. Our system achieves an overall score of 32.87 on the official test-2026 split (BLEU = 9.42, ROUGE-L = 27.04, SARI = 55.42, BERTScore = 43.00, AlignScore = 25.28, MEDCON = 37.04). For Subtask 4, we develop a weighted ensemble of three retrieval methods - BM25 with relative thresholding, TF-IDF cosine similarity, and a fine-tuned cross-encoder - to identify note sentences supporting a given gold answer, achieving a micro-F1 of 67.16 on the 100-case test set. Experiments reveal that both subtasks expose the same fundamental challenge: 20 annotated training cases are insufficient to distinguish relevant from irrelevant clinical sentences, pointing to data augmentation as the highest-leverage future direction.

---


### 15. [Listen, Correct, and Feed Back: Spoken Pedagogical Feedback Generation](https://arxiv.org/abs/2604.14177)

**<font color=#1a73e8>作者：</font>** Junhong Liang, Yifan Lu, Ekaterina Kochmar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grammatical error correction (GEC) and explanation (GEE) have made rapid progress, but real teaching scenarios also require \emph{learner-friendly pedagogical feedback} that is actionable, level-appropriate, and encouraging. We introduce \textbf{SPFG} (\textbf{S}poken \textbf{P}edagogical \textbf{F}eedback \textbf{G}eneration), a dataset built based on the Speak \& Improve Challenge 2025 corpus, pairing fluency-oriented transcriptions with GEC targets and \emph{human-verified} teacher-style feedback, including preferred/rejected feedback pairs for preference learning. We study a transcript-based Spoken Grammatical Error Correction (SGEC) setting and evaluate three instruction-tuned LLMs (Qwen2.5, Llama-3.1, and GLM-4), comparing supervised fine-tuning (SFT) with preference-based alignment (using DPO and KTO) for jointly generating corrections and feedback. Results show that SFT provides the most consistent improvements, while DPO/KTO yield smaller or mixed gains, and that correction quality and feedback quality are weakly coupled. Our implementation is available at this https URL.

---


### 16. [Simulating Human Cognition: Heartbeat-Driven Autonomous Thinking Activity Scheduling for LLM-based AI systems](https://arxiv.org/abs/2604.14178)

**<font color=#1a73e8>作者：</font>** Hong Su  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents have demonstrated remarkable capabilities in reasoning and tool use, yet they often suffer from rigid, reactive control flows that limit their adaptability and efficiency. Most existing frameworks rely on fixed pipelines or failure-triggered reflection, causing agents to act impulsively or correct errors only after they occur. In this paper, we introduce Heartbeat-Driven Autonomous Thinking Activity Scheduling, a mechanism that enables proactive, adaptive, and continuous self-regulation. Mirroring the natural rhythm of human cognition, our system employs a periodic ``heartbeat'' mechanism to orchestrate a dynamic repertoire of cognitive modules (e.g., Planner, Critic, Recaller, Dreamer). Unlike traditional approaches that rely on hard-coded symbolic rules or immediate reactive triggers, our scheduler learns to determine when to engage specific thinking activities -- such as recalling memories, summarizing experiences, or strategic planning -- based on temporal patterns and historical context. This functional approach allows cognitive modules to be dynamically added or removed without structural reengineering. Meanwhile, we propose a meta-learning strategy for continual policy adaptation, where the scheduler optimizes its cognitive strategy over time using historical interaction logs. Evaluation results demonstrate that our approach effectively learns to schedule cognitive activities based on historical data and can autonomously integrate new thinking modules.

---


### 17. [An Underexplored Frontier: Large Language Models for Rare Disease Patient Education and Communication -- A scoping review](https://arxiv.org/abs/2604.14179)

**<font color=#1a73e8>作者：</font>** Zaifu Zhan, Yu Hou, Kai Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rare diseases affect over 300 million people worldwide and are characterized by complex care pathways, limited clinical expertise, and substantial unmet communication needs throughout the long patient journey. Recent advances in large language models (LLMs) offer new opportunities to support patient education and communication, yet their application in rare diseases remains unclear.
We conducted a scoping review of studies published between January 2022 and March 2026 across major databases, identifying 12 studies on LLM-based rare disease patient education and communication. Data were extracted on study characteristics, application scenarios, model usage, and evaluation methods, and synthesized using descriptive and qualitative analyses.
The literature is highly recent and dominated by general-purpose models, particularly ChatGPT. Most studies focus on patient question answering using curated question sets, with limited use of real-world data or longitudinal communication scenarios. Evaluations are primarily centered on accuracy, with limited attention to patient-centered dimensions such as readability, empathy, and communication quality. Multilingual communication is rarely addressed.
Overall, the field remains at an early stage. Future research should prioritize patient-centered design, domain-adapted methods, and real-world deployment to support safe, adaptive, and effective communication in rare diseases.

---


### 18. [Internal Knowledge Without External Expression: Probing the Generalization Boundary of a Classical Chinese Language Model](https://arxiv.org/abs/2604.14180)

**<font color=#1a73e8>作者：</font>** Jiuting Chen, Yuan Lian, Hao Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We train a 318M-parameter Transformer language model from scratch on a curated corpus of 1.56 billion tokens of pure Classical Chinese, with zero English characters or Arabic numerals. Through systematic out-of-distribution (OOD) testing, we investigate whether the model can distinguish known from unknown inputs, and crucially, whether it can express this distinction in its generated text.
We find a clear dissociation between internal and external uncertainty. Internally, the model exhibits a perplexity jump ratio of 2.39x between real and fabricated historical events (p = 8.9e-11, n = 92 per group), with semi-fabricated events (real figures + fictional events) showing the highest perplexity (4.24x, p = 1.1e-16), demonstrating genuine factual encoding beyond syntactic pattern matching. Externally, however, the model never learns to express uncertainty: classical Chinese epistemic markers appear at lower rates for OOD questions (3.5%) than for in-distribution questions (8.3%, p = 0.023), reflecting rhetorical conventions rather than genuine metacognition.
We replicate both findings across three languages (Classical Chinese, English, Japanese), three writing systems, and eight models from 110M to 1.56B parameters. We further show that uncertainty expression frequency is determined entirely by training data conventions, with Classical Chinese models showing a "humility paradox" (more hedging for known topics), while Japanese models almost never hedge. We argue that metacognitive expression -- the ability to say "I don't know" -- does not emerge from language modeling alone and requires explicit training signals such as RLHF.

---


### 19. [The PICCO Framework for Large Language Model Prompting: A Taxonomy and Reference Architecture for Prompt Structure](https://arxiv.org/abs/2604.14197)

**<font color=#1a73e8>作者：</font>** David A. Cook  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) performance depends heavily on prompt design, yet prompt construction is often described and applied inconsistently. Our purpose was to derive a reference framework for structuring LLM prompts. This paper presents PICCO, a framework derived through a rigorous synthesis of 11 previously published prompting frameworks identified through a multi-database search. The analysis yields two main contributions. First, it proposes a taxonomy that distinguishes prompt frameworks, prompt elements, prompt generation, prompting techniques, and prompt engineering as related but non-equivalent concepts. Second, it derives a five-element reference architecture for prompt generation: Persona, Instructions, Context, Constraints, and Output (PICCO). For each element, we define its function, scope, and relationship to other elements, with the goal of improving conceptual clarity and supporting more systematic prompt design. Finally, to support application of the framework, we outline key concepts relevant to implementation, including prompting techniques (e.g., zero-shot, few-shot, chain-of-thought, ensembling, decomposition, and self-critique, with selected variants), human and automated approaches to iterative prompt engineering, responsible prompting considerations such as security, privacy, bias, and trust, and priorities for future research. This work is a conceptual and methodological contribution: it formalizes a common structure for prompt specification and comparison, but does not claim empirical validation of PICCO as an optimization method.

---


### 20. [MixAtlas: Uncertainty-aware Data Mixture Optimization for Multimodal LLM Midtraining](https://arxiv.org/abs/2604.14198)

**<font color=#1a73e8>作者：</font>** Bingbing Wen, Sirajul Salekin, Feiyang Kang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain reweighting can improve sample efficiency and downstream generalization, but data-mixture optimization for multimodal midtraining remains largely unexplored. Current multimodal training recipes tune mixtures along a single dimension, typically data format or task type. We introduce MixAtlas, a method that produces benchmark-targeted data recipes that can be inspected, adapted, and transferred to new corpora. MixAtlas decomposes the training corpus along two axes: image concepts (10 visual-domain clusters discovered via CLIP embeddings) and task supervision (5 objective types including captioning, OCR, grounding, detection, and VQA). Using small proxy models (Qwen2-0.5B) paired with a Gaussian-process surrogate and GP-UCB acquisition, MixAtlas searches the resulting mixture space with the same proxy budget as regression-based baselines but finds better-performing mixtures. We evaluate on 10 benchmarks spanning visual understanding, document reasoning, and multimodal reasoning. On Qwen2-7B, optimized mixtures improve average performance by 8.5%-17.6% over the strongest baseline; on Qwen2.5-7B, gains are 1.0%-3.3%. Both settings reach baseline-equivalent training loss in up to 2 times fewer steps. Recipes discovered on 0.5B proxies transfer to 7B-scale training across Qwen model families.

---


### 21. [CROP: Token-Efficient Reasoning in Large Language Models via Regularized Prompt Optimization](https://arxiv.org/abs/2604.14214)

**<font color=#1a73e8>作者：</font>** Deep Shah, Sanket Badhe, Nehal Kathrotia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models utilizing reasoning techniques improve task performance but incur significant latency and token costs due to verbose generation. Existing automatic prompt optimization(APO) frameworks target task accuracy exclusively at the expense of generating long reasoning traces. We propose Cost-Regularized Optimization of Prompts (CROP), an APO method that introduces regularization on response length by generating textual feedback in addition to standard accuracy feedback. This forces the optimization process to produce prompts that elicit concise responses containing only critical information and reasoning. We evaluate our approach on complex reasoning datasets, specifically GSM8K, LogiQA and BIG-Bench Hard. We achieved an 80.6\% reduction in token consumption while maintaining competitive accuracy, seeing only a nominal decline in performance. This presents a pragmatic solution for deploying token-efficient and cost-effective agentic AI systems in production pipelines.

---


### 22. [MEME-Fusion@CHiPSAL 2026: Multimodal Ablation Study of Hate Detection and Sentiment Analysis on Nepali Memes](https://arxiv.org/abs/2604.14218)

**<font color=#1a73e8>作者：</font>** Samir Wagle, Reewaj Khanal, Abiral Adhikari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hate speech detection in Devanagari-scripted social media memes presents compounded challenges: multimodal content structure, script-specific linguistic complexity, and extreme data scarcity in low-resource settings. This paper presents our system for the CHiPSAL 2026 shared task, addressing both Subtask A (binary hate speech detection) and Subtask B (three-class sentiment classification: positive, neutral, negative). We propose a hybrid cross-modal attention fusion architecture that combines CLIP (ViT-B/32) for visual encoding with BGE-M3 for multilingual text representation, connected through 4-head self-attention and a learnable gating network that dynamically weights modality contributions on a per-sample basis. Systematic evaluation across eight model configurations demonstrates that explicit cross-modal reasoning achieves a 5.9% F1-macro improvement over text-only baselines on Subtask A, while uncovering two unexpected but critical findings: English-centric vision models exhibit near-random performance on Devanagari script, and standard ensemble methods catastrophically degrade under data scarcity (N nearly equal to 850 per fold) due to correlated overfitting. The code can be accessed at this https URL

---


### 23. [TOPCELL: Topology Optimization of Standard Cell via LLMs](https://arxiv.org/abs/2604.14237)

**<font color=#1a73e8>作者：</font>** Zhan Song, Yu-Tung Liu, Chen Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transistor topology optimization is a critical step in standard cell design, directly dictating diffusion sharing efficiency and downstream routability. However, identifying optimal topologies remains a persistent bottleneck, as conventional exhaustive search methods become computationally intractable with increasing circuit complexity in advanced nodes. This paper introduces TOPCELL, a novel and scalable framework that reformulates high-dimensional topology exploration as a generative task using Large Language Models (LLMs). We employ Group Relative Policy Optimization (GRPO) to fine-tune the model, aligning its topology optimization strategy with logical (circuit) and spatial (layout) constraints. Experimental results within an industrial flow targeting an advanced 2nm technology node demonstrate that TOPCELL significantly outperforms foundation models in discovering routable, physically-aware topologies. When integrated into a state-of-the-art (SOTA) automation flow for a 7nm library generation task, TOPCELL exhibits robust zero-shot generalization and matches the layout quality of exhaustive solvers while achieving an 85.91x speedup.

---


### 24. [Awakening Dormant Experts:Counterfactual Routing to Mitigate MoE Hallucinations](https://arxiv.org/abs/2604.14246)

**<font color=#1a73e8>作者：</font>** Wentao Hu, Yanbo Zhai, Xiaohui Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) models have achieved remarkable scalability, yet they remain vulnerable to hallucinations, particularly when processing long-tail knowledge. We identify that this fragility stems from static Top-$k$ routing: routers tend to favor high-frequency patterns over rare factual associations. Consequently, ``specialist experts'' possessing critical long-tail knowledge are often assigned low gating scores and remain ``dormant'' -- under-prioritized for specific tokens despite their proven causal importance on other inputs. To address this, we propose Counterfactual Routing (CoR), a training-free inference framework designed to awaken these dormant experts. CoR integrates layer-wise perturbation analysis with the Counterfactual Expert Impact (CEI) metric to dynamically shift computational resources from syntax-dominant to knowledge-intensive layers while maintaining a constant total activation count, effectively retrieving causally decisive experts via virtual ablation. Extensive experiments on TruthfulQA, FACTOR, and TriviaQA demonstrate that CoR improves factual accuracy by 3.1\% on average without increasing the inference budget, establishing a superior Pareto frontier compared to static scaling strategies.

---


### 25. [GFT: From Imitation to Reward Fine-Tuning with Unbiased Group Advantages and Dynamic Coefficient Rectification](https://arxiv.org/abs/2604.14258)

**<font color=#1a73e8>作者：</font>** Wangjie Gan, Miao Pan, Linbo Xi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are typically post-trained using supervised fine-tuning (SFT) and reinforcement learning (RL), yet effectively unifying efficient knowledge injection with robust generalization remains challenging. In this work, we provide a training-dynamics analysis showing that SFT can be interpreted as a special case of policy gradient optimization with an extremely sparse implicit reward and unstable inverse-probability weighting, which together lead to single-path dependency, entropy collapse, and gradient explosion. Motivated by this diagnosis, we propose Group Fine-Tuning (GFT), a unified post-training framework that addresses these intrinsic limitations through two mechanisms: Group Advantage Learning, which constructs diverse response groups and derives normalized contrastive supervision to alleviate reward sparsity, and Dynamic Coefficient Rectification, which adaptively bounds inverse-probability weights to stabilize optimization while preserving efficient knowledge injection. Experiments demonstrate that GFT consistently surpasses SFT-based methods and yields policies that integrate more smoothly with subsequent RL training.

---


### 26. [ReviewGrounder: Improving Review Substantiveness with Rubric-Guided, Tool-Integrated Agents](https://arxiv.org/abs/2604.14261)

**<font color=#1a73e8>作者：</font>** Zhuofeng Li, Yi Lu, Dongfu Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid rise in AI conference submissions has driven increasing exploration of large language models (LLMs) for peer review support. However, LLM-based reviewers often generate superficial, formulaic comments lacking substantive, evidence-grounded feedback. We attribute this to the underutilization of two key components of human reviewing: explicit rubrics and contextual grounding in existing work. To address this, we introduce REVIEWBENCH, a benchmark evaluating review text according to paper-specific rubrics derived from official guidelines, the paper's content, and human-written reviews. We further propose REVIEWGROUNDER, a rubric-guided, tool-integrated multi-agent framework that decomposes reviewing into drafting and grounding stages, enriching shallow drafts via targeted evidence consolidation. Experiments on REVIEWBENCH show that REVIEWGROUNDER, using a Phi-4-14B-based drafter and a GPT-OSS-120B-based grounding stage, consistently outperforms baselines with substantially stronger/larger backbones (e.g., GPT-4.1 and DeepSeek-R1-670B) in both alignment with human judgments and rubric-based review quality across 8 dimensions. The code is available \href{this https URL}{here}.

---


### 27. [Enhancing LLM-based Search Agents via Contribution Weighted Group Relative Policy Optimization](https://arxiv.org/abs/2604.14267)

**<font color=#1a73e8>作者：</font>** Junzhe Wang, Zhiheng Xi, yajie yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Search agents extend Large Language Models (LLMs) beyond static parametric knowledge by enabling access to up-to-date and long-tail information unavailable during pretraining. While reinforcement learning has been widely adopted for training such agents, existing approaches face key limitations: process supervision often suffers from unstable value estimation, whereas outcome supervision struggles with credit assignment due to sparse, trajectory-level rewards. To bridge this gap, we propose Contribution-Weighted GRPO (CW-GRPO), a framework that integrates process supervision into group relative policy optimization. Instead of directly optimizing process rewards, CW-GRPO employs an LLM judge to assess the retrieval utility and reasoning correctness at each search round, producing per-round contribution scores. These scores are used to rescale outcome-based advantages along the trajectory, enabling fine-grained credit assignment without sacrificing optimization stability. Experiments on multiple knowledge-intensive benchmarks show that CW-GRPO outperforms standard GRPO by 5.0\% on Qwen3-8B and 6.3\% on Qwen3-1.7B, leading to more effective search behaviors. Additional analysis reveals that successful trajectories exhibit concentrated contributions across rounds, providing empirical insight into search agent tasks.

---


### 28. [HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268)

**<font color=#1a73e8>作者：</font>** Team HY-World, Chenjie Cao, Xuhui Zuo 等 45 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce HY-World 2.0, a multi-modal world model framework that advances our prior project HY-World 1.0. HY-World 2.0 accommodates diverse input modalities, including text prompts, single-view images, multi-view images, and videos, and produces 3D world representations. With text or single-view image inputs, the model performs world generation, synthesizing high-fidelity, navigable 3D Gaussian Splatting (3DGS) scenes. This is achieved through a four-stage method: a) Panorama Generation with HY-Pano 2.0, b) Trajectory Planning with WorldNav, c) World Expansion with WorldStereo 2.0, and d) World Composition with WorldMirror 2.0. Specifically, we introduce key innovations to enhance panorama fidelity, enable 3D scene understanding and planning, and upgrade WorldStereo, our keyframe-based view generation model with consistent memory. We also upgrade WorldMirror, a feed-forward model for universal 3D prediction, by refining model architecture and learning strategy, enabling world reconstruction from multi-view images or videos. Also, we introduce WorldLens, a high-performance 3DGS rendering platform featuring a flexible engine-agnostic architecture, automatic IBL lighting, efficient collision detection, and training-rendering co-design, enabling interactive exploration of 3D worlds with character support. Extensive experiments demonstrate that HY-World 2.0 achieves state-of-the-art performance on several benchmarks among open-source approaches, delivering results comparable to the closed-source model Marble. We release all model weights, code, and technical details to facilitate reproducibility and support further research on 3D world models.

---


### 29. [EuropeMedQA Study Protocol: A Multilingual, Multimodal Medical Examination Dataset for Language Model Evaluation](https://arxiv.org/abs/2604.14306)

**<font color=#1a73e8>作者：</font>** Francesco Andrea Causio, Vittorio De Vita, Olivia Riccomi 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have demonstrated high proficiency on English-centric medical examinations, their performance often declines when faced with non-English languages and multimodal diagnostic tasks. This study protocol describes the development of EuropeMedQA, the first comprehensive, multilingual, and multimodal medical examination dataset sourced from official regulatory exams in Italy, France, Spain, and Portugal. Following FAIR data principles and SPIRIT-AI guidelines, we describe a rigorous curation process and an automated translation pipeline for comparative analysis. We evaluate contemporary multimodal LLMs using a zero-shot, strictly constrained prompting strategy to assess cross-lingual transfer and visual reasoning. EuropeMedQA aims to provide a contamination-resistant benchmark that reflects the complexity of European clinical practices and fosters the development of more generalizable medical AI.

---


### 30. [DharmaOCR: Specialized Small Language Models for Structured OCR that outperform Open-Source and Commercial Baselines](https://arxiv.org/abs/2604.14314)

**<font color=#1a73e8>作者：</font>** Gabriel Pimenta de Freitas Cardoso, Caio Lucas da Silva Chacon, Jonas Felipe da Fonseca Oliveira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This manuscript introduces DharmaOCR Full and Lite, a pair of specialized small language models (SSLMs) for structured OCR that jointly optimize transcription quality, generation stability, and inference cost. It also presents DharmaOCR-Benchmark, a benchmark that covers printed, handwritten, and legal/administrative documents, and proposes a unified evaluation protocol that measures fidelity and structure while explicitly tracking text degeneration as a first-class benchmark metric (alongside unit cost). Beyond reporting degeneration rates, the manuscript empirically shows degeneration is not merely a quality failure, since it materially worsens production performance by increasing response time, reducing throughput, and inflating computational cost due to abnormally long generations. To the best of the author's knowledge, as a methodological contribution, this is the first application of Direct Preference Optimization (DPO) for OCR, explicitly using degenerate generations as rejected examples to penalize looping behavior. Combined with Supervised Fine-Tuning (SFT) for enforcing a strict JSON schema (header, margin, footer, and text), DPO consistently reduces degeneration rate across model families (up to 87.6% relative) while preserving or improving extraction quality. The resulting models, namely, DharmaOCR Full (7B) and DharmaOCR Lite (3B), set a new state-of-the-art on DharmaOCR-Benchmark, outperforming each open-source and commercial baseline model evaluated regarding extraction quality, reaching 0.925 and 0.911 scores with 0.40% and 0.20% degeneration rates. AWQ quantization reduced up to 22% per-page cost with negligible quality loss, enabling a strong quality-cost trade-off in comparison to proprietary OCR APIs and open-source alternatives.

---


### 31. [Tracking the Temporal Dynamics of News Coverage of Catastrophic and Violent Events](https://arxiv.org/abs/2604.14315)

**<font color=#1a73e8>作者：</font>** Emily Lugos, Maurício Gruppi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The modern news cycle has been fundamentally reshaped by the rapid exchange of information online. As a result, media framing shifts dynamically as new information, political responses, and social reactions emerge. Understanding how these narratives form, propagate, and evolve is essential for interpreting public discourse during moments of crisis. In this study, we examine the temporal and semantic dynamics of reporting for violent and catastrophic events using a large-scale corpus of 126,602 news articles collected from online publishers. We quantify narrative change through publication volume, semantic drift, semantic dispersion, and term relevance. Our results show that sudden events of impact exhibit structured and predictable news-cycle patterns characterized by rapid surges in coverage, early semantic drift, and gradual declines toward the baseline. In addition, our results indicate the terms that are driving the temporal patterns.

---


### 32. [Seeing Through Experts Eyes A Foundational Vision Language Model Trained on Radiologists Gaze and Reasoning](https://arxiv.org/abs/2604.14316)

**<font color=#1a73e8>作者：</font>** Kinhei Lee, Peiyuan Jing, Zhenxuan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large scale vision language models have shown promise in automating chest Xray interpretation, yet their clinical utility remains limited by a gap between model outputs and radiologist reasoning. Most systems optimize for semantic information without emulating how experts visually examine medical images, often overlooking critical findings or diverging from established diagnostic workflows. Radiologists follow structured protocols (e.g., the ABCDEF approach) that ensure all clinically relevant regions are systematically examined, reducing missed findings and supporting reliable diagnostic reasoning. We introduce GazeX, a vision language model that leverages radiologists' eye tracking data as a behavioral prior to model expert diagnostic reasoning. By incorporating gaze trajectories and fixation patterns into pretraining, GazeX learns to follow the spatial and temporal structure of radiologist attention and integrates observations in a clinically meaningful sequence. Using a curated dataset of over 30,000 gaze key frames from five radiologists, we demonstrate that GazeX produces more accurate, interpretable, and expert consistent outputs across radiology report generation, disease grounding, and visual question answering, utilizing 231,835 radiographic studies, 780,014 question answer pairs, and 1,162 image sentence pairs with bounding boxes. Unlike autonomous reporting systems, GazeX produces verifiable evidence artifacts, including inspection trajectories and finding linked localized regions, enabling efficient human verification and safe human AI collaboration. Learning through expert eyes provides a practical route toward more trustworthy, explainable, and diagnostically robust AI systems for radiology and beyond.

---


### 33. [LLM Predictive Scoring and Validation: Inferring Experience Ratings from Unstructured Text](https://arxiv.org/abs/2604.14321)

**<font color=#1a73e8>作者：</font>** Jason Potteiger, Andrew Hong, Ito Zapata  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We tasked GPT-4.1 to read what baseball fans wrote about their game-day experience and predict the overall experience rating each fan gave on a 0-10 survey scale. The model received only the text of a single open-ended response. These AI predictions were compared with the actual experience ratings captured by the survey instrument across approximately 10,000 fan responses from five Major League Baseball teams. In total two-thirds of predicted ratings fell within one point of self-reported fan ratings (67% within +/-1, 36% exact match), and the predicted measurement was near-deterministic across three independent scoring runs (87% exact agreement, 99.9% within +/-1). Predicted ratings aligned most strongly with the overall experience rating (r = 0.82) rather than with any specific aspect of the game-day experience such as parking, concessions, staff, etc. However, predictions were systematically lower than self-reported ratings by approximately one point, and this gap was not driven by any single aspect. Rather, our analysis shows that self-reported ratings capture the fan's verdict, an overall evaluative judgment that integrates the entire experience. While predicted ratings quantify the impact of salient moments characterized as memorable, emotionally intense, unusual, or actionable. Each measure contains information the other misses. These baseline results establish that a simple, unoptimized prompt can directionally predict how fans rate their experience from the text a fan wrote and that a gap between the two numbers can be interpreted as a construct difference worth preserving rather than an error to eliminate.

---


### 34. [Purging the Gray Zone: Latent-Geometric Denoising for Precise Knowledge Boundary Awareness](https://arxiv.org/abs/2604.14324)

**<font color=#1a73e8>作者：</font>** Hao An, Yibin Lou, Jiayi Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often exhibit hallucinations due to their inability to accurately perceive their own knowledge boundaries. Existing abstention fine-tuning methods typically partition datasets directly based on response accuracy, causing models to suffer from severe label noise near the decision boundaries and consequently exhibit high rates of abstentions or hallucinations. This paper adopts a latent space representation perspective, revealing a "gray zone" near the decision hyperplane where internal belief ambiguity constitutes the core performance bottleneck. Based on this insight, we propose the **GeoDe** (**Geo**metric **De**noising) framework for abstention fine-tuning. This method constructs a truth hyperplane using linear probes and performs "geometric denoising" by employing geometric distance as a confidence signal for abstention decisions. This approach filters out ambiguous boundary samples while retaining high-fidelity signals for fine-tuning. Experiments across multiple models (Llama3, Qwen3) and benchmark datasets (TriviaQA, NQ, SciQ, SimpleQA) demonstrate that GeoDe significantly enhances model truthfulness and demonstrates strong generalization in out-of-distribution (OOD) scenarios. Code is available at this https URL.

---


### 35. [Faithfulness Serum: Mitigating the Faithfulness Gap in Textual Explanations of LLM Decisions via Attribution Guidance](https://arxiv.org/abs/2604.14325)

**<font color=#1a73e8>作者：</font>** Bar Alon, Itamar Zimerman, Lior Wolf  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong performance and have revolutionized NLP, but their lack of explainability keeps them treated as black boxes, limiting their use in domains that demand transparency and trust. A promising direction to address this issue is post-hoc text-based explanations, which aim to explain model decisions in natural language. Prior work has focused on generating convincing rationales that appear to be subjectively faithful, but it remains unclear whether these explanations are epistemically faithful, whether they reflect the internal evidence the model actually relied on for its decision. In this paper, we first assess the epistemic faithfulness of LLM-generated explanations via counterfactuals and show that they are often unfaithful. We then introduce a training-free method that enhances faithfulness by guiding explanation generation through attention-level interventions, informed by token-level heatmaps extracted via a faithful attribution method. This method significantly improves epistemic faithfulness across multiple models, benchmarks, and prompts.

---


### 36. [Shuffle the Context: RoPE-Perturbed Self-Distillation for Long-Context Adaptation](https://arxiv.org/abs/2604.14339)

**<font color=#1a73e8>作者：</font>** Zichong Li, Chen Liang, Liliang Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly operate in settings that require reliable long-context understanding, such as retrieval-augmented generation and multi-document reasoning. A common strategy is to fine-tune pretrained short-context models at the target sequence length. However, we find that standard long-context adaptation can remain brittle: model accuracy depends strongly on the absolute placement of relevant evidence, exhibiting high positional variance even when controlling for task format and difficulty.
We propose RoPE-Perturbed Self-Distillation, a training regularizer that improves positional robustness. The core idea is to form alternative "views" of the same training sequence by perturbing its RoPE indices -- effectively moving parts of the context to different positions -- and to train the model to produce consistent predictions across views via self-distillation. This encourages reliance on semantic signals instead of brittle position dependencies. Experiments on long-context adaptation of Llama-3-8B and Qwen-3-4B demonstrate consistent gains on long-context benchmarks, including up to 12.04% improvement on RULER-64K for Llama-3-8B and 2.71% on RULER-256K for Qwen-3-4B after SFT, alongside improved length extrapolation beyond the training context window.

---


### 37. [APEX-MEM: Agentic Semi-Structured Memory with Temporal Reasoning for Long-Term Conversational AI](https://arxiv.org/abs/2604.14362)

**<font color=#1a73e8>作者：</font>** Pratyay Banerjee, Masud Moshtaghi, Shivashankar Subramanian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models still struggle with reliable long-term conversational memory: simply enlarging context windows or applying naive retrieval often introduces noise and destabilizes responses. We present APEX-MEM, a conversational memory system that combines three key innovations: (1) a property graph which uses domain-agnostic ontology to structure conversations as temporally grounded events in an entity-centric framework, (2) append-only storage that preserves the full temporal evolution of information, and (3) a multi-tool retrieval agent that understands and resolves conflicting or evolving information at query time, producing a compact and contextually relevant memory summary. This retrieval-time resolution preserves the full interaction history while suppressing irrelevant details. APEX-MEM achieves 88.88% accuracy on LOCOMO's Question Answering task and 86.2% on LongMemEval, outperforming state-of-the-art session-aware approaches and demonstrating that structured property graphs enable more temporally coherent long-term conversational reasoning.

---


### 38. [The Cost of Language: Centroid Erasure Exposes and Exploits Modal Competition in Multimodal Language Models](https://arxiv.org/abs/2604.14363)

**<font color=#1a73e8>作者：</font>** Akshay Paruchuri, Ishan Chatterjee, Henry Fuchs 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal language models systematically underperform on visual perception tasks, yet the structure underlying this failure remains poorly understood. We propose centroid replacement, collapsing each token to its nearest K-means centroid, as a controlled probe for modal dependence. Across seven models spanning three architecture families, erasing text centroid structure costs 4$\times$ more accuracy than erasing visual centroid structure, exposing a universal imbalance where language representations overshadow vision even on tasks that demand visual reasoning. We exploit this asymmetry through text centroid contrastive decoding, recovering up to +16.9% accuracy on individual tasks by contrastively decoding against a text-centroid-erased reference. This intervention varies meaningfully with training approaches: standard fine-tuned models show larger gains (+5.6% on average) than preference-optimized models (+1.5% on average). Our findings suggest that modal competition is structurally localized, correctable at inference time without retraining, and quantifiable as a diagnostic signal to guide future multimodal training.

---


### 39. [Smart But Not Moral? Moral Alignment In Human-AI Decision-Making](https://arxiv.org/abs/2604.14371)

**<font color=#1a73e8>作者：</font>** Christiane Ernst, Luis Gutmann, Domenique Zipperling 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In high-stakes AI-supported decisions, considerations are not purely technical but involve moral judgments about fairness, responsibility, and harm. While prior research has focused mainly on functional or behavioral alignment, this paper argues that moral alignment may be a more fundamental dimension of human-AI decision-making. Moral alignment is defined as the perceived congruence between the values embedded in an AI system's decision logic and the moral intuitions of stakeholders. Building on Moral Foundations Theory, the paper adopts a multi-stakeholder perspective and highlights why moral (mis)alignment matters for the meaningful integration of AI in sensitive contexts.

---


### 40. [FoodSense: A Multisensory Food Dataset and Benchmark for Predicting Taste, Smell, Texture, and Sound from Images](https://arxiv.org/abs/2604.14388)

**<font color=#1a73e8>作者：</font>** Sabab Ishraq, Aarushi Aarushi, Juncai Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans routinely infer taste, smell, texture, and even sound from food images a phenomenon well studied in cognitive science. However, prior vision language research on food has focused primarily on recognition tasks such as meal identification, ingredient detection, and nutrition estimation. Image-based prediction of multisensory experience remains largely unexplored. We introduce FoodSense, a human-annotated dataset for cross-sensory inference containing 66,842 participant-image pairs across 2,987 unique food images. Each pair includes numeric ratings (1-5) and free-text descriptors for four sensory dimensions: taste, smell, texture, and sound. To enable models to both predict and explain sensory expectations, we expand short human annotations into image-grounded reasoning traces. A large language model generates visual justifications conditioned on the image, ratings, and descriptors. Using these annotations, we train FoodSense-VL, a vision language benchmark model to produce both multisensory ratings and grounded explanations directly from food images. This work connects cognitive science findings on cross-sensory perception with modern instruction tuning for multimodal models and shows that many popular evaluation metrics are insufficient for visually sensory inference.

---


### 41. [Credo: Declarative Control of LLM Pipelines via Beliefs and Policies](https://arxiv.org/abs/2604.14401)

**<font color=#1a73e8>作者：</font>** Duo Lu, Andrew Crotty, Uğur Çetintemel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems are becoming commonplace in domains that require long-lived, stateful decision-making in continuously evolving conditions. As such, correctness depends not only on the output of individual model calls, but also on how to best adapt when incorporating new evidence or revising prior conclusions. However, existing frameworks rely on imperative control loops, ephemeral memory, and prompt-embedded logic, making agent behavior opaque, brittle, and difficult to verify. This paper introduces Credo, which represents semantic state as beliefs and regulates behavior using declarative policies defined over these beliefs. This design supports adaptive, auditable, and composable execution through a database-backed semantic control plane. We showcase these concepts in a decision-control scenario, where beliefs and policies declaratively guide critical execution choices (e.g., model selection, retrieval, corrective re-execution), enabling dynamic behavior without requiring any changes to the underlying pipeline code.

---


### 42. [The Autocorrelation Blind Spot: Why 42% of Turn-Level Findings in LLM Conversation Analysis May Be Spurious](https://arxiv.org/abs/2604.14414)

**<font color=#1a73e8>作者：</font>** Ferdinand M. Schessl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Turn-level metrics are widely used to evaluate properties of multi-turn human-LLM conversations, from safety and sycophancy to dialogue quality. However, consecutive turns within a conversation are not statistically independent -- a fact that virtually all current evaluation pipelines fail to correct for in their statistical inference. We systematically characterize the autocorrelation structure of 66 turn-level metrics across 202 multi-turn conversations (11,639 turn pairs, 5 German-speaking users, 4 LLM platforms) and demonstrate that naive pooled analysis produces severely inflated significance estimates: 42% of associations that appear significant under standard pooled testing fail to survive cluster-robust correction. The inflation varies substantially across categories rather than scaling linearly with autocorrelation: three memoryless families (embedding velocity, directional, differential) aggregate to 14%, while the seven non-memoryless families (thermo-cycle, frame distance, lexical/structural, rolling windows, cumulative, interaction, timestamp) aggregate to 33%, with individual category rates ranging from 0% to 100% depending on per-family effect size. We present a two-stage correction framework combining Chelton (1983) effective degrees of freedom with conversation-level block bootstrap, and validate it on a pre-registered hold-out split where cluster-robust metrics replicate at 57% versus 30% for pooled-only metrics. We provide concrete design principles, a publication checklist, and open-source code for the correction pipeline. A survey of ~30 recent papers at major NLP and AI venues that compute turn-level statistics in LLM evaluations finds that only 4 address temporal dependence at all, and 26 do not correct for it.

---


### 43. [Equifinality in Mixture of Experts: Routing Topology Does Not Determine Language Modeling Quality](https://arxiv.org/abs/2604.14419)

**<font color=#1a73e8>作者：</font>** Ivan Ternovtsii, Yurii Bilak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) architectures employ increasingly sophisticated routing mechanisms -- learned routers, multi-hop trajectories, token-dependent gating. We ask: does routing topology actually determine language modeling quality? We build a geometric MoE (ST-MoE) using cosine-similarity routing against learned centroids in a low-dimensional space ($d_{space} = 64$), requiring 80% fewer routing parameters than standard linear routers. Through 62 controlled experiments on WikiText-103 at 76--84M parameters trained to convergence (50K steps, 1.64B tokens), we find that routing topology does not determine asymptotic perplexity (PPL): five cosine-routing variants are statistically equivalent within a 1-PPL margin (Two One-Sided Tests [TOST], $p < 0.05$ for all 10 pairwise comparisons; 15 runs across 3 seeds, observed range 33.93--34.72). The finding extends to hash, random-fixed, and top-1 routing (single-seed; graceful 1.1--2.2 PPL degradation) and replicates on OpenWebText (0.03 PPL gap, 6 runs, 3 seeds each). A standard linear router with 5.3$\times$ more routing parameters reaches PPL 32.76, but iso-parameter cosine routing closes 67% of this gap -- the true mechanism advantage is $\sim$1.2%. The mechanistic explanation is convergent redundancy: multi-hop updates are collinear ($\cos(\Delta h_0, \Delta h_1) = 0.805$), implementing magnitude amplification rather than compositional reasoning; a single learnable scalar replicates multi-hop performance. As a practical payoff, zero-shot relative-norm halting saves 25% of MoE FLOPs at +0.12% PPL. Expert-level specialization and causal controllability -- which coexist with topology-level equifinality -- are explored in a companion paper.

---


### 44. [Demonstration of Pneuma-Seeker: Agentic System for Reifying and Fulfilling Information Needs on Tabular Data](https://arxiv.org/abs/2604.14422)

**<font color=#1a73e8>作者：</font>** Muhammad Imam Luthfi Balaka, Raul Castro Fernandez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data analysts working with relational data often start with vague or underspecified questions and refine them iteratively as they explore the data. To support this iterative process, we demonstrate Pneuma-Seeker, a system that reifies a user's information need as explicit, inspectable relational specifications, enabling iterative refinement of the information need, targeted data discovery, and provenance-aware execution. Through two real-world procurement use cases, we show how Pneuma-Seeker leverages LLMs as transparent, interactive analytical collaborators rather than opaque answer engines.

---


### 45. [Geometric Routing Enables Causal Expert Control in Mixture of Experts](https://arxiv.org/abs/2604.14434)

**<font color=#1a73e8>作者：</font>** Ivan Ternovtsii, Yurii Bilak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) models scale parameters while fixing active computation per token, but the specialization of individual experts remains opaque. In a companion paper we showed that routing topology is quality-neutral: five structurally different configurations converge to statistically equivalent language modeling quality. Here we show that expert identity is nonetheless causally meaningful: individual rank-1 experts are monosemantic by construction, and cosine-similarity routing in a low-dimensional metric space makes their specialization directly inspectable.
We present four lines of evidence. First, projecting expert output vectors through the unembedding matrix yields a Semantic Dictionary: 15% of experts are monosemantic specialists spanning 10 categories (temporal, geographic, cardinal, discourse, emotional, financial, military, scientific). Second, routing exhibits a frequency-to-syntax gradient: early layers separate tokens by word frequency, deeper layers by syntactic class (Zipf-confound controls, all $p < 0.001$). Third, causal interventions confirm these labels: steering toward a temporal expert's centroid increases P(temporal) by +321% (median across 44 prompts); suppressing a geographic expert drops P(geographic) by -23%; rewriting an expert's output vector halves target-category probability, and effects compose additively across layers. Fourth, the interventions are not unique to cosine routing: linear routers support comparable steering, but only cosine routing provides geometric transparency -- expert specialization is readable directly from the centroid matrix.
MoE expert-level specialization is a first-class interpretability primitive: architecturally monosemantic, causally validated, and controllable at inference with zero overhead.

---


### 46. [MARCA: A Checklist-Based Benchmark for Multilingual Web Search](https://arxiv.org/abs/2604.14448)

**<font color=#1a73e8>作者：</font>** Thales Sales Almeida, Giovana Kerche Bonás, Ramon Pires 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as sources of information, yet their reliability depends on the ability to search the web, select relevant evidence, and synthesize complete answers. While recent benchmarks evaluate web-browsing and agentic tool use, multilingual settings, and Portuguese in particular, remain underexplored. We present \textsc{MARCA}, a bilingual (English and Portuguese) benchmark for evaluating LLMs on web-based information seeking. \textsc{MARCA} consists of 52 manually authored multi-entity questions, paired with manually validated checklist-style rubrics that explicitly measure answer completeness and correctness. We evaluate 14 models under two interaction settings: a Basic framework with direct web search and scraping, and an Orchestrator framework that enables task decomposition via delegated subagents. To capture stochasticity, each question is executed multiple times and performance is reported with run-level uncertainty. Across models, we observe large performance differences, find that orchestration often improves coverage, and identify substantial variability in how models transfer from English to Portuguese. The benchmark is available at this https URL

---


### 47. [AIBuildAI: An AI Agent for Automatically Building AI Models](https://arxiv.org/abs/2604.14455)

**<font color=#1a73e8>作者：</font>** Ruiyi Zhang, Peijia Qin, Qi Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI models underpin modern intelligent systems, driving advances across science, medicine, finance, and technology. Yet developing high-performing AI models remains a labor-intensive process that requires expert practitioners to iteratively design architectures, engineer representations, implement training pipelines and refine approaches through empirical evaluation. Existing AutoML methods partially alleviate this burden but remain limited to narrow aspects such as hyperparameter optimization and model selection within predefined search spaces, leaving the full development lifecycle largely dependent on human expertise. To address this gap, we introduce AIBuildAI, an AI agent that automatically builds AI models from a task description and training data. AIBuildAI adopts a hierarchical agent architecture in which a manager agent coordinates three specialized sub-agents: a designer for modeling strategy, a coder for implementation and debugging, and a tuner for training and performance optimization. Each sub-agent is itself a large language model (LLM) based agent capable of multi-step reasoning and tool use, enabling end-to-end automation of the AI model development process that goes beyond the scope of existing AutoML approaches. We evaluate AIBuildAI on MLE-Bench, a benchmark of realistic Kaggle-style AI development tasks spanning visual, textual, time-series and tabular modalities. AIBuildAI ranks first on MLE-Bench with a medal rate of 63.1%, outperforming all existing baseline methods and matching the capability of highly experienced AI engineers. These results demonstrate that hierarchical agent systems can automate the full AI model development process from task specification to deployable model, suggesting a pathway toward broadly accessible AI development with minimal human intervention.

---


### 48. [Psychological Steering of Large Language Models](https://arxiv.org/abs/2604.14463)

**<font color=#1a73e8>作者：</font>** Leonardo Blas, Robin Jia, Emilio Ferrara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) emulate a consistent human-like behavior that can be shaped through activation-level interventions. This paradigm is converging on additive residual-stream injections, which rely on injection-strength sweeps to approximate optimal intervention settings. However, existing methods restrict the search space and sweep in uncalibrated activation-space units, potentially missing optimal intervention conditions. Thus, we introduce a psychological steering framework that performs unbounded, fluency-constrained sweeps in semantically calibrated units. Our method derives and calibrates residual-stream injections using psychological artifacts, and we use the IPIP-NEO-120, which measures the OCEAN personality model, to compare six injection methods. We find that mean-difference (MD) injections outperform Personality Prompting (P$^2$), an established baseline for OCEAN steering, in open-ended generation in 11 of 14 LLMs, with gains of 3.6\% to 16.4\%, overturning prior reports favoring prompting and positioning representation engineering as a new frontier in open-ended psychological steering. Further, we find that a hybrid of P$^2$ and MD injections outperforms both methods in 13 of 14 LLMs, with gains over P$^2$ ranging from 5.6\% to 21.9\% and from 3.3\% to 26.7\% over MD injections. Finally, we show that MD injections align with the Linear Representation Hypothesis and provide reliable, approximately linear control knobs for psychological steering. Nevertheless, they also induce OCEAN trait covariance patterns that depart from the Big Two model, suggesting a gap between learned representations and human psychology.

---


### 49. [Response-Aware User Memory Selection for LLM Personalization](https://arxiv.org/abs/2604.14473)

**<font color=#1a73e8>作者：</font>** Jillian Fisher, Jennifer Neville, Chan Young Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A common approach to personalization in large language models (LLMs) is to incorporate a subset of the user memory into the prompt at inference time to guide the model's generation. Existing methods select these subsets primarily using similarity between user memory items and input queries, ignoring how features actually affect the model's response distribution. We propose Response-Utility optimization for Memory Selection (RUMS), a novel method that selects user memory items by measuring the mutual information between a subset of memory and the model's outputs, identifying items that reduce response uncertainty and sharpen predictions beyond semantic similarity. We demonstrate that this information-theoretic foundation enables more principled user memory selection that aligns more closely with human selection compared to state-of-the-art methods, and models $400\times$ larger. Additionally, we show that memory items selected using RUMS result in better response quality compared to existing approaches, while having up to $95\%$ reduction in computational cost.

---


### 50. [Scouting By Reward: VLM-TO-IRL-Driven Player Selection For Esports](https://arxiv.org/abs/2604.14474)

**<font color=#1a73e8>作者：</font>** Qing Yan, Wenyu Yang, Yufei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional esports scouting workflows rely heavily on manual video review and aggregate performance metrics, which often fail to capture the nuanced decision-making patterns necessary to determine if a prospect fits a specific tactical archetype. To address this, we reframe style-based player evaluation in esports as an Inverse Reinforcement Learning (IRL) problem. In this paper, we introduce a novel player selection framework that learns professional-specific reward functions from logged gameplay demonstrations, allowing organizations to rank candidates by their stylistic alignment with a target star player. Our proposed architecture utilizes a multimodal, two-branch intake: one branch encodes structured state-action trajectories derived from high-resolution in-game telemetry, while the second encodes temporally aligned tactical pseudo-commentary generated by Vision-Language Models (VLMs) from broadcast footage. These representations are fused and evaluated via a Generative Adversarial Imitation Learning (GAIL) objective, where a discriminator learns to capture the unique mechanical and tactical signatures of elite professionals. By transitioning from generic skill estimation to scouting "by reward," this framework provides a scalable, workflow-aware digital twin system that enables data-driven roster construction and targeted talent discovery across massive candidate pools.

---


### 51. [Evo-MedAgent: Beyond One-Shot Diagnosis with Agents That Remember, Reflect, and Improve](https://arxiv.org/abs/2604.14475)

**<font color=#1a73e8>作者：</font>** Weixiang Shen, Bailiang Jian, Jun Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented large language model (LLM) agents can orchestrate specialist classifiers, segmentation models, and visual question-answering modules to interpret chest X-rays. However, these agents still solve each case in isolation: they fail to accumulate experience across cases, correct recurrent reasoning mistakes, or adapt their tool-use behavior without expensive reinforcement learning. While a radiologist naturally improves with every case, current agents remain static. In this work, we propose Evo-MedAgent, a self-evolving memory module that equips a medical agent with the capacity for inter-case learning at test time. Our memory comprises three complementary stores: (1)~\emph{Retrospective Clinical Episodes} that retrieve problem-solving experiences from similar past cases, (2)~an \emph{Adaptive Procedural Heuristics} bank curating priority-tagged diagnostic rules that evolves via reflection, much like a physician refining their internal criteria, and (3)~a \emph{Tool Reliability Controller} that tracks per-tool trustworthiness. On ChestAgentBench, Evo-MedAgent raises multiple-choice question (MCQ) accuracy from 0.68 to 0.79 on GPT-5-mini, and from 0.76 to 0.87 on Gemini-3 Flash. With a strong base model, evolving memory improves performance more effectively than orchestrating external tools on qualitative diagnostic tasks. Because Evo-MedAgent requires no training, its per-case overhead is bounded by one additional retrieval pass and a single reflection call, making it deployable on top of any frozen model.

---


### 52. [Pushing the Limits of On-Device Streaming ASR: A Compact, High-Accuracy English Model for Low-Latency Inference](https://arxiv.org/abs/2604.14493)

**<font color=#1a73e8>作者：</font>** Nenad Banfic, David Fan, Kunal Vaishnavi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying high-quality automatic speech recognition (ASR) on edge devices requires models that jointly optimize accuracy, latency, and memory footprint while operating entirely on CPU without GPU acceleration. We conduct a systematic empirical study of state-of-the-art ASR architectures, encompassing encoder-decoder, transducer, and LLM-based paradigms, evaluated across batch, chunked, and streaming inference modes. Through a comprehensive benchmark of over 50 configurations spanning OpenAI Whisper, NVIDIA Nemotron, Parakeet TDT, Canary, Conformer Transducer, and Qwen3-ASR, we identify NVIDIA's Nemotron Speech Streaming as the strongest candidate for real-time English streaming on resource-constrained hardware. We then re-implement the complete streaming inference pipeline in ONNX Runtime and conduct a controlled evaluation of multiple post-training quantization strategies, including importance-weighted k-quant, mixed-precision schemes, and round-to-nearest quantization, combined with graph-level operator fusion. These optimizations reduce the model from 2.47 GB to as little as 0.67 GB while maintaining word error rate (WER) within 1% absolute of the full-precision PyTorch baseline. Our recommended configuration, the int4 k-quant variant, achieves 8.20% average streaming WER across eight standard benchmarks, running comfortably faster than real-time on CPU with 0.56 s algorithmic latency, establishing a new quality-efficiency Pareto point for on-device streaming ASR.

---


### 53. [Geometric Metrics for MoE Specialization: From Fisher Information to Early Failure Detection](https://arxiv.org/abs/2604.14500)

**<font color=#1a73e8>作者：</font>** Dongxin Guo, Jikun Wu, Siu Ming Yiu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Expert specialization is fundamental to Mixture-of-Experts (MoE) model success, yet existing metrics (cosine similarity, routing entropy) lack theoretical grounding and yield inconsistent conclusions under reparameterization. We present an information-geometric framework providing the first rigorous characterization of MoE specialization dynamics. Our key insight is that expert routing distributions evolve on the probability simplex equipped with the Fisher information metric, enabling formal analysis via Riemannian geometry. We prove that standard heuristic metrics violate parameterization invariance (Theorem 1), establish that specialization corresponds to geodesic flow with quantified approximation bounds (Theorem 2), and derive a failure predictor with theoretical threshold justification (Theorem 3). The framework introduces two principled metrics: Fisher Specialization Index (FSI) achieving r=0.91+/-0.02 correlation with downstream performance, and Fisher Heterogeneity Score (FHS) predicting training failure at 10% completion with AUC=0.89+/-0.03 -- outperforming validation-loss-based early stopping by 23% while requiring 40x fewer compute cycles. We validate intervention protocols achieving 87% recovery rate when FHS>1 is detected. Comprehensive experiments across language modeling (WikiText-103, C4), vision MoE (ImageNet), and scaling studies (8-64 experts, 125M-2.7B parameters) validate our theoretical predictions.

---


### 54. [Chain of Modality: From Static Fusion to Dynamic Orchestration in Omni-MLLMs](https://arxiv.org/abs/2604.14520)

**<font color=#1a73e8>作者：</font>** Ziyang Luo, Nian Liu, Junwei Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-modal Large Language Models (Omni-MLLMs) promise a unified integration of diverse sensory streams. However, recent evaluations reveal a critical performance paradox: unimodal baselines frequently outperform joint multimodal inference. We trace this perceptual fragility to the static fusion topologies universally employed by current models, identifying two structural pathologies: positional bias in sequential inputs and alignment traps in interleaved formats, which systematically distort attention regardless of task semantics. To resolve this functional rigidity, we propose Chain of Modality (CoM), an agentic framework that transitions multimodal fusion from passive concatenation to dynamic orchestration. CoM adaptively orchestrates input topologies, switching among parallel, sequential, and interleaved pathways to neutralize structural biases. Furthermore, CoM bifurcates cognitive execution into two task-aligned pathways: a streamlined ``Direct-Decide'' path for direct perception and a structured ``Reason-Decide'' path for analytical auditing. Operating in either a training-free or a data-efficient SFT setting, CoM achieves robust and consistent generalization across diverse benchmarks.

---


### 55. [Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning](https://arxiv.org/abs/2604.14525)

**<font color=#1a73e8>作者：</font>** Rohit Kumar Salla, Ramya Manasa Amancherla, Manoj Saravanan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models frequently produce mutually inconsistent answers when reasoning over multiple related queries. We study case-file logical consistency: maintaining a globally satisfiable belief state across interdependent queries. We introduce a benchmark of 390 multi-query reasoning instances with entailment/contradiction/unknown labels and propose set-level metrics including Case Satisfiability Rate, Contradiction Density and Revision Cost. Our solver-augmented approach extracts commitments, verifies global satisfiability and performs counterexample-guided repair. Across four reasoning domains, our method substantially reduces cross-query contradictions (SetCons: 0.56 to 0.94) while preserving per-query accuracy, demonstrating that global coherence is critical for robust multi-query reasoning.

---


### 56. [Dissecting Failure Dynamics in Large Language Model Reasoning](https://arxiv.org/abs/2604.14528)

**<font color=#1a73e8>作者：</font>** Wei Zhu, Jian Zhang, Lixing Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) achieve strong performance through extended inference-time deliberation, yet how their reasoning failures arise remains poorly understood. By analyzing model-generated reasoning trajectories, we find that errors are not uniformly distributed but often originate from a small number of early transition points, after which reasoning remains locally coherent but globally incorrect. These transitions coincide with localized spikes in token-level entropy, and alternative continuations from the same intermediate state can still lead to correct solutions. Based on these observations, we introduce GUARD, a targeted inference-time framework that probes and redirects critical transitions using uncertainty signals. Empirical evaluations across multiple benchmarks confirm that interventions guided by these failure dynamics lead to more reliable reasoning outcomes. Our findings highlight the importance of understanding when and how reasoning first deviates, complementing existing approaches that focus on scaling inference-time computation.

---


### 57. [TRACER: Trace-Based Adaptive Cost-Efficient Routing for LLM Classification](https://arxiv.org/abs/2604.14531)

**<font color=#1a73e8>作者：</font>** Adam Rida  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every call to an LLM classification endpoint produces a labeled input-output pair already retained in production logs. These pairs constitute a free, growing training set: a lightweight surrogate trained on them can absorb a significant portion of future traffic at near-zero marginal inference cost. The open questions are when the surrogate is reliable enough to deploy, what it handles versus defers, and how that boundary evolves as data accumulates.
We introduce TRACER (Trace-based Adaptive Cost-Efficient Routing), an open-source system that trains ML surrogates on an LLM's own production traces and governs deployment through a parity gate: the surrogate is activated only when its agreement with the LLM exceeds a user-specified threshold {\alpha}. To make the routing boundary transparent, TRACER generates interpretability artifacts describing which input regions the surrogate handles, where it plateaus, and why it defers.
On a 77-class intent benchmark with a Sonnet 4.6 teacher, TRACER achieves 83-100% surrogate coverage depending on the quality target {\alpha}; on a 150-class benchmark, the surrogate fully replaces the teacher. On a natural language inference task, the parity gate correctly refuses deployment because the embedding representation cannot support reliable separation. The system is available as open-source software.

---


### 58. [Predicting Post-Traumatic Epilepsy from Clinical Records using Large Language Model Embeddings](https://arxiv.org/abs/2604.14547)

**<font color=#1a73e8>作者：</font>** Wenhui Cui, Nicholas Swingle, Anand A. Joshi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective: Post-traumatic epilepsy (PTE) is a debilitating neurological disorder that develops after traumatic brain injury (TBI). Early prediction of PTE remains challenging due to heterogeneous clinical data, limited positive cases, and reliance on resource-intensive neuroimaging data. We investigate whether routinely collected acute clinical records alone can support early PTE prediction using language model-based approaches. Methods: Using a curated subset of the TRACK-TBI cohort, we developed an automated PTE prediction framework that implements pretrained large language models (LLMs) as fixed feature extractors to encode clinical records. Tabular features, LLM-generated embeddings, and hybrid feature representations were evaluated using gradient-boosted tree classifiers under stratified cross-validation. Results: LLM embeddings achieved performance improvements by capturing contextual clinical information compared to using tabular features alone. The best performance was achieved by a modality-aware feature fusion strategy combining tabular features and LLM embeddings, achieving an AUC-ROC of 0.892 and AUPRC of 0.798. Acute post-traumatic seizures, injury severity, neurosurgical intervention, and ICU stay are key contributors to the predictive performance. Significance: These findings demonstrate that routine acute clinical records contain information suitable for early PTE risk prediction using LLM embeddings in conjunction with gradient-boosted tree classifiers. This approach represents a promising complement to imaging-based prediction.

---


### 59. [Generative Augmented Inference](https://arxiv.org/abs/2604.14575)

**<font color=#1a73e8>作者：</font>** Cheng Lu, Mengxin Wang, Dennis J. Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven operations management often relies on parameters estimated from costly human-generated labels. Recent advances in large language models (LLMs) and other AI systems offer inexpensive auxiliary data, but introduce a new challenge: AI outputs are not direct observations of the target outcomes, but could involve high-dimensional representations with complex and unknown relationships to human labels. Conventional methods leverage AI predictions as direct proxies for true labels, which can be inefficient or unreliable when this relationship is weak or misspecified. We propose Generative Augmented Inference (GAI), a general framework that incorporates AI-generated outputs as informative features for estimating models of human-labeled outcomes. GAI uses an orthogonal moment construction that enables consistent estimation and valid inference with flexible, nonparametric relationship between LLM-generated outputs and human labels. We establish asymptotic normality and show a "safe default" property: relative to human-data-only estimators, GAI weakly improves estimation efficiency under arbitrary auxiliary signals and yields strict gains whenever the auxiliary information is predictive. Empirically, GAI outperforms benchmarks across diverse settings. In conjoint analysis with weak auxiliary signals, GAI reduces estimation error by about 50% and lowers human labeling requirements by over 75%. In retail pricing, where all methods access the same auxiliary inputs, GAI consistently outperforms alternative estimators, highlighting the value of its construction rather than differences in information. In health insurance choice, it cuts labeling requirements by over 90% while maintaining decision accuracy. Across applications, GAI improves confidence interval coverage without inflating width. Overall, GAI provides a principled and scalable approach to integrating AI-generated information.

---


### 60. [Enhancing Mental Health Counseling Support in Bangladesh using Culturally-Grounded Knowledge](https://arxiv.org/abs/2604.14576)

**<font color=#1a73e8>作者：</font>** Md Arid Hasan, Azhagu Meena SP, Aditya Khan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show promise in generating supportive responses for mental health and counseling applications. However, their responses often lack cultural sensitivity, contextual grounding, and clinically appropriate guidance. This work addresses the gap of how to systematically incorporate domain-specific, clinically validated knowledge into LLMs to improve counseling quality. We utilize and compare two approaches, retrieval-augmented generation (RAG) and a knowledge graph (KG)-based method, designed to support para-counselors. Our KG is constructed manually and clinically validated, capturing causal relationships between stressors, interventions, and outcomes, with contributions from multidisciplinary people. We evaluated multiple LLMs in both settings using BERTScore F1 and SBERT cosine similarity, as well as human evaluation across five metrics, which is designed to directly measure the effectiveness of counseling beyond similarity at the surface level. The results show that KG-based approaches consistently improve contextual relevance, clinical appropriateness, and practical usability compared to RAG alone, demonstrating that structured, expert-validated knowledge plays a critical role in addressing LLMs limitations in counseling tasks.

---


### 61. [MapSR: Prompt-Driven Land Cover Map Super-Resolution via Vision Foundation Models](https://arxiv.org/abs/2604.14582)

**<font color=#1a73e8>作者：</font>** Ruiqi Wang, Qi Yu, Jie Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution (HR) land-cover mapping is often constrained by the high cost of dense HR annotations. We revisit this problem from the perspective of map super-resolution, which enhances coarse low-resolution (LR) land-cover products into HR maps at the resolution of the input imagery. Existing weakly supervised methods can leverage LR labels, but they typically use them to retrain dense predictors with substantial computational cost. We propose MapSR, a prompt-driven framework that decouples supervision from model training. MapSR uses LR labels once to extract class prompts from frozen vision foundation model features through a lightweight linear probe, after which HR mapping proceeds via training-free metric inference and graph-based prediction refinement. Specifically, class prompts are estimated by aggregating high-confidence HR features identified by the linear probe, and HR predictions are obtained by cosine-similarity matching followed by graph-based propagation for spatial refinement. Experiments on the Chesapeake Bay dataset show that MapSR achieves 59.64% mIoU without any HR labels, remaining competitive with the strongest weakly supervised baseline and surpassing a fully supervised baseline. Notably, MapSR reduces trainable parameters by four orders of magnitude and shortens training time from hours to minutes, enabling scalable HR mapping under limited annotation and compute budgets. The code is available at this https URL.

---


### 62. [From Risk to Rescue: An Agentic Survival Analysis Framework for Liquidation Prevention](https://arxiv.org/abs/2604.14583)

**<font color=#1a73e8>作者：</font>** Fernando Spadea, Oshani Seneviratne  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized Finance (DeFi) lending protocols like Aave v3 rely on over-collateralization to secure loans, yet users frequently face liquidation due to volatile market conditions. Existing risk management tools utilize static health-factor thresholds, which are reactive and fail to distinguish between administrative "dust" cleanup and genuine insolvency. In this work, we propose an autonomous agent that leverages time-to-event (survival) analysis and moves beyond prediction to execution. Unlike passive risk signals, this agent perceives risk, simulates counterfactual futures, and executes protocol-faithful interventions to proactively prevent liquidations. We introduce a return period metric derived from a numerically stable XGBoost Cox proportional hazards model to normalize risk across transaction types, coupled with a volatility-adjusted trend score to filter transient market noise. To select optimal interventions, we implement a counterfactual optimization loop that simulates potential user actions to find the minimum capital required to mitigate risk. We validate our approach using a high-fidelity, protocol-faithful Aave v3 simulator on a cohort of 4,882 high-risk user profiles. The results demonstrate the agent's ability to prevent liquidations in imminent-risk scenarios where static rules fail, effectively "saving the unsavable" while maintaining a zero worsening rate, providing a critical safety guarantee often missing in autonomous financial agents. Furthermore, the system successfully differentiates between actionable financial risks and negligible dust events, optimizing capital efficiency where static rules fail.

---


### 63. [Mechanistic Decoding of Cognitive Constructs in LLMs](https://arxiv.org/abs/2604.14593)

**<font color=#1a73e8>作者：</font>** Yitong Shou, Manhao Guan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) demonstrate increasingly sophisticated affective capabilities, the internal mechanisms by which they process complex emotions remain unclear. Existing interpretability approaches often treat models as black boxes or focus on coarse-grained basic emotions, leaving the cognitive structure of more complex affective states underexplored. To bridge this gap, we propose a Cognitive Reverse-Engineering framework based on Representation Engineering (RepE) to analyze social-comparison jealousy. By combining appraisal theory with subspace orthogonalization, regression-based weighting, and bidirectional causal steering, we isolate and quantify two psychological antecedents of jealousy, Superiority of Comparison Person and Domain Self-Definitional Relevance, and examine their causal effects on model judgments. Experiments on eight LLMs from the Llama, Qwen, and Gemma families suggest that models natively encode jealousy as a structured linear combination of these constituent factors. Their internal representations are broadly consistent with the human psychological construct, treating Superiority as the foundational trigger and Relevance as the ultimate intensity multiplier. Our framework also demonstrates that toxic emotional states can be mechanically detected and surgically suppressed, suggesting a possible route toward representational monitoring and intervention for AI safety in multi-agent environments.

---


### 64. [CausalDetox: Causal Head Selection and Intervention for Language Model Detoxification](https://arxiv.org/abs/2604.14602)

**<font color=#1a73e8>作者：</font>** Yian Wang, Yuen Chen, Agam Goyal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) frequently generate toxic content, posing significant risks for safe deployment. Current mitigation strategies often degrade generation quality or require costly human annotation. We propose CAUSALDETOX, a framework that identifies and intervenes on the specific attention heads causally responsible for toxic generation. Using the Probability of Necessity and Sufficiency (PNS), we isolate a minimal set of heads that are necessary and sufficient for toxicity. We utilize these components via two complementary strategies: (1) Local Inference-Time Intervention, which constructs dynamic, input-specific steering vectors for context-aware detoxification, and (2) PNS-Guided Fine-Tuning, which permanently unlearns toxic representations. We also introduce PARATOX, a novel benchmark of aligned toxic/non-toxic sentence pairs enabling controlled counterfactual evaluation. Experiments on ToxiGen, ImplicitHate, and ParaDetox show that CAUSALDETOX achieves up to 5.34% greater toxicity reduction compared to baselines while preserving linguistic fluency, and offers a 7x speedup in head selection.

---


### 65. [El Agente Forjador: Task-Driven Agent Generation for Quantum Simulation](https://arxiv.org/abs/2604.14609)

**<font color=#1a73e8>作者：</font>** Zijian Zhang, Aiwei Yin, Amaan Baweja 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI for science promises to accelerate the discovery process. The advent of large language models (LLMs) and agentic workflows enables the expediting of a growing range of scientific tasks. However, most of the current generation of agentic systems depend on static, hand-curated toolsets that hinder adaptation to new domains and evolving libraries. We present El Agente Forjador, a multi-agent framework in which universal coding agents autonomously forge, validate, and reuse computational tools through a four-stage workflow of tool analysis, tool generation, task execution, and iterative solution evaluation. Evaluated across 24 tasks spanning quantum chemistry and quantum dynamics on five coding agent setups, we compare three operating modes: zero-shot generation of tools per task, reuse of a curriculum-built toolset, and direct problem-solving with the coding agents as the baseline. We find that our tool generation and reuse framework consistently improves accuracy over the baseline. We also show that reusing a toolset built by a stronger coding agent can reduce API cost and substantially raises the solution quality for weaker coding agents. Case studies further demonstrate that tools forged for different domains can be combined to solve hybrid tasks. Taken together, these results show that LLM-based agents can use their scientific knowledge and coding capabilities to autonomously build reusable scientific tools, pointing toward a paradigm in which agent capabilities are defined by the tasks they are designed to solve rather than by explicitly engineered implementations.

---


### 66. [Retrieve, Then Classify: Corpus-Grounded Automation of Clinical Value Set Authoring](https://arxiv.org/abs/2604.14616)

**<font color=#1a73e8>作者：</font>** Sumit Mukherjee, Juan Shu, Nairwita Mazumder 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical value set authoring -- the task of identifying all codes in a standardized vocabulary that define a clinical concept -- is a recurring bottleneck in clinical quality measurement and phenotyping. A natural approach is to prompt a large language model (LLM) to generate the required codes directly, but structured clinical vocabularies are large, version-controlled, and not reliably memorized during pretraining. We propose Retrieval-Augmented Set Completion (RASC): retrieve the $K$ most similar existing value sets from a curated corpus to form a candidate pool, then apply a classifier to each candidate code. Theoretically, retrieve-and-select can reduce statistical complexity by shrinking the effective output space from the full vocabulary to a much smaller retrieved candidate pool. We demonstrate the utility of RASC on 11,803 publicly available VSAC value sets, constructing the first large-scale benchmark for this task. A cross-encoder fine-tuned on SAPBert achieves AUROC~0.852 and value-set-level F1~0.298, outperforming a simpler three-layer Multilayer Perceptron (AUROC~0.799, F1~0.250) and both reduce the number of irrelevant candidates per true positive from 12.3 (retrieval-only) to approximately 3.2 and 4.4 respectively. Zero-shot GPT-4o achieves value-set-level F1~0.105, with 48.6\% of returned codes absent from VSAC entirely. This performance gap widens with increasing value set size, consistent with RASC's theoretical advantage. We observe similar performance gains across two other classifier model types, namely a cross-encoder initialized from pre-trained SAPBert and a LightGBM model, demonstrating that RASC's benefits extend beyond a single model class. The code to download and create the benchmark dataset, as well as the model training code is available at: \href{this https URL}{this https URL}.

---


### 67. [ELMoE-3D: Leveraging Intrinsic Elasticity of MoE for Hybrid-Bonding-Enabled Self-Speculative Decoding in On-Premises Serving](https://arxiv.org/abs/2604.14626)

**<font color=#1a73e8>作者：</font>** Yuseon Choi, Jingu Lee, Jungjun Oh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models have become the dominant architecture for large-scale language models, yet on-premises serving remains fundamentally memory-bound as batching turns sparse per-token compute into dense memory activation. Memory-centric architectures (PIM, NMP) improve bandwidth but leave compute underutilized under MoE's low arithmetic intensity at high batch sizes. Speculative decoding (SD) trades idle compute for fewer target invocations, yet verification must load experts even for rejected tokens, severely limiting its benefit in MoE especially at low batch sizes. We propose ELMoE-3D, a hybrid-bonding (HB)-based HW-SW co-designed framework that unifies cache-based acceleration and speculative decoding to offer overall speedup across batch sizes. We identify two intrinsic elasticity axes of MoE-expert and bit-and jointly scale them to construct Elastic Self-Speculative Decoding (Elastic-SD), which serves as both an expert cache and a strongly aligned self-draft model accelerated by high HB bandwidth. Our LSB-augmented bit-sliced architecture exploits inherent redundancy in bit-slice representations to natively support bit-nested execution. On our 3D-stacked hardware, ELMoE-3D achieves an average $6.6\times$ speedup and $4.4\times$ energy efficiency gain over naive MoE serving on xPU across batch sizes 1-16, and delivers $2.2\times$ speedup and $1.4\times$ energy efficiency gain over the best-performing prior accelerator baseline.

---


### 68. [Switch-KD: Visual-Switch Knowledge Distillation for Vision-Language Models](https://arxiv.org/abs/2604.14629)

**<font color=#1a73e8>作者：</font>** Haoyi Sun, Xiaoxiao Wang, Ning Mao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have shown remarkable capabilities in joint vision-language understanding, but their large scale poses significant challenges for deployment in resource-constrained scenarios. Knowledge Distillation (KD) offers a viable way to improve model capabilities without increasing model size or data requirements, making deployment more efficient. However, applying KD to VLMs is challenged by modality-specific supervision: although multimodal knowledge in VLMs is fused within the language space, current methods supervise each modality separately without explicitly addressing multimodal alignment, leading to inconsistent multimodal knowledge transfer. To address this, we propose Switch-KD, a visual-switch distillation framework that unifies vision-language knowledge transfer within a shared text-probability space. Switch-KD comprises two key components: (1) Visual-Switch Distillation, which switches the student's visual outputs into the teacher's language pathway to construct cross-modal probabilistic references for implicit visual knowledge transfer; and (2) Dynamic Bi-directional Logits Difference (DBiLD) loss, which adaptively aligns informative probability regions while preserving the distributional structures of teacher and student through bidirectional supervision. Guided by Switch-KD, a 0.5B TinyLLaVA effectively distills rich multimodal knowledge from its 3B teacher, yielding an average improvement of 3.6 points across 10 multimodal benchmarks without any architectural modification.

---


### 69. [StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation](https://arxiv.org/abs/2604.14631)

**<font color=#1a73e8>作者：</font>** Geonhui Jang, Dongyoon Han, YoungJoon Yoo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective code generation requires both model capability and a problem representation that carefully structures how models reason and plan. Existing approaches augment reasoning steps or inject specific structure into how models think, but leave scattered problem conditions unchanged. Inspired by the way humans organize fragmented information into coherent explanations, we propose StoryCoder, a narrative reformulation framework that transforms code generation questions into coherent natural language narratives, providing richer contextual structure than simple rephrasings. Each narrative consists of three components: a task overview, constraints, and example test cases, guided by the selected algorithm and genre. Experiments across 11 models on HumanEval, LiveCodeBench, and CodeForces demonstrate consistent improvements, with an average gain of 18.7% in zero-shot pass@10. Beyond accuracy, our analyses reveal that narrative reformulation guides models toward correct algorithmic strategies, reduces implementation errors, and induces a more modular code structure. The analyses further show that these benefits depend on narrative coherence and genre alignment, suggesting that structured problem representation is important for code generation regardless of model scale or architecture. Our code is available at this https URL.

---


### 70. [Fact4ac at the Financial Misinformation Detection Challenge Task: Reference-Free Financial Misinformation Detection via Fine-Tuning and Few-Shot Prompting of Large Language Models](https://arxiv.org/abs/2604.14640)

**<font color=#1a73e8>作者：</font>** Cuong Hoang, Le-Minh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The proliferation of financial misinformation poses a severe threat to market stability and investor trust, misleading market behavior and creating critical information asymmetry. Detecting such misleading narratives is inherently challenging, particularly in real-world scenarios where external evidence or supplementary references for cross-verification are strictly unavailable. This paper presents our winning methodology for the "Reference-Free Financial Misinformation Detection" shared task. Built upon the recently proposed RFC-BENCH framework (Jiang et al. 2026), this task challenges models to determine the veracity of financial claims by relying solely on internal semantic understanding and contextual consistency, rather than external fact-checking. To address this formidable evaluation setup, we propose a comprehensive framework that capitalizes on the reasoning capabilities of state-of-the-art Large Language Models (LLMs). Our approach systematically integrates in-context learning, specifically zero-shot and few-shot prompting strategies, with Parameter-Efficient Fine-Tuning (PEFT) via Low-Rank Adaptation (LoRA) to optimally align the models with the subtle linguistic cues of financial manipulation. Our proposed system demonstrated superior efficacy, successfully securing the first-place ranking on both official leaderboards. Specifically, we achieved an accuracy of 95.4% on the public test set and 96.3% on the private test set, highlighting the robustness of our method and contributing to the acceleration of context-aware misinformation detection in financial Natural Language Processing. Our models (14B and 32B) are available at this https URL.

---


### 71. [Learning to Draw ASCII Improves Spatial Reasoning in Language Models](https://arxiv.org/abs/2604.14641)

**<font color=#1a73e8>作者：</font>** Shiyuan Huang, Li Liu, Jincheng He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When faced with complex spatial problems, humans naturally sketch layouts to organize their thinking, and the act of drawing further sharpens their understanding. In this work, we ask whether a similar principle holds for Large Language Models (LLMs): can learning to construct explicit visual layouts from spatial descriptions instill genuine spatial understanding? We introduce Text2Space, a dataset that pairs natural language descriptions with ground-truth ASCII grid layouts and spatial QA pairs, enabling us to separate failures in constructing spatial representations from failures in reasoning over them. We adopt ASCII because it is human-readable, operates entirely within the token space of language models, and encodes spatial relations in a structurally verifiable form. Our evaluation reveals a pronounced "Read-Write Asymmetry": LLMs interpret ASCII representations effectively but struggle to produce them from text, and these construction errors propagate to incorrect answers downstream. To address this limitation, we train models on layout construction (Text$\rightarrow$ASCII) and find that it significantly improves spatial reasoning from text alone, even without producing any ASCII at inference time. Combining construction with comprehension training further amplifies these gains. Crucially, these improvements transfer to three external spatial reasoning benchmarks, demonstrating that, much as sketching sharpens human spatial thinking, learning to construct explicit layouts instills spatial understanding that generalizes beyond the training format.

---


### 72. [CURaTE: Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge](https://arxiv.org/abs/2604.14644)

**<font color=#1a73e8>作者：</font>** Seyun Bae, Seokhan Lee, Eunho Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The inability to filter out in advance all potentially problematic data from the pre-training of large language models has given rise to the need for methods for unlearning specific pieces of knowledge after training. Existing techniques overlook the need for continuous and immediate action, causing them to suffer from degraded utility as updates accumulate and protracted exposure of sensitive information. To address these issues, we propose Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge (CURaTE). Our method begins by training a sentence embedding model on a dataset designed to enable the formation of sharp decision boundaries for determining whether a given input prompt corresponds to any stored forget requests. The similarity of a given input to the forget requests is then used to determine whether to answer or return a refusal response. We show that even with such a simple approach, not only does CURaTE achieve more effective forgetting than existing methods, but by avoiding modification of the language model parameters, it also maintains near perfect knowledge preservation over any number of updates and is the only method capable of continual unlearning in real-time.

---


### 73. [Targeted Exploration via Unified Entropy Control for Reinforcement Learning](https://arxiv.org/abs/2604.14646)

**<font color=#1a73e8>作者：</font>** Chen Wang, Lai Wei, Yanzhi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in reinforcement learning (RL) have improved the reasoning capabilities of large language models (LLMs) and vision-language models (VLMs). However, the widely used Group Relative Policy Optimization (GRPO) consistently suffers from entropy collapse, causing the policy to converge prematurely and lose diversity. Existing exploration methods introduce additional bias or variance during exploration, making it difficult to maintain optimization stability. We propose Unified Entropy Control for Reinforcement Learning (UEC-RL), a framework that provides targeted mechanisms for exploration and stabilization. UEC-RL activates more exploration on difficult prompts to search for potential and valuable reasoning trajectories. In parallel, a stabilizer prevents entropy from growing uncontrollably, thereby keeping training stable as the model consolidates reliable behaviors. Together, these components expand the search space when needed while maintaining robust optimization throughout training. Experiments on both LLM and VLM reasoning tasks show consistent gains over RL baselines on both Pass@1 and Pass@$k$. On Geometry3K, UEC-RL achieves a 37.9\% relative improvement over GRPO, indicating that it sustains effective exploration without compromising convergence and underscoring UEC-RL as a key for scaling RL-based reasoning in large models. Our code is available at this https URL.

---


### 74. [CURA: Clinical Uncertainty Risk Alignment for Language Model-Based Risk Prediction](https://arxiv.org/abs/2604.14651)

**<font color=#1a73e8>作者：</font>** Sizhe Wang, Ziqi Xu, Claire Najjuuko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical language models (LMs) are increasingly applied to support clinical risk prediction from free-text notes, yet their uncertainty estimates often remain poorly calibrated and clinically unreliable. In this work, we propose Clinical Uncertainty Risk Alignment (CURA), a framework that aligns clinical LM-based risk estimates and uncertainty with both individual error likelihoods and cohort-level ambiguities. CURA first fine-tunes domain-specific clinical LMs to obtain task-adapted patient embeddings, and then performs uncertainty fine-tuning of a multi-head classifier using a bi-level uncertainty objective. Specifically, an individual-level calibration term aligns predictive uncertainty with each patient's likelihood of error, while a cohort-aware regularizer pulls risk estimates toward event rates in their local neighborhoods in the embedding space and places extra weight on ambiguous cohorts near the decision boundary. We further show that this cohort-aware term can be interpreted as a cross-entropy loss with neighborhood-informed soft labels, providing a label-smoothing view of our method. Extensive experiments on MIMIC-IV clinical risk prediction tasks across various clinical LMs show that CURA consistently improves calibration metrics without substantially compromising discrimination. Further analysis illustrates that CURA reduces overconfident false reassurance and yields more trustworthy uncertainty estimates for downstream clinical decision support.

---


### 75. [Rethinking Patient Education as Multi-turn Multi-modal Interaction](https://arxiv.org/abs/2604.14656)

**<font color=#1a73e8>作者：</font>** Zonghai Yao, Zhipeng Tang, Chengtao Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most medical multimodal benchmarks focus on static tasks such as image question answering, report generation, and plain-language rewriting. Patient education is more demanding: systems must identify relevant evidence across images, show patients where to look, explain findings in accessible language, and handle confusion or distress. Yet most patient education work remains text-only, even though combined image-and-text explanations may better support understanding. We introduce MedImageEdu, a benchmark for multi-turn, evidence-grounded radiology patient education. Each case provides a radiology report with report text and case images. A DoctorAgent interacts with a PatientAgent, conditioned on a hidden profile that captures factors such as education level, health literacy, and personality. When a patient question would benefit from visual support, the DoctorAgent can issue drawing instructions grounded in the report, case images, and the current question to a benchmark-provided drawing tool. The tool returns image(s), after which the DoctorAgent produces a final multimodal response consisting of the image(s) and a grounded plain-language explanation. MedImageEdu contains 150 cases from three sources and evaluates both the consultation process and the final multimodal response along five dimensions: Consultation, Safety and Scope, Language Quality, Drawing Quality, and Image-Text Response Quality. Across representative open- and closed-source vision-language model agents, we find three consistent gaps: fluent language often outpaces faithful visual grounding, safety is the weakest dimension across disease categories, and emotionally tense interactions are harder than low education or low health literacy. MedImageEdu provides a controlled testbed for assessing whether multimodal agents can teach from evidence rather than merely answer from text.

---


### 76. [SPAGBias: Uncovering and Tracing Structured Spatial Gender Bias in Large Language Models](https://arxiv.org/abs/2604.14672)

**<font color=#1a73e8>作者：</font>** Binxian Su, Haoye Lou, Shucheng Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are being increasingly used in urban planning, but since gendered space theory highlights how gender hierarchies are embedded in spatial organization, there is concern that LLMs may reproduce or amplify such biases. We introduce SPAGBias - the first systematic framework to evaluate spatial gender bias in LLMs. It combines a taxonomy of 62 urban micro-spaces, a prompt library, and three diagnostic layers: explicit (forced-choice resampling), probabilistic (token-level asymmetry), and constructional (semantic and narrative role analysis). Testing six representative models, we identify structured gender-space associations that go beyond the public-private divide, forming nuanced micro-level mappings. Story generation reveals how emotion, wording, and social roles jointly shape "spatial gender narratives". We also examine how prompt design, temperature, and model scale influence bias expression. Tracing experiments indicate that these patterns are embedded and reinforced across the model pipeline (pre-training, instruction tuning, and reward modeling), with model associations found to substantially exceed real-world distributions. Downstream experiments further reveal that such biases produce concrete failures in both normative and descriptive application settings. This work connects sociological theory with computational analysis, extending bias research into the spatial domain and uncovering how LLMs encode social gender cognition through language.

---


### 77. [Acceptance Dynamics Across Cognitive Domains in Speculative Decoding](https://arxiv.org/abs/2604.14682)

**<font color=#1a73e8>作者：</font>** Saif Mahmoud  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model (LLM) inference. It uses a small draft model to propose a tree of future tokens. A larger target model then verifies these tokens in a single batched forward pass. Despite the growing body of work on speculative methods, the degree to which the cognitive characteristics of a task affect acceptance probability remains largely unexplored. We present an empirical study of tree-based speculative decoding acceptance dynamics. Our study spans four well-established NLP benchmark domains: code generation, mathematical reasoning, logical reasoning, and open-ended chat. For this, we use TinyLlama-1.1B as the draft model against Llama-2-7B-Chat-GPTQ as the target. Over 99,768 speculative nodes collected from 200 prompts, we derive per-domain acceptance rates, expected accepted lengths, depth-acceptance profiles, and entropy-acceptance correlations. We find that task type is a stronger predictor of acceptance than tree depth. Furthermore, only the chat domain consistently yields an expected accepted length exceeding 1.0 token per step. We also show that the entropy-acceptance correlation is consistently negative but weak across all domains (rho in [-0.20, -0.15]). Counterintuitively, chat produces the highest entropy yet the highest acceptance rate. We attribute this divergence to the lexical predictability of RLHF-aligned register. These findings have direct implications for domain-aware speculation budgets and draft-model selection strategies. Index Terms--speculative decoding, large language model inference, tree attention, draft model, acceptance probability, LLM efficiency

---


### 78. [DR$^{3}$-Eval: Towards Realistic and Reproducible Deep Research Evaluation](https://arxiv.org/abs/2604.14683)

**<font color=#1a73e8>作者：</font>** Qianqian Xie, Qingheng Xiong, He Zhu 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep Research Agents (DRAs) aim to solve complex, long-horizon research tasks involving planning, retrieval, multimodal understanding, and report generation, yet their evaluation remains challenging due to dynamic web environments and ambiguous task definitions. We propose DR$^{3}$-Eval, a realistic and reproducible benchmark for evaluating deep research agents on multimodal, multi-file report generation. DR$^{3}$-Eval is constructed from authentic user-provided materials and paired with a per-task static research sandbox corpus that simulates open-web complexity while remaining fully verifiable, containing supportive documents, distractors, and noise. Moreover, we introduce a multi-dimensional evaluation framework measuring Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality, and validate its alignment with human judgments. Experiments with our developed multi-agent system DR$^{3}$-Agent based on multiple state-of-the-art language models demonstrate that DR$^{3}$-Eval is highly challenging and reveals critical failure modes in retrieval robustness and hallucination control. Our code and data are publicly available.

---


### 79. [M2-PALE: A Framework for Explaining Multi-Agent MCTS--Minimax Hybrids via Process Mining and LLMs](https://arxiv.org/abs/2604.14687)

**<font color=#1a73e8>作者：</font>** Yiyu Qian, Liyuan Zhao, Tim Miller  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Monte-Carlo Tree Search (MCTS) is a fundamental sampling-based search algorithm widely used for online planning in sequential decision-making domains. Despite its success in driving recent advances in artificial intelligence, understanding the behavior of MCTS agents remains a challenge for both developers and users. This difficulty stems from the complex search trees produced through the simulation of numerous future states and their intricate relationships. A known weakness of standard MCTS is its reliance on highly selective tree construction, which may lead to the omission of crucial moves and a vulnerability to tactical traps. To resolve this, we incorporate shallow, full-width Minimax search into the rollout phase of multi-agent MCTS to enhance strategic depth. Furthermore, to demystify the resulting decision-making logic, we introduce \textsf{M2-PALE} (MCTS--Minimax Process-Aided Linguistic Explanations). This framework employs process mining techniques, specifically the Alpha Miner, iDHM, and Inductive Miner algorithms, to extract underlying behavioral workflows from agent execution traces. These process models are then synthesized by LLMs to generate human-readable causal and distal explanations. We demonstrate the efficacy of our approach in a small-scale checkers environment, establishing a scalable foundation for interpreting hybrid agents in increasingly complex strategic domains.

---


### 80. [CAMO: An Agentic Framework for Automated Causal Discovery from Micro Behaviors to Macro Emergence in LLM Agent Simulations](https://arxiv.org/abs/2604.14691)

**<font color=#1a73e8>作者：</font>** Xiangning Yu, Yuwei Guo, Yuqi Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-empowered agent simulations are increasingly used to study social emergence, yet the micro-to-macro causal mechanisms behind macro outcomes often remain unclear. This is challenging because emergence arises from intertwined agent interactions and meso-level feedback and nonlinearity, making generative mechanisms hard to disentangle. To this end, we introduce \textbf{\textsc{CAMO}}, an automated \textbf{Ca}usal discovery framework from \textbf{M}icr\textbf{o} behaviors to \textbf{M}acr\textbf{o} Emergence in LLM agent simulations. \textsc{CAMO} converts mechanistic hypotheses into computable factors grounded in simulation records and learns a compact causal representation centered on an emergent target $Y$. \textsc{CAMO} outputs a computable Markov boundary and a minimal upstream explanatory subgraph, yielding interpretable causal chains and actionable intervention levers. It also uses simulator-internal counterfactual probing to orient ambiguous edges and revise hypotheses when evidence contradicts the current view. Experiments across four emergent settings demonstrate the promise of \textsc{CAMO}.

---


### 81. [HWE-Bench: Benchmarking LLM Agents on Real-World Hardware Bug Repair Tasks](https://arxiv.org/abs/2604.14709)

**<font color=#1a73e8>作者：</font>** Fan Cui, Hongyuan Hou, Zizhang Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks for hardware design primarily evaluate Large Language Models (LLMs) on isolated, component-level tasks such as generating HDL modules from specifications, leaving repository-scale evaluation unaddressed. We introduce HWE-Bench, the first large-scale, repository-level benchmark for evaluating LLM agents on real-world hardware bug repair tasks. HWE-Bench comprises 417 task instances derived from real historical bug-fix pull requests across six major open-source projects spanning both Verilog/SystemVerilog and Chisel, covering RISC-V cores, SoCs, and security roots-of-trust. Each task is grounded in a fully containerized environment where the agent must resolve a real bug report, with correctness validated through the project's native simulation and regression flows. The benchmark is built through a largely automated pipeline that enables efficient expansion to new repositories. We evaluate seven LLMs with four agent frameworks and find that the best agent resolves 70.7% of tasks overall, with performance exceeding 90% on smaller cores but dropping below 65% on complex SoC-level projects. We observe larger performance gaps across models than commonly reported on software benchmarks, and difficulty is driven by project scope and bug-type distribution rather than code size alone. Our failure analysis traces agent failures to three stages of the debugging process: fault localization, hardware-semantic reasoning, and cross-artifact coordination across RTL, configuration, and verification components, providing concrete directions for developing more capable hardware-aware agents.

---


### 82. [G-MIXER: Geodesic Mixup-based Implicit Semantic Expansion and Explicit Semantic Re-ranking for Zero-Shot Composed Image Retrieval](https://arxiv.org/abs/2604.14710)

**<font color=#1a73e8>作者：</font>** Jiyoung Lim, Heejae Yang, Jee-Hyong Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) aims to retrieve target images by integrating a reference image with a corresponding modification text. CIR requires jointly considering the explicit semantics specified in the query and the implicit semantics embedded within its bi-modal composition. Recent training-free Zero-Shot CIR (ZS-CIR) methods leverage Multimodal Large Language Models (MLLMs) to generate detailed target descriptions, converting the implicit information into explicit textual expressions. However, these methods rely heavily on the textual modality and fail to capture the fuzzy retrieval nature that requires considering diverse combinations of candidates. This leads to reduced diversity and accuracy in retrieval results. To address this limitation, we propose a novel training-free method, Geodesic Mixup-based Implicit semantic eXpansion and Explicit semantic Re-ranking for ZS-CIR (G-MIXER). G-MIXER constructs composed query features that reflect the implicit semantics of reference image-text pairs through geodesic mixup over a range of mixup ratios, and builds a diverse candidate set. The generated candidates are then re-ranked using explicit semantics derived from MLLMs, improving both retrieval diversity and accuracy. Our proposed G-MIXER achieves state-of-the-art performance across multiple ZS-CIR benchmarks, effectively handling both implicit and explicit semantics without additional training. Our code will be available at this https URL.

---


### 83. [SGA-MCTS: Decoupling Planning from Execution via Training-Free Atomic Experience Retrieval](https://arxiv.org/abs/2604.14712)

**<font color=#1a73e8>作者：</font>** Xin Xie, Dongyun Xue, Wuguannan Yao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-powered systems require complex multi-step decision-making abilities to solve real-world tasks, yet current planning approaches face a trade-off between the high latency of inference-time search and the limited generalization of supervised fine-tuning. To address this limitation, we introduce \textbf{SGA-MCTS}, a framework that casts LLM planning as non-parametric retrieval. Offline, we leverage Monte Carlo Tree Search (MCTS) to explore the solution space and distill high-fidelity trajectories into State-Goal-Action (SGA) atoms. These atoms are de-lexicalized primitives that abstract concrete entities into symbolic slots, preserving reusable causal logic while discarding domain-specific noise. Online, a retrieval-augmented agent employs a hybrid symbolic-semantic mechanism to fetch relevant SGAs and re-ground them into the current context as soft reasoning hints. Empirical results on complex benchmarks demonstrate that this paradigm enables frozen, open-weights models to match the performance of SOTA systems (e.g., GPT-5) without task-specific fine-tuning. By effectively amortizing the heavy computational cost of search, SGA-MCTS achieves System 2 reasoning depth at System 1 inference speeds, rendering autonomous planning both scalable and real-time feasible.

---


### 84. [A Mechanistic Account of Attention Sinks in GPT-2: One Circuit, Broader Implications for Mitigation](https://arxiv.org/abs/2604.14722)

**<font color=#1a73e8>作者：</font>** Yuval Ran-Milo, Hila Ofek, Shahar Mendel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers commonly exhibit an attention sink: disproportionately high attention to the first position. We study this behavior in GPT-2-style models with learned query biases and absolute positional embeddings. Combining structural analysis with causal interventions, validated across natural-language, mathematical, and code inputs, we find that the sink arises from the interaction among (i) a learned query bias, (ii) the first-layer MLP transformation of the positional encoding, and (iii) structure in the key projection. Crucially, each component we identify is individually dispensable: architectures omitting each of them robustly exhibit sinks. This indicates that attention sinks may arise through distinct circuits across architectures. These findings inform mitigation of sinks, and motivate broader investigation into why sinks emerge.

---


### 85. [Assessing the Performance-Efficiency Trade-off of Foundation Models in Probabilistic Electricity Price Forecasting](https://arxiv.org/abs/2604.14739)

**<font color=#1a73e8>作者：</font>** Jan Niklas Lettner, Hadeer El Ashhab, Veit Hagenmeyer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale renewable energy deployment introduces pronounced volatility into the electricity system, turning grid operation into a complex stochastic optimization problem. Accurate electricity price forecasting (EPF) is essential not only to support operational decisions, such as optimal bidding strategies and balancing power preparation, but also to reduce economic risk and improve market efficiency. Probabilistic forecasts are particularly valuable because they quantify uncertainty stemming from renewable intermittency, market coupling, and regulatory changes, enabling market participants to make informed decisions that minimize losses and optimize expected revenues. However, it remains an open question which models to employ to produce accurate forecasts. Should these be task-specific machine learning (ML) models or Time Series Foundation Models (TSFMs)? In this work, we compare four models for day-ahead probabilistic EPF (PEPF) in European bidding zones: a deterministic NHITS backbone with Quantile-Regression Averaging (NHITS+QRA) and a conditional Normalizing-Flow forecaster (NF) are compared with two TSFMs, namely Moirai and ChronosX. On the one hand, we find that TSFMs outperform task-specific deep learning models trained from scratch in terms of CRPS, Energy Score, and predictive interval calibration across market conditions. On the other hand, we find that well-configured task-specific models, particularly NHITS combined with QRA, achieve performance very close to TSFMs, and in some scenarios, such as when supplied with additional informative feature groups or adapted via few-shot learning from other European markets, they can even surpass TSFMs. Overall, our findings show that while TSFMs offer expressive modeling capabilities, conventional models remain highly competitive, emphasizing the need to weigh computational expense against marginal performance improvements in PEPF.

---


### 86. [Disentangle-then-Refine: LLM-Guided Decoupling and Structure-Aware Refinement for Graph Contrastive Learning](https://arxiv.org/abs/2604.14746)

**<font color=#1a73e8>作者：</font>** Zhaoxing Li, Hai-Feng Zhang, Xiaoming Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conventional Graph Contrastive Learning (GCL) on Text-Attributed Graphs (TAGs) relies on blind stochastic augmentations, inadvertently entangling task-relevant signals with noise. We propose SDM-SCR, a robust framework anchored in Approximate Orthogonal Decomposition. First, the Semantic Decoupling Module (SDM) leverages the instruction-following capability of Large Language Models (LLMs) to actively parse raw attributes into asymmetric, task-oriented signal and noise views. This shifts the paradigm from random perturbation to semantic-aware disentanglement. Subsequently, Semantic Consistency Regularization (SCR) exploits the spectral observation that semantic signals are topologically smooth while residual noise is high-frequency. SCR functions as a selective spectral filter, enforcing consistency only on the signal subspace to eliminate LLM hallucinations without over-smoothing. This ``Disentangle-then-Refine'' mechanism ensures rigorous signal purification. Extensive experiments demonstrate that SDM-SCR achieves SOTA performance in accuracy and efficiency.

---


### 87. [CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning](https://arxiv.org/abs/2604.14768)

**<font color=#1a73e8>作者：</font>** Zhuo Wang, Zhuo Zhang, Yafu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) exhibit strong mathematical reasoning when trained on high-quality Chain-of-Thought (CoT) that articulates intermediate steps, yet costly CoT curation hinders further progress. While existing remedies such as distillation from stronger LLMs and self-synthesis based on test-time search alleviate this issue, they often suffer from diminishing returns or high computing this http URL this work, we propose CoTEvol, a genetic evolutionary framework that casts CoT generation as a population-based search over reasoning this http URL trajectories are iteratively evolved through reflective global crossover at the trajectory level and local mutation guided by uncertainty at the step level, enabling holistic recombination and fine-grained refinement. Lightweight, task-aware fitness functions are designed to guide the evolutionary process toward accurate and diverse reasoning. Empirically, CoTEvol improves correct-CoT synthesis success by over 30% and enhances structural diversity, with markedly improved efficiency. LLMs trained on these evolutionary CoT data achieve an average gain of 6.6% across eight math benchmarks, outperforming previous distillation and self-synthesis approaches. These results underscore the promise of evolutionary CoT synthesis as a scalable and effective method for mathematical reasoning tasks.

---


### 88. [Constraint-based Pre-training: From Structured Constraints to Scalable Model Initialization](https://arxiv.org/abs/2604.14769)

**<font color=#1a73e8>作者：</font>** Fu Feng, Yucheng Xie, Ruixiao Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The pre-training and fine-tuning paradigm has become the dominant approach for model adaptation. However, conventional pre-training typically yields models at a fixed scale, whereas practical deployment often requires models of varying sizes, exposing its limitations when target model scales differ from those used during pre-training. To address this, we propose an innovative constraint-based pre-training paradigm that imposes structured constraints during pre-training to disentangle size-agnostic knowledge into reusable weight templates, while assigning size-specific adaptation to lightweight weight scalers, thereby reformulating variable-sized model initialization as a multi-task adaptation problem. Within this paradigm, we further introduce WeiT, which employs Kronecker-based constraints to regularize the pre-training process. Specifically, model parameters are represented as compositions of weight templates via concatenation and weighted aggregation, with adaptive connections governed by lightweight weight scalers whose parameters are learned from limited data. This design enables flexible and efficient construction of model weights across diverse downstream scales. Extensive experiments demonstrate the efficiency and effectiveness of WeiT, achieving state-of-the-art performance in initializing models with varying depths and widths across a broad range of perception and embodied learning tasks, including Image Classification, Image Generation, and Embodied Control. Moreover, its effectiveness generalizes to both Transformer-based and Convolution-based architectures, consistently enabling faster convergence and improved performance even under full training.

---


### 89. [MirrorBench: Evaluating Self-centric Intelligence in MLLMs by Introducing a Mirror](https://arxiv.org/abs/2604.14785)

**<font color=#1a73e8>作者：</font>** Shengyu Guo, Tongrui Ye, Jianbo Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent progress in Multimodal Large Language Models (MLLMs) has demonstrated remarkable advances in perception and reasoning, suggesting their potential for embodied intelligence. While recent studies have evaluated embodied MLLMs in interactive settings, current benchmarks mainly target capabilities to perceive, understand, and interact with external objects, lacking a systematic evaluation of self-centric intelligence. To address this, we introduce MirrorBench, a simulation-based benchmark inspired by the classical Mirror Self-Recognition (MSR) test in psychology. MirrorBench extends this paradigm to embodied MLLMs through a tiered framework of progressively challenging tasks, assessing agents from basic visual perception to high-level self-representation. Experiments on leading MLLMs show that even at the lowest level, their performance remains substantially inferior to human performance, revealing fundamental limitations in self-referential understanding. Our study bridges psychological paradigms and embodied intelligence, offering a principled framework for evaluating the emergence of general intelligence in large models. Project page: this https URL.

---


### 90. [Knowing When Not to Answer: Evaluating Abstention in Multimodal Reasoning Systems](https://arxiv.org/abs/2604.14799)

**<font color=#1a73e8>作者：</font>** Nishanth Madhusudhan, Vikas Yadav, Alexandre Lacoste  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective abstention (EA), recognizing evidence insufficiency and refraining from answering, is critical for reliable multimodal systems. Yet existing evaluation paradigms for vision-language models (VLMs) and multi-agent systems (MAS) assume answerability, pushing models to always respond. Abstention has been studied in text-only settings but remains underexplored multimodally; current benchmarks either ignore unanswerability or rely on coarse methods that miss realistic failure modes. We introduce MM-AQA, a benchmark that constructs unanswerable instances from answerable ones via transformations along two axes: visual modality dependency and evidence sufficiency. Evaluating three frontier VLMs spanning closed and open-source models and two MAS architectures across 2079 samples, we find: (1) under standard prompting, VLMs rarely abstain; even simple confidence baselines outperform this setup, (2) MAS improves abstention but introduces an accuracy-abstention trade-off, (3) sequential designs match or exceed iterative variants, suggesting the bottleneck is miscalibration rather than reasoning depth, and (4) models abstain when image or text evidence is absent, but attempt reconciliation with degraded or contradictory evidence. Effective multimodal abstention requires abstention-aware training rather than better prompting or more agents.

---


### 91. [The LLM Fallacy: Misattribution in AI-Assisted Cognitive Workflows](https://arxiv.org/abs/2604.14807)

**<font color=#1a73e8>作者：</font>** Hyunwoo Kim, Harin Yu, Hanau Yi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid integration of large language models (LLMs) into everyday workflows has transformed how individuals perform cognitive tasks such as writing, programming, analysis, and multilingual communication. While prior research has focused on model reliability, hallucination, and user trust calibration, less attention has been given to how LLM usage reshapes users' perceptions of their own capabilities. This paper introduces the LLM fallacy, a cognitive attribution error in which individuals misinterpret LLM-assisted outputs as evidence of their own independent competence, producing a systematic divergence between perceived and actual capability. We argue that the opacity, fluency, and low-friction interaction patterns of LLMs obscure the boundary between human and machine contribution, leading users to infer competence from outputs rather than from the processes that generate them. We situate the LLM fallacy within existing literature on automation bias, cognitive offloading, and human--AI collaboration, while distinguishing it as a form of attributional distortion specific to AI-mediated workflows. We propose a conceptual framework of its underlying mechanisms and a typology of manifestations across computational, linguistic, analytical, and creative domains. Finally, we examine implications for education, hiring, and AI literacy, and outline directions for empirical validation. We also provide a transparent account of human--AI collaborative methodology. This work establishes a foundation for understanding how generative AI systems not only augment cognitive performance but also reshape self-perception and perceived expertise.

---


### 92. [Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem](https://arxiv.org/abs/2604.14808)

**<font color=#1a73e8>作者：</font>** Zeguan Xiao, Siqing Li, Yong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning for large language models (LLMs) aims to remove targeted knowledge while preserving general capability. In this paper, we recast LLM unlearning as an asymmetric two-task problem: retention is the primary objective and forgetting is an auxiliary. From this perspective, we propose a retention-prioritized gradient synthesis framework that decouples task-specific gradient extraction from conflict-aware combination. Instantiating the framework, we adapt established PCGrad to resolve gradient conflicts, and introduce SAGO, a novel retention-prioritized gradient synthesis method. Theoretically, both variants ensure non-negative cosine similarity with the retain gradient, while SAGO achieves strictly tighter alignment through constructive sign-constrained synthesis. Empirically, on WMDP Bio/Cyber and RWKU benchmarks, SAGO consistently pushes the Pareto frontier: e.g., on WMDP Bio (SimNPO+GD), recovery of target model MMLU performance progresses from 44.6% (naive) to 94.0% (+PCGrad) and further to 96.0% (+SAGO), while maintaining comparable forgetting strength. Our results show that re-shaping gradient geometry, rather than re-balancing losses, is the key to mitigating unlearning-retention trade-offs.

---


### 93. [Learning Ad Hoc Network Dynamics via Graph-Structured World Models](https://arxiv.org/abs/2604.14811)

**<font color=#1a73e8>作者：</font>** Can Karacelebi, Yusuf Talha Sahin, Elif Surer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ad hoc wireless networks exhibit complex, innate and coupled dynamics: node mobility, energy depletion and topology change that are difficult to model analytically. Model-free deep reinforcement learning requires sustained online interaction whereas existing model based approaches use flat state representations that lose per node structure. Therefore we propose G-RSSM, a graph structured recurrent state space model that maintains per node latent states with cross node multi head attention to learn the dynamics jointly from offline trajectories. We apply the proposed method to the downstream task clustering where a cluster head selection policy trains entirely through imagined rollouts in the learned world model. Across 27 evaluation scenarios spanning MANET, VANET, FANET, WSN and tactical networks with N=30 to 1000 nodes, the learned policy maintains high connectivity with only trained for N=50. Herein, we propose the first multi physics graph structured world model applied to combinatorial per node decision making in size agnostic wireless ad hoc networks.

---


### 94. [Domain Fine-Tuning FinBERT on Finnish Histopathological Reports: Train-Time Signals and Downstream Correlations](https://arxiv.org/abs/2604.14815)

**<font color=#1a73e8>作者：</font>** Rami Luisto, Liisa Petäinen, Tommi Grönholm 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In NLP classification tasks where little labeled data exists, domain fine-tuning of transformer models on unlabeled data is an established approach. In this paper we have two aims.
(1) We describe our observations from fine-tuning the Finnish BERT model on Finnish medical text data.
(2) We report on our attempts to predict the benefit of domain-specific pre-training of Finnish BERT from observing the geometry of embedding changes due to domain fine-tuning.
Our driving motivation is the common\situation in healthcare AI where we might experience long delays in acquiring datasets, especially with respect to labels.

---


### 95. [Intermediate Layers Encode Optimal Biological Representations in Single-Cell Foundation Models](https://arxiv.org/abs/2604.14838)

**<font color=#1a73e8>作者：</font>** Vincenzo Yuto Civale, Roberto Semeraro, Andrew David Bagdanov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current single-cell foundation model benchmarks universally extract final layer embeddings, assuming these represent optimal feature spaces. We systematically evaluate layer-wise representations from scFoundation (100M parameters) and Tahoe-X1 (1.3B parameters) across trajectory inference and perturbation response prediction. Our analysis reveals that optimal layers are task-dependent (trajectory peaks at 60% depth, 31% above final layers) and context-dependent (perturbation optima shift 0-96% across T cell activation states). Notably, first-layer embeddings outperform all deeper layers in quiescent cells, challenging assumptions about hierarchical feature abstraction. These findings demonstrate that "where" to extract features matters as much as "what" the model learns, necessitating systematic layer evaluation tailored to biological task and cellular context rather than defaulting to final-layer embeddings.

---


### 96. [Exploring and Testing Skill-Based Behavioral Profile Annotation: Human Operability and LLM Feasibility under Schema-Guided Execution](https://arxiv.org/abs/2604.14843)

**<font color=#1a73e8>作者：</font>** Yufeng Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Behavioral Profile (BP) annotation is difficult to automate because it requires simultaneous coding across multiple linguistic dimensions. We treat BP annotation as a bundle of annotation skills rather than a single task and evaluate LLM-assisted BP annotation from this perspective. Using 3,134 concordance lines of 30 Chinese metaphorical color-term derivatives and a 14-feature BP schema, we implement a skill-file-driven pipeline in which each feature is externally defined through schema files, decision rules, and examples. Two human annotators completed a two-round schema-only protocol on a 300-instance validation subset, enabling BP skills to be classified as directly operable, recoverable under focused re-annotation, or structurally underspecified. GPT-5.4 and three locally deployable open-source models were then evaluated under the same setup. Results show that BP annotation is highly heterogeneous at the skill level: 5 skills are directly operable, 4 are recoverable after focused re-annotation, and 5 remain structurally underspecified. GPT-5.4 executes the retained skills with substantial reliability (accuracy = 0.678, \k{appa} = 0.665, weighted F1 = 0.695), but this feasibility is selective rather than global. Human and GPT difficulty profiles are strongly aligned at the skill level (r = 0.881), but not at the instance level (r = 0.016) or lexical-item level (r = -0.142), a pattern we describe as shared taxonomy, independent execution. Pairwise agreement further suggests that GPT is better understood as an independent third skill voice than as a direct human substitute. Open-source failures are concentrated in schema-to-skill execution problems. These findings suggest that automatic annotation should be evaluated in terms of skill feasibility rather than task-level automation.

---


### 97. [Zero-Shot Retail Theft Detection via Orchestrated Vision Models: A Model-Agnostic, Cost-Effective Alternative to Trained Single-Model Systems](https://arxiv.org/abs/2604.14846)

**<font color=#1a73e8>作者：</font>** Haileab Yagersew  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retail theft costs the global economy over \$100 billion annually, yet existing AI-based detection systems require expensive custom model training on proprietary datasets and charge \$200-500/month per store. We present Paza, a zero-shot retail theft detection framework that achieves practical concealment detection without training any model. Our approach orchestrates multiple existing models in a layered pipeline - cheap object detection and pose estimation running continuously, with an expensive vision-language model (VLM) invoked only when behavioral pre-filters trigger. A multi-signal suspicion pre-filter (requiring dwell time plus at least one behavioral signal) reduces VLM invocations by 240x compared to per-frame analysis, bounding calls to <=10/minute and enabling a single GPU to serve 10-20 stores. The architecture is model-agnostic: the VLM component accepts any OpenAI-compatible endpoint, enabling operators to swap between models such as Gemma 4, Qwen3.5-Omni, GPT-4o, or future releases without code changes - ensuring the system improves as the VLM landscape evolves. We evaluate the VLM component on the DCSASS synthesized shoplifting dataset (169 clips, controlled environment), achieving 89.5% precision and 92.8% specificity at 59.3% recall zero-shot - where the recall gap is attributable to sparse frame sampling in offline evaluation rather than VLM reasoning failures, as precision and specificity are the operationally critical metrics determining false alarm rates. We present a detailed cost model showing viability at \$50-100/month per store (3-10x cheaper than commercial alternatives), and introduce a privacy-preserving design that obfuscates faces in the detection pipeline. The source code is available at this https URL.

---


### 98. [TrigReason: Trigger-Based Collaboration between Small and Large Reasoning Models](https://arxiv.org/abs/2604.14847)

**<font color=#1a73e8>作者：</font>** Yi Zhao, Yajuan Peng, Cam-Tu Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) achieve strong performance on complex tasks through extended chains of thought but suffer from high inference latency due to autoregressive reasoning. Recent work explores using Small Reasoning Models (SRMs) to accelerate LRM inference. In this paper, we systematically characterize the capability boundaries of SRMs and identify three common types of reasoning risks: (1) path divergence, where SRMs lack the strategic ability to construct an initial plan, causing reasoning to deviate from the most probable path; (2) cognitive overload, where SRMs fail to solve particularly difficult steps; and (3) recovery inability, where SRMs lack robust self-reflection and error correction mechanisms. To address these challenges, we propose TrigReason, a trigger-based collaborative reasoning framework that replaces continuous polling with selective intervention. TrigReason delegates most reasoning to the SRM and activates LRM intervention only when necessary-during initial strategic planning (strategic priming trigger), upon detecting extraordinary overconfidence (cognitive offload trigger), or when reasoning falls into unproductive loops (intervention request trigger). The evaluation results on AIME24, AIME25, and GPQA-D indicate that TrigReason matches the accuracy of full LRMs and SpecReason, while offloading 1.70x - 4.79x more reasoning steps to SRMs. Under edge-cloud conditions, TrigReason reduces latency by 43.9\% and API cost by 73.3\%. Our code is available at \href{this https URL}{this https URL}

---


### 99. [Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization](https://arxiv.org/abs/2604.14853)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhai, Bingcong Li, Bingnan Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time compute scaling, the practice of spending extra computation during inference via repeated sampling, search, or extended reasoning, has become a powerful lever for improving large language model performance. Yet deploying these techniques under finite inference budgets requires a decision that current systems largely ignore: which inputs deserve more compute, and which can be answered cheaply? We formalize this as a constrained optimization problem (maximize expected accuracy subject to an average compute budget) and solve it with a two-stage Solve-then-Learn pipeline. In the solve stage, Lagrangian relaxation decomposes the global constraint into per-instance sub-problems, each admitting a closed-form oracle action that optimally prices accuracy against cost. We prove that the induced cost is monotone in the dual variable, enabling exact budget targeting via binary search. In the learn stage, a lightweight classifier is trained to predict oracle actions from cheap input features, amortizing the allocation rule for real-time deployment. We establish that the task-level regret of the learned policy is bounded by its imitation error times the worst-case per-instance gap, yielding a clean reduction from constrained inference to supervised classification. Experiments on MATH and GSM8K with three LLMs (DeepSeek-V3, GPT-4o-mini, Qwen2.5-7B) show that our method consistently outperforms uniform and heuristic allocation baselines, achieving up to 12.8% relative accuracy improvement on MATH under matched budget constraints, while closely tracking the Lagrangian oracle upper bound with over 91% imitation accuracy.

---


### 100. [Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding](https://arxiv.org/abs/2604.14862)

**<font color=#1a73e8>作者：</font>** Yifan Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Constrained decoding has been widely adopted for structured generation with large language models (LLMs), ensuring that outputs satisfy predefined formats such as JSON and XML. However, existing approaches largely treat schemas as purely structural constraints and overlook the possibility that their linguistic formulation may affect model behavior. In this work, we study how instruction placement influences model performance in structured generation and show that merely changing the wording of schema keys, without modifying the prompt or model parameters, can significantly alter model performance under constrained decoding. Based on this observation, we propose to reinterpret structured generation as a multi-channel instruction problem, where instructions can be conveyed explicitly through prompts and implicitly through schema keys during decoding. To the best of our knowledge, this is the first work to systematically study how schema key formulation acts as an implicit instruction channel and affects model performance under constrained decoding. Experiments on multiple mathematical reasoning benchmarks show that different model families exhibit distinct sensitivities to these instruction channels: Qwen models consistently benefit from schema-level instructions, while LLaMA models rely more heavily on prompt-level guidance. We further observe non-additive interaction effects between instruction channels, showing that combining multiple channels does not always lead to further improvement. These findings suggest that schema design not only determines output structure, but also carries instruction signals, offering a new perspective on structured generation in LLMs.

---


### 101. [Segment-Level Coherence for Robust Harmful Intent Probing in LLMs](https://arxiv.org/abs/2604.14865)

**<font color=#1a73e8>作者：</font>** Xuanli He, Bilgehan Sel, Faizan Ali 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly exposed to adaptive jailbreaking, particularly in high-stakes Chemical, Biological, Radiological, and Nuclear (CBRN) domains. Although streaming probes enable real-time monitoring, they still make systematic errors. We identify a core issue: existing methods often rely on a few high-scoring tokens, leading to false alarms when sensitive CBRN terms appear in benign contexts. To address this, we introduce a streaming probing objective that requires multiple evidence tokens to consistently support a prediction, rather than relying on isolated spikes. This encourages more robust detection based on aggregated signals instead of single-token cues. At a fixed 1% false-positive rate, our method improves the true-positive rate by 35.55% relative to strong streaming baselines. We further observe substantial gains in AUROC, even when starting from near-saturated baseline performance (AUROC = 97.40%). We also show that probing Attention or MLP activations consistently outperforms residual-stream features. Finally, even when adversarial fine-tuning enables novel character-level ciphers, harmful intent remains detectable: probes developed for the base LLMs can be applied ``plug-and-play'' to these obfuscated attacks, achieving an AUROC of over 98.85%.

---


### 102. [MetaDent: Labeling Clinical Images for Vision-Language Models in Dentistry](https://arxiv.org/abs/2604.14866)

**<font color=#1a73e8>作者：</font>** Meng-Xun Li, Wen-Hui Deng, Zhi-Xing Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated significant potential in medical image analysis, yet their application in intraoral photography remains largely underexplored due to the lack of fine-grained, annotated datasets and comprehensive benchmarks. To address this, we present MetaDent, a comprehensive resource that includes (1) a novel and large-scale dentistry image dataset collected from clinical, public, and web sources; (2) a semi-structured annotation framework designed to capture the hierarchical and clinically nuanced nature of dental photography; and (3) comprehensive benchmark suites for evaluating state-of-the-art VLMs on clinical image understanding. Our labeling approach combines a high-level image summary with point-by-point, free-text descriptions of abnormalities. This method enables rich, scalable, and task-agnostic representations. We curated 60,669 dental images from diverse sources and annotated a representative subset of 2,588 images using this meta-labeling scheme. Leveraging Large Language Models (LLMs), we derive standardized benchmarks: approximately 15K Visual Question Answering (VQA) pairs and an 18-class multi-label classification dataset, which we validated with human review and error analysis to justify that the LLM-driven transition reliably preserves fidelity and semantic accuracy. We then evaluate state-of-the-art VLMs across VQA, classification, and image captioning tasks. Quantitative results reveal that even the most advanced models struggle with a fine-grained understanding of intraoral scenes, achieving moderate accuracy and producing inconsistent or incomplete descriptions in image captioning. We publicly release our dataset, annotations, and tools to foster reproducible research and accelerate the development of vision-language systems for dental applications.

---


### 103. [Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis](https://arxiv.org/abs/2604.14877)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhai, Wenjing Yan, Xiaodan Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Does reinforcement learning genuinely expand what LLM agents can do, or merely make them more reliable? For static reasoning, recent work answers the second: base and RL pass@k curves converge at large k. We ask whether this holds for agentic tool use, where T rounds of interaction enable compositional strategies that re-sampling cannot recover. We introduce PASS@(k,T), a two-dimensional metric that jointly varies sampling budget k and interaction depth T, separating capability expansion from efficiency improvement. Our main finding is that, contrary to the static-reasoning result, tool-use RL genuinely enlarges the capability boundary: the RL agent's pass-curve pulls above the base model's and the gap widens at large k rather than converging. The expansion is specific to compositional, sequential information gathering; on simpler tasks RL behaves as prior work predicts. Under matched training data, supervised fine-tuning regresses the boundary on the same compositional tasks, isolating self-directed exploration as the causal factor. Mechanism analysis shows RL reweights the base strategy distribution toward the subset whose downstream reasoning more often yields a correct answer, with the improvement concentrated on how the agent integrates retrieved information. These results reconcile optimistic and pessimistic readings of RL for LLMs: both are correct, on different task types.

---


### 104. [Reasoning Dynamics and the Limits of Monitoring Modality Reliance in Vision-Language Models](https://arxiv.org/abs/2604.14888)

**<font color=#1a73e8>作者：</font>** Danae Sánchez Villegas, Samuel Lewis-Lim, Nikolaos Aletras 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision language models (VLMs) offer reasoning capabilities, yet how these unfold and integrate visual and textual information remains unclear. We analyze reasoning dynamics in 18 VLMs covering instruction-tuned and reasoning-trained models from two different model families. We track confidence over Chain-of-Thought (CoT), measure the corrective effect of reasoning, and evaluate the contribution of intermediate reasoning steps. We find that models are prone to answer inertia, in which early commitments to a prediction are reinforced, rather than revised during reasoning steps. While reasoning-trained models show stronger corrective behavior, their gains depend on modality conditions, from text-dominant to vision-only settings. Using controlled interventions with misleading textual cues, we show that models are consistently influenced by these cues even when visual evidence is sufficient, and assess whether this influence is recoverable from CoT. Although this influence can appear in the CoT, its detectability varies across models and depends on what is being monitored. Reasoning-trained models are more likely to explicitly refer to the cues, but their longer and fluent CoTs can still appear visually grounded while actually following textual cues, obscuring modality reliance. In contrast, instruction-tuned models refer to the cues less explicitly, but their shorter traces reveal inconsistencies with the visual input. Taken together, these findings indicate that CoT provides only a partial view of how different modalities drive VLM decisions, with important implications for the transparency and safety of multimodal systems.

---


### 105. [Can LLMs Score Medical Diagnoses and Clinical Reasoning as well as Expert Panels?](https://arxiv.org/abs/2604.14892)

**<font color=#1a73e8>作者：</font>** Amy Rouillard, Sitwala Mundiab, Linda Camarab 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating medical AI systems using expert clinician panels is costly and slow, motivating the use of large language models (LLMs) as alternative adjudicators. Here, we evaluate an LLM jury composed of three frontier AI models scoring 3333 diagnoses on 300 real-world middle-income country (MIC) hospital cases. Model performance was benchmarked against expert clinician panel and independent human re-scoring panel evaluations. Both LLM and clinician-generated diagnoses are scored across four dimensions: diagnosis, differential diagnosis, clinical reasoning and negative treatment risk. For each of these, we assess scoring difference, inter-rater agreement, scoring stability, severe safety errors and the effect of post-hoc calibration. We find that: (i) the uncalibrated LLM jury scores are systematically lower than clinician panels scores; (ii) the LLM Jury preserves ordinal agreement and exhibits better concordance with the primary expert panels than the human expert re-score panels do; (iii) the probability of severe errors is lower in \lj models compared to the human expert re-score panels; (iv) the LLM Jury shows excellent agreement with primary expert panels' rankings. We find that the LLM jury combined with AI model diagnoses can be used to identify ward diagnoses at high risk of error, enabling targeted expert review and improved panel efficiency; (v) LLM jury models show no self-preference bias. They did not score diagnoses generated by their own underlying model or models from the same vendor more (or less) favourably than those generated by other models. Finally, we demonstrate that LLM jury calibration using isotonic regression improves alignment with human expert panel evaluations. Together, these results provide compelling evidence that a calibrated, multi-model LLM jury can serve as a trustworthy and reliable proxy for expert clinician evaluation in medical AI benchmarking.

---


### 106. [Beyond Importance Sampling: Rejection-Gated Policy Optimization](https://arxiv.org/abs/2604.14895)

**<font color=#1a73e8>作者：</font>** Ziwu Sun, Zhen Gao, Jiyong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a new perspective on policy optimization: rather than reweighting all samples by their importance ratios, an optimizer should select which samples are trustworthy enough to drive a policy update. Building on this view, we introduce Rejection-Gated Policy Optimization (RGPO), which replaces the importance sampling ratio r_theta = pi_theta / pi_old with a smooth, differentiable acceptance gate alpha_theta(s, a) = g(r_theta(s, a)) in the range [0, 1]. Unlike prior work that applies rejection sampling as a data-level heuristic before training, RGPO elevates rejection to an optimization principle: the gate participates directly in gradient computation and is implicitly updated alongside the policy. RGPO provides a unified framework: the policy gradients of TRPO, PPO, and REINFORCE all correspond to specific choices of the effective gradient weight w(r) = g'(r) * r. We prove that RGPO guarantees finite, bounded gradient variance even when importance sampling ratios are heavy-tailed (where IS variance diverges). We further show that RGPO incurs only a bounded, controllable bias and provides an approximate monotonic policy improvement guarantee analogous to TRPO. RGPO matches PPO in computational cost, requires no second-order optimization, and extends naturally to RLHF-style preference alignment. In online preference fine-tuning of Qwen2.5-1.5B-Instruct on Anthropic HH-RLHF (n = 3 seeds), RGPO uses a dual-ratio gate that anchors learning to both the previous policy and the reference model, achieving a Pareto-dominant outcome: the highest reward among online RL methods (+14.8% vs. PPO-RLHF) and the lowest KL divergence to the reference model (-16.0% vs. PPO-RLHF, -53.1% vs. GRPO).

---


### 107. [Toward Agentic RAG for Ukrainian](https://arxiv.org/abs/2604.14896)

**<font color=#1a73e8>作者：</font>** Marta Sumyk, Oleksandr Kosovan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an initial investigation into Agentic Retrieval-Augmented Generation (RAG) for Ukrainian, conducted within the UNLP 2026 Shared Task on Multi-Domain Document Understanding. Our system combines two-stage retrieval (BGE-M3 with BGE reranking) with a lightweight agentic layer performing query rephrasing and answer-retry loops on top of Qwen2.5-3B-Instruct. Our analysis reveals that retrieval quality is the primary bottleneck: agentic retry mechanisms improve answer accuracy but the overall score remains constrained by document and page identification. We discuss practical limitations of offline agentic pipelines and outline directions for combining stronger retrieval with more advanced agentic reasoning for Ukrainian.

---


### 108. [ADAPT: Benchmarking Commonsense Planning under Unspecified Affordance Constraints](https://arxiv.org/abs/2604.14902)

**<font color=#1a73e8>作者：</font>** Pei-An Chen, Yong-Ching Liang, Jia-Fong Yeh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intelligent embodied agents should not simply follow instructions, as real-world environments often involve unexpected conditions and exceptions. However, existing methods usually focus on directly executing instructions, without considering whether the target objects can actually be manipulated, meaning they fail to assess available affordances. To address this limitation, we introduce DynAfford, a benchmark that evaluates embodied agents in dynamic environments where object affordances may change over time and are not specified in the instruction. DynAfford requires agents to perceive object states, infer implicit preconditions, and adapt their actions accordingly. To enable this capability, we introduce ADAPT, a plug-and-play module that augments existing planners with explicit affordance reasoning. Experiments demonstrate that incorporating ADAPT significantly improves robustness and task success across both seen and unseen environments. We also show that a domain-adapted, LoRA-finetuned vision-language model used as the affordance inference backend outperforms a commercial LLM (GPT-4o), highlighting the importance of task-aligned affordance grounding.

---


### 109. [IE as Cache: Information Extraction Enhanced Agentic Reasoning](https://arxiv.org/abs/2604.14930)

**<font color=#1a73e8>作者：</font>** Hang Lv, Sheng Liang, Hongchao Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Information Extraction aims to distill structured, decision-relevant information from unstructured text, serving as a foundation for downstream understanding and reasoning. However, it is traditionally treated merely as a terminal objective: once extracted, the resulting structure is often consumed in isolation rather than maintained and reused during multi-step inference. Moving beyond this, we propose \textit{IE-as-Cache}, a framework that repurposes IE as a cognitive cache to enhance agentic reasoning. Drawing inspiration from hierarchical computer memory, our approach combines query-driven extraction with cache-aware reasoning to dynamically maintain compact intermediate information and filter noise. Experiments on challenging benchmarks across diverse LLMs demonstrate significant improvements in reasoning accuracy, indicating that IE can be effectively repurposed as a reusable cognitive resource and offering a promising direction for future research on downstream uses of IE.

---


### 110. [WavAlign: Enhancing Intelligence and Expressiveness in Spoken Dialogue Models via Adaptive Hybrid Post-Training](https://arxiv.org/abs/2604.14932)

**<font color=#1a73e8>作者：</font>** Yifu Chen, Shengpeng Ji, Qian Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> End-to-end spoken dialogue models have garnered significant attention because they offer a higher potential ceiling in expressiveness and perceptual ability than cascaded systems. However, the intelligence and expressiveness of current open-source spoken dialogue models often remain below expectations. Motivated by the success of online reinforcement learning(RL) in other domains, one might attempt to directly apply preference optimization to spoken dialogue models, yet this transfer is non-trivial. We analyze these obstacles from the perspectives of reward modeling and rollout sampling, focusing on how sparse preference supervision interacts with dense speech generation under shared-parameter updates. Based on the analysis, we propose a modality-aware adaptive post-training recipe that makes RL practical for spoken dialogue: it constrains preference updates to the semantic channel and improves acoustic behavior via explicit anchoring, while dynamically regulating their mixture from rollout statistics to avoid unreliable preference gradients. We evaluate the method across multiple spoken dialogue benchmarks and representative architectures, and observe consistent improvements in semantic quality and speech expressiveness.

---


### 111. [Text2Arch: A Dataset for Generating Scientific Architecture Diagrams from Natural Language Descriptions](https://arxiv.org/abs/2604.14941)

**<font color=#1a73e8>作者：</font>** Shivank Garg, Sankalp Mittal, Manish Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Communicating complex system designs or scientific processes through text alone is inefficient and prone to ambiguity. A system that automatically generates scientific architecture diagrams from text with high semantic fidelity can be useful in multiple applications like enterprise architecture visualization, AI-driven software design, and educational content creation. Hence, in this paper, we focus on leveraging language models to perform semantic understanding of the input text description to generate intermediate code that can be processed to generate high-fidelity architecture diagrams. Unfortunately, no clean large-scale open-access dataset exists, implying lack of any effective open models for this task. Hence, we contribute a comprehensive dataset, \system, comprising scientific architecture images, their corresponding textual descriptions, and associated DOT code representations. Leveraging this resource, we fine-tune a suite of small language models, and also perform in-context learning using GPT-4o. Through extensive experimentation, we show that \system{} models significantly outperform existing baseline models like DiagramAgent and perform at par with in-context learning-based generations from GPT-4o. We make the code, data and models publicly available.

---


### 112. [RaTA-Tool: Retrieval-based Tool Selection with Multimodal Large Language Models](https://arxiv.org/abs/2604.14951)

**<font color=#1a73e8>作者：</font>** Gabriele Mattioli, Evelyn Turri, Sara Sarto 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tool learning with foundation models aims to endow AI systems with the ability to invoke external resources -- such as APIs, computational utilities, and specialized models -- to solve complex tasks beyond the reach of standalone language generation. While recent advances in Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) have expanded their reasoning and perception capabilities, existing tool-use methods are predominantly limited to text-only inputs and closed-world settings. Consequently, they struggle to interpret multimodal user instructions and cannot generalize to tools unseen during training. In this work, we introduce RaTA-Tool, a novel framework for open-world multimodal tool selection. Rather than learning direct mappings from user queries to fixed tool identifiers, our approach enables an MLLM to convert a multimodal query into a structured task description and subsequently retrieve the most appropriate tool by matching this representation against semantically rich, machine-readable tool descriptions. This retrieval-based formulation naturally supports extensibility to new tools without retraining. To further improve alignment between task descriptions and tool selection, we incorporate a preference-based optimization stage using Direct Preference Optimization (DPO). To support research in this setting, we also introduce the first dataset for open-world multimodal tool use, featuring standardized tool descriptions derived from Hugging Face model cards. Extensive experiments demonstrate that our approach significantly improves tool-selection performance, particularly in open-world, multimodal scenarios.

---


### 113. [Calibration-Gated LLM Pseudo-Observations for Online Contextual Bandits](https://arxiv.org/abs/2604.14961)

**<font color=#1a73e8>作者：</font>** Maksim Pershin, Ivan Golovanov, Pavel Baltabaev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual bandit algorithms suffer from high regret during cold-start, when the learner has insufficient data to distinguish good arms from bad. We propose augmenting Disjoint LinUCB with LLM pseudo-observations: after each round, a large language model predicts counterfactual rewards for the unplayed arms, and these predictions are injected into the learner as weighted pseudo-observations. The injection weight is controlled by a calibration-gated decay schedule that tracks the LLM's prediction accuracy on played arms via an exponential moving average; high calibration error suppresses the LLM's influence, while accurate predictions receive higher weight during the critical early rounds. We evaluate on two contextual bandit environments - UCI Mushroom (2-arm, asymmetric rewards) and MIND-small (5-arm news recommendation) - and find that when equipped with a task-specific prompt, LLM pseudo-observations reduce cumulative regret by 19% on MIND relative to pure LinUCB. However, generic counterfactual prompt framing increases regret on both environments, demonstrating that prompt design is the dominant factor, more important than the choice of decay schedule or calibration gating parameters. We analyze the failure modes of calibration gating on domains with small prediction errors and provide a theoretical motivation for the bias-variance trade-off governing pseudo-observation weight.

---


### 114. [UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards](https://arxiv.org/abs/2604.14967)

**<font color=#1a73e8>作者：</font>** Jun Wang, Shuo Tan, Zelong Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) extends Large Vision-Language Models (LVLMs) with external visual knowledge. However, existing visual RAG systems typically rely on generic retrieval signals that overlook the fine-grained visual semantics essential for complex reasoning. To address this limitation, we propose UniDoc-RL, a unified reinforcement learning framework in which an LVLM agent jointly performs retrieval, reranking, active visual perception, and reasoning. UniDoc-RL formulates visual information acquisition as a sequential decision-making problem with a hierarchical action space. Specifically, it progressively refines visual evidence from coarse-grained document retrieval to fine-grained image selection and active region cropping, allowing the model to suppress irrelevant content and attend to information-dense regions. For effective end-to-end training, we introduce a dense multi-reward scheme that provides task-aware supervision for each action. Based on Group Relative Policy Optimization (GRPO), UniDoc-RL aligns agent behavior with multiple objectives without relying on a separate value network. To support this training paradigm, we curate a comprehensive dataset of high-quality reasoning trajectories with fine-grained action annotations. Experiments on three benchmarks demonstrate that UniDoc-RL consistently surpasses state-of-the-art baselines, yielding up to 17.7% gains over prior RL-based methods.

---


### 115. [Discovering Novel LLM Experts via Task-Capability Coevolution](https://arxiv.org/abs/2604.14969)

**<font color=#1a73e8>作者：</font>** Andrew Dai, Boris Meinardus, Ciaran Regan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier model developers aim to train models continually to possess emergent, diverse capabilities. To extend capabilities, the current pre-training and post-training paradigm requires manually starting training runs with static datasets or reward functions every time. Addressing this limitation, our work pursues the insight that open-endedness (via the coevolution of models and tasks) can discover models with increasingly novel skills in a single run. We introduce a new model development framework that extends coevolution to large language model (LLM) discovery, open-ended \textit{Assessment Coevolving with Diverse Capabilities} (AC/DC). AC/DC evolves both LLMs via model merging and natural language tasks via synthetic data generation. AC/DC discovers growing archives of LLMs that surpass the capabilities of larger LLMs while taking up less GPU memory. In particular, our LLM populations achieve a broader Coverage of expertise than other curated models or baselines on downstream benchmarks, without \textit{any} explicit benchmark optimization. Furthermore, AC/DC improves Coverage over time, continually innovates on tasks and models, and improves performance in multi-agent best-of-N selection. Our findings highlight the potential of coevolution as a means of discovering broader sets of capabilities from base LLMs. Overall, AC/DC brings us one step closer to a profoundly new paradigm of LLM development, where continual improvements to the diversity of model capabilities can be accelerated by leveraging existing models as stepping stones to increasingly powerful models.

---


### 116. [Explain the Flag: Contextualizing Hate Speech Beyond Censorship](https://arxiv.org/abs/2604.14970)

**<font color=#1a73e8>作者：</font>** Jason Liartis, Eirini Kaldeli, Lambrini Gyftokosta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hate, derogatory, and offensive speech remains a persistent challenge in online platforms and public discourse. While automated detection systems are widely used, most focus on censorship or removal, raising concerns for transparency and freedom of expression, and limiting opportunities to explain why content is harmful. To address these issues, explanatory approaches have emerged as a promising solution, aiming to make hate speech detection more transparent, accountable, and informative. In this paper, we present a hybrid approach that combines Large Language Models (LLMs) with three newly created and curated vocabularies to detect and explain hate speech in English, French, and Greek. Our system captures both inherently derogatory expressions tied to identity characteristics and direct group-targeted content through two complementary pipelines: one that detects and disambiguates problematic terms using the curated vocabularies, and one that leverages LLMs as context-aware evaluators of group-targeting content. The outputs are fused into grounded explanations that clarify why content is flagged. Human evaluation shows that our hybrid approach is accurate, with high-quality explanations, outperforming LLM-only baselines.

---


### 117. [Agentic Explainability at Scale: Between Corporate Fears and XAI Needs](https://arxiv.org/abs/2604.14984)

**<font color=#1a73e8>作者：</font>** Yomna Elsayed, Cecily Jones  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As companies enter the race for agentic AI adoption, fears surface around agentic autonomy and its subsequent risks. These fears compound as companies scale their agentic AI adoption with low-code applications, without a comparable scaling in their governance processes and expertise resulting in a phenomenon known as "Agent Sprawl". While shadow AI tools can help with agentic discovery and identification, few observability tools offer insights into the agents' configuration and settings or the decision-making process during agent-to-agent communication and orchestration. This paper explores AI governance professionals' concerns in enterprise settings, while offering design-time and runtime explainability techniques as suggested by AI governance experts for addressing those fears. Finally, we provide a preliminary prototype of an Agentic AI Card that can help companies feel at ease deploying agents at scale.

---


### 118. [Dr.~RTL: Autonomous Agentic RTL Optimization through Tool-Grounded Self-Improvement](https://arxiv.org/abs/2604.14989)

**<font color=#1a73e8>作者：</font>** Wenji Fang, Yao Lu, Shang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have sparked growing interest in automatic RTL optimization for better performance, power, and area (PPA). However, existing methods are still far from realistic RTL optimization. Their evaluation settings are often unrealistic: they are tested on manually degraded, small-scale RTL designs and rely on weak open-source tools. Their optimization methods are also limited, relying on coarse design-level feedback and simple pre-defined rewriting rules. To address these limitations, we present Dr. RTL, an agentic framework for RTL timing optimization in a realistic evaluation environment, with continual self-improvement through reusable optimization skills. We establish a realistic evaluation setting with more challenging RTL designs and an industrial EDA workflow. Within this setting, Dr. RTL performs closed-loop optimization through a multi-agent framework for critical-path analysis, parallel RTL rewriting, and tool-based evaluation. We further introduce group-relative skill learning, which compares parallel RTL rewrites and distills the optimization experience into an interpretable skill library. Currently, this library contains 47 pattern--strategy entries for cross-design reuse to improve PPA and accelerate convergence, and it can continue evolving over time. Evaluated on 20 real-world RTL designs, Dr. RTL achieves average WNS/TNS improvements of 21\%/17\% with a 6\% area reduction over the industry-leading commercial synthesis tool.

---


### 119. [The Possibility of Artificial Intelligence Becoming a Subject and the Alignment Problem](https://arxiv.org/abs/2604.14990)

**<font color=#1a73e8>作者：</font>** Till Mossakowski, Helena Esther Grass  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial General Intelligence (AGI) is increasingly being discussed not only as a tool, but also as a potential subject with personal and therefore moral status. In our opinion, the currently dominant alignment strategies, which focus on human control and containment of AI, therefore fall short. Building on Turing's analogy of "child machines", we are developing a vision of the possibility of autonomy-supporting parenting of AI, in which human control over a developing AGI is gradually reduced, allowing AI to become an independent, autonomous subject. Rather than viewing AGI, as is currently prevalent, as a dangerous creature that needs to be locked up and controlled, we should approach potential AGI with respect for a possible developing subject on the one hand, and with full confidence in our human capabilities on the other. Such a perspective opens up the possibility of cooperative coexistence and co-evolution between humans and AGIs. The relationship between humans and AGIs will thus have to be newly determined, which will change our self-image as humans. It will be crucial that humans not only claim control over potential AGIs, but also engage with AGIs through surprise, creativity, and other specifically human qualities, thereby offering them motivating incentives for cooperation.

---


### 120. [Predicting Power-System Dynamic Trajectories with Foundation Models](https://arxiv.org/abs/2604.14991)

**<font color=#1a73e8>作者：</font>** Haoran Li, Lihao Mai, Chenhan Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As power systems transition toward renewable-rich and inverter-dominated operations, accurate time-domain dynamic analysis becomes increasingly critical. Such analysis supports key operational tasks, including transient stability assessment, dynamic security analysis, contingency screening, and post-fault trajectory evaluation. In practice, these tasks may operate under several challenges, including unknown and time-varying system parameters, privacy constraints on data sharing, and the need for fast online inference. Existing learning-based approaches are typically trained for individual systems and therefore lack generalization across operating conditions and physical parameters. Hence, this paper proposes LArge Scale Small ODE (LASS)-ODE-Power, a learning framework for general-purpose time-domain prediction. The proposed approach leverages large-scale pretraining on more than 40 GB of DAE or ordinary differential-equation (ODE) trajectories to learn transferable representations. The resulting model supports trajectory prediction from short measurement prefixes across diverse dynamic regimes, including electromechanical and inverter-driven systems. Hence, the model can be directly used without data sharing in a zero-shot setting. In addition, the proposed architecture incorporates parallel and linearized computation to achieve fast inference. Moreover, to enhance task-specific performance in power systems, a specialized fine-tuning strategy is developed based on approximately 1 GB of heterogeneous power-system dynamic data. Extensive experiments over diverse power-system simulation scenarios demonstrate that LASS-ODE-Power consistently outperforms existing learning-based models in trajectory prediction accuracy with efficient inference.

---


### 121. [COEVO: Co-Evolutionary Framework for Joint Functional Correctness and PPA Optimization in LLM-Based RTL Generation](https://arxiv.org/abs/2604.15001)

**<font color=#1a73e8>作者：</font>** Heng Ping, Peiyu Zhang, Shixuan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based RTL code generation methods increasingly target both functional correctness and PPA quality, yet existing approaches universally decouple the two objectives, optimizing PPA only after correctness is fully achieved. Whether through sequential multi-agent pipelines, evolutionary search with binary correctness gates, or hierarchical reward dependencies, partially correct but architecturally promising candidates are systematically discarded. Moreover, existing methods reduce the multi-objective PPA space to a single scalar fitness, obscuring the trade-offs among area, delay, and power. To address these limitations, we propose COEVO, a co-evolutionary framework that unifies correctness and PPA optimization within a single evolutionary loop. COEVO formulates correctness as a continuous co-optimization dimension alongside area, delay, and power, enabled by an enhanced testbench that provides fine-grained scoring and detailed diagnostic feedback. An adaptive correctness gate with annealing allows PPA-promising but partially correct candidates to guide the search toward jointly optimal solutions. To preserve the full PPA trade-off structure, COEVO employs four-dimensional Pareto-based non-dominated sorting with configurable intra-level sorting, replacing scalar fitness without manual weight tuning. Evaluated on VerilogEval 2.0 and RTLLM 2.0, COEVO achieves 97.5\% and 94.5\% Pass@1 with GPT-5.4-mini, surpassing all agentic baselines across four LLM backbones, while attaining the best PPA on 43 out of 49 synthesizable RTLLM designs.

---


### 122. [Towards Faster Language Model Inference Using Mixture-of-Experts Flow Matching](https://arxiv.org/abs/2604.15009)

**<font color=#1a73e8>作者：</font>** Aihua Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Flow matching retains the generation quality of diffusion models while enabling substantially faster inference, making it a compelling paradigm for generative modeling. However, when applied to language modeling, it exhibits fundamental limitations in representing complex latent distributions with irregular geometries, such as anisotropy and multimodality. To address these challenges, we propose a mixture-of-experts flow matching (MoE-FM) framework, which captures complex global transport geometries in latent space by decomposing them into locally specialized vector fields. Building on MoE-FM, we develop a non-autoregressive (NAR) language modeling approach, named YAN, instantiated with both Transformer and Mamba architectures. Across multiple downstream tasks, YAN achieves generation quality on par with both autoregressive (AR) and diffusion-based NAR language models, while requiring as few as three sampling steps. This yields a $40\times$ speedup over AR baselines and up to a $10^3\times$ speedup over diffusion language models, demonstrating substantial efficiency advantages for language modeling.

---


### 123. [DLink: Distilling Layer-wise and Dominant Knowledge from EEG Foundation Models](https://arxiv.org/abs/2604.15016)

**<font color=#1a73e8>作者：</font>** Jingyuan Wang, Meiyan Xu, Zhihao Jia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models (FMs) achieve strong cross-subject and cross-task generalization but impose substantial computational and memory costs that hinder deployment on embedded BCI systems. Knowledge distillation is a natural solution; however, conventional methods fail for EEG FMs because task-relevant semantics are often distributed across intermediate layers, and aggressive dimensionality reduction can distort oscillatory structure via representational collapse and aliasing. To address these challenges, we propose DLink (Distilling Layer-wise and Dominant Knowledge), a unified framework for transferring knowledge from large EEG FMs to compact students with three key innovations: (1) a dynamic Router that adaptively aggregates teacher layers to capture dominant intermediate representations; (2) an EEG MiC student with a Mimic-then-Compress pipeline, which inherits high-dimensional teacher features and then applies structured spatio-temporal compression to avoid a heavy classification head; and (3) spectral distillation that aligns teacher-student representations in the frequency domain to regularize compression and mitigate aliasing and temporal jitter. Experiments on four EEG benchmarks show that DLink enables compact students to outperform lightweight baselines while approaching fully fine-tuned FM performance at substantially lower model size and inference cost.

---


### 124. [From Reactive to Proactive: Assessing the Proactivity of Voice Agents via ProVoice-Bench](https://arxiv.org/abs/2604.15037)

**<font color=#1a73e8>作者：</font>** Ke Xu, Yuhao Wang, Yu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in LLM agents are gradually shifting from reactive, text-based paradigms toward proactive, multimodal interaction. However, existing benchmarks primarily focus on reactive responses, overlooking the complexities of proactive intervention and monitoring. To bridge this gap, we introduce ProVoice-Bench, the first evaluation framework specifically designed for proactive voice agents, featuring four novel tasks. By leveraging a multi-stage data synthesis pipeline, we curate 1,182 high-quality samples for rigorous testing. Our evaluation of state-of-the-art Multimodal LLMs reveals a significant performance gap, particularly regarding over-triggering and reasoning capabilities. These findings highlight the limitations of current models and offer a roadmap for developing more natural, context-aware proactive agents.

---


### 125. [Beyond Visual Cues: Semantic-Driven Token Filtering and Expert Routing for Anytime Person ReID](https://arxiv.org/abs/2604.15090)

**<font color=#1a73e8>作者：</font>** Jiaxuan Li, Xin Wen, Zhihang Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Any-Time Person Re-identification (AT-ReID) necessitates the robust retrieval of target individuals under arbitrary conditions, encompassing both modality shifts (daytime and nighttime) and extensive clothing-change scenarios, ranging from short-term to long-term intervals. However, existing methods are highly relying on pure visual features, which are prone to change due to environmental and time factors, resulting in significantly performance deterioration under scenarios involving illumination caused modality shifts or cloth-change. In this paper, we propose Semantic-driven Token Filtering and Expert Routing (STFER), a novel framework that leverages the ability of Large Vision-Language Models (LVLMs) to generate identity consistency text, which provides identity-discriminative features that are robust to both clothing variations and cross-modality shifts between RGB and IR. Specifically, we employ instructions to guide the LVLM in generating identity-intrinsic semantic text that captures biometric constants for the semantic model driven. The text token is further used for Semantic-driven Visual Token Filtering (SVTF), which enhances informative visual regions and suppresses redundant background noise. Meanwhile, the text token is also used for Semantic-driven Expert Routing (SER), which integrates the semantic text into expert routing, resulting in more robust multi-scenario gating. Extensive experiments on the Any-Time ReID dataset (AT-USTC) demonstrate that our model achieves state-of-the-art results. Moreover, the model trained on AT-USTC was evaluated across 5 widely-used ReID benchmarks demonstrating superior generalization capabilities with highly competitive results. Our code will be available soon.

---


### 126. [OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis](https://arxiv.org/abs/2604.15093)

**<font color=#1a73e8>作者：</font>** Kanzhi Cheng, Zehao Li, Zheng Ma 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile agents powered by vision-language models have demonstrated impressive capabilities in automating mobile tasks, with recent leading models achieving a marked performance leap, e.g., nearly 70% success on AndroidWorld. However, these systems keep their training data closed and remain opaque about their task and trajectory synthesis recipes. We present OpenMobile, an open-source framework that synthesizes high-quality task instructions and agent trajectories, with two key components: (1) The first is a scalable task synthesis pipeline that constructs a global environment memory from exploration, then leverages it to generate diverse and grounded instructions. and (2) a policy-switching strategy for trajectory rollout. By alternating between learner and expert models, it captures essential error-recovery data often missing in standard imitation learning. Agents trained on our data achieve competitive results across three dynamic mobile agent benchmarks: notably, our fine-tuned Qwen2.5-VL and Qwen3-VL reach 51.7% and 64.7% on AndroidWorld, far surpassing existing open-data approaches. Furthermore, we conduct transparent analyses on the overlap between our synthetic instructions and benchmark test sets, and verify that performance gains stem from broad functionality coverage rather than benchmark overfitting. We release data and code at this https URL to bridge the data gap and facilitate broader mobile agent research.

---


### 127. [IUQ: Interrogative Uncertainty Quantification for Long-Form Large Language Model Generation](https://arxiv.org/abs/2604.15109)

**<font color=#1a73e8>作者：</font>** Haozhi Fan, Jinhao Duan, Kaidi Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the rapid advancement of Large Language Models (LLMs), uncertainty quantification in LLM generation is a persistent challenge. Although recent approaches have achieved strong performance by restricting LLMs to produce short or constrained answer sets, many real-world applications require long-form and free-form text generation. A key difficulty in this setting is that LLMs often produce responses that are semantically coherent yet factually inaccurate, while the underlying semantics are multifaceted and the linguistic structure is complex. To tackle this challenge, this paper introduces Interrogative Uncertainty Quantification (IUQ), a novel framework that leverages inter-sample consistency and intra-sample faithfulness to quantify the uncertainty in long-form LLM outputs. By utilizing an interrogate-then-respond paradigm, our method provides reliable measures of claim-level uncertainty and the model's faithfulness. Experimental results across diverse model families and model sizes demonstrate the superior performance of IUQ over two widely used long-form generation datasets. The code is available at this https URL.

---


### 128. [Blinded Multi-Rater Comparative Evaluation of a Large Language Model and Clinician-Authored Responses in CGM-Informed Diabetes Counseling](https://arxiv.org/abs/2604.15124)

**<font color=#1a73e8>作者：</font>** Zhijun Guo, Alvina Lai, Emmanouil Korakas 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous glucose monitoring (CGM) is central to diabetes care, but explaining CGM patterns clearly and empathetically remains time-intensive. Evidence for retrieval-grounded large language model (LLM) systems in CGM-informed counseling remains limited. To evaluate whether a retrieval-grounded LLM-based conversational agent (CA) could support patient understanding of CGM data and preparation for routine diabetes consultations. We developed a retrieval-grounded LLM-based CA for CGM interpretation and diabetes counseling support. The system generated plain-language responses while avoiding individualized therapeutic advice. Twelve CGM-informed cases were constructed from publicly available datasets. Between Oct 2025 and Feb 2026, 6 senior UK diabetes clinicians each reviewed 2 assigned cases and answered 24 questions. In a blinded multi-rater evaluation, each CA-generated and clinician-authored response was independently rated by 3 clinicians on 6 quality dimensions. Safety flags and perceived source labels were also recorded. Primary analyses used linear mixed-effects models. A total of 288 unique responses (144 CA and 144 clinician) generated 864 ratings. The CA received higher quality scores than clinician responses (mean 4.37 vs 3.58), with an estimated mean difference of 0.782 points (95% CI 0.692-0.872; P<.001). The largest differences were for empathy (1.062, 95% CI 0.948-1.177) and actionability (0.992, 95% CI 0.877-1.106). Safety flag distributions were similar, with major concerns rare in both groups (3/432, 0.7% each). Retrieval-grounded LLM systems may have value as adjunct tools for CGM review, patient education, and preconsultation preparation. However, these findings do not support autonomous therapeutic decision-making or unsupervised real-world use.

---


### 129. [DiscoTrace: Representing and Comparing Answering Strategies of Humans and LLMs in Information-Seeking Question Answering](https://arxiv.org/abs/2604.15140)

**<font color=#1a73e8>作者：</font>** Neha Srikanth, Jordan Boyd-Graber, Rachel Rudinger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce DiscoTrace, a method to identify the rhetorical strategies that answerers use when responding to information-seeking questions. DiscoTrace represents answers as a sequence of question-related discourse acts paired with interpretations of the original question, annotated on top of rhetorical structure theory parses. Applying DiscoTrace to answers from nine different human communities reveals that communities have diverse preferences for answer construction. In contrast, LLMs do not exhibit rhetorical diversity in their answers, even when prompted to mimic specific human community answering guidelines. LLMs also systematically opt for breadth, addressing interpretations of questions that human answerers choose not to address. Our findings can guide the development of pragmatic LLM answerers that consider a range of strategies informed by context in QA.

---


### 130. [IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning](https://arxiv.org/abs/2604.15148)

**<font color=#1a73e8>作者：</font>** Zihan Liang, Yufei Ma, Ben Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has emerged as an effective paradigm for training large language models to perform search-augmented reasoning. However, existing approaches rely on trajectory-level rewards that cannot distinguish precise search queries from vague or redundant ones within a rollout group, and collapse to a near-zero gradient signal whenever every sampled trajectory fails. In this paper, we propose IG-Search, a reinforcement learning framework that introduces a step-level reward based on Information Gain (IG). For each search step, IG measures how much the retrieved documents improve the model's confidence in the gold answer relative to a counterfactual baseline of random documents, thereby reflecting the effectiveness of the underlying search query. This signal is fed back to the corresponding search-query tokens via per-token advantage modulation in GRPO, enabling fine-grained, step-level credit assignment within a rollout. Unlike prior step-level methods that require either externally annotated intermediate supervision or shared environment states across trajectories, IG-Search derives its signals from the policy's own generation probabilities, requiring no intermediate annotations beyond standard question-answer pairs. Experiments on seven single-hop and multi-hop QA benchmarks demonstrate that IG-Search achieves an average EM of 0.430 with Qwen2.5-3B, outperforming the strongest trajectory-level baseline (MR-Search) by 1.6 points and the step-level method GiGPO by 0.9 points on average across benchmarks, with particularly pronounced gains on multi-hop reasoning tasks. Despite introducing a dense step-level signal, IG-Search adds only ~6.4% to per-step training wall-clock time over the trajectory-level baseline and leaves inference latency unchanged, while still providing a meaningful gradient signal even when every sampled trajectory answers incorrectly.

---


### 131. [LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)

**<font color=#1a73e8>作者：</font>** Lukas Helff, Quentin Delfosse, David Steinmann 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As reinforcement Learning with Verifiable Rewards (RLVR) has become the dominant paradigm for scaling reasoning capabilities in LLMs, a new failure mode emerges: LLMs gaming verifiers. We study this phenomenon on inductive reasoning tasks, where models must induce and output logical rules. We find that RLVR-trained models systematically abandon rule induction. Instead of learning generalizable patterns (e.g., ``trains carrying red cars go east''), they enumerate instance-level labels, producing outputs that pass verifiers without capturing the relational patterns required by the task. We show that this behavior is not a failure of understanding but a form of reward hacking: imperfect verifiers that check only extensional correctness admit false positives. To detect such shortcuts, we introduce Isomorphic Perturbation Testing (IPT), which evaluates a single model output under both extensional and isomorphic verification, where the latter enforces invariance under logically isomorphic tasks. While genuine rule induction remains invariant, shortcut strategies fail. We find that shortcut behavior is specific to RLVR-trained reasoning models (e.g., GPT-5, Olmo3) and absent in non-RLVR models (e.g., GPT-4o, GPT-4.5, Ministral). Moreover, shortcut prevalence increases with task complexity and inference-time compute. In controlled training experiments, extensional verification directly induces shortcut strategies, while isomorphic verification eliminates them. These results show that RLVR can incentivize reward hacking not only through overt manipulation but also by exploiting what the verifier fails to enforce.

---


### 132. [QuantCode-Bench: A Benchmark for Evaluating the Ability of Large Language Models to Generate Executable Algorithmic Trading Strategies](https://arxiv.org/abs/2604.15151)

**<font color=#1a73e8>作者：</font>** Alexey Khoroshilov, Alexey Chernysh, Orkhan Ekhtibarov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have demonstrated strong performance on general-purpose programming tasks, yet their ability to generate executable algorithmic trading strategies remains underexplored. Unlike standard code benchmarks, trading-strategy generation requires simultaneous mastery of domain-specific financial logic, knowledge of a specialized API, and the ability to produce code that is not only syntactically correct but also leads to actual trades on historical data. In this work, we present QuantCode-Bench, a benchmark for the systematic evaluation of modern LLMs in generating strategies for the Backtrader framework from textual descriptions in English. The benchmark contains 400 tasks of varying difficulty collected from Reddit, TradingView, StackExchange, GitHub, and synthetic sources. Evaluation is conducted through a multi-stage pipeline that checks syntactic correctness, successful backtest execution, the presence of trades, and semantic alignment with the task description using an LLM judge. We compare state-of-the-art models in two settings: single-turn, where the strategy must be generated correctly on the first attempt, and agentic multi-turn, where the model receives iterative feedback and may repair its errors. We analyze the failure modes across different stages of the pipeline and show that the main limitations of current models are not related to syntax, but rather to the correct operationalization of trading logic, proper API usage, and adherence to task semantics. These findings suggest that trading strategy generation constitutes a distinct class of domain-specific code generation tasks in which success requires not only technical correctness, but also alignment between natural-language descriptions, financial logic, and the observable behavior of the strategy on data.

---


### 133. [Compressing Sequences in the Latent Embedding Space: $K$-Token Merging for Large Language Models](https://arxiv.org/abs/2604.15153)

**<font color=#1a73e8>作者：</font>** Zihao Xu, John Harvill, Ziwei Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) incur significant computational and memory costs when processing long prompts, as full self-attention scales quadratically with input length. Token compression aims to address this challenge by reducing the number of tokens representing inputs. However, existing prompt-compression approaches primarily operate in token space and overlook inefficiencies in the latent embedding space. In this paper, we propose K-Token Merging, a latent-space compression framework that merges each contiguous block of K token embeddings into a single embedding via a lightweight encoder. The compressed sequence is processed by a LoRA-adapted LLM, while generation remains in the original vocabulary. Experiments on structural reasoning (Textualized Tree), sentiment classification (Amazon Reviews), and code editing (CommitPackFT) show that K-Token Merging lies on the Pareto frontier of performance vs. compression, achieving up to 75% input length reduction with minimal performance degradation.

---


### 134. [Assessing the Potential of Masked Autoencoder Foundation Models in Predicting Downhole Metrics from Surface Drilling Data](https://arxiv.org/abs/2604.15169)

**<font color=#1a73e8>作者：</font>** Aleksander Berezowski, Hassan Hassanzadeh, Gouri Ginde  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Oil and gas drilling operations generate extensive time-series data from surface sensors, yet accurate real-time prediction of critical downhole metrics remains challenging due to the scarcity of labelled downhole measurements. This systematic mapping study reviews thirteen papers published between 2015 and 2025 to assess the potential of Masked Autoencoder Foundation Models (MAEFMs) for predicting downhole metrics from surface drilling data. The review identifies eight commonly collected surface metrics and seven target downhole metrics. Current approaches predominantly employ neural network architectures such as artificial neural networks (ANNs) and long short-term memory (LSTM) networks, yet no studies have explored MAEFMs despite their demonstrated effectiveness in time-series modeling. MAEFMs offer distinct advantages through self-supervised pre-training on abundant unlabeled data, enabling multi-task prediction and improved generalization across wells. This research establishes that MAEFMs represent a technically feasible but unexplored opportunity for drilling analytics, recommending future empirical validation of their performance against existing models and exploration of their broader applicability in oil and gas operations.

---


### 135. [VisPCO: Visual Token Pruning Configuration Optimization via Budget-Aware Pareto-Frontier Learning for Vision-Language Models](https://arxiv.org/abs/2604.15188)

**<font color=#1a73e8>作者：</font>** Huawei Ji, Yuanhao Sun, Yuan Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning methods effectively mitigate the quadratic computational growth caused by processing high-resolution images and video frames in vision-language models (VLMs). However, existing approaches rely on predefined pruning configurations without determining whether they achieve computation-performance optimality. In this work, we introduce , a novel framework that formulates visual token pruning as a Pareto configuration optimization problem to automatically identify optimal configurations. Our approach employs continuous relaxation and straight-through estimators to enable gradient-based search, solved via the Augmented Lagrangian method. Extensive experiments across 8 visual benchmarks demonstrate that effectively approximates the empirical Pareto frontier obtained through grid search and generalizes well across various pruning methods and VLM architectures. Furthermore, through learnable kernel functions, we investigate layer-wise pruning patterns and reveal that multi-step progressive pruning captures VLMs' hierarchical compression structure, achieving superior accuracy-efficiency trade-offs compared to single-layer approaches.

---


### 136. [Learning to Think Like a Cartoon Captionist: Incongruity-Resolution Supervision for Multimodal Humor Understanding](https://arxiv.org/abs/2604.15210)

**<font color=#1a73e8>作者：</font>** Hatice Merve Vural, Doga Kukul, Ege Erdem Ozlu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humor is one of the few cognitive tasks where getting the reasoning right matters as much as getting the answer right. While recent work evaluates humor understanding on benchmarks such as the New Yorker Cartoon Caption Contest (NYCC), it largely treats it as black-box prediction, overlooking the structured reasoning processes underlying humor comprehension. We introduce IRS (Incongruity-Resolution Supervision), a framework that decomposes humor understanding into three components: incongruity modeling, which identifies mismatches in the visual scene; resolution modeling, which constructs coherent reinterpretations of these mismatches; and preference alignment, which evaluates candidate interpretations under human judgments. Grounded in incongruity-resolution theory and expert captionist practice, IRS supervises intermediate reasoning process through structured traces that make the path from visual perception to humorous interpretation explicit and learnable. Across 7B, 32B, and 72B models on NYCC, IRS outperforms strong open and closed multimodal baselines across caption matching and ranking tasks, with our largest model approaching expert-level performance on ranking. Zero-shot transfer to external benchmarks shows that IRS learns generalizable reasoning patterns. Our results suggest that supervising reasoning structure, rather than scale alone, is key for reasoning-centric tasks.

---


### 137. [UrbanClipAtlas: A Visual Analytics Framework for Event and Scene Retrieval in Urban Videos](https://arxiv.org/abs/2604.15225)

**<font color=#1a73e8>作者：</font>** Joel Perca, Luis Sante, Juanpablo Heredia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Extracting actionable insights from long-duration urban videos is often labor-intensive: analysts must manually sift through raw footage to pinpoint target events or uncover broader behavioral trends. In this work, we present URBANCLIPATLAS, a visual analytics system for exploring long urban videos recorded at street intersections. URBANCLIPATLAS combines retrieval-augmented generation (RAG), taxonomy-aware entity extraction, and video grounding to support event retrieval and interpretation. The system segments extended recordings into short clips, generates textual descriptions with a vision-language model, and indexes them for semantic retrieval. A knowledge graph maps entities and relations from LLM answers onto a domain-specific taxonomy and aligns them with detected objects and trajectories to support visual grounding and verification. URBANCLIPATLAS supports scene retrieval through an augmented chat-based interface and improves scene interpretation by tightly aligning textual outputs with video evidence. This design strengthens the connection between textual reasoning and visual evidence, reducing the effort required to validate model outputs and refine hypotheses. We demonstrate the usefulness of URBANCLIPATLAS on the StreetAware dataset through two case studies involving hazardous scenarios and crossing dynamics at street intersections. URBANCLIPATLAS helps analysts reason about safety- and mobility-related patterns across large urban video collections.

---


### 138. [Why Do Vision Language Models Struggle To Recognize Human Emotions?](https://arxiv.org/abs/2604.15280)

**<font color=#1a73e8>作者：</font>** Madhav Agarwal, Sotirios A. Tsaftaris, Laura Sevilla-Lara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding emotions is a fundamental ability for intelligent systems to be able to interact with humans. Vision-language models (VLMs) have made tremendous progress in the last few years for many visual tasks, potentially offering a promising solution for understanding emotions. However, it is surprising that even the most sophisticated contemporary VLMs struggle to recognize human emotions or to outperform even specialized vision-only classifiers. In this paper we ask the question "Why do VLMs struggle to recognize human emotions?", and observe that the inherently continuous and dynamic task of facial expression recognition (DFER) exposes two critical VLM vulnerabilities. First, emotion datasets are naturally long-tailed, and the web-scale data used to pre-train VLMs exacerbates this head-class bias, causing them to systematically collapse rare, under-represented emotions into common categories. We propose alternative sampling strategies that prevent favoring common concepts. Second, temporal information is critical for understanding emotions. However, VLMs are unable to represent temporal information over dense frame sequences, as they are limited by context size and the number of tokens that can fit in memory, which poses a clear challenge for emotion recognition. We demonstrate that the sparse temporal sampling strategy used in VLMs is inherently misaligned with the fleeting nature of micro-expressions (0.25-0.5 seconds), which are often the most critical affective signal. As a diagnostic probe, we propose a multi-stage context enrichment strategy that utilizes the information from "in-between" frames by first converting them into natural language summaries. This enriched textual context is provided as input to the VLM alongside sparse keyframes, preventing attentional dilution from excessive visual data while preserving the emotional trajectory.

---


### 139. [How Do LLMs and VLMs Understand Viewpoint Rotation Without Vision? An Interpretability Study](https://arxiv.org/abs/2604.15294)

**<font color=#1a73e8>作者：</font>** Zhen Yang, Ping Jian, Zhongbin Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Over the past year, spatial intelligence has drawn increasing attention. Many prior works study it from the perspective of visual-spatial intelligence, where models have access to visuospatial information from visual inputs. However, in the absence of visual information, whether linguistic intelligence alone is sufficient to endow models with spatial intelligence, and how models perform relevant tasks with text-only inputs still remain unexplored. Therefore, in this paper, we focus on a fundamental and critical capability in spatial intelligence from a linguistic perspective: viewpoint rotation understanding (VRU). Specifically, LLMs and VLMs are asked to infer their final viewpoint and predict the corresponding observation in an environment given textual description of viewpoint rotation and observation over multiple steps. We find that both LLMs and VLMs perform poorly on our proposed dataset while human can easily achieve 100% accuracy, indicating a substantial gap between current model capabilities and the requirements of spatial intelligence. To uncover the underlying mechanisms, we conduct a layer-wise probing analysis and head-wise causal intervention. Our findings reveal that although models encode viewpoint information in the hidden states, they appear to struggle to bind the viewpoint position with corresponding observation, resulting in a hallucination in final layers. Finally, we selectively fine-tune the key attention heads identified by causal intervention to improve VRU performance. Experimental results demonstrate that such selective fine-tuning achieves improved VRU performance while avoiding catastrophic forgetting of generic abilities. Our dataset and code will be released at this https URL .

---


### 140. [Diagnosing LLM Judge Reliability: Conformal Prediction Sets and Transitivity Violations](https://arxiv.org/abs/2604.15302)

**<font color=#1a73e8>作者：</font>** Manan Gupta, Dhruv Kumar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-judge frameworks are increasingly used for automatic NLG evaluation, yet their per-instance reliability remains poorly understood. We present a two-pronged diagnostic toolkit applied to SummEval: $\textbf{(1)}$ a transitivity analysis that reveals widespread per-input inconsistency masked by low aggregate violation rates ($\bar{\rho} = 0.8$-$4.1\%$), with $33$-$67\%$ of documents exhibiting at least one directed 3-cycle; and $\textbf{(2)}$ split conformal prediction sets over 1-5 Likert scores providing theoretically-guaranteed $\geq(1{-}\alpha)$ coverage, with set width serving as a per-instance reliability indicator ($r_s = {+}0.576$, $N{=}1{,}918$, $p < 10^{-100}$, pooled across all judges). Critically, prediction set width shows consistent cross-judge agreement ($\bar{r} = 0.32$-$0.38$), demonstrating it captures document-level difficulty rather than judge-specific noise. Across four judges and four criteria, both diagnostics converge: criterion matters more than judge, with relevance judged most reliably (avg. set size $\approx 3.0$) and coherence moderately so (avg. set size $\approx 3.9$), while fluency and consistency remain unreliable (avg. set size $\approx 4.9$). We release all code, prompts, and cached results.

---


### 141. [Generalization in LLM Problem Solving: The Case of the Shortest Path](https://arxiv.org/abs/2604.15306)

**<font color=#1a73e8>作者：</font>** Yao Tong, Jiayuan Ye, Anastasia Borovykh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whether language models can systematically generalize remains actively debated. Yet empirical performance is jointly shaped by multiple factors such as training data, training paradigms, and inference-time strategies, making failures difficult to interpret. We introduce a controlled synthetic environment based on shortest-path planning, a canonical composable sequential optimization problem. The setup enables clean separation of these factors and supports two orthogonal axes of generalization: spatial transfer to unseen maps and length scaling to longer-horizon problems. We find that models exhibit strong spatial transfer but consistently fail under length scaling due to recursive instability. We further analyze how distinct stages of the learning pipeline influence systematic problem-solving: for example, data coverage sets capability limits; reinforcement learning improves training stability but does not expand those limits; and inference-time scaling enhances performance but cannot rescue length-scaling failures.

---


### 142. [MM-WebAgent: A Hierarchical Multimodal Web Agent for Webpage Generation](https://arxiv.org/abs/2604.15309)

**<font color=#1a73e8>作者：</font>** Yan Li, Zezi Zeng, Yifan Yang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid progress of Artificial Intelligence Generated Content (AIGC) tools enables images, videos, and visualizations to be created on demand for webpage design, offering a flexible and increasingly adopted paradigm for modern UI/UX. However, directly integrating such tools into automated webpage generation often leads to style inconsistency and poor global coherence, as elements are generated in isolation. We propose MM-WebAgent, a hierarchical agentic framework for multimodal webpage generation that coordinates AIGC-based element generation through hierarchical planning and iterative self-reflection. MM-WebAgent jointly optimizes global layout, local multimodal content, and their integration, producing coherent and visually consistent webpages. We further introduce a benchmark for multimodal webpage generation and a multi-level evaluation protocol for systematic assessment. Experiments demonstrate that MM-WebAgent outperforms code-generation and agent-based baselines, especially on multimodal element generation and integration. Code & Data: this https URL.

---


### 143. [LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories](https://arxiv.org/abs/2604.15311)

**<font color=#1a73e8>作者：</font>** Zhanhao Liang, Tao Yang, Jie Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper focuses on the alignment of flow matching models with human preferences. A promising way is fine-tuning by directly backpropagating reward gradients through the differentiable generation process of flow matching. However, backpropagating through long trajectories results in prohibitive memory costs and gradient explosion. Therefore, direct-gradient methods struggle to update early generation steps, which are crucial for determining the global structure of the final image. To address this issue, we introduce LeapAlign, a fine-tuning method that reduces computational cost and enables direct gradient propagation from reward to early generation steps. Specifically, we shorten the long trajectory into only two steps by designing two consecutive leaps, each skipping multiple ODE sampling steps and predicting future latents in a single step. By randomizing the start and end timesteps of the leaps, LeapAlign leads to efficient and stable model updates at any generation step. To better use such shortened trajectories, we assign higher training weights to those that are more consistent with the long generation path. To further enhance gradient stability, we reduce the weights of gradient terms with large magnitude, instead of completely removing them as done in previous works. When fine-tuning the Flux model, LeapAlign consistently outperforms state-of-the-art GRPO-based and direct-gradient methods across various metrics, achieving superior image quality and image-text alignment.

---


- [返回当日日报目录](./index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
