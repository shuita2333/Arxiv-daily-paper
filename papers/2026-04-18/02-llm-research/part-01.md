# 🧠 大模型相关研究 | 2026年04月18日

> 本类共 **143** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-143](./part-03.md)

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


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-143](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
