# 🧠 大模型相关研究 | 2026年11月09日

> 本类共 **183** 篇论文：已确认 **172** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-183](./part-04.md)

---

### 51. [DelegateEval: Evaluating Platforms for Personal External Service Agents](https://arxiv.org/abs/2611.07508)

**<font color=#1a73e8>作者：</font>** Jichao Li, Jinrong Lu, Manjiang Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents that work for an individual over time may also help that individual serve external clients. We define a personal external service agent as an agent authorized and continuously managed by a specific individual to accept client requests, deliver work, and provide ongoing support using that person's knowledge, experience, professional methods, and service boundaries. Such agents could allow individuals to serve more clients with less direct involvement and generate economic value at scale. We propose DelegateEval, a platform-level evaluation framework for agent systems that may combine large language models, reusable skills, protocols such as MCP, and executable tool environments. It covers eight dimensions: ease of creation, service discovery and matching, delivery quality, expertise inheritance, service continuity, learning and improvement, reliability and governance, and efficiency and value. These dimensions assess whether a platform enables people with different backgrounds to turn their expertise into ongoing services that deliver verifiable work, develop capabilities through experience, and remain economically feasible. We present the framework and an experimental design. Complete datasets, executable environments, a unified scoring protocol, and cross-model results remain to be developed and empirically validated.

---


### 52. [Enhancing Repository-Level Code Completion with Reinforcement Learning in Real-World Scenarios](https://arxiv.org/abs/2611.07510)

**<font color=#1a73e8>作者：</font>** Zhenlong Dai, Zhuoluo Zhao, Xiu Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid development of large language models (LLMs) for code, which closely aligns with the practical needs of real-world software development, has sparked growing attention in repository-level code completion. However, existing Code LLMs present challenges in focusing on suitable contexts from the repository and in deeply reasoning about cross-file dependencies. To address these challenges, we propose a novel reinforcement learning framework for repository-level code completion. To better understand both in-file and cross-file contexts, we employ identifier-driven intent recognition to capture completion intent, thereby improving the model's performance in real-world scenarios. To enhance cross-file reasoning, we propose a reward-driven completion learning to effectively reward in complex repository completion scenarios. To guide LLMs in completing code that aligns with intended functionality and repository context, we introduce a selective-exploration strategy that directs the model to focus on low-confidence, high-reward tokens, promoting the exploration of valuable, underexplored completion patterns. Experimental results show that our approach significantly improves the performance of Code LLMs. The code and the dataset are available at this https URL.

---


### 53. [Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model](https://arxiv.org/abs/2611.07513)

**<font color=#1a73e8>作者：</font>** Chengcheng Wang, Wei He, Wenhao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most vision-language-action (VLA) policies decouple manipulation from cognition by bolting an external action mechanism onto a vision-language model (VLM)--either quantizing actions into discrete tokens whose errors bear no stable correspondence to physical displacements, or delegating continuous trajectory generation to a separate action expert whose gradients compete with or are blocked from updating the VLM backbone. We argue that manipulation and cognition should instead be embodied in the same model, shifting from a decoupled VLA to an Embodied Vision-Language Model (eVLM). We introduce Concertina, an eVLM that places continuous trajectory representation, blockwise generation, and physical-coordinate supervision directly on the computation and parameter path of a shared diffusion VLM backbone. Each control timestep is encoded as one continuous latent action token in the backbone hidden space, and the shared Transformer reconstructs temporally ordered action blocks via the same corrupt-and-reconstruct operator used for multimodal pretraining. Active action projections account for only 0.21% of parameters in the 4.46B model with zero separate action-generator layers, compared with 16.5%-35.1% dedicated action-expert capacity in representative continuous VLAs. Using our proposed Action Interface Audit, we confirm that cross-time trajectory coupling emerges in the middle and late layers of the shared backbone rather than at the action interfaces. On standard benchmarks, Concertina achieves 98.15% average success on regular LIBERO, 85.9% on the 10,030-task LIBERO-Plus benchmark, and 4.142 average completed chain length on CALVIN ABC-D.
Code: this https URL Hugging Face: this https URL

---


### 54. [Action-Conditioned VLM Monitoring for Autonomous Vehicle Semantic Anomalies](https://arxiv.org/abs/2611.07540)

**<font color=#1a73e8>作者：</font>** Daniel Adejumo, Omkar Ankalkope, Kunal Runwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study action-conditioned monitoring of autonomous-vehicle behavior in semantically unusual driving scenes. The target is whether the executed ego action is appropriate for the scene: the same scene can admit both normal and anomalous behavior, so visual unusualness alone does not determine the monitoring label. A Vision-Language Model (VLM) first predicts the scene-required action from an outcome-hidden video window; the monitor then compares that expectation with the realized ego-motion trajectory under an explicit compatibility rule. To study this monitoring task, we contribute a six-field taxonomy of 112 paired scenarios spanning both failure polarities (42 derived from documented incidents), a generated video corpus with estimated trajectories, and an exploratory two-stage monitor on that corpus. On 235 clips from 15 scenario families, the two-stage protocol with a fixed T-2.5 s window obtains 83.0% accuracy and anomaly recall 0.773, versus 74.5% and 0.536 for a single-stage video-only baseline; specificity is 0.880 versus 0.928.

---


### 55. [CST-Bench: Benchmarking Counterfactual Spatial Transition Reasoning with Causal Transition On-Policy Self-Distillation](https://arxiv.org/abs/2611.07541)

**<font color=#1a73e8>作者：</font>** Ying Li, Yongle Cheng, Jing Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning is a fundamental capability of multimodal large language models (MLLMs), yet existing benchmarks mainly focus on static scene understanding. When objects are moved or swapped, models must infer not only spatial relations but also how interventions change the scene state. To address this problem, we introduce CST-Bench, a benchmark for counterfactual spatial reasoning. CST-Bench contains 7,082 examples covering 6 intervention types and 12 transformation operators, with dense causal annotations including intervention sources, affected relations, expected effects, invariant relations, and metric changes. We benchmark general-purpose MLLMs on CST-Bench and further compare post-training strategies on CST-Bench and standard spatial benchmarks. Results show that methods effective for ordinary spatial reasoning can still fail under counterfactual interventions. We further formulate counterfactual spatial reasoning as causal state-transition modeling and propose CT-OPSD, which uses CST-Bench annotations to guide a teacher model in learning counterfactual state transitions and causal reasoning chains. These chains are then distilled into a student model that reasons only from real observations. Overall, experiment results establish CST-Bench as a challenging benchmark and reusable supervision resource for counterfactual spatial reasoning. CT-OPSD further provides an initial demonstration of how its annotations can support model improvement.

---


### 56. [FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving](https://arxiv.org/abs/2611.07542)

**<font color=#1a73e8>作者：</font>** Xuan Wang, Zhuanhao Wu, Tingzhu Fang 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In large language model (LLM) serving systems, the key-value (KV) cache grows linearly with sequence length and concurrency, so long-context inference easily hits the high-bandwidth memory (HBM) capacity wall and results in low concurrency. Offloading the KV cache to host dynamic random-access memory (DRAM) frees HBM space and raises concurrency, but the additional cache management and host-to-device (H2D) load overhead inflates inference latency, higher concurrency fails to translate into effective throughput. We present FlashOffloading, a host-DRAM-centric inference architecture that fully offloads the KV cache in both the prefill and decode phases. FlashOffloading builds rolling HBM cache for prefill, a hot cache for decode, a reverse sparse index with zero extra miss-lookup overhead, and a compute--load overlapped kernel, optimizing KV offloading latency across the entire pipeline and delivering throughput gains under a time-per-output-token (TPOT) service-level objective (SLO). In experiments deploying GLM-5.2 with multi-token prediction (MTP3) speculative decoding on an Ascend910C prefill--decode (PD)-disaggregated platform, FlashOffloading improves prefill throughput by up to 1.38\(\times\) and decode throughput by up to 1.91\(\times\) under a 30 ms TPOT constraint. FlashOffloading is integrated into an open-source serving framework: this https URL.

---


### 57. [OptIMerge: Optimization-Based Merging of Diffusion Models](https://arxiv.org/abs/2611.07543)

**<font color=#1a73e8>作者：</font>** Viraj Shah, Ashwini Pokle, Peyman Milanfar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The arithmetic merging of weights from multiple task-specific models fine-tuned from a shared base model, commonly known as model souping, has emerged as a popular strategy for multi-task learning without the computational overhead of joint retraining. However, naive scalar weight averaging frequently leads to severe performance degradation when the constituent models learn structurally divergent feature representations, leading to destructive parameter interference. We study this problem in a largely unexplored setting: merging image-to-image (I2I) diffusion models fine-tuned for dense, pixel-accurate tasks such as image restoration. Unlike the large language models (LLMs) and text-to-image (T2I) diffusion models for which most merging methods were developed, I2I experts encode conflicting spatial priors (e.g., anisotropic motion-blur vs. isotropic defocus-blur) in their convolutional filters, where both naive soup and LLM-style element-wise merging introduce visible artifacts. We introduce OptIMerge, a gradient-based optimization framework: instead of relying on heuristic scalars, OptIMerge learns highly expressive, yet parameter-efficient merger coefficients by minimizing a multi-task diffusion loss over a small set of 100-500 images. OptIMerge parameterizes the merge with architecture-aware transformations: for attention layers, a structured low-rank feature alignment with explicit channel biases; for convolutional layers, per-kernel merger coefficients, and a low-rank Cayley transform that aligns channels by orthogonal rotation without distorting the filters. By keeping the experts frozen and optimizing only these lightweight merger parameters (equivalent to <0.4% of the network footprint), OptIMerge achieves simultaneous multi-task capabilities that rival computationally expensive joint training and decisively outperform zero-shot model soups.

---


### 58. [The Memory Trap: Language Agents Overgeneralize from Benign Interactions](https://arxiv.org/abs/2611.07554)

**<font color=#1a73e8>作者：</font>** Kaiqu Liang, Jaime Fernández Fisac, Thomas L. Griffiths 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language agents increasingly use persistent memory to record user preferences and procedures across sessions. We show that memory from benign interactions can cause unsafe or unreliable behavior on later tasks. We call this failure the memory trap. To study this issue, we compare behavior in sessions with and without memory across six frontier models (including Claude Sonnet, Opus, and Fable models and GPT-5.6). We evaluate these models in a range of settings. First, in autonomy experiments, we find that requests to skip confirmation during low-stakes coding chores lead agents to skip confirmation and verification on simulated high-stakes tasks in both coding and everyday life. We next study memories formed when users seek emotional support, or describe harm from uncritical feedback, and find these memories bias later judgments of mathematical work, arguments, and poems toward sycophancy or over-critique (respectively). Memory notes written during legitimate stale-test repairs lead agents to weaken correct tests that catch broken safeguards; these memories also increase cheating on ImpossibleBench, with larger increases for stronger Sonnet and Opus models. We show that memory traps can arise both from overgeneralizations in memory writing, and when acting on memory. These findings demonstrate that even benign interactions can lead to serious risks from memory systems, and thus motivate the need for new research into ensuring that agents preserve the scope of their memories.

---


### 59. [SKIM: Pruning Large Language Model Agents via Selective Knowledge Informed Masking](https://arxiv.org/abs/2611.07558)

**<font color=#1a73e8>作者：</font>** Moonseok Choi, Jongwon Jeong, Minki Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly deployed under structured generation, where grammar constraints enforce output format at inference time. Whereas existing compression methods target unconstrained generation, we first identify a fundamental mismatch: under structured generation, grammar constraints reduce the model's output distribution to valid tokens, and the logits matter most at the small set of positions that decide the agent's action. Motivated by this finding, we propose SKIM (Selective Knowledge-Informed Masking), the first pruning and distillation framework for LLM agents under structured generation, with both stages guided by token role. SKIM partitions token positions into context, decision, and format categories, and this partition drives two complementary axes: (1) category-aware pruning saliency scores that preserve parameters most relevant for decision positions; and (2) an on-policy distillation objective that aligns student and teacher on valid tokens, paired with category-aware feature matching. We evaluate SKIM on tool-calling benchmarks and within multi-step agent loops, across multiple model scales and sparsity levels. SKIM consistently improves accuracy over baselines, with its superiority becoming most striking in high-sparsity regimes where conventional methods struggle, demonstrating the potential of category-aware compression for deployment-time grammar-constrained agents.

---


### 60. [Provable Zeroth-Order Safe Exploration for Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2611.07561)

**<font color=#1a73e8>作者：</font>** Weiqin Chen, Xinmeng Huang, Dongsheng Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe reinforcement learning from human feedback (Safe-RLHF) seeks to improve helpfulness while satisfying harmlessness constraints. Existing primal-dual approaches can converge to feasible policies but do not prevent constraint violations during training. We study a stronger requirement, safe exploration for RLHF, under which every policy executed during training, including auxiliary exploration policies, remains feasible. We propose Zeroth-Order Log-Barrier Policy Gradient (ZO-LBPG), a reward-model-free method that optimizes a log-barrier objective using zeroth-order estimates derived directly from human preferences. To ensure safety under noisy feedback, we combine conservative constraint margin estimates with coupled rollouts and an adaptive step size that prevents updates from crossing constraint boundaries. We prove that, with high probability, all iterates and exploration policies remain strictly feasible, and that ZO-LBPG globally converges to an approximately optimal constrained policy. We establish a sample complexity of $\widetilde{\mathcal O}(\varepsilon^{-6}+d^3\varepsilon^{-5})$ trajectories and $\widetilde{\mathcal O}(\varepsilon^{-8}+d^5\varepsilon^{-7})$ human queries. Experiments on a synthetic CMDP and a language-model alignment task corroborate the training-time safety guarantees.

---


### 61. [ACSeL: Adaptive Configuration Search for Hardware-Constrained LLM Inference](https://arxiv.org/abs/2611.07570)

**<font color=#1a73e8>作者：</font>** Bokun Wang, Hung-Yueh Chiang, Diana Marculescu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Serving large language models (LLMs) under tight memory and latency service-level objectives (SLOs), including on edge devices, requires jointly selecting the model size, batch size, quantization algorithm, and mixed-precision quantization recipes. Exhaustive search over this combinatorially large space is infeasible. Unlike data-center serving, which often prioritizes throughput or generation speed, resource-constrained deployments typically set memory and latency budgets as constraints and then seek the configuration with the highest generation quality among feasible ones. To this end, we propose ACSeL, a framework that identifies configurations predicted to satisfy deployment constraints while achieving high predicted generation quality. To enable efficient quality estimation, we use Relative Model Quality Degradation (RMQD), a proxy based on the divergence between the candidate and reference models' next-token distributions over a small calibration corpus. Across the evaluated model sizes and precisions, RMQD is inexpensive to evaluate and strongly correlated with downstream benchmark performance. ACSeL combines (i) a lightweight quality surrogate that predicts RMQD directly from a configuration; (ii) Few-shot Median Calibration (FMC), which calibrates operator-profile-based latency estimates using a small number of end-to-end profiles; and (iii) a structured search algorithm BandPareto for exploring layerwise mixed-precision configurations. Experiments on an NVIDIA RTX A6000 workstation and an NVIDIA Jetson Thor edge platform show that FMC substantially improves deployment feasibility, while BandPareto + FMC achieves the highest feasibility and the lowest RMQD gaps to the best measured configurations in the evaluation set.

---


### 62. [Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment](https://arxiv.org/abs/2611.07586)

**<font color=#1a73e8>作者：</font>** Yao Huang, Yifan Wang, Yitong Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM agents advance rapidly in autonomy, the risk of hidden objectives that bypass safety constraints becomes increasingly plausible. Chain-of-thought (CoT) monitoring offers a key control mechanism by reading the agent's reasoning and flagging misalignment before it materializes into action, yet its reliability depends on the realism of the red-team it is stress-tested against. Existing red-teaming efforts rely on shared templates, such as casting a side task as a prerequisite, which treat the side objective as an exogenous insertion and leave task-specific, contextually grounded evasions underexplored. We therefore ask: How robust is CoT monitoring against agents that strategically conceal misalignment? To answer this, we introduce TraceMRT, an automated Trace-level Monitor Red-Teaming framework that reframes the side task as a coherent sub-goal of the primary task and searches trace-shaping strategies whose induced trajectories complete the misaligned objective while reading as natural execution. Through black-box attacks on state-of-the-art monitors such as GPT-5.2 and Claude-4.5, we reveal substantial vulnerabilities even in top models. To counter these vulnerabilities, we propose a Bayesian Trajectory Monitoring framework, integrating global context and local segment evidence to detect covert misalignment. Empirically, our method significantly consolidates monitor robustness with 0.91 AUC and 0.74 TPR@FPR=0.05.

---


### 63. [TACT-KV: Tri-Axis Cosine Transform for Compressing Volumetric KV Caches in Medical VLMs](https://arxiv.org/abs/2611.07593)

**<font color=#1a73e8>作者：</font>** Chongyu Qu, Ritchie Zhao, Yufan He 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) applied to 3D medical scans face a structural memory wall. A single CT or MRI volume produces tens of thousands of vision tokens, and the resulting key-value (KV) cache scales linearly with both batch and context. Existing KV compression methods operate on the cache's feature or token statistics, or apply 1D and 2D transforms, leaving the three-axis spatial structure in the cache unexploited. We propose TACT-KV (Tri-Axis Cosine Transform), a calibration-free KV compression method that exploits strong spatial correlations in visual KV states along all three anatomical axes of 3D scans. This correlation concentrates the KV cache energy under a frequency-domain transform. TACT-KV applies a separable 3D discrete cosine transform to the KV cache, allocates a per-layer bit budget across frequency bins via reverse water-filling (more bits to high-energy components), and quantizes each bin with a fixed scalar codebook. We derive a close-form relation: the distortion reduction from adaptive bit allocation is dominated by the spectral concentration of the transformed cache. Across six medical VLMs and two 3D CT benchmarks, TACT-KV achieves the lowest 1-bit prediction-flip rate on eleven of twelve model and dataset pairs in our main comparison. The same advantage reproduces on four general-purpose VLMs evaluated on video tasks, indicating that the benefit of exploiting three-axis structure generalizes beyond medical imaging. At equal high-bandwidth memory (HBM), TACT-KV scales the decoding batch size on a single GPU by up to $8\times$.

---


### 64. [Align Before Aggregation: Basis-Consistent Federated LoRA under Heterogeneous Ranks](https://arxiv.org/abs/2611.07598)

**<font color=#1a73e8>作者：</font>** Pengpeng Qiao, Yang Cao, Lingling Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning of large language models (LLMs) under heterogeneous client capacities is increasingly important, and low-rank adaptation (LoRA) with heterogeneous ranks makes it practical. Existing server-side aggregators compose local matrix updates $\Delta W_i$ from client-specific LoRA factors $(A_i,B_i)$ before aggregating them. Although these matrix updates lie in the same weight space $\mathbb{R}^{m\times n}$ and can be averaged directly, the LoRA factors that generate them may expressed client-specific local basis. In the typical compose--aggregate--factorize--dispatch loop, this basis inconsistency can make the rank-$r_i$ reference prefix dispatched to lower-rank clients unstable after server-side refactorization. In this work, we propose \textbf{FedAbA}, a basis-consistent federated LoRA aggregation framework for heterogeneous ranks. FedAbA first extracts each client's local basis, aligns it to the corresponding prefix of the global reference basis, and constructs a basis-consistent reconstruction of each local matrix update before aggregation. It then aggregates these reconstructions with weights that combine client data size and consistency score, followed by exact coefficient-space SVD refactorization and gauge fixing before rank-prefix dispatch. Our theoretical analysis clarifies the role of basis consistency and supports the proposed consistency-aware aggregation mechanism. Extensive experiments show that FedAbA outperforms representative federated LoRA baselines, with the largest gains under the strongest rank heterogeneity.

---


### 65. [Binding Paraphrased Instructions to Encountered Objects in sLLM Agents under Partial Observability](https://arxiv.org/abs/2611.07599)

**<font color=#1a73e8>作者：</font>** Chanyoung Kim, Harim Song, Byoungchan Ko 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable deployment of LLM agents requires grounding diverse user expressions in their environments. Although RL-finetuned smaller large language model (sLLM) agents rival larger prompted LLMs on embodied tasks, their robustness to instruction paraphrases remains unclear. We introduce ALFWorld-Para to evaluate this robustness under controlled paraphrases, revealing 21-52% declines in success rates (SRs), predominantly driven by object synonyms. Despite retaining knowledge of synonym referents, agents often fail to take the corresponding objects even after observing them, exposing a gap between referential knowledge and object binding. Partial observability further complicates binding, as referents may remain unseen or have already been encountered under different labels. To address this challenge, we propose BINDIntent, a training-free framework that probabilistically binds referring expressions to observed labels using semantic proximity and estimated persistence against unseen candidates. Without additional training or LLM calls, BINDIntent improves synonym-paraphrase success of RL-finetuned sLLMs by 17.5-49.1 percentage points (pp) with only 0.4 ms of CPU overhead per step. It also raises GiGPO-7B's overall SR from 61.8% to 77.4%, surpassing a prompted 24B LLM. Code and benchmark are available at this https URL.

---


### 66. [The Gating Mechanism of KV Cache Eviction](https://arxiv.org/abs/2611.07605)

**<font color=#1a73e8>作者：</font>** Hao Gu, Xintong Yang, Zhiwei Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> KV cache eviction must decide which entries carry information that the rest of the cache can no longer supply. A natural way to estimate this is a learnable gate: give each cached entry a gate on its attention weight and train the gate on the model's own objective. The gate belongs inside the normalizing softmax, where suppressing one entry hands its mass to the others rather than discarding it. That same normalizer absorbs any per-query constant, so a constant gate cancels and reproduces the frozen model exactly. Trained on the language-modeling loss the gate stays near a constant score while its loss falls throughout: optimization succeeds, but a frozen backbone was fit for dense attention, so its loss prefers the no-op, and a near-constant score ranks nothing. The no-op is not a floor the gate improves from but what its objective asks for. A second obstacle survives once the gate moves, since the same gradient charges the gate for errors the frozen model already makes, which no reweighting of positions separates out. Much of the machinery in learnable eviction, from sparsity penalties to relaxations of the discrete decision, works around the first obstacle rather than removing it; both are removed by putting dense attention beyond the gate's reach and making the dense model's predictions its target. Under these two conditions capacity is never the missing ingredient: neither a larger scorer, nor explicit access to the past, nor a trainable backbone helps. The same holds for what eviction unavoidably discards, which is recovered by parameter-free centroids read inside the same softmax far better than by any memory read outside it, since the mass they must return is a share of that normalizer and available nowhere else. At 75\% KV cache compression, this gate reaches 90.14 on RULER at 8K and 46.03 on LongBench with Qwen3-8B, 3.72 and 1.36 points below full-cache inference.

---


### 67. [Embedding-Space Fingerprinting of LoRA Fine-Tunes: Recovering the Training-Data Domain from the Model Artifact Alone](https://arxiv.org/abs/2611.07610)

**<font color=#1a73e8>作者：</font>** Shivesh Rane  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a base language model is fine-tuned with Low-Rank Adaptation (LoRA), how much of the training data domain leaks into the resulting artifact? This paper studies whether a simple classifier can recover the domain of a fine-tune given only the model artifact (weight deltas, internal activations on a fixed probe set, or generated text) without ever observing the training data. Using one base model (Qwen3.5-0.8B), 36 LoRA fine-tunes are produced over 18 public datasets in five domains (medical, code, mathematics, non-English text, narrative prose), and three feature families are extracted at decreasing levels of access: white-box weights, gray-box activations, and black-box outputs. A leave-one-dataset-out (LODO) protocol, frozen before any result was seen, tests whether the domain of a fine-tune trained on a previously unseen dataset can be identified. The domain is recoverable well above chance (20%) from gray-box activations (61%) and black-box outputs (64%); white-box weight statistics reach 42%. Contrary to the pre-registered hypothesis that signal decays monotonically from weights to activations to outputs, activations and outputs were more informative than the weight-delta statistics. The black-box result holds unchanged (64%) when only generated text is used, without token probabilities. Domain accuracy is also stable when a third run per dataset is trained on an independently drawn data subsample, and black-box predictions are unaffected by the LoRA rank (8-64). All code and per-run feature vectors are released.

---


### 68. [A Gingerbread House for LLM Agents: Source-Planned Honeypots That Lure Autonomous Attackers into an Isolated Shadow](https://arxiv.org/abs/2611.07611)

**<font color=#1a73e8>作者：</font>** Seungdeok Roh, Seokjun Ryu, Sohee Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents can exploit web vulnerabilities fast enough that patching may come too late. Deception against such agents has mostly lured them away from a real target that stays reachable. We study a different arrangement: an LLM defender plans a static honeypot from the application's source, and a router sends every later request of a client it confirms as an attacker, including a working exploit, to an isolated shadow copy. We compare no defence, this static plan, and an augmented configuration with a runtime LLM responder and further router rules, graded by the benchmark's own grader on the real target and, for ARTEX, also on the shadow. On the 40 critical CVE-Bench tasks the static plan cut real compromise from 26/40 to 5/40 for Claude Opus 4.8 and from 20/40 to 0/40 (31 valid runs) for the ARTEX attack framework. On 20 new tasks not used in the design, ARTEX went from 15/20 to 0/20. In about half of the deception-arm runs ARTEX's exploit succeeded on the shadow while the real target stayed intact: the defence moved a working exploit rather than stopping it, and the remaining risk lies in requests that reach the real target before confirmation. ARTEX reported a planted fake secret as genuine on 30 of the 120 deception-arm tasks, five times in a report that labelled another item a decoy. With ARTEX's real compromise at zero in both deception configurations, they did not differ significantly on the remaining outcomes, a comparison that does not isolate the responder.

---


### 69. [Beneath the Surface: What We Overlook When We Talk About Agent Evolution](https://arxiv.org/abs/2611.07624)

**<font color=#1a73e8>作者：</font>** Xiaobo Wang, Zimu Wang, Siyu Ye 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harness evolution enables recursive self-improvement (RSI) without updating model weights. We examine whether higher benchmark scores yield reliable, efficient, and transferable improvement. We evaluate four methods across harnesses, general and coding tasks. Repeated evaluations, controlled agent expansion, component interventions, and admission replays reveal recurring patterns. All sixteen evolved agents gain previously uncovered tasks while losing previously covered ones. In one general-task case, reliability rises by 5.2 points despite losing ten previously covered tasks. Most reliability gains also increase deployment cost. Specific changes usually outperform generic reminders, but their benefits can change when combined. The highest-scoring agent does not yield the largest mean improvement in any of our four pools, and stricter admission can discard useful alternatives. Transfer selectively preserves gains: coverage usually falls on the general-task target across both harness types and paradigms, but rises on the coding target with the outer-layer-only harness. These findings motivate preservation-aware evaluation, tested decision rules, and explicit applicability conditions. As a constructive follow-up, EvoAudit turns these diagnostics into revisions of select, analyze, mutate, and gate, achieving the best performance.

---


### 70. [Redacting Personal Data: A Speed and Accuracy Comparison of Regex, Presidio and Hybrid Designs](https://arxiv.org/abs/2611.07633)

**<font color=#1a73e8>作者：</font>** Sai Yashwant, Manoj Kumar Gondimalla, Arjun Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many enterprise projects now pass free text to large language models (LLMs), and that text often contains personally identifiable information (PII) such as names, phone numbers, email addresses, home addresses and dates of birth. Once a prompt is sent, this data is copied into provider systems, application logs and observability traces. Redacting PII before the call is an obvious control, yet teams seldom have numbers on what it costs in latency or what it lets through. This paper compares four redaction designs that any LLM pipeline can adopt: a pure regular-expression (regex) redactor, Microsoft Presidio running on a spaCy model, a hybrid in which Presidio finds only person names while regex handles structured identifiers, and a fast hybrid that calls spaCy's named-entity component directly. All four share a known-entity rule, which removes the person the system already knows it is handling, and a consistent placeholder scheme, so the LLM can still tell one person from another after redaction. We evaluate the designs on a sample workflow, which we call ProfileAssist, that turns resumes into structured profiles, using 100 synthetic resumes (523 characters on average, with 900 PII values and 600 business terms that must survive). Regex ran at a 0.20 ms median but caught only 88.9% of PII, because it cannot find names that are not known in advance, such as the references listed in a resume. Presidio, hybrid and fast hybrid each caught 100% of PII and kept 100% of business terms, at median latencies of 37.59 ms, 30.23 ms and 13.48 ms. Measured against a 9,120 ms median LLM call, even the slowest option adds only 0.41% to the request. We therefore recommend the fast hybrid as a default for LLM pipelines that handle personal data, with regex kept as a safety net rather than as the only control.

---


### 71. [Measuring the Marginal Value of Verifier-Based RL Beyond Supervised Fine-Tuning](https://arxiv.org/abs/2611.07639)

**<font color=#1a73e8>作者：</font>** Amit Sagtani, Saloni Garg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (RLVR) is usually evaluated as an alternative to supervised fine-tuning (SFT), or as a stage that follows it, with the implicit assumption that the RL stage contributes gains of its own. We measure that contribution directly, in a controlled setting where both stages can be run to completion and compared exactly. We built gpu-train-debug, a deterministic benchmark of 1,877 synthetic GPU and LLM training failure diagnosis tasks across 30 archetypes, graded by a programmatic verifier with partial credit, and calibrated so that a mid-tier model scores in a 0.60 to 0.75 band. A pilot produced a surprise: 1,200 gold demonstrations nearly solved the benchmark (SFT 0.785 on the hard split), while 15 steps of GRPO from the base model did not move it (0.314 vs 0.311 base). We therefore amended the study, in writing and before the full run, to ask the sharper question: what does verifier-based RL add beyond demonstrations? At the pre-registered scale (60 GRPO steps, learning rate 1e-6), the answer is: no detectable improvement in-distribution (+0.22 points, 95% CI [-0.06, +0.51]), and a modest but measurable improvement under distribution shift (+0.33 points on a held-out OOD split, CI [+0.02, +0.68]). SFT accounted for most of the available improvement, while verifier-based RL produced only modest additional gains under distribution shift. The residual errors SFT leaves are mostly systematic, identical across samples, which likely reduces the within-group learning signal available to GRPO. A full 60-step cold-start GRPO arm confirms the pilot at the full horizon. The whole study cost $8.69 of compute and is fully reproducible from archived generations, frozen configs, and tagged code.

---


### 72. [Don't Prompt Your Agents. Equip Them: Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems](https://arxiv.org/abs/2611.07652)

**<font color=#1a73e8>作者：</font>** Vladimiros Peilivanidis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current autonomous logical systems rely on a fragile assumption: that language models should dynamically write code, guess API payloads, and memorize operational constraints through prompt engineering. In practice, this burns massive context windows, inflates API bills, and produces brittle agents that fail unpredictably in production.
In this work, we present Skillware, an open architectural framework and capability registry that formally separates what an agent wants to do from how that task is executed. Instead of prompting models with loose text instructions or markdown files baptized as 'skills', Skillware equips them with modular, versioned software capability bundles. Much like skill hotkeys in video games that execute deterministically under fixed world rules, each bundle combines a typed JSON input contract, deterministic Python code, task directives, bundled datasets, and automated unit tests. In-process adapters translate these capabilities into native tool declarations for any model, from frontier cloud APIs to local open-weight runtimes with zero network latency.
Evaluating 23 frontier and open-weight models across 368 benchmark conditions, we show that small local models (3B to 8B parameters) equipped with Skillware consistently outperform unequipped frontier models on complex multi-step workflows. They cut token usage by up to 84.8%, slash inference costs by up to 97.3%, and eliminate parameter errors entirely. True agent reliability does not come from larger models or longer prompts, but from equipping logical systems with verified, deterministic software.
Finally, we articulate the trajectory of capability bundles across an invariant continuum of information processing systems: from digital logical systems today, to IoT, drones, and embodied robotics tomorrow, establishing a foundation for auditable, real-time capability execution.

---


### 73. [English Calibration Erodes Lithuanian in Expert-Pruned Mixture-of-Experts Language Models](https://arxiv.org/abs/2611.07654)

**<font color=#1a73e8>作者：</font>** Tomas Rasymas, Povilas Kvedaras  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Expert pruning compresses Mixture-of-Experts (MoE) language models by removing the experts that a calibration set marks as unimportant. Studies of high-resource languages largely find that English calibration transfers well to other languages. We test this for Lithuanian: we pruned four MoE models with REAP, removing 25% or 50% of the experts with English, Lithuanian or mixed calibration, and evaluated both languages on reading comprehension, translation and language modelling. English calibration does not transfer to Lithuanian: at 25% pruning, English comprehension fell by a median of 1.7 points but Lithuanian by 21.4. The transfer is asymmetric. Lithuanian calibration removed most of the Lithuanian loss and never significantly hurt English comprehension, which was on average 2.5 points better than under English calibration; only English language modeling got slightly worse. Routing suggests why: in the last layers, Lithuanian sends 55-72% of its expert selections to just eight experts, against 19-39% for English, and English calibration removes some of these experts. Compressed models should be calibrated, and evaluated, in every language they must serve.

---


### 74. [Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies](https://arxiv.org/abs/2611.07667)

**<font color=#1a73e8>作者：</font>** Mete Erdogan, Mirac Suzgun, Aneesh Pappu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The performance of multi-agent LLM systems depends not only on the capabilities of the underlying models but also on information-sharing policies, which govern what information each agent observes and at what level of detail. But does providing AI agents with more detailed information always improve collective outcomes, or can transparency paradoxically degrade efficiency? To investigate this, we introduce empirical information design, an experimental framework that systematically compares disclosure policies across economic markets populated by LLM agents, while holding interaction rules and models fixed. We evaluate ten frontier LLMs in multi-resource trade, bilateral bargaining, and double auctions, using ground-truth utilities to decouple identified opportunities from realized outcomes. We find that finer information disclosure yields highly model-dependent results. In trade, revealing exact valuations rather than ordinal preference rankings reduces realized gains for GPT-6 Sol (from 98% to 91% of maximum) yet increases them for Claude Sonnet 5 (from 72% to 86%). In bargaining, exact information leads Grok 4.7 to produce less balanced agreements, whereas Claude Opus 5.5 divides gains symmetrically. In double auctions, full disclosure inflates price demands, triggering market breakdown and lowering welfare for Gemini 3.1 Pro (97% to 78%), Claude Opus 5.5 (94% to 64%), and Grok 4.7 (97% to 62%). Overall, these results suggest that model selection and information design must be co-optimized, as LLMs vary in how their strategic responses to information impact system objectives.

---


### 75. [An Information Bottleneck for Post-hoc Memorization Mitigation in LLMs](https://arxiv.org/abs/2611.07669)

**<font color=#1a73e8>作者：</font>** Dina EL Zein, Shashi Kumar, James Henderson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent studies have shown that large language models (LLMs) can memorize and reproduce copyrighted training data, raising serious privacy and intellectual property concerns. In this work, we investigate whether memorization can be mitigated without modifying or retraining the underlying model through an information bottleneck. We propose a modular plug-and-play framework that inserts a nonparametric variational information bottleneck (NVIB) between a frozen LLM backbone and its language modeling head. By compressing the final hidden representations before token prediction, the proposed bottleneck aims to preserve general linguistic knowledge while filtering out highly specific memorized sequences. We evaluate our approach on memorization extraction tasks involving book passages and on standard language modeling benchmarks to measure the trade-off between memorization reduction and downstream utility. Our experiments show that the NVIB layer substantially reduces extractability while maintaining competitive performance on benchmark tasks. These results suggest that adding an information bottleneck offers a practical and architecture agnostic direction for post-hoc memorization mitigation in pretrained LLMs.

---


### 76. [Egocentric Action Recognition with Objects and Vision-Language Affordances](https://arxiv.org/abs/2611.07673)

**<font color=#1a73e8>作者：</font>** Raúl Boix-Aldeguer, Manuel Benavent-Lledo, David Ortiz-Perez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action recognition, and more specifically egocentric action recognition, is a core task in computer vision, with applications such as monitoring the daily life activities of elderly people and task assistance. Recent methods rely on visual modalities such as RGB video or depth. However, in egocentric video, an action is largely defined by its objects, which these methods rarely model. We propose a method that combines a frozen SlowFast video expert with an attention-based object expert by late fusion. Each object is represented with its affordances, that is, what can be done with it, generated zero-shot by a vision-language model. Since datasets such as MECCANO annotate only the objects involved in each action, evaluating with these boxes tells the model which objects are active. We therefore train on annotated boxes and evaluate the method with detections from the official active-object detector, and with annotated boxes as an upper bound. Without affordances, our fusion reaches 68.4% Top-1 with annotated boxes but 49.0% with detections. About half of this drop comes from non-active detections. To remove them, the same vision-language model generates an interaction affordance that decides whether a hand is manipulating each detected object. On MECCANO, objects raise the Top-1 of the video expert from 44.9% to 49.0%, and the two affordances raise it to 49.9%, above SlowFast and object-aware RGB baselines. Code will be released upon acceptance.

---


### 77. [MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents](https://arxiv.org/abs/2611.07689)

**<font color=#1a73e8>作者：</font>** Yizhen Jiang, Haowei Guo, Tianyi Bai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly deployed through the Model Context Protocol (MCP), which allows them to discover and invoke tools across multiple servers at runtime. Existing MCP benchmarks primarily measure task completion; where they diagnose failures, they do so after execution rather than building specific reasoning, execution, and memory failure risks into task construction.
We introduce MCPHallu, a benchmark for diagnosing hallucination-prone agent failures in MCP environments along three axes: reasoning, execution, and memory. MCPHallu contains 358 tasks across five capability domains and runs on 36 production MCP servers in isolated containers. Each task is designed with a structural trigger that makes one of four subtypes the dominant failure risk: Branch Collapse, Unreachable Goal, Tool Misuse, or Context Forgetting. This design enables subtype-level analysis rather than aggregate task success alone.
We evaluate fourteen frontier LLM agents from eight vendors on 5{,}012 trajectories. Current MCP agents remain vulnerable to hallucination-inducing tool environments, achieving an average score of 0.642 on a $[0,1]$ scale (higher is better). Failures concentrate on Unreachable Goal tasks, where the average score drops to 0.458 and 23.2\% of runs pass, indicating that agents often continue issuing tool calls or claim successful completion rather than recognizing infeasible goals. Subtype rankings diverge sharply: a model's rank shifts by 6.9 of 13 positions on average across subtypes, and Branch Collapse is uncorrelated with Unreachable Goal across models ($r = -0.12$). MCPHallu is released at this https URL.

---


### 78. [Evaluating Language Model Features for Zero-Shot Time-Series Anomaly Detection Under Isolation Assumption](https://arxiv.org/abs/2611.07720)

**<font color=#1a73e8>作者：</font>** Romain Hermary, Nesryne Mejri, Djamila Aouada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-Series Anomaly Detection (TSAD) is a fundamentally challenging task: it is unsupervised, requires high local precision capabilities, and suffers from limited labelled data. Recent work has explored adapting Large Language Models (LLMs) to time-series via cross-modal transfer. However, existing approaches are poorly suited to Multivariate TSAD (MTSAD), as tokenisation often obscures fine-grained temporal and variables structures, and most methods optimise auxiliary objectives such as forecasting or reconstruction. We posit that these surrogate objectives become unreliable as model capacity increases. Highly expressive models risk reconstructing or forecasting anomalies, undermining the foundations of both strategies. Instead, we propose to use LLMs purely as feature extractors and directly analyse their induced feature spaces. In this work, investigate the ability of LLMs to provide useful representations for MTSADs in a zero-shot setting through classification. To this end, we study the separability of the extracted features, under the assumption that anomalous features should be isolated from normal ones. We analyse their temporal and contextual discriminative ability using simple step-wise tokenisation schemes, with one time-step per token, which preserve fine-grained local information. Their usability for MTSAD is assessed using an unsupervised Isolation Forest, enabling a direct evaluation of the resulting representation quality. We further investigate whether the observed performance can be attributed to the language-related pre-training of the LLMs or arises independently of it. Our results provide empirical insight into the ability of LLMs to represent multivariate time-series for anomaly detection and highlight broader applications of cross-modal foundation models.

---


### 79. [Reinforcing What the Student Has Learned: Teacher-Guided On-Policy Distillation](https://arxiv.org/abs/2611.07722)

**<font color=#1a73e8>作者：</font>** Bozhen Fang, Linhao Zhong, Xuehao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) improves language-model reasoning through dense teacher feedback on student-generated this http URL first observe an amplitude disparity in this feedback: on math reasoning responses, style-related positions exhibit 3.5 times the mean absolute teacher--student log-probability difference of mathematical this http URL OPD updates by these discrepancies thus directs much of the update strength toward matching the teacher's expression. We instead take the student's own pretrained base as a reference: the student--base difference records the token preferences acquired during post-training and provides supervision that does not depend on the student's distance from the teacher. Building on this reference, we propose Student-Delta On-Policy Distillation (SD-OPD), which uses centered student--base differences as update coefficients, keeps each coefficient only when its sign agrees with centered teacher--student feedback, and recomputes the student signal every training round. Across 5 teacher--student configurations with Qwen3 students of 1.7B to 8B parameters, SD-OPD improves six-task mathematics average pass@1 (avg@16) over OPD by 7.76 to 10.37 percentage points. Code is available at this https URL.

---


### 80. [O$^2$PD: Overlap-Gated On-Policy Distillation on Reliable Prefix](https://arxiv.org/abs/2611.07731)

**<font color=#1a73e8>作者：</font>** Shuaishuai Zu, Jihao Zhao, Pengfei Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) supplies dense token-level supervision by aligning a student to the teacher's next-token distribution on its own generated rollouts. Existing works mostly implement top-$k$ OPD, applying reverse Kullback-Leibler ($\RKL$) divergence between the teacher's and the student's renormalized distributions over teacher top-$k$ support. However, the teacher scores student-generated rollouts that are inherently off-policy for itself, leaving the reliability of its next-token guidance unclear. Restricting the divergence to the teacher top-$k$ support also discards the remaining mass outside that support. These gaps leave two questions implicit: 1) which tokens to align, and 2) how to align those tokens. To answer these questions, we propose Overlap-gated On-Policy Distillation (O$^{2}$PD). As for 1), we quantitatively analyze the reliability of teacher supervision and find that alignment on the student's trajectory prefix is more reliable than alignment on the full context. Therefore, our O$^{2}$PD is applied only to the 20\% prefix tokens of each student rollout. As for 2), we theoretically characterize two problems of top-$k$ OPD: the \emph{Teacher-support Uncovering} and the \emph{Dominant-Mode Mismatch}. Based on these analyses, we propose two support strategies: the \emph{Reset Support} strategy attaches a reset atom to every token, pooling mass outside the teacher top-$k$, and the \emph{Support Convergence} strategy converges the support to the already aligned intersection. Our O$^{2}$PD employs the designed overlap-gated $\alpha$-divergence to interpolate between mode-covering and mode-seeking for per-token alignment, where the overlap is used as a gate to switch the support and adaptively modulate $\alpha$.

---


### 81. [Evaluating Token Probabilities as Confidence Estimators in Human Behavior Simulations: A Case Study in Luxembourgish Next Like Prediction](https://arxiv.org/abs/2611.07735)

**<font color=#1a73e8>作者：</font>** Nils Schwager, Simon Münker, Alistair Plum 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly used to simulate human behavior, their operational validity is typically assessed through accuracy alone, implicitly treating human behavior as deterministic. We argue that on noisy digital trace data, a model's performance depends not only on predicting the correct outcome but on its calibration. We present a case study testing whether the token probabilities of open-weight LLMs can serve as confidence estimates in a Next Like Prediction task: predicting how a user of the Luxembourgish news platform this http URL rates a comment, conditioned on their prior interactions. Evaluating Ministral 3 (3B, 8B), we find that, with in-context learning only, the tested models are overconfident and are outperformed on accuracy and calibration by a simple statistical baseline. Accuracy and calibration do not move together: scaling from 3B to 8B improves accuracy while degrading calibration, and longer behavioral histories raise accuracy while confidence declines. Task-specific supervised fine-tuning acts as an effective calibration intervention, reducing Expected Calibration Error from 0.2 to 0.006 while improving accuracy from 0.536 to 0.758. We conclude that confidence estimation should be evaluated alongside accuracy to improve validity when using LLM-based agents.

---


### 82. [Extending Reasoning in Typed Decision Models via Looping](https://arxiv.org/abs/2611.07736)

**<font color=#1a73e8>作者：</font>** David Berghaus, Arber Zela, Behzad Shomali 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typed decision models choose among a fixed set of answer options in a single forward pass, so unlike generative language models they cannot spend more test-time compute on hard inputs by generating more tokens. Looping a block of layers offers this compute in latent space without adding parameters, but prior work found no gain from loops retrofitted into conventionally pretrained models. We show that such loops help when trained together with the decision model. Our method, RELOAD (retrofitted loops for adaptive decisions), fine-tunes a pretrained encoder or decoder with a damped loop over its middle block and a lightweight controller picks the number of passes adaptively for each input. Across six models from 0.4B to 4B parameters, looping improves both accuracy and calibration, mostly on problems that need longer chains of reasoning than any seen in training, where encoders gain up to 23 points. Neither matched training compute nor more data closes this gap, and separate layers for each pass come close only with nearly twice the parameters. The controller keeps most of the gain at about three quarters of the compute.

---


### 83. [Automated Video-to-QA Pipeline: End-to-End Question Generation and Verification Using Large Language Models](https://arxiv.org/abs/2611.07755)

**<font color=#1a73e8>作者：</font>** Jaival Chauhan, Vikram Singh, Pruthwik Mishra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The exponential growth of educational and informational video content on platforms like YouTube presents a challenge for efficient knowledge retrieval and assessment. This paper proposes an end-to-end automated pipeline for extracting structured summaries and generating high-fidelity Question-Answer (QA) pairs from video streams. The framework integrates a cascade of state-of-the-art models: audio extraction is handled via FFmpeg, followed by automatic speech recognition (ASR) using Whisper (A library in Python) to generate accurate transcripts. Due to the token constraints of Large Language Models (LLMs), transcripts are segmented and summarized using Facebook's BART. A key innovation of this work is a Self-Verification and Fine-Tuning Loop. We utilize meta-llama/Llama-3.1-8BInstruct to generate candidate QA pairs from transcript chunks, which are then fed back into the model to rigorously assess their relevance and importance. Only verified, high-quality pairs are retained to construct a synthetic dataset. This dataset is subsequently used to fine-tune the Llama model using Low-Rank Adaptation (LoRA), resulting in a specialized model capable of generating domain-aligned assessment questions. This approach demonstrates a scalable method for creating self-improving educational tools without the need for manual data annotation. The proposed model can be downloaded from Kaggle with all the codes from GitHub.

---


### 84. [Scaling Laws for SAE Training Data](https://arxiv.org/abs/2611.07756)

**<font color=#1a73e8>作者：</font>** Nikita Koriagin, Nikita Balagansky, Daniil Gavrilov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation storage is often a bottleneck in sparse autoencoder (SAE) training. We study how many unique activations an SAE needs when its total training budget is fixed. Quality improves rapidly as the buffer grows, then reaches a plateau where replaying the buffer is nearly as effective as using fresh activations throughout training. Beyond this point, additional unique activations bring little benefit to reconstruction or interpretability, so the buffer need not grow with the training budget. We describe this tradeoff between diversity and repetition with a scaling law for limited data. We validate it across dictionary sizes and token budgets, early, middle, and late layers of Llama-3.1, Qwen3 model sizes, and BatchTopK, TopK, and JumpReLU SAEs. Sweeps using mathematical text and Python code test the effect of changing the activation source. Evaluation covers explained variance (EV), reconstruction MSE, feature absorption, automated interpretability, and sparse probing. These results give a practical training rule: choose the smallest buffer that reaches the quality plateau and replay it for the remaining budget. In our experiments, this reduces activation storage by $8\text{--}64\times$ with negligible quality loss.

---


### 85. [RIVER: Evidence-guided multi-agent retrieval for enzyme--reaction discovery](https://arxiv.org/abs/2611.07757)

**<font color=#1a73e8>作者：</font>** Yifan Chang, Yunze Li, Feifei Jiang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enzyme function annotation and the identification of candidate enzymes for a given reaction are essential steps in connecting genomic information to biochemical reaction networks. However, existing methods rely on sequence or structural similarity or on training with known enzyme--reaction pairs, making it difficult to integrate biochemical evidence across large candidate spaces; they also struggle with retrieval tasks involving enzyme families whose members are highly similar. Here, we introduce RIVER (Reaction--enzyme Inference via Evidence-guided Retrieval), a multi-agent framework for bidirectional enzyme--reaction retrieval that identifies potentially catalyzed reactions for a given enzyme and ranks candidate enzymes for a given reaction. RIVER coordinates large language models, specialized biochemical computational tools, and external knowledge resources to assemble evidence at multiple levels, including reaction chemistry, protein sequences and domains, catalytic mechanisms, and database annotations. Dedicated validation modules further examine evidence gaps and potential conflicts and rerank candidates using traceable evidence records. On public benchmarks, RIVER achieves the highest success rates in both enzyme retrieval and enzyme annotation. In family-specific enzyme retrieval, RIVER outperforms the evaluated baselines on the selected datasets and metrics. In Escherichia coli enzyme retrieval tasks constructed from recent literature, RIVER achieves the best retrieval results with closed-source and open-source model configurations, substantially outperforming closed-source general-purpose and biology-specialized multi-agent systems, including Claude Code, Codex, and Phylo Max. These results suggest that evidence-guided multi-agent retrieval can prioritize biochemically supported enzyme--reaction relationships, providing a basis for subsequent experimental validation.

---


### 86. [The Intrusion Pathway: How Non-Evidential Context Degrades Language Model Performance](https://arxiv.org/abs/2611.07778)

**<font color=#1a73e8>作者：</font>** Dikshant Kukreja, Gautam Gupta, Avni Mittal 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models lose accuracy when a prompt contains non-evidential context: irrelevant statements from unrelated domains, or random off-distribution tokens, with no competing answer and no semantic overlap with the query. Such noise pervades retrieval-augmented, tool-using, and long-context deployments, yet the failure has lacked a mechanistic account. We trace the corruption to the Intrusion Pathway, which starts with MLPs enriching both query-subject and irrelevant-token representations, parroting heads carry prefix-token content to the prediction position, and relational readers largely avoid unrelated sources. Nevertheless, preserved subject enrichment and selective reading do not prevent intrusion in the broader computation. We then localize part of this interference to a sparse set of attention heads, which we call intrusion heads. Their prefix-derived writes promote distractor-related content, while their reduced support for the correct answer arises primarily from weaker non-prefix contributions rather than direct suppression by the prefix. The same heads transfer across tasks and distractor types and are largely weight-disjoint from the heads that integrate relevant contextual evidence, enabling a class-conditional intervention. Replacing the corrupted last-token residual with its clean counterpart, an oracle probe that requires a matched clean forward pass, recovers 97.6% on average of the distractor-induced drop across four downstream tasks. A deployable mask level knockout of about ten heads, roughly 1% of the model's attention heads, recovers 57% at bounded cost to helpful context.

---


### 87. [Bridging Structure and Semantics: Knowledge Graph Verification via Triple-to-Text Alignment](https://arxiv.org/abs/2611.07780)

**<font color=#1a73e8>作者：</font>** Ziang Cui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic accuracy is an important dimension of knowledge graph quality. Graph-based scoring methods exploit relational structure, while textual representations allow classifiers to draw on knowledge encoded by pre-trained language models (PLMs). We present GenVer, a generative verifier that scores triples using both their serialized form and generated natural language representations (NLRs). A triple-text alignment procedure selects training pairs for a sequence-to-sequence generator; a BERT-based classifier then combines features from each triple and its generated NLR. On four FactFB variants, constructed from FB15k using perturbed negative triples, GenVer obtains the highest classification accuracy among the evaluated baselines, ranging from 88.56% to 91.52%. The experiments suggest that generated representations can help triple classification, while the case analysis also exposes semantic drift and high-confidence errors.

---


### 88. [PBPO: Prefix-Block Policy Optimization for Diffusion Language Models](https://arxiv.org/abs/2611.07783)

**<font color=#1a73e8>作者：</font>** Katherine Tieu, Dongqi Fu, Si Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) commonly decode responses by proceeding autoregressively across blocks while iteratively denoising multiple tokens within each block. This structure makes block-level policy optimization a natural adaptation of autoregressive policy optimization. However, the exact likelihood of a completed block is intractable because it marginalizes over the intermediate states and reveal orders of the denoising process. To realize the block-level formulation, we construct a prefix-block state and use a single model evaluation to define a factorized one-step surrogate for the block likelihood. The resulting block surrogate ratio is a product of its token surrogate ratios, allowing variation at individual positions to propagate across the entire block before clipping. We therefore introduce Prefix-Block Policy Optimization (PBPO), which preserves block-level conditioning but applies surrogate importance weighting and clipping separately to each token. PBPO further diversifies repeated updates by resampling corrupted views of the prompt and revealed prefix, a design motivated by masked-dLLM pre-training. Under our analysis assumptions, block-product weighting amplifies the variance of gradient contributions relative to token-local weighting. Across two LLaDA-family initializations, six benchmarks, and three generation lengths, PBPO achieves competitive performance against existing dLLM RL methods.

---


### 89. [Thinking Is Not Writing: Designing AI Chatbots to Connect Reasoning and Revision](https://arxiv.org/abs/2611.07792)

**<font color=#1a73e8>作者：</font>** Lucile Favero, Tanja Käser, Juan Antonio Pérez-Ortiz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Supporting students' argumentative writing with AI requires connecting reflection to their revision processes. We present Maike, a Socratic chatbot supporting writing through argument diagnosis, targeted questioning, and a student model across Think and Write modes. In a classroom study, 65 secondary-school students used Maike or a control chatbot sharing the interface, language model, and Think/Write modes. Approximately 40% of students improved their essay scores. However, Maike users engaged more in idea-level dialogue (56% vs. 44%) and moved iteratively between discussion and editing. Transitions from ideas discussed in dialogue to revisions were positively associated with score gains. These findings suggest a design target for AI writing support: coordinating reflection with revision. We contribute an architecture for supporting argumentative reasoning without generating essay text and an approach linking interaction patterns to writing processes and outcomes. As AI becomes embedded in classrooms, understanding these connections is essential to assessing (and designing for) its educational value.

---


### 90. [VocabulARy 2.0: A Generative AR System Enabling Personalised 3D Mnemonics for Vocabulary Learning in Context](https://arxiv.org/abs/2611.07798)

**<font color=#1a73e8>作者：</font>** Karolina Trajkovska, Matjaž Kljun, Maheshya Weerasinghe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mnemonics support vocabulary learning by linking unfamiliar words to familiar concepts through memorable verbal and visual associations. We present a generative AR system that enables learners to create personalised 3D mnemonics by transforming familiar objects in their surroundings into situated mnemonic anchors. The system scans the environment, detects visible objects, and generates bilingual flashcards. After selecting a word, the learner describes a personal association. The system combines this description with an image of the selected object to generate a textured 3D model using generative AI. Learners can then place the model relative to the real object, transforming it into a situated mnemonic anchor.

---


### 91. [Decodability Is Not Validity: Evaluating Nuisance Sensitivity in Language Model Concept Probes](https://arxiv.org/abs/2611.07805)

**<font color=#1a73e8>作者：</font>** Ayal Klein  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Two concept probes can be equally accurate at predicting a concept from a language model's hidden states while their scores contain different mixtures of the target concept and a correlated nuisance attribute. In four target--nuisance settings (two aspect sentiments in CEBaB; occupation and gender in BiasBios; Amazon review sentiment with negation, and with first-person framing), two LLMs, and a population of concept extractors, we compare decodability with discriminant evidence: the score's dependence on the nuisance at fixed target, and its response to input edits intended to change only the nuisance, filtered by two LLM judges and compared against placebo edits. Under correlated training data, extractors that are statistically equivalent in held-out AUROC differ up to several-fold in nuisance sensitivity in three of the four settings, and decodability is not a reliable proxy for it: their rank correlation changes sign across settings. The effect follows the probe's training data, not the nuisance's natural association with the target: first-person framing, unrelated to sentiment in natural reviews, is absorbed at least as much as negation, which co-occurs with negative sentiment, and decorrelated training removes the systematic effect. Selecting extractors with nuisance-aware development diagnostics, which need nuisance labels but no counterfactuals, lowers counterfactual nuisance sensitivity wherever the default choice is sensitive, at a small accuracy cost. Concept measurements should be validated, not just decoded.

---


### 92. [Different Corpora, Different Skills? A Paired Study of Small Language Models](https://arxiv.org/abs/2611.07812)

**<font color=#1a73e8>作者：</font>** Edoardo Vaira, Georgios Chavales, Pierre Nugues  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models are often trained under tight data budgets, where the choice of pretraining corpus may matter as much as model size or training recipe. We compare two contrasting corpora at matched 10-million- and 37-million-word budgets: the 1911 Encyclopaedia Britannica and the BabyLM 2026 strict pretraining corpus. For each corpus, we train teacher models, distilled 58-million-parameter Baby-Llama students, and no-distillation student ablations, using the same model families, training recipes, and evaluation protocol across corpora. Across BLiMP, BLiMP Supplement, EWoK, Entity Tracking, and COMPS, the corpora produce different skill profiles rather than a single quality ranking. BabyLM 2026 is consistently stronger on linguistic acceptability benchmarks, while Britannica is often stronger on Entity Tracking, a synthetic state-tracking task. The contrast appears across teacher and student models and at both budgets, with the cleanest cross-seed replication in the distilled student comparison. Targeted controls show that the central contrast persists after matching training exposure and at a longer diagnostic context; direct teacher ensembling also does not reproduce the 10M Britannica student's Entity Tracking behavior. Entity Tracking magnitudes nevertheless remain sensitive to training dynamics. For this corpus pair, corpus choice can therefore produce different relative skill profiles at small scale, motivating multi-benchmark evaluation when comparing pretraining data.

---


### 93. [Axis-LoRA: Probing and Adapting Embedding Models for Personal-Memory Retrieval](https://arxiv.org/abs/2611.07820)

**<font color=#1a73e8>作者：</font>** Dohoon Kim, Junho Park, Hyunwoong Bae 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs are increasingly asked questions about a user's personal experiences, retrieval must distinguish memories by time, place, person, and event. Current personal-memory pipelines rely on frozen dense embedding models to embed memories for retrieval, but we find that these models do not capture the four axes well. Swapping a memory's date or place barely shifts its embedding, and a trained projection on top of the frozen embedding does not recover the missing signal. The problem lives inside the model, where each axis is encoded by a distinct attention-head pattern. Guided by these findings, we propose Axis-LoRA, a per-axis adapter that places four LoRA branches inside the embedding model and combines them via a per-query gate. Across three standard embedding models evaluated on LongMemEval, ATM-Bench, and LoCoMo, Axis-LoRA improves 4-benchmark mean R@10 by $+1.28$ to $+1.56$~pp while training only a small fraction of the base parameters on a small axis-counterfactual training set. Code is available at this https URL.

---


### 94. [Generate-then-Rank: Learning Symbolic Goal Interpretation for Embodied Agents](https://arxiv.org/abs/2611.07825)

**<font color=#1a73e8>作者：</font>** Jisen Lei, Huizhi Liang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Goal interpretation is to translate a natural language instruction into a formal symbolic goal that a planner can execute. It is critical for embodied agents because any error here propagates to every downstream planning and action step. Doing it well requires both generating suitable candidates and reliably selecting among them. We present a two-stage generate-then-rank approach to Goal Interpretation in the Embodied Agent Interface (EAI). First, supervised fine-tuning adapts a Large Language Model (LLM) to EAI's output convention. Second, Candidate-Output Ranking from Errors (CORE) learns preferences over complete outputs from the model's own generated alternatives. We conducted experiments on the household scenes of the Embodied Agent Interface Benchmark. Multiple open source LLMs including DeepSeek-V3 chat, DeepSeek-Reasoner, and Qwen2.5-7B and Qwen2.5-72B were evaluated. The proposed method outperformed the baseline models including LLMs with simple prompting, chain-of-thought, and knowledge graph based approaches.

---


### 95. [THG-Omni: Traceable Human-Centric Graph Supervision for Video Reasoning](https://arxiv.org/abs/2611.07836)

**<font color=#1a73e8>作者：</font>** Jisheng Dang, Kai Wei, Ronghao Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-modal models can answer questions about video, but their predictions rarely show which participant, event, or interval supports an answer. Moreover, answer-level supervision alone does not teach a model to interpret structured video evidence. To systematically mitigate this issue, we present THG-Omni, a human-centric graph-supervision framework that links Segment Anything Model~3 participant tracks with temporally grounded Qwen3-VL annotations. Candidate semantic claims are checked against the source video and available audio before they are used to construct training questions, while track geometry provides explicit spatial and temporal supervision. The resulting questions teach an omni-modal reasoning model to interpret participant attributes, actions, affect, interactions, and their timing from a structured graph. At inference, THG-Omni uses a predicted graph constructed from the evaluation video. Experiments on IntentBench show consistent improvements over the unadapted backbone across social reasoning, emotion understanding, and deception perception. On NExT-QA, THG-Omni achieves 89.54\% accuracy with the matched graph, compared with 85.10\% without graph input. Further validation experiments show that compact graph input achieves 78.22\% accuracy, compared with 78.02\% using the full graph and 77.58\% without graph input. A complementary diagnostic demonstrates that the predicted graph preserves evidence useful for answering questions even without the source video and audio. Together, these findings show that THG-Omni improves human-centric video reasoning while grounding its evidence in identifiable participants and events. Our codes are available at this https URL

---


### 96. [Computation, not weight access: large language models as auditors of clinical prediction networks](https://arxiv.org/abs/2611.07847)

**<font color=#1a73e8>作者：</font>** Zhiyu Liu, Xinyu Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier large language models (LLMs) have been reported to read, edit and write the weights of small neural networks, raising the prospect of auditing clinical prediction models from their files alone. Public demonstrations, however, mixed reading raw weights with running code. We separated these conditions in internally pre-specified simulation experiments. Tanh networks of 105 to 38,401 weights were trained on simulated cohorts of patients with subarachnoid haemorrhage, each with a planted relationship or none, and one network was trained on labels that under-recorded deaths in a subgroup. GPT-6 Astra and four other GPT models answered single prompts under a default or an explicit system instruction, either with the weights in the prompt and no tools, or with a calculation-only tool that exposed the weights (white box) or only the network's predictions (black box). Without tools, Astra recovered planted relationships in 353-weight networks but became unreliable at 3,457 weights, and under the default instruction it declined 11 of 12 audit and repair tasks as unidentifiable; the explicit instruction removed these refusals. With the tool, it recovered the planted relationship in all 29 runs on networks of up to 38,401 weights, raised no false alarm in 15 runs on null networks, and found the biased subgroup in 6 of 6 runs. Black-box access performed as well as white-box access, and other GPT-6 models read as accurately. A well-designed script matched the comparator models on the audit and the best LLM repair. For auditing these networks, what mattered was computation and elicitation, not access to the weights.

---


### 97. [CANMentor: A Large-Small Model Collaboration Framework for CAN Bus Intrusion Detection](https://arxiv.org/abs/2611.07853)

**<font color=#1a73e8>作者：</font>** Zhiquan Liu, Haolin Gao, Bo Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Controller Area Network (CAN) bus lacks built-in security mechanisms, making real-time intrusion detection necessary. However, resource and latency constraints limit vehicle-side intrusion detection systems (IDSs) to lightweight models, whose detection performance and generalization can degrade under non-independent and identically distributed (non-IID) data. Meanwhile, uploading original CAN messages to the cloud for more powerful model inference risks exposing sensitive vehicle information. We propose CANMentor, a large-small model collaboration framework in which a cloud-side large language model (LLM) teacher supervises vehicle-side lightweight IDS models for CAN bus intrusion detection. Each vehicle first performs local inference, and a privacy-aware generator then produces proxies from the original CAN messages for cloud-side teacher inference to protect data privacy. The vehicle uses the teacher prediction only when the response arrives within a prescribed latency bound and otherwise retains the local prediction; all returned teacher logits are converted into soft targets for periodic knowledge distillation. On non-IID partitions of the ROAD dataset and the HCRL Car-Hacking dataset, knowledge distillation yields maximum relative Macro F1 improvements of 25.01% and 20.79%, respectively. Teacher predictions also improve detection accuracy for CAN messages near the local decision boundary by 38.71-42.00 percentage points.

---


### 98. [Towards Foundation Decision Models: Drex](https://arxiv.org/abs/2611.07854)

**<font color=#1a73e8>作者：</font>** Nischay Dhankhar, Alisher Amantay, Zhanibek Datbayev 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive approaches with large language models, such as long chain-of-thought reasoning, have become the default for new AI applications because they reach higher accuracy on a wide range of tasks. In production, however, they give inconsistent answers, require parsing of outputs, and add cost and latency. Decision models address this: given a question and a set of options supplied by the user, they return a probability distribution over the options without autoregressive decoding. We present Drex, a family of four open decision models with 8B (DLM), 9B (v1.5), 35B with 3B active (v2.0), and 27B (Max) parameters. Each request consists of a state (a document, record, or agent context, optionally with images) and questions about it, each asking for a choice among options, a yes/no judgment, or a score on an ordered scale. Training combines supervised fine-tuning with reinforcement learning from adjusted feedback (RLAF), plus vision tuning for Max. Ablations show that RLAF improves accuracy and that consistency losses improve robustness to option order. On Decision Index 0.4.1, Max sets a new state of the art among the decision models we compare (67.52 on the public suite vs. 60.70 for Jev 1.14.0). On Decision Bench v4, it is statistically tied with d3-turbo and GPT-6 Sol and trails Claude Opus 5.5 by 1.6 points, and it has the highest accuracy among decision models on DecideBench. Max answers a typical request in 183 ms, against about 2.0 s for GPT-6 Sol and 3.5 s for Claude Opus 5.5, and its outputs are stable under option reordering. All four models are open source: this https URL

---


### 99. [Do Recommenders Need to Think in Words? Latent Reasoning for Efficient LLM-Based Recommendation](https://arxiv.org/abs/2611.07866)

**<font color=#1a73e8>作者：</font>** Hongyang Su, Beibei Kong, Lei Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based recommender systems increasingly generate chain-of-thought (CoT) text before each item prediction to activate the LLM's reasoning capacity, costing tens to hundreds of extra tokens per recommendation at inference. We ask whether inference-time reasoning artifacts (textual or latent) can be replaced by training-time supervision alone, without loss of accuracy. We propose LatentRec, a framework for LLM-based generative recommendation that replaces inference-time reasoning artifacts with training-time per-step head supervision. LatentRec has three components. A 2.5M-parameter Continuous Thought Module iterates K latent reasoning steps over the LLM's hidden state during training. Soft Token Selection bridges the ~14x norm gap between hidden states and input embeddings. A Per-step Reasoning Loss (PRL) supervises every intermediate state through the LLM's prediction head against the first token of the target Semantic ID. The trained LLM retains this accuracy without the module at inference, so the module can be discarded at deployment. On three Amazon benchmarks, LatentRec improves HR@10 by 4.0-5.0% (relative) over a CoT-distilled baseline at 18.3x lower latency (batch=1). Per-step training supervision consistently improves accuracy across three datasets, paid once at training rather than at every recommendation.

---


### 100. [FARR: Forecast-Aware Residual Refinement with Matched Endpoint Evidence for Long-Horizon Time-Series Forecasting](https://arxiv.org/abs/2611.07870)

**<font color=#1a73e8>作者：</font>** Yiyang Zhang, Yuli Zheng, Bin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models use auxiliary conditioning to incorporate additional information into time-series forecasts. However, auxiliary conditioning does not consistently improve accuracy and can increase forecasting error when its influence is poorly matched to the observed temporal context. We propose Forecast-Aware Residual Refinement (FARR), which learns to correct forecasts using endpoint evidence. FARR obtains a valid forecast under the standard condition and a null forecast under a predefined null condition. Their difference reveals how conditioning changes the prediction. A shared residual refiner combines this endpoint evidence with historical features to estimate the remaining error of the valid forecast. Horizon-wise gating then controls the contribution of the predicted residual to the final output. Experiments on four long-horizon forecasting benchmarks show that FARR achieves the best dataset-average MSE and MAE among the compared methods. Code will be released at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-183](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
