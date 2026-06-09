# 🧠 大模型相关研究 | 2026年06月10日

> 本类共 **331** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**301-331**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-331**

---

### 301. [From Rigid to Dynamic: Entropy-Guided Adaptive Inference for Long-Context LLMs](https://arxiv.org/abs/2606.09508)

**<font color=#1a73e8>作者：</font>** Zhanchao Xu, Haoyang Li, Qingfa Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing sparse attention and KV cache compression methods for long-context LLM inference typically apply fixed sparsity patterns or uniform budgets across all attention heads, overlooking the substantial variation in attention behavior among heads and contexts. We observe two distinct entropy patterns among attention heads: Rigid Heads, whose entropy stays near zero across input segments, and Dynamic Heads, whose entropy fluctuates significantly. Crucially, the distribution of these types is context-dependent and cannot be predetermined offline. We therefore propose EntropyInfer, a training-free framework that uses attention entropy to adaptively allocate compute at the granularity of individual heads and segments during prefilling. For decoding, we introduce a latent KV cache compression scheme that leverages generated output tokens, rather than prefill tokens alone, to identify and retain the most critical cache entries. Extensive experiments on Llama, Qwen and openPangu model series show that EntropyInfer consistently outperforms baselines including SnapKV, AdaKV, and CritiPrefill, achieving up to 2.39$\times$ end-to-end speedup beyond 100k tokens with minimal quality degradation compared to full attention. The code is released in this https URL.

---


### 302. [Securing Self-supervised Data Curation for Foundation Models Robustness](https://arxiv.org/abs/2606.09511)

**<font color=#1a73e8>作者：</font>** Sandeep Gupta, Roberto Passerone  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised data curation provides a pathway to scaling and improving the generalization capabilities of machine learning models. By leveraging self-supervised learning (SSL) for data curation, the demand for massive training datasets required by foundation models can be effectively met. SSL greatly alleviates the costs associated with annotation and manual dataset curation while minimizing the need for human oversight. However, the integrity of SSL-curated datasets must be rigorously checked, as reliance on anonymous and unvetted external sources can substantially increase the risk of data poisoning. In this paper, we propose a Poisoned Data Detector (PDD), an active defense mechanism designed to ensure the integrity of SSL-curated datasets prior to foundation model training. PDDs are designed using a combination of the pretrained ImageBind model and traditional classifiers, including Random Forest (RF), k-Nearest Neighbors (KNN), Naive Bayes (NB), and Support Vector Machines (SVM). We rigorously evaluated PDDs using 176,200 images from three diverse datasets and three different adversarial attacks encompassing both in-distribution and out-of-distribution scenarios. Notably, SVM-PDD achieves superior performance for both in-distribution (Set3-Set5) and out-of-distribution (TrueFace and 140K RealFace) datasets. Our design demonstrates strong scalability and enables the rapid integration of new adversarial attack detectors through an ensemble approach.

---


### 303. [BUDDY: BUdget-Driven DYnamic Depth Routing for Adaptive Large Language Model Inference](https://arxiv.org/abs/2606.09514)

**<font color=#1a73e8>作者：</font>** Yuhua Zhou, Shaoqi Yu, Shichao Weng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) incur high inference cost due to their depth and parameter scale. Depth pruning can reduce latency by skipping redundant Transformer blocks, but existing methods (i) provide limited control under user-specific compute budgets and (ii) typically fix the routing path, failing to adapt as the context grows during decoding. We propose Buddy, a budget-driven dynamic depth routing framework. Buddy uses a lightweight Decision Module to score intermediate layers conditioned on the input and deterministically executes the top-k layers to satisfy a given budget. To support decode-time adaptation, Buddy reuses the first-layer KV cache as a low-overhead global context source and pools it together with the newest token representation before each routing decision. When no explicit budget is provided, an optional Budget Predictor estimates an input-dependent compute level to balance quality and efficiency. Experiments on Llama-family and Qwen models show that Buddy is competitive with strong static pruning baselines and often improves the accuracy-compute trade-off, while uniquely supporting strict budget control, decode-time rerouting, and multiple budgets within a single trained model.

---


### 304. [Emergence of Context Characteristics Sensitivity in Large Language Models](https://arxiv.org/abs/2606.09525)

**<font color=#1a73e8>作者：</font>** Nadya Yuki Wangsajaya, Haeun Yu, Isabelle Augenstein  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> During instruction fine-tuning (IFT), large language models (LLMs) learn to follow instructions by using the provided context to answer a query. While prior work has studied how context characteristics correlate with context usage by the LLM, this analysis has been limited to inference time, leaving open how these relationships are acquired in the first place. Here, we measure how models' sensitivity to such characteristics shifts across successive IFT stages: supervised fine-tuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable rewards (RLVR). Experiments across four models and three datasets show that SFT makes models more likely to use contexts that are easy to understand, such as containing high length, context-query similarity, and fluency. Post-SFT dynamics may either reinforce or resolve these preferences depending on the training dataset. Our findings reveal that context usage is actively reshaped at each IFT stage, and designing a balanced IFT dataset is important in ensuring robust context utilization of instruction-tuned models.

---


### 305. [Streaming Interventions: Can Video Large Language Models Correct Mistakes as They Occur?](https://arxiv.org/abs/2606.09547)

**<font color=#1a73e8>作者：</font>** Apratim Bhattacharyya, Shweta Mahajan, Sanjay Haresh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning everyday skills, like cooking a dish, relies increasingly on instructional media such as online videos. This opens the door to the use of video (and multimodal) large language models (LLMs) as task guidance assistants. A crucial capability for the real-world success of a prospective task guidance assistant is it's ability to intervene proactively as soon as a mistake is apparent in order to guide the user. To evaluate this crucial capability, we introduce Ego-MC-Bench (Mistake Corrections), a benchmark for evaluating reactive, step-by-step task guidance in realistic cooking scenarios. Extensive experiments show that Ego-MC-Bench is highly challenging for state-of-the-art video LLMs. We argue that a key reason is the limited availability of training data for fine-tuning models on this task. Although there exists a wide range of cooking video datasets, existing datasets lack examples of mistakes along with appropriately timed interventions. To help address this data limitation, we also introduce Ego-CoMist, a counterfactual synthetic dataset created by transforming non -interactive cooking videos into supervised training examples showing proactive interventions. We show that fine-tuning on Ego-CoMist yields performance gains especially for smaller and more efficient video LLMs that are well suited for delivering assistance on edge devices.

---


### 306. [PRISM: Recovering Instruction Sets from Language Model Activations](https://arxiv.org/abs/2606.09563)

**<font color=#1a73e8>作者：</font>** Gilad Gressel, Rahul Pankajakshan, Julia Diament 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLMs are deployed as agents, reliable monitoring requires knowing not only what they output, but which instructions are steering their behavior. This is difficult when models infer unintended subgoals, follow contextual cues, or are influenced by prompt injections and hidden objectives. While activation-to-language methods suggest that hidden states can reveal natural-language information, existing approaches are not designed to recover the full set of simultaneous instructions, constraints, prohibitions, and subgoals active in agentic settings. We formalize this problem as instruction set retrieval and introduce PRISM, an activation-conditioned interpreter that decodes hidden states from a frozen target model into a faithful bullet list of active instructions. Unlike prior activation-to-language methods, PRISM is trained to recover instruction sets directly, using judge-guided GRPO to reward covered instructions and penalize unsupported ones. Across benign, constrained, prompt-injection, and hidden-objective settings, PRISM outperforms activation-to-language baselines, especially on security-relevant objectives.

---


### 307. [Code Is More Than Text: Uncertainty Estimation for Code Generation](https://arxiv.org/abs/2606.09577)

**<font color=#1a73e8>作者：</font>** Yuling Shi, Caiqi Zhang, Yuexian Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as code generators, where silently wrong programs pose real safety and reliability risks. Reliable uncertainty estimation (UE) is essential for selective prediction, human-in-the-loop review, and downstream agentic decisions. Yet most existing code UE methods are inherited from natural language (NL) generation and ignore properties that make code distinct. We argue that code differs from NL in three ways: a single wrong token can break an entire program (token fragility); algorithmic intent and concrete implementation can disagree independently (intent-code gap); and programs can be executed (executability). We instantiate these properties as three orthogonal uncertainty axes: lexical (Top-K token entropy), algorithmic (pseudo-code consistency), and functional (behavioral consistency). Across five code LLMs, our three-axis ensemble improves average AUROC from 0.696 for the strongest NL-derived baseline to 0.776 (+8.1 points). Notably, on Qwen3-14B, our single-pass Top-K token entropy matches the strongest multi-pass baseline while being over 3x cheaper; across models, it remains a competitive low-cost signal. These results suggest that code UE deserves code-specific design rather than direct NL ports.

---


### 308. [TABVERSE: Benchmarking Cross-Format Table Understanding in LLMs and VLMs](https://arxiv.org/abs/2606.09578)

**<font color=#1a73e8>作者：</font>** Momina Ahsan, Sarfraz Ahmad, Ming Shan Hee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) and Vision-Language Models (VLMs) are increasingly evaluated on table reasoning tasks, but the role of table representation remains under-explored. In practice, the same table content may appear in different structural formats, such as HTML, Markdown, and LaTeX, or as rendered images. However, existing evaluations often let content, format, layout, and modality vary together, making it difficult to isolate representation effects. We introduce TABVERSE, a controlled multimodal table benchmark that aligns the same table content across multiple structural formats and rendered images, with question category and difficulty tags. This design enables systematic evaluation of representation effects while holding table content fixed. We evaluate LLMs and VLMs across three tasks: Question Answering (QA), Structural Understanding Capability (SUC), and Structure Reconstruction (SR). Our results show that representation choice substantially affects table understanding. Models generally perform better with structured text than with rendered images, but the size of this gap depends on the task, model, and format. HTML is often the most robust text format, while row-sensitive structural tasks and syntactically usable LaTeX reconstruction remain challenging. These findings show that table representation is a key factor in reliable table evaluation.

---


### 309. [Optical Reasoning: Rethinking Images as an Expressive Reasoning Medium Beyond Text](https://arxiv.org/abs/2606.09585)

**<font color=#1a73e8>作者：</font>** Yutong Bian, Dongjie Cheng, Heming Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) improves the performance of Large Language Models (LLMs) and has been extended to Multimodal Large Language Models (MLLMs). More recent work further moves from text-based multimodal reasoning toward interleaved-modal reasoning, where intermediate steps can incorporate both textual rationales and visual evidence. In this work, we propose a bolder and more ambitious idea: could images alone serve as the reasoning medium for both language and multimodal tasks? To explore this, we propose optical reasoning, which treats images as a standalone reasoning medium. We instantiate this concept with two variants: typographic-based optical reasoning, which optimizes visual layouts for compact rationale rendering, and graphical-based optical reasoning, which composes text and graphical elements into structured visual rationales. Across mathematical, scientific, and interleaved-modal reasoning benchmarks, optical reasoning can match or even exceed traditional text reasoning while reducing reasoning tokens by an average of 28.57% on language tasks and 16% on multimodal tasks, achieving 1.96 times the token efficiency of text reasoning. These results show that images can effectively and efficiently encode rationales while providing a unified visual canvas for reasoning.

---


### 310. [Automated IEP Generation from Traditional Chinese Parent-Teacher Interviews via Corpus-Grounded Feature Diffusion](https://arxiv.org/abs/2606.09603)

**<font color=#1a73e8>作者：</font>** Kuanlin Chen, Cheng-En Ou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Writing Individualized Education Programs (IEPs) is a high-labor, knowledge-intensive document burden; English-language research has demonstrated that generative AI can significantly reduce drafting time, yet automated IEP generation in Traditional Chinese remains virtually unexplored due to domain data scarcity, strict privacy regulations, and the absence of local evaluation benchmarks. We propose a low-resource fine-tuning pipeline centered on Corpus-Grounded Feature Diffusion (CGFD): (1) 25 dual-expert high-score seed transcripts are selected via a tau threshold with flag-aware score caps; (2) a FeatureProfile (sentence length, structure, quantification templates) is extracted from seeds and injected into LLM prompts alongside Verbalized-Sampling-style diversity control to drive diffusion; (3) 15 expert gold seeds are used as diffusion anchors, targeting 585 samples; 567 valid diffusion samples are obtained, yielding a 582-sample training set used to fine-tune Breeze-7B with QLoRA; (4) schema-constrained inference via Grammar-Constrained Decoding (GCD) enforces a hierarchical SMART Goal Ladder schema at inference time. Ablation results on a 55-sample schema stress set reveal an unexpected finding: GCD is counterproductive under Traditional Chinese token budgets -- the no-GCD path achieves 100% schema pass rate at 34% lower median latency, outperforming GCD on both reliability and speed. On the n=10 formal hold-out, the no-GCD inference path achieves BERTScore F1 = 0.779, exceeding GPT-5.4 (0.726), DeepSeek-V3.2 (0.703), Gemini-3-Flash-Preview (0.703), and Llama-4-Maverick (0.700) zero-shot baselines while maintaining fully local, air-gapped inference. This system addresses a gap in Traditional Chinese special-education NLP and offers a scalable, privacy-preserving local inference solution under an industrial engineering paradigm.

---


### 311. [AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving](https://arxiv.org/abs/2606.09613)

**<font color=#1a73e8>作者：</font>** Rakibul Hasan Rajib, Mengxin Zheng, Qian Lou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn LLM agents interleave model calls with external tool invocations, shifting serving from stateless request processing to stateful program execution. Serving these workloads requires scheduling, KV-cache management, and routing policies that use program-level context, including turn dependencies, tool-induced gaps, and reusable KV state. Evaluating such policies directly on real systems is costly, since each design point may require dedicated accelerator time across arrival rates, model scales, serving-instance counts, and memory hierarchies. Simulation offers a scalable alternative, but existing LLM serving simulators target stateless request-level workloads and therefore omit the core dynamics of agent serving: multi-turn program execution, cross-turn cache locality, and KV-cache residency during tool gaps. We present AGENTSERVESIM, a hardware-aware simulator for multi-turn LLM agent serving. AGENTSERVESIM evaluates serving policies at program granularity through composable modules: a Program Orchestrator preserves program identity and turn order, a Tool Simulator materializes tool-induced gaps, a Session-Aware Router maintains program-to-instance affinity for cache-aware dispatch, and a KV Residency Model tracks policy-defined KV placement across HBM, host DRAM/CXL, and eviction. Across real serving deployments and hardware configurations, AGENTSERVESIM reproduces real-system behavior within 6% error across key performance metrics while running entirely on commodity CPUs. These results show that AGENTSERVESIM enables controlled, repeatable exploration of agent-serving policies without requiring exhaustive deployment on costly accelerators.

---


### 312. [Civil Court Simulation with Large Language Models](https://arxiv.org/abs/2606.09632)

**<font color=#1a73e8>作者：</font>** Yifan Chen, Haitao Li, Kaiyuan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Court simulation bridges legal education and judicial practice, yet human-based simulations are costly and difficult to scale. Large language models (LLMs) offer a scalable alternative, but existing court-simulation research mainly focuses on criminal cases. Civil litigation is more common in practice and harder to simulate because its claims, liability, and remedies are more flexible. We present a multi-agent court simulation framework for Chinese civil cases. The framework organizes role-based interaction through a five-stage civil trial procedure and integrates memory module and statute retrieval to support long-process adjudication. Experiments show that the framework produces reliable civil judgments, with clear strengths in liability allocation and multi-item adjudication. Further experiments show that memory quality substantially affects downstream simulation quality. Through a five-layer factor framework, we analyze how legal grounding, information conditions, judicial capability and role orientation, organizational pressure, and social context affect the framework's reliability and behavior. These results support the effectiveness of the proposed framework for civil court simulation. The dataset and code are available at: this https URL.

---


### 313. [Gradient-Guided Reward Optimization for Inference-time Alignment](https://arxiv.org/abs/2606.09635)

**<font color=#1a73e8>作者：</font>** Hankun Lin, Ruqi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ensuring the reliability of Large Language Models (LLMs) under distribution drift requires inference-time adaptation. While inference-time alignment methods such as Best-of-$N$ and rejection sampling are widely used, they frame the task as a sampling-intensive, reward-guided search, leading to two key limitations: their performance is bounded by the base model's generation quality, and their reliance on imperfect reward models makes them vulnerable to reward hacking. To address these challenges, we introduce Gradient-Guided Reward Optimization (GGRO), a lightweight inference-time method that performs targeted, minimal intervention during decoding via gradient guidance. Specifically, GGRO monitors token-level entropy to identify high-uncertainty regions indicative of drift or misalignment. Upon detection, it responds by injecting nudging tokens, generated using gradient signals from an off-the-shelf reward model, to steer the generation trajectory rather than merely re-ranking samples. Experiments show that GGRO consistently improves inference-time alignment across safety, helpfulness, and reasoning benchmarks. It also increases coverage of high-quality responses and robustness to reward hacking, with minimal computational overhead. Code is available at this https URL.

---


### 314. [Where Does the Answer Come From? Benchmarking View-Level Visual Evidence Identification in Multi-View MLLMs for Autonomous Driving](https://arxiv.org/abs/2606.09644)

**<font color=#1a73e8>作者：</font>** Yimu Wang, Yee Man Choi, Barry Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) achieve strong results on visual reasoning benchmarks, but answer accuracy alone does not indicate whether a model relied on the correct visual evidence. This gap is particularly important in multi-view driving scenes used for autonomous driving, where a model can produce a plausible answer while grounding it in the wrong camera view. We introduce a multi-view visual question answering benchmark for evaluating evidence-source identification: given six synchronized NuScenes views and a question, the model must identify the supporting camera view and answer the question. The benchmark contains 122 conflict-centric question-answer pairs from 73 scenes, spanning causality, counterfactual reasoning, and intent prediction. View labels are proposed by an automatic conflict-mining pipeline and manually verified by annotators. We evaluate three settings: camera-view selection, oracle QA given the golden view, and joint prediction in which the model selects a view and answers in one pass. Answers are evaluated in both multiple-choice and free-form formats, using exact match for structured predictions and an LLM judge for free-form responses. By explicitly separating visual-source identification from answer correctness, the benchmark exposes grounding failures that answer-only evaluation misses.

---


### 315. [Do Video Foundation Models Understand Intuitive Physics? A Layerwise Probing Analysis](https://arxiv.org/abs/2606.09646)

**<font color=#1a73e8>作者：</font>** Samuele Punzo, Niccolò Caselli, Ippokratis Pantelidis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study whether pretrained video foundation models encode intuitive-physics information in their frozen representations, and how this information varies across model families, layers, and probe types. Using frozen-feature probing on IntPhys2 and Minimal Video Pairs (MVP), we compare predictive joint-embedding models (V-JEPA), masked reconstruction models (VideoMAE), and a diffusion-based video generator (LTX-Video). V-JEPA achieves the strongest overall results across benchmarks, especially with probes that model temporal dynamics, while VideoMAE remains competitive and LTX-Video recovers weaker but non-trivial signal. Layerwise analyses show that physics-relevant information is weakest in early layers and becomes most accessible at intermediate-to-late depth, and temporal controls show that disrupting frame order substantially reduces performance, especially on MVP. Together, these results suggest that intuitive-physics knowledge emerges reliably in pretrained video representations, but its accessibility depends strongly on pretraining paradigm, representational depth, and readout mechanism.

---


### 316. [Muon Learns More Robust and Transferable Features than Adam](https://arxiv.org/abs/2606.09658)

**<font color=#1a73e8>作者：</font>** Tianyu Ruan, Fengzhuo Zhang, Shuche Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has recently emerged as a state-of-the-art optimizer for pretraining Large Language Models (LLMs) and vision classifiers. Despite its efficiency advantage over Adam and SGD, the feature-learning advantage of Muon remains unclear. This paper investigates Muon's feature-learning advantage through the lens of robustness and transferability. First, by evaluating pretrained models on corrupted images and texts, we show that features learned by Muon are consistently more robust than those learned by Adam and SGD across different architectures, including transformers and Convolutional Neural Networks (CNNs). Using trained layer-wise probes, we further show that this robustness advantage is reflected in larger logit margins across layers. Second, by training linear classifiers or fine-tuning full models from pretrained parameters on downstream tasks, we demonstrate that Muon-learned features transfer more effectively than those learned by Adam and SGD. This transferability advantage is further supported by the diversity of hidden states across layers, as measured by effective rank. Finally, in a representative classification problem with multi-component features, we prove that Muon attains larger margins and higher effective rank than Adam and SGD, providing theoretical support for our empirical findings.

---


### 317. [In-Context Learning for Latent Space Bayesian Optimization](https://arxiv.org/abs/2606.09664)

**<font color=#1a73e8>作者：</font>** Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.

---


### 318. [SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks](https://arxiv.org/abs/2606.09669)

**<font color=#1a73e8>作者：</font>** Hongcheng Gao, Hailong Qu, Jingyi Tang 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.

---


### 319. [PsychoSafe: Eliciting Psychologically-Informed Refusals in Large Language Models](https://arxiv.org/abs/2606.09697)

**<font color=#1a73e8>作者：</font>** Gianluca Barmina, Federico Torrielli, Sven Harms 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) routinely face requests that should be refused, creating a trade-off between helpfulness and harm prevention. However, refusals themselves can be helpful. In high-risk interactions involving crisis, coercion, or escalating intent, blunt non-compliance may prevent direct harm while still failing to support the needs of the person behind the request. We present PsychoSafe, a psychologically-informed refusal framework that reframes refusal as structured supportive communication grounded in evidence-based intervention strategies. To develop PsychoSafe, we construct a corpus of 8019 prompt-response pairs spanning five psychologically salient risk domains and apply prompting and parameter-efficient fine-tuning to Qwen 3.5 27B. On a balanced validation set of 500 prompts, evaluated with an LLM judge and validated through human ratings, PsychoSafe prompting improves overall refusal quality by 28.1% over a generic baseline, with particularly strong gains in external resource referral (+46.8%) and psychological grounding (+34.8%), while preserving downstream performance on non-refusal tasks. Fine-tuning achieves near-perfect refusal and resource-referral rates but reduces response relevance. Additional evaluations on SORRY-Bench and XSTest show strong in-domain robustness but limited out-of-domain generalization, suggesting that future work should diversify fine-tuning data to help models apply interventions selectively rather than schematically.

---


### 320. [Learning to Attack and Defend: Adaptive Red Teaming of Language Models via GRPO](https://arxiv.org/abs/2606.09701)

**<font color=#1a73e8>作者：</font>** Blake Bullwinkel, Eugenia Kim, Amanda Minnich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI red teaming must continually adapt to evolving attackers and defenders. Reinforcement learning offers a promising approach to discovering novel attacks, and co-training methods can produce more robust defenders in tandem. Recent works have demonstrated the efficacy of attacker-defender co-training by applying PPO and DPO, but report that GRPO is unstable in this setting. We introduce AdvGRPO, a co-training framework that makes GRPO viable for joint attacker-defender optimization using dense multi-channel rewards and decoupled advantage normalization. Training progresses through a curriculum from single-turn to closed-loop multi-turn attacks before bootstrapping co-training, where attacker and defender models are updated in alternation. We show that our method can produce highly effective and transferable attacks and that co-trained defenders outperform baselines on safety benchmarks.

---


### 321. [IS-CoT: Breaking the Long-form Generation Collapse via Interleaved Structural Thinking](https://arxiv.org/abs/2606.09709)

**<font color=#1a73e8>作者：</font>** Zechen Sun, Yuyang Sun, Zecheng Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating coherent and controllable long-form content remains a persistent challenge for Large Language Models (LLMs). While reasoning-enhanced models have demonstrated success in logic-intensive domains, our evaluation reveals that they suffer from a severe length collapse in open-ended writing, where performance degrades sharply as target lengths exceed 2,000 words. We attribute this failure to the limitation of static hierarchical planning, which struggles to provide dynamic guidance over extended contexts. To bridge this gap, we introduce the Interleaved Structural Chain-of-Thought (IS-CoT) framework. Unlike external agentic workflows, IS-CoT embeds a dynamic Plan-Write-Reflect cycle into the generation process, enabling continuous strategy adaptation and global alignment without additional assistance. Based on this framework, we construct a high-quality dataset of interleaved reasoning traces via a multi-teacher pipeline and train IS-Writer-8B. Experiments demonstrate that IS-Writer-8B achieves state-of-the-art performance on challenging long-form benchmarks (e.g., +3.08 vs. DeepSeek-V3.2 on LongBench-Write), exhibiting robust length compliance and coherence competitive with significantly larger proprietary models.

---


### 322. [Beyond Probabilistic Similarity: Structural, Temporal, and Causal Limitations of Retrieval-Augmented Generation in the Legal Domain](https://arxiv.org/abs/2606.09724)

**<font color=#1a73e8>作者：</font>** Hudson de Martim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has become a standard architectural response to unreliability in legal AI, yet high-profile failures, including fabricated citations submitted to courts and anachronistic legal content presented as current, continue to appear across jurisdictions. We argue that these failures are not residual confabulations to be eliminated by scaling language models, but symptoms of an architectural mismatch between probabilistic retrieval and the hierarchical, temporal, and institutional structure of legal knowledge. We develop the argument in three moves. First, we articulate the ontological commitment of legal knowledge as a triad of properties derivable from classical legal theory: hierarchical and mereological structure, diachronic dynamism under operational closure, and causal traceability of institutional provenance grounded in the duty of justification. Second, we identify three corresponding pathologies of retrieval (mereological blindness, diachronic blindness, and causal opacity), each developed with an operational definition, a failure mechanism, a canonical example, and detection criteria for diagnostic use. Third, we review the state of the art through this lens, showing that existing approaches address these requirements unevenly and do not yet compose into a paradigm that treats them as co-constitutive. From this analysis we derive four architectural commitments that characterize the deterministic-by-design direction for legal retrieval: ontological primacy, event reification, bitemporal correctness, and deterministic interaction protocols. The framework concerns quaestio juris (which norms apply and in what state) rather than the downstream tasks that act on identified norms, and addresses legislative and constitutional retrieval primarily, with interpretive time as an explicit extension.

---


### 323. [SearchSwarm: Towards Delegation Intelligence in Agentic LLMs for Long-Horizon Deep Research](https://arxiv.org/abs/2606.09730)

**<font color=#1a73e8>作者：</font>** Pu Ning, Quan Chen, Kun Tao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly expected to handle complex, long-horizon real-world tasks whose context demands can grow without bound, yet model context windows remain inherently finite. Recent work explores a paradigm where a main agent decomposes tasks and dispatches subtasks to subagents, which execute and return only summarized results, conserving the main agent's context budget. However, performing this well requires delegation intelligence: the ability to decompose complex tasks, determine when and what to delegate, and integrate returned results into the ongoing workflow. Training data for this capability is scarce in naturally occurring text, and to our knowledge, how to synthesize such data and train models to acquire this capability remains largely unexplored in the open-source community. To bridge this gap, we present a preliminary exploration targeting deep research, a representative long-horizon agent task. Specifically, we design a harness that guides the model toward high-quality task decomposition and delegation, while constraining subagents to return results properly to support the main agent's workflow. The harness-guided trajectories naturally encode correct delegation decisions, which we use as supervised fine-tuning data to internalize delegation intelligence into model weights. Our resulting model, SearchSwarm-30B-A3B, achieves 68.1 on BrowseComp and 73.3 on BrowseComp-ZH, the best results among all models of comparable scale. We will release our harness, model weights, and training data to facilitate future research.

---


### 324. [The Neutral Mask: How RLHF Provides Shallow Alignment while Leaving Partisan Structure Intact in a Large Language Model](https://arxiv.org/abs/2606.09735)

**<font color=#1a73e8>作者：</font>** Wendy K. Tam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The ambition behind alignment training is to make large language models safe and useful. The primary mechanism, reinforcement learning from human feedback (RLHF), shapes the behavior of deployed language models by aligning them with ``human values.'' Yet the process is opaque. What values are being encoded; whose values are they; and how does RLHF encode them? A growing body of evidence suggests that RLHF produces only functional compliance rather than deep alignment. We offer a mechanistic case study of this phenomenon for partisan political orientation with a comparison of the internal representations of Llama 3.1 8B before and after RLHF. We show that RLHF does not remove the structured partisan direction in the base model. Instead, it compresses the variance of the partisan signal to generate consistently balanced and non-partisan output. Sparse autoencoder decomposition reveals that policy-encoding features, which activate sporadically in the base model, are completely inactive in the Instruct model. Feature-level steering experiments confirm the causal disconnect. RLHF thus encodes a norm of political neutrality, not by erasing the model's knowledge of partisanship, but by severing the causal pathway from partisan geometry to output generation. Importantly, this neutrality is functional, not structural so that the underlying geometry that enables partisan steering remains intact. The mechanisms that bypass RLHF's guardrails, such as inferring and amplifying a user's partisan identity, reactivate partisan generation. If RLHF operates by disconnecting rather than removing value-laden structure, then the same pattern may hold for other value domains, and the aligned model's behavior may be more fragile than its outputs suggest.

---


### 325. [HDSL: A Hierarchical Domain-Specific Language for Structured 3D Indoor Scene Generation and Localized Editing with LLM Agents](https://arxiv.org/abs/2606.09738)

**<font color=#1a73e8>作者：</font>** Letian Li, Chao Shen, Shuzhao Xie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven indoor scene generation and editing require an intermediate representation that language models can both produce and revise. Existing LLM-based systems often rely on scene graphs or global constraint lists, which are compact but underspecify local geometry and make instruction-based edits difficult to localize. We frame this problem as structured program generation and local program repair, and propose Hierarchical Descriptive Scene Language (HDSL), an XML/CSS-style domain-specific language for structured 3D indoor scenes. HDSL represents rooms, regions, objects, and support surfaces as a tree with local coordinates, making complex scenes easier to plan recursively and easier to retrieve for editing. Our pipeline uses LLM agents to generate HDSL subtrees with bounded verification, grounds non-virtual nodes through multimodal asset retrieval, and applies force-directed layout optimization to repair boundary and collision errors. For editing, Hierarchical Retrieval-Augmented Generation retrieves the relevant subtree, asks the LLM to rewrite only that local context, and merges the result back through a deterministic three-way merge. In our reproduced benchmark, HDSL improves average object coverage, text-scene alignment, and generation time over full text-to-scene baselines while remaining competitive with recent layout-only reproductions on geometry metrics; for editing, HRAG reduces token use by $5.22\times$ and runtime by $6.19\times$, produces valid DSL for all eight paired edits, and better preserves unrelated scene objects.

---


### 326. [Data Synthesis and Parameter-Efficient Fine-Tuning for Low-Resource NMT: A Case Study on Q'eqchi' Mayan](https://arxiv.org/abs/2606.09767)

**<font color=#1a73e8>作者：</font>** Alexander Chulzhanov, Soeren Eberhardt, Arjun Mukherjee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural machine translation for digitally low-resource Indigenous languages is often hindered by extreme data scarcity, prompting reliance on extractive web-scraping. To ensure data sovereignty, this study introduces a data synthesis methodology to bootstrap NMT models without scraping target-language parallel text. Focusing on Q'eqchi' Mayan, we transformed community-sourced dictionaries into a massive synthetic corpus, utilizing Parameter-Efficient Fine-Tuning (PEFT) via LoRA adapters on an mT5-base model.
In-domain evaluation demonstrates high structural acquisition (BLEU 42.02), proving that synthetic constraints effectively teach complex agglutinative morphology and VOS word order. However, evaluation against an organic glossary reveals a structural-semantic gap (BLEU 0.59), where the model maintains grammatical integrity but lacks the lexical grounding of natural language. The model exhibits overfitting to the constrained structural variance of the synthetic templates; despite high semantic entropy in the pipeline, it struggles with the syntactic fluidity of natural language, forcing organic inputs into rigid learned patterns. Furthermore, an ablation study utilizing a Multi-Task Learning architecture resulted in negative transfer, suggesting that auxiliary tasks competed for limited parameter capacity within the LoRA adapters, causing over-optimization for synthetic markers at the expense of organic flexibility. Ultimately, we establish that synthetic bootstrapping is a highly effective structural primer, but requires authentic data for semantic refinement via Curriculum Learning.

---


### 327. [SemDINO: A DINOv3-Driven Network for Cross-Temporal Semantic Alignment in Change Detection](https://arxiv.org/abs/2606.09772)

**<font color=#1a73e8>作者：</font>** Xinyu Tong, Meihua Zhou, Jinxiao Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic change detection (SCD) aims to simultaneously locate land-cover changes and identify semantic categories before and after transition. However, existing methods suffer from insufficient cross-temporal alignment, weak multi-scale representation, and poor robustness to pseudo-changes caused by illumination, season, and registration noise. To address these issues, we propose a novel end-to-end semantic change detection network named SemDINO, which integrates a dual-branch encoder, multi-scale temporal interaction, semantic purification, change enhancement, and decoupled multi-task prediction into a unified framework. Specifically, we construct a dual-branch encoder that combines a CNN backbone and frozen DINOv3 features via gated pyramid fusion, enabling rich multi-scale semantic representation. Then, a multi-scale temporal bidirectional transformer interaction (M-TBTT) module is proposed to achieve global cross-temporal feature alignment and information interaction. To further enhance genuine changes and suppress pseudo-variations, we introduce semantic purification (SCP), bidirectional change enhancement (BiChangeEnhance), and multi-scale change enhancement (MCE) modules collaboratively. Finally, a multi-branch CD prediction head is designed to jointly output binary change mask, bi-temporal semantic maps, and edge constraint. Extensive experiments on public remote sensing CD datasets demonstrate that SemDINO achieves superior performance and generalization ability against state-of-the-art methods, especially in complex scenarios with interference factors.

---


### 328. [Echo-Memory: A Controlled Study of Memory in Action World Models](https://arxiv.org/abs/2606.09803)

**<font color=#1a73e8>作者：</font>** Wayne King, Zeyue Xue, Yuxuan Bian 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present \textbf{Echo-Memory}, a controlled study of memory mechanisms in action-conditioned world models. These models generate multi-segment videos from a first frame, text prompt, and camera-action sequence, but their central failure is often memory rather than local image synthesis: after the camera leaves and returns, the scene or salient object may silently change. Existing memory designs are hard to compare because gains are entangled with backbone, training, retrieval, and evaluation differences. Echo-Memory fixes the action-to-video interface and varies only how history is stored and read by the generator. Under a shared video diffusion backbone, optimizer, camera-action representation, sampler, and evaluation pipeline, we compare raw context, compression-based memory, spatial summaries with different read-out paths, and state-space recurrence. This matched matrix separates four otherwise conflated axes: \emph{capacity}, \emph{compression}, \emph{read-out}, and \emph{recurrence}. We also evaluate memory through a three-branch protocol: replay quality, in-domain loop revisit, and open-domain return probes. The branches routinely disagree, showing that replay fidelity is not a sufficient proxy for remembering a world. Three findings follow. Raw context is a strong capacity baseline and improves open-domain return far more than it improves replay metrics. Compactness is not a free substitute for capacity: aggressive spatial and hybrid-compression memories lose the salient evidence needed for return. Finally, block-wise state-space recurrence is the strongest open-domain return mechanism in our matrix, showing that the structure of implicit memory matters as much as the decision to use it. These results provide a compact protocol for studying memory in action world models beyond isolated replay metrics.

---


### 329. [Rethinking the Divergence Regularization in LLM RL](https://arxiv.org/abs/2606.09821)

**<font color=#1a73e8>作者：</font>** Jiarui Yao, Xiangxin Zhou, Penghui Qi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a key component of post-training large language models (LLMs). In practice, LLM RL is often off-policy because of training-inference mismatch and policy staleness, making trust-region control essential for stable optimization. Mainstream methods such as PPO and GRPO approximate this control with a ratio-clipping mechanism, but the importance ratio can be a poor proxy for distributional shift in long-tailed vocabularies. Recent work such as DPPO addresses this mismatch by replacing ratio-based clipping with a divergence-based mask, yielding a trust region defined by the sampled token's absolute probability shift. However, DPPO still relies on a hard mask: once a token crosses the trust-region boundary in a harmful direction, its gradient is discarded rather than corrected. To address this, we propose Divergence Regularized Policy Optimization (DRPO), which replaces the hard mask with a smooth advantage-weighted quadratic regularizer on policy shift. DRPO preserves the same trust-region geometry as DPPO while inducing bounded, continuous gradient weights that attenuate diverging updates and provide corrective signals beyond the boundary. Experiments across model scales, architectures, and precision settings show that DRPO improves the stability and efficiency of LLM RL training.

---


### 330. [OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics](https://arxiv.org/abs/2606.09826)

**<font color=#1a73e8>作者：</font>** Mingxian Lin, Shengju Qian, Yuqi Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language model (VLM) agents are increasingly deployed in interactive game environments. Yet game benchmarks for VLM agents typically report a single first-attempt score per (agent, game) pair, focus on single-agent Solo play, and lack unified protocols for evaluating heterogeneous agent classes (commercial VLMs, open-weight VLMs, and specialized game policies) on the same footing. We address these gaps with OmniGameArena, a real-time benchmark of twelve newly built Unreal Engine 5 games spanning Solo (7), PvP (3), and Coop (2) with unified action interfaces, and the Improvement Dynamics Curve (IDC), an agentic-reflection harness in which a tool-using reflector LLM autonomously refines a bounded skill prompt across multiple rounds. Beyond cold-start leaderboard scores, IDC exposes two additional observables for each (agent, game) pair: how the score evolves across reflection rounds, and how the learned skill behaves on held-out task variants. We report these observables for twelve VLM agents on the cold-start leaderboard and four top agents under IDC.

---


### 331. [Latent Spatial Memory for Video World Models](https://arxiv.org/abs/2606.09828)

**<font color=#1a73e8>作者：</font>** Weijie Wang, Haoyu Zhao, Yifan Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models that maintain 3D spatial consistency across generated frames typically rely on explicit point cloud memory constructed in RGB space. This design is both computationally expensive, requiring repeated rendering and VAE encoding, and inherently lossy, as the round trip through pixel space discards rich features of the learned latent representation. In this paper, we introduce \emph{latent spatial memory} for video world models, a persistent 3D cache that stores scene information directly in the diffusion latent space, avoiding pixel-space reconstruction. Building on this, we propose Mirage, a latent-space spatial memory framework that constructs the memory by lifting latent tokens into 3D via depth-guided back-projection and queries it by synthesizing novel views through direct latent-space warping. This unified formulation eliminates both the information loss of pixel-space reconstruction and the computational burden of repeated encoding and rendering. Experiments show that latent spatial memory achieves up to \textbf{10.57}$\times$ faster end-to-end video generation and \textbf{55}$\times$ reduction in memory footprint relative to explicit 3D baselines. Leveraging the geometric prior of the diffusion model, Mirage attains state-of-the-art performance on WorldScore and strong reconstruction quality on RealEstate10K.

---


> [!TIP]
> 当前位于：**301-331**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-331**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
