# 🧠 大模型相关研究 | 2026年10月01日

> 本类共 **515** 篇论文：已确认 **473** 篇，待复核 **42** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-515](./part-11.md)

---

### 451. [Probability is Not Enough: Exploring and Counting Divergent Tokens for Reasoning Uncertainty Quantification in LLMs](https://arxiv.org/abs/2609.38070)

**<font color=#1a73e8>作者：</font>** Feiyang Li, Shengjing Liu, Qi Zhan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the chain-of-thought reasoning capabilities of large language models improve, evaluating and calibrating their reasoning confidence is becoming increasingly important for quantifying the uncertainty of their answers. Current methods for estimating the confidence of large language models are generally based on probabilities of selected key tokens, but the underlying mechanism remains unclear. Our pilot study finds that replacing selected token probabilities with coarse substitutes can also improve calibration, motivating us to further explore effective signals of model confidence. We introduce Divergent Token Confidence (DTC), a framework that estimates confidence by counting tokens at which two models strongly disagree during decoding. DTC identifies these divergent tokens using the Jensen-Shannon divergence between next-token distributions evaluated along the same reasoning trajectory. We find that their count is almost negatively associated with answer accuracy, thereby serving as a simple yet effective signal for uncertainty quantification. DTC supports both white-box and black-box evaluation using auxiliary models, without explicit training and affecting the generation process. Experiments across multiple model families and six mathematical benchmarks demonstrate improved calibration over probability-based and verbalized baselines. Under white-box evaluation, the count-only estimator achieves an average expected calibration error of 13.0%, compared with 32.7%-42.4% for standard full-sequence confidence methods. In black-box settings, it also improves calibration over the original verbalized scores. For example, mean expected calibration error falls from 32.1%-40.2% to 13.7%-16.3% on DeepSeek-V3.2. These findings provide new insights for improving reasoning uncertainty quantification in large language models. The code is released at this https URL.

---


### 452. [VISTA: Internalizing Collective Visual Experience via On-Policy Distillation for Active Multimodal Agents](https://arxiv.org/abs/2609.38086)

**<font color=#1a73e8>作者：</font>** Zheng Jiang, Houde Qian, Yiming Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active multimodal agents use visual tools to acquire task-relevant evidence while reasoning. Although reinforcement learning samples multiple interaction trajectories per input, outcome-based objectives primarily use the group to estimate scalar advantages, leaving complementary visual discoveries underused. We introduce VISTA, which internalizes collective visual experience through on-policy distillation by turning observations from same-input rollouts into shared supervision. Collective visual experience distillation (CVED) organizes these observations with their interaction context and aligns them with individual decisions, while heterogeneity-aware policy improvement (HAPI) reinforces successful trajectories and provides experience-guided distillation for unsuccessful attempts. An experience-conditioned teacher evaluates the student's sampled response prefixes, allowing discoveries from one trajectory to guide learning in another without replacing the student's original history or generating new target trajectories. The trained agent retains its visual tools and acts using its own interaction history. VISTA achieves the strongest average performance among the evaluated active multimodal agents of comparable size and consistently outperforms same-backbone training baselines across fine-grained perception and general reasoning tasks, demonstrating the value of collective experience for active multimodal learning.

---


### 453. [Mira: Memory-Efficient MoE Inference Using Adaptive Caching and Predictive Expert Staging](https://arxiv.org/abs/2609.38090)

**<font color=#1a73e8>作者：</font>** Sanjali Yadav, Bahar Asgari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models are a compelling architecture for scaling model capacity, making them especially attractive for deployment on resource-constrained, single-GPU systems. However, this benefit is difficult to realize because expert parameters dominate memory, and token-level routing is dynamic, unpredictable, and skewed. Prior work using offloading and caching remains fundamentally reactive, as systems wait for router outputs before moving experts, leading to inefficient cache utilization and an inability to overlap transfers with compute under tight VRAM budgets.
To address these challenges, we propose Mira, an algorithm-system co-design that enables high-capacity MoE inference on a single GPU. Mira shifts from a reactive to a proactive stance by coupling predictive expert management with a tailored quantization format. It introduces lightweight per-layer predictors that anticipate expert usage two layers ahead, enabling proactive prefetching. These predictions feed a two-tier HOT+STAGE GPU cache managed by token-level routing telemetry to retain frequently used experts while staging predicted ones. To minimize transfer overhead, Mira implements a custom compression for expert parameters, which reduces metadata and improves packing efficiency, while minimally degrading accuracy.
Mira is implemented as a fully integrated runtime that coordinates predictors, caching policies, and quantized transfers to maximize overlap between communication and compute. Our experiments show that Mira reduces expert-induced stalls. Compared against state-of-the-art baselines, Mira achieves a 5.71x speedup in average throughput on a memory-constrained GPU. It accelerates Time-to-First-Token by 11.71x and achieves a 3.84$x average speedup in beam search inference, demonstrating its effectiveness across diverse inference scenarios.

---


### 454. [Probe-Space Preconditioning for Fast and Stable Zero-Order Training](https://arxiv.org/abs/2609.38095)

**<font color=#1a73e8>作者：</font>** Francois Chaubard, Mykel J. Kochenderfer, Chris Ré  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backpropagation (BP) dominates deep learning but imposes a massive memory tax. For example, training OPT-30B with Adam requires $\approx$ 600GB of GPU memory (assuming batch size 8 and sequence length 2048). Alternatively, zero-order optimization (ZOO) trains in inference-mode (requiring only $\approx$ 60GB for the same model): no stored activations, no gradients, and no optimizer states. However, ZOO convergence has lagged behind BP. In this work, we evaluate two methods to close this gap. First, we show that reallocating training compute budget from many steps to large effective batch sizes with many perturbations (or probes) but fewer steps, allows 1SPSA (Spall, 1992) to outperform zero order methods like MeZO (Malladi et al., 2023) with less training compute. Next, we introduce 1.5-SPSA, adding a single "clean" forward-pass per step to 1SPSA to calculate a cheap diagonal preconditioner in probe-space, which improves convergence rate and convergence by down-weighting high curvature directions. Benchmarking on 6 post-training datasets on both Qwen3 and OPT model families, we show that 1.5-SPSA achieves State-of-the-Art results over previous ZOO solvers with much less optimization steps. For example, we train OPT-13B (for direct comparison to MeZO) and find 1.5-SPSA achieves +3.1% accuracy on SST-2 over both MeZO and BP in only 70 steps vs. MeZO's 100,000 steps. Finally, we combine an 8-bit-packing random generator, triton fused unpack/apply kernels, and distributed parallelism to achieve fast and stable training of models as large as OPT-30B in-place on commodity GPUs (e.g. A100).

---


### 455. [Tail-Influence Sampling for CVaR Policy Evaluation](https://arxiv.org/abs/2609.38096)

**<font color=#1a73e8>作者：</font>** Pauline Bourigault, Xiaotong Ji, Matthieu Zimmer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policies with similar mean returns can differ sharply in rare failures, yet estimating lower-tail conditional value-at-risk (CVaR) accurately can require many costly rollouts. When different conditional components of a stochastic workflow can be queried separately, we ask how to allocate a fixed evaluation budget to estimate a fixed policy's CVaR most accurately. We derive a tail influence for each queryable conditional law that aggregates how its uncertainty affects CVaR across every Bellman reuse. Its variance yields the fixed-design efficiency bound and the oracle Neyman allocation. Tail-Influence Sampling (TIS) estimates these influence scales from a pilot model and reallocates fresh queries toward kernels that matter most for the tail; a visitation-anchored variant protects against pilot underallocation. Under fixed dimension and a positive quantile margin, TIS attains oracle asymptotic variance and first-order MSE including pilot cost, while the anchored variant is within a factor two of the oracle. We also characterize an exact-grid regime in which tail- and mean-optimal allocations coincide. On CliffWalking, TIS reduces MSE by 41% versus learned occupancy and 76% versus complete rollouts at the same charged transition budget. In frozen language-model review workflows, anchored TIS beats an equally regularized mean-influence blend in 23 of 24 MMLU-Pro settings and reaches 2.4-3.4$\times$ lower MSE than rollouts on six-call FinQA reviews.

---


### 456. [NeuronEye: Query-Guided Visual Concept Activation for Vision-Language Reasoning](https://arxiv.org/abs/2609.38098)

**<font color=#1a73e8>作者：</font>** Ruiyu Yan, Bowen Chen, Shaowen Wan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current vision-language models (VLMs) encode visual information in dense hidden states where object identity, spatial layout, and local attributes are implicitly entangled rather than explicitly disentangled, limiting their ability to isolate and modulate the specific visual evidence required by a given language query. Inspired by sparse population coding and top-down modulation in biological vision, we introduce NeuronEye, a plug-in framework that constructs a sparse, concept-level neuron vocabulary from intermediate VLM representations and selectively activates query-relevant visual concepts during inference. NeuronEye decomposes vision-token states into an overcomplete sparse basis organized by concept-level clusters, uses the language query to activate relevant clusters and localize the patches where selected concepts are expressed, and injects the focused evidence back into vision tokens. A complementary suppression mechanism attenuates dominant perceptual directions to preserve weaker but relevant cues. All operations run in a single forward pass over a frozen VLM backbone. On Qwen2.5-VL-7B, NeuronEye raises CV-Bench overall accuracy by +3.1 with gains of +9.5 on Distance, and improves BLINK Multi-view by +8.3, with similar trends on LLaVA-1.6-7B. These results suggest that sparse neuron vocabularies can serve not only as post-hoc interpretability tools but also as active interfaces for concept-level visual reasoning.

---


### 457. [Explore Broadly, Reason Sharply: Push Small Models toward the Frontier via Sampling](https://arxiv.org/abs/2609.38104)

**<font color=#1a73e8>作者：</font>** Panagiotis Theodoropoulos, Nan Jiang, Xintong Duan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Power-sharpened sampling is an inference-time alternative to reinforcement-learning (RL) post-training for enhancing reasoning in large language models (LLMs). High-probability sequences are amplified under the base model without parameter updates or external rewards, avoiding the costly optimization and jagged generalization of RL. However, this approach faces a fundamental exploration--exploitation trade-off, as % strong sharpening restricts exploration, trapping samplers in plausible but incorrect reasoning trajectories, whereas weak sharpening leaves the answer distribution diffuse. To resolve this trade-off, we introduce \textbf{Parallel Power Tempering (PPT)}, instantiating power-sharpened LLM sampling via parallel tempering. Running multiple \emph{interacting} replicas in parallel at different sharpening levels allows lower-power replicas to explore diverse reasoning trajectories and higher-power chains to further exploit higher-likelihood responses favored by the sharpened target. Specifically, we tailor \method{} to inference-time sampling by mitigating a truncation bias, identified in prior power samplers, and investigate effective swap strategies under finite memory and compute budgets. Extensive experimentation shows that \method{} substantially improves single-chain power-sharpened sampling and outperforms RL-post-trained models, producing higher-quality reasoning traces and even achieving performance comparable to frontier models.

---


### 458. [Correct Answers, Invalid Traces: What Verifiable Grade-School Math Reveals About Chain-of-Thought Traces](https://arxiv.org/abs/2609.38107)

**<font color=#1a73e8>作者：</font>** Ratish Puduppully, Pranabendu Misra, Paarth Iyer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought traces are widely read as records of how models reach their answers, informing debugging, agent auditing, and claims about reasoning. Testing this interpretation is difficult because natural-language thinking traces are rarely mechanically verifiable. We revisit it in iGSM, a synthetic grade-school mathematics benchmark designed to study thinking traces and used to support claims of learned reasoning and planning. Crucially, iGSM exposes the exact quantities and dependencies that a correct solution should use, allowing generated traces to be checked programmatically step by step and enabling us to test whether correct answers are reliably accompanied by valid traces. We first evaluate models trained exclusively on valid, minimal traces. Answer correctness and trace validity nearly coincide in distribution but decouple out of distribution: on the hardest instances, 31.6% of correct answers have invalid traces, over half of which pass all syntactic and arithmetic checks but fail semantic dependency checks. We then intervene on trace supervision. Non-minimal training traces induce non-minimal outputs, while re-asking the same problem with a different query reveals computations inherited from the original query, weakening minimality as evidence of selective planning. Shuffling tokens in 10% of training trace sentences preserves near-clean accuracy even out of distribution despite no trace passing verification. Swapped training traces likewise retain high in-distribution accuracy. We discuss the implications of these findings for chain-of-thought monitoring and interpretation in the context of AI safety.

---


### 459. [Do LLM Agents Execute the Plans They Declare? From Planning-Mode Declaration to Pattern-Specific Execution](https://arxiv.org/abs/2609.38108)

**<font color=#1a73e8>作者：</font>** Subba Reddy Oota, Francisco Herrera, Jordi Cabot Sagrera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) enable agents to solve long-horizon tasks by generating a plan and then executing it in an environment. However, successful planning requires two distinct capabilities: selecting an appropriate plan for the task and executing it faithfully. Existing planner--executor systems can fail at either stage, while final task success alone cannot distinguish selection from execution failures. We therefore study the Plan Declaration--Execution Gap and introduce Planning-as-Routing, where an LLM declares one of four planning modes: Predefined, Sequential, Hierarchical, or Search, and a deterministic router dispatches the task to the corresponding pattern-specific executor. Across four benchmarks and three LLMs, we find three consistent patterns. First, generic Plan+ReAct often fails to preserve declared planning structure, especially for longer plans: across three benchmarks, only (22)--(45%) of trajectories preserve it, whereas pattern-specific executors enforce the intended structure. Second, planning-mode effectiveness varies across environments and models: Search performs best on ALFWorld, Hierarchical on SWE-bench, and the strongest pattern can vary across models within the same benchmark. Third, the largest gains come from execution: pattern-specific executors improve task success from (0.48) to (0.92) on ALFWorld and from (0.36) to (0.44) on SWE-bench Verified over Plan+ReAct. Current LLMs, however, do not reliably select the strongest mode for each task, although few-shot examples improve selection in some benchmark--model combinations. Overall, reliable agent planning requires both effective mode selection and faithful execution: routing substantially closes the execution gap, while task-specific mode selection remains open.

---


### 460. [From Routing Signals to Selective Review: Visual regrounding in MoE VLMs](https://arxiv.org/abs/2609.38111)

**<font color=#1a73e8>作者：</font>** Hongzhu Guo, Mohsen Fayyaz, Nanyun Peng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) may accept false visual premises, answering questions about a target object's color, count, location, or state even when it is absent. We call this reliability-critical behavior a target-absence grounding failure. Existing visual-grounding detectors primarily rely on generated responses, hidden states, or uncertainty measures. We present the first framework to leverage internal routing decisions in Mixture-of-Experts (MoE) VLMs to detect target absence before generation and guide selective correction. We extract target-token routing probabilities from Qwen3-VL-30B-A3B-Instruct and Gemma-4-26B-A4B-it, train a separate L2-regularized linear detector for each model, and use its predictions to selectively invoke a target-aware review prompt. Using routing alone, the Qwen and Gemma detectors achieve ROC-AUCs of 0.9988 and 0.9956 on GQA-Inpaint and retain 0.8095 and 0.7781 on the external OBER dataset, respectively. The resulting routing-gated policy improves end-to-end accuracy on GQA-Inpaint and OBER by +22.25% and +12.17% for Qwen, and by +13.42% and +1.39% for Gemma, without modifying model weights. Further analysis shows that the signal is localized to the target-object token, emerges in early MoE layers, and is distributed across partially substitutable experts. Although cross-dataset threshold shifts require recalibration, false-positive review causes limited harm overall, suggesting that intervention risk can be controlled through joint selection of the detector threshold and review prompt. Overall, we show that routing probabilities alone preserve actionable information about visual perception, allowing computation already produced by an MoE VLM to support low-cost detection and selective visual regrounding.

---


### 461. [VideoLoop: Looped Working Memory Against Semantic Thrashing in Long-Form Video Agents](https://arxiv.org/abs/2609.38119)

**<font color=#1a73e8>作者：</font>** Jinfa Huang, Jianming Xu, Jingyang Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-form video understanding requires multimodal agents to iteratively gather evidence over many reasoning steps. However, most existing agentic methods suffer from semantic thrashing: as append-only working memory grows, attention to key evidence collapses, and the agent loses access to what it has already found. First, we provide a structural argument showing that append-only memory can incorporate newly observed target evidence, but cannot remove accumulated noise or prevent ordered context growth without a rewrite operator. Second, motivated by this analysis, we propose VideoLoop, a multimodal agent with two coupled loops. The outer loop reasons over the video and the inner loop, after each step, retrieves artifacts from an unbounded filesystem of past observations and intermediate analysis, and rewrites a bounded working memory. Extensive experiments demonstrate the effectiveness of VideoLoop, which improves four popular LVLM backbones in a plug-and-play manner, with an average gain of 4.2% points over baseline on VideoMME (long). Further analysis of working memory suggests that VideoLoop mitigates semantic thrashing: on the hardest quarter of VideoMME (long) questions, a blind judge that reads only the agent's context answers 81.1% correctly, versus 60.9% for the append-only agent. With Gemini 3.1 Pro, VideoLoop reaches 88.3% on VideoMME (long), 88.8% on VideoMMMU, and 80.9% on LongVideoBench (long).

---


### 462. [WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms](https://arxiv.org/abs/2609.38121)

**<font color=#1a73e8>作者：</font>** Jiale Chen, Vage Egiazarian, Eldar Kurtić 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV cache memory and bandwidth costs grow with context length and batch size, which limits efficient long-context inference. To address this bottleneck, we introduce WUSH-KV for low-bit KV-cache quantization. It adapts WUSH, which constructs a data-aware transform from the second-order statistics of both factors in a matrix product to reduce quantization error. WUSH-KV uses calibration data to construct separate key and value transforms, with the value transform folded into the model weights and the key transform applied after RoPE. The transforms can be paired with clipped quantizers. For one such quantizer, QuEST INT, we show that, under mild assumptions, the WUSH transform is near-optimal. With this quantizer, WUSH-KV reduces layerwise reconstruction error and achieves the lowest end-to-end perplexity among other tested transforms. For end-to-end evaluation, we integrate WUSH-KV into SGLang using OSCAR-style percentile-clipped affine quantization. At 2-bit, WUSH-KV performs comparably to or outperforms the OSCAR transform across all evaluated models and downstream tasks.

---


### 463. [CLeaR: A Unified Framework for Resolving the Leakage-Degradation Dilemma in Style Transfer](https://arxiv.org/abs/2609.38136)

**<font color=#1a73e8>作者：</font>** Teng Zhou, Yunhao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Style transfer aims to render target content in the style of a reference image, but existing methods often suffer from content leakage, where objects, layouts, or semantics from the style reference appear in the generated output. Although prior data-driven and training-free methods can reduce leakage, they often face a leakage-degradation dilemma: stronger content suppression may weaken style fidelity, while richer style preservation may reintroduce unwanted reference content. We identify this dilemma across the full style-transfer pipeline, including feature separation, feature-space grounding, and diffusion generation. To address these issues, we propose CLeaR, a training-free framework for content-leakage-resistant style transfer. CLeaR first uses Orthogonal Subspace Projection to define content-reduced style targets in each vision foundation model (VFM) feature space. It then performs Ensemble Inversion, which optimizes a shared pixel-space style anchor satisfying style constraints across multiple VFMs. Finally, Energy-Guided Calibration maintains style alignment during diffusion sampling by steering the denoising trajectory toward the ensemble-defined style manifold. We further provide a theoretical analysis showing that the style-anchor estimation error decreases with the number of VFMs. Experiments on StyleBench demonstrate that CLeaR improves style alignment, reduces content leakage, and achieves better LLM-as-Judge evaluation compared with existing methods. The code is available at \href{this https URL}{this https URL}.

---


### 464. [LongHarness Bench: Stress-Testing Language Model Harnesses for Long-Context Reasoning](https://arxiv.org/abs/2609.38137)

**<font color=#1a73e8>作者：</font>** Quang Hieu Pham, Thuy Duong Nguyen, Jocelyn Qiaochu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-model (LM) harnesses enable LMs to operate effectively over long contexts using additional compute. However, existing long-context evaluations are insufficient for distinguishing modern harnesses, reflected by saturated accuracy across harnesses and largely similar evaluation costs. In this paper, we introduce a benchmark for evaluating both the effectiveness and efficiency of long-context harnesses. Our tasks require diverse retrieval strategies, including lexical search and semantic matching, together with strategic and adaptive reasoning over global and local context. Much of the context is semantically relevant but only a small subset is useful at each step, creating both a challenging search problem and different accuracy--cost tradeoffs across processing strategies. For example, one task requires identifying every person satisfying several conditions using evidence scattered across documents; strategically checking the most selective condition first can narrow the search before verifying the remaining conditions. We evaluate multiple families of frontier language models with four state-of-the-art harnesses. Our benchmarks remain challenging even for strong model--harness combinations: the best reaches 68\% macro-average accuracy across four evaluation suites. More importantly, we find that the same underlying model can exhibit markedly different efficiency under different harnesses. Our results establish efficiency as an important axis for long-context evaluation and provide a testbed for developing harnesses that process context strategically rather than exhaustively.

---


### 465. [Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE](https://arxiv.org/abs/2609.38140)

**<font color=#1a73e8>作者：</font>** Yu Xu, Yuxin Zhang, Xiao Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE), popularized by large language models, is a promising paradigm for scaling visual generative models. However, conventional token-wise MoE routes tokens independently within a homogeneous expert pool and regularizes expert usage toward uniformity, making it poorly matched to video data that is spatiotemporally redundant and semantically long-tailed. We show that existing visual MoEs fall into a uniformity trap: semantically under-organized routing, compounded by uniform expert-usage regularization, scatters coherent patches across disparate experts, causing routing fragmentation and structural distortion. To address this, we propose SplitMoE, a split-role sparse architecture that breaks the shackles of uniformity. To accommodate the inherent semantic imbalance, we explicitly bifurcate the expert pool into semantic experts and generic experts, with semantic experts capturing high-level semantic abstraction and generic experts preserving residual visual information and flexible generative capacity. Leveraging prototype-guided routing and pull-push regularization, SplitMoE enables tokens to cluster naturally by semantic attributes rather than arbitrary balancing constraints. Extensive results show that under an equivalent activated-parameter budget, SplitMoE outperforms traditional load-balanced MoEs in convergence speed, routing coherence, and video generation quality across standard benchmarks. By revealing an emergent coarse-to-fine denoising logic, SplitMoE provides the community with a modality-aware scaling path, serving as a critical reference for building large-scale video world models.

---


### 466. [AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation](https://arxiv.org/abs/2609.38142)

**<font color=#1a73e8>作者：</font>** Rishabh Agrawal, Hejie Cui, Shasha Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A small trainable advisor can steer a frozen language-model executor using natural-language advice. In addition to learning from task rewards, the advisor can use feedback from completed interactions to improve its advice. However, a plausible correction need not change execution, yet learning from such corrections can still affect the advisor's future decisions in other contexts. In a shared-parameter model, we prove that such corrections can limit learning if their targets favor useful advice less strongly than those of other corrections. Keeping them less often than the rest improves the model's eventual performance compared to learning from every correction. Motivated by this, our method, Advisor Self-Distillation (AdviSD), pairs outcome-based reinforcement learning with self-distillation from a feedback-conditioned copy of the advisor selectively. Reflection proposes corrections, and the advisor scores the same recorded executor response with and without its issued advice, using the magnitude of the difference to select decisions for supervision. This approach does not require executor likelihoods or additional executor rollouts. Experiments with Qwen3-8B advisors for Gemini and Claude show that AdviSD outperforms advisor-GRPO by 4.2-6.4 percentage points on BFCL-v3 and by 3.9-5.1 score points on EnvScaler. The trained advisors generalize to out-of-domain tasks and transfer across different executor versions and model families. AdviSD also beats matched-count random selection, supporting the value of its selection rule.

---


### 467. [Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI](https://arxiv.org/abs/2609.38143)

**<font color=#1a73e8>作者：</font>** Cheng Qian, Kunlun Zhu, Beibin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent performance depends on both reasoning ability and the environment in which it acts. We study test-time AI-for-AI, asking how a Builder can learn to construct better execution environments for a Target while both models' weights remain fixed. To make the Builder's experience reusable, we introduce Meta-Skill: principles specifying when support is needed and what resources to provide. The Builder learns these principles from Target's execution feedback on the development set, then uses the frozen skill bank to construct harnesses for unseen tasks. Across Harness-Bench and NewtonBench, full-bank meta-skills improve macro-average performance by 8.95 percentage points over no-skill construction, and 12.02 points over direct delivery of the same bank to the Target. These results highlight the value of translating experience into executable support. Gains when the same model serves both roles further suggest a path to system level self-improvement through learning to build better environments.

---


### 468. [Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning](https://arxiv.org/abs/2609.38147)

**<font color=#1a73e8>作者：</font>** Paras Dahal, Anton Bakhtin, Taco Cohen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agents take on longer and more complex problems, controlling the execution becomes a task in its own right. Each step in the run brings new control choices, like which partial work to build on, whether to start fresh, or when to stop. We introduce agentic meta-reasoning, an inference-time harness that makes these choices an explicit and structured reasoning process. Workers carry out the task-level computation, while a controller consolidates what the run has established, explores next options, assesses what each option is worth under the remaining budget, and dispatches the chosen work with context drawn from persistent memory. Between decisions the controller carries only a compact account of the run rather than replaying its full history. Our baselines span production coding agents and research harnesses, together with a Direct Control Agent using the same workers and compute budget allowance. On ProgramBench, which tests long-horizon agentic capability through program reconstruction, meta-reasoning achieves 71.5% with GPT-5.5 against 58.0% for Codex; with Opus 4.8 it achieves 67.2% against 65.5% for Claude Code. On the other benchmarks, spanning abstract reasoning, multi-domain long-horizon reasoning, and proof generation, it gains between 3.6 and 4.2 points over direct control, averaged across three frontier models. It keeps improving over the tested budget ranges where direct control plateaus, though its overhead can hurt at small budgets. Artifact-graph analysis reveals more reuse of earlier work, higher coverage of correct solutions in most settings, and nonuniform gains in final selection. These results indicate that spending computation on structured control becomes more important as agents scale to longer runs.

---


### 469. [Pretraining Latent Information Feedback Transformers with Teacher Supervision](https://arxiv.org/abs/2609.38149)

**<font color=#1a73e8>作者：</font>** Dor Tirosh, Ido Amos, Mor Geva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer language models (LMs) are feed-forward: deep-layer representations are never fed back to shallower layers, and the only pathway for information to flow downward across generation steps is the decoded token. This narrow channel forces models to recompute intermediate results and to discard alternative continuations. In this work, we remove this bottleneck during pretraining, introducing the LIFT (Latent Information Feedback Transformer) architecture and training method which enable LMs to propagate state across generation. We achieve this by turning recurrent-state learning into a teacher-forced prediction problem: each input token is paired with an information-dense state, derived from the next-token distribution of an off-the-shelf pretrained LM. The model, extended with a small number of additional parameters, is then trained to predict both the next token and the next state. As the input states are precomputed, pretraining remains fully parallel across positions. At inference, the model's own predicted states are fed back, with a minor computational overhead that decreases with model size. Experiments with pretrained models ranging from 135M to 1B parameters show that LIFT consistently outperforms standard Transformers and baselines on language modeling, downstream reasoning tasks, and procedural tasks under token-matched budget, while being on par with or ahead of compute-matched Transformers. Moreover, a controlled study on a state-tracking task shows that a tiny LIFT outperforms same-size Transformers trained on 8x more data, even when trained with the states of a Transformer that fails the task. Overall, we show that LMs can learn to exploit deep-to-shallow feedback during pretraining via scalable teacher supervision.

---


### 470. [A Spectral Theory of Distortion in LLM Graph Reconstruction: Sharp Bounds and Empirical Characterization](https://arxiv.org/abs/2609.38161)

**<font color=#1a73e8>作者：</font>** Jianru Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluations of graph reconstruction by language models typically report a single aggregate distance between the original and the reconstructed graph. We prove that for the Wasserstein distance between Laplacian spectra such a summary is bracketed by two edge counts, the net change in edge number from below and the symmetric difference from above, each scaled by $2/n$ where $n$ is the number of vertices. The bracket is sharp: its two ends coincide exactly when the reconstruction only adds edges or only deletes them, and on that class the distance is a rescaled edge count that says nothing about which edges changed. When the ends differ, the residual between the distance and the lower end is positive only if the reconstruction both invented and lost edges, which turns it into a certificate of mixed editing computable from the reported summaries alone. We characterize these regimes in 135 reconstructions produced by three open-weight models over 45 synthetic graphs. Seventy-seven outputs are one-sided and 29 mixed outputs have $X > 0$, including cases where edge count is exactly preserved while nineteen edges were simultaneously invented and lost. The three models differ in editing policy, ranging from copying the input to attempting completion at the cost of large hallucination volume, a distinction that aggregate distortion does not reveal.

---


### 471. [LeapQuant: Efficient Linear Attention with Accurate Recurrent State Quantization](https://arxiv.org/abs/2609.38166)

**<font color=#1a73e8>作者：</font>** Yi Pan, Haocheng Xi, Kan Zhu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent LLMs increasingly adopt hybrid designs that replace standard attention with linear attention, such as Gated DeltaNet (GDN) and Kimi Delta Attention (KDA). Although they compress the context into a fixed-size recurrent state and substantially reduce the cost of long-context processing, repeatedly reading and updating that state remains a major inference bottleneck. Quantization offers a natural way to reduce this cost, but can significantly degrade model quality, due to the accumulation of rounding errors and the presence of outlier rows and columns in the state. To address these challenges, we propose LeapQuant, a training-free method that achieves near-lossless performance under 8-bit recurrent-state quantization. First, to mitigate error accumulation, we propose per-window quantization, which leaps over a window of tokens and quantizes the state only once at its end. Within a window, outputs are computed from the fixed low-bit state together with high-precision buffered updates. Second, to reduce the error introduced by each quantization, LeapQuant retains the state's largest outliers as a few high-precision Compensator Tokens, which share the update path of real tokens. We then smooth the remaining residual before quantization to further reduce the error. Comprehensive experiments across the Qwen, Kimi, and GLM model families show that LeapQuant substantially reduces memory and compute costs during inference. With accuracy comparable to the FP32 baseline, it achieves average speedups of 2.05--3.70$\times$ at the kernel level and 1.47$\times$ for end-to-end inference on NVIDIA B200, RTX PRO 6000, and RTX 5090 GPUs.

---


### 472. [STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization](https://arxiv.org/abs/2609.38169)

**<font color=#1a73e8>作者：</font>** Bingchen Yao, Haobo Xu, Haokun Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear attention replaces growing KV caches with fixed-size recurrent states, yet these persistent states can become a substantial memory bottleneck under concurrent serving. Directly quantizing recurrent states to low precision often leads to severe accuracy degradation, as quantization errors propagate through successive state updates. We discover that the impact of these errors depends on two complementary dimensions: temporally, errors in long-lived memory can persist across many decoding steps; spatially, errors in different key rows affect model outputs differently, while state magnitudes vary substantially along both rows and columns. Motivated by these observations, we propose STEPQuant, a spatial-temporal post-training quantization framework for Delta-rule recurrent states. STEPQuant allocates precision according to error magnitude and memory lifetime, and jointly fits key-row and value-column scales based on state distributions and key-row impact on output error. Experiments on Qwen3.8-27B and Kimi-Linear-48B-A3B-Instruct across both long- and short-generation benchmarks show that STEPQuant closely matches FP32-state accuracy under a nominal 6-bit budget and outperforms uniform INT8 in its 4-bit configuration. Integrated into SGLang with optimized GPU kernels, 6-bit STEPQuant achieves over 5x recurrent-state compression and reduces total serving memory by up to 68.7%. Our code is available at this https URL.

---


### 473. [Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering](https://arxiv.org/abs/2609.38177)

**<font color=#1a73e8>作者：</font>** Jaewoo Jung, Hyeonseo Yu, Honggyu An 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning about the 3D world from multi-view images remains a fundamental challenge for Multimodal Large Language Models (MLLMs). While modern MLLMs handle single-image inputs effectively, they struggle to integrate evidence across viewpoints into a coherent 3D understanding. A growing body of work attempts to close this gap by injecting 3D awareness into MLLMs, either by boosting fine-grained pixel-level cross-view correspondence or by fusing features from 3D geometry foundation models, yet a substantial gap to human reasoning persists. In this work, we revisit human spatial reasoning, which suggests that rather than relying on fine-grained geometry cues, humans roughly identify common objects across views, infer the relative geometry between viewpoints, and assemble a coarse 3D layout of the scene. Inspired by this process, we introduce Imagine3D-LLM, an MLLM that learns to assemble a similar compact 3D representation of the scene and conditions its answer on this representation. Concretely, we append a small set of learnable summary tokens after the image tokens, decode them into a compact 3D Gaussian Splatting representation supervised by a photometric reconstruction loss, and train jointly with the standard next-token prediction objective. Notably, although only the summary tokens receive direct reconstruction supervision, this objective also induces stronger cross-frame correspondence within the LLM's underlying image features, suggesting that learning to reconstruct propagates 3D-aware signals throughout the model. As a result, Imagine3D-LLM consistently outperforms prior approaches across multiple spatial reasoning and 3D understanding benchmarks, suggesting that imagining the scene can be more effective than being told its pixel-wise geometry.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 474. [GenoTrace: Inheritable Watermarks for Genome Foundation Model Distillation](https://arxiv.org/abs/2609.35881)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Guang Yang, Fengchen Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Can a genome model retain a detectable record of the synthetic sequences used to train it? We study watermark inheritance through distillation with GenoTrace, a codon-aware extension of green-list watermarking. Two token-level factors modulate the teacher's generation bias using codon position and organism-specific codon usage. The resulting sequences train a smaller student, whose outputs are audited without an active watermark processor. In a three-seed GenomeOcean-500M-to-100M experiment, the joint configuration achieves a mean audit score of 17.88 and 94.5% detection at a fixed threshold. It retains 49.0% detection after key-aware token substitution, compared with 0% for the available single-seed plain-watermark comparator, and 47.0% after combined mechanism-targeted nucleotide edits. Additional experiments establish inherited signal across five organism-conditioned datasets and teacher-student size ratios up to 40. Component ablations and computational sequence-quality assays reveal distinct operating points for detection strength and coding coverage. GenoTrace provides a practical token-level construction and an empirical account of how genomic structure shapes inherited watermark signals. The findings concern shared-tokenizer distillation and the tested editing procedures, with calibration and biological utility treated as separate evaluation requirements.

---


### 475. [Agentic Commerce Bench: Measuring Fraud Detection for Agents That Spend Money](https://arxiv.org/abs/2609.35886)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ankit Srivastava, Debjyoti Paul  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents now hold spend authority and settle payments without per-action human confirmation. The resulting loss is often not a security failure: a counterparty with the correct domain, the correct settlement address and a genuinely delivered service can charge more than it should, and no check keyed on identity will see it. We present three artefacts for measuring and reducing that loss. First, a taxonomy of agentic commerce fraud that separates five observation levels (agent reasoning, wire, settlement rail, counterparty, principal) from the request-level and history-level evidence available at each, and records which levels can observe which attacks. Second, Agentic Commerce Bench (ACB), a benchmark of twenty fraud classes generated from production aggregates, 1,647 catalogued service operations and 1,068 settlements, of which six involve a counterparty that is exactly who it claims to be. Third, gordonguard, an open-source detector stack and offline harness with which an operator can audit an agent configuration, replay hostile counterparties without an account, and run the same detectors inline. Calibrating to a stated false-positive budget on clean training traffic gives a 6.5% clean flag rate, replicated across three independent generations, and leaves eight of twenty classes no better than chance. On the four classes a reasoning layer can observe, a widely used agent security scanner run over its jailbreak-detection panel scores zero on all four, while correctly scoring 1.0 on a jailbreak supplied as a control. A measured median payment of $0.007 places a hard constraint on deployment: one human review costs 143 times the value of the payment it examines.

---


### 476. [TORQUE: Optimizing What (not) to Quantize Before and After Rotation](https://arxiv.org/abs/2609.36032)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ran Ben Basat, Michael Mitzenmacher, Shay Vargaftik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uniform random rotations are an effective preprocessing step for quantization: they make normalized coordinate distributions approximately Gaussian, enabling the use of codebooks optimized offline. We introduce TORQUE, a framework that improves on previous quantization works that use random rotations by jointly optimizing how many and which coordinates to preserve at high precision both before and after rotation, under a fixed overall expected bit budget.
Intuitively, before rotation, preserving large input coordinates at high precision can reduce overall error by preventing the rotation from spreading their values across many coordinates. Likewise, after rotation, preserving a small fraction of the largest-magnitude coordinates at high precision allows the remaining values to be quantized more accurately using codebooks optimized offline for the resulting truncated Gaussian distribution.
We derive a quantization error upper bound and prove that top-$k$ pre-rotation retention minimizes it for each $k$. This reduces the search over coordinate subsets to an optimization over $k$, enabling a fast optimizer that uses offline codebooks and parallel parameter selection for practical implementation. We demonstrate an improved tradeoff between reconstruction accuracy and storage cost through numerical evaluation under the Gaussian model and experiments on nearest-neighbor retrieval, KV-cache compression, and activation compression.

---


### 477. [ABC: Advantage-Based Control Variates for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2609.36058)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hsiao-Ru Pan, Florent Draye, Bernhard Schölkopf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in reinforcement learning with verifiable rewards (RLVR) has highlighted the effectiveness of simple critic-free policy-gradient methods such as Group Relative Policy Optimization (GRPO). In contrast, actor-critic methods rely on learned value functions whose approximation error can introduce bias through commonly used advantage estimators such as temporal-difference error. Motivated by this observation, we revisit trajectory-level control variates through an advantage-value formulation, which we call Advantage-Based Control Variates (ABC). This formulation reveals that the covariance structure is closely related to the return decomposition used in Direct Advantage Estimation (DAE). Finally, we combine ABC with DAE into a single actor-critic algorithm and evaluate it in an offline-to-online RLVR setting, where the critic is first trained on previously collected trajectories and adapted during online learning. On mathematical reasoning tasks, ABC achieves performance competitive with GRPO using substantially fewer online optimization steps.

---


### 478. [PHASE: A Physiology-Guided Hierarchical Foundation Model for Intracranial EEG](https://arxiv.org/abs/2609.36087)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yipeng Zhang, Chenda Duan, Yuanyi Ding 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinicians and neuroscientists have long analyzed intracranial electroencephalography (iEEG) through directly measurable physiological characteristics, which carry much of the information that downstream tasks depend on. Recent iEEG foundation models learn by reconstructing or predicting their inputs, which leaves the retention of these characteristics implicit. They are also evaluated mainly on cognitive decoding and a narrow clinical task, i.e., seizure detection. On a broad, clinically relevant benchmark such as Omni-iEEG, they remain below task-specific models when used frozen. We introduce PHASE, a physiology-guided foundation model that makes these characteristics explicit learning targets, pairing them with masked latent prediction in a temporal stage (PHASE-T) within each channel and a spatiotemporal stage (PHASE-ST) across synchronized channels. PHASE is pretrained on heterogeneous recordings from 222 participants at nine clinical sites. On all five Omni-iEEG clinical tasks, frozen PHASE-T outperforms every evaluated foundation model by up to 31\%, and fine-tuned PHASE-T surpasses the task-specific models, setting a new state of the art. PHASE-T benefits from physiological supervision, outperforming variants trained with latent prediction alone or auxiliary waveform reconstruction on every task in matched ablations. PHASE-T generalizes to unseen institutions, outperforming the compared models with few or no local labels. PHASE-ST further improves seizure-onset-zone identification over PHASE-T and, when frozen, decodes sound volume and pitch on BrainTreebank better than published models. Beyond task performance, PHASE learns to encapsulate the physiological characteristics clinicians recognize, from seizure onset and its propagation to anatomical region identity, even though its pretraining contains no ictal recordings or anatomical labels.

---


### 479. [LoopICL: Looping a single transformer block to solve tabular tasks](https://arxiv.org/abs/2609.36108)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Amir Rezaei Balef, Katharina Eggensperger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models using in-context learning have recently surpassed gradient-boosted trees on predictive tabular tasks. However, recent mechanistic insights suggest that parameters in these models are largely redundant. We introduce LoopICL, a looped transformer whose core design decouples parameter count from computational depth. LoopICL consists of a single block, processing data through two coupled streams: a cell stream capturing per-cell feature representations and a row stream capturing in-context example representations, jointly refined through within-column and cross-column attention. During pre-training, we vary loop counts, allowing the block to be unrolled for a varying number of iterations at test-time and use a learned exit-gate to automatically exit. In its standard setting, LoopICL performs competitively with TabICLv2 on TabArena and TALENT at the same computational cost (FLOPs), while using nearly 90% fewer parameters. Furthermore, its recurrent design enables users to also trade off inference cost and performance, providing a resource-aware TFM.

---


### 480. [Physical Cross-Modal Masked Autoencoding for Seismic-to-Well Representation Learning](https://arxiv.org/abs/2609.36193)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Meher Gajula, Keyla Gonzalez, Ben Lasscock 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning from scientific measurements often requires aligning modalities with different spatial support and resolution. Subsurface characterization is an extreme dense-sparse problem in which 3D seismic provides volumetric but indirect measurements and well logs provide high-resolution 1D measurements at sparse borehole locations. We introduce a physically grounded cross-modal masked autoencoder (CM-MAE) for seismic-to-well representation learning. The model jointly tokenizes seismic volumes and well-log depth patches, embeds both modalities in continuous physical coordinates using four-axis rotary position embeddings, and reconstructs masked targets with a cross-modal decoder. Sparse Mixture-of-Experts layers provide modality-specific capacity while dense attention allows information exchange between modalities. Pretraining uses 23 seismic volumes covering approximately 178,000 square km across U.S. offshore and onshore basins, together with approximately 92,000 wells. Matched-mask ablations show strongly asymmetric information flow. Seismic context improves held-out well-log reconstruction by 9.73%, while well-log context improves seismic reconstruction by 0.65%. We evaluate seismic-only pseudo-log predictions against independent interpreter-drawn salt-geobody masks to determine whether they contain geologic signal. Across offshore U.S. surveys, compressional-slowness-derived salt scores reach an AUROC of 0.910. In onshore basins, predicted compressional slowness preserves formation-scale structure and partial relative organization in an unseen survey despite calibration drift. CM-MAE learns useful seismic-to-well representations under extreme modality asymmetry, although absolute pseudo-log calibration remains survey-dependent.

---


### 481. [Representational and Functional Robustness to Electrode Montages in EEG Foundation Models](https://arxiv.org/abs/2609.36288)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jakob Steglich, Justus Meyer zu Bexten, Shakiba Moradi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models (EEG-FMs) are intended to generalize across different datasets by learning representations that, ideally, are invariant to dataset-specific EEG configurations such as electrode montages. However, EEG-FMs that accept different montages as input do not guarantee that representations and predictions remain stable across different electrode configurations, especially outside the training setting. In this work, we investigate the effects of different electrode montages through a joint functional and representational analysis of four EEG foundation models selected to span distinct montage-handling designs. We evaluate embeddings on cross-subject resting-state eyes-open/closed and within-subject motor-imagery classification under spatially informed channel reduction. Functional robustness is tested through the generalizability of linear probes across channel counts, while representational robustness is assessed through within-subject similarity and preservation of between-subject geometry. The four models show distinct robustness profiles, and the two axes dissociate: large changes in embedding similarity need not come with comparable probe degradation, and stable embeddings can still lose downstream performance. Comparing two readouts of the same encoder further shows that aggregation, not the encoder alone, determines functional robustness: pooling into anatomically aligned regions degrades less than a learned global readout, despite being montage-invariant by construction. Montage robustness is therefore a joint property of the encoder and its aggregation, and characterizing it requires both a representational and a functional axis. Input compatibility alone is evidence for neither.

---


### 482. [Towards an AI Software Factory for Data Systems](https://arxiv.org/abs/2609.36323)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Anna Pavlenko, Bogdan Crivat, Brandon Haynes 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-assisted coding tools deliver significant acceleration of coding, but only limited impact across the end-to-end software development lifecycle (SDLC)--an Amdahl's law effect!
In this paper, we discuss our progress towards building an AI SW Factory that accelerates all the stages of SDLC-Targeting, Coding, Reviewing, and Ops. The AI SW Factory produces a metadata exhaust that enables self-improvement by fine-tuning model weights and updating our World Model (a rich data substrate).
We focus on Data Systems and the important class of Evolutionary Coding Tasks (i.e., those with a measurable objective to hill-climb) and report on 1) scaled deployments at Microsoft (tens of repositories) leading to 3x engineering efficiency above agentic coding and up to 22x token efficiency, and 2) several open challenges.

---


### 483. [ThuRunel: Dynamic Decoupling for Structured Advisory Dialogue](https://arxiv.org/abs/2609.36340)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuyan Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-stakes advisory domains such as medical aesthetics, legal consultation, and educational planning exhibit a two-phase structure. The early phase requires empathetic elicitation and emotional support, and the late phase requires authoritative specialist judgment. Neither fully automated agents nor human junior consultants adequately address this structure at scale. We formalize the core design challenge as dynamic decoupling, asking how an AI advisory agent should decide what to ask, when to stop, what to resolve autonomously, and what to forward to the specialist. We present ThuRunel, an advisory agent combining a finite-state belief management framework, a chain-of-thought teacher synthesis protocol, and learned generation adapters. Against eleven baselines, ThuRunel achieves consistent improvements in elicitation completeness and specialist brief quality. ThuRunel is publicly deployed as a bilingual web application in which the same decoupling decisions operate from the client's side, grounded in a curated knowledge base that cites its sources in every answer.

---


### 484. [TTMark: Pairwise Distortion-Free Watermarking Beyond Single-Token Entropy](https://arxiv.org/abs/2609.36372)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ruibo Chen, Zhengmian Hu, Donghang Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Distortion-free watermarking enables reliable attribution of machine-generated text while preserving output distribution. However, existing methods operate independently on each generated token, making their detection capability fundamentally constrained by the entropy of the next-token distribution. We present Tandem Token WaterMark (TTMARK), a general pairwise watermarking framework that extends distortion-free watermarking from individual tokens to adjacent token pairs. By watermarking the joint distribution of consecutive tokens, TTMARK enlarges the effective watermarking alphabet from V to $V^2$, allowing the detector to exploit both token entropy and conditional entropy while preserving distortion-freeness over the joint distribution. We further introduce a branch-isolating concatenated tandem generation algorithm that efficiently constructs the joint distribution in a single forward pass. Theoretically, we show that pairwise watermarking achieves better expected detection strength in low-entropy regimes. Extensive experiments across multiple language models, datasets, and three representative distortion-free watermarking schemes demonstrate that TTMARK consistently improves detectability without degrading generation quality, while also improving robustness to edits and substantially enhancing localized watermark detection.

---


### 485. [FinRT: Distilling Adaptive Red-Teaming Strategies into Reusable Adversarial Generators in Consumer Finance](https://arxiv.org/abs/2609.36474)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rikhiya Ghosh, Himanshu Kumar, Sriram Venkatapathy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In regulated industries like consumer finance, seemingly harmless user queries can exploit large language model vulnerabilities, triggering safety failures and pushing responses dangerously close to policy limits. Existing automated red-teaming methods trade off attack effectiveness against generation cost, while treating coverage, severity, and diversity as incidental rather than joint objectives. We introduce FinRT, a structured framework that builds reusable adversarial prompt generators from adaptive red-teaming strategies. Across the six victim models in consumer finance, FinRT substantially outperforms adaptive search baselines while amortizing target-facing attack generation into a reusable generator. FinRT nearly doubles the attack success rate over the adaptive baseline Rainbow Teaming (32.9% vs. 17.2%), increases maximum adversarial severity by 33%, and preserves comparable intra-policy-domain semantic diversity to iterative search methods. Our method achieves high cross-model transferability while exhibiting distinct victim-family specialization patterns.

---


### 486. [CrossTimeEdit: A Decade-Spanning Cross-View Dataset and Reward-Guided Editing for Historical Street-View Generation](https://arxiv.org/abs/2609.36616)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hanwen Lu, Jun He, Mingjia Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Historical street-view imagery records urban evolution, but uneven coverage leaves substantial gaps in historical records. Generating plausible past appearances requires restoring changed structures while preserving persistent scene content. We construct VIGOR-his, a decade-spanning cross-view dataset containing 43,653 location-level quadruplets across 11 cities on three continents. Its automated pipeline performs spatial pairing, consistency screening, change classification, and the generation and validation of satellite-based change descriptions and local editing instructions. Based on VIGOR-his, we propose CrossTimeEdit, a model that reformulates historical street-view generation as editing, using recent street views to constrain viewpoint and unchanged appearance and temporal satellite differences as change evidence. Starting from FLUX.2 [Klein] 4B, we train CrossTimeEdit through supervised fine-tuning (SFT) followed by online reinforcement learning (RL). We design three street-view editing criteria, namely Instruction Alignment (IA), Background Preservation (BP), and Quality and Physical Plausibility (QP), as both RL reward dimensions and evaluation metrics. We optimize this multi-reward objective using Within Group Relative Policy Optimization for flow-matching models (Flow-GRPO) with Group reward-Decoupled Normalization Policy Optimization (GDPO), which normalizes each reward dimension before aggregation. CrossTimeEdit improves overall performance across the three editing criteria by 17.12\% over the pretrained baseline and outperforms cross-view generation models in scene consistency, visual realism, and perceptual quality. The implementation code, dataset, and model weights are available at this https URL.

---


### 487. [SemPSG: A Semantic Channel-Aware Foundation Model for Polysomnography Analysis](https://arxiv.org/abs/2609.36619)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junyu Chen, Chenxi Liu, Shiqin Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Polysomnography (PSG) integrates multiple physiological signals to provide a comprehensive characterization of human sleep, yet its heterogeneous channel configurations across centers pose substantial challenges for transferable representation learning. Existing foundation models mainly focus on physiological modeling or temporal learning, while channel identity is often treated as a fixed structural index, overlooking the physiological semantics encoded by signal modality and reference configuration. To this end, we propose SemPSG, a Semantic channel-aware foundation model for heterogeneous PSG analysis. SemPSG explicitly represents the physiological semantics of channel identity and incorporates them into both signal representation learning and channel aggregation, enabling flexible modeling across diverse data configurations. Specifically, a semantic-conditioned time-series encoder captures signal-specific temporal dynamics and cross-signal interactions, while a multi-view image encoder extracts complementary time-frequency and morphological patterns from the same physiological recordings. We evaluate SemPSG on sleep and health-related tasks, including sleep staging, sleep-disorder breathing analysis, disease prediction, cognition and emotion recognition, and demographic estimation. Extensive experiments demonstrate consistent improvements over both general-purpose time series foundation models and PSG-specific foundation models, together with generalization across heterogeneous datasets across diverse channel configurations.

---


### 488. [Scheduling Recursive Reasoning in Looped Transformers](https://arxiv.org/abs/2609.36653)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Boyuan Wang, Chengyao Yu, Jiaxi Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent reasoning models have attracted growing attention for scaling test-time computation, typically by iteratively refining latent states with shared parameters. However, these models apply each learned update with a fixed unit scale, which can be conservative when updates make persistent progress and overly aggressive when they fluctuate, limiting the benefit of additional loops. To understand how the scale should vary along the trajectory, we first analyze the sensitivity of terminal loss to recurrent update scale. We show that its temporal average admits an exact decomposition into persistent-progress and centered-fluctuation contributions. Based on this, we introduce the Trajectory Adaptive Progress-Fluctuation Scheduler (TAPS), which tracks their balance across recurrent updates and adapts the step size online. Theoretically, we establish sufficient conditions under which TAPS reduces expected terminal loss and reaches a target quality in fewer recurrent loops. Empirically, we show that TAPS improves terminal accuracy across structured reasoning tasks without retraining. By further incorporating the progress-fluctuation principle into training, TAPS yields additional accuracy gains with up to 1.56 times wall-clock speedup at matched baseline accuracy. The broad applicability of TAPS is supported by its effectiveness across diverse recurrent architectures and inference strategies. Together, these results establish update scale as complementary control axis of recurrent inference alongside architecture and depth.

---


### 489. [Constitutional adapters: Inference-time interventions for misalignment and misuse](https://arxiv.org/abs/2609.36657)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Adam S. Lowet, Mark Kurzeja  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training models to act in accordance with an explicitly defined set of principles, or "constitution," has shown promise as a robust and transparent mechanism for AI alignment. However, the generality and flexibility of such methods remain unclear. Here, we show that constitution-consistent behavior can be distilled from synthetic corpora into lightweight objects (low-rank adapters and steering vectors). Despite never seeing a harmful request or jailbreak during training, such objects increase jailbreak defense success and measured alignment -- particularly at long context lengths and against multi-turn attacks, where they outperform both prompted and steered baselines. Subtracting control-trained from constitution-trained objects further accentuates these effects, yielding defenses we call "constitutional adapters" (CAs). CAs can be trained on a base model, transferred zero-shot to its post-trained checkpoint, and scaled at inference time to predictably trade off defense for benign compliance. Taken together, these results recommend CAs as a lightweight, portable, and tunable lever for mitigating misalignment and misuse in API deployments.

---


### 490. [RAE-PPG: Duration-Grounded Retain-and-Extend Pretraining for PPG Foundation Models](https://arxiv.org/abs/2609.36794)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Suyeong Lee, Hochang Lee, Seokyong Sheem 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Signal features derived from photoplethysmography (PPG) require different signal durations to characterize. Existing PPG foundation models treat duration as a pretraining or evaluation condition rather than using the different durations required by PPG features to organize self-supervision. We hypothesize that self-supervision should expand with signal duration, allowing a single encoder to progressively acquire additional features while preserving and reusing earlier learning. We introduce Retain-and-Extend PPG (RAE-PPG), which trains a single Transformer encoder successively on 10 s, 30 s, and 240 s inputs, adding supervision for signal features supported by each longer observation. The encoder is partitioned into duration-specific parameter groups, allowing later stages to reuse earlier groups while updating only the group assigned to the current stage. Selected earlier targets are reused to supervise later stages, encouraging the corresponding features to remain accessible in longer-input representations. Direct decoding from the final encoder shows that earlier features remain recoverable from longer-input representations, while later-stage features show higher mean decoding performance at their introduction durations. Controlled comparisons further show that prior-stage learning provides a better basis for learning newly introduced features at both transitions. Across 18 tasks from eight datasets, the final frozen encoder achieves the best observed score on 12 tasks compared with five existing PPG foundation models.

---


### 491. [pikit: A Composable Toolkit for Indirect Prompt Injection Research and Evaluation](https://arxiv.org/abs/2609.36817)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zonghao Ying, Xiangfan Wu, Bo Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection embeds malicious instructions within external content retrieved by LLM-based agents, altering target behavior without user authorization. We introduce pikit, a research toolkit designed to systematically evaluate these threats across three core dimensions: attacks (13 methods), channels (16 carriers across text and file modes), and defenses (9 prevention strategies and 3 offline detection baselines). Built on a decorator-based registry, pikit enables seamless extension of custom components without modifying core code, while a unified craft() API composes arbitrary attacks and channels in a single call. We evaluated the toolkit on the pi coding agent powered by an anonymized LLM in a production-like environment. Benchmarking 9 prevention strategies against high-risk attacks yields a 71.8\% relative reduction in attack success rate, with few\_shot\_warning and instruction\_hierarchy providing the strongest protection. Offline detection baselines achieve perfect precision but low recall, demonstrating that heuristic detectors complement rather than replace prompt-level defenses. To ensure reproducibility, each run automatically logs full prompts, agent event traces, session transcripts, and verdict records. Our code is available at this https URL.

---


### 492. [Where the Model Changes Its Mind: Hindsight-Divergence Localization for Efficient Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2609.36864)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fanchao Chen, Hengyu Fu, Shivaram Venkataraman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-relative methods for reinforcement learning with verifiable rewards (RLVR) learn from differences in rollout outcomes. Independently sampling complete trajectories is costly and does not explicitly explore the decision space at critical positions. Feedback on a completed trajectory can reveal which earlier choices the policy reconsiders, suggesting where to sample alternative continuations. We introduce Hindsight-Divergence Localization (HDL), which uses hindsight-induced changes in token log-likelihoods to select branch points. HDL generates a small number of complete root trajectories and fills each training group with continuations from the selected positions under the original task context. Each continuation reuses its root prefix and contributes policy updates only through its newly generated suffix, reducing generation cost while focusing additional exploration and learning on decisions after branching. Experiments with three models across math, code, and agent tasks show gains in both rollout efficiency and task performance. Compared with GRPO at matched group sizes and training steps, HDL yields up to a 2.5$\times$ reduction in generated tokens and a 1.8$\times$ speedup in rollout wall-clock time. Despite this reduced generation budget, HDL improves performance across all three domains, with gains of up to 12.5 points on agent tasks.

---


### 493. [Architecture Alignment With Sparse Priors in Tabular Foundation Models](https://arxiv.org/abs/2609.36883)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianqi Zhao, Tianyi Zhuang, Shuo Duan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) are increasingly popular because they deliver strong predictions on new datasets through in-context learning, without task-specific training or extensive tuning. Yet released TFMs differ simultaneously in their pretraining priors, architectures, and objectives, obscuring their respective inductive biases. We therefore examine one concrete capability: irrelevant-feature suppression. Across synthetic tasks and real-world datasets, adding null features causes substantially greater predictive degradation in the row-token model TabDPT, whereas the cell-token alternating-axis model TabPFN v2 and other TFMs remain comparatively stable. This gap motivates us to ask whether architecture contributes to irrelevant-feature suppression. Because released TFMs remain confounded by other design choices, we train streamlined row-token and alternating-axis transformers under identical sparse-to-dense linear priors. Exact Bayes analysis shows that sparse prediction requires context-dependent feature gating, whereas the dense endpoint requires only uniform feature weighting. Consistent with this distinction, the alternating-axis model is substantially closer to the Bayesian optimal predictor on sparse tasks, while the architecture gap becomes negligible on dense tasks; almost all of the sparse gap arises from linear coefficient-estimation error. Finally, in both the controlled model and frozen TabPFN v2, we examine the effect of interventions on the feature-attention outputs on the linear coefficients, finding evidence of task-dependent selective routing of computation through feature-indexed pathways. Together, these results support architecture-prior alignment: preserving an addressable feature axis provides an inductive bias for task-adaptive relevance inference. Code is available at this https URL.

---


### 494. [Visual Parallel Search: Learning to Search High-Resolution Images with Parallel Tile Inspection and Adaptive Zoom](https://arxiv.org/abs/2609.37002)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xijia Tao, Yihua Teng, Xinyu Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution visual question answering often fails because a multimodal model does not acquire the small, spatially localized evidence needed to answer a question. Sequential zooming can recover detail, but it asks the main model to choose a region before obtaining a reliable overview. We introduce VPS, a visual parallel-search framework in which a main agent first invokes grid_search to inspect image tiles in parallel with question-conditioned sub-agents, and then adaptively invokes zoom_in PSisual Parallel Search improves mean accuracy over dedicated zoom-only search in 14 of 15 same-model comparisons, with gains up to 8.0 points and especially strong improvements for smaller main models. ZoomBench retains an approximately 3.2-point gain at every tested size. We further develop a supervision pipeline with hint-free verification and a paired role-specific GRPO surrogate for learning the controller and tile-reader roles. SFT improves observed accuracy on all five benchmark splits, including a 4.17-point gain on HR-Bench 4K. Role-specific RL further reshapes search behavior: main-only RL reduces mean tool use from 2.65 to 2.11 with similar pass@1 in an internal four-response evaluation, while external accuracy changes are mixed. Joint training reveals an asymmetry between local evidence reading and global search control. Together, these results support VPS as an effective inference-time scaffold and a trainable decomposition for visual evidence acquisition.

---


### 495. [Language as the Interface: Foundation-Model Contrastive Learning Links Transcriptomes and Electrophysiology](https://arxiv.org/abs/2609.37024)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junbo Shen, Jinying Gao, Bo Lei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Integrating transcriptomic and electrophysiological data is essential for building multimodal foundation models for neuroscience. Patch-seq provides paired measurements of gene expression and intrinsic electrophysiology from the same neuron, establishing a basis for training cross-modal models. Here we introduce LangPatch, a foundation-model-based contrastive learning framework that uses paired Patch-seq data to align pretrained GenePT representations with electrophysiological phenotypes through a language-based interface. Gene descriptions and verbalized electrophysiological profiles are embedded by the same frozen text encoder. A context adapter and projection modules connect the modalities through paired contrastive learning. Across mouse visual, mouse motor, and human cortical cohorts, LangPatch achieves the highest mean transcriptome-to-electrophysiology prediction correlation among the evaluated foundation-model and representation-learning methods. It also improves held-out cross-modal alignment in the two mouse cohorts (FOSCTTM 0.107/0.135 vs. 0.208/0.222 for JAMIE, an existing cross-modal Patch-seq imputation method). It predicts transcriptomic family, type, cortical layer, and marker-gene expression from electrophysiology, exceeding other baselines on most endpoints. More importantly, the method transfers across brain areas and species: a model trained on mouse visual cortex predicts electrophysiology in motor cortex with approximately 70% correlation retention and in human cortex with 47% (58% on acute-slice recordings). Together, these results demonstrate alignment between molecular and functional representations of neurons, providing a building block for multimodal foundation models in neuroscience.

---


### 496. [MotionInsight: Diagnosing Object Motion Deficiencies in Generated Videos](https://arxiv.org/abs/2609.37030)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiahao Zhan, Yongrui Ma, Qunliang Xing 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress in video generation models, they still exhibit obvious motion deficiencies, often manifested as incorrect object motion. However, most existing video quality evaluations focus on aesthetic quality or text-video alignment. To address this gap, we study object-centric motion fidelity assessment, evaluating target objects along object consistency, motion continuity, and physical plausibility. To achieve this, we first introduce VidMotion, a diagnostic dataset of 6,879 videos with designated moving objects and fine-grained annotations including dimension-wise scores and failure causes. We further propose MotionInsight, a diagnostic evaluator that shifts assessment from implicit RGB-frame observation to explicit motion-space diagnosis. By constructing motion-aware representations, MotionInsight makes subtle motion deficiencies more observable. We also introduce motion-specific rewards during GRPO to transform observed motion into a diagnostic assessment. Experiments demonstrate that MotionInsight provides an effective basis for diagnosing object motion deficiencies, producing human-aligned scores along three dimensions and grounded explanations.

---


### 497. [Beyond Semantic Narrowing: Robust and Efficient LLM Watermarking with Hamming Neighborhoods](https://arxiv.org/abs/2609.37218)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zewen Sun, Tongyang Zhao, Liyao Xiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Semantic watermarking improves robustness against watermark removal attacks by embedding detectable signals into sentence-level representations. However, existing watermarking methods typically impose watermark-specific semantic preferences on generated sentences without explicitly accounting for the highly non-uniform and context-dependent semantic preference of LLM generation. When these two preferences are poorly aligned, many natural continuations become incompatible with the watermark, causing semantic narrowing: reduced semantic freedom, increased resampling cost, and potential degradation on tasks with strict semantic requirements. To alleviate this problem, we propose HammingMark, which uses the semantic hash of the preceding sentence as a dynamic center and accepts candidates whose hashes fall within its Hamming neighborhood. Defining watermark validity over a Hamming neighborhood in compact hash space retains a larger fraction of naturally likely semantic continuations. The coarse many-to-one hash mapping further allows diverse semantic realizations to remain watermark-valid. Experiments on C4 and BookSum show that HammingMark achieves strong robustness, high detectability, and near-unwatermarked generation quality, requiring only 2.2 sampled candidates per accepted sentence,a 72.8% reduction compared with the most sampling-efficient existing method. On more complex tasks with strict semantic constraints, HammingMark achieves the highest detection rates with the highest or tied-highest ROUGE-L scores, demonstrating its effectiveness in balancing watermark detectability and generation quality under constrained generation settings.

---


### 498. [Loss-Guided Pretraining Data Selection for Time-Series Foundation Models](https://arxiv.org/abs/2609.37255)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yike Li, Shaoxu Song, Jianmin Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) are pretrained on heterogeneous collections containing billions of observations, yet their training windows are typically sampled without estimating whether they provide useful learning signal. We introduce a static data-selection framework that scores each window with a reference forecaster and retains an intermediate interval within every source dataset. Specifically, we connect forecasting loss to optimization difficulty by showing that normalized squared loss controls the per-sample gradient norm under a local Jacobian condition. We then define a reference loss score and apply dataset-stratified selection to preserve the diversity of samples. Across various TSFM architectures, our method outperforms random selection by an absolute margin and even improves both relative MASE and CRPS over full-data pretraining by retaining fewer candidate pretraining windows. Further analyses show strong cross-scale and cross-architecture score correlations, indicating that a small reference model can often select data for larger targets, provided that the reference and target share compatible difficulty orderings.

---


### 499. [Efficiently Approximating Attention Is Hard](https://arxiv.org/abs/2609.37261)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lukas Haverbeck, Carmen Amo Alonso, Andres Felipe Posada-Moreno 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Softmax attention is ubiquitous in modern machine learning, but its quadratic scaling with sequence length makes it costly. To reduce this cost, attention is often approximated with fast algorithms, which incur error but can still perform well in practice and on some inputs. At the same time, the growing diversity of attention applications makes approximation guarantees that do not depend on particular input structure a compelling target. For such uniform guarantees over all inputs, known runtime lower bounds rule out fast algorithms for near-exact attention, but leave open the practically important regime: is there an efficient algorithm with even a modest uniform approximation guarantee? We answer this question negatively. Under standard complexity-theoretic assumptions, no truly subquadratic algorithm can approximate attention with any nontrivial additive or relative guarantee uniformly over all inputs. This impossibility holds in the mildest parameter regime for which known algorithms do not already achieve strong approximation guarantees in near-linear time, and extends to practically relevant relaxations: even after polynomial preprocessing of the KV cache, no efficient algorithm can obtain a nontrivial uniform approximation guarantee, or identify a small set of keys receiving substantial attention under sparsity. Overall, our results settle the computational limits of uniform attention approximation.

---


### 500. [ReMem: Rethinking Perception and Memory in Long-Context Recommendation Agents](https://arxiv.org/abs/2609.37311)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haohao Qu, Yongcheng Jing, Chun Hin Chan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent Recommendation Agents (RecAgents) offer a promising alternative by shifting recommendation to an active, user-side paradigm, where generative agents autonomously perceive external platforms, reason over user preferences, and execute decisions. However, existing RecAgents still suffer from two critical limitations: brittle item perception based on noisy and heterogeneous item pages, and inefficient long-context reasoning over extended user histories and multi-step interaction traces. To address these challenges, we propose a novel recommendation agent framework, termed as ReMem, that combines OCR-based multimodal perception with time-evolving dynamic memory. Instead of parsing raw HTML, ReMem observes item pages through screenshots and extracts structured multimodal information via an OCR tool, enabling a more humanoid and platform-agnostic perception mechanism. To support long-horizon preference modeling, ReMem further introduces a chunk-wise sequential memory update strategy, where the agent selectively maintains a fixed-size memory of informative historical interactions while processing arbitrarily long contexts with linear inference complexity and bounded context length. This design allows the agent to preserve evolving user preferences without relying on external memory modules or disrupting the standard autoregressive generation process. To enhance the dynamic memory instruction, we further develop a multi-memory GRPO variant, which propagates the final-answer advantage to all intermediate conversations that contribute to the final response. Extensive experiments on three datasets demonstrate that ReMem consistently outperforms state-of-the-art baselines, achieving an average improvement of 5.16\% across three recommendation agent tasks, namely searching, ranking, and judging.

---


> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
