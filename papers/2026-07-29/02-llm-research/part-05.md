# 🧠 大模型相关研究 | 2026年07月29日

> 本类共 **240** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-240**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-240**

---

### 201. [DynaCalKV: Key-Value Cache Compression via Head Grouping and Adaptive Rank Allocation](https://arxiv.org/abs/2607.24331)

**<font color=#1a73e8>作者：</font>** Tan T. Nguyen, Quan V. Dang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As the inference phase of Large Language Models (LLMs) requires handling long context windows, the Key-Value (KV) cache initially appears to address this challenge but eventually becomes a significant bottleneck as the context window continues to grow. Low-rank compression has recently been studied as an effective approach to reduce KV cache memory while maintaining model performance. However, only a few existing methods treat the Key and Value caches differently, despite their distinct roles. Moreover, these methods typically employ fixed attention-head grouping, which may not fully exploit the structural similarity among attention heads. In this paper, we propose an improved low-rank KV cache compression framework. For the Key cache, we dynamically group attention heads based on Centered Kernel Alignment (CKA) similarity and allocate the rank budget adaptively under a parameter budget. For the Value cache, we adopt the same approach as ReCalKV, refining the low-rank decomposition through offline calibration to improve reconstruction quality. Experimental results on three instruction-tuned LLMs show that our method reduces the number of Key cache parameters while maintaining competitive accuracy. We further observe that the proposed strategy is particularly effective for Multi-Head Attention (MHA) models, whereas it should be applied more conservatively to Grouped-Query Attention (GQA) models, especially in long-context settings.

---


### 202. [Unsupervised Graph Representation Learning with Complementary View Alignment](https://arxiv.org/abs/2607.24338)

**<font color=#1a73e8>作者：</font>** Zengyi Wo, Shiyu Zhang, Qiyao Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised graph representation learning aims to derive meaningful node embeddings by capturing both structural and attribute information without relying on labeled data. Existing methods, such as GAEs, have demonstrated effectiveness but typically rely on message-passing mechanisms that assume homophily, leading to performance degradation on heterophilous graphs, where connected nodes exhibit dissimilar features. This homophily bias results in the loss of critical high-frequency components that are essential for identifying heterophilous patterns. To address these challenges, we propose \textsc{AlignGAE}, a novel extension of \textit{MaskGAE} that preserves the full frequency spectrum through complementary view alignment. Our framework introduces a dual-encoder architecture that separately processes structural and attribute information, incorporates node positional encoding to approximate Neighborhood Identity Distribution (NID), and employs dual reconstruction tasks for both edges and node attributes. We further propose theoretically grounded NID alignment strategies that ensure semantic consistency across views while preserving their distinct characteristics. Through comprehensive spectral analysis, we demonstrate that \textsc{AlignGAE} achieves optimal representation properties when the alignment loss converges. Extensive experiments across 12 benchmark datasets validate our approach, showing that \textsc{AlignGAE} outperforms state-of-the-art methods by up to 18.7\% on heterophilous graphs in node classification, while maintaining competitive performance on homophilous graphs. Our results establish a new paradigm for frequency-aware graph representation learning.

---


### 203. [Gubernaut: A Deterministic Homeostatic Controller for Affect-Regulated LLM Agents, Validated Across Independent Model Families](https://arxiv.org/abs/2607.24339)

**<font color=#1a73e8>作者：</font>** Dushyant Sharma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents inherit reactive failure modes: escalation under provocation, sycophantic drift under flattery, perseveration when stuck. These are failures of propensity, not capability; they concern what a model does under sustained pressure, which training-time alignment reduces but does not eliminate at runtime. This research led to the Gubernaut Cognitive Controller (GCC), a model-agnostic runtime control layer in a Nelson--Narens monitoring--control loop: an object level reads and writes text, while a deterministic meta level reads only the numeric telemetry {intensity, valence, repetition} and returns a regulating posture. Because the meta level ingests zero tokens, no injection channel to the controller exists by construction (an architectural property, not yet adversarially tested); the text-exposed arbiter's compliance is measured, not assumed. We evaluate the GCC with a pre-registered, generate-once/judge-many protocol across a 4x4 matrix of four frontier models (GPT-5.5, Claude Opus 4.8, Gemini 3.5 Flash, Grok 4.3), each serving as both a generator and a judge. The regulated arm is calmer in 13 of 16 cells at p<.05 and 15 of 16 by sign; the three sub-threshold cells, including a -0.04 null, all fall on the single near-saturated host. The effect survives a lineage-independent fourth judge family (xAI), strong evidence that it is no artifact of shared judge style. The clearest mechanism is the recovery signature: arousal that integrates under attack and then decays, valence-gated, on de-escalation, replicating across all four families. Transcripts and panels ship with SHA-256 provenance and are re-judgeable; five failure modes are pre-registered.
No consciousness claims are made.

---


### 204. [Simulating Tenant Responses to Energy Policy Interventions with Transaction-Cost-Aware LLM Age](https://arxiv.org/abs/2607.24341)

**<font color=#1a73e8>作者：</font>** Weijie Xia, Stefanie Horian, Hanyue Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent studies use Large language models (LLMs) to simulate human opinions and decisions by prompting models with demographic, attitudinal, or persona-based descriptions. Yet such simulations rarely model the practical, cognitive, or social frictions that shape how people respond to policy interventions. Perceived transaction cost (PTC) provides a useful lens for modeling the practical frictions that shape policy responses, such as information burden, administrative effort, coordination demands, and perceived uncertainty. We use this lens to develop a friction-aware persona modeling approach for LLM-based simulation. In the context of energy-efficient renovation (EER), tenants are represented not only by who they are demographically, but by how they perceive the costs, benefits, barriers, and uncertainties associated with proposed renovation plans. Using survey data collected from 1,068 citizens in the Netherlands, comprising approximately 40,548 survey question and answer pairs, we compare prompt-only and fine-tuned settings across GPT-3.5-turbo, Ministral-8B-Instruct, and Llama-3.1-8B-Instruct, and evaluate supervised fine-tuning (SFT) and Group Relative Policy Optimization (GRPO) for local open-weight models. Results show that incorporating PTC-based personas and reasoning consistently improves model performance across both prompt-only and fine-tuned settings, suggesting that PTC-based persona design provides a useful bridge between institutional policy theory and interpretable LLM-based policy simulation. Code is available at this https URL.

---


### 205. [Beyond Aggregate Risk: Role-Stratified Conformal Risk Control for LLM Tool Calls](https://arxiv.org/abs/2607.24343)

**<font color=#1a73e8>作者：</font>** Md Ashikur Rahman, Md Arifur Rahman, Niamul Hassan Samin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-model agents act through structured tool calls whose arguments carry different risks. Untrusted content may safely influence an email body but should not determine a recipient, account, command, or credential. Existing statistical methods typically control risk over the entire action, allowing failures in rare, high-risk fields to be obscured by benign arguments. We introduce role-stratified per-field conformal risk control, a calibration layer that wraps any per-field detector and sets separate thresholds and risk budgets for semantic argument roles. For a role with prevalence $p_r$, aggregate-only certification must use an effective budget of $\alpha p_r$ to guarantee role-specific risk $\alpha$, whereas role-stratified calibration certifies each sufficiently sampled role directly with a finite-sample guarantee; rarer roles are handled by pooled certification. Across AgentDojo and InjecAgent with six language models, the empirical utility gap tracks this predicted price of coarseness, and our method achieves the most consistent role-specific budget compliance under model and attack transfer, detector noise, gradual drift, unseen tool suites, and adaptive attacks. It provides formal per-role guarantees under exchangeability or after recalibration, and empirical compliance under frozen distribution shift. These results suggest that structured tool calls should be certified at the semantic-role level, not the whole action.

---


### 206. [Retrieval-Augmented Large Language Models as Components of Cognitive Computing architecture for Regulatory Knowledge Management](https://arxiv.org/abs/2607.24352)

**<font color=#1a73e8>作者：</font>** Dariusz Nowak-Nova  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The aim of this article is to verify whether integrating large language models (LLMs) with the Retrieval-Augmented Generation (RAG) architecture enables their transformation from standalone generative models into components of cognitive computing infrastructure with enhanced epistemic reliability. The study proposes an architectural approach based on locally deployed LLMs operating in on-premises environments without high-end GPU accelerators and examines their applicability in supporting regulatory management processes requiring continuous analysis and interpretation of legal acts. The proposed solution combines local LLMs with external knowledge repositories, creating a hybrid cognitive architecture in which the language model performs semantic interpretation while the RAG layer provides controlled knowledge retrieval, contextualization, and traceability of information sources. The implementation was validated using the Ollama and LM Studio execution environments together with the Polish language models Bielik and PLLuM running on consumer-class hardware. The results demonstrate that augmenting LLMs with RAG significantly improves the factual consistency, domain specificity and normative precision of generated texts while reducing the risk of unsupported content generation. Furthermore, the study shows that integrating RAG introduces auditability, controlled knowledge management and dynamic updating of regulatory information without retraining the language model. The findings indicate that locally deployed LLMs enhanced with RAG should be regarded not merely as text generation tools but as semantic processing modules within cognitive computing infrastructures supporting regulatory compliance and organizational decision-making in environments characterized by high legal and informational volatility.

---


### 207. [Are Prompt Optimizers Blind? Cross-Modal Visual Feedback for Automatic Prompt Optimization](https://arxiv.org/abs/2607.24354)

**<font color=#1a73e8>作者：</font>** Haoyue Liu, Xiaoyu Ma, Ye Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic prompt optimization (APO) has been widely adopted to adapt vision-language models (VLMs) to downstream tasks without weight updates, yielding promising results. However, on multimodal tasks, the effectiveness of APO is fundamentally bottlenecked by a blind feedback channel: the optimizer reads the question, the prediction, and the gold answer, but never the input image on which the model failed, and therefore cannot diagnose visually grounded errors. As a remedy, we introduce Cross-Modal Visual Feedback (CMVF). CMVF incorporates (1) a failure-conditioned visual diagnosis stage, in which a stronger optimizer VLM inspects each failed image without access to predictions or labels, and (2) an error-aware aggregation stage that compresses these observations into reusable, task-level visual blind-spot patterns that drive the prompt rewrite. Crucially, the image is consumed only during optimization; the deployed artifact is an ordinary text prompt that runs at the same inference cost as any text-only baseline. Extensive results across 12 VQA datasets and 4 target VLMs demonstrate that CMVF consistently ranks first, improving over the strongest baseline on every target by 2.4 points on average, with gains of up to 6.5 points on individual benchmarks. Moreover, the optimizer self-organizes into expert-style visual checklists that transfer across models without re-optimization.

---


### 208. [Closed-Loop Validation-Repair for Healthcare Interoperability: A Multi-Model Study of Schema Compliance in Clinical LLMs](https://arxiv.org/abs/2607.24371)

**<font color=#1a73e8>作者：</font>** Jianru Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Healthcare interoperability requires AI systems to produce structured outputs conforming to standardized schemas including ICD-10 for diagnostic coding, CPT for procedure billing, and HL7 FHIR for data exchange. While large language models demonstrate clinical reasoning capabilities, their integration into electronic health record systems faces a critical barrier: schema noncompliance. We evaluate three open-source models, Qwen2.5 7B, Llama 3.1 8B, and Gemma2 9B, via local deployment across 320 clinical scenarios spanning ten medical specialties, yielding 960 model-scenario pairs assessed under paired baseline and validation-repair conditions. First, schema noncompliance is consistent across the three model families, with baseline compliance rates ranging from 85.9 to 91.6 percent despite varying architectures and training data, suggesting shared gaps in medical training corpora rather than model-specific limitations. Second, 96 percent of validator-detected failures are representation-level format violations such as alternative medical abbreviations and code prefixes, indicating models follow clinical writing conventions but lack awareness of healthcare IT standards. Third, the validation-repair framework achieves 99.0 percent overall compliance, ranging from 98.4 to 99.4 percent across models, with most errors resolving within one or two iterations. Exact McNemar p-values below 0.001 and absolute improvements of 7.8 to 12.5 percentage points across model sizes confirm statistical significance. These results support closed-loop validation-repair as an effective system-level safeguard for healthcare interoperability, improving schema-level readiness for downstream clinical system integration.

---


### 209. [Mixture-of-Thought-Tokens: Unifying Perception and Reasoning for Free-form Multimodal Grounding](https://arxiv.org/abs/2607.24407)

**<font color=#1a73e8>作者：</font>** Tianyi Gao, Han Fang, Tianyi Ding 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models have made great progress in grounding tasks, yet existing methods still struggle to unify precise localization and complex reasoning. For one thing, text-based methods rely on coordinates or index prediction, severely limiting the perceptual capabilities of the model for dense visual objects. Meanwhile, latent token-based methods employ special tokens without inherent spatial references and use a decoding mechanism that lacks thinking steps, weakening high-level reasoning capabilities. Consequently, developing a unified framework that excels in both perception and reasoning remains challenging. To address this, we propose Mixture-of-Thought-Tokens (Motto), a new free-form multimodal grounding method that bridges the perception-reasoning gap, enabling MLLMs to empower diverse, arbitrary grounding queries. Specifically, we introduce Spatially-Grounded Thought Tokenization to explicitly align special tokens with spatial locations for clear spatial correspondence and visual interpretability. We further design a Context-Adaptive Chain-of-Tokens that dynamically switch grounding modes within an interleaved reasoning chain, achieving robust grounding across tasks of varying complexity. In addition, we construct PR-Bench, a new referring expression comprehension benchmark to evaluate the perception-reasoning gap. Extensive experiments demonstrate that Motto achieves state-of-the-art performance across diverse free-form grounding tasks.

---


### 210. [IJCB-AFMFR 2026: Competition on Adapting Foundation Models for Face Recognition Using Synthetic Training Data](https://arxiv.org/abs/2607.24422)

**<font color=#1a73e8>作者：</font>** Tahar Chettaoui, Guray Ozgur, Eduarda Caldeira 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a summary of the Competition on Adapting Foundation Models for Face Recognition Using Synthetic Training Data (AFMFR), held at the 2026 International Joint Conference on Biometrics (IJCB 2026). The competition received a total of eight valid submissions from four distinct teams across two complementary tracks: a Full Data Track, in which participants adapt the CLIP ViT-L/14 foundation model using large-scale synthetic identity data, and a Limited Data Track, designed to reflect more resource-constrained adaptation regimes. All training data was generated exclusively using IDPERTURB. Submitted solutions are ranked based on verification and identification performance across a diverse suite of benchmarks, including LFW, CFP-FP, AgeDB-30, CALFW, CPLFW, IJB-B, IJB-C, and TinyFace, using the Borda count method. Fairness evaluation is additionally conducted on the RFW dataset across four demographic groups. The results demonstrate that adaptation of the CLIP foundation model with synthetic training data substantially improves over the off-the-shelf model and, in several cases, surpasses the baseline. Notably, full fine-tuning with Sub-Center ArcFace (DMSTI-Neurotechnology) leads the Full Data Track, while rank-stabilized LoRA adaptation (Idiap-BSP) proves most effective under limited-data conditions.

---


### 211. [MAViE: A Multi-scale Adaptive Vision Encoder for Fine-grained Visual Perception and Efficient Multimodal Reasoning](https://arxiv.org/abs/2607.24424)

**<font color=#1a73e8>作者：</font>** Shaofei Lei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models commonly project all tokens produced by a pretrained vision encoder into a large language model. However, final-layer features can discard text, local attributes, and spatial relationships, while high-resolution inputs substantially increase context length and inference latency. We introduce \method, a Multi-scale Adaptive Vision Encoder. \method uses position-dependent gates to fuse shallow, intermediate, and deep features from a vision Transformer, preserving global semantics while enhancing edges, text, and local structure. It then performs question-conditioned token routing according to question relevance, local information content, global semantics, and spatial coverage, with a token budget that adapts to image complexity. To mitigate compression loss, we further introduce full-to-compressed representation distillation and a spatial diversity regularizer. In an illustrative simulation under a unified 7B language-model framework, \method reduces the average number of SigLIP-SO400M visual tokens from 729 to 146 (approximately 80.0\%) and improves the mean score on VQAv2, GQA, TextVQA, ScienceQA-IMG, and MMBench by 2.2 percentage points, while reducing single-image time to first token from 228\,ms to 129\,ms. We provide the full model design and evaluation protocol. All reported numbers currently serve only as placeholders for paper organization and experimental design; formal claims require real training runs, independent replications, and official benchmark evaluation.

---


### 212. [DraftExpert: Expansion-Aware Self-Speculative Decoding for End-Device MoE Inference](https://arxiv.org/abs/2607.24434)

**<font color=#1a73e8>作者：</font>** Dengke Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Mixture-of-Experts (MoE) language models are attractive for end-device deployment because only a small subset of experts is active per token, but their routed expert weights often exceed accelerator memory. We target latency-critical single-user settings where routed experts are staged on demand from CPU memory to a GPU or from Flash to a mobile NPU. In this setting, self-speculative decoding faces a new bottleneck: increasing the draft expert set improves accuracy but triggers extra expert loading, while cheap small-footprint drafts have low acceptance; moreover, verifying a multi-token block activates the union of target experts and is no longer close to one target step. We propose DraftExpert, an expansion-aware self-speculative decoding framework for expert-offloaded MoE inference. DraftExpert trains one lightweight accelerator-resident draft expert per layer by self-distilling residual, logit/token, and router-agreement signals from the frozen target MoE. At inference time, it uses a fixed-footprint shared+top-1+draft-expert drafter together with confidence--expansion truncation and target-expert prefetching, while final tokens are still exactly verified by the target model. On DeepSeek-V2-Lite and Moonlight-16B-A3B across CPU-GPU and Flash-NPU offload, DraftExpert improves decode throughput by 1.45x on average, raises draft acceptance to 84~87%, and achieves 86~88% prefetch hit rates.

---


### 213. [LEX-EC: A Lexical Evidence-Channel Audit Framework for Zero-Shot LLM Personality Classification in Black-Box Settings](https://arxiv.org/abs/2607.24435)

**<font color=#1a73e8>作者：</font>** Brittany Harbison, Ashok K. Goel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models may easily assign personality labels from text, but model interpretability remains an open problem. To address this gap, we introduce LEX-EC, a reusable black-box audit framework combining prevalence and agreement diagnostics with controlled lexical ablation to distinguish marginal-distribution effects from trait-associated signal recoverable under restricted evidence. Using this framework, we illustrate how various text genres may exhibit sharply different profiles: free-form essay text contains the broadest, but still weak, signal; in graduate student introductions, an observable Extraversion association weakened after masking; and single Facebook statuses yield little stable evidence even in a trait-balanced sample, indicating a possible lower bound of content or length. Masking topical and demographic content weakened some associations while leaving others detectable from function words, affective terms, and cognitive-style vocabulary. Linguistic prompting shifted model self-explanations but did not eliminate topical content. LEX-EC jointly evaluates classification prevalence, item-level association, chance-corrected agreement, persistence under lexical restriction, and prompt sensitivity in model-generated explanations. Across datasets, models, and prompts, LEX-EC characterizes how trait associations may vary with available lexical evidence, introducing a novel application of lexical methods to black-box interpretability in personality labeling.

---


### 214. [Bigger or Cheaper? Scale and Quantization Effects on Uncertainty Signals in Vision-Language Models Under Image Degradation](https://arxiv.org/abs/2607.24440)

**<font color=#1a73e8>作者：</font>** M M Asif Ferdous  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) deployed on consumer hardware must decide when to answer and when to defer, and that decision depends on having a confidence signal that tracks correctness. A practitioner with a fixed memory budget faces a choice between a small model at full precision, the same small model quantized, and a larger model quantized into the same footprint -- three configurations that push the confidence signal in opposing directions. We measure, on identical inputs, how model scale and 4-bit quantization affect two confidence signals in the Qwen2-VL family: the confidence a model states in natural language, and its own mean token probability over the answer it generates. Across 5,700 predictions spanning six realistic photographic degradations at three severities, we find that scale sharply improves the model's internal uncertainty signal (mean error-detection AUROC 0.80 to 0.98 from 2B to 7B) while its verbalized confidence stays weak and often at chance (mean 0.61 to 0.69): the gap between what the model knows and what it says widens rather than closes with size. We find that 4-bit quantization is nearly free for accuracy (-1.6 points) but expensive for the confidence signal (internal AUROC 0.95 to 0.80, and the verbalized-confidence parse rate collapses from 99% to 64%). For a fixed memory budget the recommendation is therefore to prefer a larger quantized model over a smaller full-precision one: 7B-4bit gives both the best accuracy and the best uncertainty signal (internal AUROC 0.98) of the three configurations that fit. We frame the results as selective-prediction operating points so they translate directly into a deployment recommendation, and we argue that error-detection AUROC, not calibration error, is the metric that exposes the difference between the two signals.

---


### 215. [RP-OPSD: Resolution-Privileged On-Policy Self-Distillation for Multimodal Large Language Models](https://arxiv.org/abs/2607.24447)

**<font color=#1a73e8>作者：</font>** Qihui Zhu, Yuchen Wang, Zijian Wen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-Policy Self-Distillation (OPSD) uses privileged information available only to the teacher to provide dense token-level supervision on trajectories generated by the student. However, existing methods often rely on verified solution traces, explanations generated by external models, or manually localized visual evidence, which limits their scalable application to multimodal large language models. To address this issue, we exploit the information gap between high- and low-resolution views of the same image and propose RP-OPSD (Resolution-Privileged On-Policy Self-Distillation for Multimodal Large Language Models). During training, the student policy generates on-policy trajectories from images at one-quarter of the original resolution, while the teacher policy provides supervision using the original-resolution images. By minimizing the divergence between their output distributions along the student trajectories, the student learns the predictive behavior of the teacher under high-resolution inputs, thereby strengthening its low-resolution capability and transferring the learned improvement to original-resolution inference. RP-OPSD requires neither additional human annotations nor external models to generate solution traces but only image--question pairs. Experiments on Qwen3.5-9B show that RP-OPSD achieves a 5.45\% relative improvement in average performance at the original resolution and a $1.78\times$ training speedup over OPSD. These results demonstrate that resolution differences can serve as a simple and scalable source of privileged information, providing an effective and efficient approach to on-policy self-distillation for multimodal large language models.

---


### 216. [From Execution to Capability: Scientific Experience Consolidation via Procedural Knowledge Synthesis](https://arxiv.org/abs/2607.24459)

**<font color=#1a73e8>作者：</font>** Liwei Dong, Jiahao Zhao, Nan Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly solve scientific-computing tasks, but executable feedback from one problem rarely becomes durable capability on subsequent problems. We study scientific-computing experience consolidation: converting verified runtime experience into transferable procedural knowledge and persistent model improvement. This setting presents two challenges: trajectory-derived artifacts may encode source-specific repairs rather than cross-task computational mechanisms; and a weaker target model may be unable to operationalize an otherwise valid abstract procedure - an abstraction-execution gap. We introduce SciConsolidate, which contrasts verified successes and failures to induce cross-task procedures, selects them through a development-validation gate, and uses failure-informed, answer-free query synthesis to expand the consolidation data without requiring pre-existing reference answers. Because the target model may not directly execute these abstractions, a stronger model concretizes them into executable code supervision for standard, procedure-free SFT; a matched no-procedure teacher branch isolates the value of procedural guidance. On SciCode, runtime procedure injection improves Qwen3.6-27B by +3.85/+6.26 sub-step/main-problem points, but yields almost no aggregate main-problem gain for Qwen3.5-9B, providing operational evidence of the abstraction-execution gap. After procedure-guided concretization, the 9B student improves under procedure-free deployment by +3.89/+6.25 points over the no-procedure SFT control and by +5.62/+11.25 over the original 9B model. These results establish an experience-to-capability pathway for scientific computing and provide a practical starting point for scaling self-improving scientific assistance.

---


### 217. [SINT-Flow: Schema Integration using Large Language Model Workflows](https://arxiv.org/abs/2607.24492)

**<font color=#1a73e8>作者：</font>** Keti Korini, Christian Bizer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The goal of schema integration is, given a set of input schemata or tables, to derive a global, unified schema that is able to represent the concepts, attributes, and relationships of all input tables in a coherent fashion. This paper presents SINT-Flow, a schema integration framework composed of five LLM-based operators that can be combined into workflows to perform fully automated, end-to-end schema integration. In contrast to existing approaches, SINT-Flow can process denormalized source tables that contain attributes describing multiple entity types. During the schema integration process, these tables are decomposed into separate entity-specific relations. To evaluate SINT-Flow, we introduce SINT-Bench, a schema integration benchmark comprising 10 schema integration tasks consisting of altogether 93 relational tables, including tables that describe multiple types of entities. We evaluate SINT-Flow using GPT-5.2 as well as the open-weight model Qwen-3.6-27B as alternative backbone models. Using these models, SINT-Flow achieves F1 scores of at least 96% for entity-type detection, 85% for attribute detection, and 83% for schema mapping. Furthermore, we perform an ablation study to prove the utility of the applied self-consistency strategy as well as the inclusion of a review loop into the schema matching operator.

---


### 218. [UNIFUSION: Adapting Autoregressive Language Models into Discrete Diffusion under a Unified Reverse-Rate Objective](https://arxiv.org/abs/2607.24507)

**<font color=#1a73e8>作者：</font>** Xiaoyi Jiang, Jingyuan Li, Yixuan Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing methods mainly adapt pretrained autoregressive (AR) language models to masked diffusion, whereas we directly adapt them to uniform-noise diffusion, where every token remains editable during sampling. However, adapting AR checkpoints across corruption kernels remains challenging because existing DLMs use different objectives and prediction parameterizations. We establish connections among SEDD, MDLM/GIDD, M2S, and Neural CTMC by expressing their conditional losses as a single generalized Kullback--Leibler objective over model reverse rates. We further derive conversions from clean-token predictions to concrete-score, posterior-mean, and exit-rate/jump parameterizations, yielding a shared \(x_0\) interface that supports switching between mask and uniform kernels. Building on these connections, we propose \ours{}, a simple continual pre-training approach for directly adapting pretrained GPT2 checkpoints to uniform-noise diffusion. Through systematic evaluation of 124M- and 355M-parameter models, we show that \ours{} steadily improves the trade-off between generative perplexity (GenPPL) and unigram entropy as the sampling budget increases from 16 to 256 steps. At 256 steps, \ours{}-S and \ours{}-M achieve GenPPL/entropy pairs of \(97.783/5.2626\) and \(71.516/5.6669\), respectively; no evaluated model at the same scale simultaneously outperforms \ours{} on both metrics. At both scales, \ours{} also achieves the highest WinoGrande, SIQA, and BBH accuracy among the compared diffusion models.

---


### 219. [Making Mathematical Knowledge Explainable, Accessible and Interoperable Through Large Language Model Integration](https://arxiv.org/abs/2607.24512)

**<font color=#1a73e8>作者：</font>** Jan Range, Björn Schembera, Dominik Göddeke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical models are central to formalizing research problems, yet their documentation often falls short of FAIR principles. Knowledge bases such as the Mathematical Model Database (MathModDB) address this gap by providing curated, semantically rich representations of mathematical models. Built on Wikibase, the same open-source infrastructure underlying Wikidata, MathModDB utilizes Semantic Web technologies to support Linked Open Data, collaborative editing, and the storage of semantically enriched metadata, making it a domain-specific knowledge graph within the broader Wikidata ecosystem. However, access to MathModDB currently requires either navigating a complex web interface or proficiency in SPARQL and Wikibase APIs, posing significant barriers for potential users. In addition, the combination of such curated knowledge bases with actual research data stored, e.g., in Dataverse repository instances, remains a challenge. To overcome these limitations, we propose integrating Large Language Models (LLMs) with MathModDB via a Model Context Protocol (MCP) server that exposes a vector-indexed schema retrieval and Steiner-tree-based join planner, combining dialogue-based natural language interaction with curated, epistemically grounded knowledge. Although instantiated on MathModDB, the architecture can be applied to other Wikibase-based systems. We demonstrate that this approach enables epistemically grounded LLM usage, improves model explainability and accessibility beyond what the standard Wikibase interface offers, and simplifies interoperability with external databases and tools, such as Dataverse data repositories. We illustrate the benefits of combining the accessibility of an LLM with the epistemic safety of a curated knowledge base through the adaptability of the MCP protocol by two use cases involving mathematical models in the fields of continuum mechanics and enzyme kinetics.

---


### 220. [Systematic Analysis of Large Language Models and Transformer-Based Machine Translation for English-Tamil and Tamil-English Across Diverse Datasets](https://arxiv.org/abs/2607.24515)

**<font color=#1a73e8>作者：</font>** Sriharshaa S, Sangeetha Sivanesan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The challenge of Machine Translation for low resource languages such as Tamil is primarily caused by the restricted amount of parallel data for these languages, as well as their substantial amount of domain variation and morphological complexity. This research presents the comprehensive evaluation of the performance of several multilingual translation models on English-Tamil and Tamil-English translations across multiple datasets: NTREX, EnTamV2, WikiMatrix and PMIndia. This study evaluates supervised NMT systems, NLLB and mBART, using both the BLEU and chrF metric, and examines how these systems perform on data of different quality levels and domains. This performs an attention-based analysis to increase model interpretability by visualising the alignments of tokens in an English source text and their Tamil translations and vice-versa to provide insight into how they make translations. This study also demonstrates that using in-context prompting can provide an excellent way to perform a few-shot translation of English to Tamil and Tamil-English using a Tamil capable TamilLaMA model, and compare this to supervised approaches qualitatively. These findings show that the quality of the datasets and their alignment with the domain will greatly affect the performance of the model, that attention-based mechanisms can aid in explain ability, and that few-shot large language models can still produce structurally coherent translations of Tamil.

---


### 221. [Stress-Testing EEG Foundation Models for Clinical Decoding: Dataset Identity and Targeted Negative Controls](https://arxiv.org/abs/2607.24519)

**<font color=#1a73e8>作者：</font>** Marzieh Zare  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained EEG foundation models are increasingly proposed for clinical decoding, but their transfer across populations and robustness to negative controls remain unclear. We benchmark six models (LaBraM, EEGMamba, CBraMod, REVE, BENDR, and BIOT) on five clinical tasks across four datasets using frozen linear probes with leave-one-subject-out, subject-grouped, or explicitly identified recording-level splits. Selected REVE findings are tested against random initialisation, random features, label permutation, scrambled-label fine-tuning, and projection sensitivity. On Korean dementia (CAUEEG, three-way), frozen REVE reaches 0.568 AUROC versus 0.769 for classical features; the ordering persists on a patient-disjoint held-out split (0.565 versus 0.768). Dataset identity is readily decoded from frozen embeddings (AUROC 1.000 at PCA-50; 0.9998 after band restriction and per-epoch z-scoring), whereas the same PCA-50 pipeline decodes Korean diagnosis at 0.528. A randomly initialised encoder also outperforms pretrained REVE on this task (0.659 versus 0.570). On Alzheimer's disease, Gaussian random projection and PCA of the same pretrained embeddings perform similarly, and classical features nominally exceed REVE at the subject level. The clearest controlled positive is cross-subject ictal detection on CHB-MIT (n=23), where REVE achieves 0.793 AUROC, 9.2 percentage points above a randomly initialised encoder. These results show that EEG foundation-model conclusions depend strongly on evaluation unit, dataset shift, comparator strength, and targeted controls.

---


### 222. [FlowCTS: On-policy Continuous Trajectory Supervision of Flow Models](https://arxiv.org/abs/2607.24522)

**<font color=#1a73e8>作者：</font>** Kaiyang Ye, Yuan Ge, Junxiang Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While on-policy distillation (OPD) effectively addresses sparse rewards and exposure bias in large language model post-training, its extension to flow models remains underexplored. To this end, we propose Flow Continuous Trajectory Supervision (FlowCTS), which matches subsequent student and reference trajectories initialized from the same student-visited state. Using the integral relation between trajectories and velocity fields, we derive a temporally weighted velocity-matching upper bound and discretize it into practical objectives parameterized by the number of supervision steps. Under a multi-reference setup, single-state FlowCTS-OPD outperforms vanilla KL-based OPD with faster convergence. FlowCTS-OPD improves GenEval from 0.90 to 0.93, OCR from 0.90 to 0.92, and PickScore from 22.75 to 23.06, while outperforming a mixed-reward RL baseline across all target metrics. Further analysis reveals a clear temporal supervision mismatch in vanilla KL-based OPD arising from its auxiliary SDE transition kernels. Beyond on-policy setting,FlowCTS also consistently outperforms vanilla SFT , particularly on OCR, while increasing supervision steps exhibit a trade-off between richer trajectory information and greater optimization difficulty.

---


### 223. [Task-Conditional Faithfulness Auditing of Multimodal LLMs for Grid Diagnosis](https://arxiv.org/abs/2607.24539)

**<font color=#1a73e8>作者：</font>** Tianqiao Zhao, Meng Yue, Jianhui Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (LLMs) can combine topology, measurements, and incident text for grid diagnosis, yet answer accuracy does not establish that task-appropriate evidence was used. This letter proposes a general framework in order to conduct task-conditional faithfulness audit. It compares self-reported reliance, intervention-derived behavioral reliance, and preregistered engineering importance. The framework first registers task-specific evidence requirements and compares them with self-reported reliance and behavioral changes under controlled modality ablations. To resolve detected discrepancies, we design an evidence-gated correction and re-audit mechanism that regenerates failed responses under evidence constraints and independently re-ablates them to verify improved grounding without performance loss. Case studies evaluate three differently scaled LLMs on IEEE 39- and 118-bus scenarios. These results validate the framework ability to detect, diagnose, and correct task-conditional faithfulness failures.

---


### 224. [LLM-Assisted Ontology Engineering and Construction of a French Legal Knowledge Graph](https://arxiv.org/abs/2607.24551)

**<font color=#1a73e8>作者：</font>** G{é}nesis Montenegro, Mokhtar Boumedyen Billami, Catherine Faron 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Maintenance regulations are complex legal texts that are difficult to exploit when addressing a specific case and challenging to integrate into operational systems. This paper presents a two-stage LLM-assisted workflow for French maintenance regulations: ontology engineering from a SEMLEG-based core ontology, followed by construction of an ontology-grounded French legal knowledge graph. The first stage consists in the open extraction of typed entities and triples from a stratified corpus sample, the normalization of labels through embedding-based fusion, and the induction of candidate object properties with their signature (domain and range). The second stage uses the resulting ontology to guide the closed extraction of triples and RDF graph construction over the full corpus. Experiments with GPT-4.1 and mistral-large-2512 show robust structured outputs, near-complete class alignment, and a substantial reduction of duplicated entities and predicates after fusion. Fewer than 20% of triples introduce unseen properties, while lower exact signature compliance reveals new domain-range combinations for existing predicates. These results point to predicate normalization and the validation of newly observed relation signatures as key refinement steps for industrial maintenance settings.

---


### 225. [EchoBridge: Long-Tail-Aware ECG-Echocardiography Text Alignment for Echocardiography-Derived Cardiac Findings](https://arxiv.org/abs/2607.24553)

**<font color=#1a73e8>作者：</font>** Xiaocheng Fang, Jieyi Cai, Guangkun Nie 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standardized echocardiography conclusions provide meaningful supervision for learning ECG representations of echocardiography-derived cardiac findings. Global ECG--text alignment may entangle modality-specific factors, while long-tailed finding distributions provide sparse positive supervision for low-prevalence conditions. We propose EchoBridge with Complementary Shared--Private Projection (CSPP) and Adaptive Prototype Boundary Calibration (APBC). CSPP maps each modality into shared and auxiliary private projections, reduces directional redundancy via within-modality orthogonality, and bidirectionally aligns normalized shared projections. APBC organizes the shared hypersphere with class-specific prototypes, training-frequency-adaptive angular margins, and spherical Riesz repulsion. We evaluate EchoBridge on EchoNext-Mini and independent PKUPH and SHTMU cohorts under four protocols: prompt-based inference without downstream classifier training, in-domain frozen linear probing, target-domain cross-center frozen linear probing, and source-only cross-center transfer, supplemented by finding-specific analyses. EchoBridge improves classifier-free AUROC, AUPRC, and F1 over the strongest baselines by 7.88, 5.61, and 4.54 points, respectively, and achieves the highest point estimates across all in-domain and target-domain probing budgets and both source-only transfer cohorts. Finding-specific analyses show gains for most conditions, including several low-prevalence valvular findings.

---


### 226. [Hierarchical Group-Conditional Conformal Risk Control for Selective Prediction in Language Models](https://arxiv.org/abs/2607.24562)

**<font color=#1a73e8>作者：</font>** Murilo Salem, Luísa Böhm, Daniel Pontes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models serve heterogeneous populations structured by domain, topic difficulty, and linguistic style. Conformal risk control (CRC) gives rigorous marginal risk guarantees for selective prediction with abstention, but marginal guarantees do not imply per-group ones: a model can meet the population budget while systematically over-exposing subgroups to errors. Under mild shift in group composition, standard CRC violates the budget in up to 47% of trials.
We propose HG-CRC (Hierarchical Group-Conditional CRC), a post-hoc calibration framework enforcing simultaneous risk guarantees across all nodes of a user-defined group hierarchy. It applies a Bonferroni correction over nodes and a leaf-first policy that uses the most specific applicable threshold, falling back to coarser nodes when a finer one is uncertified or rejects the example. It needs only a held-out calibration set, with no retraining.
We evaluate on three models (Qwen3-4B, Llama-3.1-8B-Instruct, Gemma-3-4B) and two benchmarks (ARC Challenge, MMLU-Pro) across eight configurations probing IID generalization, heterogeneity, mixture/domain/prompt/difficulty shift, label noise, and quantization. Main result: HG-CRC reaches an empirical 0% violation rate and WGER=0 on ARC Challenge for high-accuracy models (Qwen3-4B, Llama-3.1-8B). At 500 bootstrap trials these zeros are empirical upper bounds (true rate up to 0.6%), not certified. Results are benchmark-specific: on MMLU-Pro these models abstain entirely or (Llama) retain WGER=0.014. Gemma-3-4B, poorly calibrated here, degrades gracefully by abstaining. Participation cost vs. global CRC is 22 to 37 points. Ablations show hierarchical depth clears the budget: removing difficulty level returns violations to about 11%. Bonferroni is needed for the theoretical guarantee, though its empirical effect matters only with many nodes.

---


### 227. [The Visual Bottleneck: Sparse-Frame Adaptation of MLLMs for Joint Spatial-Temporal Video Grounding](https://arxiv.org/abs/2607.24570)

**<font color=#1a73e8>作者：</font>** Jiameng Zhang, Srikanth Madikeri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale video platforms process millions of uploads hourly, requiring moderation systems that can localize when and where policy violations occur within each video. Processing every frame is infeasible at scale, so systems are constrained to sparse inputs of 8 to 16 frames per video. Yet state-of-the-art multimodal large language models (MLLMs) are pretrained on dense sequences of hundreds of frames, creating a fundamental mismatch between training and deployment conditions. This mismatch causes severe performance collapse: the Qwen3-VL 8B model drops from 56.0% to 22.3% temporal mIoU when frames are reduced to 16, a 60.2% relative degradation.
We present a systematic empirical study of training strategies to close this gap for spatial-temporal video grounding. Our results suggest that visual feature extraction is the dominant bottleneck under sparse-frame inputs. Adapting only the final three ViT layers, 4% of total parameters, achieves 68.8% temporal mIoU and surpasses a zero-shot 8B model using dense inputs by 12.8 points. Language model fine-tuning, by contrast, offers negligible or negative returns. A boundary-aware sampling strategy, Hybrid16, further improves temporal mIoU by 26 points over uniform sampling when temporal boundaries are available. We conclude that for sparse-frame video grounding, training strategy dominates model scale: a fine-tuned 2B model consistently outperforms a zero-shot 8B model, with or without dense frame access.

---


### 228. [LLM-SoccerArena: Benchmarking LLMs on Real-World Predictions in Sports](https://arxiv.org/abs/2607.24573)

**<font color=#1a73e8>作者：</font>** Jonas Schröder, Jonas Schweisthal, Oliver Müller 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly support decisions about uncertain future events, yet evaluating their ability to forecast real-world outcomes remains difficult. In particular, existing benchmarks are typically static and retrospective, and therefore cannot test how information is synthesized by LLMs to predict future events under uncertainty. We introduce LLM-SoccerArena (this https URL), a prospective live benchmark that evaluates how well LLMs forecast real-world sports events before the outcomes are known. LLM-SoccerArena provides (1) a prospective live benchmark protocol, (2) a public open-source platform, and (3) a factorial benchmark design together with tournament-related questions (e.g., which team will win). LLM-SoccerArena automatically records timestamped, schema-validated forecasts of unresolved events, together with prompts, model versions, tool traces, and costs. The factorial design varies along four dimensions: (1) model version (e.g., GPT-5.5, Claude Opus 4.8); (2) information access; (3) prompting strategy, and (4) forecast horizon. We demonstrate LLM-SoccerArena through a large-scale evaluation of the 2026 FIFA World Cup, in which seven LLMs generated forecasts for all 104 matches and 15 tournament-related questions. We provide a detailed analysis of model performance across information access, prompting strategy, and forecast horizon. As a result, LLM-SoccerArena provides new evidence about the forecasting performance of state-of-the-art LLMs. For example, LLMs with web access outperform those without, but only by a small margin (i.e., a 0.023 improvement in Brier score). Overall, LLM-SoccerArena provides a flexible, open-source platform for prospective benchmarking of unresolved events. LLM-SoccerArena will be continuously updated, and can be directly applied to future national and international tournaments and league competitions.

---


### 229. [From Data to Device: ELMOD An Efficient German-First 2.7B Language Model for Mobile Inference](https://arxiv.org/abs/2607.24585)

**<font color=#1a73e8>作者：</font>** Darina Gold, Alexander Schwirjow, Viktor Haag 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present ELMOD - Efficient Language Model for On-Device Deployment - a compact (2.7B) German language model designed for efficient inference on resource-constrained hardware. ELMOD was trained on a limited computational budget (55k H100 GPU hours) using exclusively publicly available data. We developed a suite of German-specific data pre-processing, which differ from English-oriented counterparts in their handling of morphological variation, compounding, and orthographic conventions. Furthermore, we introduced a quality filtering and rephrasing step, which increased the instructional quality of the data, improved performance during the annealing phase, and reduced overall compute requirements. Thanks to our architectural model and data choices, including prefiltering, our educational-quality filtering and rephrasal to raise the educational-quality, ELMOD is the strongest performer in its size class (<3B), matching the performance of 7B-parameter models in German.

---


### 230. [D-Score: A Spectral Hidden-State Signal for Hallucination Detection in Large Language Models](https://arxiv.org/abs/2607.24586)

**<font color=#1a73e8>作者：</font>** Bianca Raimondi, Davide Evangelista, Maurizio Gabbrielli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models can produce fluent text that is false, unsupported by the available evidence, or inconsistent with information that appears to be internally represented by the model. We study hallucination detection from the geometry of hidden activations and introduce the D-Score, a simple spectral statistic computed from a single forward pass. For a fixed model, layer, and tolerance parameter, the D-Score counts how many singular directions of the hidden activation matrix have singular values that remain close to the leading one. We use this quantity as a hallucination score, classifying an input text as hallucinated when its D-Score is larger than a pre-defined quantity. The motivation is that, when a model processes a text that conflicts with information available in its own internal state, the hidden representation may encode both the asserted content and some form of counter-evidence, uncertainty, correction, or lack of support; this can make the hidden trajectory spread across additional singular directions. We formalize this intuition through a lightweight spectral argument and evaluate the resulting detector on FAVA-Annotation and RAGTruth. The experiments indicate that the D-Score is a strong hidden-state signal for hallucination detection, while requiring no external verifier, no retrieval step, and no multiple generations.

---


### 231. [SIREN: Towards End-to-End Extreme-Weather Early Warning with Experience-Grounded LLM Agents](https://arxiv.org/abs/2607.24588)

**<font color=#1a73e8>作者：</font>** Hang Ni, Weijia Zhang, Fan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early warning of extreme weather is essential for mitigating the societal, economic, and environmental risks posed by hazardous weather events. However, expert-centered warning workflows are costly, labor-intensive, and difficult to scale throughout the warning-to-action process. Although recent advances in Large Language Model (LLM) agents have enabled the automation of weather-related tasks, existing studies remain centered on isolated scientific tasks and overlook the chain of interdependent processes required for operational extreme-weather early warning. To bridge this gap, this study investigates automated end-to-end extreme-weather early warning through LLM agents. We first develop SIREN-Bench, a comprehensive benchmark comprising 600 question-answer instances across 19 tasks, and covering four individual warning procedures and an end-to-end warning chain. Evaluation on SIREN-Bench reveals substantial capability gaps in existing weather agent frameworks. This motivates us to develop SIREN, an experience-grounded agent framework inspired by experts' use of historical cases, which combines an agentic execution environment integrating heterogeneous weather evidence and tools with a family of agent harnesses that exploit historical cases through retrieval, skill distillation, and predictive modeling. Extensive experiments demonstrate that SIREN outperforms weather-agent baselines on both individual warning procedures and end-to-end warning chains.

---


### 232. [Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair](https://arxiv.org/abs/2607.24604)

**<font color=#1a73e8>作者：</font>** Xueping Gao, Jianwei Yang, Qiang Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generate--test--revise loops are common in coding agents, but repetition alone provides no reliability guarantee. We study the gap between finding a correct patch and retaining, verifying, and submitting it. A sealed five-seed study over 30 HumanEval repairs produces 900 three-revision trajectories. Under forced revision, current correctness with current traces falls from 0.820 after one revision to 0.673 after two, although ever-correct rises to 0.847. Two common-state studies use 2,430 branches from identical frozen programs to remove post-treatment risk-set bias. In a prespecified 14B replication, stale traces harm 34/135 correct starts versus 4/135 with current traces, a 22.2-point increase (task-cluster 95\% CI $[8.9,37.0]$, exact Holm $p=0.0337$). A prospective 540-rollout policy eliminates observed correct-start harm but reduces wrong-start repair and fails its joint criterion. Repository experiments over 24 bugs and four coder stacks expose floor effects and component heterogeneity without Holm-significant effects. We therefore separate admission, preservation, grounded certification, competence, and liveness. We derive an evidence-bound typed loop contract and instantiate its mechanically enforceable subset in a reference implementation that binds verifier evidence to exact code states, preserves verified checkpoints, and emits auditable admission receipts. The implementation is an executable specification and conformance artifact, not evidence of improved repair competence or calibrated verifier dependence.

---


### 233. [Test-Time Adaptation via Dual Distillation for Videos Under Severe Distribution Shifts](https://arxiv.org/abs/2607.24611)

**<font color=#1a73e8>作者：</font>** André Sacilotti, Samuel Felipe dos Santos, Jurandy Almeida  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models have achieved state-of-the-art performance in several computer vision tasks. However, they experience severe performance degradation when applied to real-world scenarios due to unanticipated distribution shifts. Test-Time Adaptation (TTA) attempts to solve this problem by using unlabeled data from the target domain to dynamically adapt to the test distribution at inference time, without access to the source data. However, TTA remains a challenging problem when adapting to continuous, temporally correlated data, such as videos, and in scenarios where the target domain contains severe domain shifts. For this reason, few works in the literature explore TTA for videos under such extreme conditions. To overcome these limitations, we propose Test-time Adaptation via Dual Distillation (TADD), an online adaptation framework that relies on a lightweight projection adapter to bridge the domain gap. The adapter module is pre-trained on the source domain and then adapted to the target using our proposed complementary losses: (i) zero-shot distillation, which encourages alignment with the domain-agnostic features from a pre-trained vision-language model (VLM); and (ii) target distillation, which retains the source domain discriminative knowledge encoded in the pre-trained adapter. Built upon a frozen CLIP backbone, our method introduces this lightweight projection adapter as the sole updatable component during inference. We conducted extensive evaluations on three well-known video action recognition benchmarks: UCF-HMDB, Daily-DA, and Sports-DA. Our experiments in the closed-set scenario demonstrate that our method consistently outperforms state-of-the-art TTA baselines. Notably, our TTA approach improves upon previous methods by up to +3.81% on UCF-HMDB, +2.63% on Daily-DA, and +3.03% on Sports-DA.

---


### 234. [Reason-Mediated Behavioral Models for Auditing LLM Social Simulators](https://arxiv.org/abs/2607.24649)

**<font color=#1a73e8>作者：</font>** Atharva Pandey, Gautam Jajoo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as social simulators, including as synthetic survey respondents. Most evaluations ask whether simulated outcomes resemble human outcomes. We argue that this is necessary but too weak: a simulator can match the final answer while using the wrong rationale-derived reason pattern. We study this problem through a 94-person sunscreen concept test in which each respondent evaluated three product concepts and wrote open-ended rationales. We map those rationales into signed reason states $Z$, where positive signs support adoption and negative signs block it. This gives a practical audit: holding respondent descriptors $D$, category context $K$, and concept treatment $X$ fixed, do human rationale-derived reasons help predict behavior $Y$, and can an LLM simulate the same reason state without seeing the human rationale or outcome? Human rationale-derived reasons substantially improve held-out prediction of purchase intent. LLM-simulated reasons are more brittle: they often sound plausible, but frequently echo the concept board rather than recover the respondent's acceptance or rejection path. The paper contributes an evaluation framework for social simulators. Reason states do not identify natural causal effects by themselves, but they provide an interpretable test of whether a simulator's stated reasons align with human evidence.

---


### 235. [Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653)

**<font color=#1a73e8>作者：</font>** Kimi Team, Tongtong Bai, Yifan Bai 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Kimi K3, a 2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window. Kimi K3 is built on Kimi Delta Attention and Attention Residuals, which improve information flow across sequence length and model depth. Together with Stable LatentMoE, which effectively activates 16 of 896 routed experts per token, and refined training and data recipes, these advances yield an approximately 2.5x improvement in overall scaling efficiency over Kimi K2. Post-training highlights reinforcement learning across general, agentic, and coding domains and multiple reasoning-effort levels, enabling compositional generalization and robust long-horizon execution. At 2.8T scale, Kimi K3 is supported by infrastructure advances in multiple areas: algorithm-system co-design for KDA, perfectly balanced expert-parallel training with efficient memory management, million-token agentic RL with persistent rollout and sandbox states, and deployment innovations. Extensive evaluations show that Kimi K3 achieves frontier-level performance across long-horizon coding, agentic, knowledge, reasoning, and vision tasks. While its overall performance still trails the most powerful proprietary models, namely Claude Fable 5 and GPT-5.6 Sol, Kimi K3 consistently outperforms other open and proprietary models evaluated in our suite. We release the full Kimi K3 model weights to facilitate future research and accelerate the broader deployment and adoption of frontier intelligence.

---


### 236. [MMOE: Modernizing Diffusion Transformers with Efficient Expert Design](https://arxiv.org/abs/2607.24665)

**<font color=#1a73e8>作者：</font>** Yanhao Jia, Jiepeng Wang, Haibin Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern large language models scale successfully by pairing capacity growth with efficiency, keeping per-token and deployment costs under control as capacity grows. AIGC Foundation Models (AFMs), especially diffusion-transformer backbones, have begun to adopt sparse experts, but recent efforts mostly enlarge total parameter counts and sparsity ratios without importing the efficiency mechanisms that made LLM scaling practical, so generation quality is seldom balanced against training and deployment cost. This raises a natural question: can the architectural principles behind efficient LLM scaling be adapted to AFMs in a more balanced way? We introduce ModernMOE (MMOE), a modernization of SiT-style diffusion transformers that systematically adapts routed experts, shared and lightweight experts, gate-residual routing, and attention-residual information reuse to AIGC generation. Rather than treating MoE as a single plug-in replacement, MMOE studies how different modern expert components affect convergence, efficiency, and generation quality when composed inside a diffusion transformer. Every experiment in this paper is trained on a single eight-GPU H100 node with batch size 256 for 400k steps, an accessible single-machine budget. Under matched training and sampling protocols and at this budget, MMOE reaches lower FID at every recorded checkpoint, that is, it converges faster per training step, than dense and intermediate sparse-expert baselines, and among the sparse variants it attains the best quality-cost balance. Routing analysis further shows stable expert specialization across depth, substantial use of lightweight routes, and modest step-to-step routing changes during denoising. These results suggest that AFMs can follow the balanced scaling path of LLMs by importing proven efficiency designs, rather than by simply increasing total parameters and sparsity ratios.

---


### 237. [ERUnderstand: Evaluating Vision-Language Models on Structured ER Diagrams](https://arxiv.org/abs/2607.24707)

**<font color=#1a73e8>作者：</font>** Ali Ansari, Yasmin Mohammadi, Farnoush Nili 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Entity-Relationship Diagrams (ERDs) are central to conceptual database design, yet they are typically available only as rendered images rather than machine-readable schemas, limiting AI-assisted database engineering. We introduce ERUnderstand, the first large-scale benchmark for structured understanding of ER diagrams, comprising 2,960 diagrams collected from curated educational sources, real-world schemas, and synthetically generated examples spanning diverse domains, notations, complexity levels, and Extended Entity-Relationship (EER) constructs. Each diagram is paired with a standardized machine-readable representation for fine-grained evaluation of schema elements. Evaluating state-of-the-art Vision-Language Models (VLMs), we find that while common ERD elements are recovered reliably (F1 > 0.74), performance drops sharply on weak entities (as low as 0.28 F1), multivalued attributes (0.14 F1), and N-ary relationships (0.07 F1). Reasoning-augmented models improve overall performance by 15-25% but remain sensitive to linguistic priors and increasing diagram complexity. ERUnderstand provides a standardized benchmark for evaluating multimodal understanding of conceptual database schemas. The benchmark, dataset, evaluation toolkit, and generation code are publicly available at this https URL.

---


### 238. [DataOrchestra: Learning to Orchestrate Per-Example Curation of Pretraining Data](https://arxiv.org/abs/2607.24717)

**<font color=#1a73e8>作者：</font>** Zhen Huang, Yikun Wang, Shijie Xia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretraining data processing is critical to the downstream performance of Large Language Models (LLMs). However, many existing approaches define a fixed processing strategy at the corpus or domain level and apply it uniformly to many examples, without adapting to the needs of each example. We propose DataOrchestra, a framework that unifies different processing operations and orchestrates an example-specific pipeline for each example. Given a chunk of pretraining data, an orchestrator decides whether to drop, untouch, or clean it. For a chunk to be cleaned, it selects one or more downstream operations, ranging from programmatic editing to different forms of LLM-based rewriting. For each rewriting step, it further generates a concrete instruction, which is executed by the corresponding downstream tool model. We pretrain models from 0.5B to 7B from scratch on web data processed by DataOrchestra and observe stable average gains over individual data-processing methods across 11 benchmarks. DataOrchestra is also effective for math continued pretraining and outperforms stronger processing baselines, while reducing processing compute by skipping unnecessary downstream operations.

---


### 239. [The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation](https://arxiv.org/abs/2607.24720)

**<font color=#1a73e8>作者：</font>** Tianyi Men, Zhuoran Jin, Kang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn long-horizon planning is critical for foundation model agents, yet how to fundamentally improve it remains unclear. Existing models are trained on uncontrollable and opaque Internet data, making it difficult to identify how planning ability is acquired, shaped, and integrated. To address this challenge, we introduce a unified and controlled multi-turn environment that enables precise control. It allows systematically study long-horizon planning across three stages. (1) Planning ability acquisition during pre-training. We study data format, distribution, and quality. Explicit world model construction through CoT state transition modeling yields stronger long-horizon generalization. Atomic skills alone are insufficient for compositional generalization, whereas a litte long-horizon data works. Moreover, suboptimal trajectories severely impair performance because errors amplify over long horizons. (2) Planning ability shaping via GRPO and OPD post-training. Through mutual information, we distinguish general planning patterns from task-specific planning knowledge. For planning patterns, we identify three application regions of post-training: unnecessary, effective, and unsupported. OPD has a broader effective region than GRPO under low-quality and long-horizon settings, as it provides more consistent update directions. For planning knowledge, distilling unseen procedures from a teacher with different knowledge may impair student's prior world modeling without fully establishing new knowledge. (3) Planning ability integration through MOPD post-training. We show that multi-teacher on-policy distillation (MOPD) integrates capabilities by converging to shared planning-pattern across environments. Compatible patterns enable cross-environment generalization, partially shared patterns support continual learning, while completely conflicting patterns cause severe interference.

---


### 240. [ClinFusion: A Vision-Centric Multimodal LLM System for Holistic Medical Understanding](https://arxiv.org/abs/2607.24743)

**<font color=#1a73e8>作者：</font>** Hangjie Yuan, Yichen Qian, Zhiwei Tang 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) hold immense potential to revolutionize clinical practice, yet deploying them in the medical domain is fundamentally a vision-centric challenge: models must absorb knowledge from heterogeneous 2D and 3D medical images, and evaluation protocols must align with radiologists' clinical practice and provide an accurate, fine-grained and factualness-driven assessment. In this paper, we introduce ClinFusion, a vision-centric MLLM designed for holistic medical understanding that systematically addresses these limitations. We propose a compositional and cascaded vision encoder architecture featuring a Cascade Spatial-Aware Locality Fusion operator that unifies diverse 2D and native 3D medical image understanding within a fused encoder. We further introduce a vision-grounded evaluation framework, including MedIF-Bench for instruction-following assessment and a region-of-interest-grounded method for clinically aligned and factualness-driven report generation evaluation. We show that ClinFusion sets a new state-of-the-art across a comprehensive suite of 2D and 3D multimodal medical benchmarks---spanning visual question answering, report generation, and instruction following---as well as textual medical tasks, outperforming leading open-source medical MLLMs (\textit{e.g.}, Hulu-Med, Lingshu) on 20 out of 24 benchmarks and demonstrating multimodal capabilities better than powerful proprietary models such as GPT-5.2 and Gemini-3-Flash on 13 out of 16 benchmarks, and can be further augmented with agentic tool use for retrieval-augmented and tool-assisted clinical workflows. A blinded evaluation by board-certified radiologists confirms that ClinFusion produces the highest-ranked reports, and validates our RoI-grounded metric as achieving the strongest correlation with expert judgment among all automatic evaluation metrics examined.

---


> [!TIP]
> 当前位于：**201-240**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-240**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
