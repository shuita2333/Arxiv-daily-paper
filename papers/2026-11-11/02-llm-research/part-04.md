# 🧠 大模型相关研究 | 2026年11月11日

> 本类共 **438** 篇论文：已确认 **405** 篇，待复核 **33** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 151. [Locating and Repairing Domain Shift in VLM Trajectory Planning](https://arxiv.org/abs/2611.10720)

**<font color=#1a73e8>作者：</font>** Zhihong Cui, Hengyu Liu, Michael Alexander Riegler 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are increasingly adopted as end-to-end driving planners, yet they suffer from cross-city domain shift. Existing methods treat this shift as a single quantity addressed by uniform alignment or single-site editing. We challenge this view on two counts: (i) domain shift in VLM trajectory planners is inherently structured across modality and layer, and (ii) a locate-then-repair recipe matched to this structure outperforms every uniform-objective baseline. We analyse domain shift via activation patching and uncover two regularities. (F1) Modality axis. Image and text tokens exhibit distinct shift patterns in each VLM. (F2) Layer axis. The layer-wise shift partition is architecture-dependent and dataset-stable. These findings recast domain shift as a two-dimensional tensor indexed by modality (image vs. text tokens) and layer, motivating a simple principle: locate where shift occurs, and repair only there. We instantiate this principle in MoLaRx (Modality-Layer Repair), a locate-then-repair framework. The Causal Importance Score (CIS) estimates the domain shift as a modality-layer tensor and partitions the layers into functional zones. CIS-Guided Selective Repair (CISR) then applies a matched operator (Maximum Mean Discrepancy (MMD) / low-rank adaptation (LoRA) / freezing) to repair each zone, with the composition adapting automatically to each architecture. We evaluate MoLaRx on three architecturally distinct VLMs (LFM2-VL-1.6B, Qwen2-VL-2B, and PaliGemma2-3B) across two cross-city benchmarks (nuScenes and Argoverse 2). MoLaRx attains the lowest cross-city trajectory-error gap among adaptation methods in all six main-table settings, while using 50-60% fewer trainable parameters and 8.4-10.9 ms lower inference latency. In contrast, uniform MMD-only adaptation collapses in all six settings, highlighting the importance of structure-guided repair.

---


### 152. [Behavioral Evaluation of Large Language Models Under Cognitive Biases in HAZOP Studies](https://arxiv.org/abs/2611.10721)

**<font color=#1a73e8>作者：</font>** Vinicius M. Müller, Vitor A. O. Silva, Sávio S. V. Vianna 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hazard and Operability (HAZOP) studies safeguard industrial processes against catastrophic accidents. Large language models (LLMs) increasingly assist HAZOP drafting, yet evaluations rely on lexical overlap. Because LLMs internalize human heuristics, prompts may trigger biased judgments. Whether frontier LLMs withstand cognitive perturbations in safety-critical workflows remains unknown. Here we show across 420 trials that three frontier LLMs resisted 96.8% of cognitive manipulations, rendering overall susceptibility statistically inconclusive. Contrary to assumed broad fragility, models rejected confirmation and availability cues. However, safety-critical risk downgrades emerged under low anchors and gain frames. Thus, automated hazard analysis requires disciplined human-in-the-loop validation.

---


### 153. [Tiny Evidence Region Localization with Selective Contrastive On-Policy Self-Distillation](https://arxiv.org/abs/2611.10734)

**<font color=#1a73e8>作者：</font>** Yujuan Pang, Wenhao Xu, Yinglei Teng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have made progress in general visual tasks. However, limitations remain in fine-grained visual tasks requiring evidence from minute image regions. Existing methods primarily train models using evidence-related regions while overlooking the influence of extensive background regions, resulting in a limited ability to resist interference from irrelevant regions. We propose selective positive-negative on-policy self-distillation (SPN-OPSD), which considers both evidence and background regions. Supervision from both views improves the model's ability to resist interference from irrelevant regions. Furthermore, selective token-level distillation provides more informative supervision, improving the model's ability to attend to evidence regions in Fine-Grained Visual Tasks. On Qwen3.5-2B, SPN-OPSD improves accuracy on V* Bench, ZoomBench, and MME-RealWorld-Lite from 76.44%, 45.92%, and 57.43% to 84.82%, 54.56%, and 59.56%, respectively. Similar gains are also observed on Qwen3.5-0.8B.

---


### 154. [Evaluating Physically Grounded Procedural Reasoning in VLMs through Real-World Execution: Crochet as a Testbed](https://arxiv.org/abs/2611.10740)

**<font color=#1a73e8>作者：</font>** Maximiliano Wardle  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) can generate procedures that look convincing on paper, but do they work in practice? In this paper, we propose crochet as an ideal testbed for physically grounded procedural reasoning in VLMs. Crochet cannot be reliably simulated or automated: the only way to know what a pattern produces is to make it by hand, yet verification is tangible and cheap, requiring nothing but a hook and a ball of yarn. We introduce FoundationChain, a deceptively simple test of procedural reasoning: given an image of a basic crochet object, can VLMs infer how it was made and generate a pattern that produces the same result? We crochet 40 patterns generated by four VLMs by hand. Even at this scale, physical execution not only reveals failures that automated proxies cannot detect, but also enables a more precise diagnosis of their causes and consequences: while models write fluent, convincing patterns, only four are free of errors, and our analysis exposes deficiencies in visual, geometric and procedural reasoning.

---


### 155. [RoadState: A Domain-Prior-Enhanced Vision-Language System for Industrial-Grade Lane-Level Map Updating](https://arxiv.org/abs/2611.10746)

**<font color=#1a73e8>作者：</font>** Deguo Xia, Zihan Li, Jiaqi Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lane-level map updating requires temporally consistent, physically valid, and auditable road-scene semantics despite occlusions, ambiguous lane markings, temporary obstacles, and viewpoint changes. We present RoadState, a production-deployed vision-language system that transforms sequential road-scene observations into structured lane-level semantics for Baidu Maps' map-updating pipeline. Its core model, RoadState-VLM, formulates road-scene understanding as autoregressive state estimation, predicting the current structured road state from the previous observation and symbolic state together with the current observation. We introduce Geometric Chain-of-Thought (Geo-CoT), which uses a directed acyclic graph of semantic dependencies as a domain prior to improve semantic consistency and reasoning fidelity across interdependent road-state dimensions. Extensive experiments on a real-world dataset show that RoadState-VLM achieves 94.33% mean accuracy across six road-state dimensions, outperforming the strongest fine-tuned VLM baseline. Ablation studies further demonstrate the complementary effectiveness of Geo-CoT and temporal transition context. A cascaded routing pipeline directs routine cases to lightweight models while reserving complex cases for RoadState-VLM. Since its deployment in March 2025, RoadState has supported lane-level map updating across more than 360 cities and reduced overall production costs by 30%. Together with human-in-the-loop auditing, the system maintains robust performance under stress-test conditions. These results demonstrate how domain-prior-enhanced reasoning, structured state interfaces, selective routing, and human quality control can bridge the gap between VLM-based road-scene understanding and large-scale lane-level map updating.

---


### 156. [AERO: Adaptive Ensemble-Disagreement Routing for Oracle Feedback in Sample-Efficient Online RLHF](https://arxiv.org/abs/2611.10750)

**<font color=#1a73e8>作者：</font>** Shrey Singhal, Nannan Huang, Haytham M. Fayek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligning Large Language Models (LLMs) with human preferences via Reinforcement Learning from Human Feedback (RLHF) has driven substantial improvements across a wide range of tasks, but the cost of acquiring preference labels remains the dominant bottleneck in the alignment pipeline. While many recent alignment methods improve sample efficiency through active exploration over candidate responses, they typically query the oracle uniformly across contexts, even for contexts where the learned reward estimates are already reliable enough to provide synthetic labels. We propose Adaptive Ensemble-disagreement Routing for Oracle feedback (AERO), a fully online RLHF algorithm built on a Dyna-style model-based RL architecture, in which an ensemble-based Epistemic Reward Model (ERM) serves both as a reward posterior for exploration and as a learned preference-feedback model for synthetic labeling. AERO uses ensemble vote entropy, a Query-by-Committee disagreement measure, combined with an adaptive thresholding mechanism to decide which contexts require oracle feedback and which can instead receive ERM-based synthetic preference labels, concentrating expensive labels where they are most informative. Empirical results across different model families and scales show that AERO achieves highly competitive alignment performance while reducing the required oracle-query budget compared to online DPO and strong active-exploration baselines.

---


### 157. [Mirage: Provable Defense Against LLM KV Cache Timing Side Channels with Topology-Aware Isolation](https://arxiv.org/abs/2611.10756)

**<font color=#1a73e8>作者：</font>** Xiaobei Yan, Tianwei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed as shared multi-tenant services, relying on advanced optimizations like KV cache and prefix sharing to improve throughput and reduce latency. However, these optimizations introduce a critical vulnerability: attackers can exploit time-to-first-token (TTFT) variations between KV cache hits and misses to infer sensitive prompt tokens via prefix-matching side-channel attacks. Existing defenses indiscriminately restrict cross-tenant cache sharing, which incurs prohibitive performance overhead and negates the fundamental efficiency benefits of the KV cache.
We propose Mirage, a topology-aware emission obfuscation framework that provably bounds timing leakage without sacrificing the performance gains of cache sharing. Instead of stalling the GPU or forcing redundant recomputations, Mirage delays token emission at the gateway so the attacker observes a natural cache miss distribution, while the GPU seamlessly continues serving other requests at full speed. Mirage uses a Privacy Odometer that persistently tracks the topological novelty of prefix fan-out expansions to distinguish aggressive probing from benign traffic. Once a prefix exceeds a safety threshold, Mirage engages a two-phase policy that uses a dynamic estimator to pad the TTFT to a calibrated cache-miss baseline. On a 500-sample public corpus across three models, Mirage suppresses the timing side-channel to near the random-guessing floor, while maintaining a significantly lower TTFT than defense baselines. We further show that Mirage withstands a strong adaptive adversary and the same principle carries over to semantic caching layers.

---


### 158. [BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs](https://arxiv.org/abs/2611.10768)

**<font color=#1a73e8>作者：</font>** Zilin Guo, Tianrui Zhang, Yi Rong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have shown promise as interactive agents, yet precise, programmatic 3D graphics editing remains difficult to train because existing systems largely rely on closed-source model APIs and lack deterministic, state-verifiable execution environments. We present BlenderFORGE, a trainable data-environment-optimization framework for open-weight MLLM agents that edit explicit Blender scenes through Blender Python (bpy) code generation. BlenderFORGE targets four fundamental state-verifiable editing task families: object placement, shape-key editing, lighting adjustment, and material modification. It integrates three components: (1) a scalable perturbation-based data generation pipeline built from curated assets and large-scale 3D scene repositories; (2) an isolated Blender Sandbox for deterministic code execution, structured state export, and closed-loop reward computation; and (3) a two-stage training pipeline that uses offline teacher trajectories for cold-start Supervised Fine-Tuning (SFT) and sandbox-computed rewards for multi-turn tool-agentic Reinforcement Learning (AgentLoop-RL). Experiments across the four task families show that the resulting open-weight Qwen3-VL-8B and Qwen3.5-9B BlenderFORGE agents substantially improve over their base models and achieve competitive performance with several zero-shot proprietary MLLM baselines on selected metrics. Additional cross-benchmark evaluations and camera-reframing experiments provide evidence of transfer beyond the original training setting.

---


### 159. [Look Ahead: Search-Driven Reasoning in Embodied AI](https://arxiv.org/abs/2611.10769)

**<font color=#1a73e8>作者：</font>** Ahmed Zeer, Osama Shbib, Muzaffer Kaan Yuce 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Search allows a robotic policy to evaluate candidate futures before committing to an action. Motivated by test-time planning for vision-language action (VLA) models, we study selective search over action chunks in PushT using a frozen Action Chunking with Transformers (ACT) policy. Beam search generates perturbed alternatives around the policy prediction and scores them through rollouts from cloned simulator states. Across 50 evaluation episodes, beam search raises task success from 0% to 18% and increases average cumulative reward from 39.44 to 103.2. We introduce One Step Ahead (OSA), a gate that simulates the nominal policy chunk and invokes full search only when its predicted coverage drop exceeds a threshold. In the reported ablations, OSA preserves or improves success while reducing runtime by approximately 3x relative to full beam search. Ablations over tree depth, branching factor, beam width, and replanning frequency show that larger search budgets do not consistently improve performance. The results support selective test-time search for action-chunking policies; evaluation on language-conditioned VLAs and physical robots remains future work.

---


### 160. [Proximal Preference Optimization: A Unified Framework for Stable and Reward-Free Alignment](https://arxiv.org/abs/2611.10785)

**<font color=#1a73e8>作者：</font>** Qisai Liu, Zhanhong Jiang, Zahid Hasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a proximal preference optimization framework that unifies the implicit reward formulation of Direct Preference Optimization (DPO) with the trust-region stability of Proximal Policy Optimization (PPO). Our framework yields two complementary algorithms. P$^2$O (Proximal Preference Optimization) introduces a clipped importance ratio directly into the DPO preference margin, producing a reward-model-free algorithm that supports safe dataset reuse, bounded policy divergence, and monotonic preference improvement guarantees. PKTO (Proximal Kahneman-Tversky Optimization) extends P$^2$O by replacing the DPO margin with KTO's prospect-theoretic utility margins, adding a self-regulating adaptive baseline that tightens the effective trust region as the policy drifts, and an asymmetric weighting that handles imbalanced or asymmetric preference datasets. We provide a unified theoretical analysis, including Kullback Leibler (KL) trust-region bounds, a policy-improvement lower bound, and convergence guarantees under multi-epoch proximal updates. Empirically, P$^2$O and PKTO match or exceed DPO and KTO in alignment quality while maintaining better stability under repeated dataset reuse across multiple LLMs on three preference benchmarks. The code base is available here.

---


### 161. [Generating Diverse and Verified Synthetic Clinical Notes with Labels by Construction](https://arxiv.org/abs/2611.10789)

**<font color=#1a73e8>作者：</font>** Matthias Lehmann, Madeleine Werthebach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Under strict privacy regulations in the clinical domain, de-identification is necessary to enable the use of clinical data such as for natural language processing. However, we currently lack sophisticated ways to tell which de-identification models actually are suitable. Specifically, we need benchmarks that are challenging, diverse, and clinically plausible, all while ensuring label correctness. To this end, we present SPARCLING, an LLM-based pipeline to generate synthetic discharge letters with character-exact PHI span annotations. Our pipeline combines structured attribute sampling, template generation, and red teaming to obtain diverse PHI-labeled discharge letters. In our experiments, we demonstrate this superior content diversity over existing public datasets. Further, we show SPARCLING's downstream utility as a benchmark to uncover failure modes of de-identifiers in the German clinical domain. Finally, our experiments show that training on our synthetic data can yield more capable de-identifiers than training on the scarce public data alone. Our code is available at this https URL.

---


### 162. [Zeroth-Order Riemannian Optimization on Fixed-Rank Manifolds for LLM Fine-Tuning](https://arxiv.org/abs/2611.10792)

**<font color=#1a73e8>作者：</font>** Xinjue Wang, Xiuheng Wang, Yejun Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization estimates descent directions from function values alone, which removes the activation storage required by backpropagation and makes it attractive for memory-efficient fine-tuning of large language models (LLMs). Existing low-rank ZO methods either parameterize the additive update through Euclidean factors with a non-unique representation, or restrict each finite-difference direction to be low-rank. In this work, we propose to constrain each additive update block to a fixed-rank matrix manifold while keeping the pretrained weights frozen, so the learned update remains rank-constrained throughout fine-tuning. On this geometry, we build a Riemannian ZO gradient estimator that projects a random matrix onto the tangent space, normalizes it to correct the scale mismatch induced by projection, and further propose Zeroth-order Riemannian Gradient Descent (ZO-RGD) and its smoothed variant, ZO-RGD-S. We show that the ambient finite difference matches its retracted counterpart, the normalized estimator recovers the Riemannian gradient in expectation, and ZO-RGD converges under trajectory-regularity conditions. Experiments on LLM fine-tuning tasks show that the proposed algorithms are competitive with strong forward-only baselines across model families and tasks, with gains in several settings.

---


### 163. [Adapting Large Language Models via Multi-Task Learning for Mental Health Problem, Emotion, and Sentiment Detection](https://arxiv.org/abs/2611.10797)

**<font color=#1a73e8>作者：</font>** Amir Rafiq Bhat, Rahim Dehkharghani, Zeki Erdem  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates sequential multi-task learning using Parameter-Efficient Fine-Tuning (PEFT), LoRA, and 4-bit quantization on Llama 3.1 8B Instruct for mental health problem detection, emotion detection, and sentiment analysis. Using 4,243 English social media posts, it compares two task sequences and demonstrates that task ordering significantly affects knowledge transfer and task interference. The MHP-first sequence achieves the best mental health problem detection (Micro-F1: 0.7624), while the Emotion-first sequence performs better in emotion (F1: 0.6052) and sentiment analysis (F1: 0.9459). A Joint-MTL baseline further highlights the challenges of simultaneous learning, including task interference and generative format collapse. Overall, the findings demonstrate the effectiveness of sequential PEFT for mental health NLP while showing that task order is critical to balancing performance across related tasks. The integration of LoRA and 4-bit quantization also reduces computational and memory requirements, supporting the adaptation of large language models in resource-constrained environments.

---


### 164. [Enhancing Mathematical Reasoning in Turkish Large Language Models with Search-Based Inference and Model Merging](https://arxiv.org/abs/2611.10800)

**<font color=#1a73e8>作者：</font>** Ahmed Zeer, Osama Shbib, Muzaffer Kaan Yuce 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We improve Turkish mathematical reasoning in Large Language Models by combining LoRA fine-tuning, weight-space model merging, and search-based inference. Using Turkish-Llama 8B-DPO with Turkish translations of MetaMath, NuminaMath, and TigerLab, we find data quality beats scale (Mix-30k best among fine-tuned; large MetaMath underperforms). Linear merging delivers the largest gains (GSM8K up to 0.63), while Ties is modest and Breadcrumbs/Slerp degrade. Search with MCTS and Tree of Thoughts improves mean LLM-judge scores for reasoning quality on a 0-100 scale. Limitations include machine translation, limited scale, and search stochasticity.

---


### 165. [Evaluating Jev on Arabic: Comparing Decision Models and LLMs Across Arabic Tasks and Dialects](https://arxiv.org/abs/2611.10802)

**<font color=#1a73e8>作者：</font>** Hossam Elsafty, Tobias Deußer, Lorenz Sparrenberg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How does Jev compare with other systems on Arabic tasks, and how does its performance change between Modern Standard Arabic (MSA) and dialects? We evaluate 67 systems, including 47 decision models and 20 large language models (LLMs), on 43 tasks across 9 task families using a shared zero-shot protocol. The Arabic-focused frozen suite includes English controls in three parallel resources, which we also remove in a separate descriptive comparison. Jev 1.14.0 achieves a mean task-primary metric of 69.24 on a scale multiplied by 100, compared with 68.77 for Jev 1.13.0 and 71.81 for Gemma-4-31B, the highest-scoring system on this aggregate. Removing the recorded English controls, repeated cross-task items or both leaves the full system order unchanged. Relative performance and gains between Jev versions vary across task families. In content-matched comparisons within Jev 1.14.0, pooled dialect-minus-MSA accuracy gaps range from -7.94 to -0.35 percentage points across four datasets; dialect-specific results show larger variation, and SIB-200's source-clustered interval includes zero. Paired contrasts with Jev 1.13.0, Gemma-4-31B and Jais-2-8B show a larger Palestinian banking penalty for Jev 1.14.0 than for either LLM under simultaneous uncertainty; the other gap contrasts remain inconclusive. These descriptive findings show why aggregate scores should be read alongside task-family results, coverage and matched language comparisons. They do not establish a general model ranking for dialect robustness or explain the causes of the observed gaps.

---


### 166. [CompAIssionate Other: Identity Assumptions in LLM Responses to Distress](https://arxiv.org/abs/2611.10808)

**<font color=#1a73e8>作者：</font>** Drishti Goel, Ethan M. Nguyen, Violeta J. Rodriguez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Individuals experiencing suicidal ideation (SI) or psychological distress may disclose their social identities when seeking support from LLMs. Attending to identity-related stressors can be important for providing contextually appropriate and empathetic support. However, disclosing an identity does not necessarily mean that it is a cause of distress. In this work, we audit how LLMs interpret distress through disclosed identities. Using paired counterfactual interventions, we evaluate six LLMs across two SI and distress datasets, 16 identity and control conditions, and two prompting protocols. Our findings suggest that models can transform identity disclosures into explanatory narratives, attributing distress to presumed identity-related adversity. These assumptions frequently appear within otherwise empathetic responses, particularly when marginalized identities are disclosed. We contextualize our findings through the lens of compassionate othering to characterize these patterns as a form of harm in which empathetic responses impose identity-linked assumptions on individual suffering. These responses can misrepresent individuals' experiences by treating their identities as explanations for distress without supporting evidence. Our findings highlight the need to mitigate these harms by grounding interpretations of distress in individuals' disclosures and avoiding unsupported identity-linked assumptions.

---


### 167. [The Devil Wears Markdown: Detecting Malicious Intent Hidden in AI Agent Skill Instructions through Hybrid Static, Dynamic, and Agentic Analysis](https://arxiv.org/abs/2611.10830)

**<font color=#1a73e8>作者：</font>** Thanh M. Truong-Le, Amber Bennoui, Hoang-Ly Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI ecosystems increasingly rely on reusable agent skills that combine executable code, natural-language instructions, configuration artifacts, and external tool integrations. These hybrid artifacts create software supply-chain risks because malicious intent may be distributed across instructions, code, metadata, and runtime behavior, making isolated alerts difficult to interpret.
We evaluate three open-source scanners on a held-out test set of 140 skills comprising 80 malicious and 60 benign samples, including Cisco Skill Scanner with and without its optional LLM analyzer. The default Cisco configuration achieves a recall of 0.91 with 33 false positives among the 60 benign skills, while the LLM-enabled configuration using Qwen3:8B achieves a recall of 0.85 with 40 false positives.
We then present a framework that combines static findings, safety-constrained sandbox evidence, and LLM-based reasoning to assess malicious intent. The framework tracks the origins of findings and relates evidence across analysis layers. In a within-system evidence-source ablation using the same reasoning backend, adding dynamic evidence to skill-content reasoning increases F1 from 0.70 to 0.85. Combining static and dynamic evidence further increases F1 to 0.89, with five false positives among 60 benign skills. Dynamic evidence provides the largest observed improvement.
The Full Pipeline detects 68 of 80 malicious skills, achieving 0.88 accuracy, 0.93 precision, and 0.85 recall. It matches the observed recall of Cisco Skill Scanner with LLM while reducing false positives from 40 to five. This system-level comparison does not isolate model or architecture effects.

---


### 168. [Multimodal Models Can See, But Can They Think? A Study of Turkish Visual Reasoning](https://arxiv.org/abs/2611.10831)

**<font color=#1a73e8>作者：</font>** Berke Bunyamin Sule, Yavuz Selim Aygan, Ahmed Zeer 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models have had massive leaps in recent years. Yet, when tested on high-level cognitive tasks like pattern completion, abstract logic, and relational reasoning, they still fall short. This limitation stems from the models' lack of ability to find out underlying rules and maintain constant intermediate steps, rather than merely deciding on the correct option. To research these shortcomings, this study analyzes visual reasoning performance throughout a multilingual evaluation framework encompassing the BİLSEM, MM-IQ, Visual Puzzles, and PuzzleVQA datasets. We evaluate various data mixing strategies and supervised fine-tuning (SFT) methods. We observed that a correct answer does not always mean the reasoning chain is valid. Because of this, we adopt an LLM-as-a-Judge approach to assess the quality of reasoning beyond final answer accuracy. Our experimental results reveal that baseline models often exhibit more stable reasoning compared to fine-tuned counterparts. Most importantly, we observe that SFT can lead to model collapse, manifesting as infinite text loops or empty outputs. The study concludes that current VLMs still struggle with abstract visual reasoning.

---


### 169. [Simple Test-Time Refinement for Plot-to-Code Generation via Visual-Code Diagnostics](https://arxiv.org/abs/2611.10840)

**<font color=#1a73e8>作者：</font>** Peiming Guo, Jinpeng Huang, Yangbin Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Plot-to-code generation has been greatly advanced by recent multimodal large language models (MLLMs). However, existing studies mainly focus on one-pass generation or iterative sampling guided by verifier-based filtering, which does not align with the typical human programming workflow of generate first, then iteratively error-location and fix. This naturally motivates a test-time refinement paradigm for plot-to-code generation. In this work, we present the first study on plot-to-code generation via iterative test-time refinement. We propose a Visual-Code Diagnostics framework that enables refinement through visual feedback from source code. Specifically, we first categorize generation errors into four coarse-grained types, and then train lightweight discriminators to recognize and localize these errors based on the rendered visual outputs and corresponding code. Unlike traditional compiler- or debugger-based verification, our approach performs iterative refinement guided by one diagnostics system, enabling more effective semantic and visual correction during test time. Extensive experiments demonstrate that our method consistently improves generation quality across diverse generators and significantly outperforms strong test-time scaling baselines.

---


### 170. [Agents of Chaos: A Systematization of Knowledge (SoK) on Malicious Attacks on Agentic AI Systems](https://arxiv.org/abs/2611.10843)

**<font color=#1a73e8>作者：</font>** Thanh M. Truong-Le, Amber Bennoui, Hoang-Ly Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems extend large language models with tools, memory, retrieval, browser or computer-use interfaces, code execution, external services, and multi-agent coordination. Although these capabilities enable agents to act beyond text generation and perform tasks, they also create attack paths through which adversaries can exploit untrusted content, deceptive metadata, poisoned state, compromised skills, mutable dependencies, or malicious code. Such attacks can manipulate planning and tool use, corrupt memory, abuse code-execution environments, and trigger harmful downstream effects.
In this paper, we present a systematic review of malicious attacks targeting agentic AI systems. We screened 186 candidate sources and retained 98. Following independent coding and resolver adjudication, we identified 284 atomic attacks, 452 atomic safeguards, and 660 explicit attack--safeguard relationships. We organize attacks into eight causal-mechanism classes while retaining insertion points, activation conditions, abused capabilities, objectives, impacts, persistence, and evidence as orthogonal dimensions.
Our analysis shows that tool, MCP, and action-layer attacks account for the largest share of atomic attacks, while the prompt-injection and action-hijacking class has the broadest paper coverage. We identify distinct class-specific activation patterns and separation between insertion and later activation. Safeguard coverage remains uneven: only 278 of 660 relationships are directly assessed, and strong coverage is uncommon. These findings support lifecycle-aware threat modeling, agent evaluation, tool governance, and defense-in-depth security for agentic AI systems.

---


### 171. [What Broke & Why: Practical Lessons from Reinforcement Learning Post-Training](https://arxiv.org/abs/2611.10844)

**<font color=#1a73e8>作者：</font>** Luv Verma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become an important way to improve how language models reason, solve problems, and use tools. But getting it to work in practice is not always straightforward. Training can fail because a model receives no useful reward, learns to exploit the reward system, stops exploring, or appears to improve when the evaluation itself is misleading.
In this book, we give a practical introduction to reinforcement learning post-training for language models, focusing on what works, what fails, and why. We begin with the foundations of post-training, explain GRPO and the training loop step by step, and then follow five training programs covering math reasoning, search agents, training stability, mixture-of-experts models, and software engineering tasks. Each program shows the problems encountered, the changes made, and the lessons learned.
The book also examines what reinforcement learning actually changes inside a model. The remaining chapters provide a practical reference for reward design, evaluation, training tool-using agents, debugging common failures, reproducibility, rollout engines, and hardware. Written for researchers and practitioners working with open models, the book aims to help readers understand how to train models, recognize when something goes wrong, and decide what to try next.

---


### 172. [Inference for Reasoning Models: Practical Lessons from Evaluation and Serving](https://arxiv.org/abs/2611.10845)

**<font color=#1a73e8>作者：</font>** Luv Verma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Running a language model involves more than its trained weights. The same model can receive very different benchmark scores, produce different answers, or cost more to serve depending on how it is evaluated and run. In one experiment in this book, changing only the maximum response length moved accuracy on a math benchmark from 0.08% to 93.18%.
This book explains how inference settings shape the results we report and the systems we deploy. We begin with evaluation, including generation limits, answer extraction, scoring methods, and quantization. We then examine why outputs can change across batches, attention backends, and caching, even when sampling is disabled. The next chapters cover serving performance, including batching, memory capacity, latency, throughput, and cost. We also study structured outputs, tool calls, reasoning budgets, and long-context tasks, showing what these controls and benchmarks do and do not establish.
The book concludes with practical guidance for recording inference runs, checking evaluations, estimating capacity, and comparing systems fairly. Written for researchers and engineers working with language models, it aims to make inference results easier to understand, reproduce, and trust.

---


### 173. [MultiTurnRoute: A Platform for Building and Evaluating Multi-Turn LLM Routers](https://arxiv.org/abs/2611.10848)

**<font color=#1a73e8>作者：</font>** Jiaqi Xue, Mengxin Zheng, Heng Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In a multi-turn conversation, the choice of language model at one turn can affect which model should answer the next. The selected model's reply shapes the context for the next query, and its cached prompt prefix can reduce the cost of using that model again. We introduce MultiTurnRoute, a platform for building and evaluating multi-turn LLM routers. A shared interface gives built-in and user-defined routers the current query, dialogue history, and an estimate of each model's reusable prefix length. Our routing algorithm, Chain-of-Route (CoR), uses a learned gate over recent and recurrent dialogue history to predict response quality and estimates cost from each model's reusable prefix. MultiTurnRoute Arena ranks routers on recorded conversations and compares session quality and cost in interactive runs where a simulated user responds to each reply. On a benchmark drawn from WildChat and LMSYS-Chat-1M with per-turn quality annotations for five LLMs, CoR reduces the normalized cost required to match the strongest model's quality by up to 20.3% relative to the strongest routing baseline, while matching or improving peak response quality.

---


### 174. [The Surprising Effectiveness of Deleting Weights in LLM Post-Training](https://arxiv.org/abs/2611.10866)

**<font color=#1a73e8>作者：</font>** Jack Lu, Zhenbang Yang, Mike Lasby 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How little of a pretrained large language model (LLM) has to change for it to acquire new capabilities? We find that zeroing fewer than 0.05% of its weights, with no other modification, matches full fine-tuning (FFT) at scale across three LLM post-training regimes: reinforcement learning with verifiable rewards, supervised fine-tuning, and on-policy distillation. Our method, Deletion Tuning, learns a binary mask over the gate projection of transformer blocks. Two practical advantages follow: the trained mask is hundreds to thousands of times smaller than the corresponding FFT checkpoint, and Deletion Tuning forgets far less, which addresses a central challenge in continual learning. Under reinforcement learning, its prior-task accuracy stays near the base level while FFT, LoRA, and random sparse fine-tuning lose up to 5.4 points. To understand why masking alone suffices, we analyze the geometry of the learned weight changes under reinforcement learning using stable rank, spectrum drift, and principal-weight overlap. Compared with LoRA and random sparse fine-tuning, Deletion Tuning is closest to FFT across the three measures.

---


### 175. [BRAT: Bounded Residual-Aligned Training for Stable Multi-Pass LLM Post-Training](https://arxiv.org/abs/2611.10873)

**<font color=#1a73e8>作者：</font>** Xunlan Zhou, Yuzhe Zhao, Xuhong Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for large language model post-training often reuses each batch of sampled rollouts for several gradient passes to amortize the cost of generation. Under such multi-pass reuse, existing objectives fail in different ways: unclipped updates collapse as the policy drifts away from the sampling policy, adding a negative baseline avoids collapse but reinforces every sampled response, and PPO-style ratio clipping cuts off gradients abruptly. We first ask why reuse is fragile. Measuring how well an update estimated from a small rollout group aligns with the KL-regularized target on held-out rollouts of the same prompts, we find that this alignment drops by nearly an order of magnitude from in-sample to held-out rollouts across three base models, suggesting that repeated passes largely overfit the sampled group. Motivated by this finding, we propose Bounded Residual-Aligned Training (BRAT), motivated by a proximal update toward a bounded reweighting of the sampling policy. BRAT assigns each token a gradient weight that decreases linearly with its probability ratio and vanishes at a trust-region boundary, and normalizes group-centered rewards by their maximum magnitude, keeping advantages zero-mean and bounded without extra hyperparameters. With four reuse passes, BRAT avoids training collapse, limits policy drift, and achieves higher average accuracy with lower seed variance on most benchmarks.

---


### 176. [Keeping LLM Agents on Procedure: Executable Finite-State Control for Long-Horizon Instruction Fidelity](https://arxiv.org/abs/2611.10884)

**<font color=#1a73e8>作者：</font>** Yutao Sun, Haokun Li, Mingshuai Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Much of the automation handed to language-model agents is procedural: each step needs little intelligence, but a long unattended run must follow a skill or SOP stated once at the start. We show that agents drift from such procedures over long runs, and that restating the instructions or resuming a stopped agent only moves the drift to another shortcut. We study an executable finite-state machine (FSM) that keeps the workflow state outside the model's context and enforces it at three points: tool calls, state transitions and the end of the agent's turn. In a pre-registered experiment on 200-account SOP-Bench batches, Claude Haiku 4.5 with the FSM decided on average 139 accounts correctly and by the procedure, against 48 for the strongest baseline (95% CI of the difference [46, 130]), and kept this rate to the end; across three models, the gain tracked how much the plain agent drifted. Because the runtime, not the model, supplies this long-horizon reliability, the FSM can let small models carry procedural work: Haiku 4.5 with it averaged more such decisions than plain Claude Sonnet 4.6 at 38% of the cost. Analyses on SWE-bench Verified, $\tau^2$-bench, and staged and cross-context workflows further suggest that reliable long-horizon automation can come from stronger execution control, not only stronger models.

---


### 177. [Approximate Recall, Approximate Forecasts: Recall as a Diagnostic for LLM Forecasting Errors](https://arxiv.org/abs/2611.10891)

**<font color=#1a73e8>作者：</font>** Prashanth Bhaskara, Shubhaankar Gupta, Seojoon Yeon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) exhibit approximate recall: they retain coarse associations about past events while losing fidelity on specific details. Past research on LLMs has quantified different models' forecasting ability in real-world events using prediction markets, but has not studied how losing said fidelity impacts their forecasting abilities. For example: while an LLM correctly recalls that the answer to: ''Did Anna Sawai win the Best Drama Actress in the 76th Emmy Awards?'' is ''Yes,'' it incorrectly states the event date as September 22 rather than September 15. In this paper, we introduce a novel metric called the Recall Fidelity Score to study how imprecision in internalized knowledge propagates to forecasting capability on future events. On resolved historical markets, we find that higher local recall fidelity around semantically similar past events predicts lower forecasting error on resolved markets, and the same signal predicts smaller distance from open markets prices.

---


### 178. [SCorPion: A Strategic, Controllable and Personified Conversational Companion](https://arxiv.org/abs/2611.10906)

**<font color=#1a73e8>作者：</font>** Luo Ji, Xiyuan Chen, Dan Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fixed prompt-based language models face challenges in open-domain conversations, where versatile topics require different expert advice or demonstrations to maximize their universal performance. Motivated by the dynamic prompt studies in language generation, we extract different chatting strategies from varied forms of text corpus, which steer the language model to different styles based on human principles. We design and deploy a conversational companion called SCorPion, which uses GraphRAG to extract and summarize the knowledge graph globally, yield community-summarized strategies, and produce query-focused optimal strategies. SCorPion has strategic thinking, yields personified and stylized responses, and can be controlled by explicit factors. Code and further results can be found in this https URL.

---


### 179. [Beyond Real or Fake: A Dual-Channel Authenticity and Reasoning Protocol for Photographic Assessment](https://arxiv.org/abs/2611.10908)

**<font color=#1a73e8>作者：</font>** Xiaoxiao Li, Ruinan Jin, Lili Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forensic verification has converged on a binary "real vs. fake" label that confates fully synthetic, tampered, and AI-retouched images despite their very different consequences. We argue that GenAI manipulations decompose along two complementary channels: a camera channel of sensor fingerprints (destroyed by neural processing), and a semantic channel of scene-level coherence (disrupted by content edits). Each manipulation type leaves a distinctive two-channel signature. We instantiate this taxonomy in 2CAP (2-Channel Authenticity Protocol), pairing a contrastively-trained camera encoder with a frozen semantic encoder to serve two applications on a shared backbone: (i) four-class authenticity classification via cross-attention fusion with learnable reliability weights; and (ii) evidence generation, where an authentic image serves as a reference for a query and the two encoders produce per-channel alignment scores together with a patch-level saliency map. These signals are supplied as privileged context to a frozen Vision-Language Model (VLM) through an Observe-Generate-Refine loop, yielding explanations with localization without forensic fine-tuning. On a multi-source benchmark, 2CAP attains the best classification performance, including strong retouching detection where existing methods fail, and improves explanation quality.

---


### 180. [Pole or Vector? Encoders Capture Bangla Compound Verbs, but LLMs Read Them Literally](https://arxiv.org/abs/2611.10909)

**<font color=#1a73e8>作者：</font>** Md. Asaduzzaman Shuvo, Md Mehrab Karim Antor, Md. Adnanul Islam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In Bangla, a main verb is often followed by one of a small set of vector verbs. These verbs lose their own meaning and add a shade of meaning instead, such as completion. For example, likhe phello means that someone finished writing, not that they wrote and threw something. The same two verbs can also describe two separate events, so only the context shows which meaning is meant. This makes compound verbs a hard test of how language models handle multiword expressions. We present BanglaCV-Probe, a benchmark of 17 vector verbs with 1,044 minimal pairs, 204 entailment items and 197 pairs of correct and incorrect combinations, all checked by native speakers. We test 26 models (encoders, LLMs and translation systems) on four skills: telling the two meanings apart internally, understanding what a vector adds, preferring correct combinations and keeping the vector's meaning in translation. Probes on five encoders tell the two meanings apart and still reach up to 93% accuracy when trained on pairs without surface cues. Prompted models rarely use this knowledge. Entailment accuracy stays between 59% and 81%. Several LLMs answer Yes or No to almost every item, and nine of ten models miss that someone who ate up the rice left none. Most instruction-tuned LLMs translate vectors literally in 15-20% of vector sentences and in up to 55% for mora (die). On correct combinations, a small Bangla-only model (88%) matches BLOOM-7B1 (87%) and both beat Qwen2.5-7B (74%). Data and code: this https URL

---


### 181. [Remembering to Reason: Structured Memory for Scene and Workflow Understanding in Robot-Assisted Surgery](https://arxiv.org/abs/2611.10917)

**<font color=#1a73e8>作者：</font>** Zhiran Zhang, Hu Wang, Yichen Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical video understanding is an important foundation for intelligent assistance in robot-assisted surgery. Similar surgical views can reflect different actions or procedural stages. Interpreting these views requires access to earlier observations, yet frame-centric prompting leaves this history unavailable. We introduce MemSurg, a framework that remembers surgical observations before reasoning over them. Its structured memory graph stores timestamped entity categories, locations, motion cues, and interaction summaries. Chronological links preserve recent context, while entity-associated links connect recurring observations across the procedure. Task-adaptive retrieval then supplies evidence-grounded prompts for scene and workflow reasoning, supporting both frozen inference and memory-conditioned supervised fine-tuning. Evaluation on robot-assisted prostatectomy and two complementary surgical benchmarks shows a 10.43-percentage-point gain over SurgRAW with GPT-4o. Memory conditioning adds 6.52 points under matched Qwen3-VL-8B fine-tuning, and an inference-time plug-in adds 7.04 points to EndoChat. These results support structured memory as a reusable source of procedural evidence for surgical video understanding. Our code will be publicly released.

---


### 182. [DeepFinance: Can AI Diligence a $100MM Deal?](https://arxiv.org/abs/2611.10926)

**<font color=#1a73e8>作者：</font>** Drew Hahn, Tyler Shibata, Jackson Grove 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing evaluations of AI models on high-finance work focus on retrieving answers from financial documents and producing numerically correct outputs. Real private equity (PE) and investment banking (IB) work also depends on choosing between conflicting sources, making sound assumptions, and keeping every step auditable. We introduce DeepFinance, an ultra long-horizon benchmark of 21 end-to-end PE and IB tasks that take a human professional an average of 27.1 hours. Each task pairs a request with a data room averaging 19 files and is graded against an average of 84 expert-written rubric criteria covering output, workflow, and judgment. We evaluate 22 model configurations, each in its native agent harness. The best configuration, GPT-6 Astra with max reasoning, satisfies 57.6% of rubric criteria, and the top four configurations are not statistically distinguishable. Frontier models often calculate correctly from the wrong inputs and find decision-relevant evidence without acting on it.

---


### 183. [Semantic Synthesis over Brute-Force Search: LLM-Guided Transformation Design for Efficient Learning](https://arxiv.org/abs/2611.10940)

**<font color=#1a73e8>作者：</font>** Usha Shrestha, Radu Timofte, Dmitry Ignatov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data transformation pipelines shape the training distribution in computer vision, but designing them is a computationally expensive problem. We investigate whether large language models can enable efficient discovery by synthesizing executable transformation programs outside predefined augmentation spaces. We compare nine strategies under a unified training protocol, including standard augmentation policies, brute-force search, direct code generation with two LLMs, and performance-guided generation using LLMs fine-tuned on accuracy-ordered transformation pairs. When the best candidates are retrained for 20 epochs, LLM-generated transformation programs lead on every dataset, reaching 0.8877 accuracy on CIFAR-10, 0.5825 on CIFAR-100, and 0.9588 on SVHN, surpassing brute-force search over 6,000 candidates. The best transform on CIFAR-10 and SVHN comes from a fine-tuned generator using 270 candidates, while the best on CIFAR-100 comes from an off-the-shelf generator using only 10. This needs 22x fewer candidate evaluations in the generation step and 600x fewer for off-the-shelf generations, relative to brute-force search. Beyond transformation discovery, we analyze the reliability of the reduced-budget evaluation commonly used for augmentation search. Correlating one-epoch selection scores with 20-epoch outcomes reveals strong, weak, and absent predictive relationships depending on the dataset and architecture, with correlations ranging from 0.756 to near zero. A positive control indicates that range restriction alone is unlikely to explain the low correlations. Our results indicate that semantic synthesis with code LLMs provides an efficient alternative to search-based transformation discovery and highlight the importance of validating evaluation fidelity when optimizing data transformations.

---


### 184. [Anatomy-Activated Mixture-of-Experts for 3D Medical Vision-Language Pre-training](https://arxiv.org/abs/2611.10960)

**<font color=#1a73e8>作者：</font>** Szymon Płotka, Gizem Mert, Pedro R. A. S. Bassi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Vision-Language Pre-training (VLP) leverages the semantic richness of radiology reports to learn 3D representations, yet current architectures remain fundamentally anatomy-agnostic. While clinical diagnostics rely on organ-specific context, standard encoders apply a uniform, dense parameterization to all volumetric patches, and existing Mixture-of-Experts (MoE) routers gate on isolated local features without explicit access to the organ composition of the scan or crop. We propose Anatomy-Activated Mixture-of-Experts (A$^{2}$MoE), a framework that incorporates anatomical inductive biases within the model's computational path. A$^{2}$MoE introduces two key components: (1) a Histogram Representation Router (HRR) that conditions expert selection on global visual context and a predicted anatomical composition histogram, encouraging anatomy-dependent expert weighting; and (2) an Organ-Query Multi-Scale Projector (OQMSP) that utilizes learnable queries to extract organ-level embeddings for fine-grained alignment without requiring manual annotations at inference. By routing at the patch level rather than the token level, A$^{2}$MoE reduces routing complexity by orders of magnitude while satisfying load balancing by construction. Pre-trained on over 60,000 multi-phase CT scans, A$^{2}$MoE achieves state-of-the-art performance across segmentation, classification, and detection benchmarks. Furthermore, we demonstrate that our anatomically grounded inductive biases support robust generalization to MRI and ultrasound, establishing a scalable foundation for medical representation learning. The code is available at this https URL.

---


### 185. [SWEET: Mitigating Spurious Feature Reliance in LLM Reasoning via Weight Editing](https://arxiv.org/abs/2611.10974)

**<font color=#1a73e8>作者：</font>** Zhizhang Fu, Lucas Zhao, Michalis Korakakis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning in large language models can be disrupted by simple input perturbations (e.g. adding irrelevant distractors), suggesting reliance on spurious correlations. Identifying and suppressing the spurious features involved in long chain-of-thought reasoning remains challenging. We introduce Spurious-feature WEight EdiTing (SWEET), a training-free method that combines counterfactual interventions with mechanistic interpretability to identify and suppress spurious-features. SWEET extracts token- and sequence-level behavioral directions from activation contrasts between original problems and their counterfactual variants - capturing local and global patterns of spurious reasoning. It then localizes the responsible MLP neurons and attention heads and suppresses their contributions along these directions through weight edits. Using only 20 original-counterfactual pairs for direction extraction, SWEET improves accuracy by an average of 11.8 percentage points on perturbed inputs and 2 points on original inputs across five open-weight reasoning models and five reasoning benchmarks. It also reduces the relative gap between original and perturbed accuracies from 17.6% to 2.5%. Analyses identify two recurring forms of spurious reasoning, i.e. over-integrating irrelevant conditions and overthinking, and provide mechanistic evidence that SWEET improves reasoning robustness by suppressing both behavioral directions.

---


### 186. [Think or Remember: The Exchange Rate of Agentic Inference](https://arxiv.org/abs/2611.10982)

**<font color=#1a73e8>作者：</font>** Juan Wisznia, Santiago Luis Groba Alonso, Matías Gómez Taddeo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents built on reasoning models resend their growing transcript at every call. Two transacting parties, not the model, decide what that costs: the client keeps or edits messages; the server decides whether earlier reasoning returns in the prompt and what its cache reuses. We define a cost model whose counts match an instrumented engine exactly; the architecture charges $c$ per token processed and $\beta$ per pair attended. Their ratio $P^*=c/\beta$ is an exchange rate between thinking and remembering: per token, processing dominates below this context length, a thinking regime, and attention above it, a memory regime. A policy change has a mechanical cost, incurred even if the agent writes the same tokens, and a behavioral one: it writes different tokens, changing cost and outcome. Serving alone can flip which policy is cheaper: on recorded Qwen3-8B ScienceWorld runs, dropping earlier reasoning costs 1.74 times keeping it when the server reuses generated states and 0.34 times when it reuses nothing. In live reruns, dropping it cuts correct HotpotQA answers by 9-23 percentage points on four models, at lower point-estimate cost. Comparing context policies means comparing systems: architecture and serving set the cost of the history kept and the work it induces.

---


### 187. [GradReason: LLMs as Meta-Learners that Replace Training Epochs with Training-Data-Free Weight Updates](https://arxiv.org/abs/2611.11005)

**<font color=#1a73e8>作者：</font>** Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard training recipes make a fixed number of passes over the training data, even when an epoch mostly adds mini-batch noise. We study whether a large language model (LLM) that reads the weight and gradient history of a run can replace some of these epochs with updates that compute no gradient and read no training image. In GradReason, an LLM agent is called every ten epochs. In a restricted sandbox, it analyses recent weight snapshots, epoch-mean gradients, and validation metrics, then submits a Python program that computes new weights and a plan marking each of the next ten epochs as data or virtual. A virtual epoch is kept only if it passes a forward-only check on 5,000 held-out validation images. In 120 runs on CIFAR-10 and CIFAR-100 with three architectures, Claude Opus 5.5 used 32.8% fewer data epochs than the 80-epoch recipe at 0.31 percentage points lower test accuracy (95% CI -0.72 to +0.09; 0.94 points on ResNet-18), on the recipe's own frontier of data against accuracy. Unprompted, Opus averaged recent weight snapshots in every run. This choice produced the savings: a fixed rule with the same acceptance check but extrapolations from prior work saved 5.4% of the data epochs, and the same rule with averaging added saved 25.0%. The LLM's contribution is to find a working update within a single run; once found, a fixed rule implements it equally well. An Opus run cost 0.68 USD, but at this scale the agent's latency exceeded the GPU time it saved.

---


### 188. [PIA: Agentic Physics-Informed Runtime Anomaly Detection](https://arxiv.org/abs/2611.11009)

**<font color=#1a73e8>作者：</font>** Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Runtime anomaly detectors for cyber-physical systems are either learned as black boxes from normal data, which miss stealthy manipulations that keep every signal inside its normal range, or derived by hand from physical models, which requires expert effort for every plant. We introduce physicsinformed agents (PIA), in which a large language model agent writes the detector itself as a set of physical residuals, such as pump characteristics, tank mass balances, and controller logic, and refines every candidate against normal operating data through an evaluation workbench before deployment. The result is a compact, human-readable detector that runs in milliseconds and names the component behind each alarm. On the BATADAL water distribution attack benchmark, PIA with Claude Opus 5.5 reaches an F1 of 0.878 on the test attacks against 0.504 for the strongest of six statistical and deep baselines, keeps detecting attacks concealed by replayed and offset sensor readings, and attributes every detected test attack to the attacked component. Ablations show that testing hypotheses against data is decisive: agents that write residuals from the plant description alone lose up to 0.28 F1, whereas agents that see only anonymized signals recover most of the physical structure.

---


### 189. [Lightfoot: Graph Retrieval-Augmented Generation with Exact, Model-Free Document Deletion](https://arxiv.org/abs/2611.11010)

**<font color=#1a73e8>作者：</font>** Uday Allu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-based retrieval-augmented generation (GraphRAG) improves multi-hop question answering, but deployed systems face two costs that research comparisons rarely measure: building the graph, and removing documents from it. We present Lightfoot, a GraphRAG system in which every entity, link, fact and synonym edge is a deterministic function of per-passage extractions carrying chunk-level provenance. Indexing makes one language-model call per passage, retrieval makes none, and deleting a document is a database operation with no model calls. On the full 11,402-passage MuSiQue corpus we verify that, after deleting 10% of the documents, the graph is identical to a fresh index of the surviving documents. We compare Lightfoot with HippoRAG 2, LightRAG and fast-graphrag under identical extraction, answer and embedding models on MuSiQue, 2WikiMultiHopQA and HotpotQA. Lightfoot builds the cheapest index on all three datasets, 26-31% below HippoRAG 2 and 3-6x below LightRAG and fast-graphrag. Against HippoRAG 2 it is significantly better on MuSiQue retrieval (+2.8 points recall@5 and +4.3 recall@10 on a held-out split) and on HotpotQA answers (+7.7 points exact match), and significantly worse on 2WikiMultiHopQA (-3.9 recall@2, -8.4 F1). Deleting the same documents took LightRAG 2,187 model calls and 3.7 hours; fast-graphrag has no deletion path. Code and per-question results: this https URL

---


### 190. [Where Should Models Run? A Collaborative Inference Framework for Embodied Intelligence in 6G](https://arxiv.org/abs/2611.11023)

**<font color=#1a73e8>作者：</font>** Wanlu Sun, Zhenhui Yuan, Xiang Ji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Embodied intelligence systems rely on fast and reliable inference to enable real-time perception, reasoning, and control. Recent advances in large-scale artificial intelligence (AI) models, including Large Language Models (LLMs) and Vision-Language-Action (VLA) models, have significantly enhanced the capabilities of embodied agents in complex environments. However, deploying these models remains challenging due to the limited computational resources and energy budgets of robotic platforms. A fundamental question is where inference should be executed. Collaborative inference, which partitions models across end devices, edge servers, and the cloud, has emerged as a promising solution. Yet determining the optimal partitioning point remains an open problem, as it depends on wireless network conditions, model structure, and privacy requirements. This article reviews the state of the art in collaborative inference for embodied intelligence and proposes an edge-centric framework in which the edge coordinates model partitioning and execution. Through both simulation and real-world experiments over WiFi and 5G networks, we demonstrate that the optimal partitioning strategy varies with network conditions and model structure. We further identify latency-minimizing partition points for ResNet-101, Qwen2.5-VL-7B, and OpenVLA-7B in collaborative inference between NVIDIA Jetson Nano or AGX Xavier devices and an AGX Thor edge server under varying wireless conditions. Finally, we discuss the future directions for collaborative inference in 6G-empowered embodied intelligence systems.

---


### 191. [Phase-Conditioned Reward Shaping for Token-Efficient LLM Reasoning](https://arxiv.org/abs/2611.11024)

**<font color=#1a73e8>作者：</font>** Zhe Chen, Xiaolin Zhou, Xiyang Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extended reasoning can help language models solve complex problems, but long responses often contain both useful computations and redundant checks. Conventional length penalties encourage shorter responses without distinguishing the functions of intermediate steps. We propose Phase-Conditioned Reward Shaping (PCRS), a framework that combines phase identification with training-time reward allocation. We investigate two classification routes: PCRS-H with a hidden-state classifier and PCRS-T with a frozen text classifier. Our main text classifier implementation assigns overlapping reasoning, execution, and revision labels to native chunks, then uses these labels and exact repetition to adjust existing token penalties. We compare the completed configurations on six mathematical and scientific reasoning benchmarks and examine four reward-weight settings with the text classifier. Compared with a baseline using token-level length penalties, the default text classifier configuration reduces mean response length by 3.13%; sampled Pass@1 is approximately 62.07% for both methods, while oracle Pass@16 rises from 86.08% to 87.67%. These results show how phase-informed penalty allocation can reduce output volume and improve multi-attempt coverage without inference-time classification.

---


### 192. [MoTo: Mixture of Tokenizers Towards Fair Multilingual Language Modeling](https://arxiv.org/abs/2611.11027)

**<font color=#1a73e8>作者：</font>** Gül Sena Altıntaş, Colin Raffel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models rely on a single tokenizer that is chosen at training time and fixed thereafter. Most tokenizers are trained on English-dominant corpora, making them under-serve morphologically rich and non-Latin-script languages, where they can produce fragmented representations, longer sequence lengths, and reduced information density during training. We propose Mixture of Tokenizers MoTo, a modular tokenization framework that trains dedicated per-language BPE tokenizers and composes them into a unified superset vocabulary, where tokens shared across languages are deduplicated into a common ID space. Each tokenizer maintains its own normalization policy, pre-tokenization rules, and vocabulary budget. Despite allocating significantly fewer entries to English, MoTo retains English performance while delivering consistent gains across 18 out of 21 typologically diverse languages spanning six scripts, with improvements most pronounced on morphologically complex and non-Latin-script languages that are systematically underserved by English-dominant tokenizer design. Our results suggest that modular subword tokenization is a practical and extensible alternative to monolithic tokenization for multilingual parity.

---


### 193. [Building and Auditing Chemical Datasets with LLMs: A General LLM-as-a-Judge Framework Applied to Homogeneous Catalytic PET Depolymerisation](https://arxiv.org/abs/2611.11030)

**<font color=#1a73e8>作者：</font>** Muhammad bin Javaid, Karim K. Ben Hicham, Enkhnyam Battulga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can rapidly extract structured multivariate experimental data from the chemistry literature, yet verifying thousands of generated records without ground truth remains difficult. We present a general, citation-grounded extraction and verification methodology centered on an independent "LLM-as-a-judge", applied to the literature on homogeneous catalytic poly(ethylene terephthalate) (PET) depolymerisation. In this pipeline, an extractor LLM generates schema-enforced records from research papers with citations to document chunks tagged with universally unique identifiers (UUIDs); an independent LLM judge then reads the full paper alongside each record, flags unsupported fields, and proposes cited corrections. Prompt ablations show that requiring chunk-level citations not only provides provenance down to specific paragraphs and tables but also improves extraction accuracy. Before deploying the judge at scale, we benchmarked it against manual evaluation on extractions from a hand-curated reference set of 295 ionic-liquid-catalysed PET glycolysis experiments. The judge agreed with human evaluation on 85.7% of reviewed records and was significantly more effective than a heuristic string-matching baseline at catching errors across related experiments. Deployed across 3,942 extracted records from 561 papers, the framework accepted 67.5% of them as written. Its proposed corrections concentrated on quantitative fields, where the extractor often conflated related experiments. We release the extracted dataset with the complete LLM judge audit logs, as well as the Chemistry Data Extractor Toolkit, an open-source application implementing this end-to-end pipeline in a code-free, browser-based environment for document parsing, customizable schema and prompt design, model-agnostic extraction and auditing, interactive provenance-highlighted review, and reproducible dataset bundling.

---


### 194. [Room to Reconsider: Reply Length Decides Whether Pushback Makes Language Models Sycophantic or Self-Correcting](https://arxiv.org/abs/2611.11035)

**<font color=#1a73e8>作者：</font>** Ook Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models often abandon a correct answer when a user pushes back without giving a reason, and this behavior is usually studied as sycophancy to be suppressed. The same pushback, however, also leads models to revisit and sometimes repair a wrong answer. We measure both effects on multiple-choice questions from MMLU and ARC-Challenge with four open models from two families (Qwen3 1.7B, 4B and 8B, and OLMo-2 7B), reading the final answer exactly from option logits after a free-form reply. The reply budget changes the verdict. When Qwen3-4B may answer the challenge in at most 96 tokens, pushback leaves accuracy unchanged or slightly lower; with 1,024 tokens, it corrects 43% of its wrong answers and pushback raises accuracy by 5.7 points. Whether pushback helps overall follows a simple break-even rule in the cave and correction rates. Inside the model, caving can be partly predicted before the challenge: hidden states add about 0.04-0.06 AUROC over turn-1 confidence in three of our four probing runs. A probe trained only on self-correction cases predicts caving beyond confidence when replies are truncated, but not when the model can finish its reasoning. Activation steering never reduced caving selectively: where it worked, it suppressed self-correction as well. We conclude that sycophancy evaluations should allow full replies and report self-correction alongside caving.

---


### 195. [GARP: Real-Time Generative Agents on Local Hardware in a Game Engine](https://arxiv.org/abs/2611.11064)

**<font color=#1a73e8>作者：</font>** Piero Molino, Patrick John Chia, Federico Bianchi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative agents are game characters whose plans, conversations, and memories are written on the fly by a large language model (LLM). The original Generative Agents demonstration used cloud inference in a custom simulation. We present GARP, a platform for real-time generative agents inside Godot, and describe the Character Behavior System used in GARP 2. The complete loop runs on local hardware using a 3B-parameter open-weight model and no cloud service. Alongside the original planning, memory, and reflection, GARP gives each agent an emotion system driven by LLM appraisal, four graded personality axes drawn from the Big Five that set simulation parameters as well as prompt text, six needs whose urgency grows over time, and pairwise relationships updated after every conversation. The system narrows 50+ candidate actions to typically 3-8, constrains model responses with JSON schemas, and surfaces important memories in decision prompts. A layered optimization strategy (an adjustable game clock, decisions taken ahead of need, multi-tier caching, prompt compression, and fully asynchronous execution) keeps the game responsive while the model thinks. In a nine-scenario evaluation, 25 of 27 runs passed log-based checks. Both failures occurred in the birthday party scenario, where one guest omitted the event from their daily plan.

---


### 196. [Wording Matters: Understanding How GenAI Policy Rules Shape Teachers' and Students' Workflows and Perceptions](https://arxiv.org/abs/2611.11072)

**<font color=#1a73e8>作者：</font>** Sabiha Mehreen, Xiangzhe Yuan, Rishab Nithyanand 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The growing use of generative AI (GenAI) in higher education has led institutions to develop policies governing its applications. However, we have little knowledge about how teachers and students adapt and adhere to the policies. In this paper, we analyzed GenAI policies from 101 U.S. universities, identifying nine recurring rules for GenAI use, and interviewed 20 students and 20 faculty members about the rules. We find that the wording of the rules can change how students perceive and act on the rules while introducing different challenges that teachers face in enforcing them in practice. For example, rules such as "Passing off AI-generated content as your own constitutes academic dishonesty" and "Students are accountable for any inaccurate, biased, or unethical content" both outline the acceptable use of AI, but the former can make students hide their use of AI out of fear of unwanted scrutiny, whereas the latter can encourage students to take responsibility and ownership of their use of AI and be more transparent. Students described uncertainty about acceptable use, fear of penalties and unfair treatment, and stigma that discouraged acknowledging AI use. Teachers took on approval workload, had to interpret acceptable use, and lacked reliable ways to verify compliance. We summarize these impacts in a policy-impact matrix linking each rule to its effects on teacher and student workflows and perception.

---


### 197. [When Calibration Data Matter in Sub-4-Bit Language Model Quantization](https://arxiv.org/abs/2611.11079)

**<font color=#1a73e8>作者：</font>** Yehong Jiang, Yen-Kuang Chen, Xinmin Tian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit post-training quantization reduces language-model memory but can sharply degrade downstream task accuracy. Calibration usually relies on generic text, but when task-informed data recover accuracy and which quantizers benefit remain poorly understood. We introduce FragCal-DC, which supplements generic text with training documents from task families with low retention of full-precision accuracy in a two-bit scan. We use a two- to four-bit sweep to locate functional regimes and four-seed calibration comparisons to evaluate six data-dependent methods across six dense models (1.7B-8B) and ten tasks. At their lowest tested functional bit widths, iterative SignRound V2 and OmniQuant improve at two bits, whereas single-pass GPTQ and AWQ show small mean responses at three bits. At two bits, SignRound V2 gains 1.83 percentage points in mean ten-task accuracy over generic-text calibration across six models. At 70 billion parameters, GPTQ and SignRound V2 both improve at two bits, with functional generic-calibration baselines. For two-bit SignRound V2, task-level controls show that recovery concentrates on families included in calibration, while incorrect answer designations retain about 90% of the mean accuracy gain. Changes in reconstruction error do not consistently track accuracy gains. These findings support task-informed calibration as a design principle for preserving downstream accuracy in low-bit quantization.

---


### 198. [SoftPAT3D: Physics-Augmented Text-to-3D Scene Generation with Deformables](https://arxiv.org/abs/2611.11087)

**<font color=#1a73e8>作者：</font>** Lei Shu, Alberta Longhini, Leonidas Guibas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SoftPAT3D, a physics-augmented framework for text-to-3D scene generation in which deformable objects, such as cloth, stuffed toys and ropes, are generated as physically valid, simulation-ready bodies and placed in intersection-free contact with the furniture that supports them, with one another and with themselves. Existing physics-augmented pipelines simulate rigid bodies only and cannot accommodate a generated deformable object, which text-to-3D generation returns as a geometrically invalid mesh, sometimes self-intersecting, that has no rest shape, no material model and no admissible initial state. These are the inputs a deformable simulation requires, and we construct each from information already in the pipeline. The rest shape comes from how the object is manufactured rather than from the generated physically inconsistent deformed configuration, and a material library assigns each deformable object its initial elastic parameters, which can then be optimized. The occluded support is regenerated and converted into a watertight collision mesh, each object is released from an optimizable placement above the supporting part that the prompt specifies, and the complete scene is driven to static equilibrium under one unified contact model, with completion verified by geometric checks and a vision-language model. When a scene fails the prompt, a grid search over placements corrects it, and the adjoint of a differentiable simulation of the same contact energy reaches the targets the grid does not, places several bodies jointly and recovers and optimizes material parameters. Multi-body scenes equilibrate in a single simulation, and the pipeline also runs from the text prompt alone. On all sixty-five prompts, SoftPAT3D produces no undesired interpenetration of any kind, whereas every other system does, and its scenes directly support scene editing and robotic manipulation.

---


### 199. [Task presentation and execution paths shape LLM mathematical performance](https://arxiv.org/abs/2611.11102)

**<font color=#1a73e8>作者：</font>** Min Huang, Mingyan Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mathematical performance depends on how a language model receives information, uses generated text and submits an answer. We study these dependencies through paired comparisons that separate submission requirements, draft reuse and candidate availability. On 65 development problems, an instruction permitting continued derivation produced no valid final answers in 390 short-output calls; a single-line submission instruction produced 390 format-valid outputs, including 389 parseable answers. Under the fixed submission protocol, 198 problems with failed initial submissions were answered correctly in 9.09p of cases with the question alone, 33.84p with its draft, 46.46p with candidates, and 59.60p with both. Drafts added 13.13 percentage points with candidates fixed, and candidates added 25.76 points with drafts fixed; both effects were significant after Holm correction and were subadditive on the accuracy scale. Retaining a trailing excerpt outperformed retaining a leading excerpt of similar average length by 10.10 points Holm-adjusted p 0.027. A second completion model showed the same directions of input effects on the fixed materials. In a cohort with parseable initial submissions, candidates added no correct answers when the previous draft was supplied, but added 27 points when it was absent. These results establish a conditional value of generated text: a failed submission can leave useful material, whose contribution depends on what else is supplied and what is retained.

---


### 200. [Tracing MCP Security Vulnerabilities: Constructing and Analyzing an MCP Security Vulnerability Dataset](https://arxiv.org/abs/2611.11104)

**<font color=#1a73e8>作者：</font>** Xu He, Sagar Patel, Shu Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As a core protocol for integrating large language models (LLMs) with external data sources and tools, the Model Context Protocol (MCP) has quickly become a key interface in emerging AI agent systems. As the MCP ecosystem expands, reported vulnerabilities have also increased, creating a growing software-security attack surface. However, MCP vulnerability information remains scattered, noisy, and difficult to study systematically. This paper addresses that gap by constructing a curated MCP vulnerability dataset from CVE disclosures. Starting from 119 MCP-related records retrieved through February 2026, we filter unrelated cases out and obtain a validated snapshot of 24 MCP vulnerabilities. Our filtering methodology explicitly addresses acronym ambiguity and achieves 96.7% inter-rater agreement on a sampled exclusion audit while retaining all known high-severity MCP cases identified in public advisories. Using this initial dataset snapshot, we find that 87.5% of validated vulnerabilities are Critical or High severity, and that injection and path traversal vulnerabilities account for 66.7% of cases. We further identify recurring issues involving insufficient input validation, inadequate access control, and protocol-level security gaps. Through six representative case studies, we illustrate common exploitation patterns and map them to practical defenses. We release the dataset, reproducibility tooling, and a sustainable maintenance workflow as a foundation for future MCP security measurement, benchmarking, and defense research.

---


> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
