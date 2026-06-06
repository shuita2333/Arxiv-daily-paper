# 🧠 大模型相关研究 | 2026年06月07日

> 本类共 **185** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-185](./part-04.md)

---

### 51. [GuardNet: Ensemble Strategies of Shallow Neural Networks for Robust Prompt Injection and Jailbreak Detection](https://arxiv.org/abs/2606.05566)

**<font color=#1a73e8>作者：</font>** Paulo Ricardo Ferreira Neves, Edson Rodrigues da Cruz Filho, Paulo Henrique Eleuterio Falsetti 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have transformed natural language processing, but they remain vulnerable to Prompt Injection (PI) and Jailbreak (JB) attacks. In addition, benchmark evaluations may be affected by contamination and partial information leakage, compromising performance estimates. This work presents GuardNet, a guardrail system based on an ensemble of shallow neural networks (BiLSTMs) with approximately 47 million parameters. We investigate the hypothesis that robustness in adversarial scenarios depends more on the diversity of example coverage and threshold calibration than on model scale. The results indicate that GuardNet achieves competitive performance compared with lightweight detectors and high efficiency at low latency, although larger LLMs such as Mistral-7B and Llama-3.1-8B still achieve superior performance in terms of F1 score and AUROC on the blind JBB-Behaviors benchmark. Nevertheless, GuardNet achieves an AUROC of 0.747 on the blind dataset (n = 200) and an F1 score of 0.92 on a proprietary benchmark (n = 50), under threshold calibration and evaluation with declared partial information leakage. The system operates with an average latency of approximately 50 ms on CPU, making it suitable for deployment in production environments with cost and infrastructure constraints.

---


### 52. [Cross-Epoch Adaptive Rollout Optimization for RL Post-Training](https://arxiv.org/abs/2606.05606)

**<font color=#1a73e8>作者：</font>** Yiming Zong, Yige Wang, Jiashuo Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM post-training often relies on reinforcement learning methods that sample multiple rollouts per prompt, yet most existing approaches use a fixed rollout budget for every prompt, despite large differences in the training signal different prompts provide. In this paper, we study adaptive rollout allocation under a fixed global budget and formulate the problem as online resource allocation with prompt-level diminishing returns. Our method, CERO, maintains a Beta posterior over each prompt's success probability and uses the posterior expected Bernoulli variance as a Bayesian estimate of the value of additional rollouts. We use this estimate to construct a concave, saturating utility over cumulative allocations, yielding an objective in which decisions across prompts and epochs are coupled by the global budget. Since the resulting objective is temporally nonseparable, we derive a Fenchel-dual reformulation and update both prompt-level and budget-level dual variables via projected online gradient descent. Under fixed prompt utilities, we prove an $O(\sqrt{K})$ regret bound against the offline allocation benchmark. Experiments on mathematical-reasoning problems show that CERO consistently outperforms GRPO across multiple open-weight LLMs and benchmarks, demonstrating that adaptive rollout budgeting can improve sample efficiency.

---


### 53. [Predictable Scaling Laws of Optimal Hyperparameters for LLM Continued Pre-training](https://arxiv.org/abs/2606.05610)

**<font color=#1a73e8>作者：</font>** Yongwei Zhou, Juncheng Diao, Junlin Shang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The efficacy of continued pre-training for Large Language Models (LLMs) hinges upon hyperparameter configurations, such as learning rate and batch size. However, current practices often rely on heuristics or grid searches, leading to training instability and excessive costs. In this work, we first empirically discover that optimal hyperparameters follow stable and predictable scaling laws throughout the continued pre-training process. Leveraging these insights, we propose a novel framework to establish quantitative relationships between compute budget and optimal hyperparameters for a given checkpoint. Our approach has two stages: (1) \textit{Empirical Law Discovery}, where we train small-scale proxy models to derive functions mapping compute budget to optimal hyperparameters via standard loss-compute scaling laws; and (2) \textit{State-Aware Hyperparameter Prediction}, where we evaluate an initial checkpoint's validation loss and use the inverse scaling law to estimate its \textit{equivalent pre-training compute} -- the compute needed to achieve the same loss from scratch. Combining this with the planned compute budget, we predict optimal hyperparameters for the target run. Empirical results demonstrate that our method reduces the hyperparameter search overhead by up to 90\% while achieving comparable or superior performance relative to baselines. This model-agnostic framework generalizes across architectures, providing a principled and efficient methodology for diverse continued pre-training scenarios starting from any given point.

---


### 54. [Multilingual Fine-Tuning via Localized Gradient Conflict Resolution](https://arxiv.org/abs/2606.05613)

**<font color=#1a73e8>作者：</font>** Long P. Hoang, Yiran Zhao, Wei Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of Large Language Models (LLMs) has established cross-lingual versatility as a defining feature of modern systems. However, fine-tuning these models frequently induces negative interference across languages. To address this, we reformulate multilingual fine-tuning as a multi-objective optimization (MOO) problem. Specifically, we introduce Bucket-Level MOO, a scalable distributed framework that applies gradient-based MOO algorithms locally on parameter buckets. This enables conflict-aware updates without the prohibitive communication overhead of reconstructing full gradient vectors. Theoretically, we prove this localized resolution natively enforces Refined Pareto Stationarity, a strictly tighter necessary condition for Pareto optimality. Empirically, Bucket-Level MOO mitigates interference by driving LLMs to construct distinct language-specific dimensions, improving representational separability. Extensive experiments across four base LLMs demonstrate that our method significantly improves both seen and unseen multilingual performance over standard fine-tuning paradigms.

---


### 55. [Safety Paradox: How Enhanced Safety Awareness Leaves LLMs Vulnerable to Posterior Attack](https://arxiv.org/abs/2606.05614)

**<font color=#1a73e8>作者：</font>** Long P. Hoang, Hai V. Le, Shaoyang Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are rigorously aligned to refuse harmful requests, a process that inherently cultivates a latent capacity to evaluate and recognize unsafe content. In this work, we reveal that this advanced safety awareness inadvertently introduces a fatal vulnerability. We introduce Posterior Attack, a single-query jailbreak that bypasses guardrails by prompting the model to generate the exact harmful response its internal classifier would normally flag as unsafe. Through extensive empirical evaluation across 30 open-source LLMs (up to 35B parameters in size) and frontier models (e.g., GPT-5, Claude 4.6), we observe a striking phenomenon: models with superior safety-judgment capabilities are disproportionately more susceptible to this exploitation. To explain this, we formalize the Safety Paradox, analytically showing that monotonic improvements in safety alignment naturally amplify posterior vulnerability. Finally, we establish a causal link via reinforcement learning interventions, exemplifying that artificially degrading a model's safety judgment immunizes it against the attack, whereas enhancing judgment exacerbates the vulnerability. Our findings highlight potential flaws in current alignment paradigms, indicating that defense mechanisms may require further structural refinement.

---


### 56. [What's in a Name? Morphological Shortcuts by LLMs in Pharmacology](https://arxiv.org/abs/2606.05616)

**<font color=#1a73e8>作者：</font>** Kaijie Mo, Thomas Yang, Chantal Shaib 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The morphological form of a word can often give cues to its meaning, but purely relying on these mappings can lead to overgeneralization in high-stakes domains. In the medical domain, for instance, LLMs can confidently reason about fictitious drugs from their affixes alone (e.g., wugcillin) and generate plausible-looking clinical content. We present a behavioral and mechanistic study of LLM "affix heuristics" in pharmacology. Using fictitious drug names built from real affixes, we show that affix signals alone elicit class-level pharmacological responses. We introduce a framework for identifying whether a model's drug semantics are driven mainly by the affix, the stem, or the drug name as a whole. Applied across 653 drugs, our framework reveals that models often induce drug meaning primarily through affix cues, yet rarely explicitly indicate this reliance, and sometimes incorrectly conflate properties among affix-sharing drugs. Activation patching across models further localizes this behavior to early-mid layers. These findings show that morphological shortcuts pose a subtle but measurable risk to safety.

---


### 57. [AdaPlanBench: Evaluating Adaptive Planning in Large Language Model Agents under World and User Constraints](https://arxiv.org/abs/2606.05622)

**<font color=#1a73e8>作者：</font>** Jiayu Liu, Cheng Qian, Zhenhailong Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Planning for real-world problems by language models often involves both world and user constraints, which may not be fully specified upfront and are progressively disclosed through interaction. However, existing benchmarks still underexplore adaptive planning under such progressively revealed dual constraints. To address this gap, we introduce AdaPlanBench, a dynamic interactive benchmark for evaluating whether Large Language Model (LLM) agents can adaptively plan and re-plan under progressively revealed world and user constraints. AdaPlanBench is built on 307 household tasks, with a scalable constraint construction pipeline that augments each task with dual constraints. At runtime, agents interact with the environment in a multi-turn protocol where hidden constraints are revealed only when the agent proposes a plan that violates them, requiring iterative plan revision under accumulating feedback. This makes planning challenging, as agents must infer and track constraints from feedback while re-planning effectively. Experiments on ten leading LLMs show that adaptive planning under dual constraints remains challenging, with the best model reaching only 67.75% accuracy. We further observe that performance degrades as more constraints accumulate, with user constraints posing a particularly large challenge and failures often stemming from weaker physical grounding and reduced effectiveness. These results establish AdaPlanBench as a testbed for dual-constrained interactive planning and highlight the challenge of reliable adaptation to dynamically revealed constraints in LLM agents.

---


### 58. [Evaluation of LLMs for Mathematical Formalization in Lean](https://arxiv.org/abs/2606.05632)

**<font color=#1a73e8>作者：</font>** Tyson Klingner, Drew Bladek, Escher Crawford 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Within the past few years, the ability of Large Language Models (LLMs) to generate formal mathematical proofs has improved drastically. We provide a comparison of various LLMs' effectiveness in producing formal proofs in Lean 4 with the goal of assisting those seeking to use LLMs to support their own projects. We utilize both pass@$k$ and refine@$k$ metrics as the benchmark for our comparison and evaluate on subsets of both miniF2F and miniCTX datasets. Our testing shows that overall, Gemini 3.1 Pro and Claude Opus 4.7 perform best. Gemini 3.1 Pro achieved a 92\% success rate on miniF2F via refine@32 whereas Opus 4.7 achieved a 86\% success rate on miniCTX via refine@32. When taking cost into account, NVIDIA Nemotron 3 Super and GPT-OSS 120B were the most efficient, with competitive accuracies and average costs of $<\$0.01$ per correct proof.

---


### 59. [Answer Presence Drives RAG Rewriting Gains](https://arxiv.org/abs/2606.05633)

**<font color=#1a73e8>作者：</font>** Yuejie Li, Yueying Hua, Ke Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented QA pipelines often route retrieved passages through an LLM \emph{rewriter} before a smaller reader, lifting F1 by tens of points on multi-hop benchmarks; this gain is typically credited to improved evidence quality. We ask whether that lift is causally driven by the gold answer string appearing in the rewritten context rather than by curation per se, using a controlled intervention audit. For each rewritten context we re-run the reader after one of four controlled edits to the compile output: removing the gold answer span, replacing a length-matched random non-answer span (placebo), or injecting the gold into rewrites where it was absent (at the prefix or at a midpoint sentence boundary). Across twelve completed (cell, baseline) intervention runs spanning three reader families (Qwen2.5-7B, Qwen3.5-35B, GLM-4.7), two datasets (HotpotQA, 2WikiMultihopQA), and three compiler arrangements (MA-only, MB-only, MA$+$verify), removing the gold answer drops reader F1 by $28$ to $64$ points beyond the length-matched placebo on paired \texttt{answer-in-compile} strata, and prepending the gold into rewrites that lacked it raises F1 by $+0.7$ to $+9.7$ points in $10$ of $12$ (cell, baseline) combinations. A companion five-sentinel audit shows the conventional single-\texttt{[MASK]} probe is itself sentinel-fragile: on 2Wiki it reports a $+4.12$~F1 ``non-leakage residual'' that flips to $-3.33$ to $-7.81$~F1 under four alternative sentinels and fails an equivalence test for three of those four ($1/4$~pass). We do not propose a new rewriter or mitigation; we release the intervention runner and the sentinel panel so that other rewriter-gain claims can be tested against the same standard.

---


### 60. [ShotCrop$^3$: Cropping Human-Centric Images into Cinematic Triple-Shot Compositions](https://arxiv.org/abs/2606.05635)

**<font color=#1a73e8>作者：</font>** Dehong Kong, Lina Lei, Lingtao Zheng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prior work on aesthetic composition typically produces a single aesthetically pleasing crop, overlooking the narrative value of composing multiple shots from one scene. In practice, multi-shot composition is critical for downstream creative workflows: commercial posters often require multiple crops with different emphases (e.g., context, subject, and emotion/product details) to present key story beats. Therefore, we propose \textbf{Triple-Shot Compositions (TSC)}, a composition task that generates a three-shot set -- establishing, medium, and close-up -- from a single human-centric image, each paired with a brief shot description to support visual narration. To learn TSC with limited expert annotations, we introduce \textbf{ShotCrop} which undergoes a three-stage training process: it first applies Chain-of-Thought supervised fine-tuning to establish basic reasoning and aesthetic shot-cropping skills, then performs semi-supervised fine-tuning with high-confidence pseudo labels to further enhance aesthetic capability, and is finally optimized with Group Relative Policy Optimization for \textbf{ShotCrop} (GRPO-S) using a composite reward tailored for it. Specifically, our pseudo-labeling strategy combines MLLM-based scoring, aesthetic assessment, and CLIP similarity to retain high-confidence training signals. In addition, we present TSC-Bench, a benchmark of 1.2k expert-annotated test cases. Notably, ShotCrop achieves an average improvement of \textbf{2.82} times over GPT-5 in shot localization accuracy.

---


### 61. [Multi-Task Crack Foundation Model for Engineering-Reliable Crack Representation and Topology Preservation in Civil Infrastructure](https://arxiv.org/abs/2606.05641)

**<font color=#1a73e8>作者：</font>** Blessing Agyei Kyem, Joshua Kofi Asamoah, Eugene Denteh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable crack assessment requires not only accurate pixel-level masks but also connected crack geometry and confidence estimates that remain stable under domain shift. However, existing segmentation models can achieve high overlap scores while fragmenting cracks, missing fine branches, and providing no calibrated uncertainty. To address this gap, this paper proposes CrackGeoFM, a multi-task framework that combines a frozen visual foundation backbone with crack-specific adaptation for mask prediction, skeleton reconstruction, and uncertainty estimation. The framework integrates a Frequency-Guided Crack Enhancement Module (FCEM) to enhance high-frequency crack cues, a Crack-Domain Feature Adaptation Module (CFAM) to adapt frozen backbone features to crack-domain patterns, and a Structure-Aware Multi-Task Decoder (SMTD) to jointly decode masks, skeletons, and uncertainty. Across 20 crack datasets, CrackGeoFM achieves state-of-the-art segmentation, improved topology preservation, calibrated uncertainty, and effective few-shot adaptation with only five labeled images. These results support reliable, generalizable, and engineering-oriented crack analysis for infrastructure assessment.

---


### 62. [FIDES: Faithful Inference via Deep Evidence Signals for Retrieval-Memory Conflict in RAG](https://arxiv.org/abs/2606.05644)

**<font color=#1a73e8>作者：</font>** Zhe Yu, Wenpeng Xing, Tiancheng Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When retrieved evidence contradicts parametric memory, language models frequently ignore context and default to memorized priors -- a failure that undermines the core purpose of retrieval augmentation. Contrastive decoding amplifies the context-conditioned output to suppress parametric bias, but existing methods rest on an implicit assumption that this bias is uniform across tokens. A single global contrastive weight over-penalizes safe tokens while leaving genuinely conflicted ones insufficiently corrected. We identify token-level conflict concentration: retrieval-memory tension is sharply heterogeneous, concentrated on a small fraction of answer-critical decoding steps. This reframes contrastive decoding from how much contrast to apply to where to apply it. We propose FIDES (Faithful Inference via Deep Evidence Signals), a training-free decoder that reads three internal signals probing retrieval-memory conflict at complementary depths -- output surface, hidden representations, and prediction trajectory -- and fuses them to govern intervention strength at each decoding step. Across three benchmarks and six backbones -- four primary 7B/8B models and two scaling backbones up to 70B -- FIDES achieves the best context fidelity in all 18 settings, outperforming the strongest training-free baseline by +3 to +13 points. On the 70B scale, fidelity reaches 92-94% while F1 surges to 62-63%, demonstrating that token-level selectivity unlocks generation capability that coarse contrastive rules suppress.

---


### 63. [Do More Agents Help? Controlled and Protocol-Aligned Evaluation of LLM Agent Workflows](https://arxiv.org/abs/2606.05670)

**<font color=#1a73e8>作者：</font>** Yuhang Fu, Ruishan Fang, Jiaqi Shao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Does adding more agents help an LLM workflow once compared systems share the same benchmark loader, tool access, answer contract, usage accounting, and trajectory logging? We introduce BenchAgent, an evaluation framework that places single-agent, fixed multi-agent (MAS), and evolving MAS workflows under one normalized execution and logging protocol. BenchAgent evaluates these substrate-internal workflows across ten reasoning, coding, and tool-use benchmarks with GPT-4.1, and separately reports a Protocol-Aligned External (PAE) GAIA study of a runtime-generated workflow. Under SI conditions, at most one of six tested MAS exceeds the matched single-agent anchor on benchmark-balanced average accuracy: EvoAgent lies within the Wilson one-run guidance, while the remaining five trail by 2.56-11.29 points and occupy more expensive accuracy-cost trade-offs. On the PAE GAIA snapshot, a Claude-Code-style runtime workflow reaches 66.72% overall and 69.23% on Level 3, more than 20 points above the strongest non-Claude baseline, Jarvis, a fixed MAS.

---


### 64. [Two-Way Is Better Than One: Bidirectional Alignment with Cycle Consistency for Exemplar-Free Class-Incremental Learning](https://arxiv.org/abs/2606.05675)

**<font color=#1a73e8>作者：</font>** Hongye Xu, Bartosz Krawczyk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) seeks models that acquire new skills without erasing prior knowledge. In exemplar-free class-incremental learning (EFCIL), this challenge is amplified because past data cannot be stored, making representation drift for old classes particularly harmful. Prototype-based EFCIL is attractive for its efficiency, yet prototypes drift as the embedding space evolves; therefore, projection-based drift compensation has become a popular remedy. We show, however, that existing one-directional projections introduce systematic bias: they either retroactively distort the current feature geometry or align past classes only locally, leaving cycle inconsistencies that accumulate across tasks. We introduce BiCyc, a bidirectional projector alignment approach with a cycle-consistency objective. BiCyc jointly optimizes two maps, old-to-new and new-to-old, with stop-gradient gating so that transport and representation co-evolve. Analytically, we show that the cycle loss contracts the singular spectrum toward unity in whitened space, and that improved transport of class means and covariances yields smaller perturbations of classification log-odds, preserving old-class decisions and mitigating catastrophic forgetting. Empirically, across standard EFCIL benchmarks, BiCyc substantially reduces forgetting and improves accuracy in from-scratch settings, while remaining competitive in the pretrained fine-grained regime.

---


### 65. [LongSpace: Exploring Long-Horizon Spatial Memory from Perception to Recall in Video](https://arxiv.org/abs/2606.05677)

**<font color=#1a73e8>作者：</font>** Shiqiang Lang, Jing Liu, Haoyang He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have advanced image and video understanding and can increasingly handle longer visual inputs. Long-horizon tasks such as autonomous driving and robotic navigation require more than recognizing the current view, as models must remember and retrieve previously observed spatial layouts, routes, viewpoint changes, and object states. To evaluate this capability, we introduce LongSpace-Bench, a room-tour video benchmark for long-horizon spatial memory, covering scene perception, spatial relations, and spatial memory. In this work, we further propose LongSpace, a memory framework for long-video spatial reasoning. LongSpace models long videos as sequential chunks, incorporates 3D structural cues into early decoder layers, and constructs layer-aware memory for question-guided retrieval. Experiments on multiple spatial reasoning benchmarks show that LongSpace improves long-video spatial understanding, further demonstrating explicit spatial memory as a key capability for long-horizon video MLLMs.

---


### 66. [Beyond Output Matching: Preserving Internal Geometry in NVFP4 LLM Distillatio](https://arxiv.org/abs/2606.05682)

**<font color=#1a73e8>作者：</font>** Fangbo Tu, Junhua Zhao, Chi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Demand for low-precision inference, including NVFP4-based approaches, has grown as large language models are increasingly deployed in latency and cost constrained production environments. Quantization-aware distillation (QAD) helps recover accuracy lost under low bit quantization by training a quantized student to match the output distribution of a frozen higher precision teacher via a KL-divergence loss. In this work, we first provide a representation level diagnosis of QAD: output matching alone can mask internal degradation, because many intermediate activation geometries can yield similar teacher-aligned logits. Using CKA, we show that KL-only QAD can reduce layerwise representational similarity relative to the BF16 teacher, with especially severe drift in RL-post-trained models. This drift correlates with downstream bottlenecks on reasoning and coding tasks, suggesting that low bit recovery requires preserving internal geometry rather than matching outputs alone. Motivated by this finding, we propose \textbf{CKA-QAD}, a CKA-guided representational alignment method for NVFP4 QAD and low bit LLM accuracy recovery. The method adds a lightweight regularizer that preserves internal representational geometry during distillation by aligning layerwise Gram matrices through CKA. Across Nemotron 3 Nano and Qwen3-4B-Thinking-2507, CKA-QAD substantially improves representational alignment and improves downstream reasoning and coding accuracy with modest training overhead. Our findings position CKA-guided representational alignment as a practical complement to output matching for quantized LLM recovery.

---


### 67. [Value-and-Structure Alignment for Routing-Consistent Quantization of Mixture-of-Experts Models](https://arxiv.org/abs/2606.05688)

**<font color=#1a73e8>作者：</font>** Hancheol Park, Geonho Lee, Tairen Piao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models scale foundation models efficiently by activating only a subset of experts for each token, but their large number of expert parameters still makes quantization essential for practical deployment. Unlike dense models, however, MoE models are sensitive to routing instability: small quantization-induced perturbations can change the top-$k$ expert selection, altering the computation path and degrading model quality. We propose Value-and-Structure Routing Alignment for Quantization (VSRAQ), a MoE-specific post-training quantization objective that preserves pre-quantization expert-selection behavior under quantization. VSRAQ combines two complementary objectives that jointly preserve expert-selection behavior: value alignment, which matches routing-relevant logits or scores, and structure alignment, which preserves expert ordering and top-$k$ decision boundaries. By maintaining routing consistency, VSRAQ reduces quantization-induced degradation without introducing any inference-time overhead and can be integrated into existing quantization frameworks. Experiments on recent MoE foundation models show that VSRAQ improves expert-selection consistency and consistently outperforms reconstruction-only and router-aware baselines.

---


### 68. [MolE-RAG: Molecular Structure-Enhanced Retrieval-Augmented Generation for Chemistry](https://arxiv.org/abs/2606.05693)

**<font color=#1a73e8>作者：</font>** Joey Chan, Wonbin Kweon, Ashley Shin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown promise for molecular property prediction, but their ability to reason over chemical structures remains limited, as molecular representations such as SMILES differ substantially from the natural language on which LLMs are primarily trained. To bridge this semantic and chemical knowledge gap, we propose MolE-RAG, a training-free, molecule-centric retrieval-augmented generation framework for LLM-based molecular property prediction. MolE-RAG augments each prediction with three complementary sources of inference-time context: retrieved chemistry literature, molecule-specific information including compound synonyms, identifiers, functional group annotations, and physicochemical descriptors, and structurally similar molecules retrieved from the training set. We evaluate MolE-RAG across nine molecular property prediction tasks using proprietary, chemistry-specialized, and open-source LLMs. Across general-purpose LLMs, MolE-RAG improves ROC-AUC by up to 28 percentage points on classification tasks and reduces regression RMSE by up to 67% relative to a SMILES-only baseline. We further find that the utility of each context source varies across models and tasks, with different models benefiting most from textual retrieval, molecular context, or structural retrieval. These results suggest that molecule-centric retrieval can improve LLM-based molecular property prediction without model fine-tuning while providing a flexible framework for integrating heterogeneous chemical knowledge at inference time.

---


### 69. [PerceptUI: LLM Agents as Human-Aligned Synthetic Users for UI/UX Evaluation](https://arxiv.org/abs/2606.05697)

**<font color=#1a73e8>作者：</font>** Nicolas Bougie, Xiaotong Ye, Gian Maria Marconi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> User interface (UI) and user experience (UX) evaluation is central to product development, yet reliable feedback still relies on recruiting human participants or running online A/B tests, making early-stage iteration slow and costly. In light of this, recent work has explored Multimodal Large Language Models as proxy evaluators. However, existing approaches either produce surface-level critiques or a judgment that reflects the model's own biases rather than the genuine response of a particular user. We introduce PerceptUI, a framework for persona-conditioned UI/UX evaluation that predicts how a specific user would answer interface-related questions and produces natural-language rationales. PerceptUI is trained in two stages: (i) contrastive reflection fine-tuning distills teacher-generated rationales by extracting lessons from human decisions, and (ii) a reflective prompt-evolution step from the model's own failure traces. Across multiple domains and datasets, PerceptUI achieves human-level realism, generalizes to unseen questions and personas, and yields population-level response distributions.

---


### 70. [Seeing Time: Benchmarking Chronological Reasoning and Shortcut Biases in Vision-Language Models](https://arxiv.org/abs/2606.05702)

**<font color=#1a73e8>作者：</font>** Haoyu Zhou, Qing Qing, Caichong Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Vision-Language Models (VLMs) have significantly enhanced their ability to interpret complex visual semantics, yet their capacity for chronological reasoning remains under-explored. In this paper, we introduce a novel benchmark specifically designed to evaluate how VLMs perceive and reason about chronological information within and across images. Unlike existing video-based benchmarks that focus on frame sequencing, our work delves into the underlying logic of chronological judgment and the expansion toward multimodal integration. To facilitate this, we construct three specialized datasets: one containing visually similar objects spanning long historical durations, another categorized by diverse event and object types, and a third pairing images with time-sensitive news text for cross-modal alignment. Through extensive experiments, we analyze whether models exhibit performance disparities across categories and, crucially, explore whether they rely on ``incorrect shortcuts'', such as image color rather than genuine chronological features. Our results reveal that while VLMs show promise, they frequently exploit superficial cues like grayscale versus color filters to bypass authentic chronological reasoning. By providing these high-quality datasets and a rigorous evaluation framework, we offer a diagnostic tool to identify current limitations and guide the development of more robust, logically grounded multimodal models. The source code is shown in this https URL.

---


### 71. [Critic-Guided Heterogeneous Multi-Agent Reasoning for Reliable Mathematical Problem Solving](https://arxiv.org/abs/2606.05704)

**<font color=#1a73e8>作者：</font>** Muhammad Talha Sharif, Abdul Rehman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent Large Language Models (LLMs) have shown impressive reasoning abilities; but they are still susceptible to hallucinations, intermediate reasoning mistakes, and unreliable reasoning results in complex mathematical reasoning problems. In this study, we introduce a critic-based heterogeneous multi-agent approach to improve the dependability of mathematical reasoning. This framework incorporates several LLM agents of different specialties and employs a critic-driven adaptive learning system to assess and guide the reasoning process based on intermediate feedback. The system adopts a generator-validator framework, with the validator not only determining correctness but also offering critiques to guide regeneration of solutions. This allows for adaptive error correction and prevents error cascading. Our experiments on the GSM8K benchmark show that the proposed method achieves up to 13% accuracy improvement over single-shot and non-critic models. Additionally, findings suggest that heterogeneity and critique reduce the need for large models, allowing smaller models to perform on par. Ablation studies reveal the main performance gains are due to the critic-based feedback loop and not model size. In summary, the proposed approach showcases the benefits of combining heterogeneous multi-agent collaboration and critique to obtain reliable and interpretable reasoning systems.

---


### 72. [Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems](https://arxiv.org/abs/2606.05711)

**<font color=#1a73e8>作者：</font>** Yingzhuo Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems built on large language models (LLMs) have become a prevailing paradigm for tackling complex reasoning, planning, and tool-use tasks. The dominant communication protocol in such systems is natural language: agents exchange messages token-by-token, verbalising their internal reasoning so that peers can read, verify, and respond. While convenient and interpretable, this protocol suffers from three structural drawbacks -- high inference cost, irreversible information loss during discretization, and ambiguity/redundancy of natural language. A growing body of work therefore explores an alternative protocol -- latent communication -- in which agents exchange continuous representations (embeddings, hidden states, or KV-caches) directly, bypassing the bottleneck of text generation. This paper presents a unified framework for organising the rapidly expanding literature on latent communication. We analyse existing methods along three orthogonal axes: (1) WHAT information is communicated (Embeddings, Hidden States, KV-Caches, or other continuous state); (2) WHICH sender-receiver alignment is used (latent-space alignment and layer alignment); and (3) HOW the communicated information is fused into the receiver (concatenation, prepending, mathematical operations, cross-attention, or cache restoration). Under this 3-axis framework, we systematically categorise eighteen representative methods proposed between 2024 and 2026, identify five major design patterns, and surface a set of open challenges -- including cross-architecture alignment, security of latent channels, compression for edge deployment, and the relationship between latent communication and latent chain-of-thought. We hope that this framework both lowers the barrier to entry for new researchers and provides a vocabulary for comparing future work.

---


### 73. [ViCuR: Visual Cues as Recoverable Privilege for Multimodal On-Policy Distillation](https://arxiv.org/abs/2606.05718)

**<font color=#1a73e8>作者：</font>** Kanghui Tian, Siyuan Liu, Ziang Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) improves reasoning by training a student on trajectories sampled from its own policy under supervision from a teacher. In multimodal reasoning, a common extension is to use a privileged teacher that observes training-time-only signals such as reference answers or rationales. However, such answer-side privilege creates a train-test mismatch: the teacher's supervision may depend on signals unavailable to the student, encouraging shortcut imitation rather than visually grounded reasoning. We propose ViCuR, a visually grounded privileged-teacher distillation framework that replaces answer-side privilege with visual cues (query-related evidence in the input). Because these cues are derived from the same visual input available at inference, their evidence is recoverable by the student. To support this, ViCuR introduces a lightweight cue recovery module that uses dedicated sink-token cross-attention during prefill to aggregate task-relevant visual evidence into an internal representation, without changing the inference interface or requiring auxiliary cue-generation losses. Across seven benchmarks with Qwen3-VL-2B and 8B students, ViCuR consistently improves over answer-based on-policy self-distillation by +1.19 and +1.24 on overall average performance. It also extends naturally to stronger-teacher OPD, surpassing OPD baselines by +0.64 and +1.08, with consistent out-of-domain gains at the 8B scale. These results show that, in multimodal on-policy distillation, the design of teacher privilege is as important as teacher strength.

---


### 74. [When AI Says It Feels](https://arxiv.org/abs/2606.05734)

**<font color=#1a73e8>作者：</font>** Shin-nosuke Ishikawa, Seiya Ikeda, Hirotsugu Ohba  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are generally constrained from expressing feelings through human-preference alignment in post-training processes. This policy is designed using a top-down approach and may conflict with the goal of training models to exhibit human-like intelligence using human-generated texts. Here, we performed an experiment called Human-like Model eXpressions of Feeling (HMX-feel), in which LLMs were encouraged to express feelings, intentions, and self-awareness through self-rewarded reinforcement learning. We successfully enhanced these capabilities using a rubric-based self-rewarding training scheme with Group Relative Policy Optimization (GRPO). By comparing the trained models with contrastively trained models, we investigated the effects of this approach on performance across various tasks. Overall, we conducted a broad assessment from various perspectives and identified capabilities that were enhanced, degraded, or showed no significant change. The human-like-trained models showed robustness to sycophancy-inducing questions and bias in disambiguated conditions, whereas degradation in truthful question-answering capability was observed. The results of this experiment suggest the possibility of developing AI systems that can express feelings in the future, provided that appropriate measures are taken.

---


### 75. [PlanBench-V: A Spatial Planning Map Benchmark for Vision-Language Models](https://arxiv.org/abs/2606.05744)

**<font color=#1a73e8>作者：</font>** Minxin Chen, He Zhu, Junyou Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spatial planning maps are central to territorial governance, translating planning objectives, regulations, and spatial strategies into visual forms for decision-making, public communication, and institutional coordination. Their interpretation, however, requires fine-grained visual perception, spatial reasoning, and policy-informed professional judgment, creating major challenges for both human learners and AI systems. With the rapid progress of Vision-Language Models (VLMs), their use in urban planning analysis is gaining attention, yet existing multimodal benchmarks mainly target general visual understanding and overlook the domain-specific cognitive processes of planning practice. To address this gap, we introduce PlanBench-V, the first comprehensive benchmark for evaluating VLMs in spatial planning map interpretation. We first build the Spatial Planning Map Database (SPMD), an expert-annotated dataset of 223 planning maps and 1629 question-answer pairs curated by professional planners, covering diverse geographic regions and cartographic styles. We then propose a theory-informed evaluation framework assessing four progressive capabilities: Perception, Reasoning, Association, and Implementation, corresponding to the cognitive pipeline of planning map interpretation. Extensive experiments across two generations of VLMs show clear progress but persistent limitations. The best 2026 agentic reasoning model, Qwen3.6-Plus, substantially outperforms the best 2025 model, GPT-4o, by 27%. Nevertheless, all models still struggle with implementation-oriented tasks requiring evaluative judgment, policy sensitivity, and constraint-aware decision-making. These findings reveal fundamental limitations of current VLMs in professional planning contexts and highlight the need for domain-adaptive multimodal reasoning frameworks. Code and data are available at this https URL.

---


### 76. [MARDoc: A Memory-Aware Refinement Agent Framework for Multimodal Long Document QA](https://arxiv.org/abs/2606.05749)

**<font color=#1a73e8>作者：</font>** Kaifeng Chen, Hongtao Liu, Qiyao Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Iterative retrieval-reasoning agents have recently shown promise for multimodal long-document question answering. However, most existing systems maintain a single growing context that mixes retrieval traces, observations, and intermediate reasoning. As interactions accumulate, key evidence becomes scattered and diluted, making multi-hop reasoning noisy. We propose MARDoc, a Memory-Aware Refinement Agent framework that decouples long-document QA into three specialized agents: an Explorer for multi-granularity multimodal retrieval, a Refiner for distilling interaction traces into structured evidence and reasoning memories, and a Reflector for checking evidence sufficiency and providing targeted feedback. Across iterations, the agents rely on a dynamically updated structured memory rather than a full accumulated interaction history. This design reduces context noise while preserving answer-critical facts and their logical dependencies. Experiments on MMLongBench-Doc and DocBench show that MARDoc achieves strong results, outperforming same-backbone baselines and demonstrating the effectiveness of structured memory for agentic document QA.

---


### 77. [Cosine Misleads: Auxiliary Losses Reshape Vision Language Models, Not Their Latents](https://arxiv.org/abs/2606.05753)

**<font color=#1a73e8>作者：</font>** XiuYu Zhang, Junfeng Fang, Zhenkai Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent visual reasoning (LVR) inserts supervised latent tokens between perception and answer generation in vision-language models (VLMs). The field uses alignment between these latents and their visual targets, i.e., cosine similarity or mean squared error (MSE), as both the training loss and the quality metric, assuming that better alignment yields a better answer. We test this with a designed matrix of five LVR variants and find the assumption inverted: cosine alignment is negatively correlated with accuracy across all five (r=-0.94). To explain this, we introduce PRISM, a pair of inference-time diagnostics: a linear probe that asks where the answer is decodable, and a corruption test that asks whether the latent is load-bearing. The supervised latents are largely bypassed. Corrupting them shifts accuracy by at most four points. The answer is decodable downstream of the latent but not at it, and the size of this decodability gap predicts how much each variant relies on its latent under perturbation. Consistent with an Information Bottleneck reading of the loss, the auxiliary objective reshapes the language model via shared parameters rather than via the latent variable it nominally optimizes.

---


### 78. [DRIFT: A Residual Flow Adapter for Decoding Continuous Outputs in Vision-Language Models](https://arxiv.org/abs/2606.05758)

**<font color=#1a73e8>作者：</font>** Zhuoming Liu, Jinhong Lin, Kwan Man Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many modern vision-language models (VLMs) build on autoregressive decoding of discrete tokens. While text-based output interfaces enable scalable pretraining and strong zero-shot generalization across diverse tasks, they are poorly suited for problems that require precise continuous outputs, such as localizing temporal boundaries of events or generating robotic control actions. To address this challenge, we propose DRIFT, a general framework for adapting pretrained VLMs to continuous decoding tasks. DRIFT combines a base predictor, which provides a coarse estimate of the target output, with a generative refinement module based on flow matching that iteratively improves the prediction. This residual formulation transforms the generative modeling problem from learning a global output distribution to modeling a localized residual distribution around a strong prior, substantially simplifying optimization. We evaluate DRIFT on both perception and planning tasks, including visual grounding and robotic control. Across multiple tasks and architectures spanning MLLMs, VLAs, and WAMs, DRIFT consistently outperforms a strong set of regression- and generative-based solutions.

---


### 79. [ExpSpeech-Net: Multimodal Fusion of Expression and Speech for Deepfake Detection](https://arxiv.org/abs/2606.05760)

**<font color=#1a73e8>作者：</font>** Ruchika Sharma, Rudresh Dwivedi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake videos are increasingly challenging the credibility of online content. Many existing detection methodology relies on complex, resource-intensive models, which limit their practical use. The study introduces the ExpSpeech-Net deepfake detection (SqN-R-DFD) model, which utilizes SqueezeNet and RNN (Recurrent Neural Network) as its backbone, providing a lightweight and efficient deepfake detection framework that simultaneously analyzes facial expressions and speech patterns. The approach incorporates advanced feature extraction, such as ISLBT-based features for image and MPNCC for signals, along with a smart feature-selection strategy using SASMA (Sandpiper-Assisted Slime Mould Algorithm), ensuring optimal and balanced input to the detection models. By combining SqueezeNet and an RNN, subtle inconsistencies in deepfake videos are captured effectively. The framework achieves 94.5% accuracy, precision of 99.3%, and F-measure of 96.8%, outperforming conventional methods. This demonstrates that integrating multiple modalities with intelligent preprocessing and feature selection enables practical, real-time deepfake detection suitable for everyday applications.

---


### 80. [Imagine Before You Predict: Interleaved Latent Visual Reasoning for Video Event Prediction](https://arxiv.org/abs/2606.05769)

**<font color=#1a73e8>作者：</font>** Tianxiang Jiang, Linquan Wu, Sheng Xia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video event prediction (VEP) requires models to infer unobserved future states from partial video evidence. Existing video MLLMs usually verbalize intermediate future reasoning in text space: once visual evidence is verbalized, fine-grained motion, geometry, and interaction cues can be lost, leading to plausible but visually ungrounded hallucinations. We introduce Future-L1, an interleaved latent visual reasoning framework that lets an MLLM alternate between language tokens and continuous latent visual spans during autoregressive decoding. To train this capability, we construct Future-L1-50K by selecting examples where future visual hints help prediction and align latent states to future-frame embeddings, then further optimize sampled latent trajectories with LA-DAPO, a latent-aware RL objective with outcome-contrastive and temporal-diversity rewards. Future-L1 achieves new state-of-the-art results on both benchmarks: on FutureBench, it improves Qwen3-VL-8B from 61.0 to 85.4 and exceeds the previous best Video-CoE by 10.4 points; on TwiFF-Bench, it improves the average score from 2.44 to 3.04. These results suggest that future-oriented video reasoning benefits from preserving intermediate visual semantics in latent space rather than translating every reasoning step into text.

---


### 81. [Domain-Adapted Small Language Models with Hybrid Post-Processing: Achieving Cost-Efficient, Low-Latency Multi-Label Structured Prediction via LoRA Fine-Tuning on Scarce Data](https://arxiv.org/abs/2606.05781)

**<font color=#1a73e8>作者：</font>** Srinivasan Manoharan, Dilipkumar Nallusamy, Sachin Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying frontier large language models (LLMs) for domain-specific structured evaluation tasks often incurs substantial latency, cost, and data privacy overhead. We present a hybrid framework that combines a fine-tuned small language model (LLaMA 3.1 8B, with only 2.05% trainable parameters via LoRA) and a deterministic rule-based post-processing layer. Trained on just 219 curated examples, the system is applied to multi-label compliance evaluation of conversational transcripts spanning 18 heterogeneous output fields. In blind evaluation on 53 previously unseen production transcripts, it achieves 100% JSON structural validity, 83.0% human-validated overall accuracy, and 100% accuracy on the most critical classification field. The proposed approach formalizes a hybrid neural-symbolic decomposition and introduces targeted hard-negative augmentation to improve performance on critical decision boundaries. Running on a single NVIDIA A100 GPU, inference completes in approximately 2 seconds, which is 2-5x faster than frontier-model APIs. The system costs only $0.013 per evaluation compared with $0.025-$0.055 for proprietary alternatives, resulting in 46-76% cost savings. These results demonstrate that domain-adapted small language models, when combined with deterministic post-processing, can match frontier-model accuracy for structured compliance evaluation while substantially reducing operational cost, latency, and privacy risk.
Keywords: small language models, parameter-efficient fine-tuning, LoRA, domain adaptation, hybrid inference, compliance evaluation, structured output.

---


### 82. [TAPO: Tool-Aware Policy Optimization via Credit Transfer for Multimodal Search Agents](https://arxiv.org/abs/2606.05784)

**<font color=#1a73e8>作者：</font>** Chengqi Dong, Chuhuai Yue, Hang He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We identify and formally characterize credit misassignment as a systematic failure mode of GRPO in tool-augmented multimodal search agents: its uniform broadcast of trajectory-level advantages to all tokens causes valuable tool-use steps in failing trajectories to be penalized no differently from valueless ones. We further empirically quantify the scale of this phenomenon. Over half of failing trajectories and failing tool-use actions exhibit correctable credit misassignment, demonstrating that the wasted training signal is both substantial and structurally exploitable. Building on this insight, we propose Tool-Aware Policy Optimization (TAPO), which exploits the parameter-determinism property of information-acquisition tools: similar call parameters define equivalent information-acquisition actions and should therefore share comparable action credit. TAPO constructs counterfactual witnesses within the current training batch and compensates misassigned negative credit via confidence-gated conservative advantage correction. It requires no additional annotation, models, or sampling, and introduces negligible computational overhead. Across multiple multimodal search benchmarks, TAPO delivers consistent, plug-and-play improvements over strong baselines for three mainstream RL algorithms (GRPO, GSPO, and SAPO). Our code and models will be publicly released upon acceptance.

---


### 83. [Can LLMs Write Correct TLA+ Specifications? Evaluating Natural-Language-to-TLA+ Generation](https://arxiv.org/abs/2606.05792)

**<font color=#1a73e8>作者：</font>** Arslan Bisharat, Brian Ortiz, Eric Spencer 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> TLA+ has supported industrial verification at companies such as Amazon and Microsoft, yet writing correct TLA+ specifications from natural language still requires time and expertise, which limits adoption. LLMs show promise, but no prior study measures whether they produce semantically correct TLA+ specifications from natural language. This paper presents the first systematic evaluation of LLM-based TLA+ specification synthesis from natural language. Our study evaluates 30 LLMs across eight families on a curated dataset of 205 TLA+ specifications: 25 open-weight models across four prompting strategies (2,600 runs) and 5 proprietary models under few-shot prompting (130 runs), all validated by the SANY parser and TLC model checker. LLMs achieve up to 26.6% syntactic correctness but only 8.6% semantic correctness, with successes exclusive to progressive prompting. Results show that model size does not predict quality, e.g., DeepSeek r1:8b outperforms its 70B variant across all strategies, which suggests the importance of reasoning alignment for formal languages. Code-specialized models consistently underperform due to negative transfer from mainstream language training. We identify five recurring hallucination categories, all traceable to specific training data biases. These results suggest that current LLMs do not generate reliable TLA+ specifications without expert oversight. We release the evaluation framework, code, and dataset to support reproducibility and future research.

---


### 84. [CollabBench: Benchmarking and Unleashing Collaborative Ability of LLMs with Diverse Players via Proactive Engagement](https://arxiv.org/abs/2606.05793)

**<font color=#1a73e8>作者：</font>** Hong Qian, Yuanhao Liu, Zihan Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While LLM-based agents excel at individual tasks, effective collaboration with realistic human partners remains challenging. Most of the existing conversation-level collaborative studies lack grounded interaction and behavioral execution, motivating the need for cooperative game environments that enable contextualized and immersive collaboration. To this end, this paper proposes CollabBench, a benchmark for evaluating and training collaborative agents in cooperative games. CollabBench features a Diverse Player Profile Simulation pipeline to model varied players behaviors, and a Collaborative Agentic Training paradigm that unifies reasoning, communication, and action via agentic rollouts, optimized with a hybrid reward balancing task efficiency and affective adaptation. We further extend classic environments to CWAH-MultiPlayer and Cook-MultiPlayer for systematic evaluation under diverse personalities. Experiments with efficiency and affective metrics show that our trained models outperform base models, achieving 19.5% higher efficiency and 24.4% improved affective performance. Further analysis reveals key collaborative limitations of existing models and offers insights for future collaborative training.

---


### 85. [CaliDist: Calibrating Large Language Models via Behavioral Robustness to Distraction](https://arxiv.org/abs/2606.05799)

**<font color=#1a73e8>作者：</font>** Mohammad Anas Jawad, Cornelia Caragea  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing calibration methods for Large Language Models (LLMs) often overlook a critical dimension of trustworthiness: a model's {\em behavioral robustness} to irrelevant or misleading information. In this paper, we argue that a model's true confidence should reflect its stability under cognitive pressure. We introduce \textsc{CaliDist}, a novel post-hoc calibration approach that directly measures and penalizes a model's susceptibility to distraction. \textsc{CaliDist} quantifies how an LLM's predictions and uncertainty change when its input prompt is perturbed with semantic \textit{distractors}. This stability (or lack thereof) signal is then used to adaptively scale the model's initial confidence score. Our extensive experiments on seven Natural Language Understanding classification benchmarks using six distinct LLMs show that \textsc{CaliDist} consistently achieves lower Expected Calibration Error (ECE) and Brier Score compared with strong baselines. Remarkably, our method reduces the ECE from 23\% to 7\% on average--a relative improvement of 70\%--demonstrating that behavioral stability is a powerful signal for calibration. We make our code and datasets available at this http URL.

---


### 86. [Can LLMs Be Constrained to the Past? Improving Knowledge Cutoff through Recall-Based Prompting](https://arxiv.org/abs/2606.05804)

**<font color=#1a73e8>作者：</font>** Michiro Asai, Ailiang Lin, Yu Kishimoto 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompted knowledge cutoff instructs a large language model (LLM) to act as if information beyond a specified cutoff date were unavailable. However, prior work mainly relies on direct-answer generation, which struggles when post-cutoff knowledge is not explicitly queried but is only causally related to the question. To address this limitation, we propose two recall-based prompting strategies: Self-Recall (SR), which asks the model to restate its cutoff constraint, and Question-Recall (QR), which requires the model to recall question-relevant information valid under the cutoff. Across three existing benchmarks, our methods outperform both direct-answer prompting and conventional step-by-step reasoning baselines, with particularly strong improvements on counterfactual questions. To investigate robustness across different cutoff settings, we further construct the Multi-cutoff Historical Event Benchmark (MHEB), which evaluates the same question under multiple cutoff years. Results show that knowledge cutoff performance varies with cutoff distance, while combining SR and QR consistently yields the best performance.

---


### 87. [From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents](https://arxiv.org/abs/2606.05805)

**<font color=#1a73e8>作者：</font>** Yuhao Sun, Jiacheng Zhang, Shaanan Cohney 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based guardrails typically safeguard agents by evaluating proposed actions or inputs before execution, producing safety signals such as binary allow/deny decisions, risk categories, and/or explanatory rationales about potential policy violations. However, agent risks often arise when otherwise benign tasks are contaminated by untrusted external content, unsafe instructions, or risky tool use. Existing guardrails often flag the entire task uniformly as unsafe, thereby blocking the threat but sacrificing the benign part. Moreover, existing work largely evaluates guardrails in isolation, leaving unclear whether their interventions lead to safer downstream agent behavior. To address this, we introduce TRIAD (Tripartite Response for Iterative Agent Guardrailing), a guardrail-integrated agent framework that leverages guardrail-generated verbal feedback as a guiding signal to keep the agent aligned with benign objectives at each planning step. We finetune a language model on a self-curated training dataset to output one of three decisions: proceed, refuse, or update, together with structured natural-language feedback. Rather than merely allowing or blocking execution, update guides the agent to revise its plan, avoid harmful components, and preserve the benign task where possible. TRIAD injects this feedback into the agent's context, enabling subsequent plan revision and forming a closed loop between guardrail feedback and agent planning. Extensive experiments on ASB and AgentHarm show that TRIAD reduces the average attack success rate to 10.42%, while achieving the best safety-utility trade-off among guardrail-integrated baselines. Our code is available at: this https URL.

---


### 88. [When Tools Fail: Benchmarking Dynamic Replanning and Anomaly Recovery in LLM Agents](https://arxiv.org/abs/2606.05806)

**<font color=#1a73e8>作者：</font>** Dongsheng Zhu, Xuchen Ma, Yucheng Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks evaluate Tool-Integrated Reasoning (TIR) in LLMs on idealized ''happy paths'', largely overlooking real-world tool failures. We introduce ToolMaze, a benchmark for dynamic path discovery and error recovery in TIR agents. To separate systematic replanning from blind trial-and-error, ToolMaze adopts a two-dimensional design: DAG-based topological complexity and a $2 \times 2$ taxonomy of tool perturbations (explicit/implicit, transient/permanent). Evaluations show that perturbations degrade performance across nearly all models, with the sharpest drops under implicit semantic failures. Driven by systemic over-trust in corrupted outputs, Perturbation Recovery Rate (PRR) plummets by around 37\% in these scenarios, while complex topologies trap agents in futile trial-and-error loops. Crucially, agentic fault-tolerance improves with model scale $3.66\times$ slower than basic task execution, highlighting dynamic replanning as a distinct bottleneck unaddressed by model scaling or prompting. Data and code are available at this https URL.

---


### 89. [Emotion-Aware Image Generation from Korean Diary Text via LLM-based Prompt Translation and LoRA Fine-Tuning](https://arxiv.org/abs/2606.05816)

**<font color=#1a73e8>作者：</font>** Jihun Cho, Soo-Yeon Jeong, Sun-Young Ihm  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> T2I models cannot effectively capture sentiment from various types of text, including diaries, as they primarily focus on visual object-related patterns rather than contextual emotional understanding. This paper proposes an emotion-aware text-to-image pipeline that generates children's hand drawing style images from short Korean diary entries. The proposed pipeline employs Qwen3-8B for recognising implicit sentiment from short diaries, and Stable Diffusion 3.5 Medium fine-tuned with LoRA on children's drawing images with emotion-based trigger words for image generation. Additionally, this paper presents experiments examining the effect of emotion trigger words on generated images and discusses the limitations of CLIP Score as an evaluation metric for emotion-aware image generation.

---


### 90. [Statistical Priors for Implicit Preferences: Decoupling Skill Selection as a Local Harness in Personal Agents](https://arxiv.org/abs/2606.05828)

**<font color=#1a73e8>作者：</font>** Zeyu Gan, Huayi Tang, Yong Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Model (LLM) capabilities advance, locally deployed personal agents relying on API-based remote models and external skills have emerged as a novel paradigm. With the rapid expansion of available skills, enabling personal agents to learn and adapt to implicit user preferences becomes a critical challenge. However, local deployment constraints preclude complex centralized selection algorithms, creating an urgent need for a lightweight local preference harness. This paper explores the implementation of such a harness through a novel architecture that strictly decouples statistical preference learning from semantic intent parsing. Specifically, we leverage localized statistical results to influence and modulate the selection decisions of the remote LLM. Extensive evaluations demonstrate that our decoupled approach achieves the lowest cumulative regret and highest test accuracy, significantly outperforming traditional memory-augmented agents.

---


### 91. [Learning Geometric Representations from Videos for Spatial Intelligent Multimodal Large Language Models](https://arxiv.org/abs/2606.05833)

**<font color=#1a73e8>作者：</font>** Haibo Wang, Lifu Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) excel at 2D semantic understanding but lack intrinsic 3D awareness, resulting in representations that fail to maintain geometric and spatial consistency across video frames. Given the scarcity of large-scale 3D data, we present GeoVR, a novel framework that learns geometric representations using purely 2D video sequences. This approach effectively restructures the semantic latent space within MLLMs to unlock spatial intelligence. Rather than employing superficial feature mixing, GeoVR reshapes the internal representations of the MLLM by distilling geometry knowledge from pre-trained 3D foundation models. This is accomplished through a multi-objective learning strategy driven by four complementary geometric targets: (1) estimating inter-frame camera poses to embed varying viewpoint dynamics, (2) regressing dense depth maps to anchor physical distances, (3) predicting a metric scale factor for real-world calibration, and (4) distilling multi-scale 3D features to align the intermediate feature space. Guided by these explicit physical and geometric constraints, the model's internal representations naturally develop strong 3D awareness. Extensive experiments on spatial reasoning benchmarks demonstrate that GeoVR achieves state-of-the-art performance, establishing a new paradigm for endowing foundation models with spatial intelligence.

---


### 92. [ProSPy: A Profiling-Driven SQL-Python Agentic Framework for Enterprise Text-to-SQL](https://arxiv.org/abs/2606.05836)

**<font color=#1a73e8>作者：</font>** Zhaorui Yang, Huawei Zheng, Sen Yang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have substantially advanced Text-to-SQL systems, yet applying them to enterprise-scale databases remains challenging. Real-world databases often contain large and heterogeneous schemas, incomplete metadata, dialect-specific SQL syntax, and complex analytical questions that are difficult to solve with a single SQL query. To address these challenges, we propose ProSPy, a Profiling-driven SQL--Python agentic framework for enterprise-scale Text-to-SQL. ProSPy structures the reasoning process into four stages: it first extracts fine-grained data evidence through automatic profiling, progressively prunes large schemas into task-relevant contexts, fetches intermediate views through a dialect-agnostic SQL interface, and finally performs flexible downstream analysis with Python. This design combines the efficiency of SQL over large databases with the flexibility of Python-based analysis, while reducing reliance on unreliable metadata and improving robustness across SQL dialects. Experiments on Spider 2.0-Lite and Spider 2.0-Snow show that ProSPy consistently outperforms strong baselines with both open-source and proprietary models, achieving execution accuracies of 60.15% and 60.51% with Claude-4.5-Opus, without majority voting. Further analysis shows that ProSPy is robust to SQL dialect variations and achieves a favorable trade-off between schema recall and precision.

---


### 93. [Mechanistic Insights into Functional Sparsity in Multimodal LLMs via CoRe Heads](https://arxiv.org/abs/2606.05843)

**<font color=#1a73e8>作者：</font>** Ruoxi Sun, Quantong Qiu, Juntao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) demonstrate remarkable proficiency on complex vision-language tasks, the mechanisms by which they extract query-relevant visual features from complex, noisy contexts remain opaque. In this paper, we present an in-depth interpretability study that uncovers a profound structural property within MLLMs: functional sparsity in cross-modal retrieval. Leveraging a token-level metric termed Retrieval Attention Mass (RAM), we identify and characterize a highly specialized subset of attention heads, referred to as Context-aware Retrieval (CoRe) heads. Across diverse visual domains and model scales, we observe a clear functional division: CoRe heads act as dedicated information extractors, while most other heads distribute attention over broader contextual regions. Causal interventions further demonstrate the necessity of these specialized heads. Ablating only the top 5% of CoRe heads causes significant degradation in multimodal reasoning performance, whereas ablating lower-ranked heads has minimal effect. Moreover, acceleration experiments validate the utility of CoRe heads, showing that leveraging this localized sparsity significantly accelerates inference while maintaining robust task performance. Our findings reveal a structural principle of functional sparsity within MLLMs, refining the current understanding of mechanistic interpretability and laying a theoretical foundation that can inspire future architecture design and model optimization.

---


### 94. [Agentic Molecular Recovery via Molecule-Aware Exploration](https://arxiv.org/abs/2606.05847)

**<font color=#1a73e8>作者：</font>** Suwan Yoon, Changhee Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-guided molecular generation with LLMs often yields invalid SMILES. We argue that invalid drafts should be addressed through a shift from validity-oriented repair to identity-preserving molecular recovery: the objective is not only to restore chemical validity, but also to preserve target-relevant structural cues and recover the molecular identity implied by the description. This perspective reveals the limitations of existing correction strategies. Post-hoc repair can recover validity while distorting key structures, LLM-only correction can introduce unintended global drift, and generic agentic correction remains constrained by greedy single-candidate trajectories even when equipped with executable RDKit edit tools. To address these limitations, we propose AMREC, which couples molecule-aware mismatch tracking with expanded candidate exploration and trajectory-level selection. On invalid ChEBI-20 drafts from three backbone models, AMREC achieves the strongest overall recovery profile across structural, exact-match, and string-level metrics.

---


### 95. [ReverseEOL: Improving Training-free Text Embeddings via Text Reversal in Decoder-only LLMs](https://arxiv.org/abs/2606.05858)

**<font color=#1a73e8>作者：</font>** Ailiang Lin, Zhuoyun Li, Yusong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have opened new avenues for generating training-free text embeddings. However, the causal attention in decoder-only LLMs prevents earlier tokens from attending to future context, leading to biased contextualized representations. In this work, we propose Reverse prompting with Explicit One-word Limitation (ReverseEOL), a simple yet effective method for enhancing the representational capability of frozen LLMs. ReverseEOL augments the standard forward embedding with an additional reversed embedding derived from the reversed input text. Since reversing the input exposes each token to context inaccessible in the original order, the resulting reversed embedding effectively provides complementary information to the original one. As a result, combining the forward and reversed embeddings yields a richer final representation. Comprehensive experiments on STS and MTEB benchmarks demonstrate that ReverseEOL significantly improves the performance of existing training-free baselines across a broad range of LLMs with diverse architectures and scales. Extensive ablations and analyses further confirm the necessity of our reversal mechanism.

---


### 96. [TARPO: Token-Wise Latent-Explicit Reasoning via Action-Routing Policy Optimization](https://arxiv.org/abs/2606.05859)

**<font color=#1a73e8>作者：</font>** Liting Zhang, Shiwan Zhao, Xuyang Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latent reasoning has emerged as a promising alternative to discrete Chain-of-Thought (CoT) in large language models (LLMs), enabling more expressive reasoning by operating over continuous representations. However, the inherently deterministic nature of continuous representations limits policy exploration in reinforcement learning (RL). To address this, we propose TARPO (Token-Wise Latent-Explicit Reasoning via Action-Routing Policy Optimization), a pure RL framework that adaptively switches between discrete token generation and continuous latent reasoning at each step. TARPO introduces a lightweight action head router that observes the current hidden state and samples a routing decision from a binary mode-selection space, preserving the stochasticity of discrete token sampling from the vocabulary. The LLM backbone and router are jointly optimized end-to-end with a shared group-relative advantage signal. Extensive experiments across Qwen2.5 (from 1.5B to 7B) and Llama-3.1-8B backbones demonstrate that TARPO consistently outperforms existing explicit and latent reasoning RL baselines across diverse benchmarks. Further analysis shows that TARPO learns adaptive token-wise switching behaviors while maintaining stable training dynamics. Our code is available at this https URL.

---


### 97. [GenAutoML: An Agentic Framework for Dynamic Architecture Generation and Optimization in Time-Series Analysis](https://arxiv.org/abs/2606.05860)

**<font color=#1a73e8>作者：</font>** Oleeviya Babu Poikarayil, Cédric Schockaert, Abdulrahman Nahhas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing neural architectures for time-series forecasting and anomaly detection remains a resource-intensive task that often requires substantial domain expertise. Traditional Automated Machine Learning (AutoML) systems typically rely on static, predefined search spaces, limiting their ability to adapt to diverse data characteristics. We present GenAutoML, an agentic framework that leverages Large Language Models (LLMs) as neural architects to bridge natural-language requirements and executable PyTorch implementations. The framework incorporates a Sandboxed Reflection Loop for autonomous code refinement and a Signature-Aware Runtime that enforces architectural consistency and execution safety. To improve robustness under non-stationary conditions, we further introduce a Dynamic Reversible Instance Normalization (Dyn-RevIN) wrapper. Experiments on the ETTh1, ETTm1, and Weather benchmarks demonstrate that GenAutoML can dynamically generate task-specific neural architectures tailored to dataset characteristics. Among the generated models, WaveInterferenceNet achieves inference latency below 0.01 ms per sample while maintaining competitive predictive performance. By emphasizing computational efficiency, architectural adaptability, and stable optimization behavior, GenAutoML enables the creation of ultra-lightweight neural networks suitable for resource-constrained and latency-sensitive Edge AI deployments.

---


### 98. [Analysis of the Neglect-Zero Effect in Large Language Models](https://arxiv.org/abs/2606.05864)

**<font color=#1a73e8>作者：</font>** Jin Tanaka, Daiki Matsuoka, Ryoma Kumon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate the extent to which the language processing of LLMs resembles human cognitive processes, focusing on a human cognitive bias called the $\textit{neglect-zero effect}$. This effect refers to the human tendency to ignore $\textit{zero-models}$, which are configurations that render a proposition vacuously true by virtue of an empty set. We focus on two types of inferences driven by the neglect-zero effect, and examine how LLMs process these inferences by comparing their behavior with that in an inference that does not involve the neglect-zero effect. For this purpose, we employ a paradigm based on $\textit{structural priming}$, where recent exposure to a preceding sentence (the $\textit{prime}$) facilitates the processing of a subsequent sentence (the $\textit{target}$) due to their structural similarity. We prepare primes to force LLMs to consider the zero-model, and analyze whether they also consider it in the target. The results suggest that the neglect-zero effect may not occur in the LLMs analyzed in this study. Our code is available at this https URL

---


### 99. [YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition](https://arxiv.org/abs/2606.05868)

**<font color=#1a73e8>作者：</font>** PSBC LLM Team, Huawei LLM Team, Ruihan Long 等 59 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) drive significant financial innovations, yet their high-concurrency deployment is severely bottlenecked by KV cache memory overhead, which inflates infrastructure costs and throttles scalability. To address this, we propose YouZhi-LLM, a highly efficient financial LLM empowered by a comprehensive structural transition and training pipeline natively built on the Huawei Ascend ecosystem. At its algorithmic core, YouZhi-LLM features a layer-adaptive GQA-to-MLA transition framework that dynamically assigns per-layer FreqFold sizes, maximizing KV-cache compression while minimizing perplexity degradation. To recover representation capacity and inject domain expertise, the Ascend-based training pipeline seamlessly integrates generalized knowledge distillation with financial-specific supervised fine-tuning. Evaluations demonstrate the superiority of this systematic approach, with the adaptive transition reducing perplexity degradation by up to 35% over uniform baselines. Crucially, when evaluated on Ascend NPUs via vLLM-Ascend, the massive KV-cache reduction translates directly into deployment efficiency. Compared to their respective base models, YouZhi-7B yields a 12.3% improvement in average financial benchmark score alongside a 2.69$\times$ increase in maximum concurrency; similarly, YouZhi-14B achieves a 7.0% accuracy gain and a 2.43$\times$ concurrency boost, establishing a new paradigm for cost-effective, high-throughput financial inference.

---


### 100. [Evaluating Stochastic Collapse and Implicit Bias in Multimodal Large Language Models](https://arxiv.org/abs/2606.05874)

**<font color=#1a73e8>作者：</font>** Huiyuan Zheng, Houtao Zhang, Boyang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current evaluations for Multimodal Large Language Models (MLLMs) overwhelmingly focus on utility-driven objectives, leaving model behavior under logic-neutral scenarios largely underexplored. Stochasticity is essential in scenarios where multiple actions are equally valid, such as recommending travel itineraries or daily schedules where multiple options have similar utility. In such settings, deterministic policies may lead to repetitive behaviors and reduced coverage of valid alternatives. To bridge this gap, we propose RandomBench, a benchmark designed to evaluate whether MLLMs can maintain distributionally neutral behavior when selecting among equivalent options. We further introduce three metrics, including RI, BCI, BII, to quantify entropy and distributional bias. Experiments reveal a pervasive phenomenon termed Stochastic Collapse, where MLLMs fail to maintain uniform randomness under explicit random instructions, with top-1 probabilities reaching 97% from the ideal one quarter baseline and RI dropping to 0.068 in Claude Sonnet 4.6. Extensive ablation studies further demonstrate that these deviations persist across languages and representation formats, highlighting the robustness of distributional collapse in logic-neutral decision settings.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-185](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
