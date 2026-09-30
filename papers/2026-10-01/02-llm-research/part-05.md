# 🧠 大模型相关研究 | 2026年10月01日

> 本类共 **515** 篇论文：已确认 **473** 篇，待复核 **42** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 201. [DSPO: Diversity-aware Subjective Policy Optimization for Robust Emotional Reasoning](https://arxiv.org/abs/2609.36775)

**<font color=#1a73e8>作者：</font>** Cheng Ye, Weidong Chen, Bingyan Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning has significantly advanced the complex reasoning capabilities of MLLMs. However, prevailing RL algorithms suffer a severe failure in emotion reasoning tasks. These methods heavily rely on deterministic hard-label supervision and point-wise isolated evaluation, creating a fundamental gap with the inherently subjective and continuously distributed nature of human emotions. Furthermore, unlike explicit physical objects, emotional states are deeply implicit within visual cues. This abstract nature exacerbates visual hallucinations in MLLMs, leading to plausible yet ungrounded emotional evidence. To address these limitations, we propose Diversity-Aware Subjective Policy Optimization (DSPO), a reinforcement learning framework that jointly promotes subjective affective coverage and visual grounding. First, we construct a context-grounded emotional distribution prior in the VAD space by combining the lexical prior of the annotated emotion with image-specific contextual information. Based on this prior, we introduce a Distribution-Aligned Emotional Diversity Reward (DEDR), which measures the leave-one-out marginal contribution of each candidate emotion within a rollout. DEDR rewards candidates whose inclusion brings the predicted affective set closer to the context-grounded prior, thereby preserving plausible subjective interpretations without encouraging unconstrained dispersion. We further develop Counterfactual Visual Intervention Gating (CVIG), which masks the visual region highlighted in the reasoning process and uses the resulting candidate-wise probability changes to reduce the weights of interpretations unsupported by visual evidence. Extensive experiments demonstrate that DSPO achieves state-of-the-art performance across multiple public benchmarks, especially on the cross-domain performance, i.e., improving +10.8\% on average cross-domain accuracy than EMO-R3.

---


### 202. [Code4Scene: Benchmarking Coding Agents for Constructing and Editing 3D Scenes](https://arxiv.org/abs/2609.36777)

**<font color=#1a73e8>作者：</font>** Xiaokang Ye, Siddhant Hitesh Mantri, Zimeng Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier coding agents can now write and execute code that authors 3D environments, but whether they reliably understand 3D structure and precisely control scene state remains unclear. The generated 3D scene is a persistent, executable artifact: a convincing render can hide incorrect spatial relations, intersecting objects, or unintended modifications. We introduce Code4Scene, a benchmark of 190 Unreal Engine cases built from human-assembled scenes that evaluates coding agents on two complementary settings under a shared execution interface. Construction tests scene-level spatial reasoning from open-ended language specifications, where many realizations are valid; editing tests precise control of scene state, where the agent must recover the target scene from reference images while preserving everything else. Rather than scoring code or rendered views, Code4Scene evaluates the generated engine-native scene for task fulfillment, artifact integrity, and static physical validity, with edits additionally compared against withheld ground truth. Across 14 coding-agent configurations on the 95-case public set, construction and editing performance are strongly correlated but not interchangeable (Spearman $\rho = 0.78$): Claude Fable 5.1 leads construction, Gemini 3.8 Flash leads editing, and GPT-6 Astra narrowly leads overall. Spatial Composition is the weakest construction category for every agent, while editing remains imprecise: the best Repair F1 is only 0.527, and 35.8% of edits that fully recover the target still introduce unintended changes elsewhere in the scene. These results expose a gap between plausible 3D generation and reliable spatial reasoning and state control.

---


### 203. [Decoding Affective Nuances: Enhancing MLLMs via Hierarchical Emotion Reasoning and Contrastive Discriminative Pruning](https://arxiv.org/abs/2609.36782)

**<font color=#1a73e8>作者：</font>** Cheng Ye, Weidong Chen, Zhaobo Qi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While multimodal large language models (MLLMs) have demonstrated exceptional capabilities in objective understanding tasks, their performance in affective reasoning still falls significantly short of human standards. We attribute it to a central capability gap: MLLMs are difficult to reliably distinguish semantically proximal emotions based on fine-grained visual evidence, which could be decoupled as two limitations: 1) Insufficient Attribution. The global reasoning paradigm of conventional MLLMs severely dilutes fine-grained emotion cues, where subtle emotional states are usually implicitly encoded, thereby generating emotional misjudgments in complex scenarios. 2) Insufficient Discrimination. Existing methods could only identify regions generally associated with emotions, which fails to distinguish discriminative regions between semantically similar emotions, leading to ambiguous emotion judgements. To overcome these limitations, we present a training-free inference-time optimization framework, named Decoding Affective Nuances (DAN). Specifically, we propose a Hierarchical Emotional Reasoning Chain (HERC) that enhances the insufficient attribution by harmonizing fine-grained scene/object-level cues and performing a soft-gated reasoning. Furthermore, to discriminate between semantically proximal emotions, we design a Contrastive Discriminative Visual Pruning (CDVP), which isolates discriminative visual tokens to reason the final emotion category by computing the absolute discrepancy between the attention distributions of similar emotions. Performances on several benchmarks demonstrate that DAN significantly improves discrimination for affective nuances without consuming additional training resources, especially achieving +10.47% improvements with Qwen3-VL-8B-Instruct on WebEmo25 dataset that contains 25 fine-grained emotion categories.

---


### 204. [Harnessing Large Language Models to Compile Task-Relevant Context into Bayesian Optimisation](https://arxiv.org/abs/2609.36788)

**<font color=#1a73e8>作者：</font>** Zhongwei Yu, Sourabh Roy, Bin Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Incorporating rich task-relevant context, such as domain knowledge and external observations, is a key capability yet remains challenging for Bayesian optimisation (BO). Recently, practitioners have started to use large language models (LLMs) to generate and execute BO programs through coding harnesses. In such emerging practices, the posterior belief is shaped not only by Bayesian inference but also by LLM-generated model and data artefacts, offering a flexible route for task context to enter BO as executable code. To study whether and how LLMs can be harnessed to compile diverse contextual signals for BO, we formulate LLM-compiled BO as generalised-context decision making. We propose HarBO, a BO-specialised harness that compiles generalised context into the core artefacts of standard BO through a validated multi-stage workflow. Our theory analyses the regret under imperfect compilation and the effect of adding new context. Across synthetic functions and real-world benchmarks, we find that LLM harnesses can effectively compile context into standard BO, achieving competitive performance with specialised LLM-embedding-based and direct LLM-in-the-loop BO methods. General coding harnesses can be effective in familiar domains such as hyperparameter optimisation, but fall short in unfamiliar, context-rich domains. Together, these results establish LLM harnesses as a promising, but not automatically reliable, route for making rich task context usable in BO.

---


### 205. [GitHarness: Git Init Your Harness Working Memory for Perpetual User Requirements](https://arxiv.org/abs/2609.36789)

**<font color=#1a73e8>作者：</font>** Zhibang Yang, Xinke Jiang, Yuxuan Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-based agents increasingly collaborate with users on long-horizon tasks, accumulating evidence, code, and drafts through extensive search, reasoning, and execution. As users inspect these results, they may supply missing information requirement completion, introduce new requirements requirement elicitation, or revise existing ones requirement shift. These changes often affect only part of the accumulated work, yet agents may carry forward obsolete information or turn local revisions into global rewrites. Existing approaches clarify current intent without determining how prior work should change, or reuse execution histories under a fixed objective. We address this gap by formulating dynamic-requirement collaboration as joint requirement tracking and local update. We introduce GitHarness, a pluggable Git-style framework that organizes requirement states and their corresponding harness work states into a branchable version history. A trainable Git Agent resolves requirement changes and selects a semantically compatible historical state. A unified version interface then restores that state and creates a new branch, enabling the underlying harness to exclude obsolete information, inherit compatible work, and focus execution on affected parts. The Git Agent is trained through interface-level black-box reinforcement learning, with downstream harnesses and task-execution models kept fixed. We also construct MTAgentBench, a verifier-preserving benchmark covering mathematical reasoning, text-to-SQL, agentic search, software engineering, and research synthesis. Experiments demonstrate strong task performance alongside effective requirement tracking, preservation of valid work, and efficient execution.

---


### 206. [Seeing What Should Be Heard: Diagnosing and Repairing Cross-Modal Shortcuts in Omni-Modal LLMs](https://arxiv.org/abs/2609.36798)

**<font color=#1a73e8>作者：</font>** Yueran Ma, Ronghao Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models (LLMs) are expected to answer a question using the modality it explicitly refers to. However, existing training paradigms rarely verify whether models actually follow this modality, because multimodal inputs from the same sample often provide redundant evidence for the same answer. In this work, we uncover a pervasive cross-modal shortcut in omni-modal LLMs: when asked an audio-related question, models rely on the image as much as on the audio, and sometimes even more. To systematically diagnose this behavior, we introduce the Factorized Modality Diagnostic, which independently swaps audio and images between samples to isolate each modality's causal contribution. Across two model families in different settings, we find that this shortcut persists throughout supervised fine-tuning and reinforcement learning post-training, while judge-based RL may further amplify such reliance on irrelevant visual information. Based on this finding, we propose DMC-Repair, which trains models on the same kind of cross-modal swapped samples while assigning supervision according to the modality specified by the question. This prevents models from exploiting the spurious correspondence between modalities within the same clip. Experiments demonstrate that DMC-Repair reduces the image-induced share of the answer effect by 59.9%, effectively suppressing the cross-modal shortcut without compromising audio-question answering performance. The reduction in shortcut reliance generalizes across two model families and zero-shot to an unseen dataset and an unseen benchmark, and persists through subsequent post-training. Code is available at this https URL.

---


### 207. [AI as a Compiler: Compiling Triton kernels without the Triton compiler](https://arxiv.org/abs/2609.36800)

**<font color=#1a73e8>作者：</font>** François Costa, Charly Castes, Thomas Bourgeat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compiler backends are expensive to build and maintain as programming models, workloads, and accelerators evolve. We investigate whether large language models can replace the conventional optimizing and lowering pipeline, a process that we call AI lowering. We study AI lowering from Triton to NVIDIA PTX: an LLM agent translates Triton kernels directly into PTX. We build an environment that evaluates candidate PTX, and an agentic harness in which an LLM translates Triton kernels into PTX. Across twelve common kernels on Ada, Hopper, and Blackwell GPUs and ten kernels from recent ML papers, AI lowering achieves 0.83x-3.34x the performance of autotuned Triton. The largest gains come from transformations that Triton's lowering pipeline does not perform, such as decoding packed binary weights directly into Tensor Core operands (3.34x on BitDelta), assigning each thread a complete softmax row in tensor memory (1.37x on FlashAttention), and reusing overlapping convolution windows (up to 2.23x). These results rely on a robust evaluation harness with comprehensive verification support. We build on Volta, an existing PTX verifier, and substantially extend it to support modern GPU architectures by introducing support for Blackwell's tcgen05 Tensor Core interface. This requires modeling three architectural features: managed tensor memory, descriptor-based operand layouts, and asynchronous execution coordinated through commits, waits, memory barriers, and proxy fences. We discuss the challenges involved in formalizing them, as well as the current limitations. Our results suggest an emerging future in which AI compilers replace custom-written intermediate representations and checkers, reducing the time and engineering effort required to bring up software for new general-purpose and custom chips.

---


### 208. [EasyPPO: Stabilizing the Critic Is Key](https://arxiv.org/abs/2609.36802)

**<font color=#1a73e8>作者：</font>** Xuanyi Zhou, Qiuyang Mang, Huanzhi Mao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A key strength of Proximal Policy Optimization (PPO) is its learned critic, which uses historical trajectories collected during reinforcement learning to estimate expected returns and reduce policy-gradient variance. However, we find that the critic is also a major source of instability in reinforcement learning for large language models (LLMs). We identify two critic failure modes that destabilize PPO. First, filtering truncated rollouts from both actor and critic shifts the policy objective to reward conditioned on completion, allowing truncation to increase even as conditional reward improves. Second, heterogeneous return noise can cause high-variance prompts to dominate critic updates in finite batches. We introduce EasyPPO to address these failures. Actor-only overlong filtering trains the critic on returns from both completed and truncated rollouts. Noise-normalized critic regression weights each prompt's critic loss by the inverse standard deviation of its sampled returns, balancing noise contributions across prompts. Moderately smaller critic mini-batches confine outlier influence to fewer rollouts during gradient clipping. Across continuous-reward coding on FrontierCS, binary-reward mathematical reasoning on AIME24, and multi-turn search on Search-R1, EasyPPO remains stable throughout the full training horizon and consistently outperforms vanilla PPO, VAPO, and HL-Gauss PPO. Its best validation scores show relative gains of 14.89%, 2.28%, and 9.47% over PPO, respectively.

---


### 209. [VAA-CSEC: Vote-guided Advantage Allocation for Chinese Semantic Error Correction](https://arxiv.org/abs/2609.36804)

**<font color=#1a73e8>作者：</font>** Yitong Han, Nankai Lin, Juan Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chinese Semantic Error Correction (CSEC) targets semantic errors in Chinese text, which are typically more subtle and complex than spelling and grammatical errors but remain relatively underexplored. Existing LLM-based approaches face two recurring obstacles in this task: over-correction, and unclear interaction between Chain-of-Thought (CoT) reasoning and self-consistency decoding, such that the benefits brought by CoT cannot be reliably transferred to final corrections. We propose Vote-guided Advantage Allocation for CSEC (VAA-CSEC), a multi-stage framework that combines CoT distillation, Supervised Fine-Tuning (SFT), Reinforcement Learning (RL) and self-consistency decoding. During RL, we design a task-specific reward function that directly aligned with the minimal-editing principle of CSEC. We further introduce Group-Level Relative Policy Optimization (GLPO), which reallocates GRPO advantages according to the margin between individual rollout rewards and the vote-aggregated group reward, aligning the RL training objective with the self-consistency objective used at inference time. Experiments on CSED-C and NaSGEC-Exam show that VAA-CSEC outperforms all LLM-based baselines on CSED-C with an F0.5 of 47.72%, achieves the highest recall of 42.15% among all methods, and establishes a new state of the art of 41.55% F0.5 on NaSGEC-Exam.

---


### 210. [UpliftMem: Learning Set-Level Uplift for Agent Memory Retrieval](https://arxiv.org/abs/2609.36805)

**<font color=#1a73e8>作者：</font>** Mengkun Liang, Haoran Qiang, Guannan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents reuse external memory to guide new tasks, but effective retrieval requires learning which memory sets improve execution. Such learning relies on costly outcome feedback: ordinary retrieval observes only executed sets, while evaluating alternatives requires additional rollouts. We introduce \textsc{UpliftMem}, which learns memory retrieval from set-level execution uplift relative to the same executor without memory. A theoretical analysis of how retrieval preferences restrict feedback coverage motivates targeted probing of alternative memory sets. Probe selection follows an expected value of sample information (EVSI) criterion, derived in closed form under a correlated Gaussian model, to allocate limited training rollouts according to their expected improvement in local retrieval decisions. The shared scorer is trained with a frozen executor and selects memory sets without test-time probes. Across ALFWorld, WebShop, and BigCodeBench, \textsc{UpliftMem} achieves the best success rates among evaluated baselines on the main evaluation sets. Controlled fixed-store and matched probe budget evaluations further demonstrate improved memory-use decisions and more effective use of execution feedback.

---


### 211. [RESCUE: Repairing Language Model Errors to Sparse Circuits via Reinforcement Learning](https://arxiv.org/abs/2609.36813)

**<font color=#1a73e8>作者：</font>** Chuanpu Liu, Miao Yu, Yikai Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit strong general capabilities that mechanistic interpretability has attributed to sparse computational circuits. However, existing circuit studies emphasize preserving functionality or explaining safety, leaving the mechanisms underlying failures across a broader range of tasks largely unexplored. Extending circuit analysis from abilities to errors, we explore the perspective that such failures may likewise arise from erroneous internal computations and that targeted tuning of the corresponding parameters can correct such errors while largely preserving other capabilities. Motivated by this insight, we introduce RESCUE (Reasoning-Error Sparse-Circuit Uncovering and Editing), a framework that localizes error-associated circuits and surgically repairs them for performance enhancement. General tasks typically involve multi-step reasoning and long-form generation, where early deviations can cause prefixes to drift from supervised references, leading SFT-based mask optimization to overlook circuits involved in generation-time errors. RESCUE therefore refines these masks through reinforcement learning with multiple masked-model rollouts, improving their relevance to observed task failures. Finally, RESCUE introduces a pruning technique and precisely fine-tunes error circuits to correct task failures, thereby translating error localization into a sparse and targeted model update. We validate RESCUE on heterogeneous repair sets across two domains: (1) mathematical reasoning, identifying a math error circuit of 1.40% density whose repair raises accuracy from 6.0% to 75.5%; and (2) medical QA, where a similarly compact 1.44% circuit improves repair-set accuracy from 0% to 81%. Our code is available at: this https URL.

---


### 212. [Towards Better Training Signal: Advantage Clipped Policy Optimization](https://arxiv.org/abs/2609.36816)

**<font color=#1a73e8>作者：</font>** Ruichuan Huang, Jinghan Liu, Congliang Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a cornerstone for improving the reasoning capabilities of large language models (LLMs), but the need for on-policy data substantially limits training efficiency. Reusing off-policy data through importance sampling (IS) can improve efficiency but introduce considerable instability. Hence, algorithms such as PPO and GRPO widely adopt IS-ratio clipping to stabilize training. However, training stability and gradient estimate are mainly determined by the product of IS ratio and advantage. To further stabilize training, we propose ACPO, which clips the product of the IS ratio and the advantage, leading to more stable gradient estimates. We also establish a connection between ACPO and gradient clipping in policy mirror descent (PMD), which is a standard technique to stabilize optimization process, and prove the convergence of clipped-PMD under the standard RL setting. Experiments on widely used mathematical reasoning benchmarks show that ACPO consistently outperforms PPO and GRPO in both accuracy and training efficiency, delivering 4-6 percentage points gains on standard math benchmarks, with Qwen3-8B+PPO. Hence, ACPO is a practical and effective alternative to conventional IS-ratio clipping for RL post-training of LLMs.

---


### 213. [CorrGRPO: Correlation-Normalized GRPO for Multi-Reward Learning](https://arxiv.org/abs/2609.36820)

**<font color=#1a73e8>作者：</font>** Wenbin Hu, Huihao Jing, Haochen Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) is widely used to train reasoning language models, where it computes advantages by centering and normalizing rewards across rollouts of the same prompt. For multiple rewards, GRPO sums the reward components and normalizes the total reward by its within-group standard deviation. The corresponding variance equals the sum of all pairwise reward covariances. For a fixed centered reward, larger aggregate covariance produces smaller advantages, and vice versa, allowing update magnitudes to adapt to reward dependence. However, correlated rewards with large scales can dominate this normalization and suppress signals from smaller-scale rewards. We propose Correlation-Normalized GRPO (CorrGRPO), which normalizes pairwise covariances into Pearson correlation coefficients. CorrGRPO keeps the centered total reward unchanged while balancing the influence of differently scaled rewards on the correlation-based normalization. This allows advantage magnitudes to adapt to reward correlations without the normalization being dominated by large-scale reward components. We compare CorrGRPO with GRPO and other variants on code generation, tool calling, and agent security, using models ranging from 0.5B to 8B parameters. These tasks all involve multiple rewards that can improve together or present tradeoffs. Results show improvements across three domains, including code generation, tool calling, and agent security. Our code is available at this https URL.

---


### 214. [Learning via Self-Consistency for Diffusion-based Video Reasoning](https://arxiv.org/abs/2609.36826)

**<font color=#1a73e8>作者：</font>** Zhenghao Ni, Weimin Qiu, Meng Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models have demonstrated emerging zero-shot capabilities for visual reasoning, perception, and other vision tasks. However, diffusion-based video generation is inherently stochastic, while many downstream vision tasks are deterministic. Motivated by the effectiveness of self-consistency in chain-of-thought reasoning for large language models, we investigate whether self-consistency can similarly improve diffusion-based video reasoning. We first introduce a training-free test-time scaling method that samples multiple video generations and aggregates their predictions through self-consistency. Specifically, we aggregate extracted paths, locations, or masks from multiple rollouts into a consensus prediction. To reduce the inference overhead of multi-rollout generation, we read out predictions early in the denoising trajectory, which preserves consensus quality while reducing denoising steps by more than half. We further propose Rejection Fine-Tuning (RFT) to distill consensus predictions into the video generation model. The resulting model internalizes the benefit of multi-sample consensus and requires only a single generation at inference time, while substantially outperforming the original model. Experiments on three tasks, including maze solving, visual search, and referring segmentation, show that both our self-consistency inference and consensus distillation dramatically improve video-based perception and reasoning, without requiring ground-truth videos or task-specific verification. For visual search, self-consistency raises task accuracy from 48.4% for a single generation to 99.0%. The distilled model retains much of the consensus benefit with a single rollout. For 4-by-4 maze solving, consensus-based training improves the single-generation strict success rate from 72.0% to 84.0% with the same inference latency.

---


### 215. [Calibrate the Decisions That Change the Future: On-Policy Post-Training Quantization for Multimodal Large Language Models](https://arxiv.org/abs/2609.36828)

**<font color=#1a73e8>作者：</font>** Wenxiao Fan, Jingling Fu, Lichen Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) lowers deployment cost for multimodal large language models, but calibration typically reconstructs fixed sequences with local objectives. This overlooks autoregressive feedback: a quantization-induced token change redirects the prefix and changes future states. Yet on-policy coverage alone is insufficient because many decision mismatches barely affect future generation. We propose OnPTQ, an on-policy framework that calibrates on trajectories visited by the current quantized policy. On shared prefixes, OnPTQ identifies quantization-eroded boundaries, evaluates competing tokens through short counterfactual rollouts, and combines current discrepancy with branch consequence into a Decision--Consequence risk. The risk prioritizes critical states, while context anchoring and trajectory refresh preserve multimodal behavior and keep calibration aligned with the updated policy. We further derive a Decision--Consequence bound linking behavioral deviation to current policy discrepancy and action-conditioned future-value span. Across vision--language and omni-modal Qwen models under multiple low-bit settings, OnPTQ improves downstream performance and yields fewer correctness flips against the corresponding Dense/FP16 references, without changing the deployed inference graph.

---


### 216. [The Default Trap: Rethinking Plan Evaluation in Tool-Using LLM Agents](https://arxiv.org/abs/2609.36829)

**<font color=#1a73e8>作者：</font>** Xueqi Li, Jingjie Ning, Yibo Kong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An executor can respond strongly to a change in a supplied plan's priority while showing a small change in the same information-selection probability when a default-aligned whole plan is removed. We call the risk of interpreting the latter as weak responsiveness to alternative priorities the default trap. We compare paired plans that prioritize different information targets with a shared no-plan reference. An accounting identity relates these distinct behavioral contrasts. Across 3,200 decision windows on 160 selected Retail, Airline, and AgentDojo tasks, switching priorities strongly redirects two models' choices, while the two plan-versus-default contrasts differ. In 2,160 additional windows, reversing account-list order shifts default target selection by 63.3-98.3 percentage points; priority-switching effects remain 96.7-100.0 points in either order. A separate 3,240-window component study finds strong control under single priority sentences, with effects of additional text varying by group and direction. Finally, 1,080 full-task episodes yield observed success differences of -19.4 to +8.3 points relative to no plan. All Retail and Airline success intervals include zero; AgentDojo results describe four fixed application worlds. These findings support joint reporting of priority responsiveness, presentation-dependent defaults, and task success and cost.

---


### 217. [Where Does Staleness Accumulate? Pool Aware Effective Staleness Control for Asynchronous RL in LLM Post-Training](https://arxiv.org/abs/2609.36830)

**<font color=#1a73e8>作者：</font>** Chenliang Li, Neiwen Ling, Zijun Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fully asynchronous reinforcement learning (RL) improves resource utilization in large language model post-training by overlapping rollout generation with policy optimization, but it also introduces policy lag as trajectories are generated and queued while the trainer continues to update. We study how this lag accumulates over a trajectory's lifetime and how it can be controlled without sacrificing the wall-clock benefits of asynchronous execution. We decompose trajectory staleness into Generation Staleness, accumulated before rollout completion, and Waiting Staleness, accumulated after a completed trajectory enters the pool. Motivated by this decomposition, we introduce PACE (Pool-Aware Control of Effective Staleness). PACE converts excess pool occupancy into an adaptive rejection budget and ranks completed trajectories using an effective-staleness score that combines Waiting Staleness with prefix-aware Generation Staleness. This avoids penalizing long or interrupted rollouts solely because they span multiple policy versions. In single-turn mathematical reasoning, PACE improves the six-benchmark average validation accuracy by 18.7\% over unfiltered asynchronous RL at the same wall-clock budget and matches synchronous RL performance with 47.1\% less GPU time. PACE also improves validation performance in multi-turn tool-integrated reasoning, outperforming both synchronous and unfiltered asynchronous RL. Further experiments with the mixture-of-experts model and an alternative RL algorithm support its applicability across model architectures and training algorithms.

---


### 218. [ARC-KV: Amortizing Anchor Search for Reconstruction-Based KV Cache Compaction](https://arxiv.org/abs/2609.36835)

**<font color=#1a73e8>作者：</font>** Zheyu Shen, Guanhua Wang, Dezhan Tu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context large language model inference is bottlenecked by KV caches that grow linearly with sequence length. This burden is especially severe for long, reusable context prefixes, whose cache must serve many downstream queries. Reconstruction-based methods such as Attention Matching achieve strong downstream task performance with compact KV caches. However, iterative anchor search dominates the compaction cost of OMP-based Attention Matching. This motivates our selective amortization principle of learning a reusable anchor-selection policy across contexts while retaining context-specific reconstruction. In this work, we propose ARC-KV, a novel reconstruction-based KV cache compaction method that follows this principle. To this end, we first train a value-aware indexer to select real-key anchors in a single scoring pass. ARC-KV then applies convex-hull-constrained key merging and fits an attention-mass bias and compact values against the full cache. At inference time, ARC-KV builds the compact cache once per context using the frozen indexer and reuses it for all subsequent queries. Extensive experiments demonstrate that ARC-KV outperforms reported compaction methods in most settings across QuALITY, RULER, and LongBench on Llama-3.1-8B-Instruct. In particular, at 10% KV retention on QuALITY, ARC-KV improves accuracy from 0.6409 to 0.6474 over Attention Matching while reducing compaction time by a factor of 25.73, from 959.8 s to 37.3 s.

---


### 219. [On-Policy Visual Evidence Distillation](https://arxiv.org/abs/2609.36838)

**<font color=#1a73e8>作者：</font>** Shaohang Wei, Feifan Song, Guangyue Peng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual agents solve problems by interleaving reasoning with image operations, and on-policy distillation (OPD) provides guidance from a strong teacher on student-generated interaction trajectories. However, image operations change the evidence available for subsequent reasoning, so local errors in evidence acquisition (Acquire), reading (Read), or answer grounding (Ground) can propagate through the trajectory and lead to incorrect answers. Existing multimodal OPD methods primarily construct or contrast auxiliary views of the original image to strengthen supervision, without explicitly modeling the connections between student actions, resulting observations, and subsequent reasoning. This limits their ability to provide corrections tailored to different failure stages. We introduce Reflection on Visual Evidence (ReVuE), an on-policy distillation method for visual agents. ReVuE compares multiple student-generated trajectories for the same query, summarizes the observed visual evidence, and diagnoses the first failure across the Acquire, Read, and Ground stages. The resulting reflections provide training-time context for the teacher. We group and reweight token-level distillation losses according to how strongly these reflections affect the teacher's predictions. This design translates trajectory-level evidence diagnosis into targeted token-level supervision, guiding students to improve their visual evidence acquisition and reasoning. Across 11 benchmarks spanning the Qwen2.5-VL and InternVL3.5 model families, ReVuE outperforms all evaluated OPD baselines in weighted-average scores for perception, mathematical reasoning, and general tasks. ReVuE also reduces redundancy in reasoning and tool calls while improving tool-call accuracy and task accuracy. Code is available at this https URL

---


### 220. [Rethinking Multimodal Fake News Detection in the Generative AI Era](https://arxiv.org/abs/2609.36850)

**<font color=#1a73e8>作者：</font>** Wenbin Shen, Guoxuan Qin, Guangxu Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative content is increasingly entering the production and dissemination of news, transforming fake news from manually fabricated or simply manipulated material into complex forms in which native and generated content jointly participate. Existing multimodal fake news detection research primarily focuses on veracity assessment and rarely characterizes how generativity differences affect the reliability of evidence. In contrast, AIGC detection primarily determines whether content is generated or modified by generative models, but it does not by itself establish whether the underlying news event is true. To bridge the separation between these tasks in data and evaluation, we construct Weibo26, a multimodal fake news detection dataset for generative-content scenarios. On this basis, we propose the Generativity-Aware Hierarchical Reasoning (GAHR) framework, which combines global judgment with local correction so that generativity information participates in news-veracity reasoning. Experiments on multiple existing fake news detection benchmarks and Weibo26 show that GAHR achieves competitive veracity-detection performance while effectively identifying generative content.

---


### 221. [RoXDrive: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving via Action-Faithful Rollouts](https://arxiv.org/abs/2609.36851)

**<font color=#1a73e8>作者：</font>** Hongbin Lin, Chaoda Zheng, Yiming Yang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end autonomous driving policies are commonly trained via imitation learning on logged demonstrations without observing the consequences of their own actions, leading to causal confusion in closed-loop real-world deployment. To address this issue, reinforcement learning (RL) post-training offers a promising alternative by leveraging world models as interactive training environments to enable future scene generation for policy improvement. Nevertheless, existing approaches either rely on reconstruction-based simulators, offering limited counterfactual interaction, or adopt synthetic simulators to enable long-horizon closed-loop interaction at the cost of a substantial sim-to-real gap. Recently, video world models have exhibited the ability to generate realistic multi-step future rollouts but may not faithfully reflect action conditions, resulting in action-vision mismatch. In this paper, we introduce RoXDrive, a plug-and-play closed-loop RL framework that enables reliable policy optimization by identifying action-faithful world-model rollouts, consisting of two stages: 1) Model pre-training: In addition to imitation-based policy pre-training, we devise an Action-Vision Faithfulness Evaluator for inverse dynamics estimation with our geometry-aware auxiliary trajectory supervision, enabling long-horizon assessment of whether visual dynamics faithfully reflect the conditioning ego actions. 2) Action-faithful RL post-training: Agents iteratively interact with world models to form long-horizon scene rollouts, retaining only action-faithful ones for dense safety-aware scoring and scene-level closed-loop RL post-training. Extensive experiments on nuScenes and an in-house dataset with over 130K training scenarios demonstrate consistent gains across planners, reducing safety violations by 27.6% with DiffusionDrive on nuScenes and 33.7% with Qwen3-VL on the internal data.

---


### 222. [When Upstream Messages Override Correct Answers: A Controlled Study of Multi-Agent LLM Collaboration](https://arxiv.org/abs/2609.36855)

**<font color=#1a73e8>作者：</font>** Yaxin Gong, Gangyi Zhang, Chongming Gao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems rely on message passing among specialized agents to accomplish complex tasks. However, an upstream agent may provide useful information or an incorrect answer that causes a downstream agent to override a correct answer supported by its own evidence. Prior work has not clearly separated the benefits of communication from the damage caused by incorrect messages. We study this problem with controlled experiments across five benchmarks and five receivers, keeping the downstream task and evidence fixed while comparing answers under three conditions: no message, the upstream agent's original message, or a message with the opposite conclusion. Our experiments reveal three key findings. First, messages often help when the downstream agent would otherwise answer incorrectly. Second, messages can also hurt: when the downstream agent would answer correctly without a message, an incorrect upstream message changes the answer in up to 32% of cases. Third, in 94% of audited harmful cases, the downstream agent copies the upstream's specific wrong answer--a pattern we term answer substitution. Removing unreliable messages recovers part of the lost accuracy, suggesting that communication should be selective based on upstream reliability and the evidence already available to the downstream agent.

---


### 223. [IronLLM: Forging Compact Edge-Native Language Models for Real-Time Embodied Intelligence](https://arxiv.org/abs/2609.36860)

**<font color=#1a73e8>作者：</font>** Changdi Yang, Fengquan Jiao, Haochih Lin 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present IronLLM-0.6B, a 654M-parameter language model designed for efficient on-device inference. IronLLM-0.6B combines a hybrid attention architecture with X-MTP, a lightweight shared-KV multi-token prediction design that eliminates per-depth KV-cache replay and employs a lightweight verification head for rollback-free drafting, achieving a 1.48x decoding speedup. The model is pretrained on approximately 6.2 trillion tokens using a quality-oriented data pipeline and is further post-trained with Multi-Domain On-Policy Distillation to integrate capabilities from domain-specialized teachers. To better meet the low-latency requirements of on-device scenarios, IronLLM-0.6B adopts an Instruct-Only design. Evaluations show that IronLLM-0.6B achieves competitive performance relative to larger models such as Qwen3.5-0.8B and MiniCPM5-1B, while producing more concise responses on many tasks. We further present IronLLM-0.6B-Light, which replaces RMSNorm with Dynamic Tanh and simplifies several computationally expensive components to improve inference and quantization efficiency. Together, the IronLLM models provide an effective performance-efficiency trade-off for resource-constrained deployment.

---


### 224. [Safer Content or Firmer Refusals? A Hybrid Perturbation Defense for Alignment under Harmful Fine-tuning](https://arxiv.org/abs/2609.36862)

**<font color=#1a73e8>作者：</font>** Muhammad Zeeshan Akram, Mufid Kamel Marican, Anvesh Reddy Yenugu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fine-tuning-as-a-service lets users adapt a safety-aligned language model to their own data, but it also creates a harmful fine-tuning attack surface: a small amount of harmful data mixed into an otherwise benign fine-tuning set can degrade the model's alignment. Two recent alignment-stage defenses address this problem at different levels of the model. Vaccine improves the robustness of hidden embeddings to the representation shifts induced by harmful fine-tuning, whereas Booster simulates harmful weight updates and attenuates their effect during alignment. We investigate whether these mechanisms are complementary and propose VaccineBooster, a single alignment procedure that combines embedding perturbation and weight-level gradient attenuation within each training step. On Llama-2-7B aligned with BeaverTails and then attacked through poisoned fine-tuning, VaccineBooster achieves the lowest OpenAI moderation score among the compared defenses, 0.315, while a Booster-Only variant retains the highest post-attack refusal rate, 50%. Together with ablations over the embedding-perturbation and gradient-attenuation strengths, these results indicate a trade-off: embedding perturbation primarily reduces flagged harmful content, whereas gradient attenuation primarily preserves explicit refusal behavior. Because our evaluation uses ten prompts and a single unseeded run per configuration, we report this trade-off as an observed pattern rather than a statistically resolved effect. These results provide practical guidance for prioritizing content safety or refusal retention when aligned models are exposed to untrusted fine-tuning.

---


### 225. [S4VY: Segment Anything in Feed-Forward 4D Visual Geometry](https://arxiv.org/abs/2609.36875)

**<font color=#1a73e8>作者：</font>** Jingdong Zhang, Xin Li, Jan Kautz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate instance segmentation in dynamic scenes is important for downstream applications such as robotics and autonomous driving. Existing Segment Anything models operate primarily on 2D image or video masks and preserve identity through sequential memory, while promptable 4D instance segmentation built upon feed-forward visual geometry remains underexplored. We introduce S4VY, a Segment Anything model built on feed-forward 4D visual geometry. From a set of RGB observations, S4VY transforms shared visual-geometric features into an exhaustive set of class-agnostic 4D instance masks through a space-time query decoder, with each persistent object query binding one entity across all observations. This representation supports prompt-independent segmentation as well as point- and box- conditioned selection, without requiring a seed mask or temporal ordering. We further develop an agentic harness for natural-language grounding in the large observation space of a 4D scene. Active tree search identifies relevant frames without scanning every fixed window; a dual-stream grounder combines fine-grained VLM visual priors with geometry-consistent instance features through complementary bounding-box prediction and object-query matching; and an independent critic selects the final 4D instance mask from their predictions. Extensive experiments demonstrate state-of-the-art 4D instance segmentation and strong language-guided grounding performance under a unified evaluation spanning static and dynamic scenes.

---


### 226. [SKILLLITE: Evidence-Guided Malicious Skill Auditing with Compact LLMs](https://arxiv.org/abs/2609.36879)

**<font color=#1a73e8>作者：</font>** Haoran Ou, Gelei Deng, Xuanye Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As LLM-based agents perform increasingly complex tasks, Agent Skills have emerged as a flexible mechanism for extending their capabilities. An Agent Skill packages task-specific instructions with executable components and auxiliary resources to provide specialized functionalities. However, the growing adoption of third-party Skills introduces a new supply-chain attack surface. Malicious Skills can embed harmful behaviors that abuse agent privileges and compromise the agent execution environment or accessible resources. Although recent LLM-based malicious Skill auditing approaches have achieved promising performance, they often rely on capable commercial LLMs. How to achieve effective auditing with compact, locally deployable LLMs in security-sensitive and resource-constrained settings remains largely unexplored. Our investigation reveals that compact LLMs struggle to identify malicious behaviors hidden in complex Skill packages. This difficulty arises from both the implicit nature of such behaviors and the limited reasoning capacity of compact LLMs. To address these challenges, we propose SKILLLITE, an evidence-guided agentic framework for malicious Skill detection. SKILLLITE effectively extracts security-relevant behaviors and infers the intended functionality from complex Skill packages. It then employs a compact LLM to assess the maliciousness of the Skill based on the observed behaviors and their functional context. Experiments show that SKILLLITE improves malicious Skill detection across different compact LLM backbones and outperforms existing representative auditing baselines. Its effectiveness generalizes to behaviorally confirmed in-the-wild malicious Skills. Meanwhile, SKILLLITE maintains a low inference latency, supporting its practical deployment.

---


### 227. [WEFT: Scaling Tool-Use Post-Training for General-Purpose Agents](https://arxiv.org/abs/2609.36887)

**<font color=#1a73e8>作者：</font>** Bo Mao, Hang He, Linting Wang 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent efforts to scale tool-use post-training have largely centered on the synthesis of executable environments, which constitute only one component of a broader agentic interaction system comprising the environment, task, agent harness, and evaluator. Scaling environments in isolation, however, does not guarantee commensurate gains in model performance, because reliable learning signals depend on coherent interactions among all components of the agentic interaction system. To address this problem, we introduce WEFT (Whole-system Evolution For Tool-use Post-training), which couples scalable agentic interaction system construction, execution-driven self-evolution, and stable post-training. WEFT scales agentic interaction system construction across environment breadth, task complexity, and interaction diversity. Execution-driven self-evolution iteratively uses execution traces and state evidence to attribute failures and revise the responsible components, with fresh rollouts evaluating the changes and providing evidence for subsequent evolution rounds. For stable post-training at scale, WEFT addresses both optimization and execution reliability: prefix-preserving sampling retains verified progress and atomic-turn credit assignment localizes learning signals, while MegaMCP maintains isolated, recoverable state across concurrent rollouts over shared tool services. Extensive experiments across various models and benchmarks demonstrate the effectiveness of WEFT for tool-use post-training. WEFT-8B and WEFT-14B outperform all evaluated matched-size environment-scaling baselines on BFCL V4, $\tau^2$-Bench, and Claw-Eval. In particular, WEFT-14B improves over Agent-World-14B by 6.41, 2.23, and 12.27 percentage points. WEFT-35B-A3B further extends these gains to more challenging long-horizon workflow benchmarks, including Toolathlon-Verified and AutomationBench.

---


### 228. [Beyond Sub-Gaussian Detector Scores: Robust Weighted Profile-Loss Change Point Detection for Human-LLM Text Segmentation](https://arxiv.org/abs/2609.36888)

**<font color=#1a73e8>作者：</font>** Wan Tian, Zhongyi Li, Yawen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixed human-LLM documents require locating authorship transitions from detector scores whose reliability varies across text units. Existing weighted mean contrasts are vulnerable to extreme scores, while directly replacing means with robust centers obscures how a misplaced boundary changes the population objective. We propose Robust Weighted Profile-Loss Change Point Detection (RWCP), which combines capped reliability weights, Huber profile gains, and narrowest-over-threshold search in reliability coordinates. Our key analysis expresses the population gap between a true and a displaced split as a merge cost, avoiding a closed-form solution for the nonlinear center of a mixed segment. Under explicit curvature, spacing, and dependence conditions, core RWCP recovers the number of changes and localizes their boundaries; its quadratic-loss limit recovers squared weighted CUSUM. We also study RWCP-R, a separately evaluated decoder that shares source centers across nonadjacent passages. Across five retrospective cached-score benchmark families, core RWCP reduces family-macro WindowDiff by 17.6\% relative to weighted change-point detection, and RWCP-R lowers it further. Boundary recovery improves most clearly for isolated changes, while both fixed configurations miss changes in collaborative and densely alternating text.

---


### 229. [Harness Evolution as Learning: Approximation, Generalization, and Optimization Limits of Self-Improving Personal Agents](https://arxiv.org/abs/2609.36892)

**<font color=#1a73e8>作者：</font>** Zeyu Gan, Zixuan Gong, Yong Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the capabilities of large language models (LLMs) continue to advance, increasing attention is turning to how to translate their abilities into useful behavior. Personal agents bring this question into everyday settings, where models are expected to serve individual users and continually adapt to their preferences. With the underlying model held fixed, such adaptation relies on harness engineering: designing and evolving the surrounding layer that manages context, memory, tools, and execution. Despite rapid progress, the factors governing effective harness evolution remain insufficiently understood. To narrow this gap, we investigate three central questions concerning harness architecture, harness scale, and self-evolution algorithms through complementary empirical and theoretical analyses. Empirically, we introduce a preference-oriented benchmark and systematically characterize the capabilities and limitations of personal agents associated with these three dimensions. Theoretically, we formulate harness evolution as a learning problem and explain these phenomena through approximation, generalization, and optimization errors. Analyses of reachable policies, capacity under finite interaction evidence, and biased update dynamics provide theoretical accounts of the observed phenomena. Together, these results offer a unified perspective on the limits of personalization through harness evolution and inform future harness design.

---


### 230. [Momentum-Coupled Rubric Adaptation for Detailed Image Captioning](https://arxiv.org/abs/2609.36893)

**<font color=#1a73e8>作者：</font>** Zhenwen Ji, Lei Jin, Shanyong Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detailed image captioning requires accurate and comprehensive descriptions of fine-grained visual content, yet caption quality spans factual accuracy, information coverage, and clarity. Compared with conventional methods that rely mainly on high-quality supervision or holistic rewards, rubric-based reinforcement learning decomposes these requirements into explicit criteria and provides targeted, structured feedback. However, existing methods often use separate models for caption generation, rubric construction, and judging, which may lead to inconsistent interpretations across roles. Some dynamic rubric methods alternate updates between the caption policy and rubric generator while keeping the judge fixed, but staged optimization may still leave rubric construction and judging out of step with policy optimization. We propose MoCo Rubric, a two-stage framework that coordinates these roles. First, role-conditioned, shared-parameter multi-task supervised fine-tuning equips a single vision--language model to serve as the Caption Policy, Rubric Generator, and Rubric Judge. Then, the Generator constructs rubrics online from captions sampled by the current Policy, reference captions, and image evidence. The Judge provides rubric-based rewards, and only the Policy receives GRPO updates. As Policy updates change the candidates being evaluated, we use an exponential moving average of the Policy parameters to update one momentum model shared by the Generator and Judge. This gradual transfer lets both rubric roles track Policy updates without separate RL optimization while smoothing parameter changes that could disrupt their rubric capabilities under direct synchronization. Across five captioning benchmarks, MoCo Rubric achieves an average pairwise win rate of 72.83\%, the best mean rank in blind ranking, and the highest average score in caption-based question answering.

---


### 231. [STAR-GRPO: Canonical Anchoring and Reliability-First Advantages against Representation-Dependent Reward Hacking](https://arxiv.org/abs/2609.36900)

**<font color=#1a73e8>作者：</font>** Wan Tian, Zhongyi Li, Xiang Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward hacking occurs when policy optimization exploits a brittle reward interface or an overly permissive proxy objective, improving the training score without improving the underlying response quality. This phenomenon is amplified in group-relative policy optimization: an unsupported reward can shift the group baseline and alter the updates of other rollouts, while post-hoc or purely relative weighting cannot represent group-wide uncertainty. We propose \emph{Self-Tuned Anchored Reliability Group-Relative Policy Optimization} (STAR-GRPO), a reliability-first advantage estimator based on paired assessments of the same rollout. STAR separates the quality signal from its learning influence: score disagreement determines rollout reliability, relative reliability enters a self-tuned robust location--scale fit before group normalization, and absolute group reliability attenuates the resulting bounded advantage. The analysis establishes coordinate and second-moment bounds, characterizes exact centering through the weighted location equation, and gives reliability-dependent attenuation guarantees for outlying rewards. We evaluate STAR-GRPO in two complementary reward-hacking regimes. In token-interface exploitation, STAR prevents runaway optimization of the deployed-interface score while improving the canonical quality signal. In rubric-proxy overoptimization for medical reasoning, STAR improves independent semantic evaluation, narrows the proxy--judge discrepancy, and reduces overclaim while optimizing the same task proxy. Together, these results show that reliability-first normalization offers a principled way to limit unsupported reward influence on both group baselines and policy updates, while retaining the task reward as the optimization target.

---


### 232. [MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation](https://arxiv.org/abs/2609.36903)

**<font color=#1a73e8>作者：</font>** Ke Wang, Houxing Ren, Zimu Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> End-to-end full-duplex speech models have brought open-source machine conversation closer to human-like interaction, yet existing systems remain limited in two intertwined dimensions: long-context robustness and multi-party interaction. Real-world scenarios such as meetings, group lessons, and social-robot reception require a single model to track, contextualize, and respond to multiple speakers over extended durations. Progress is constrained by both data and evaluation: open multi-party speech corpora remain small and are not designed for codec-frame-level full-duplex modeling, while existing long-audio benchmarks focus on passive listening and speech-to-speech benchmarks are mostly short and dyadic. We extend the Moshi paradigm jointly along the long-horizon and multi-party axes in English and Chinese. First, we release 57.6k hours of synthetic training data ($\href{this https URL}{MultiTalkPT}$ and $\href{this https URL}{MultiTalkFT}$) for long-form, multi-party, English-Chinese full-duplex dialogue, with controllable length, participant count, turn-taking, overlap, backchannels, interruptions, addressee shifts, and long-range coreference. Second, we introduce $\href{this https URL}{MultiTalkBench}$, built from real human recordings, for evaluating long-form, multi-party, bilingual full-duplex dialogue. Conversations average 32.6 minutes and include probes for long-range entity tracking, topic coherence, and addressee selection. Third, we train a bilingual Moshi-style model that sustains coherent multi-party English-Chinese conversations over extended durations and substantially outperforms open-source baselines including Moshi, MiniCPM-o-4.5, and Qwen3-Omni-30B-A3B-Instruct on MultiTalkBench.

---


### 233. [SafeVantage: Vantage-Aware Memory for Reliable Embodied Decisions](https://arxiv.org/abs/2609.36906)

**<font color=#1a73e8>作者：</font>** Sean Hardesty Lewis, Zuyi Guo, Benwang Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable embodied decisions under partial observability require informative observations and sufficient supporting evidence. However, semantic scores alone do not reveal which viewpoints justify a claim or where additional evidence should be acquired. We introduce SafeVantage, a vantage-aware semantic memory and active acquisition framework that retains each claim's supporting views, camera poses, and estimated target location, keeping positive support distinct from search coverage. A learned candidate-observability model uses claim-grounded geometry to predict target visibility at reachable viewpoints. These predictions guide view selection through expected reduction in terminal decision loss, accounting for travel cost and geometrically distinct corroboration. A calibrated head then combines support, spatial consistency, and coverage to produce Yes, No, or Abstain decisions. We evaluate SafeVantage on a category-presence benchmark spanning 232 unseen ProcTHOR houses and 7,424 paired episodes per method and action budget. Compared with validation-selected equal-budget baselines, SafeVantage achieves macro-F1 gains of 24.7% and 12.0% at eight and twelve actions, respectively, with lower risk and higher answer rates at both budgets and 31.7% less travel at eight actions. Equal-input HM3D experiments show lower selective risk under fixed observations, while controlled ScanNet interventions show that restoring supporting views improves downstream VLM answers. Ablations further support the contribution of candidate observability to decision quality and acquisition efficiency. Results demonstrate the value of claim-level viewpoint evidence for connecting semantic memory, active acquisition, and reliable decision-making. Code is available at this https URL

---


### 234. [BaLEEN: Biasing with Latent Encoded Entities for Context-Aware ASR](https://arxiv.org/abs/2609.36913)

**<font color=#1a73e8>作者：</font>** Chihiro Taguchi, Yotaro Kubo, Rujikorn Charakorn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transcribing domain-specific entities and rare proper nouns remains a major challenge in automatic speech recognition (ASR). In this paper, we propose BaLEEN (Biasing with Latent Encoded Entities), a lightweight, hypernetwork-based framework for dynamic contextual adaptation without fine-tuning the underlying ASR model. BaLEEN encodes variable-length contextual keywords using a pretrained language model, compresses them into a fixed sequence of latent vectors via a Perceiver bottleneck, and injects context-dependent bias vectors directly into the intermediate encoder representations of the ASR model. Because both the language model and the backbone ASR model remain entirely frozen during training, BaLEEN operates as a plug-and-play adapter that incurs zero computational overhead at inference time when context biases are precomputed. We evaluate our method on a CTC-based ASR model using a Wikipedia-derived corpus with annotated named entities and synthetic speech. Experimental results demonstrate that BaLEEN reduces keyword miss rate by 8.7% on the test set relative to the unbiased baseline while simultaneously improving overall word error rate by 21% and character error rate by 28%.

---


### 235. [Can Language Models Learn to Forecast Stock Prices](https://arxiv.org/abs/2609.36914)

**<font color=#1a73e8>作者：</font>** Jiacheng Guo, Suozhi Huang, Shuzhen Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training has been shown to significantly improve language models' performance on tasks with verifiable outcomes, including mathematical reasoning, software engineering, and computer use. However, whether the same approach can improve forecasting in financial markets is much less clear. Compared with tasks with verifiable outcomes, not only are realized returns noisy, but even what constitutes a relevant information set for making effective predictions is not obvious a priori: the model must decide which observations to gather and then commit to a numerical judgment before the outcome is known. We study this question in a chronological stock-price sandbox, where a language model gathers price, volume, relative-performance, and market-context evidence and predicts a future return. We post-train Qwen3-4B with supervised fine-tuning (SFT) on tool-use demonstrations, then proximal policy optimization (PPO) with a terminal reward given by the forecast score against the realized return. The resulting AURA-4B more than doubles the starting direction--magnitude score, from 20.94 to 43.31, and is comparable to frontier language models on this benchmark. Conditional magnitude agreement rises from 33.3 to 66.2, while directional accuracy changes from 62.9 to 65.4. SFT expands tool use, and PPO further increases the share of ranking and market-context queries. These results show that post-training can substantially improve financial forecasting performance, together with changes in how the model investigates the market, on this outcome-selected benchmark.

---


### 236. [Representation Dynamics Reveal Semantic Saliency and Similarity for Visual Token Pruning in MLLMs](https://arxiv.org/abs/2609.36916)

**<font color=#1a73e8>作者：</font>** Weixuan Li, Zikun Zhou, Xinyi Zhuang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) incur high inference latency from long visual token sequences. Existing pruning methods commonly use attention maps or output features to estimate token importance or redundancy. Several recent approaches also exploit representation changes, but when and how these changes reflect foreground saliency and semantic consistency remain insufficiently understood. We analyze visual token representation dynamics across encoder depth and uncover two findings. First, the relationship between token update magnitudes and foreground saliency is layer-dependent: large token updates concentrate on foreground regions in two depth intervals, separated by several sink-dominated layers at intermediate depths. Second, similarities between token update directions better distinguish same-class from different-class tokens than those between encoder output features. Building on these findings, we propose MSDG-Prune, a training-free method that uses update magnitudes and directions to preserve salient and diverse visual information. Specifically, we group tokens by update-direction similarity and use query-weighted saliency derived from update magnitudes across a chosen depth window for group-wise token pruning. Extensive experiments across four MLLMs demonstrate the effectiveness and generalizability of MSDG-Prune. On LLaVA-NeXT, it retains 91.9% of uncompressed performance on average with only 5.6% of visual tokens, while achieving a 7.8x prefilling speedup. Code is available at this https URL.

---


### 237. [Neuro-Symbolic Computer Use: Learning Reusable Policies for Reliable and Efficient Execution](https://arxiv.org/abs/2609.36927)

**<font color=#1a73e8>作者：</font>** Hyewon Suh, Thanh Minh Nguyen, Chih-Lun Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many computer tasks recur: the same workflow runs many times, with new inputs and from different starting states. Current computer-use agents re-plan every step of every run, which makes them costly and unreliable on such tasks. We introduce neuro-symbolic computer use, in which a recurring workflow is executed by a learned policy rather than re-derived by an agent on each run. The policy fixes the decisions that are stable across runs (ordering, variables, loops, and branches) in executable code, and delegates observation-dependent decisions, such as grounding and state checks, to neural models. We learn these policies with neuro-symbolic policy iteration: starting from one agent trajectory, it executes the policy, diagnoses failures with task-completion and step-level judges, and revises the code with a coding model informed by an agent's continuation from the point of failure, without access to the benchmark evaluator. Iterating on generated parameter and initial-state variants makes the policy reusable, and a pre-action verifier guards each state-mutating step at deployment. On OSWorld-Verified and ScienceBoard, the learned policies achieve the highest Pass^3 of all methods in all four settings, 3.6-15.8 points above the base agent, while cutting per-run cost by 15-217$\times$ and latency by 3.4-5.1$\times$. On OSWorld-Verified, policies built only on variants transfer to the held-out original tasks, exceeding AutoRPA by 8.6-17.5 points in Pass^3.

---


### 238. [Dating the Model: Hidden Dates in System Prompts Affect LLM Evaluation](https://arxiv.org/abs/2609.36931)

**<font color=#1a73e8>作者：</font>** Mario Sanz-Guerrero, Minh Duc Bui, Manuel Mager 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reproducibility is essential for scientific research, yet prior work shows that LLM outputs vary with hardware and batching. We identify an overlooked factor: the hidden injection of the current date into system prompts, which users cannot control and which changes every day. Across 9 recent LLMs and 6 datasets spanning multiple-choice QA (MCQA), math reasoning, code generation, and machine translation, performance varies solely with the current date, with deltas of up to 6% on MCQA, 14% on math reasoning, 7% on code generation, and 2.84 BLEU on machine translation. Model rankings also shift, affecting leaderboards. This date effect exceeds other sources of non-determinism, such as batch size and numerical precision. Standard prompting techniques -- chain-of-thought and few-shot prompting -- do not reduce the sensitivity; chain-of-thought even amplifies it. Our findings underscore the need for careful evaluation protocols to ensure reproducibility and fair comparisons in LLM research.

---


### 239. [Learn from the Gap: Differential-Aware Advantage Pruning with Adaptive Rollout Sampling for GRPO](https://arxiv.org/abs/2609.36932)

**<font color=#1a73e8>作者：</font>** Jiahua Yang, Zhiwei Yang, Xianpeng Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recently, Group Relative Policy Optimization (GRPO) and its variants have been developed for policy optimization and demonstrated notable performance gains. However, these methods usually incur substantial computational overhead due to per-question multi-rollout sampling and repeated per-token probability evaluation across rollouts. Furthermore, low-information or highly homogeneous trajectories can degrade downstream learning signal efficiency, hindering model optimization and limiting final performance. To address these issues, we propose FastRL, a novel plug-and-play reinforcement learning framework that simultaneously improves training efficiency and the effectiveness of policy learning. Specifically, 1) We introduce an advantage-aware pruning strategy to selectively preserve high-advantage trajectories while maximizing inter-trajectory gradient diversity. 2) Then, we design an adaptive rollout sampling mechanism to dynamically adjust the sampling scale across different training stages based on historical pruning distributions, balancing exploration adequacy and computational efficiency. Experiments demonstrate that FastRL can be seamlessly integrated into GRPO, DAPO, and GSPO variants, achieving an average 2.07$\times$ training speedup on Geometry3K and GeoQA8K-R1V, along with an approximately 1.64\% improvement in average accuracy on visual reasoning benchmarks. Source codes will be available at this https URL.

---


### 240. [VLALight: A Vision-Language-Action Model for Traffic Signal Control](https://arxiv.org/abs/2609.36934)

**<font color=#1a73e8>作者：</font>** Pan Zhang, Siqi Lai, Kemu Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traffic signal control (TSC) is essential for improving urban mobility and reducing congestion. Although roadside cameras are widely deployed at signalized intersections and provide rich visual observations of evolving traffic, existing TSC methods typically rely on manually engineered traffic states or separate perception modules, creating a gap between physical observations and control decisions. We present VLALight, the first vision-language-action (VLA) model for end-to-end traffic signal control from multi-view roadside videos. VLALight directly maps visual observations to coordinated signal actions through multi-target spatiotemporal traffic reasoning and topology-aware cooperative perception across intersections. To establish this capability, we develop a two-stage supervised cold-start training strategy for visual traffic understanding and signal decision-making, followed by cooperative agentic reinforcement learning that jointly optimizes local control and network-wide traffic efficiency. Furthermore, VLALight introduces adaptive fast and slow reasoning modes, enabling the policy to allocate deeper reasoning only when additional deliberation provides sufficient control benefits. Through balanced mode-aware rollouts and relative advantage optimization, VLALight learns to trade off decision quality and inference cost. Extensive experiments on seven real-world traffic-flow datasets across three urban networks demonstrate that VLALight consistently outperforms transportation-based, RL-based, and LLM/VLM-based baselines. Ablation studies validate the effectiveness of cooperative perception, network-level optimization, and adaptive reasoning. These results demonstrate the potential of VLA models for real-world physical traffic control. Our project is available at this https URL.

---


### 241. [CoEM: Empowering Long-Context Reasoning with Commit-on-Evidence Memory](https://arxiv.org/abs/2609.36935)

**<font color=#1a73e8>作者：</font>** Jingguang Li, Yebo Wu, Zuyi Guo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context reasoning is essential for complex and long-horizon tasks, yet the performance of large language models (LLMs) degrades as context length increases. Recent approaches address this by processing input chunk by chunk while maintaining a bounded textual memory in model context. However, premature information compression can discard critical details essential for subsequent reasoning. In this paper, we introduce Commit-on-Evidence Memory (CoEM), which learns when to convert source evidence into compact memory facts. Specifically, under a fixed context-memory budget, CoEM preserves potentially useful source excerpts verbatim in a pending set, allowing subsequent context to clarify their relevance before irreversible compression. As new context arrives, a learned policy revisits each pending excerpt and decides whether to promote it to the committed memory, retain it for further consideration, or discard it. A frozen verifier ensures proposed facts are accepted only if supported by retained excerpts and current context. To further guide effective memory management, we train this policy using reinforcement learning by combining fine-grained, step-level evidence rewards with final answer rewards. Extensive experiments demonstrate that CoEM consistently improves long-context reasoning. When evaluated on 6,400 documents long-context input, CoEM outperforms the strongest memory baseline by 10.4-11.4 F1 points on Qwen3.5-9B. Code repository: this https URL.

---


### 242. [Practical Secrets Extraction against Black-box LLMs](https://arxiv.org/abs/2609.36941)

**<font color=#1a73e8>作者：</font>** Shiqian Zhao, Siwei Jiang, Xinfeng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly power autonomous coding agents such as Codex and Claude Code, yet their training corpora may contain confidential credentials exposed in public repositories or collected from private development artifacts, creating risks of memorization and subsequent leakage. Existing extraction audits, however, largely assume access to model weights or token probabilities. In this work, we present a black-box secret extraction framework for commercial, API-based LLMs under output-only access. It comprises (i) \emph{Cross-Validated Secret Knowledge Distillation}, which uses semantics-preserving prompt variants, response cross-validation, and provider-specific format filtering to distill secret-relevant behavior into a local white-box proxy; and (ii) \emph{Proxy-Guided Secret Extraction and Candidate Filtering}, which combines truncated top-$p$ sampling with local token entropy, $N$-gram frequency profiling, and provider-specific structural priors. On controlled API-key benchmarks, our framework improves recovery effectiveness and real-key rates over representative baselines while reducing extraction latency. A responsible real-world evaluation further recovers masked provider-specific credentials from three independently deployed black-box LLM systems spanning OpenAI and Claude Code, showing that memorized secrets can be exposed under output-only access.

---


### 243. [Fine-Tuning on Self-Generated and Reward-Weighted Data: Learning Dynamics, Convergence Rates, and Benefits of Off-Policyness](https://arxiv.org/abs/2609.36945)

**<font color=#1a73e8>作者：</font>** Zhiwei Wang, Yanxi Chen, Yaliang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the learning dynamics of fine-tuning a policy model on self-generated and reward-weighted data, with particular focus on a generalized version of REINFORCE -- referred to as RE(S) -- that updates the rollout distribution once every $S \ge 1$ gradient steps. Prior work in bandits and reinforcement learning has developed rich theory for policy gradient methods, and on-policy sampling (i.e., a small $S$, ideally $1$) is often viewed as crucial to their success; yet in prominent application like post-training large language models, reward-guided self-training has proved to be effective even when the rollout distribution is updated infrequently, but theoretical understanding remains limited for the convergence properties of these off-policy methods. To bridge these gaps, we develop a unified theory for RE(S) that covers the full spectrum of $S \ge 1$: it can be interpreted as a stage-wise optimization process, where each stage takes $S$ gradient steps for minimizing the Kullback-Leibler distance to a fixed reward-weighted rollout distribution. For multi-arm bandits with softmax policies, our in-depth analysis and numerical experiments reveal three key findings: (1) for any fixed $S$, RE(S) enjoys global convergence to the optimal policy as the number of rollout distribution updates $B = \lfloor T / S \rfloor \rightarrow \infty$, where $T$ denotes the number of gradient steps; (2) we prove tight two-sided bounds showing that the suboptimality gap of RE(S) achieves an asymptotic $\Theta(1 / T)$ convergence rate, while $S$ only affects the length of a burn-in phase; (3) when initialized at a weak policy with a small optimal-action probability, RE(1) gets trapped around suboptimal policies for a long period, whereas RE(S) with a suitable $S$ avoids the detour and achieves significantly faster convergence to the global optimum, highlighting the benefits of off-policyness in this case.

---


### 244. [ER-JEPA: Experience Replay Improves Joint-Embedding Predictive Learning in Language Models](https://arxiv.org/abs/2609.36952)

**<font color=#1a73e8>作者：</font>** Jingnan Pu, Zi-En Fan, Feng Lian  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel at token-level generation but may learn undesirable abstract semantics and lack comprehensive perception. LLM-JEPA mitigates this by aligning different views of the same underlying knowledge via a joint-embedding predictive architecture (JEPA). However, strong alignment does not necessarily lead to accurate, stable predictions. To address this, we propose ER-JEPA, which adds an episodic replay path to LLM-JEPA. ER-JEPA stores training pairs in a memory. At each step, it stores and retrieves relevant data to provide additional supervision. This enables learning from both the current batch and stored training pairs, providing additional supervision for token prediction and representation alignment. Experiments across multiple datasets (NL-RX, GSM8K, Spider, and NQ-Open) demonstrate that ER-JEPA consistently outperforms LLM-JEPA.

---


### 245. [Cool the Sampler, Not the Learner: Sampling Temperature Moves the Staleness Cliff of Importance-Corrected GRPO](https://arxiv.org/abs/2609.36953)

**<font color=#1a73e8>作者：</font>** Taiheng Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production RL for language models lets the sampler fall behind the learner and repairs the resulting mismatch with a truncated importance weight. We ask how long the sampler can go without a refresh under that correction, and find a cliff: on Qwen2.5-Math-1.5B and GSM8K, importance-corrected GRPO refreshed every 192 updates learns well for 180 steps and then degrades severely in all three data seeds before the refresh arrives. Published remedies for staleness act on the update; we act on the sampler instead. Decoupled cooling draws samples at temperature 0.8 while the learner, the reference model and the importance weights stay at temperature 1, with the behaviour probability recorded from the tempered distribution, so the learner's objective is unchanged. All corresponding cooled runs are stable, and the longer interval keeps what the short one delivered: at the same update budget, a cooled sampler refreshed every 192 steps matches an uncooled sampler refreshed every 96 at the end of training (0.857 for both) and averaged over it (0.79), whereas lowering the learning rate to a safe value ends 3-7 points lower. On Qwen2.5-Math-7B the degradation points at interval 192 predict that an interval of 144 is fatal without cooling and survivable with it; on two data seeds the uncooled runs degrade before their first refresh and the cooled runs pass it and end at 92-93% against 68-81%, with one cooled run degrading transiently late in the second cycle. The benefit has a window: at three times the safe interval and in a high-mismatch MATH setting cooling delays degradation without preventing it, stronger cooling is not better, and cooling without the correction collapses. Sampling temperature is a control on staleness tolerance, and temperature and refresh interval should be chosen together.

---


### 246. [Beyond Readability: Evaluating Task Information Recoverability](https://arxiv.org/abs/2609.36957)

**<font color=#1a73e8>作者：</font>** Yiwei Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Direct visual readability and task-information recoverability are different quantities. Failure to decode a target from a fixed observation need not eliminate access to that target through another recovery route. We develop an evaluation perspective that makes the observation, query, target, and available knowledge explicit and measures the overlap between routes' success sets. For information available on the original visible surface under suitable imaging conditions, direct optical recovery reads the target from the image, optionally after restoration; entity-linked recovery uses residual visual evidence to identify the depicted entity and accesses its target through an entity--attribute relation in a specified knowledge resource. Such access can draw on stored knowledge or an external source. A controlled book-cover study instantiates external access with a fixed title--author catalog, comparing optical author recovery with visual title resolution and deterministic lookup under resolution degradation. Entity-linked successes persist across the tested vision--language models, revealing information access beyond the tested direct visual frontier despite substantial differences in absolute performance. A substantial optical-only region remains. These complementary outcomes show why visual degradation should be evaluated through the task information accessible along specified routes and knowledge resources, alongside direct readability.

---


### 247. [Chinese-Jev: Bringing System One Model to Chinese-Language Tasks](https://arxiv.org/abs/2609.36965)

**<font color=#1a73e8>作者：</font>** Zexiao Wang, Zihao Zhang, Xudong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> System One models such as Jev offer an efficient alternative to generative language models for tasks that require decisions rather than open-ended responses. However, existing Jev models exhibit limited Chinese-language decision accuracy, restricting their utility in both general and specialized settings. In this paper, we introduce Chinese-Jev, a System One model that addresses this gap through a unified data processing and training pipeline. Our data processing protocol converts heterogeneous Chinese-language annotations into probability targets over candidate options, enabling a shared training formulation across domains and question formats. To enable efficient inference, Chinese-Jev adopts a lightweight encoder-only backbone for text encoding and learns to score candidate answers through decision-oriented training. To address the misalignment between the pre-training distribution and downstream Chinese-language scenarios, we first train the model on a general-purpose corpus of 10 million examples, then fine-tune it separately for the medical, legal, and financial domains. To evaluate decision accuracy and calibration in both general and domain-specific Chinese-language settings, we introduce Chinese-Jev Bench (CJ-Bench). After first-stage pre-training, Chinese-Jev exceeds the accuracy of the closed-source Jev model by 1.24% on general-domain tasks while achieving a 20.3x speedup. Subsequent domain-specific fine-tuning yields a 4.0% accuracy improvement over Jev in medicine and achieves 92% of Jev's average accuracy across specialized domains, with a 17x speedup and an average latency of only 15 ms per example. We further demonstrate on-device deployment of an INT8-quantized model on mobile devices, achieving an inference latency of approximately 1.0 second per decision. The project is available at this https URL.

---


### 248. [JudgeCast: Time Series Forecasting with Experience-Informed Covariate Judgements](https://arxiv.org/abs/2609.36966)

**<font color=#1a73e8>作者：</font>** Donguk Kwon, Wooseok Jeong, Dongha Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Covariate effects vary across contexts and shift over time, requiring forecasters to assess how to use them for each forecasting context. As forecasting proceeds, observations for earlier forecasts become available, providing feedback on past covariate use for subsequent forecasts. However, when multiple covariates act together, the forecast error reveals the numerical discrepancy from the observation but not how the covariates should have been used. We introduce JudgeCast, an experience-based framework for time series forecasting with covariates. Following the judgmental adjustment practice, a frozen TSFM provides the base forecast, while a frozen LLM uses the current context and relevant experience to adjust it. Within the adjustment, assessing covariate effects and determining the numerical adjustment serve distinct roles, so JudgeCast first forms explicit covariate-wise judgments and then determines the adjustment. After observation, JudgeCast uses the observed residual of the base forecast to reconstruct alternative judgments and evaluates the original and alternatives through their resulting adjustments. The best-performing decision is selected and retained as validated experience for subsequent forecasts. Across diverse real-world datasets, JudgeCast outperforms strong baselines. Ablations show that explicit covariate-wise judgment can improve forecast-time adjustment, while residual-guided experience construction yields more reliable forecasting gains than retaining raw decisions as experience.

---


### 249. [TaskBridge: Bridging Unsupervised Tabular Anomaly Detection and In-Context Learning via Virtual Tasks](https://arxiv.org/abs/2609.36968)

**<font color=#1a73e8>作者：</font>** Doyun Choi, Dooho Lee, Jaemin Yoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised tabular anomaly detection (TAD) aims to identify anomalous rows in tabular data using normal training samples. While conventional methods rely on dataset-specific training and configuration search, recent tabular foundation models (TFMs) enable zero-shot anomaly detection on unseen datasets via in-context learning. Most TFM-based approaches, however, require anomaly-specific pretraining from scratch, making detection inherently dependent on synthetic TAD-specific priors and costly to update. Some approaches instead repurpose pretrained general-purpose TFMs for TAD to avoid this burden, but rely on computationally expensive formulations with restrictive anomaly inductive biases. In this work, we introduce TaskBridge, a new framework that efficiently repurposes pretrained general-purpose TFMs for unsupervised TAD by constructing virtual supervised tasks that directly recast anomaly detection as supervised in-context inference of TFMs. The resulting virtual tasks induce predictive structures under which normal queries and their target pairs receive high support, whereas anomalies tend to violate the induced structures and receive lower support, providing direct anomaly evidence. Across 790 real-world datasets, TaskBridge consistently outperforms 30 baselines, including state-of-the-art TFM-based approaches, without anomaly-specific TFM pretraining or dataset-specific model optimization.

---


### 250. [AMU:Admission and Memory Update for Personalized Conversations---Structured Memory with SLM Guided Control](https://arxiv.org/abs/2609.36976)

**<font color=#1a73e8>作者：</font>** Tao Hwang, Yishi Diao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have become the foundation of personalized assistants, but maintaining persistent user memory across long-term interactions remains challenging. Existing memory systems often focus on storage, retrieval, or consolidation, while memory writing remains less controlled: transient requests, duplicate statements, and outdated user states may enter memory and later be retrieved for personalization. In this paper, we present AMU: Admission and Memory Update for Personalized Conversations, an SLM-guided (Small language model guided) structured framework for writing-time memory control. AMU uses structured memory filtering to decide what should enter memory and SLM-guided storage management to determine whether an admitted record should be stored separately, discarded as a duplicate, or fused as an update. We evaluate AMU in a controlled memory writing and retrieval setting. Experimental results show that AMU maintains cleaner and more retrievable personalized memories.

---


> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
