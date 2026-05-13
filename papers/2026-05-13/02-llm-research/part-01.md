# 🧠 大模型相关研究 | 2026年05月13日

> 本类共 **223** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-223](./part-05.md)

---

### 1. [Steering Without Breaking: Mechanistically Informed Interventions for Discrete Diffusion Language Models](https://arxiv.org/abs/2605.10971)

**<font color=#1a73e8>作者：</font>** Hanhan Zhou, Shamik Roy, Rashmi Gangadharaiah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion language models (DLMs) generate text by iteratively denoising all positions in parallel, offering an alternative to autoregressive models. Controlled generation methods for DLMs, imported from autoregressive models, apply uniform intervention at every denoising steps. We show this uniform schedule degrades quality, and the damage compounds when multiple attributes are steered jointly. To diagnose the failure, we train sparse autoencoders on four DLMs (124M-8B parameters) and find that different attributes commit on distinct schedules, varying in timing, sharpness, and magnitude. For instance, topic commits within the first 2\% of denoising, whereas sentiment emerges gradually over 20\% of the process. Consequently, uniform intervention wastes steering capacity on steps where the target attribute has already solidified or has yet to emerge. We propose a novel adaptive scheduler that concentrates interventions on the steps where an attribute is actively forming and leaves the rest of generation untouched. The cost-control trade-off admits a closed-form characterization: the advantage of adaptive over uniform scheduling is governed by a single dispersion statistic of the commitment distribution. Across four DLMs and seven steering tasks, our method achieves precise control without the degradation typical of uniform interventions. Especially on challenging simultaneous three-attribute control, it reaches up to 93\% steering strength, beating the strongest baseline by up to 15\% points while preserving generation quality.

---


### 2. [Rotation-Preserving Supervised Fine-Tuning](https://arxiv.org/abs/2605.10973)

**<font color=#1a73e8>作者：</font>** Hangzhan Jin, Tianwei Ni, Lu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) improves in-domain performance but can degrade out-of-domain (OOD) generalization. Prior work suggests that this degradation is related to changes in dominant singular subspaces of pretrained weight matrices. However, directly identifying loss-sensitive directions with Hessian or Fisher information is computationally expensive at LLM scale. In this work, we propose preserving projected rotations in pretrained singular subspaces as an efficient proxy for Fisher-sensitive directions, which we call Rotation-Preserving Supervised Fine-Tuning (RPSFT). RPSFT penalizes changes in the projected top-$k$ singular-vector block of each pretrained weight matrix, limiting unnecessary rotation while preserving task adaptation. Across model families and sizes trained on math reasoning data, RPSFT improves the in-domain/OOD trade-off over standard SFT and strong SFT baselines, better preserves pretrained representations, and provides stronger initializations for downstream RL fine-tuning. Code is available at \href{this https URL}{this https URL}.

---


### 3. [LEAP: Unlocking dLLM Parallelism via Lookahead Early-Convergence Token Detection](https://arxiv.org/abs/2605.10980)

**<font color=#1a73e8>作者：</font>** Haohui Zhang, Zhiye Wang, Xiaoying Gan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (dLLMs) have garnered significant attention for their potential in highly parallel processing. The parallel capabilities of existing dLLMs stem from the assumption of conditional independence at high confidence levels, which ensures negligible discrepancy between the marginal and joint distributions. However, the stringent confidence thresholds required to preserve accuracy severely constrain the scalability of parallelism. Through systematic token-level statistical analysis, we reveal that a substantial proportion of tokens converge to their correct predictions early in the denoising process yet fail to reach standard confidence thresholds, confirming that current confidence-based criteria are overly conservative. In response, we introduce LEAP (Lookahead Early-Convergence Token Detection for Accelerated Parallel Decoding). LEAP is a training-free, plug-and-play method that leverages future context filtering and multi-sequence superposition to detect early-converging tokens. By validating the alignment between early convergence and correctness, we enable reliable early decoding of these tokens. Benchmarking across diverse domains demonstrates that LEAP significantly lowers inference latency and decoding steps. Compared to confidence-based decoding, the average number of denoising steps is reduced by about 30%. On the GSM8K dataset, combining LEAP with dParallel accelerates decoding to 7.2 tokens per step while preserving model precision. LEAP effectively breaks the reliance on high-confidence priors, offering a novel paradigm for parallel decoding.

---


### 4. [Structural Interpretations of Protein Language Model Representations via Differentiable Graph Partitioning](https://arxiv.org/abs/2605.10985)

**<font color=#1a73e8>作者：</font>** Siddhant Dutta, Edward Tan Beng Wai, Soumick Sarker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein language models such as ESM-2 learn rich residue representations that achieve strong performance on protein function prediction, but their features remain difficult to interpret as structural $\&$ evolutionary signals are encoded in dense latent spaces. We propose a plug-$\&$-play framework that projects ESM-2 representations onto protein contact graphs $\&$ applies $\textbf{SoftBlobGIN}$, a lightweight Graph Isomorphism Network with differentiable Gumbel-softmax substructure pooling, to perform structure-aware message passing $\&$ learn coarse functional substructures for downstream prediction tasks. Across enzyme classification, SoftBlobGIN achieves 92.8\% accuracy $\&$ 0.898 macro-F1. Unlike post hoc analysis of protein language models alone, our method produces directly auditable structural explanations: GNNExplainer recovers biologically meaningful active-site residues, spatially localized functional clusters, $\&$ catalytic contact patterns. On binding-site detection, SoftBlobGIN improves residue AUROC from $0.885$ using an ESM-2 linear probe to $0.983$, indicating that these structural explanations are not recoverable from language-model features alone. Learned blob partitions provide an additional layer of interpretability by automatically grouping residues into functional substructures, with blobs containing annotated active-site residues showing $1.85\times$ higher importance than other blobs ($\rho{=}0.339$, $p{=}0.009$), without any active-site supervision. Our framework requires no retraining of the language model, adds only $\sim$1.1M parameters, $\&$ generalises across ProteinShake tasks, achieving $F_{\max}$ of $0.733$ on Gene Ontology prediction $\&$ AUROC of $0.969$ on binding-site detection. We position this as an interpretable structural companion to protein language models that makes their predictions more transparent $\&$ auditable.

---


### 5. [DisagMoE: Computation-Communication overlapped MoE Training via Disaggregated AF-Pipe Parallelism](https://arxiv.org/abs/2605.11005)

**<font color=#1a73e8>作者：</font>** Zhichen Zeng, Chi-Chih Chang, Jiayi Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) architectures enable trillion-parameter LLMs with sparsely activated experts. Expert parallelism (EP) is a widely adopted MoE training strategy, but it suffers from severe all-to-all communication bottlenecks, which is exaggerated by the limited inter-node network bandwidth as the growing model size requires distributing experts across GPU nodes. Prior work focused on overlapping these all-to-all communications with feed-forward network (FFN) and self-attention computations, which often leaves residual network-bound stalls due to inherent imbalance in attention and FFN layers' computation-communication ratios. We present DisagMoE, a disaggregated MoE training system that jointly optimizes model placement and scheduling for maximal efficiency. DisagMoE separates attention and FFN layers into disjoint GPU groups, introduces a multi-stage pipeline with uni-directional, many-to-many communications, and employs a computation-communication roofline model to balance GPU and network bandwidth allocation among the attention and FFN groups. DisagMoE is implemented on Megatron-LM, and evaluation shows that DisagMoE improves training efficiency across multiple MoE models with up to 1.8x speedup on 16-node 8xH800 clusters.

---


### 6. [LoopUS: Recasting Pretrained LLMs into Looped Latent Refinement Models](https://arxiv.org/abs/2605.11011)

**<font color=#1a73e8>作者：</font>** Taekhyun Park, Yongjae Lee, Dohee Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped computation shows promise in improving the reasoning-oriented performance of LLMs by scaling test-time compute. However, existing approaches typically require either training recurrent models from scratch or applying disruptive retrofits, which involve substantial computational costs and may compromise pretrained capabilities. To address these limitations, we introduce \textbf{Looped Depth Up-Scaling} (LoopUS), a post-training framework that converts a standard pretrained LLM into a looped architecture. As a key technical contribution, LoopUS recasts the pretrained LLM into an encoder, a looped reasoning block, and a decoder. It operationalizes this latent-refinement architecture through four core components: (1) block decomposition, guided by staged representation dynamics; (2) an input-dependent selective gate to mitigate hidden-state drift; (3) random deep supervision for memory-efficient learning over long recursive horizons; and (4) a confidence head for adaptive early exiting. Collectively, these mechanisms transform a standard non-looped model into a looped form while stabilizing it against both computational bottlenecks and representation collapse. Through stable latent looping, LoopUS improves reasoning-oriented performance without extending the generated traces or requiring recurrent training from scratch. For more details, see this https URL

---


### 7. [Efficient LLM Reasoning via Variational Posterior Guidance with Efficiency Awareness](https://arxiv.org/abs/2605.11019)

**<font color=#1a73e8>作者：</font>** Zizhao Chen, Yuying Li, Siting Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although large language models rely on chain-of-thought for complex reasoning, the overthinking phenomenon severely degrades inference efficiency. Existing reinforcement learning methods compress reasoning chains by designing elaborate reward functions, which renders high-quality samples extremely sparse in the exploration space and creates a sampling bottleneck for the prior policy. Inspired by cognitive science, we theoretically prove that a posterior distribution guided by reference answers achieves higher expected utility than the prior distribution, thus capable of breaking through the sampling bottleneck of high-quality samples. However, the posterior distribution is unavailable during inference. To this end, we formalize efficient reasoning as a variational inference problem and introduce an efficiency-aware evidence lower bound as the theoretical foundation. Based on this, we propose the VPG-EA framework. It adopts a parameter-shared dual-stream architecture to instantiate both the posterior distribution and the prior policy; after filtering out pseudo-efficient paths via cross-view evaluation, it unidirectionally transfers the posterior's efficient patterns to the prior policy through variational distillation. Experiments on DeepSeek-R1-Distill-Qwen-1.5B and 7B scales demonstrate that VPG-EA improves the comprehensive efficiency metric epsilon cubed by 8.73% and 12.37% over the strongest baselines on each model size, respectively.

---


### 8. [HiDream-O1-Image: A Natively Unified Image Generative Foundation Model with Pixel-level Unified Transformer](https://arxiv.org/abs/2605.11061)

**<font color=#1a73e8>作者：</font>** Qi Cai, Jingwen Chen, Chengmin Gao 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The evolution of visual generative models has long been constrained by fragmented architectures relying on disjoint text encoders and external VAEs. In this report, we present HiDream-O1-Image, a natively unified generative foundation model via pixel-space Diffusion Transformer, that pioneers a paradigm shift from modular architectures to an end-to-end in-context visual generation engine. By mapping raw image pixels, text tokens, and task-specific conditions into a single shared token space, HiDream-O1-Image achieves a structural unification of multimodal inputs within an Unified Transformer (UiT) architecture. This native encoding paradigm eliminates the need for separate VAEs or disjoint pre-trained text encoders, allowing the model to treat diverse generation and editing tasks as a consistent in-context reasoning process. Extensive experiments show that HiDream-O1-Image excels across various generation tasks, including text-to-image generation, instruction-based editing, and subject-driven personalization. Notably, with only 8B parameters, HiDream-O1-Image (8B) achieves performance parity with or even surpasses established state-of-the-art models with significantly larger parameters (e.g., 27B Qwen-Image). Crucially, to validate the immense scalability of this paradigm, we successfully scale the architecture up to over 200B parameters. Experimental results demonstrate that this massive-scale version HiDream-O1-Image-Pro (200B+) unlocks unprecedented generative capabilities and superior performance, establishing new state-of-the-art benchmarks. Ultimately, HiDream-O1-Image highlights the immense potential of natively unified architectures and charts a highly scalable path toward next-generation multimodal AI.

---


### 9. [Enabling Performant and Flexible Model-Internal Observability for LLM Inference](https://arxiv.org/abs/2605.11093)

**<font color=#1a73e8>作者：</font>** Nengneng Yu, Sixian Xiong, Yibo Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Today's inference-time workloads increasingly depend on timely access to a model's internal states. We present DMI-Lib, a high-speed deep model inspector that treats internal observability as a first-class systems primitive, decoupling it from the inference hot path via an asynchronous observability substrate built from Ring^2, a GPU-CPU memory abstraction for capturing and staging tensors, and a policy-controlled host backend that exports them. DMI-Lib enables the placement of observation points across a rich space of internal signals and diverse inference backends while preserving serving optimizations and adhering to tight GPU memory budgets. Our experiments demonstrate that DMI-Lib incurs only 0.4%--6.8% overhead in offline batch inference and an average of 6% in moderate online serving, reducing latency overhead by 2x-15x compared to existing baselines with similar observability features. DMI-Lib is open-sourced at this https URL.

---


### 10. [Birds of a Feather Flock Together: Background-Invariant Representations via Linear Structure in VLMs](https://arxiv.org/abs/2605.11107)

**<font color=#1a73e8>作者：</font>** Youssef Zaazou, Mark Thomas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs), such as CLIP and SigLIP 2, are widely used for image classification, yet their vision encoders remain vulnerable to systematic biases that undermine robustness. In particular, correlations between foreground objects and their backgrounds constitute a salient and practically important class of spurious dependencies. In this work, we revisit the well-known property of high linear additivity in VLM embedding spaces and show that it enables a decomposition of scene representations into foreground and background components. Leveraging this insight, we introduce a pre-training approach that exploits this property to construct background-invariant representations using synthetic data. Our method achieves, to our knowledge, the first worst-group accuracy exceeding $90\%$ on Waterbirds under perfect ($100\%$) spurious correlation (i.e., no minority-group examples in the training data). Furthermore, it demonstrates strong sim-to-real transfer and requires no access to real-world debiased data, making it practical for real-world deployment.

---


### 11. [GRAFT-ATHENA: Self-Improving Agentic Teams for Autonomous Discovery and Evolutionary Numerical Algorithms](https://arxiv.org/abs/2605.11117)

**<font color=#1a73e8>作者：</font>** Juan Diego Toscano, Zhaojie Chai, George Em Karniadakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific discovery can be modeled as a sequence of probabilistic decisions that map physical problems to numerical solutions. Recent agentic AI systems automate individual scientific tasks by orchestrating LLM-driven planners, solvers, and evaluators. Each method is a combination of methodological actions, with many viable combinations for any given problem and structural dependencies between choices. However, existing frameworks treat each problem in isolation, with no shared substrate to accumulate methodological experience across domains. Here we show that GRAFT-ATHENA, a self-improving agentic framework, learns from past problems and autonomously expands its own action space across diverse domains. GRAFT (Graph Reduction to Adaptive Factored Trees) projects combinatorial decision spaces into factored probabilistic trees in which each method is a single path, taking the parameter footprint from exponential to linear. In the lineage of classical Bayesian networks, the factorization is an $I$-map of the policy, and the resulting paths embed as unique fingerprints in a metric space whose closeness lets each new problem learn from similar past ones. On canonical physics-informed machine learning (PIML) benchmarks, GRAFT-ATHENA improves over human and prior agentic baselines, and on production solvers, it tackles complex engineering problems such as reconstructing Mach-10 flow over the Apollo Command Module from a 1968 report and recovering shear-thinning blood-cell rheology. Notably, the system grows its own knowledge substrate, autonomously proposing regularization constraints for ill-posed inverse problems and discovering new numerical methods such as a spectral PINN with exponential convergence. These results provide a foundation for autonomous laboratories that grow more capable with every problem they solve.

---


### 12. [Language Modeling with Hyperspherical Flows](https://arxiv.org/abs/2605.11125)

**<font color=#1a73e8>作者：</font>** Justin Deschenaux, Caglar Gulcehre  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete Diffusion Language Models progressed rapidly as an alternative to autoregressive (AR) models, motivated by their parallel generation abilities. However, for tractability, discrete diffusion models sample from a factorized distribution, which is less expressive than AR. Recent Flow Language Models (FLMs) apply continuous flows to language, transporting noise to data with a deterministic ODE that avoids factorized sampling. FLMs operate on one-hot vectors whose dimension scales with the vocabulary size, making FLMs costly to train. Moreover, since all distinct one-hot embeddings are equidistant in $\ell_2$, adding Gaussian noise does not have a clear semantic interpretation (unlike images, where Gaussian noise progressively degrades structure). We introduce $\mathbb{S}$-FLM, a latent FLM in the hypersphere. $\mathbb{S}$-FLM generates sequences by rotating vectors in $\mathbb{S}^{d-1}$ along a velocity field learned with cross-entropy, avoiding the overhead of materializing one-hot vectors. Previous FLMs match AR in Generative Perplexity (Gen.\ PPL), but samples with high likelihood are not necessarily correct in verifiable domains such as math and code. $\mathbb{S}$-FLM substantially improves continuous flow language models on large-vocabulary reasoning and closes the gap to masked diffusion under standard-temperature sampling ($T=1$), while a gap remains under optimized low-temperature ($T=0.1$) decoding.

---


### 13. [Sampling More, Getting Less: Calibration is the Diversity Bottleneck in LLMs](https://arxiv.org/abs/2605.11128)

**<font color=#1a73e8>作者：</font>** Amin Banayeeanzade, Qingchuan Yang, Dhruv Tarsadiya 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diversity is essential for language-model applications ranging from creative generation to scientific discovery, yet modern LLMs often collapse into a narrow subset of plausible outputs. While prior work has developed benchmarks for measuring this lack of diversity, less is known about how the step-by-step probability distributions at inference time cause the problem. We introduce a validity--diversity framework that attributes diversity collapse to how an LLM allocates probability mass across valid and invalid continuations during decoding. This framework decomposes the bottleneck into two complementary forms of miscalibration. First, order calibration: valid tokens are not reliably ranked above invalid tokens, so rank-based cutoff rules must trade off between recovering valid continuations and admitting invalid ones. Second, shape calibration: probability mass is overly concentrated only on few valid continuations while having a heavy-tail of mixed valid and invalid tokens, so maintaining high validity limits diversity. We formalize both mechanisms and show that local failures compound across decoding steps, producing strong sequence-level losses in diversity. Empirically, we develop controlled diagnostics for probing these bottlenecks, including tasks with exactly known valid sets and oracle cutoff baselines. Across 14 language models spanning multiple families and scales, we find that diversity collapse is not merely a limitation of particular sampling heuristics, but a consequence of order and shape miscalibration in the LLM distribution.

---


### 14. [ClinicalBench: Stress-Testing Assertion-Aware Retrieval for Cross-Admission Clinical QA on MIMIC-IV](https://arxiv.org/abs/2605.11143)

**<font color=#1a73e8>作者：</font>** Alex Stinard  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning benchmarks measure clinical performance on clean inputs. We evaluate the step before reasoning: retrieval over real EHR notes, where negation, temporality, and family-versus-patient attribution can flip a correct answer to a wrong one. EpiKG carries an assertion label and a temporality tag with every fact in a patient knowledge graph, then routes retrieval by question intent. ClinicalBench is a 400-question test over 43 MIMIC-IV patients across 9 assertion-sensitive categories. A 7-condition ablation tests each piece of EpiKG across six LLMs (Claude Opus 4.6, GPT-OSS 20B, MedGemma 27B, Gemma 4 31B, MedGemma 1.5 4B, Qwen 3.5 35B). Three physicians blindly adjudicated 100 paired items. The author-blind primary endpoint, leave-author-out paired exact McNemar on 50 unanimous-strict items rated by two external physicians, yields +22.0 percentage points (95 percent Newcombe CI [+5.1, +31.5], p=0.0192). The architectural novelty, intent-aware KG-RAG over a Contriever dense-RAG baseline (C2b to C4g_kw on the change-excluded n=362 endpoint), is +8.84 percentage points (paired McNemar p=1.79e-3); +12.43 percentage points under oracle intent. Sensitivities agree directionally: three-rater physician majority +24.0 percentage points (subject to single-author circularity); deterministic keyword reproducibility proxy +39.5 percentage points. Across the six models, the gain shrinks as the LLM-alone baseline rises (beta=-1.123, r=-0.921, p=0.009). With n=6 this looks more like regression to the mean than encoding substituting for model size. Physician adjudication identified 56 percent of auto-generated reference answers as defective, a methodological finding indicating that NLP-pipeline clinical-QA benchmarks require physician adjudication to be usable. ClinicalBench, the frozen evaluator, three-rater adjudication data, and the EpiKG output stack are publicly released.

---


### 15. [The Bicameral Model: Bidirectional Hidden-State Coupling Between Parallel Language Models](https://arxiv.org/abs/2605.11167)

**<font color=#1a73e8>作者：</font>** Cedric Flamant, Udaya Ghai, Kanna Shimizu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing multi-model and tool-augmented systems communicate by generating text, serializing every exchange through the output vocabulary. Can two pretrained language models instead coordinate through a continuous, concurrent channel? The Bicameral Model couples two frozen language models through a trainable neural interface on their intermediate hidden states. At every generation step, both models run in lockstep: a primary model drives the task while an auxiliary model operates tools, solves constraints, or executes code, with both conditioning on each other's activations through a translation network and a learned suppression gate ($\sim$1\% of combined parameters). The gate learns a selective communication protocol from task loss alone, without a prescribed format. We demonstrate the mechanism across three tool backends. On arithmetic, coupling two 0.5B models with a calculator raises accuracy from 36\% to 96\%. On logic grid puzzles, coupling two 0.6B models with a Z3 solver achieves $1.7\times$ the unaugmented baseline on ZebraLogic. On mathematical reasoning, coupling with a Python sandbox enables the auxiliary to generate problem-specific code from hidden-state signals alone, without ever seeing the problem text.

---


### 16. [OLIVIA: Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents](https://arxiv.org/abs/2605.11169)

**<font color=#1a73e8>作者：</font>** Sheldon Yu, Junda Wu, Xintong Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents interleave reasoning, action selection, and observation to solve sequential decision-making tasks. In deployed settings where agents repeatedly handle related multi-step tasks, small action-selection errors can accumulate into wasted tool calls, latency, and reduced reliability. Despite this need for deployment-time improvement, existing inference-time adaptation methods for LLM agents mainly rely on prompting or retrieval, which influence behavior indirectly through context manipulation. For ReAct-style agents, such approaches do not expose an explicit decision layer that can score candidate actions, represent uncertainty, or be updated online from action-level feedback. As a result, they provide limited support for trackable, fine-grained, and uncertainty-aware adaptation during deployment. We propose OLIVIA, an inference-time action adaptation framework for ReAct-style agents. OLIVIA models the LLM's final action-selection layer as a contextual linear bandit over candidate actions, with frozen hidden states as decision contexts. This choice is particularly suitable for deployment because it adapts behavior directly at the action-selection interface, preserves the underlying reasoning process, and provides explicit uncertainty estimates and lightweight online updates from action-level feedback. With upper-confidence-bound exploration, OLIVIA improves the policy sample-efficiently with minimal computational overhead. We instantiate OLIVIA on four benchmarks and show that it consistently improves task performance over static ReAct and prompt-based inference-time baselines. Our results suggest that explicit online decision layers provide an effective alternative to purely prompt- or retrieval-based adaptation for LLM agents during deployment.

---


### 17. [Optimistic Dual Averaging Unifies Modern Optimizers](https://arxiv.org/abs/2605.11172)

**<font color=#1a73e8>作者：</font>** Thomas Pethick, Wanyun Xie, Roman Machacek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce SODA, a generalization of Optimistic Dual Averaging, which provides a common perspective on state-of-the-art optimizers like Muon, Lion, AdEMAMix and NAdam, showing that they can all be viewed as optimistic instances of this framework. Based on this framing, we propose a practical SODA wrapper for any base optimizer that eliminates weight decay tuning through a theoretically-grounded $1/k$ decay schedule. Empirical results across various scales and training horizons show that SODA consistently improves performance without any additional hyperparameter tuning.

---


### 18. [The Many Faces of On-Policy Distillation: Pitfalls, Mechanisms, and Fixes](https://arxiv.org/abs/2605.11182)

**<font color=#1a73e8>作者：</font>** Siqi Zhu, Xuyan Ye, Hongyu Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) and on-policy self-distillation (OPSD) have emerged as promising post-training methods for large language models, offering dense token-level supervision on trajectories sampled from the model's own policy. However, existing results on their effectiveness remain mixed: while OP(S)D has shown promise in system prompt and knowledge internalization, recent studies also report instability and degradation. In this work, we present a comprehensive empirical study of when OPD and OPSD work, when they fail, and why. We find that OPD on mathematical reasoning is highly sensitive to teacher choice and loss formulation, whereas OPSD fails in our tested settings due to test-time absence of instance-specific privileged information (PI). In contrast, OPSD is effective when PI represents a shared latent rule, such as a system prompt or alignment preference. We identify three failure mechanisms: (1) distribution mismatch between teacher and student caused by conditioning on student-generated prefixes, (2) optimization instability from biased TopK reverse-KL gradients, and (3) an OPSD-specific limitation where the student learns a PI-free policy that aggregates PI-conditioned teachers, which is insufficient when PI is instance-specific. We further show that stop-gradient TopK objectives, RLVR-adapted teachers, and SFT-stabilized students mitigate these failures.

---


### 19. [CATS: Cascaded Adaptive Tree Speculation for Memory-Limited LLM Inference Acceleration](https://arxiv.org/abs/2605.11186)

**<font color=#1a73e8>作者：</font>** Yuning Han, Yangchenchen Jin, Dylan Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auto-regressive decoding in Large Language Models (LLMs) is inherently memory-bound: every generation step requires loading the model weights and intermediate results from memory (e.g., High-Bandwidth Memory (HBM) for GPU servers), making throughput bottlenecked by memory bandwidth rather than compute. Speculative decoding addresses this by enabling parallel verification of multiple draft tokens, effectively amortizing the cost of each target-model call. However, existing speculative decoding methods are designed under the assumption that HBM is sufficiently large to hold both the target model and an auxiliary draft model simultaneously -- an assumption that breaks down on memory-constrained devices such as edge platforms with limited DRAM. We analyze the inference bottleneck in this memory-limited regime and propose CATS, a self-speculative decoding framework that conducts cascaded verification and correction based on the memory budget and parameter offloading patterns on memory-limited devices. This design maximizes token acceptance rate and end-to-end speedup while keeping the peak memory footprint on the device equal to that of the target model alone. We evaluate CATS on different models across five benchmarks on real edge devices. CATS can achieve a wall-clock speedup of up to 5.08x with no degradation in generation quality, outperforming the SOTA method by up to 1.45x under edge memory constraints.

---


### 20. [How Does Differential Privacy Affect Social Bias in LLMs? A Systematic Evaluation](https://arxiv.org/abs/2605.11195)

**<font color=#1a73e8>作者：</font>** Eduardo Tenorio, Karuna Bhaila, Xintao Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) trained on web-scale corpora can memorize sensitive training data, posing significant privacy risks. Differential privacy (DP) has emerged as a principled framework that limits the influence of individual data points during training, yet the relationship between differential privacy and social bias in LLMs remains poorly understood. To investigate this, we present a systematic evaluation of social bias in a pretrained LLM trained with DP-SGD, comparing a DP model against non-DP baselines across four complementary paradigms: sentence scoring, text completion, tabular classification, and question answering. We find that DP reduces bias in sentence scoring tasks, where bias is measured through controlled likelihood comparisons, yet this improvement does not generalize across all tasks. Our results reveal a discrepancy between logit-level bias and output-level bias. Moreover, decreasing memorization does not necessarily reduce unfairness, underscoring the importance of multi-paradigm evaluation when assessing fairness in LLMs.

---


### 21. [The Scaling Law of Evaluation Failure: Why Simple Averaging Collapses Under Data Sparsity and Item Difficulty Gaps, and How Item Response Theory Recovers Ground Truth Across Domains](https://arxiv.org/abs/2605.11205)

**<font color=#1a73e8>作者：</font>** Jung Min Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmark evaluation across AI and safety-critical domains overwhelmingly relies on simple averaging. We demonstrate that this practice produces substantially misleading rankings when two conditions co-occur: (1) the evaluation matrix is sparse and (2) items vary substantially in difficulty. Through controlled simulation experiments across four domains -- NLP (GLUE), clinical drug trials, autonomous vehicle safety, and cybersecurity -- we show that Spearman rank correlation $\rho$ between simple-average rankings and ground-truth rankings degrades from $\rho = 1.000$ at 100% coverage to $\rho = 0.809$ at 67% coverage with high difficulty heterogeneity (mean over 20 seeds). A standard two-parameter logistic (2PL) Item Response Theory (IRT) model maintains $\rho \geq 0.996$ across all conditions. A 150-condition grid sweep over sparsity $S \in [0, 0.70]$ and difficulty gap $D \in [0.5, 5.0]$ confirms that ranking error forms a failure surface with a strong $S \times D$ interaction ($\gamma_3 = +0.20$, $t = 13.05$), while IRT maintains $\rho \geq 0.993$ throughout. We discuss implications for Physical AI benchmarking, where evaluation matrices are often incomplete and difficulty gaps are extreme.

---


### 22. [Hi-GaTA: Hierarchical Gated Temporal Aggregation Adapter for Surgical Video Report Generation](https://arxiv.org/abs/2605.11208)

**<font color=#1a73e8>作者：</font>** Kedi Sun, Chaohui Dang, Yue Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated, clinician-grade assessment reports for surgical procedures could reduce documentation burden and provide objective feedback, yet remain challenging due to the difficulty of aligning dense spatio-temporal video representations with language-based reasoning and the scarcity of high-quality, privacy-preserving datasets. To address this gap, we establish a benchmark comprising 214 high-quality simulated surgical videos paired with surgeon-authored evaluation reports. Building on this resource, we propose a Perception-Alignment-Reasoning framework for surgical video report generation, featuring Hi-GaTA, a novel lightweight temporal adapter that efficiently compresses long video sequences into compact, LLM-compatible visual prefix tokens through short-to-long-range temporal aggregation. For robust visual perception, we pretrain Sur40k, a surgical-specific ViViT-style video encoder on 40,000 minutes of public surgical videos to capture fine-grained spatio-temporal procedural priors. Hi-GaTA employs a temporal pyramid with text-conditioned dual cross-attention, and improves multi-scale consistency through cross-level gated fusion and an increasing-depth strategy. Finally, we fine-tune the LLM backbone using LoRA to enable coherent and stylistically consistent surgical report generation under limited supervision. Experiments show our approach achieves the best overall performance, with consistent gains over strong Multimodal Large Language Model (MLLM) baselines. Ablation studies further validate the effectiveness of each proposed component.

---


### 23. [Measuring Five-Nines Reliability: Sample-Efficient LLM Evaluation in Saturated Benchmarks](https://arxiv.org/abs/2605.11209)

**<font color=#1a73e8>作者：</font>** Eungyeup Kim, Chenchen Gu, Vashisth Tiwari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While existing benchmarks demonstrate the near-perfect performance of large language models (LLMs) on various tasks, this apparent saturation often obscures the need for rigorous evaluation of their reliability. In real-world deployment, however, achieving extremely high reliability (e.g., "five-nines" (99.999%) vs. "three-nines" (99.9%)) is fundamentally critical, as this gap results in an order-of-magnitude increase in failures, which is catastrophic in reliability-critical applications. Still, estimating such a rare failure probability with tight confidence bounds requires prohibitively large LLM inference sizes, making standard Monte Carlo evaluation infeasible under limited compute budgets. In this paper, we observe that LLM failures exhibit strong systematic patterns: across broad parameterized input spaces, a small subset of inputs disproportionately accounts for the majority of failures. Leveraging this observation, we propose to learn a sampling distribution concentrated on failure-prone inputs via the cross-entropy method (CEM). We evaluate our framework on three LLMs, Qwen2.5-Math-7B-Instruct, gpt-oss-20b-low, and Gemini 2.5 Flash Lite, across parameterized GSM8K templates and achieve up to 156.22x reduction in required inferences compared to naive uniform sampling. Our estimates reveal that models with indistinguishable accuracy on standard benchmarks can differ substantially in estimated failure rates, underscoring that reliability is a distinct and measurable axis of model quality. Our simple yet practical framework enables the evaluation of extreme reliability in LLMs, a distinct and underexplored dimension of evaluation beyond existing benchmarks, for their growing use in reliability-sensitive applications.

---


### 24. [ReVision: Scaling Computer-Use Agents via Temporal Visual Redundancy Reduction](https://arxiv.org/abs/2605.11212)

**<font color=#1a73e8>作者：</font>** Amirhossein Abaskohi, Yuhang He, Peter West 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computer-use agents~(CUAs) rely on visual observations of graphical user interfaces, where each screenshot is encoded into a large number of visual tokens. As interaction trajectories grow, the token cost increases rapidly, limiting the amount of history that can be incorporated under fixed context and compute budgets. This has resulted in no or very limited improvement in the performance when using history unlike other domains. We address this inefficiency by introducing ReVision, which is used to train multimodal language models on trajectories where redundant visual patches are removed using a learned patch selector that compares patch representations across consecutive screenshots while preserving spatial structure required by the model. Across three benchmarks, OSWorld, WebTailBench, and AgentNetBench, when processing trajectories with 5 history screenshots using Qwen2.5-VL-7B, ReVision reduces token usage by approximately 46% on average while improving success rate by 3% over the no drop baseline. This establishes a clear efficiency gain, enabling agents to process longer trajectories with fewer tokens. With this improved efficiency, we revisit the role of history in CUAs and find that performance continues to improve as more past observations are incorporated when redundancy is removed. This suggests that the commonly observed saturation in visual history is not due to limited usefulness of past information, but rather a consequence of inefficient token representations.

---


### 25. [Leveraging RAG for Training-Free Alignment of LLMs](https://arxiv.org/abs/2605.11217)

**<font color=#1a73e8>作者：</font>** John T. Halloran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) alignment algorithms typically consist of post-training over preference pairs. While such algorithms are widely used to enable safety guardrails and align LLMs with general human preferences, we show that state-of-the-art alignment algorithms require significant computational resources while being far less capable of enabling refusal guardrails for recent agentic attacks. Thus, to improve refusal guardrails against such attacks without drastically increasing computational overhead, we introduce Retrieval Augmented Generation for Pref erence alignment (RAG-Pref), a simple RAG-based alignment algorithm which conditions on preferred and dispreferred samples to leverage contrastive information during inference. RAG-Pref is online (training-free), compatible with off-the-shelf packages, and, when combined with offline (training-based) alignment algorithms, enables more than an average 3.7 factor improvement in agentic attack refusals across five widely used LLMs, compared to 2.9 for other online alignment algorithms and 1.5 for offline alignment alone. We conclude by showing that, in stark contrast to other online alignment methods, RAG-Pref similarly increases performance on general human-preference alignment tasks and does not drastically increase overall computational requirements.

---


### 26. [ADMM-Q: An Improved Hessian-based Weight Quantizer for Post-Training Quantization of Large Language Models](https://arxiv.org/abs/2605.11222)

**<font color=#1a73e8>作者：</font>** Ryan Lucas, Mehdi Makni, Xiang Meng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization is an effective strategy to reduce the storage and computation footprint of large language models (LLMs). Post-training quantization (PTQ) is a leading approach for compressing LLMs. Popular weight quantization procedures, including GPTQ and RTN, suffer in model utility, especially at aggressive quantization levels (sub-4-bit). We propose ADMM-Q, a novel weight quantization algorithm that considers the layer-wise quantization problem. Our algorithm is based on a combinatorial variant of the Alternating Direction Method of Multipliers (ADMM). Our operator-splitting procedure updates weights continuously to minimize the layer-wise reconstruction error, while gradually enforcing the quantization constraints with convergence guarantees. We propose additional algorithmic enhancements (e.g., penalty scheduling, preconditioning, and a local search post-processing step) to make ADMM-Q efficient at LLM scale. ADMM-Q is modular and can be used as a drop-in replacement for any weight quantizer within existing quantization pipelines: ADMM-Q is fully composable with existing techniques including range clipping, learned or random rotations, and activation scaling. Using ADMM-Q in place of GPTQ on Qwen3-8B, we decrease WikiText-2 perplexity in: (i) the W3A16 weight-only setting (12.85 $\rightarrow$ 10.06); (ii) the W4A8 SmoothQuant procedure (9.29 $\rightarrow$ 8.68); and (iii) the W2A4KV4 SpinQuant procedure (66.11 $\rightarrow$ 19.42).

---


### 27. [PIVOT: Bridging Planning and Execution in LLM Agents via Trajectory Refinement](https://arxiv.org/abs/2605.11225)

**<font color=#1a73e8>作者：</font>** Tuo Zhang, Alin-Ionut Popa, Yan Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents frequently generate seemingly coherent plans that fail upon execution due to infeasible actions, constraint violations, and compounding errors over extended horizons. PIVOT (Plan-Inspect-eVOlve Trajectories) addresses this plan-execution misalignment through a self-supervised framework that treats trajectories as optimizable objects iteratively refined via environment interaction. The framework comprises four stages: PLAN generates candidate trajectories; INSPECT executes them and computes structured losses with textual gradients encoding plan-execution discrepancies; EVOLVE applies these signals to produce improved trajectories; and VERIFY performs a final global check against task constraints. A monotonic acceptance process ensures a non-decreasing solution quality. Empirical evaluations on DeepPlanning and GAIA demonstrate state-of-the-art performance: with human-in-the-loop (HITL) feedback, PIVOT establishes a strong upper bound up to 94% relative improvement in constraint satisfaction, while its fully autonomous variant retains substantial gains, showing that the core trajectory-refinement mechanism remains effective without external supervision. At the same time, PIVOT remains computationally efficient, requiring up to 3x to 5x fewer tokens than competing refinement methods. These findings establish that (self- or human-supervised) feedback-based trajectory optimization is a principled methodology for mitigating plan-execution gaps in autonomous agent systems.

---


### 28. [Rethinking LLMOps for Fraud and AML: Building a Compliance-Grade LLM Serving Stack](https://arxiv.org/abs/2605.11232)

**<font color=#1a73e8>作者：</font>** Prathamesh Vasudeo Naik, Naresh Dintakurthi, Yue Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fraud detection and anti-money-laundering (AML) compliance are high-value domains for large language models (LLMs), but their serving requirements differ sharply from generic chat workloads. Compliance prompts are often prefix-heavy, schema-constrained, and evidence-rich, combining reusable policy instructions, risk taxonomies, transaction or document context, and short structured outputs such as JSON labels or risk factors. These properties make prefix reuse, KV-cache efficiency, runtime tuning, model orchestration, and output validation first-order systems concerns. This paper introduces a workload-aware LLMOps stack for fraud and AML workloads using self-hosted open-weight models such as Meta Llama and Alibaba Qwen. The stack combines vLLM-style runtime tuning, PagedAttention, Automatic Prefix Caching, multi-adapter serving, adapter and prompt-length-aware batching, sleep/wake lifecycle management, speculative decoding, and optional prefill/decode disaggregation. To avoid exposing institution-specific data, the reproducibility track converts public synthetic AML datasets, including IBM AML and SAML-D, into prefix-heavy compliance prompts with reusable policy text, transaction evidence, typology definitions, and schema-constrained outputs. We also incorporate an LLM-as-judge quality gate using deterministic compliance checks, reference metrics, expert-adjudicated calibration data where available, and multi-judge rubric scoring. Across public-synthetic AML workloads and controlled serving benchmarks, workload-aware tuning improved throughput from 612-650 to 3,600 requests/hour, reduced P99 latency from 31-38 seconds to 6.4-8.7 seconds, and increased GPU utilization from 12% to 78%. These results show that regulated LLM performance is a workload-design, serving-optimization, and quality-gating problem, not only a model-selection problem.

---


### 29. [The Semantic Training Gap: Ontology-Grounded Tool Architectures for Industrial AI Agent Systems](https://arxiv.org/abs/2605.11234)

**<font color=#1a73e8>作者：</font>** Grama Chethan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based AI agents are increasingly deployed in manufacturing environments for analytics, quality management, and decision support. These agents demonstrate statistical fluency with domain terminology but lack grounded understanding of operational semantics -- the relational structure that connects equipment identifiers, process parameters, failure codes, and regulatory constraints within a specific production context. This paper identifies and formalizes the semantic training gap: a structural disconnect between how AI systems acquire domain vocabulary through training and how manufacturing operations define meaning through ontological relationships. We demonstrate that this gap causes operationally incorrect outputs even when model responses are linguistically precise, and that in multi-agent configurations it produces a compounding failure mode we term semantic drift. To close this gap, we present an architecture that embeds manufacturing ontology directly into the AI tool layer as a typed relational configuration, enforcing semantic constraints at runtime rather than relying on model training. The architecture is formalized as a three-operation interface contract -- resolve, contextualize, annotate -- with invariants enforced by an AIOps orchestration layer. In a controlled experiment across six industry configurations (72 tool invocations using Qwen3-32B), unconstrained tool parameters produced a 43% hallucination rate for domain identifiers; ontology-grounded parameters reduced this to 0%. We validate the approach through a digital twin analytics platform demonstrating that a single codebase with domain-specific ontology configurations eliminates tool-call hallucination and achieves cross-domain configurability without application code changes.

---


### 30. [Internalizing Curriculum Judgment for LLM Reinforcement Fine-Tuning](https://arxiv.org/abs/2605.11235)

**<font color=#1a73e8>作者：</font>** Han Zheng, Yining Ma, Karthick Gunasekaran 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In LLM Reinforcement Fine-Tuning (RFT), curriculum learning drives both efficiency and performance. Yet, current methods externalize curriculum judgment via handcrafted heuristics or auxiliary models, risking misalignment with the policy's training dynamics. In this paper, we introduce METIS (METacognitive Internalized Self-judgment), a novel framework that internalizes curriculum judgment as a native capability. Leveraging a critical observation that within-prompt reward variance effectively gauges prompt informativeness, METIS predicts this metric based on recent training outcomes as lightweight in-context learning examples. This intrinsic self-judgment then dynamically dictates the training allocation. Moreover, METIS closes the loop between judgment and optimization by jointly optimizing the standard RFT rewards and a self-judgment reward. This allows the policy to learn what to learn next, as a form of metacognition. Across extensive discrete and continuous RFT benchmarks from mathematical reasoning, code generation, to agentic function-calling, METIS consistently delivers superior performance while accelerating convergence by up to 67%. By bypassing handcrafted heuristics and auxiliary models, our work establishes a simple, closed-loop, and highly efficient curriculum internalization paradigm for LLM reinforcement fine-tuning.

---


### 31. [HEBATRON: A Hebrew-Specialized Open-Weight Mixture-of-Experts Language Model](https://arxiv.org/abs/2605.11255)

**<font color=#1a73e8>作者：</font>** Noam Kayzer, Dan Revital, Ori Bar Joseph 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Hebatron, a Hebrew-specialized open-weight large language model built on the NVIDIA Nemotron-3 sparse Mixture-of-Experts architecture. Training employs a three-phase easy-to-hard curriculum with continuous anti-forgetting anchoring, followed by supervised fine-tuning on 2 million bilingual Hebrew--English samples. The curriculum ordering alone yields a 3-point aggregate benchmark gain over the reversed configuration. Hebatron achieves a Hebrew reasoning average of 73.8\%, outperforming DictaLM-3.0-24B-Thinking (68.9\%) and remaining competitive with Gemma-3-27B-IT on GSM8K-HE and Israeli Trivia, while activating only 3B parameters per forward pass across a 30B-parameter model, delivering approximately 9 times higher inference throughput at native context lengths up to 65,536 tokens. To our knowledge, this is the first language-specific adaptation of the Nemotron-3 architecture for any target language, and the first open-weight Hebrew-specialized MoE model with native long-context support. Model weights are released openly to support further research in Hebrew and Semitic-language NLP.

---


### 32. [Unlocking LLM Creativity in Science through Analogical Reasoning](https://arxiv.org/abs/2605.11258)

**<font color=#1a73e8>作者：</font>** Andrew Shen, Shaul Druckmann, James Zou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous science promises to augment scientific discovery, particularly in complex fields like biomedicine. However, this requires AI systems that can consistently generate novel and diverse solutions to open-ended problems. We evaluate LLMs on the task of open-ended solution generation and quantify their tendency to mode collapse into low-diversity generations. To mitigate this mode collapse, we introduce analogical reasoning (AR) as a new approach to solution generation. AR generates analogies to cross-domain problems based on shared relational structure, then uses those analogies to search for novel solutions. Compared to baselines, AR discovers significantly more diverse generations (improving solution diversity metrics by 90-173%), generates novel solutions over 50% of the time (compared to as little as 1.6% for baselines), and produces high-quality analogies. To validate the real-world feasibility of AR, we implement AR-generated solutions across four biomedical problems, yielding consistent quantitative gains. AR-generated approaches achieve a nearly 13-fold improvement on distributional metrics for perturbation effect prediction, outperform all baselines on AUPRC when predicting cell-cell communication, infer brain region interactions with a high Spearman correlation ($\rho$=0.729) to published methods, and establish state-of-the-art performance on 2 datasets for oligonucleotide property prediction. The novel and diverse solutions produced by AR can be used to augment the search space of existing solution generation methods.

---


### 33. [Template-as-Ontology: Configurable Synthetic Data Infrastructure for Cross-Domain Manufacturing AI Validation](https://arxiv.org/abs/2605.11259)

**<font color=#1a73e8>作者：</font>** Grama Chethan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLarge language model (LLM)-based AI agents deployed in manufacturing environments require populated, schema-correct data for validation, yet production MES data is proprietary, privacy-encumbered, and vendor-specific. This paper introduces the Template-as-Ontology principle: a single Python configuration module (700-770 lines, 45 validated exports) serves simultaneously as the specification for a time-stepped manufacturing simulator and as the runtime domain schema for AI analytics tools, producing alignment by construction rather than integration. We formally define the domain template as a typed relational configuration schema and prove that structural alignment between simulation and tool layers is guaranteed by single-source consumption. A five-layer pipeline--simulation, PostgreSQL, CDC/Iceberg lakehouse, star schema, and 12 parameterized AI tools--generates causally coherent, MES-shaped data spanning 66 entity types across four operational domains mapped to ISA-95/IEC 62264. We validate the architecture with six industry templates (aerospace, pharma, automotive, electronics, beverages, warehousing) running on identical framework code. Calibration experiments (60 runs, 10 seeds per template) confirm parametric controllability: observed KPIs fall within configured ranges across all templates. A controlled hallucination experiment (72 tool invocations, Qwen3-32B) demonstrates that ontology-constrained parameters eliminate tool-parameter fabrication (0% constrained vs. 43% unconstrained hallucination rate for the evaluated model, Fisher's exact test p < 10^-12); the 0% constrained rate is an architectural guarantee that holds for any model. The framework provides a reusable data layer for discrete manufacturing AI validation.

---


### 34. [Curriculum Learning-Guided Progressive Distillation in Large Language Models](https://arxiv.org/abs/2605.11260)

**<font color=#1a73e8>作者：</font>** Jincheng Cao, Fanzhi Zeng, Leqi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation is a key technique for transferring the capabilities of large language models (LLMs) into smaller, more efficient student models. Existing distillation approaches often overlook two critical factors: the learning order of training data and the capacity mismatch between teacher and student models. This oversight limits distillation performance, as manifested by the counter-intuitive phenomenon where stronger teachers fail to produce better students. In this work, we propose Curriculum Learning-Guided Progressive Distillation (CLPD), a unified framework that explicitly accounts for both factors by aligning data difficulty with teacher strength. CLPD constructs an explicit curriculum by organizing training examples from easy to hard, while simultaneously applying an implicit curriculum over supervision signals by progressively scheduling teachers of increasing capacity. Our framework is modular and can be integrated into standard distillation algorithms with minimal overhead. Empirical results on the reasoning benchmarks demonstrate that CLPD consistently outperforms standard distillation, data ordering alone, and teacher scheduling alone across multiple settings. These findings highlight the importance of jointly considering data ordering and teacher capacity when distilling reasoning abilities into small language models.

---


### 35. [Quotient-Categorical Representations for Bellman-Compatible Average-Reward Distributional Reinforcement Learning](https://arxiv.org/abs/2605.11289)

**<font color=#1a73e8>作者：</font>** Ege C. Kaya, Aliasghar Pourghani, Vijay Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Average-reward reinforcement learning requires estimating the gain and the bias, which is defined only up to an additive constant. This makes direct distributional analogues ill-posed on the real line. We introduce a quotient-space formulation in which state-indexed bias laws are identified up to a common translation, together with a categorical parameterization that respects this symmetry. On this quotient-categorical space, we define a projected average-reward distributional operator and show that it is well-defined, non-expansive in a coordinate Cramér metric, and admits fixed points. We then study sampled recursions whose mean-field maps are asynchronous relaxations of this operator. In an idealized centered-reward setting, a one-state temporal-difference update enjoys almost sure convergence together with finite-iteration residual bounds under both i.i.d. and Markovian sampling. When the gain is unknown, we augment the recursion with an online gain estimator, and prove non-expansiveness and Markovian convergence of the resulting coupled scheme. Finally, we show that synchronous exact updates are gain-independent at the quotient-law level, isolating a structural contrast between ideal quotient distributions and practical fixed-grid categorical representations.

---


### 36. [ReAD: Reinforcement-Guided Capability Distillation for Large Language Models](https://arxiv.org/abs/2605.11290)

**<font color=#1a73e8>作者：</font>** Xueqi Cheng, Xugui Zhou, Tyler Derr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Capability distillation applies knowledge distillation to selected model capabilities, aiming to compress a large language model (LLM) into a smaller one while preserving the abilities needed for a downstream task. However, most existing methods treat capabilities as independent training targets and overlook how improving one capability can reshape the student's broader capability profile, especially when multiple abilities jointly determine task success. We study capability distillation under a fixed token budget and identify two consistent patterns: distillation induces systematic, budget-dependent cross-capability transfer, and additional budget often brings limited task-relevant gains while sometimes degrading other useful abilities. Building on these insights, we propose ReAD, a Reinforcement-guided cApability Distillation framework that explicitly accounts for capability interdependence. ReAD first infers task-essential capabilities, then generates capability-targeted supervision on the fly, and finally uses an uncertainty-aware contextual bandit to adaptively allocate the distillation budget based on expected utility gains. Extensive experiments show that ReAD improves downstream utility under the same token budget while reducing harmful spillover and wasted distillation effort compared to strong baselines. Our code is publicly available at this https URL.

---


### 37. [LatentRouter: Can We Choose the Right Multimodal Model Before Seeing Its Answer?](https://arxiv.org/abs/2605.11301)

**<font color=#1a73e8>作者：</font>** Xueqi Cheng, Yushun Dong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have heterogeneous strengths across OCR, chart understanding, spatial reasoning, visual question answering, cost, and latency. Effective MLLM routing therefore requires more than estimating query difficulty: a router must match the multimodal requirements of the current image-question input with the capabilities of each candidate model. We propose LatentRouter, a router that formulates MLLM routing as counterfactual multimodal utility prediction. Given an image-question query, LatentRouter extracts learned multimodal routing capsules, represents each candidate MLLM with a model capability token, and performs latent communication between these states to estimate how each model would perform if selected. A distributional outcome head predicts model-specific counterfactual quality, while a bounded capsule correction refines close decisions without allowing residual signals to dominate the prediction. The resulting utility-based policy supports performance-oriented and performance-cost routing, and handles changing candidate pools through shared per-model scoring with availability masking. Experiments on MMR-Bench and VL-RouterBench show that LatentRouter outperforms fixed-model, feature-level, and learned-router baselines. Additional analyses show that the gains are strongest on multimodal task groups where model choice depends on visual, layout-sensitive, or reasoning-oriented requirements, and that latent communication is the main contributor to the improvement. The code is available at: this https URL.

---


### 38. [Predicting Psychological Well-Being from Spontaneous Speech using LLMs](https://arxiv.org/abs/2605.11303)

**<font color=#1a73e8>作者：</font>** Erfan Loweimi, Sofia de la Fuente Garcia, Saturnino Luz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate the use of Large Language Models (LLMs) for zero-shot prediction of Ryff Psychological Well-Being (PWB) scores from spontaneous speech. Using a few minutes of voice recordings from 111 participants in the PsyVoiD database, we evaluated 12 instruction-tuned LLMs, including Llama-3 (8B, 70B), Ministral, Mistral, Gemma-2-9B, Gemma-3 (1B, 4B, 27B), Phi-4, DeepSeek (Qwen and Llama), and QwQ-Preview. A domain-informed prompt was developed in collaboration with experts in clinical psychology and linguistics. Results show that LLMs can extract semantically meaningful cues from spontaneous speech, achieving Spearman correlations of up to 0.8 on 80\% of the data. Additionally, to enhance explainability, we conducted statistical analyses to characterise prediction variability and systematic biases, alongside keyword-based word cloud analyses to highlight the linguistic features driving the models' predictions.

---


### 39. [CheXTemporal: A Dataset for Temporally-Grounded Reasoning in Chest Radiography](https://arxiv.org/abs/2605.11304)

**<font color=#1a73e8>作者：</font>** Eva Prakash, Yunhe Gao, Chong Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest radiograph interpretation requires temporal reasoning over prior and current studies, yet most vision-language models are trained on static image-report pairs and lack explicit supervision for modeling longitudinal change. We introduce CheXTemporal, a dataset for temporally grounded reasoning in chest radiography consisting of paired prior-current chest X-rays (CXR) with finding-level temporal and spatial annotations. The dataset includes a five-class progression taxonomy (new, worse, stable, improved, resolved), localized spatial supervision of pathology, explicit spatial-temporal alignment across paired studies, and multi-source coverage for cross-domain evaluation. We additionally construct a 280K-pair silver dataset with automatically derived temporal and anatomical supervision for large-scale evaluation under weaker supervision. Using these resources, we evaluate multiple state-of-the-art vision-language CXR models on grounding and progression-classification tasks in a zero-shot setting. Across both gold and silver evaluations, current models exhibit consistent limitations in spatial grounding, fine-grained temporal reasoning, and robustness under distribution shift. In particular, models perform substantially better on salient progression categories such as worse than on temporally subtle states such as stable and resolved, suggesting limited modeling of longitudinal disease evolution in chest radiography.

---


### 40. [SOMA: Efficient Multi-turn LLM Serving via Small Language Model](https://arxiv.org/abs/2605.11317)

**<font color=#1a73e8>作者：</font>** Xueqi Cheng, Qiong Wu, Zhengyi Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in multi-turn dialogue settings where preserving conversational context across turns is essential. A standard serving practice concatenates the full dialogue history at every turn, which reliably maintains coherence but incurs substantial cost in latency, memory, and API expenditure, especially when queries are routed to large proprietary models. Existing approaches often struggle to balance the trade-off between response quality and efficiency. We propose a framework that exploits the early turns of a session to estimate a local response manifold and then adapt a smaller surrogate model to this local region for the remainder of the conversation. Concretely, we learn soft prompts that maximize semantic divergence between the large and surrogate small language models' responses to surface least-aligned local directions, stabilize training with anti-degeneration control, and distill the mined cases into localized LoRA fine-tuning so the surrogate runs without prompts at inference. A simple gate enables a one-time switch with rollback on drift. We further provide a theoretical analysis for key components in SOMA. Extensive experiments show the effectiveness of SOMA. The source code is provided at: this https URL.

---


### 41. [Rethinking Evaluation for LLM Hallucination Detection: A Desiderata, A New RAG-based Benchmark, New Insights](https://arxiv.org/abs/2605.11330)

**<font color=#1a73e8>作者：</font>** Wenbo Chen, Veena Padmanabhan, Tootiya Giyahchi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hallucination, broadly referring to unfaithful, fabricated, or inconsistent content generated by LLMs, has wide-ranging implications. Therefore, a large body of effort has been devoted to detecting LLM hallucinations, as well as designing benchmark datasets for evaluating these detectors. In this work, we first establish a desiderata of properties for hallucination detection benchmarks (HDBs) to exhibit for effective evaluation. A critical look at existing HDBs through the lens of our desiderata reveals that none of them exhibits all the properties. We identify two largest gaps: (1) RAG-based grounded benchmarks with long context are severely lacking (partly because length impedes human annotation); and (2) Existing benchmarks do not make available realistic label noise for stress-testing detectors although real-world use-cases often grapple with label noise due to human or automated/weak annotation. To close these gaps, we build and open-source a new RAG-based HDB called T RIVIA+ that underwent a rigorous human annotation process. Notably, our benchmark exhibits all desirable properties including (1) T RIVIA+ contains samples with the longest context in the literature; and (2) we design and share four sets of noisy labels with different, both sample-dependent and sampleindependent, noise schemes. Finally, we perform experiments on RAG-based HDBs, including our T RIVIA+, using popular SOTA detectors that reveal new insights: (i) ample room remains for current detectors to reach the performance ceiling on RAG-based HDBs, (ii) the basic LLM-as-a-Judge baseline performs competitively, and (iii) label noise hinders detection performance. We expect that our findings, along with our proposed benchmark 1 , will motivate and foster needed research on hallucination detection for RAG-based tasks.

---


### 42. [VERDI: Single-Call Confidence Estimation for Verification-Based LLM Judges via Decomposed Inference](https://arxiv.org/abs/2605.11334)

**<font color=#1a73e8>作者：</font>** Jasmine Qi, Danylo Dantsev, Muyang Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-as-Judge systems are widely deployed for automated evaluation, yet practitioners lack reliable methods to know when a judge's verdict should be trusted. Token log-probabilities, the standard post-hoc confidence signal, are unavailable for many commercial LLMs and, even when accessible, saturate above 0.999 with structured JSON output.
We introduce VERDI (VERification-Decomposed Inference), a method that extracts confidence from the reasoning trace a structured judge already produces, with no additional inference calls. VERDI decomposes each verification-style evaluation into sub-checks and derives three structural signals: Step-Verdict Alignment, Claim-Level Margin, and Evidence Grounding Score. We combine them with Platt-scaled logistic regression.
On three public benchmarks, VERDI achieves AUROC 0.72-0.91 on GPT-4.1-mini and 0.66-0.80 on GPT-5.4-mini. On Qwen3.5-4B/9B/27B, where answer-token logprobs are anti-calibrated (higher confidence on errors, AUROC 0.32-0.49), VERDI achieves 0.56-0.70. We additionally validate on a production system with eight rubrics (AUROC 0.73-0.88 on factual rubrics), demonstrate cross-model transfer (AUROC 0.66-0.69), and show that a 33M-parameter NLI (Natural Language Inference) model provides a scalable alternative to regex extraction.

---


### 43. [CPEMH: An Agentic Framework for Prompt-Driven Behavior Evaluation and Assurance in Foundation-Model Systems for Mental Health Screening](https://arxiv.org/abs/2605.11341)

**<font color=#1a73e8>作者：</font>** Giuliano Lorenzoni, Ivens Portugal, Paulo Alencar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents CPEMH, an agentic framework designed to evaluate prompt-driven behavior in foundation-model systems operating on transcript-based datasets for mental-health screening. CPEMH serves as an engineering methodology for behavioral assurance in large-scale language systems, introducing an orchestrated architecture that autonomously performs the design, evaluation, and selection of prompt strategies, enabling systematic control of behavioral variability across contexts. Its modular agentic design, combining orchestrator, inference, and evaluation agents, ensures traceability, reproducibility, and robustness throughout the prompting lifecycle. A case study on automated depression screening from interview transcripts demonstrates the framework's capacity to stabilize and audit foundation-model behavior in conversational and clinically sensitive domains. Lessons learned emphasize the role of modular orchestration in behavioral assurance, the prioritization of stability over architectural complexity, and the integration of F1, bias, and robustness as core acceptance criteria.

---


### 44. [Gradient-Free Noise Optimization for Reward Alignment in Generative Models](https://arxiv.org/abs/2605.11347)

**<font color=#1a73e8>作者：</font>** Jeongsol Kim, Hongeun Kim, Jian Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing reward alignment methods for diffusion and flow models rely on multi-step stochastic trajectories, making them difficult to extend to deterministic generators. A natural alternative is noise-space optimization, but existing approaches require backpropagation through the generator and reward pipeline, limiting applicability to differentiable settings. To address this, here we present ZeNO (Zeroth-order Noise Optimization), a gradient-free framework that formulates noise optimization as a path-integral control problem, estimable from zeroth-order reward evaluations alone. When instantiated with an Ornstein--Uhlenbeck reference process, the update connects to Langevin dynamics implicitly targeting a reward-tilted distribution. ZeNO enables effective inference-time scaling and demonstrates strong performance across diverse generators and reward functions, including a protein structure generation task where backpropagation is infeasible.

---


### 45. [Large Language Models for Causal Relations Extraction in Social Media: A Validation Framework for Disaster Intelligence](https://arxiv.org/abs/2605.11348)

**<font color=#1a73e8>作者：</font>** Ujun Jeong, Saketh Vishnubhatla, Bohan Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> During disasters, extracting causal relations from social media can strengthen situational awareness by identifying factors linked to casualties, physical damage, infrastructure disruption, and cascading impacts. However, disaster-related posts are often informal, fragmented, and context-dependent, and they may describe personal experiences rather than explicit causal relations. In this work, we examine whether Large Language Models (LLMs) can effectively extract causal relations from disaster-related social media posts. To this end, we (1) propose an expert-grounded evaluation framework that compares LLM-generated causal graphs with reference graphs derived from disaster-specific reports and (2) assess whether the extracted relations are supported by post-event evidence or instead reflect model priors. Our findings highlight both the potential and risks of using LLMs for causal relation extraction in disaster decision-support systems.

---


### 46. [The tractability landscape of diffusion alignment: regularization, rewards, and computational primitives](https://arxiv.org/abs/2605.11361)

**<font color=#1a73e8>作者：</font>** Ankur Moitra, Andrej Risteski, Dhruv Rohatgi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time reward alignment asks how to turn a pre-trained diffusion model with base law $p$ into a sampler that favors a reward $r$ while remaining close to $p$. Since there is no canonical distributional distance for this closeness constraint, different choices lead to different "reward-aligned" laws and, just as importantly, different algorithmic problems. We develop a primitive-based approach to reward alignment: rather than assuming arbitrary reward-aligned laws can be sampled, we ask which simple algorithmic primitives suffice to implement alignment for non-trivial reward classes. If closeness is measured in KL distance, the target law is $q(x) \propto p(x) \exp(\lambda^{-1}r(x))$. For this setting, we show that linear exponential tilts of the form $q(x)\propto p(x)\exp(\langle \theta, x \rangle)$ -- which according to recent work [MRR26] can be efficiently sampled from -- are a sufficient primitive for aligning to a very broad class of convex low-dimensional rewards. If closeness is measured in Wasserstein distance, the corresponding primitive is a proximal transport oracle: given $x$, solve $\mbox{argmax}_y \{r(y)- \lambda c(x,y)\}$. This oracle can be efficiently implemented for concave or low-dimensional Lipschitz rewards $r(x)=f(Ax)$. Together, these results illustrate that the choice of distribution distance for alignment affects the computational primitive and the tractable reward class.

---


### 47. [PresentAgent-2: Towards Generalist Multimodal Presentation Agents](https://arxiv.org/abs/2605.11363)

**<font color=#1a73e8>作者：</font>** Wei Wu, Ziyang Xu, Zeyu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Presentation generation is moving beyond static slide creation toward end-to-end presentation video generation with research grounding, multimodal media, and interactive delivery. We introduce PresentAgent-2, an agentic framework for generating presentation videos from user queries. Given an open-ended user query and a selected presentation mode, PresentAgent-2 first summarizes the query into a focused topic and performs deep research over presentation-friendly sources to collect multimodal resources, including relevant text, images, GIFs, and videos. It then constructs presentation slides, generates mode-specific scripts, and composes slides, audio, and dynamic media into a complete presentation video. PresentAgent-2 supports three independent presentation modes within a unified framework: Single Presentation, which generates a single-speaker narrated presentation video; Discussion, which creates a multi-speaker presentation with structured speaker roles, such as for asking guiding questions, explaining concepts, clarifying details, and summarizing key points; and Interaction, which independently supports answering audience questions grounded in the generated slides, scripts, retrieved evidence, and presentation context. To evaluate these capabilities, we build a multimodal presentation benchmark covering single presentation, discussion, and interaction scenarios, with task-specific evaluation criteria for content quality, media relevance, dynamic media use, dialogue naturalness, and interaction grounding. Overall, PresentAgent-2 extends presentation generation from document-dependent slide creation to query-driven, research-grounded presentation video generation with multimodal media, dialogue, and interaction. Code: this https URL. Website: this https URL.

---


### 48. [3D-Belief: Embodied Belief Inference via Generative 3D World Modeling](https://arxiv.org/abs/2605.11367)

**<font color=#1a73e8>作者：</font>** Yifan Yin, Zehao Wen, Jieneng Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in visual generative models have highlighted the promise of learning generative world models. However, most existing approaches frame world modeling as novel-view synthesis or future-frame prediction, emphasizing visual realism rather than the structured uncertainty required by embodied agents acting under partial observability. In this work, we propose a different perspective: world modeling as embodied belief inference in 3D space. From this view, a world model should not merely render what may be seen, but maintain and update an agent's belief about the unobserved 3D world as new observations are acquired. We identify several key capabilities for such models, including spatially consistent scene memory, multi-hypothesis belief sampling, sequential belief updating, and semantically informed prediction of unseen regions. We instantiate these ideas in 3D-Belief, a generative 3D world model that infers explicit, actionable 3D beliefs from partial observations and updates them online over time. Unlike prior visual prediction models, 3D-Belief represents uncertainty directly in 3D, enabling embodied agents to imagine plausible scene completions and reason over partially observed environments. We evaluate 3D-Belief on 2D visual quality for scene memory and unobserved-scene imagination, object- and scene-level 3D imagination using our proposed 3D-CORE benchmark, and challenging object navigation tasks in both simulation and the real world. Experiments show that 3D-Belief improves 2D and 3D imagination quality and downstream embodied task performance compared to state-of-the-art methods.

---


### 49. [Test-Time Compute for Dense Retrieval: Agentic Program Generation with Frozen Embedding Models](https://arxiv.org/abs/2605.11374)

**<font color=#1a73e8>作者：</font>** Han Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time compute is widely believed to benefit only large reasoning models. We show it also helps small embedding models. Most modern embedding checkpoints are distilled from large LLM backbones and inherit their representation space; a frozen embedding model should therefore benefit from extra inference compute without retraining. Using an agentic program-search loop, we explore 259 candidate inference programs over a frozen embedding API across ninety generations. The entire Pareto frontier collapses onto a single algebra: a softmax-weighted centroid of the local top-K documents interpolated with the query. This parameter-free default lifts nDCG@10 statistically significantly across seven embedding-model families spanning a tenfold parameter range, with held-out full-BEIR validation confirming the lift on every model tested.

---


### 50. [LLM-X: A Scalable Negotiation-Oriented Exchange for Communication Among Personal LLM Agents](https://arxiv.org/abs/2605.11376)

**<font color=#1a73e8>作者：</font>** Giuliano Lorenzoni, Paulo Alencar, Donald Cowan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a personal-LLM exchange (LLM-X), a scalable negotiation-oriented environment that enables direct, structured communication across populations of personal agents (LLMs), each representing an individual user. Unlike existing tool-centric protocols that focus on agent-API interaction, LLM-X introduces a message bus and routing substrate for LLM-to-LLM coordination with guarantees around schema validity and policy enforcement. We contribute: (1) an architecture for LLM-X comprising federated gateways, topic-based routing, and policy enforcement; (2) a typed message protocol supporting capability negotiation and contract-net-style coordination; and (3) the first empirical evaluation of LLM-based multi-agent negotiation at scale. Experiments span 5, 9, and 12 agents, under distinct negotiation policies (Low, Medium, High), and across both short-run (minutes) and long-run (2h, 12h) load conditions. Results highlight clear policy-performance trade-offs: stricter policies improve robustness and fairness but increase latencies and message volume. Extended runs confirm that LLM-X remains stable under sustained load, with bounded latency drift.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-223](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
