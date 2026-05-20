# 🧠 大模型相关研究 | 2026年05月21日

> 本类共 **172** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-172](./part-04.md)

---

### 101. [Investigating Cross-Modal Skill Injection: Scenarios, Methods, and Hyperparameters](https://arxiv.org/abs/2605.19523)

**<font color=#1a73e8>作者：</font>** Zhiyu Xu, Lean Wang, Yuanxin Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated remarkable proficiency in general multi-modal understanding; yet they struggle to efficiently acquire continually evolving domain-specific skills. Conventional approaches to enhancing VLM capabilities, such as Supervised Fine-Tuning (SFT), require extensive dataset curation and substantial computational resources. Model merging has emerged as an efficient alternative that enables the transfer of domain-specific expertise from Large Language Models (LLMs) to VLMs without incurring additional training data requirements or significant computational overhead. Unlike conventional merging of homogeneous LLMs, which mainly aggregates existing capabilities, cross-modal skill injection aims to induce emergent cross-modal capabilities by integrating a domain-expert LLM into a VLM. However, existing research lacks a systematic analysis of the applicability and methodology of cross-modal skill injection. In this study, we investigate cross-modal skill injection across three main aspects: scenarios, methods, and hyperparameters. For scenarios, we find that cross-modal skill injection generally performs well in instruction-following and cross-lingual settings, yet struggles with mathematical reasoning. For methods, we find that classic approaches such as TA and DARE consistently achieve superior performance over alternative merging methods. We also provide a systematic and quantitative analysis of the hyperparameter tuning that these classic methods critically depend on.

---


### 102. [Towards Camera-Robust 3D Localization: Equation-Anchored Tool-Use for MLLMs](https://arxiv.org/abs/2605.19528)

**<font color=#1a73e8>作者：</font>** Xueying Jiang, Wenhao Li, Quanhao Qian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D localization in Multimodal Large Language Models (MLLMs), including 3D object detection and 3D visual grounding, is fundamentally limited by camera intrinsic ambiguity: the same image admits different 3D scenes under different cameras. Existing MLLMs either ignore camera parameters and overfit to a canonical training intrinsic, or retrieve depth and 3D cues from external tools but treat the returned values as reference cues (numerical hints that the model is free to interpret implicitly), both preventing camera information from being deterministically propagated into the prediction. We propose an equation-anchored tool-use framework that re-purposes spatial tools as formula variables. The proposed framework proactively retrieves camera intrinsics and samples multi-point metric depths, writes the pinhole back-projection equation $\hat{X} = (u_c - c_x)\bar{Z}/f_x$ explicitly in Chain-of-Thought (CoT), and substitutes tool outputs into the formula before regressing the final 9-DoF bounding box. On both 3D object detection and 3D visual grounding tasks under rescaled camera intrinsics from $0.5\times$ to $1.5\times$, our method outperforms RGB-only and tool-augmented baselines, with significant gains where the camera deviates most from the training scale. Code and data will be released.

---


### 103. [Generative-Evaluative Agreement: A Necessary Validity Criterion for LLM-Enabled Adaptive Assessment](https://arxiv.org/abs/2605.19529)

**<font color=#1a73e8>作者：</font>** Grandee Lee, Yue Wang, Che Yee Lye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When the same LLM generates assessment items, simulates student responses, and scores them, the validation loop is self-referential. We introduce Generative-Evaluative Agreement (GEA), a validity criterion measuring whether an LLM's scoring function recovers the skill levels its generative function was instructed to produce. In the first direct measurement of GEA on a two-stage adaptive assessment, the model recovers roughly half the intended variance r = 0.698 with systematic positive bias. GEA is strong r > 0.7 for syntactically verifiable skills but near zero for design-level skills, and low-skill overestimation inflates scores near the routing threshold. We argue that granular, skill-decomposed rubrics are the principal proposed mechanism for strengthening GEA and outline complementary mitigations.

---


### 104. [The Silent Hyperparameter: Quantifying the Impact of Inference Backends on LLM Reproducibility](https://arxiv.org/abs/2605.19537)

**<font color=#1a73e8>作者：</font>** David Pape, Jonathan Evertz, Lea Schönherr  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Progress in LLMs is increasingly measured through standardized benchmarks, where state-of-the-art improvements are often separated by fractions of a percentage point. At the same time, the computational cost of evaluating modern LLMs has driven widespread adoption of specialized inference backends, software systems that execute trained models efficiently at inference time. While critical for scalability, system-level optimizations, such as custom CUDA kernels and reduced-precision arithmetic, can alter token probabilities and introduce non-determinism, possibly cascading into divergent generation. In this work, we first survey the inference landscape, identifying 200 distinct engines, and analyze 35,000 ML publications, finding that the specific inference stack is rarely reported despite this widespread diversity. We then present a systematic empirical study of how inference backends affect LLM benchmark results. Holding model weights, decoding parameters, and hardware constant, we evaluate five widely used inference engines, including vLLM, SGLang, and this http URL, across multiple open-weight models and established benchmarks. We show that the choice of backend alone can shift benchmark scores by up to 16.6 percentage points and induce high rates of output disagreement. By isolating backend optimizations and tracing the execution pipeline, we find this divergence is driven by system-level optimizations like prefix caching and CUDA graphs, custom kernels, and engine-specific defaults in logit processing. Our findings identify the inference backend as a previously unreported but consequential hyperparameter in the evaluation of LLM and advocate standardized reporting of inference stacks to improve the reproducibility and interpretability of benchmark comparisons.

---


### 105. [EgoCoT-Bench: Benchmarking Grounded and Verifiable Operation-Centric Chain of Thought Reasoning for MLLMs](https://arxiv.org/abs/2605.19559)

**<font color=#1a73e8>作者：</font>** Yang Dai, Dian Jiao, Tianwei Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid development of Multimodal Large Language Models (MLLMs) has led to growing interest in egocentric video understanding, specifically the ability for MLLMs to recognize fine-grained hand-object interactions, track object state changes over time, and reason about manipulative processes in dynamic environments from a first-person perspective. However, existing egocentric video benchmarks suffer from \textbf{limited grounded rationale evaluation}, offering limited support for fine-grained operation-centric reasoning and rarely examining whether model rationales are grounded in explicit spatio-temporal evidence. To address this gap, we introduce \textbf{EgoCoT-Bench}, a fine-grained egocentric benchmark for grounded and verifiable operation-centric reasoning with explicit step-by-step rationale annotations. Overall, EgoCoT-Bench comprises 3,172 verifiable QA pairs over 351 egocentric videos separated into four task groups for a total of 12 sub-task groups, encompassing perception and retrospection, anticipation, and high-level reasoning. The benchmark is constructed through a spatio-temporal scene graphs (STSG) guided generation framework and is further refined by human annotators to ensure correctness, egocentric relevance and fine-grained quality. Experimental results show continuing difficulties with egocentric fine-grained reasoning and further reveal that many multimodal models produce explanations that are answer-correct, but have evidence that is inconsistent with the answer. We hope EgoCoT-Bench can serve as a useful testbed for grounded and verifiable reasoning in egocentric video understanding. Project page and supplementary materials are available at: this https URL.

---


### 106. [TORQ: Two-Level Orthogonal Rotation for MXFP4 Quantization](https://arxiv.org/abs/2605.19561)

**<font color=#1a73e8>作者：</font>** Zukang Xu, Xing Hu, Dawei Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) advance toward practical deployment, the Microscaling FP4 (MXFP4) format has emerged as a cornerstone for next-generation low-bit inference, owing to its ability to balance high dynamic range with hardware efficiency. However, directly applying MXFP4 to LLM activation quantization inevitably leads to significant accuracy degradation. In this paper, we theoretically analyze the error structure of MXFP4 activation quantization, revealing that the root cause of this performance drop lies in two structural imbalances between activation distributions and the MXFP4 block floating-point format: (1) extreme inter-block variance imbalance and (2) intra-block codebook utilization imbalance. To address these challenges, we propose TORQ (Two-level Orthogonal Rotation for MXFP4 Quantization), a training-free Post-Training Quantization (PTQ) framework designed to reshape the geometric properties of the activation space through optimal coordinate transformations. At the macroscopic level, TORQ leverages the Schur-Horn theorem to redistribute activation energy via inter-block orthogonal rotation, preventing high-variance blocks from driving up shared scaling factors and thereby preserving the precision of small-magnitude elements. At the microscopic level, TORQ employs maximum-entropy-guided intra-block rotation to alleviate codebook collapse and maximize the MXFP4 codebook's information capacity. Experiments on mainstream LLMs such as LLaMA3 and Qwen3 show that TORQ significantly improves the accuracy of MXFP4 activation quantization compared to existing methods: on Qwen3-32B, the perplexity on WikiText is reduced to 8.43 (vs. 7.61 for BF16), and the average accuracy increases from 38.40% with direct RTN to 73.63% (vs. 74.82% for BF16), substantially narrowing the gap between 4-bit floating-point quantization and full-precision inference.

---


### 107. [Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries](https://arxiv.org/abs/2605.19576)

**<font color=#1a73e8>作者：</font>** Xing Zhang, Yanwei Cui, Guanghui Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving skill libraries face a silent failure mode we term \emph{library drift}: unbounded skill accumulation without outcome-driven lifecycle management causes retrieval degradation, false-positive injections, and performance stagnation. Recent evaluation confirms the symptom--LLM-authored skills deliver +0.0pp gain while human-curated ones deliver +16.2pp (SkillsBench)--yet the underlying mechanism has not been isolated. We provide (1) a reproducible trigger: ablations that isolate drift--one disables skill injection (flat floor, +0.002), one imposes premature retirement (active harm, $-$0.019); (2) trace-level diagnostics: an append-only evidence log with per-skill contribution scores, attribution verdicts, and router engagement metrics that make the failure visible before it reaches end-task scores; and (3) a verified fix: a minimal governance recipe (outcome-driven retirement + bounded active-cap + meta-skill authoring prior) that lifts held-out pass@1 from a 0.258 baseline to a late-window mean of 0.584 (rolling gain $+$0.328) on MBPP+ hard-100 over 100 rounds. Eight ablations decompose which governance mechanisms are load-bearing and which are subsumed, providing a concrete playbook for diagnosing library drift in any self-evolving agent.

---


### 108. [GoLongRL: Capability-Oriented Long Context Reinforcement Learning with Multitask Alignment](https://arxiv.org/abs/2605.19577)

**<font color=#1a73e8>作者：</font>** Minxuan Lv, Tiehua Mei, Tanlong Du 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present GoLongRL, a fully open-source, capability-oriented post-training recipe for long-context reinforcement learning with verifiable rewards (RLVR). Existing long-context RL methods often treat data construction as a matter of designing increasingly complex retrieval paths, leading to homogeneous task coverage and reward formulations that inadequately reflect practical long-context requirements. Our work offers two contributions. (1) Capability-oriented data construction with full open release. We openly release a dataset of 23K RLVR samples, the complete construction pipeline, and all training code. Guided by a taxonomy of long-context capabilities, the dataset spans 9 task types, each paired with its natural evaluation metric. It comprises curated open-source samples from established corpora and synthetic samples whose QA pairs are generated from real source documents such as books, academic papers, and multi-turn dialogues. Under the same vanilla GRPO setup, our dataset alone outperforms the closed-source QwenLong-L1.5 dataset. Moreover, our Qwen3-30B-A3B model trained on this data delivers long-context performance comparable to DeepSeek-R1-0528 and Qwen3-235B-A22B-Thinking-2507, suggesting that broader coverage and greater reward diversity substantially benefit long-context capability improvement. (2) TMN-Reweight for heterogeneous multitask optimization. To address optimization challenges from heterogeneous rewards, we propose TMN-Reweight, which combines task-level mean normalization for cross-task reward scale alignment with difficulty-adaptive weighting for more reliable advantage estimation. TMN-Reweight further improves average performance over vanilla GRPO, with general capabilities preserved or improved across reported evaluations.

---


### 109. [Towards Multi-Model LLM Schedulers: Empirical Insights into Offloading and Preemption](https://arxiv.org/abs/2605.19593)

**<font color=#1a73e8>作者：</font>** Mert Yildiz, Pietro Spadaccino, Alexey Rolich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern deployments of Large Language Models (LLMs) increasingly require serving multiple models with diverse architectures, sizes, and specialization on shared, heterogeneous hardware. This setting introduces new challenges for resource allocation, dispatching, and scheduling, particularly under GPU memory constraints where partial CPU-GPU offloading and preemption become necessary. While existing systems primarily optimize throughput for a single model, comparatively little work addresses multi-model scheduling under these conditions. In this paper, we present an empirical study of how different LLMs behave across hardware platforms, focusing on the performance implications of layer offloading and preemption. We show that offloading leads to strongly non-linear and model-dependent degradation in decode throughput, with smaller models exhibiting sharper sensitivity to reduced GPU residency. We further demonstrate that preemption incurs substantial overhead, largely dominated by model state reload rather than key-value cache transfer, and that this cost varies significantly across models and hardware platforms. Additionally, we highlight the role of sequence length and interconnect bandwidth in amplifying data movement and execution inefficiencies. Based on these findings, we identify a set of key features that future schedulers must consider, including model-specific offloading sensitivity, workload characteristics, and the cost structure of preemption and data transfer. These insights provide guidance for the design of next-generation LLM serving systems capable of efficiently managing heterogeneous, multi-model workloads with hybrid CPU-GPU execution.

---


### 110. [A novel YOLO26-MoE optimized by an LLM agent for insulator fault detection considering UAV images](https://arxiv.org/abs/2605.19595)

**<font color=#1a73e8>作者：</font>** João Pedro Matos-Carvalho, Laio Oriel Seman, Stefano Frizzo Stefenon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The inspection of electrical power line insulators is essential for ensuring grid reliability and preventing failures caused by damaged or degraded insulation components. In recent years, Unmanned Aerial Vehicles (UAVs) combined with deep learning-based vision systems have emerged as an effective solution for automating this process. However, insulator fault detection remains challenging due to small defect regions, heterogeneous fault patterns, complex backgrounds, and varying imaging conditions. To address these challenges, this paper proposes an optimized YOLO26-MoE, a novel object detection architecture that integrates a sparse Mixture-of-Experts (MoE) module into the high-resolution branch of the YOLO26 detector. The proposed modification enables adaptive feature refinement for subtle and diverse fault patterns while preserving the efficiency of a one-stage detection framework. Hyperparameter optimization, final training, and evaluation were coordinated through a tool-augmented Large Language Model (LLM) agent. The proposed model achieved 0.9900 mAP@0.5 and 0.9515 mAP@0.5:0.95, outperforming the latest YOLO versions. These results demonstrate that the proposed model provides an effective and reliable solution for UAV-based insulator fault detection.

---


### 111. [LLMEval-Logic: A Solver-Verified Chinese Benchmark for Logical Reasoning of LLMs with Adversarial Hardening](https://arxiv.org/abs/2605.19597)

**<font color=#1a73e8>作者：</font>** Ming Zhang, Qiyuan Peng, Yinxi Wei 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) on natural-language logical reasoning is essential because rule-governed tasks require conclusions to follow strictly from stated premises. Many existing logical-reasoning benchmarks are generated by templating natural-language items from sampled formulas, provide only coarse or unaudited formal annotations, and are now quickly saturated by frontier reasoning models. We present LLMEval-Logic, a Chinese logical reasoning benchmark built from realistic situational scenarios. Its pipeline forward-authors and expert-audits natural-language items together with their reference formalizations, verifies annotated answers with Z3, constructs expert rubrics for natural-to-formal grading, and hardens selected items through a closed-loop adversarial workflow. The benchmark is released in two paired subsets: a 246-item Base subset shipped with 1,400 expert-developed rubric atoms, and a 190-item Hard subset with 938 multi-step sub-questions over closed model spaces. Evaluating 14 frontier LLMs on LLMEval-Logic reveals substantial gaps in current models: the best model reaches only 37.5% Hard Item Accuracy, and even with reference symbols the highest joint Z3+Rubric formalization score among evaluated models reaches only 60.16%. Our benchmark is publicly available at this https URL.

---


### 112. [Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents](https://arxiv.org/abs/2605.19604)

**<font color=#1a73e8>作者：</font>** Xi Zhang, Meijun Gao, Yuntian Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents increasingly act inside real workspaces, where tools and skills determine whether model reasoning becomes reliable action. Existing skills remain largely informal: Markdown skills and instruction packs encode procedures as long natural-language documents, while function calling, Model Context Protocol (MCP) servers, and framework tools structure individual actions but usually leave workflow state, policy enforcement, and completion discipline outside the skill itself. We introduce Formal Skill, a runtime-native abstraction that represents reusable capability with JSON metadata and action schemas, reliable Python executors, hook-governed control logic, Formal Skill routing, and skill-local runtime state. By moving reusable procedure from repeated prompt text into executable state machines and hook policies, Formal Skill gives agents a token-efficient and enforceable control surface. We implement the abstraction in FairyClaw, an open-source event-driven runtime for executable, observable, and composable Formal Skills. On Harness-Bench, FairyClaw obtains highly competitive average scores while using substantially fewer tokens, with especially strong results on tasks that expose the role of Formal Skill.

---


### 113. [The Accessibility Capability Boundary: Operational Limits and Expansion Potential of AI-Generated Browser-Native Accessibility Systems](https://arxiv.org/abs/2605.19638)

**<font color=#1a73e8>作者：</font>** Rizwan Jahangir, Daisuke Ishii  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) demonstrate increasing competence in synthesizing functional user interfaces, a fundamental question emerges in accessibility computing: \textit{how far can AI-driven accessibility systems go?} This paper introduces the \textit{Accessibility Capability Boundary} (ACB), a formal framework for reasoning about the operational limits and expansion potential of autonomous accessibility systems, and grounds this theory in a real-world systems artifact. We model accessibility not as a binary compliance property but as a dynamic, multidimensional capability space constrained by measurable variables including deployment latency, cognitive load, infrastructure dependency, offline persistence, interaction complexity, and adaptability. We argue that AI-generated, browser-native systems constructed as single-file HTML artifacts leveraging standard browser APIs may dramatically shift the ACB outward by reducing deployment friction to near-zero and enabling rapid, context-specific interface adaptation. We ground our theoretical framework in the analysis of two real-world exploratory prototypes. The first is an AI-generated browser-native accessibility interface deployed for a blind user in Nepal. The second is a fully functional, open-source webcam alignment assistant for visually impaired users, serving as a concrete systems artifact. Through formal definitions, propositions, and a comparative evaluation matrix, we characterize the regions of the accessibility capability space that such systems can and cannot reach. We further identify remaining computational, infrastructural, and verification constraints that constitute the hard boundaries of this paradigm. This work contributes a theoretical foundation for understanding the scalable limits of autonomous accessibility computing and proposes a research agenda for future work in accessibility-aware AI systems.

---


### 114. [Benchmarking and Evolving Reason-Reflect-Rectify for Reflective Visual Generation](https://arxiv.org/abs/2605.19639)

**<font color=#1a73e8>作者：</font>** Junjie Wang, Xinghua Lou, Jason Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-Image (T2I) models and Unified Multimodal Models (UMMs) have achieved remarkable progress in visual generation. However, their reliance on a single-pass generation paradigm limits their ability to handle complex prompts requiring iterative refinement. To enable multi-round Reflective Visual Generation (RVG), we formalize the Reason-Reflect-Rectify (R^3) loop as a core framework and introduce R^3-Bench, a benchmark of over 600 expert-annotated instances that quantifies iterative reasoning and rectification capabilities. Evaluation on R^3-Bench reveals a critical gap: while state-of-the-art models can identify generation errors, they fail to generate actionable rectification instructions. To bridge this gap, we propose R^3-Refiner, a dual-stage framework leveraging Group Relative Policy Optimization (GRPO) and a Hierarchical Reward Mechanism (HRM) to better align rectification with reflective reasoning. Experiments show that R^3-Refiner achieves significant improvements on R^3-Bench (+12.0% in Reflective Verdict Score, +9.0% in Rectification Score), and can be seamlessly integrated with various MLLMs to enhance the generation quality of different T2I models on GenEval++ and T2I-CompBench. Code is available at this https URL.

---


### 115. [OScaR: The Occam's Razor for Extreme KV Cache Quantization in LLMs and Beyond](https://arxiv.org/abs/2605.19660)

**<font color=#1a73e8>作者：</font>** Zunhai Su, Rui Yang, Chao Zhang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid advancement toward long-context reasoning and multi-modal intelligence has made the memory footprint of the Key-Value (KV) cache a dominant memory bottleneck for efficient deployment. While the established per-channel quantization effectively accommodates intrinsic channel-wise outliers in Key tensors, its efficacy diminishes under extreme compression. In this work, we revisit the inherent limitations of the per-channel quantization paradigm from both empirical and theoretical perspectives. Our analysis identifies Token Norm Imbalance (TNI) as the primary bottleneck to quantization fidelity. We demonstrate that TNI systematically amplifies errors when shared quantization parameters are required to span token groups exhibiting substantial norm disparities. Instead of relying on intricate quantization pipelines (e.g., TurboQuant), we propose OScaR (Omni-Scaled Canalized Rotation), an accurate and lightweight KV cache compression framework for X-LLMs (i.e., text-only, multi-modal, and omni-modal LLMs). Advancing the per-channel paradigm, OScaR employs Canalized Rotation followed by Omni-Token Scaling to mitigate TNI-induced sequence-dimensional variance both effectively and efficiently, further supported by our optimized system design and CUDA kernels. Extensive evaluations across X-LLMs show that OScaR consistently outperforms existing methods and achieves near-lossless performance under INT2 quantization, establishing it as a robust, low-complexity, and universal framework that defines a new Pareto front. Compared with the BF16 FlashDecoding-v2 baseline, our OScaR implementation achieves a notable up to 3.0x speedup in decoding, reduces memory footprint by 5.3x, and increases throughput by 4.1x. The code for OScaR is publicly available at this https URL.

---


### 116. [When Tabular Foundation Models Meet Strategic Tabular Data: A Prior Alignment Approach](https://arxiv.org/abs/2605.19662)

**<font color=#1a73e8>作者：</font>** Xinpeng Lv, Yunxin Mao, Renzhe Xu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models based on pretrained prior-data fitted networks~(PFNs) have shown strong generalization on diverse tabular tasks, but they are typically designed for \emph{non-strategic} settings where data distributions are independent of deployed classifiers. In many real-world decision scenarios, however, individuals may strategically modify their features after deployment to obtain favorable outcomes, inducing a post-deployment distribution shift. This paper studies whether PFN-style tabular foundation models can generalize to such \emph{strategic} tabular data. We show that strategic manipulation creates a mismatch between the non-strategic prior learned during pretraining and the post-manipulation strategic prior, which leads to systematic prediction bias. To address this issue, we propose \textbf{Strategic Prior-data Fitted Network}~\textit{(SPN)}, an inference-time strategy-aware framework that adapts tabular foundation models to strategic environments without retraining. SPN constructs strategic in-context examples to approximate post-manipulation inputs and aligns PFN predictions with the induced strategic distribution. Experiments on real-world and synthetic tabular datasets show that SPN consistently improves robustness and predictive performance under strategic manipulation compared with both tabular foundation models and classical tabular methods.

---


### 117. [Pseudocode-Guided Structured Reasoning for Automating Reliable Inference in Vision-Language Models](https://arxiv.org/abs/2605.19663)

**<font color=#1a73e8>作者：</font>** Weicong Ni, Tianbao Jiang, Linlin Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are becoming the cornerstone of high-level reasoning for robotic automation, enabling robots to parse natural language commands and perceive their environments. However, their susceptibility to hallucinations introduces critical failures in decision-making, posing significant safety and reliability risks in physical deployments. This challenge is exacerbated by the open-ended nature of real-world tasks, where questions vary vastly in difficulty and modality, demanding robust and adaptable reasoning strategies. To tackle this, we propose the Pseudocode-guided Structured Reasoning framework (PStar), which adaptively selects structured pseudocode reasoning paths to help VLMs perform flexible and step-by-step reasoning. We first design a set of abstract reasoning functions and formulate a structured pseudocode library to represent modular reasoning strategies. Crucially, we design a Difficulty Feature Vector (DFV) that allows the model to assess question complexity and adaptively choose appropriate reasoning strategies-enhancing robustness and interpretability. Extensive experiments demonstrate that PStar significantly reduces hallucination rates, achieving state-of-the-art scores of 87.1% on POPE and 68.0% on MMStar, outperforming even GPT-4V. By providing a validated mechanism to reduce visual-language errors, PStar offers a critical step toward deploying more trustworthy and deterministic VLMs for real-world automated systems, where such errors can lead to catastrophic outcomes.

---


### 118. [Agentic Discovery of Cryomicroneedle Formulations](https://arxiv.org/abs/2605.19677)

**<font color=#1a73e8>作者：</font>** Hao Li, Lifu Du, Nurul Hameed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cryomicroneedles offer a route to minimally invasive intradermal delivery of living cells, but their cryogenic formulations must reconcile cell protection with constraints on toxicity and device fabrication. Here we report an AI-assisted, closed-loop workflow for cryomicroneedle cryoprotectant discovery that combines literature curation, Gaussian-process surrogate modelling, Bayesian optimization, and sequential wet-lab validation. A curated dataset of 198 mesenchymal stem-cell cryopreservation formulations from 42 studies was converted into 21 ingredient features and used to train an uncertainty-aware literature prior. This model captured moderate structure in the literature data but failed prospectively, motivating iterative wet-lab correction. Across ten validation iterations and 106 wet-lab observations, the model progressively adapted to cryomicroneedle-specific outcomes: batch RMSE decreased from 41.21 to 6.86 percentage points, later-stage rank correlations became consistently positive, and the cumulative wet-lab predicted-versus-measured summary reached $R^2 = 0.942$. The best validated formulation achieved 95.15\% post-thaw viability with low DMSO, ectoin, ethylene glycol, and fetal bovine serum. However, high viability alone did not ensure intact cryomicroneedle formation, highlighting the need for future multi-objective optimization. These results demonstrate that agent-assisted computational infrastructure can make data-efficient formulation discovery more accessible to labs with minimal data expertise in-house. Project code is available at this https URL.

---


### 119. [Can Large Language Models Reliably Correct Errors in Low-Resource ASR? A Contamination-Aware Case Study on West Frisian](https://arxiv.org/abs/2605.19711)

**<font color=#1a73e8>作者：</font>** Yun Hao, Reihaneh Amooie, Wietse de Vries 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) has improved substantially in recent years, yet performance remains limited for low-resource languages. Large language models (LLMs) have shown promise for improving ASR through generative error correction (GER), but their effectiveness in low-resource settings remains underexplored. In addition, it remains unclear to what extent data contamination influences the reported improvements in LLM-based GER. This study investigates LLM-based GER for low-resource Frisian. In addition to a public corpus, we construct and use a Frisian offline dataset with non-public texts for evaluation to control for potential data contamination. Results show that GER improves ASR performance in most settings, with the best GPT-5.1 results surpassing oracle WERs. Comparable gains on the offline dataset indicate that improvements reflect true correction ability. We further provide a detailed error analysis revealing model correction patterns.

---


### 120. [LLM-Based Financial Sentiment Analysis in Arabic: Evidence from Saudi Markets](https://arxiv.org/abs/2605.19714)

**<font color=#1a73e8>作者：</font>** Mona H. Albaqawi, Eman M. Albalkhi, Joud A. Albaiti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Investor sentiment shapes financial markets, yet modeling sentiment in Arabic financial contexts remains challenging due to linguistic complexity and limited resources. We present an Arabic NLP framework for large-scale financial sentiment analysis tailored to the Saudi market, integrating official financial news and social media to capture institutional and public investor sentiment. The framework constructs a large Arabic financial corpus through a multi-stage pipeline encompassing data collection, cleaning, deduplication, entity linking, and sentiment annotation. Transformer-based NER combined with a curated company lexicon links textual mentions to canonical company identifiers, with sentiment labels assigned using a five-class scheme. The resulting dataset of 84K samples supports company-level sentiment aggregation and analysis of sentiment dynamics relative to stock market behavior on the Saudi Exchange. Experimental results demonstrate reliable and scalable Arabic financial sentiment analysis.

---


### 121. [Physics-in-the-Loop: A Hybrid Agentic Architecture for Validated CAD Engineering Design](https://arxiv.org/abs/2605.19717)

**<font color=#1a73e8>作者：</font>** Elias Berger, Muhammad Usama, Jan Mehlstäubl 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can generate Computer-Aided Design (CAD), yet lack physical comprehension required for reliable engineering design. Instead of attempting to implicitly learn physical laws from data, we propose a Hybrid Agentic-Physical Architecture that embeds validated knowledge-based engineering tools directly into the decision making loop of autonomous AI agents. In this framework, engineering design is formulated as a closed-loop, sequential decision making process guided by explicit physical verification. Based on a load case, dedicated agents iteratively plan, generate, evaluate, and revise engineering designs using knowledge-based tools as a feedback signal. We introduce a benchmark dataset and metrics for assessing functional validity in generative CAD. Our system generates more complex and physically verified designs, with a 4.2 increase in structural complexity and improving compile rate by 3.5% compared to similar agentic methods. The codebase, prompts and dataset will be made publicly available to support reproducibility and future research.

---


### 122. [Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges](https://arxiv.org/abs/2605.19723)

**<font color=#1a73e8>作者：</font>** Husnain Amjad, Raja Khurram Shahzad, Aamir Shahzad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mathematical reasoning is essential for problem-solving in education, science, and industry, serving as a crucial benchmark for evaluating artificial intelligence systems. As Large Language Models (LLMs) improve their reasoning capabilities, understanding how well they perform mathematical reasoning has become increasingly important. This survey synthesizes recent advancements in mathematical reasoning with LLMs through a structured analysis of datasets, architectures, training strategies, and evaluation protocols. Our systematic review encompasses approximately 120 peer-reviewed studies and preprints, examining the evolution of this research area and providing a unified analytical framework to understand current progress and limitations. Our study particularly introduces a unified taxonomy of mathematical datasets, distinguishing between pretraining corpora, supervised fine-tuning resources, and evaluation benchmarks across varying levels of reasoning complexity. A systematic analysis of reasoning architectures and training strategies, including tool integration, verifier-guided reasoning, and parameter-efficient adaptation, is presented to assess their effects on reasoning robustness and generalization. Moreover, a comparative evaluation of existing metrics highlights the gap between final-answer accuracy and process-level reasoning verification. By synthesizing insights across these areas, our analysis identifies recurring failure modes, such as reasoning faithfulness issues, benchmark biases, and generalization limitations, and outlines key research directions toward improving symbolic grounding, evaluation reliability, and the development of more robust and trustworthy LLM-based reasoning systems.

---


### 123. [Efficient Long-Context Modeling in Diffusion Language Models via Block Approximate Sparse Attention](https://arxiv.org/abs/2605.19726)

**<font color=#1a73e8>作者：</font>** Wenhu Zhang, Yiming Wu, Huanyu Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) enable globally coherent, bidirectional, and controllable text generation, offering advantages over traditional autoregressive LLMs, while scaling to ultra-long sequences remains costly. Many existing block-sparse attention methods select blocks by fixed sampling patterns over the high-resolution attention space, such as tail regions or anti-diagonal stripes. Such prior-driven sampling can miss salient tokens and introduce instability under distribution shifts. In this paper, we propose the Block Approximate Sparse Attention framework (BA-Att) with block-wise pre-downsampled operation, which identifies informative regions within a compact downsampled space, avoiding reliance on brittle positional priors. To analyze its theoretical behavior, we define an oracle post-downsample attention map and formalize the approximation error between pre- and post-downsample schemes. Based on this insight, we introduce a lightweight norm-sorting module and a covariance-compensated correction that approximates full covariance using diagonal QK variances, reducing computational complexity. Extensive experiments show that our operator achieves up to 6.95x acceleration over FlashAttention in attention computation, and maintains near full-attention performance at 50% sparsity across language models, multimodal language models, and video generation models, demonstrating strong efficiency and generalization.

---


### 124. [Tango3D: Towards Alignment for Global and Local 2D-3D Correspondence](https://arxiv.org/abs/2605.19727)

**<font color=#1a73e8>作者：</font>** Zebin He, Mingxin Yang, Shuhui Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D foundation models typically align point clouds to frozen vision-language spaces like CLIP, which achieve strong cross-modal retrieval by compressing 3D shape into a global vector. However, this global-only alignment cannot establish fine-grained pixel-to-point correspondence. To solve this, we present Tango3D, a foundation model that unifies dense correspondence and global retrieval. We use a geometry-aware 2D visual backbone and a pretrained 3D VAE to encode images into 2D patches and point clouds into 3D tokens. These are mapped into a single shared space to achieve both local pixel-to-point alignment and global semantic alignment. To stabilize the joint learning of dense and global objectives, we introduce a three-stage progressive training strategy. Experiments show our model successfully achieves object-level pixel-to-point alignment while maintaining competitive global retrieval, a joint capability not offered by existing 3D foundation models. By establishing a fine-grained alignment feature space, Tango3D injects rich semantics into purely geometric 3D tokens, paving the way for a wide range of dense 3D downstream tasks.

---


### 125. [ContextRAG: Extraction-Free Hierarchical Graph Construction for Retrieval-Augmented Generation](https://arxiv.org/abs/2605.19735)

**<font color=#1a73e8>作者：</font>** Roman Prosvirnin, Sergei Kuznetsov, Seungmin Jin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph-structured retrieval-augmented generation (RAG) systems can improve answer quality on multi-hop questions, but many current systems rely on large language models (LLMs) to extract entities, relations, and summaries during indexing. These calls add token and wall-clock costs that grow with corpus size. We present ContextRAG, a graph RAG system whose graph topology is constructed without LLM-based entity or relation extraction. ContextRAG derives a fuzzy concept graph over chunk embeddings using residual-quantization k-means and Formal Concept Analysis with Lukasiewicz residuated logic. Bridge-like and meet-derived context nodes are induced by soft fuzzy join and meet operations, rather than by LLM-written graph edges. On a 130-task UltraDomain subset, ContextRAG builds its index with 30 LLM calls and 22,073 tokens. In contrast, a local HiRAG reproduction stress test required 870 indexing calls and 3.54M tokens on a 20-task subset before failing during graph construction; linear extrapolation to 130 tasks implies over 23M indexing tokens. ContextRAG obtains 33.6% F1 overall and 36.8% F1 on multi-hop tasks. An activation analysis shows that queries retrieving at least one lattice-derived node in the top five achieve +3.9 percentage points F1 over queries that do not; this association is diagnostic rather than causal.

---


### 126. [EngiAI: A Multi-Agent Framework and Benchmark Suite for LLM-Driven Engineering Design](https://arxiv.org/abs/2605.19743)

**<font color=#1a73e8>作者：</font>** Gioele Molinari, Florian Felten, Soheyl Massoudi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly applied to engineering design tasks, yet existing evaluation frameworks do not adequately address multi-agent systems that combine simulation, retrieval, and manufacturing preparation. We introduce a benchmark suite with three evaluation dimensions: (1) a workflow benchmark with seven prompt styles targeting distinct cognitive demands-including direct tool use, semantic disambiguation, conditional branching, and working-memory tasks; (2) a Retrieval-Augmented Generation (RAG) benchmark with gated scoring isolating retrieval contributions to parameter selection; and (3) an High Performance Computing (HPC) benchmark evaluating end-to-end ML training orchestration on a SLURM cluster. Alongside the benchmark we present EngiAI, a Multi-Agent System (MAS) reference implementation built on LangGraph that operationalizes the benchmark by coordinating seven specialized agents through a supervisor architecture, unifying topology optimization, document retrieval, HPC job orchestration, and 3D printer control. Across four LLM backends and two EngiBench problems, proprietary models achieve 96-97% average task completion on Beams2D, while open-source 4B-parameter models reach 55-78%, with clear generational improvement. Conditional branching proves most challenging, with task completion dropping to 20-53% for the conditional style on Photonics2D. RAG gating confirms near-perfect retrieval-augmented scores ($\approx 1.0$) versus near-zero without retrieval, validating the evaluation design. On HPC orchestration, one model completes all pipeline steps in 100% of runs while another drops to 50%, revealing that multi-step instruction following degrades over long-running workflows.

---


### 127. [MSAlign: Aligning Molecule and Mass Spectra Foundation Models for Metabolite Identification](https://arxiv.org/abs/2605.19752)

**<font color=#1a73e8>作者：</font>** Paul Krzakala, Gabriel Melo, Camille Lançon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurately identifying metabolites i.e. small molecules from mass spectrometry data remains a core challenge in metabolomics, with broad applications in drug discovery, environmental analysis, and clinical research. We address the Molecule Retrieval task, which consists in recovering the chemical structure of a metabolite from its MS/MS spectrum given a set of candidate molecules. While the recent release of benchmark datasets such as MassSpecGym and Spectraverse has considerably accelerated the development of novel machine learning approaches, the complexity of data preprocessing pipelines and the lack of unified implementations make methods and results difficult to reproduce and compare. We make three contributions. First, we propose a unified framework encompassing recent approaches based on representation alignment and contrastive learning. Second, we introduce MSAlign, inspired by multimodal alignment in vision-language models, which learns a shared representation space by aligning two frozen foundation models (DreaMS for mass spectra and ChemBERTa for molecules) through lightweight MLP projections trained with a candidate-based contrastive objective. MSAlign is simple to implement, fast to train and consistently outperforms existing approaches across all benchmarks. Third, we investigate a long-standing evaluation problem: data splitting strategies in molecule retrieval implicitly trade off data leakage against domain shift. We formalize this tension by introducing a quantitative measure of distribution shift, and use it to evaluate splitting strategies in existing benchmarks. All datasets, splits, candidate sets, and a unified implementation of MSAlign and baselines are publicly released to support reproducible research.

---


### 128. [GroupAffect-4: A Multimodal Dataset of Four-Person Collaborative Interaction](https://arxiv.org/abs/2605.19765)

**<font color=#1a73e8>作者：</font>** Meisam Jamshidi Seikavandi, Alice Modica, Anna Obara 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing affective-computing, social-signal-processing, and meeting corpora capture important parts of human interaction, but they rarely support analysis of affect in co-located groups as a coupled individual, interpersonal, and group-level process. The required signals (per-participant physiology, eye movement, audio, self-report, task outcomes, and personality) are usually fragmented across separate dataset traditions. We introduce GroupAffect-4, a multimodal corpus of 40 participants in 10 four-person groups, each completing four ecologically varied collaborative tasks spanning information pooling, negotiation, idea generation, and a public-goods game. Each participant is instrumented with a wrist-worn physiology sensor, eye-tracking glasses, and a close-talk microphone; sessions include continuous affect self-reports, post-task questionnaires, task outcomes, and Big-Five personality scores, all time-aligned to a shared clock. The dataset covers over 91% of expected physiology windows and 98% of eye-tracking windows, with strong task validity confirmed by a clear affective manipulation check across the negotiation block. We define fifteen benchmarkable targets spanning three analysis levels -- within-person state, between-person traits, and group dynamics -- and report leave-one-group-out feasibility baselines establishing the dataset's evaluative scope. GroupAffect-4 is released with a BIDS-inspired structure, Croissant metadata, a datasheet, per-session quality reports, and open processing scripts. Code and processing scripts are available at this https URL the dataset is publicly archived at this https URL.

---


### 129. [AR1-ZO: Topology-Aware Rank-1 Zeroth-Order Queries for High-Rank LoRA Fine-Tuning](https://arxiv.org/abs/2605.19767)

**<font color=#1a73e8>作者：</font>** Ziye Chen, Hongbin Lin, Chenyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization enables large-language-model fine-tuning without storing backpropagation activations, while LoRA supplies compact trainable adapters. Combining them creates a rank paradox: increasing LoRA rank improves adapter capacity, but standard two-point ZO either perturbs a rank-dependent number of coordinates or, under atomwise updates, can make the finite-difference signal unobservable. This paper shows that the bottleneck is a measurement-topology problem rather than a need for an external subspace. LoRA already decomposes into matched rank-$1$ atoms, each a complete factor-coordinate block of dimension $d_\text{out}+d_\text{in}$. Querying one atom per step keeps the stored adapter rank $r$ while removing $r$ from the single-query perturbation dimension. The naive atomwise query is still miscalibrated: if it inherits canonical LoRA scaling $\alpha/r$, the active finite-difference signal shrinks as $1/r$ and the active finite-difference signal-to-noise ratio (FD-SNR) as $1/r^2$, producing directional collapse under a fixed residual evaluation-noise floor. AR1-ZO pairs alternating rank-$1$ atom queries with topology-aware scaling $\gamma=\alpha r$, restoring rank-invariant active signal without auxiliary bases, activation hooks, curvature estimates, or extra forward queries. Theory proves atom minimality, rank-independent active query dimension, directional collapse and restoration, and the remaining rank dependence as an amortized coverage cost. Experiments on OPT and Qwen3 models validate the signal mechanism and show that AR1-ZO makes high-rank LoRA effective among matched-budget ZO methods under the standard two-forward-pass query budget.

---


### 130. [Prior Knowledge or Search? A Study of LLM Agents in Hardware-Aware Code Optimization](https://arxiv.org/abs/2605.19782)

**<font color=#1a73e8>作者：</font>** Dmitry Redko, Albert Fazlyev, Konstantin Sozykin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM discovery and optimization systems are increasingly applied across domains, implementing a common propose-evaluate-revise loop. Such optimization or discovery progresses via context conditioning on received feedback from an environment. However, as modern LLM agents are increasingly complex in their structure, it is difficult to evaluate which components contribute the most, and when and how this exploration may fail. We answer these questions through three controlled experiments. Our findings: (1) In pure black-box optimization, LLMs act as greedy optimizers. (2) In zero-shot kernel generation, providing explicit input-size information has no measurable effect, models converge to the same kernel parameters regardless of size or temperature, as though the size instruction were invisible. Moreover, when tasked to perform kernel optimization for uncommon kernel sizes, performance sharply degrades regardless of the language used. (3) In feedback-loop kernel optimization, CUDA improves monotonically under iterative feedback, while TVM IR actively degrades, which demonstrates that kernel optimization degrades when models operate with low-density language. Our results conclude that LLMs in code optimization tasks highly depend on pretrained priors rather than provided feedback or agentic structure.

---


### 131. [Mechanisms of Object Localization in Vision-Language Models](https://arxiv.org/abs/2605.19792)

**<font color=#1a73e8>作者：</font>** Timothy Schaumlöffel, Martina G. Vilas, Gemma Roig  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visually-grounded language models (VLMs) are highly effective in linking visual and textual information, yet they often struggle with basic classification and localization tasks. While classification mechanisms have been studied more extensively, the processes that support object localization remain poorly understood. In this work, we investigate two representative families, LLaVA-1.5 and InternVL-3.5, using a suite of mechanistic interpretability tools, including token ablations, attention knockout, and causal mediation analysis. We find that localization is driven by a containerization mechanism in which object-aligned tokens define the spatial extent of the object, while the semantic arrangement of tokens within those boundaries is largely irrelevant to the predicted box. Only a very small set of attention heads mediates the causal effect for both classification and localization, concentrating in early-mid layers for LLaVA and mid-late layers for InternVL. The two tasks share some early processing but ultimately depend on largely distinct specialized heads. Overall, we provide the first layer- and head-level account of localization in VLMs, revealing narrow computational pathways that can guide future model design and grounding objectives.

---


### 132. [AffectAI-Capture: A Reproducible Multimodal Protocol for Small-Group Meeting Research](https://arxiv.org/abs/2605.19794)

**<font color=#1a73e8>作者：</font>** Meisam Jamshidi Seikavandi, Alice Modica, Anna Obara 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present AffectAI-Capture, a protocol for collecting synchronized multimodal data in four-person meeting-like interactions, combining eye tracking, wearable physiology, close-talk and room audio, multi-view video, event logging, and structured self-report. Sessions use fixed task blocks grounded in established group-interaction paradigms, while acquisition and post-processing are organized around a single authoritative event timeline and standardized outputs. We describe the experimental rationale, synchronization philosophy, data organization, and practical trade-offs. Pilot-level validation of audio quality and video synchronization has been conducted using controlled bench tests; full protocol sessions with participants remain ongoing work. The contribution is a reproducible protocol architecture linking task design, instrumentation, timing provenance, and data packaging for affective, behavioral, and meeting-analytics research.

---


### 133. [Towards Trust Calibration in Socially Interactive Agents: Investigating Gendered Multimodal Behaviors Generation with LLMs](https://arxiv.org/abs/2605.19798)

**<font color=#1a73e8>作者：</font>** Lucie Galland, Chloé Clavel, Magalie Ochs  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Socially Interactive Agents (SIAs) become increasingly integrated into daily life, the ability to calibrate user trust to an agent's actual capabilities would help ensure appropriate usage of these agents. In this paper, we explore the capacity of Large Language Models (LLMs) to generate multimodal behaviors (verbal, vocal, gestural, and facial expression modalities) that reflect varying levels of ability and benevolence, two key dimensions of trustworthiness. We propose a novel method for automatically generating behaviors aligned with specific levels of these traits, a first step towards enabling nuanced and trust-calibrated interactions. By analyzing a large dataset of multimodal transcripts generated by LLMs, we demonstrate that GPT-5.4 is able to produce coherent behavior across different modalities (text, intonation, facial expression, and gesture). Using Random Forest feature importance analysis, we show that the generated behaviors align with theoretical expectations for ability and benevolence. However, we also find that when gender is specified in the prompt, LLMs tend to reproduce societal gender stereotypes, associating male agents' behaviors with high ability and female agents' behaviors with high benevolence. To validate our approach, we conducted a user study on Prolific using a within-subjects design. Participants perceived different levels of ability and benevolence in the generated behaviors align with the intended instructions.

---


### 134. [Synergistic Foundation Models for Semi-Supervised Fetal Cardiac Ultrasound Analysis: SAM-Med2D Boundary Refinement and DINOv3 Semantic Enhancement](https://arxiv.org/abs/2605.19799)

**<font color=#1a73e8>作者：</font>** Tonghao Zhuang, Shanglong Hu, Yongsheng Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a semi-supervised framework for joint segmentation and classification of fetal cardiac ultrasound images. Built upon the EchoCare multi-task backbone, our method integrates SAM-Med2D for boundary refinement and leverages DINOv3 to enhance pseudo-label quality. We introduce view-specific hard masking along with a two-stage optimization strategy: an EMA phase to consolidate segmentation capabilities, followed by a Classification Fine-Tuning phase that freezes segmentation parameters and resets the classification head to recover classification performance without compromising segmentation gains.
Evaluated on the FETUS 2026 leaderboard, our method achieves a Dice Similarity Coefficient at 79.99%, Normalized Surface Distance at 61.62%, and F1-score at 41.20%, validating the effectiveness of our approach for prenatal congenital heart disease screening. Source code is publicly available at: this https URL.

---


### 135. [From Prompts to Pavement Through Time: Temporal Grounding in Agentic Scene-to-Plan Reasoning](https://arxiv.org/abs/2605.19824)

**<font color=#1a73e8>作者：</font>** Ahmed Y. Gado, Omar Y. Goba, Alaa Hassanein 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent attempts to support high-level scene interpretation and planning in Autonomous Vehicles (AVs) using ensembles of Large Language Models (LLMs) and Large Multimodal Models (LMMs) continue to treat time as a secondary property. This lack of temporal grounding leads to inconsistencies in reasoning about continuous actions, undermining both safety and interpretability. This work explores whether temporal conditioning within inter-agent communication can preserve or enhance coherence without introducing degradation in semantic or logical consistency. To investigate this, we introduce three planner architectures with progressively increasing temporal integration and evaluate them on curated subsets of the BDD-X dataset using semantic, syntactic, and logical metrics. Results show that while temporal conditioning reshapes reasoning style, it yields no statistically significant improvements in standard NLP-based correctness metrics. However, qualitative analysis reveals predictive hazard reasoning, stable corrective behavior, and strategic divergence in the Sentinel. These findings clarify the limits of prompt-based temporal grounding and establish the first empirical benchmark for temporal scene-to-plan reasoning.

---


### 136. [FineBench: Benchmarking and Enhancing Vision-Language Models for Fine-grained Human Activity Understanding](https://arxiv.org/abs/2605.19846)

**<font color=#1a73e8>作者：</font>** Gueter Josmy Faure, Min-Hung Chen, Jia-Fong Yeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated remarkable capabilities in general video understanding, yet they often struggle with the fine-grained comprehension crucial for real-world applications requiring nuanced interpretation of human actions and interactions. While some recent human-centric benchmarks evaluate aspects of model behaviour such as fairness/ethics, emotion perception, and broader human-centric metrics, they do not combine long-form videos, very dense QA coverage, and frame-level spatial/temporal grounding at scale. To bridge this gap, we introduce FineBench, a human-centric video question answering (VQA) benchmark specifically designed to assess fine-grained understanding. FineBench comprises 199,420 multiple-choice QA pairs densely annotated across 64 long-form videos (15 minutes each), focusing on detailed person movement, person interaction, and object manipulation, including compositional actions. Our extensive evaluation reveals that while proprietary models like GPT-5 achieve respectable performance, current open-source VLMs significantly underperform, struggling particularly with spatial reasoning in multi-person scenes and distinguishing subtle differences in human movements and interactions. To address these identified weaknesses, we propose FineAgent, a modular framework that enhances VLMs by leveraging a Localizer and a Descriptor. Experiments show that FineAgent consistently improves the performance of various open VLMs on FineBench. FineBench provides a rigorous testbed for future research into fine-grained human-centric video understanding, while FineAgent offers a practical approach to enhance such reasoning in current VLMs.

---


### 137. [Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning](https://arxiv.org/abs/2605.19852)

**<font color=#1a73e8>作者：</font>** Qinghe Ma, Zhen Zhao, Yiming Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-augmented reasoning has emerged as a promising direction for enhancing the reasoning capabilities of multimodal large language models (MLLMs). However, existing studies mainly focus on enabling models to perform tool invocation, while neglecting the necessity of invoking tools. We argue that tool usage is not always beneficial, as redundant or inappropriate invocations largely increase reasoning overhead and even mislead model predictions. To address this issue, we introduce AutoTool, a model that adaptively decides whether to invoke tools according to the characteristics of each query. Within a reinforcement learning framework, we design an explicit dual-mode reasoning strategy with mode-specific reward functions to guide the model toward producing accurate responses. Moreover, to prevent premature bias toward a single reasoning mode, AutoTool jointly explores and balances tool-assisted and text-centric reasoning throughout training, and promotes free exploration in later stages. Extensive experiments demonstrate that AutoTool exhibits outstanding performance and high efficiency, yielding a 21.8\% accuracy gain on V* benchmark compared to the base model, and a 44.9\% improvement in efficiency over existing tool-augmented methods on POPE benchmark. Code is available at this https URL.

---


### 138. [Eyes on VLM: Benchmarking Gaze Following and Social Gaze Prediction in Vision Language Models](https://arxiv.org/abs/2605.19859)

**<font color=#1a73e8>作者：</font>** Hengfei Wang, Anshul Gupta, Pierre Vuillecard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have rapidly evolved into general-purpose multimodal reasoners with strong zero-shot generalization. In this context, VLMs could greatly benefit the analysis of human gaze and attention, a central task in human behavior understanding that requires reasoning about the physical scene as well as the activity, interactions, and social context. However, the extent to which VLMs can reliably understand human gaze and related attentional behaviors remains largely unexplored. In this work, we present EyeVLM, a systematic evaluation framework for gaze understanding in VLMs across two complementary dimensions: tasks and models. To assess gaze understanding capabilities, we focus on two core tasks. The first, gaze following, i.e., predicting the 2D location where a person is looking, has a geometric and visual processing focus, requiring a precise understanding of the human face, attention direction, 3D scene structure, and spatial grounding of attended targets. The second, social gaze prediction, requires social and relational reasoning over multi-person interactions (e.g., mutual gaze and shared attention), and may benefit more from the LLM semantic reasoning capabilities within VLMs. Regarding models, EyeVLM evaluates these tasks in two ways: a zero-shot setting with a diverse set of state-of-the-art open- and closed-source VLMs, exploring different prompting strategies; and a fine-tuning approach based on task-specific QA pairs, studying the impact of model scale and data scale. As benchmarks, we rely on existing gaze understanding datasets and perform a systematic comparison with state-of-the-art purely visual models. Overall, our results show that current VLMs lack precise gaze understanding capabilities. While standard training helps reduce the gap with visual models, significant improvements are still needed.

---


### 139. [Where Does Authorship Signal Emerge in Encoder-Based Language Models?](https://arxiv.org/abs/2605.19908)

**<font color=#1a73e8>作者：</font>** Francis Kulumba, Guillaume Vimont, Laurent Romary 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Authorship attribution models fine-tuned with the same pretrained encoder, data, and loss can differ four-fold in performance depending only on their scoring mechanism. We use mechanistic interpretability tools to explain this gap. Stylistic features such as word length, punctuation density, and function-word frequency are equally available at every layer in every model, including in an off-the-shelf control encoder, hence the gap not coming from representation quality. Instead, causal intervention shows that the scorer determines where the encoder consolidates authorship signal. Mean pooling forces consolidation by early to mid layers, while late interaction defers it to later layers. We further derive this difference from the gradient structure of each scorer, and training dynamics reveal distinct learning trajectories that follow from that difference.

---


### 140. [LLM Agents Make Collective Belief Dynamics Programmable: Challenges and Research Directions](https://arxiv.org/abs/2605.19915)

**<font color=#1a73e8>作者：</font>** Xin He, Junxi Shen, Yuchen Mou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Classical models of opinion dynamics assume human participants with bounded rationality and limited coordination. The rise of LLM-based agents introduces a qualitative shift: agents can now participate in online discussions at scale, maintain consistent persuasion strategies, and coordinate systematically. This paper argues that LLM agents make collective belief dynamics programmable, enabling deliberate steering of population-level beliefs. We term this emerging problem programmable collective belief control. Through controlled multi-agent simulations, we provide proof-of-concept evidence that coordinated AI agents can induce measurable belief shifts that stabilize within a few interaction rounds. We identify four structural properties (indistinguishability, persistence, contextuality, and configurability) that make detection and defense fundamentally difficult. Based on these findings, we outline a research agenda spanning theoretical foundations for adversarial belief dynamics, operational methods for system-level detection and intervention, and simulation infrastructure for scalable experimentation. Our goal is not to present a complete solution, but to articulate why this problem demands urgent attention and to provide a conceptual foundation for future work.

---


### 141. [Breaking Modality Heterogeneity in Low-Bit Quantization for Large Vision-Language Models](https://arxiv.org/abs/2605.19929)

**<font color=#1a73e8>作者：</font>** Yi Zhong, Haotong Qin, Xindong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-bit post-training quantization (PTQ) is a pivotal technique for deploying Vision-Language Models (VLMs) on resource-constrained devices. However, existing PTQ methods often degrade VLMs' accuracy due to the heterogeneous activation distributions of text and vision modalities during quantization. We find that this cross-modal heterogeneity is distributed unevenly across channels: a small subset of channels contains most modality-specific outliers, and these outliers typically reside in different channels for each modality. Motivated by this, we propose SplitQ, a channel-Splitting-driven post-training Quantization framework. At its core, SplitQ introduces a novel Modality-specific Outlier Channel Decoupling (MOCD) module that effectively isolates salient modality-specific outlier channels with minimal overhead. To further address the remaining cross-modal distribution discrepancies, we design an Adaptive Cross-Modal Calibration (ACC) module that employs dual lightweight learnable branches to dynamically mitigate modality-induced quantization errors. Extensive experiments on popular VLMs demonstrate that SplitQ significantly outperforms existing approaches across 6 popular multi-modal datasets under all evaluated quantization settings, including W4A8, W4A4, W3A3, and W3A2. Notably, SplitQ preserves 93.5% of FP16 performance under the challenging W3A3 setting (69.5 vs. 74.3), pushing the efficiency frontier for deploying advanced VLMs. Our code is available at this https URL

---


### 142. [PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents](https://arxiv.org/abs/2605.19932)

**<font color=#1a73e8>作者：</font>** Zhuohan Gu, Qizheng Zhang, Omar Khattab 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate over long and recurring external contexts, like document corpora and code repositories. Across invocations, existing approaches preserve either the agent's trajectory, passive access to raw material, or task-level strategies. None of them preserves what we argue is most needed for repeated same-context workloads: reusable orientation knowledge (e.g., what the context contains, how it is organized, and which entities, constants, and schemas have historically been useful) about the recurring context itself. We introduce PEEK, a system that caches and maintains this orientation knowledge as a context map: a small, constant-sized artifact in the agent's prompt that gives it a persistent peek into the external context. The map is maintained by a programmable cache policy with three modules: a Distiller that extracts transferable knowledge from inference-time signals, a Cartographer that translates it into structured edits, and a priority-based Evictor that enforces a fixed token budget. On long-context reasoning and information aggregation, PEEK improves over strong baselines by 6.3-34.0% while using 93-145 fewer iterations and incurring 1.7-5.8x lower cost than the state-of-the-art prompt-learning framework, ACE. On context learning, PEEK improves solving rate and rubric accuracy by 6.0-14.0% and 7.8-12.1%, respectively, at 1.4x lower cost than ACE. These gains generalize across LMs and agent architectures, including OpenAI Codex, a production-grade coding agent. Together, these results show that a context map helps long-context LLM agents interact with recurring external contexts more accurately and efficiently.

---


### 143. [What Are LLMs Doing to Scientific Communication? Measuring Changes in Writing Practices and Reading Experience](https://arxiv.org/abs/2605.19936)

**<font color=#1a73e8>作者：</font>** Filip Miletić, Neele Falk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Has the style of scientific communication changed due to the growing use of large language models in the writing process? We address this question in the domain of Natural Language Processing by leveraging two data resources we create: a naturalistic corpus of over 37,000 papers from the ACL Anthology (2020-2024); and a synthetic dataset of 3,000 human-written passages and their LLM-generated improvements. We first implement a series of diachronic lexical analyses, showing that both word frequency and usage contexts have changed significantly over time, indicating semantic specialization in some cases and generalization in others. Broadening our perspective, we then model a range of more complex stylistic features and find that LLM-modified texts more frequently contain certain syntactic constructions, more complex and longer words and a lower lexical diversity. Finally, we connect these changes in writing practices to subjective reading experience through a pilot annotation study with 20 domain experts. They overall rate LLM-improved texts as more understandable and exciting, but also express negative qualitative attitudes towards LLMs, highlighting the strongly subjective effect of AI-assisted writing on reading experience.

---


### 144. [Robotics-Inspired Guardrails for Foundation Models in Socially Sensitive Domains](https://arxiv.org/abs/2605.19940)

**<font color=#1a73e8>作者：</font>** Rebecca Ramnauth, Drazen Brscic, Brian Scassellati  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly deployed in socially sensitive domains such as education, mental health, and caregiving, where failures are often cumulative and context-dependent. Existing guardrail approaches -- ranging from training-time alignment to prompting, decoding constraints, and post-hoc moderation -- primarily provide empirical risk reduction rather than enforceable behavioral guarantees, and largely treat safety as a property of individual outputs rather than interaction trajectories. We reframe guardrails as a problem of runtime behavioral control over interaction trajectories, drawing on robotics to introduce formal constructs for constraint enforcement in uncertain, closed-loop systems. We instantiate these ideas in the Grounded Observer framework and apply it across three real-world deployments: small talk, in-home autism therapy, and behavioral de-escalation in schools. Across settings, the framework enables runtime interventions that mitigate drift into undesirable interaction regimes while adapting to diverse social contexts. We discuss extensions to the framework and propose research directions toward stronger guarantees.

---


### 145. [AffectVerse: Emotional World Models for Multimodal Affective Computing](https://arxiv.org/abs/2605.19950)

**<font color=#1a73e8>作者：</font>** Bo Zhao, Fanghua Ye, Yixin Ji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans infer emotions by integrating observed multimodal cues with expectations about how affective states may unfold. Existing multimodal large language models (MLLMs), however, often treat emotion recognition as static fusion over complete audiovisual-text inputs, leaving affective dynamics implicit. We propose AffectVerse, a Qwen2.5-Omni-based model equipped with an Emotion World Module (EWM), an action-free representation-level module for short-horizon latent affective prediction. \rev{EWM contains three modules: 1) Cross-Modal Temporal Imagination predicts future video/audio representations from past tokens with multi-step rollout. 2) MAMA(Modality-Aware Multi-step Attention) Belief Aggregation compresses imagined tokens into modality-aware belief tokens. 3) Belief Injection inserts these belief tokens into the LLM for affective reasoning.} AffectVerse uses future prediction as a past-conditioned self-supervised signal: it does not replace modeling observed history or require unseen signals at inference, but forces the current belief state to encode transition cues that are predictive of subsequent affective change. Across nine benchmarks, AffectVerse improves at least 2.57\% over other models, while controlled ablations show additive gains from temporal imagination, cross-modal rollout, and belief aggregation. These results suggest predictive belief-state modeling is a practical alternative for affective computing.

---


### 146. [Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory](https://arxiv.org/abs/2605.19952)

**<font color=#1a73e8>作者：</font>** Jingwei Sun, Jianing Zhu, Jiangchao Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To enable reliable long-term interaction, LLM agents require a memory system that can faithfully store, efficiently retrieve, and deeply reason over accumulated dialogue history. Most existing methods adopt an extracted fact based paradigm: handcrafted static prompts compress raw dialogues into atomic facts, which are then stored, matched, and injected into downstream reasoning. Nevertheless, such fact-centric designs inevitably discard fine-grained details in original dialogues and fail to support deep reasoning over scattered isolated facts. Moreover, static prompts cannot maintain consistent extraction granularity across diverse dialogue styles. To address these limitations, we propose TriMem, which maintains three coexisting representation granularities, including raw dialogue segments anchored by source identifiers for storage fidelity, extracted atomic facts for efficient memory retrieval, synthesized profiles that aggregate dispersed facts into holistic semantic understanding for deep reasoning. We further adopt TextGrad-based prompt optimization, which iteratively refines extraction and profiling prompts via response quality feedback, achieving lifelong evolution without any parameter updating. Extensive experiments on LoCoMo and PerLTQA across multiple LLM backbones demonstrate that TriMem consistently outperforms strong memory baselines. The code is available at this https URL .

---


### 147. [Towards Fine-Grained Robustness: Attention-Guided Test-Time Prompt Tuning for Vision-Language Models](https://arxiv.org/abs/2605.19956)

**<font color=#1a73e8>作者：</font>** Jia-Wei Hai, Yijun Wang, Xiu-Shen Wei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs), such as CLIP, have achieved significant zero-shot performance on downstream tasks with various fine-tuning adaptation methods. However, recent studies have proven that adversarial attacks can significantly degrade the inference ability of VLMs, posing substantial risks to their practical applications. Prevalent test-time adaptation methods typically rely on multi-view augmentation to implement various fine-tuning strategies, which struggle to identify semantic information and are prone to destroying discriminative regions in fine-grained scenarios. To address these limitations, we propose Attention-Guided Test-Time Prompt Tuning (A-TPT), a semantics-preserving method designed for test-time adaptation. We first refine the gradient attention rollout mechanism to identify semantically meaningful regions surviving under adversarial attacks. Furthermore, we leverage them to guide the spatially varying augmentation intensities and multi-view ensemble for prompt tuning and inference. Extensive experiments demonstrate that A-TPT outperforms existing test-time adaptation methods on both adversarial and clean data. Codes are available at this https URL .

---


### 148. [Detecting Fluent Optimization-Based Adversarial Prompts via Sequential Entropy Changes](https://arxiv.org/abs/2605.19966)

**<font color=#1a73e8>作者：</font>** Mohammed Alshaalan, Miguel R. D. Rodrigues  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization-based adversarial suffixes can jailbreak aligned large language models (LLMs) while remaining fluent, weakening static and windowed perplexity-based detectors. We cast adversarial suffix detection as an online change-point detection problem over the token-level next-token entropy stream. Using the LLM system prompt to estimate a robust baseline, we standardize user-token entropies and apply a one-sided CUSUM statistic. The resulting detector, CPD Online (CPD), is model-agnostic, training-free, runs online, and localizes the adversarial suffix onset. On a benchmark of 1,012 optimization-based suffix attacks (GCG, AutoDAN, AdvPrompter, BEAST, AutoDAN-HGA) and 1,012 perplexity-controlled benign prompts, CPD improves F1 over the strongest windowed-perplexity baseline on all six open-weight chat models (LLaMA-2-7B/13B, Vicuna-7B/13B, Qwen2.5-7B/14B). On LLaMA-2-7B at the canonical CUSUM setting ($k=0$), CPD reaches AUROC $0.88$ and F1 $0.82$. Beyond prompt-level detection, CPD concentrates 79.6% of its triggers inside the adversarial suffix, versus 17-46% for windowed perplexity. Finally, when used as a lightweight gate for LLaMA Guard, CPD reduces guard calls by 17-22% on a high-volume, benign-dominated deployment while preserving guard-level detection quality

---


### 149. [Your Neighbors Know: Leveraging Local Neighborhoods for Backdoor Detection in Decentralized Learning](https://arxiv.org/abs/2605.19969)

**<font color=#1a73e8>作者：</font>** Sayan Biswas, Antoine Boutet, Davide Frey 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized learning (DL) is an emerging machine learning paradigm where nodes collaboratively train models without a central server. However, the collaborative nature of DL makes it vulnerable to backdoor attacks, where a model is taught to behave normally on standard inputs while executing hidden, malicious actions when encountering data with specific triggers. Backdoor attacks in DL remain understudied and existing defenses often overlook DL constraints. We introduce Argus, a novel backdoor detection framework native to DL that requires neither a central coordinator nor prior knowledge of the trigger. In Argus, honest nodes locally analyze received model updates to identify potential backdoor triggers. Nodes then collectively share their triggers with their neighbors and use a structural similarity metric to separate true backdoors from false alarms induced by data heterogeneity. A key insight is that false positive triggers exhibit inconsistencies across participants while true positive ones show consistent patterns. Model updates that fail this collaborative test are rejected, and persistently malicious senders are eventually evicted. We provide the first theoretical convergence guarantees for a DL-specific backdoor detection mechanism, showing that filtering out suspicious model updates with high probability preserves a convergence rate comparable to standard DL. We implement and evaluate Argus on three standard datasets and against three state-of-the-art baselines. Across settings, Argus reduces attack success rates by up to 90 points compared to no defense, while preserving model utility within 5 percentage points of an omniscient oracle. Furthermore, the effectiveness of Argus compared to baselines improves as data heterogeneity increases.

---


### 150. [RECIPE: Procedural Planning via Grounding in Instructional Video](https://arxiv.org/abs/2605.19976)

**<font color=#1a73e8>作者：</font>** Luigi Seminara, Antonino Furnari, Lorenzo Torresani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual planning asks a model to generate the remaining steps of a procedure in natural language given a partial video context and a goal. Progress on this task is bottlenecked by annotation: clean labeled datasets are small, domain-narrow, and encode a single execution trajectory per example, even though many valid orderings exist. Large-scale instructional video corpora offer orders of magnitude more procedural content, but supervised fine-tuning on pseudo-labels from their noisy ASR narrations propagates segmentation and alignment errors and stays single-trajectory. We identify a key asymmetry: extracting clean step labels from noisy video is hard, but verifying whether a generated step sequence is temporally grounded in ASR transcripts is cheap and scales to millions of videos via precomputed text embeddings. We exploit this asymmetry in RECIPE, which uses grounding quality as a reward for GRPO, turning the noisy corpus into a verifier rather than a label source. The framework applies uniformly to two planner input configurations (Socratic, with a textual history extracted by a frozen VLM, and Video, consuming video tokens directly) and to annotated and weakly supervised regimes. We evaluate on 7 procedural benchmarks using a reference-based LLM-as-judge protocol scoring plans across 6 procedural criteria. RECIPE-RL improves over the base checkpoint at all scales (0.5B, 3B, 7B) and every benchmark, with macro-accuracy gains of +7 to +8 points in-domain and up to +16 points zero-shot. It outperforms supervised fine-tuning on both annotated and pseudo-labeled plans (the latter degrades the base) and remains robust without human annotations. Used as the proposal stage of a prior propose-assess-search planner, it improves over the strongest zero-shot baseline at every horizon on Visual Planning for Assistance, and on COIN it preserves the generation diversity that SFT collapses.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-172](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
