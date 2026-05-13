# 🧠 大模型相关研究 | 2026年05月13日

> 本类共 **223** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-223](./part-05.md)

---

### 51. [JACoP: Joint Alignment for Compliant Multi-Agent Prediction](https://arxiv.org/abs/2605.11385)

**<font color=#1a73e8>作者：</font>** Qingze Liu, Alen Mrdovic, Danrui Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stochastic Human Trajectory Prediction (HTP) using generative modeling has emerged as a significant area of research. Although state-of-the-art models excel in optimizing the accuracy of individual agents, they often struggle to generate predictions that are collectively compliant, leading to output trajectories marred by social collisions and environmental violations, thus rendering them impractical for real-world applications. To bridge this gap, we present JACoP: Joint Alignment for Compliant Multi-Agent Prediction, an innovative multi-stage framework that ensures scene-level plausibility. JACoP incorporates an Anchor-Based Agent-Centric Profiler for effective initial compliance filtering and employs a Markov Random Field (MRF) based aligner to formalize the joint selection for scene predictions. By representing inter-agent spatial and social costs as MRF energy potentials, we successfully infer and sample from the joint trajectory distribution, achieving prediction with optimal scene compliance. Comprehensive experiments show that JACoP not only achieves competitive accuracy, but also sets a new standard in reducing both environmental violations and social collisions, thereby confirming its ability to produce collectively feasible and practically applicable trajectory predictions.

---


### 52. [Behavioral Mode Discovery for Fine-tuning Multimodal Generative Policies](https://arxiv.org/abs/2605.11387)

**<font color=#1a73e8>作者：</font>** Alberta Longhini, David Emukpere, Jean-Michel Renders 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the problem of fine-tuning pre-trained generative policies with reinforcement learning (RL) while preserving the multimodality of their action distributions. Existing methods for RL fine-tuning of generative policies (e.g., diffusion policies) improve task performance but often collapse diverse behaviors into a single reward-maximizing mode. To mitigate this issue, we propose an unsupervised mode discovery framework that uncovers latent behavioral modes within generative policies. The discovered modes enable the use of mutual information as an intrinsic reward, regularizing RL fine-tuning to enhance task success while maintaining behavioral diversity. Experiments on robotic manipulation tasks demonstrate that our method consistently outperforms conventional fine-tuning approaches, achieving higher success rates and preserving richer multimodal action distributions.

---


### 53. [Deep Reasoning in General Purpose Agents via Structured Meta-Cognition](https://arxiv.org/abs/2605.11388)

**<font color=#1a73e8>作者：</font>** Dean Light, Michael Theologitis, Kshitish Ghate 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans intuitively solve complex problems by flexibly shifting among reasoning modes: they plan, execute, revise intermediate goals, resolve ambiguity through associative judgment, and apply formal procedures to well-specified subproblems. Current LLM agents lack this flexibility, as their scaffolds hard-code such reasoning decisions in advance. These scaffolds are effective when their prescribed structure matches the task, but brittle when solving the task requires adapting the structure of reasoning itself. We introduce Deep Reasoning -- an inference-time approach for constructing task-specific scaffolds through structured meta-reasoning. Deep Reasoning uses a formal language that represents meta-reasoning as executable decompositions over associative inference, formal computation, and recursive subproblem solving, enabling decomposition principles to be encoded as in-context examples that guide test-time scaffold construction. We instantiate this approach in a general-purpose agent (DOLORES) that distributes complex tasks across more controlled reasoning threads. We evaluate it against state-of-the-art scaffolding methods across four hard benchmarks: multi-hop reasoning, long-chain question answering, long-context aggregation, and deep research-style information seeking. DOLORES outperforms all evaluated scaffolds across three model sizes and two model families, improving over the strongest evaluated scaffold baseline by 24.8% on average. DOLORES distributes cognition across structured, lower-load reasoning threads, thereby reducing premature termination and hallucinations. This advantage can even bridge the scaling gap, with an 8B version surpassing all evaluated 32B baselines from the same family in more than half the settings. These results point toward future agentic systems that treat scaffolding as adaptive reasoning, constructing the structure each task requires just-in-time.

---


### 54. [MuonQ: Enhancing Low-Bit Muon Quantization via Directional Fidelity Optimization](https://arxiv.org/abs/2605.11396)

**<font color=#1a73e8>作者：</font>** Yupeng Su, Ruijie Zhang, Ziyue Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Muon optimizer has emerged as a compelling alternative to Adam for training large language models, achieving remarkable computational savings through gradient orthogonalization. However, Muon's optimizer state is more sensitive to quantization errors: because the orthogonalization discards the magnitudes of singular values and retains only directional information, even small quantization errors in singular vector directions are amplified in the update. In this work, we propose MuonQ, a low-bit Muon training framework built on the principle of directional fidelity optimization. First, we apply a pre-quantization normalization so that each step introduces quantization errors of the same magnitude, preventing the accumulated error from developing a preferred direction. Second, we introduce a structural decomposition that separately quantizes the dominant singular components via power iteration, ensuring that quantization errors perturb only singular value magnitudes rather than rotating singular vector directions. Third, we adopt $\mu$-law companding quantization to allocate higher resolution to densely packed momentum values, shifting the quantization objective from outlier preservation to dense-region distinguishability. Together, these techniques enable stable 4-bit quantization of Muon's optimizer states. Pre-training experiments on GPT-style and LLaMA-style models demonstrate that MuonQ at 4-bit precision closely matches full-precision Muon in both training loss and downstream task accuracy, while reducing optimizer state memory by up to 7.3 $\times$. Our code is available at this https URL.

---


### 55. [AcuityBench: Evaluating Clinical Acuity Identification and Uncertainty Alignment](https://arxiv.org/abs/2605.11398)

**<font color=#1a73e8>作者：</font>** Robin Linzmayer, Georgianna Lin, Di Coneybeare 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce AcuityBench, a benchmark for evaluating whether language models identify the appropriate urgency of care from user medical presentations. Existing health benchmarks emphasize medical question answering, broad health interactions, or narrow workflow-specific triage tasks, but they do not offer a unified evaluation of acuity identification across these settings. AcuityBench addresses this gap by harmonizing five public datasets spanning user conversations, online forum posts, clinical vignettes, and patient portal messages under a shared four-level acuity framework ranging from home monitoring to immediate emergency care. The benchmark contains 914 cases, including 697 consensus cases for standard accuracy evaluation and 217 physician-confirmed ambiguous cases for uncertainty-aware evaluation. It supports two complementary task formats: explicit four-way classification in a QA setting, and free-form conversational responses evaluated with a rubric-based judge anchored to the same framework. Across 12 frontier proprietary and open-weight models, we find substantial variation in clear-case acuity accuracy and error direction. Comparing task formats reveals a systematic tradeoff: conversational responses reduce over-triage but increase under-triage relative to QA, especially in higher-acuity cases. In ambiguous cases, no model closely matches the distribution of physician judgments, and model predictions are more concentrated than expert clinical uncertainty. We also compare expert and model adjudication on a subset of maximally ambiguous cases, using those cases to examine the role of clinical uncertainty in label disagreement. Together, these results position acuity identification as a distinct safety-critical capability and show that AcuityBench enables systematic comparison and stress-testing of how well models guide users to the right level of care in real-world health use.

---


### 56. [fg-expo: Frontier-guided exploration-prioritized policy optimization via adaptive kl and gaussian curriculum](https://arxiv.org/abs/2605.11403)

**<font color=#1a73e8>作者：</font>** Mingxiong Lin, Zhangquan Gong, Maowen Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has become the standard paradigm for LLM mathematical reasoning, with Group Relative Policy Optimization (GRPO) serving as the dominant algorithm. We identify two overlooked inefficiencies inherent in GRPO. First, a fixed KL coefficient overly restricts policy exploration at moments when the model needs to diverge significantly from the reference policy. Second, uniform question sampling overlooks that moderately difficult problems produce the most informative gradient signals. We propose FG-ExPO, short for Frontier-Guided Exploration-Prioritized Policy Optimization, which integrates two lightweight components. Accuracy-Conditioned KL Scaling (AKL) adjusts the KL penalty strength through a smooth nonlinear function of batch average accuracy, loosening the constraint when the model performs poorly and strengthening it when the model achieves satisfactory results. Gaussian Curriculum Sampling (GCS) assigns sampling weights to questions following a Gaussian distribution centered at a moderate accuracy level around 0.5, focusing model training on its learning frontier. We conduct evaluations on DeepSeek-R1-Distill-Qwen-1.5B and Qwen3-8B-Base across six mainstream mathematical reasoning benchmarks. Experimental results demonstrate that FG-ExPO consistently outperforms vanilla GRPO. It delivers an absolute improvement of 13.34 on the AIME 2025 pass@32 metric, rising from 63.33 percent to 76.67 percent, and obtains an average pass@32 gain of 2.66 on the 8B model. The substantially larger performance gains observed on pass@32 compared to pass@1 verify that FG-ExPO enlarges the model's effective exploration space under a fixed inference budget.

---


### 57. [20/20 Vision Language Models: A Prescription for Better VLMs through Data Curation Alone](https://arxiv.org/abs/2605.11405)

**<font color=#1a73e8>作者：</font>** Siddharth Joshi, Haoli Yin, Rishabh Adiga 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data curation has shifted the quality-compute frontier for language-model and contrastive image-text pretraining, but its role for vision-language models (VLMs) is far less established. We ask how far data curation alone can take VLM performance, holding architecture, training recipe, and compute fixed and varying only the training data. Our pipeline, applied to the MAmmoTH-VL single-image subset, lifts performance by +11.7pp on average across 20 public VLM benchmarks (spanning grounding, VQA, OCR/documents, captioning, spatial/3D, counting, charts, math, brand-ID, and multi-image reasoning) and by +11.3pp on average across all nine capability axes of DatBench, our high-fidelity VLM eval suite. At 2B, our curated model surpasses InternVL3.5-2B by 9.9pp at ~17x less training compute and closes the gap to Qwen3-VL-2B to within 1.8pp at ~87x less compute, from pretraining alone. Beyond accuracy, curation delivers four further properties: (1) Reliability: per-capability std across training seeds drops by ~67% and the lift survives a 4k-to-16k context-length sweep; (2) OOD generalization: the 9-eval OOD average rises by +7.2pp, and multi-image BLINK rises by +3.09pp despite single-image-only training, with Visual Correspondence gaining +11.8pp; (3) Behavioral gains beyond benchmarks: across ~1,100 open-ended queries the curated 2B is more honest and more specific than the matched-compute baseline, and more concise and less refusal-prone than a frontier 2B reference; (4) Pareto-dominance on inference cost: at every scale (1B, 2B, 4B) the curated model raises accuracy while lowering response FLOPs vs. the matched-compute baseline, and the curated 4B matches near-frontier accuracy at 3.3x lower response FLOPs than Qwen3-VL-4B. Data curation is a high-leverage tool for building better VLMs, reaching near-frontier accuracy at up to ~150x less training compute.

---


### 58. [What Do EEG Foundation Models Capture from Human Brain Signals?](https://arxiv.org/abs/2605.11410)

**<font color=#1a73e8>作者：</font>** Ling Tang, Qian Chen, Jilin Mei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical electroencephalogram (EEG) analysis rests on a hand-crafted feature catalog refined over decades, \emph{e.g.,} band power, connectivity, complexity, and more. Modern EEG foundation models bypass this catalog, learn directly from raw signals via self-supervised pretraining, and match or outperform feature-engineered baselines on most clinical benchmarks. Whether the two representations align is an open question, which we decompose into three sub-questions: \emph{what does the model learn}, \emph{what does the model use}, and \emph{how much can be explained}. We answer them with layer-wise ridge probing, LEACE-style cross-covariance subspace erasure, and a transparent classifier benchmarked against a random-feature baseline. The audit covers three foundation models (CSBrain, CBraMod, LaBraM), five clinical tasks (MDD, Stress, ISRUC-Sleep, TUSL, Siena), and a 6-family 63-feature lexicon. Of the $945$ (model, task, feature) units, $648$ ($68.6\%$) are representation-causal and $199$ ($21.1\%$) are encoded-only. Across tasks, $50$ features qualify as universal candidates with strong support (all three architectures RC) in two or more tasks. Frequency-domain features dominate, but the other five families each contribute substantial causal mass. Confirmed features recover, on average, $79.3\%$ of the foundation model's advantage over the random baseline, with a clean task gradient (MDD $\approx 0.99$ down to Stress $\approx 0.56$): tasks near ceiling are almost fully recovered by the lexicon, while harder tasks leave a non-trivial residual that pinpoints a concrete target for future concept discovery.

---


### 59. [Freeze Deep, Train Shallow: Interpretable Layer Allocation for Continued Pre-Training](https://arxiv.org/abs/2605.11416)

**<font color=#1a73e8>作者：</font>** Yu-Hang Wu, Qin-Yuan Liu, Qiu-Yang Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Selective layer-wise updates are essential for low-cost continued pre-training of Large Language Models (LLMs), yet determining which layers to freeze or train remains an empirical black-box problem due to the lack of interpretable guidance. To address this issue, we propose LayerTracer, an architecture-agnostic diagnostic framework that reveals the evolution patterns of layer-wise representations and stability by locating task execution positions and quantifying layer sensitivity. Analysis results reveal that deep layers act as critical regions for task execution and maintain high stability against disruptive updates. Guided by this finding, we conduct three controlled continued pre-training trials to compare diverse freeze-train strategies, demonstrating that training shallow layers while freezing deep layers consistently outperforms full-parameter fine-tuning and the opposite allocation on both C-Eval and CMMLU benchmarks. We further present a hybrid model case study, which validates that placing high-quality pre-trained modules in deep layers effectively preserves inherent knowledge of the model. This work delivers a low-cost and interpretable solution for resource-constrained teams, offering actionable guidance for layer-wise parameter allocation in continued pre-training and hybrid model construction.

---


### 60. [A Mechanistic Investigation of Supervised Fine Tuning](https://arxiv.org/abs/2605.11426)

**<font color=#1a73e8>作者：</font>** Ruhaan Chopra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The cosine similarity between a large language model's hidden activations before and after Supervised Fine-Tuning (SFT) remains very high. This, at first glance, suggests that SFT leaves the model's activation geometry largely undisturbed. However, projecting both sets of activations through a Sparse Autoencoder (SAE) pretrained on the base model reveals that the underlying sparse latents diverge significantly. We introduce a novel investigative pipeline which utilizes these pretrained SAEs as a high-resolution diagnostic tool to mechanistically investigate the drivers of this representational divergence. Through our analytical pipeline, we discover task-specific and layer-specific distributions of the precise semantic features that are systematically altered during supervised fine-tuning. We additionally identify a layer-wise update profile specific to safety alignment. All code, experimental scripts, and analysis files associated with this work are publicly available at: this https URL.

---


### 61. [Agent-BRACE: Decoupling Beliefs from Actions in Long-Horizon Tasks via Verbalized State Uncertainty](https://arxiv.org/abs/2605.11436)

**<font color=#1a73e8>作者：</font>** Joykirat Singh, Zaid Khan, Archiki Prasad 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed on long-horizon tasks in partially observable environments, where they must act while inferring and tracking a complex environment state over many steps. This leads to two challenges: partial observability requires maintaining uncertainty over unobserved world attributes, and long interaction history causes context to grow without bound, diluting task-relevant information. A principled solution to both challenges is a belief state: a posterior distribution over environment states given past observations and actions, which compactly encodes history for decision making regardless of episode length. In LLM agents, however, the open-ended nature of text makes it unclear how to represent such a distribution. Therefore, we introduce Agent-BRACE: Agent Belief state Representation via Abstraction and Confidence Estimation, a method that decouples an LLM agent into a belief state model and a policy model, jointly optimized via reinforcement learning. The belief state model produces a structured approximation of the belief distribution: a set of atomic natural language claims about the environment, each annotated with an ordinal verbalized certainty label ranging from certain to unknown. The policy model conditions on this compact, structured approximate belief rather than the full history, learning to select actions under explicit uncertainty. Across long-horizon, partially observable embodied language environments, Agent-BRACE achieves an average absolute improvement of +14.5% (Qwen2.5-3B-Instruct) and +5.3% (Qwen3-4B-Instruct), outperforming strong RL baselines while maintaining a near-constant context window independent of episode length. Further analysis shows that the learned belief becomes increasingly calibrated over the course of an episode as evidence accumulates.

---


### 62. [Instruct-ICL: Instruction-Guided In-Context Learning for Post-Disaster Damage Assessment](https://arxiv.org/abs/2605.11439)

**<font color=#1a73e8>作者：</font>** Armin Zarbaft, Ehsan Karimi, Nhut Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid and accurate situational awareness is essential for effective response during natural disasters, where delays in analysis can significantly hinder decision-making. Training task-specific models for post-disaster assessment is often time-consuming and computationally expensive, making such approaches impractical in time-critical scenarios. Consequently, pretrained multimodal large language models (MLLMs) have emerged as a promising alternative for post-disaster visual question answering (VQA), a task that aims to answer structured questions about visual scenes by jointly reasoning over images and text. While these models demonstrate strong multimodal reasoning capabilities, their responses can be sensitive to prompt formulation, which can limit their reliability in real-world disaster assessment scenarios. In this paper, we investigate whether structured reasoning strategies can improve the reliability of pretrained MLLMs for post-disaster VQA. Specifically, we explore multiple prompting paradigms in which one MLLM is used to generate task-specific instructions that serve as Chain-of-Thought (CoT) guidance for a second MLLM. These instructions are incorporated during answer generation with varying degrees of in-context learning (ICL), enabling the model to leverage both explicit reasoning guidance and contextual examples. We conduct our evaluation on the FloodNet dataset and compare these approaches against a zero-shot baseline. Our results demonstrate that integrating instruction-driven CoT reasoning consistently improves answer accuracy.

---


### 63. [Leveraging Multimodal Large Language Models for All-in-One Image Restoration via a Mixture of Frequency Experts](https://arxiv.org/abs/2605.11444)

**<font color=#1a73e8>作者：</font>** Eunho Lee, Youngbae Hwang, Rei Kawakami  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> All-in-one image restoration seeks to recover clean images from inputs affected by diverse and unknown degradations using a unified framework. Recent methods have shown strong performance by identifying degradation characteristics to guide the restoration process. However, many of them treat degradations as discrete categories, which limits their ability to model the continuous relational structure that arises in composite degradations. To address this issue, we propose a multimodal large language model (MLLM)-guided image restoration framework that exploits multimodal embeddings as guidance for low-level restoration. Specifically, MLLM-derived features are injected into an encoder-decoder architecture through an MLLM-guided fusion block (MGFB) to enhance degradation-aware representations. In addition, we incorporate a mixture-of-frequency-experts (MoFE) module that adaptively combines frequency experts using MLLM-guided contextual cues. To further improve expert routing, we design an MLLM-guided router with a relational alignment loss that encourages routing patterns consistent with the embedding-space relationships of degraded inputs. Extensive experiments on multiple benchmarks show that the proposed method achieves strong performance across diverse restoration settings and establishes a new state of the art on the challenging CDD11 dataset, outperforming previous methods by up to 1.35 dB.

---


### 64. [Predictive Maps of Multi-Agent Reasoning: A Successor-Representation Spectrum for LLM Communication Topologies](https://arxiv.org/abs/2605.11453)

**<font color=#1a73e8>作者：</font>** Ethan David James Park, Dalal Alharthi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Practitioners deploying multi-agent large language model (LLM) systems must currently choose between communication topologies such as chain, star, mesh, and richer variants without any pre-inference diagnostic for which topology will amplify drift, converge to consensus, or remain robust under perturbation. Existing evaluation answers these questions only post hoc and only for the task measured. We introduce a structural diagnostic for multi-agent LLM communication graphs based on the successor representation $M = (I - \gamma P)^{-1}$ of the row-stochastic communication operator, and we connect three of its spectral quantities, the spectral radius $\rho(M)$, the spectral gap $\Delta(M)$, and the condition number $\kappa(M)$, to three distinct failure modes. We derive closed-form spectra for the chain, star, and mesh under row-stochastic normalization, and validate the predictions on a 12-step structured state-tracking task with Qwen2.5-7B-Instruct over 100 independent trials. The condition number is a perfect rank-order predictor of empirical perturbation robustness ($r_s = 1.0$); the spectral gap partially predicts consensus dynamics ($r_s = 0.5$); and the spectral radius is perfectly \emph{inverted} with respect to cumulative error ($r_s = -1.0$). We trace this inversion to a regime in which linear spectra are blind to non-contracting bias drift, and we propose an affine-noise extension of the predictive map that recovers the empirical ordering. We read this as a first step toward representational, drift-aware structural diagnostics for multi-agent LLM systems, sitting alongside classical spectral and consensus theory.

---


### 65. [Adaptive Teacher Exposure for Self-Distillation in LLM Reasoning](https://arxiv.org/abs/2605.11458)

**<font color=#1a73e8>作者：</font>** Zihao Han, Tiangang Zhang, Huaibin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation has become a strong recipe for LLM reasoning, where a privileged teacher supervises the student's own rollouts while conditioning on the reference solution. A design choice shared by nearly all such methods, however, has gone unquestioned: the teacher always sees the full reference reasoning. We argue that this default itself is part of the problem and identify a teacher-side exposure mismatch: when the teacher conditions on reasoning far beyond the student's current competence, the resulting token targets become too strong to absorb. A controlled fixed-exposure sweep makes this concrete on two fronts: 1) full exposure is not reliably the best choice, and 2) student-teacher mismatch grows monotonically as the teacher sees more privileged reasoning. This motivates treating teacher exposure not as a fixed hyperparameter but as a learnable training-time control variable. We therefore propose Adaptive Teacher Exposure for Self-Distillation (ATESD). ATESD models the reveal ratio with a lightweight Beta-policy controller conditioned on compact training-state statistics, and uses one sampled exposure for a short hold window of student updates. To make this exposure controller learnable, we optimize it with a discounted learning-progress reward that scores each held decision by its effect on the student's future improvement rather than its immediate loss change, addressing the delayed credit assignment induced by on-policy distillation. Experiments on AIME 24, AIME 25, and HMMT 25 across Qwen3-{1.7B, 4B, 8B} show that ATESD consistently outperforms competitive self-distillation and RL baselines, improving over OPSD by +0.95, +2.05, and +2.33 Average@12 points respectively, and establishing adaptive teacher exposure as an effective new axis for reasoning self-distillation.

---


### 66. [Breaking $\textit{Winner-Takes-All}$: Cooperative Policy Optimization Improves Diverse LLM Reasoning](https://arxiv.org/abs/2605.11461)

**<font color=#1a73e8>作者：</font>** Haoxuan Chen, Tianming Liang, Wei-Shi Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiers (RLVR) has become a central paradigm for improving LLM reasoning, yet popular group-based optimization algorithms like GRPO often suffer from exploration collapse, where the models prematurely converge on a narrow set of high-scoring patterns, lacking the ability to explore new solutions. Recent efforts attempt to alleviate this by adding entropy regularization or diversity bonus. However, these approaches do not change the \textit{winner-takes-all} nature, where rollouts still compete for individual advantage rather than cooperating for maximizing global diversity. In this work, we propose Group Cooperative Policy Optimization (GCPO), which shifts the training paradigm from rollout competition to team cooperation. Specifically, GCPO replaces independent rollout scoring with team-level credit assignment: a rollout is rewarded by how much it contributes to the team's valid solution coverage, rather than its individual accuracy. This coverage is described as a determinant volume over reward-weighted semantic embeddings, where only correct and non-redundant rollouts contribute to this volume. During advantage estimation, GCPO redistributes the collective team reward to each single rollout according to its average marginal contribution to the team. This cooperative training paradigm routes optimization toward non-redundant correct reasoning paths. Experiments across multiple reasoning benchmarks demonstrate that GCPO significantly improves both reasoning accuracy and solution diversity over existing approaches. Code will be released at $\href{this https URL}{this}$.

---


### 67. [Drop the Act: Probe-Filtered RL for Faithful Chain-of-Thought Reasoning](https://arxiv.org/abs/2605.11467)

**<font color=#1a73e8>作者：</font>** Swapnil Parekh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models post-hoc rationalize answers they have already committed to internally, producing chains of *reasoning theater*: deliberative-looking steps that contribute nothing to correctness. This wastes inference tokens, pollutes interpretability, and obscures what the model actually computed. We introduce **ProFIL** (**Pro**be-**Fil**tered Reinforcement Learning) to *reduce theater, increase chain-of-thought faithfulness, and shrink chain length* in a single, drop-in extension to Group Relative Policy Optimization (GRPO). A multi-head attention probe is trained *once* on the *frozen* base model to detect post-commitment steps from internal activations alone; during GRPO, rollouts whose probe score exceeds a threshold have their advantage zeroed. *Our central finding is that a probe trained on a frozen base, with verifier-derived labels and no human annotation, provides a stable signal that suppresses theater while resisting the RL-obfuscation failure mode predicted by prior work.* Across four reasoning domains (GSM8K, LiveCodeBench, ToolUse, MMLU-Redux) and two model architectures (Llama-8B, Qwen-7B), ProFIL reduces post-commitment theater by **11--100%**, raises faithful-fraction (e.g., +24pp on LiveCodeBench under an independent Claude 3.7 Sonnet judge), and shortens chains by 4--19%, all while preserving or improving task accuracy. ProFIL also beats a matched length-penalty GRPO baseline, isolating the gain as semantic commitment-detection rather than chain compression. Probe weights, training configurations, and rollouts are released across all four domains.

---


### 68. [CAMPA: Efficient and Aligned Multimodal Graph Learning via Decoupled Propagation and Aggregation](https://arxiv.org/abs/2605.11468)

**<font color=#1a73e8>作者：</font>** Daohan Su, Hao Liu, Xunkai Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Graph Neural Networks (MGNNs) have shown strong potential for learning from multimodal attributed graphs, yet most existing approaches rely on tightly coupled architectures that suffer from prohibitive computational overhead. In this paper, we present a systematic empirical analysis showing that decoupled MGNNs are substantially more efficient and scalable for large-scale graph learning. However, we identify a critical bottleneck in existing decoupled pipelines, namely modal conflict, which arises in both the propagation and aggregation stages. Specifically, independent multi-hop diffusion causes cross-modal semantic divergence during propagation, while naive fusion fails to align multi-hop feature trajectories during aggregation, jointly limiting effective representation learning. To address this challenge, we propose CAMPA, a Cross-modal Aligned Multimodal Propagation & Aggregation framework for decoupled multimodal graph learning. Concretely, CAMPA introduces a two-stage alignment mechanism: (1) cross-modal aligned propagation, which injects cross-modal similarity priors into message passing to preserve semantic consistency without additional parameter overhead; (2) trajectory aligned aggregation, which leverages trajectory-level self-attention and cross-attention to capture and align long-range dependencies across modalities and hops. Extensive experiments on diverse benchmark datasets and tasks demonstrate that CAMPA consistently outperforms strong coupled and decoupled baselines while preserving the efficiency advantages of the decoupled paradigm.

---


### 69. [LDDR: Linear-DPP-Based Dynamic-Resolution Frame Sampling for Video MLLMs](https://arxiv.org/abs/2605.11477)

**<font color=#1a73e8>作者：</font>** Jingfeng Chen, Jiawen Qian, Wendi Deng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding in multimodal large language models requires selecting informative frames from long, redundant videos under limited visual-token budgets. Existing methods often rely on uniform sampling, point-wise relevance scoring, chunk-wise selection, or agentic exploration, which either miss global dependencies or introduce substantial overhead. We propose LDDR (Linear DPP-Based Dynamic Resolution), a training-free, plug-and-play, and budget-aware video frame sampling framework. LDDR performs query-aware Determinantal Point Process (DPP) frame selection in a task-conditioned feature space, achieving a 3x runtime speedup over standard DPP baselines. It further introduces a Group DPP importance metric to guide frame retention and dynamic resolution allocation, assigning more tokens to informative, non-redundant frames while downscaling or pruning less useful ones. Across four video benchmarks spanning short-, medium-, and long-range videos, LDDR consistently outperforms the next-best baselines, achieving gains of 2.5 points under budget-constrained settings and 1.6 points in high-budget scenarios. These improvements are consistently observed across multiple MLLM backbones, including both open- and closed-source models. Qualitative analysis confirms that relevant frames are selected and allocated a higher budget, facilitating improved video understanding.

---


### 70. [Efficient Adjoint Matching for Fine-tuning Diffusion Models](https://arxiv.org/abs/2605.11480)

**<font color=#1a73e8>作者：</font>** Jeongwoo Shin, Dongsoo Shin, Joonseok Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward fine-tuning has become a common approach for aligning pretrained diffusion and flow models with human preferences in text-to-image generation. Among reward-gradient-based methods, Adjoint Matching (AM) provides a principled formulation by casting reward fine-tuning as a stochastic optimal control (SOC) problem. However, AM inevitably requires a substantial computational cost: it requires (i) stochastic simulation of full generative trajectories under memoryless dynamics, resulting in a large number of function evaluations, and (ii) backward ODE simulation of the adjoint state along each sampled trajectory. In this work, we observe that both bottlenecks are closely tied to the \textit{non-trivial base drift} inherited from the pretrained model. Motivated by this observation, we propose \textbf{Efficient Adjoint Matching (EAM)}, which substantially improves training efficiency by reformulating the SOC problem with a \textit{linear base drift} and a correspondingly modified \textit{terminal cost}. This reformulation removes both sources of inefficiency; it enables training-time sampling with a few-step deterministic ODE solver and yields a closed-form adjoint solution that eliminates backward adjoint simulation. On standard text-to-image reward fine-tuning benchmarks, EAM converges up to 4x faster than AM and matches or surpasses it across various metrics including PickScore, ImageReward, HPSv2.1, CLIPScore and Aesthetics.

---


### 71. [StoicLLM: Preference Optimization for Philosophical Alignment in Small Language Models](https://arxiv.org/abs/2605.11483)

**<font color=#1a73e8>作者：</font>** Ishmam Khan, Sindhuja Thogarrati, Shuo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language models excel at factual adaptation, their ability to internalize nuanced philosophical frameworks under severe data constraints remains underexplored. We investigate this by specializing small LLMs on micro-datasets of foundational Stoic texts using preference optimization (ORPO, AlphaPO). Evaluated via a multi-model critic bank, our results show that just 300 high-fidelity examples can induce strong alignment with inward-facing Stoic virtues, closely approaching few-shot prompting while freeing the context window. Critically, however, all models, including few-shot baselines, exhibit a persistent failure on Stoicism's outward-facing cosmopolitan duties, pointing to a representational limitation of small models that micro-dataset adaptation alone cannot overcome.

---


### 72. [CTFusion: A CTF-based Benchmark for LLM Agent Evaluation](https://arxiv.org/abs/2605.11504)

**<font color=#1a73e8>作者：</font>** Dongjun Lee, Ga-eun Bae, Insu Yun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have enabled agentic systems for complex, multi-step tasks; cybersecurity is emerging as a prominent application. To evaluate such agents, researchers widely adopt Capture The Flag (CTF) benchmarks. However, current CTF benchmarks reuse existing challenges, which exposes them to data contamination and potential cheating. Notably, we confirmed these issues in practice by integrating web search tools into an existing agent. To address these limitations, we present CTFusion, a streaming evaluation framework built on Live CTFs. To achieve this, CTFusion preserves per-agent independence under a single team account and reduces competition impact by forwarding only the first correct flag per challenge. Moreover, we implement CTFusion as a Model Context Protocol (MCP) server on the widely used CTFd platform, which offers broad applicability to diverse CTF events and agent types. Through experiments with three LLMs, two agents, and five Live CTFs, we demonstrate that existing CTF benchmarks can be unreliable in assessing LLM-based agents, while CTFusion can serve as a robust solution for evaluating cybersecurity agents. We release CTFusion as open source to foster future research in this area.

---


### 73. [Hierarchical LLM-Driven Control for HAPS-Assisted UAV Networks: Joint Optimization of Flight and Connectivity](https://arxiv.org/abs/2605.11509)

**<font color=#1a73e8>作者：</font>** Zijiang Yan, Hao Zhou, Wael Jaafar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Uncrewed aerial vehicles (UAVs) are increasingly deployed in complex networked environments, yet the joint optimization of multi-UAV motion control and connectivity remains a fundamental challenge. In this paper, we study a multi-UAV system operating in an integrated terrestrial and non-terrestrial network (ITNTN) comprising terrestrial base stations and high-altitude platform stations (HAPS). We consider a three-dimensional (3D) aerial highway scenario where UAVs must adapt their motion to ensure collision avoidance, efficient traffic flow, and reliable communication under dynamic and partially observable conditions. We first model the problem as a hierarchical multi-objective partially observable Markov decision process (H-MO-POMDP), capturing the coupling between control and communication objectives. Based on this formulation, we propose a large language model (LLM)-driven hierarchical multi-rate control framework. At the global level, an LLM-based controller on the HAPS performs long-term planning for load balancing and handover decisions. At the local level, each UAV employs a hybrid controller that integrates a slow-timescale LLM for high-level spatial reasoning with a reinforcement learning agent for faster UAV-to-infrastructure (U2I) communication and motion control. We further develop a high-fidelity 3D simulation platform by integrating the gym-pybullet-drones environment with 3GPP-compliant RF/THz channel models. Numerical results demonstrate that the proposed framework significantly outperforms state-of-the-art baselines, achieving a 14% increase in transportation efficiency and a 25% improvement in telecommunication throughput. Additionally, it achieves a 23% reduction in physical collision rates, demonstrating strong handover stability and zero-shot generalization in dynamic scenarios.

---


### 74. [A Study on Hidden Layer Distillation for Large Language Model Pre-Training](https://arxiv.org/abs/2605.11513)

**<font color=#1a73e8>作者：</font>** Maxime Guigon, Lucas Dixon, Michaël E. Sander  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge Distillation (KD) is a critical tool for training Large Language Models (LLMs), yet the majority of research focuses on approaches that rely solely on output logits, neglecting semantic information in the teacher's intermediate representations. While Hidden Layer Distillation (HLD) showed potential for encoder architectures, its application to decoder-only pre-training at scale remains largely unexplored. Through compute-controlled experiments, we benchmark HLD against logit-based KD and self-supervised baselines with Gemma3 3.4B as teacher and 123M and 735M students trained on up to 168B tokens from the C4 dataset. Our experiments show that HLD does not consistently outperform standard KD on downstream evaluation tasks. Nevertheless, we show that HLD can yield a systematic perplexity gain over KD across all shared-hyperparameter configurations, suggesting that a latent signal can be extracted, but a breakthrough may be needed for it to play a more significant role in LLM pre-training.

---


### 75. [AutoLLMResearch: Training Research Agents for Automating LLM Experiment Configuration -- Learning from Cheap, Optimizing Expensive](https://arxiv.org/abs/2605.11518)

**<font color=#1a73e8>作者：</font>** Taicheng Guo, Nitesh V. Chawla, Olaf Wiest 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effectively configuring scalable large language model (LLM) experiments, spanning architecture design, hyperparameter tuning, and beyond, is crucial for advancing LLM research, as poor configuration choices can waste substantial computational resources and prevent models from realizing their full potential. Prior automated methods are designed for low-cost settings where repeated trial and error is feasible, but scalable LLM experiments are too expensive for such extensive iteration. To our knowledge, no work has addressed the automation of high-cost LLM experiment configurations, leaving this problem labor-intensive and dependent on expert intuition. Motivated by this gap, we propose AutoLLMResearch, an agentic framework that mimics how human researchers learn generalizable principles from low-fidelity experiments and extrapolate to efficiently identify promising configurations in expensive LLM settings. The core challenge is how to enable an agent to learn, through interaction with a multi-fidelity experimental environment that captures the structure of the LLM configuration landscape. To achieve this, we propose a systematic framework with two key components: 1) LLMConfig-Gym, a multi-fidelity environment encompassing four critical LLM experiment tasks, supported by over one million GPU hours of verifiable experiment outcomes; 2) A structured training pipeline that formulates configuration research as a long-horizon Markov Decision Process and accordingly incentivizes cross-fidelity extrapolation reasoning. Extensive evaluation against diverse strong baselines on held-out experiments demonstrates the effectiveness, generalization, and interpretability of our framework, supporting its potential as a practical and general solution for scalable real-world LLM experiment automation.

---


### 76. [Read, Grep, and Synthesize: Diagnosing Cross-Domain Seed Exposure for LLM Research Ideation](https://arxiv.org/abs/2605.11532)

**<font color=#1a73e8>作者：</font>** Yunju Choi, Min Song  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The discovery of novel methodologies for emerging problems is a continuing cycle in ML, often driven by the migration of techniques across domains. Building on this observation, we ask whether current LLM ideation systems benefit from targeted cross-domain retrieval or simply from exposure to diverse mechanisms. We study this question through PaperGym, a three-stage pipeline: (1) tool-augmented seed extraction via read, grep, and bash over an isolated paper environment, (2) cross-domain seed retrieval via paraphrasing across seven ML domains, and (3) method synthesis from retrieved seeds, each scored by rubric-based judges. Tool-augmented extraction improves specificity, and paraphrase-based retrieval broadens domain coverage. In synthesis, cross-domain retrieval receives more pairwise novelty wins than no-retrieval and same-domain baselines, but shows no significant difference from a random diverse-seed control. These findings suggest LLM ideation systems benefit from diverse seed exposure, but do not yet reliably exploit the semantic reason particular seeds were retrieved. We release the seed library, rubric prompts, and run scripts at this https URL

---


### 77. [Checkup2Action: A Multimodal Clinical Check-up Report Dataset for Patient-Oriented Action Card Generation](https://arxiv.org/abs/2605.11533)

**<font color=#1a73e8>作者：</font>** Sike Xiang, Shuang Chen, Kevin Qinghong Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical check-up reports are multimodal documents that combine page layouts, tables, numerical biomarkers, abnormality flags, imaging findings, and domain-specific terminology. Such heterogeneous evidence is difficult for laypersons to interpret and translate into concrete follow-up actions. Although large language models show promise in medical summarisation and triage support, their ability to generate safe, prioritised, and patient-oriented actions from multimodal check-up reports remains under-benchmarked. We present \textbf{Checkup2Action}, a multimodal clinical check-up report dataset and benchmark for structured \textit{Action Card} generation. Each card describes one clinically relevant issue and specifies its priority, recommended department, follow-up time window, patient-facing explanation, and questions for clinicians, while avoiding diagnostic or treatment-prescriptive claims. The dataset contains 2,000 de-identified real-world check-up reports covering demographic information, physical examinations, laboratory tests, cardiovascular assessments, imaging-related evidence, and physician summaries. We formulate checkup-to-action generation as a constrained structured generation task and introduce an evaluation protocol covering issue coverage and precision, priority consistency, department and time recommendation accuracy, action complexity, usefulness, readability, and safety compliance. Experiments with general-purpose and medical large language models reveal clear trade-offs between issue coverage, action correctness, conciseness, and safety alignment. Checkup2Action provides a new multimodal benchmark for evaluating patient-oriented reasoning over clinical check-up reports.

---


### 78. [Fast MoE Inference via Predictive Prefetching and Expert Replication](https://arxiv.org/abs/2605.11537)

**<font color=#1a73e8>作者：</font>** Ankit Jyothish, Ali Jannesari, Aishwarya Sarkar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Mixture of Experts (MoE) architecture has become a fundamental building block in state-of-the-art large language models (LLMs), improving domain-specific expertise in LLMs and scaling model capacity without proportionally increasing their computational overhead. However, MoE inference often suffers from suboptimal GPU utilization, load imbalance, and elevated latency arising from multiple tokens waiting on the same experts for their computation which arises from sparsity of expert activation. To address these challenges, we propose a dynamic expert replication strategy that predicts which experts are likely to be overloaded and replicates them for upcoming batches of tokens. The replicated experts process batch tokens concurrently across layers, which leads to improved parallelism, shorter GPU idle time, and significantly faster inference. Experimental evaluations conducted on large-scale MoE models, including Switch-base-128 and Switch-base-256, demonstrate that our method achieves near-complete GPU utilization (approx 100%), leading to upto 3x improvement in inference speed while preserving approximately 90-95% of the performance of baseline architectures

---


### 79. [UNIPO: Unified Interactive Visual Explanation for RL Fine-Tuning Policy Optimization](https://arxiv.org/abs/2605.11549)

**<font color=#1a73e8>作者：</font>** Aeree Cho, Alexander D. Greenhalgh, Jonathan Bodea 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has emerged as a dominant technique for fine-tuning the behavior of large language models, with policy optimization (PO) algorithms such as GRPO, DAPO, and Dr. GRPO emerging in rapid succession to advance state-of-the-art reasoning and alignment performance. However, the modular differences between these algorithms, including targeted improvements to clipping, advantage estimation, and reward aggregation, are introduced across separate papers with inconsistent notation, making them difficult to compare and intimidating to the non-expert community. We present UNIPO, the first interactive visualization tool that exposes the token-level training dynamics of RL fine-tuning algorithms through a unified design. UNIPO connects three complementary views, a high-level training overview, a step-level prompt and response inspector, and a side-by-side algorithm comparison, allowing learners to observe how individual design decisions propagate through training. Through two usage scenarios, we demonstrate how UNIPO supports both classroom instruction for non-experts and algorithm selection for AI practitioners. Our tool is open-source and publicly available at this https URL.

---


### 80. [When Looking Is Not Enough: Visual Attention Structure Reveals Hallucination in MLLMs](https://arxiv.org/abs/2605.11559)

**<font color=#1a73e8>作者：</font>** Fanpu Cao, Xin Zou, Xuming Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have become a key interface for visual reasoning and grounded question answering, yet they remain vulnerable to visual hallucinations, where generated responses contradict image content or mention nonexistent objects. A central challenge is that hallucination is not always caused by a simple lack of visual attention: the model may still assign substantial attention mass to image tokens while internally drifting toward an incorrect answer. In this paper, we show that the high-frequency structure of visual attention, measured by layer-wise Laplacian energy, reveals both the layer where hallucinated preferences emerge and the layer where the ground-truth answer transiently recovers. Building on this finding, we propose LaSCD (Laplacian-Spectral Contrastive Decoding), a training-free decoding strategy that selects informative layers via Laplacian energy and remaps next-token logits in closed form. Experiments on hallucination and general multimodal benchmarks show that LaSCD consistently reduces hallucination while preserving general capabilities, highlighting its potential as a faithful decoding paradigm. The code is available at this https URL.

---


### 81. [Three Regimes of Context-Parametric Conflict: A Predictive Framework and Empirical Validation](https://arxiv.org/abs/2605.11574)

**<font color=#1a73e8>作者：</font>** Pruthvinath Jeripity Venkata  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The literature on how large language models handle conflict between their training knowledge and a contradicting document presents a persistent empirical contradiction: some studies find models stubbornly retain their trained answers, ignoring provided documents nearly half the time, while others find models readily defer to the document, following context approximately 96% of the time. We argue these contradictions dissolve once one recognises that prior experiments have studied three qualitatively distinct processing situations without distinguishing them. We propose a three-regime framework: Regime 1 (single-source updating, dominant predictor: evidence coherence), Regime 2 (competitive integration, dominant predictor: parametric certainty), and Regime 3 (task-appropriate selection, dominant predictor: task knowledge requirement). We formalise a distinction between parametric strength (exposure frequency) and parametric uniqueness (encoding consistency), showing empirically that these are orthogonal dimensions (r = -0.002, p = .97) with strength as the operative predictor in stable factual domains. We validate the framework across Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Flash, Llama 4 Maverick, and DeepSeek V3 using 9,970 API calls in three experimental phases. GEE logistic regression confirms the predicted Regime 2 certainty gradient for all five models (beta = -0.38 to -0.50, all p <= .013, BH-FDR corrected). A Regime 3 ablation shows task framing alone flips context-following from near-100% (contextual knowledge condition) to 6-71% (parametric knowledge condition), with all five models significant (p < .001). The certainty gradient is robust to multinomial outcome modeling, sensitivity analyses for hedging responses, and FDR correction.

---


### 82. [Ada-MK: Adaptive MegaKernel Optimization via Automated DAG-based Search for LLM Inference](https://arxiv.org/abs/2605.11581)

**<font color=#1a73e8>作者：</font>** Wenxin Dong, Mingqing Hu, Guanghui Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When large language models (LLMs) serve real-time inference in commercial online advertising systems, end-to-end latency must be strictly bounded to the millisecond range. Yet every token generated during the decode phase triggers thousands of kernel launches, and kernel launch overhead alone can account for 14.6% of end-to-end inference time. MegaKernel eliminates launch overhead and inter-operator HBM round-trips by fusing multiple operators into a single persistent kernel. However, existing MegaKernel implementations face a fundamental tension between portability and efficiency on resource-constrained GPUs such as NVIDIA Ada: hand-tuned solutions are tightly coupled to specific architectures and lack portability, while auto-compiled approaches introduce runtime dynamic scheduling whose branch penalties are unacceptable in latency-critical settings. We observe that under a fixed deployment configuration, the optimal execution path of a MegaKernel is uniquely determined, and runtime dynamic decision-making can be entirely hoisted to compile time. Building on this insight, we propose Ada-MK: (1) a three-dimensional shared-memory constraint model combined with K-dimension splitting that reduces peak shared memory usage by 50%; (2) MLIR-based fine-grained DAG offline search that solidifies the optimal execution path, completely eliminating runtime branching; and (3) a heterogeneous hybrid inference engine that embeds MegaKernel as a plugin into TensorRT-LLM, combining high-throughput Prefill with low-latency Decode. On an NVIDIA L20, Ada-MK improves single-batch throughput by up to 23.6% over vanilla TensorRT-LLM and 50.2% over vLLM, achieving positive gains across all tested scenarios--the first industrial deployment of MegaKernel in a commercial online advertising system.

---


### 83. [Efficient LLM-based Advertising via Model Compression and Parallel Verification](https://arxiv.org/abs/2605.11582)

**<font color=#1a73e8>作者：</font>** Wenxin Dong, Chang Gao, Guanghui Yu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown remarkable potential in advertising scenarios such as ad creative generation and targeted advertising. However, deploying LLMs in real-time advertising systems poses significant challenges due to their high inference latency and computational cost. In this paper, we propose an Efficient Generative Targeting framework that integrates adaptive group quantization, layer-adaptive hierarchical sparsification, and prefix-tree parallel verification to accelerate LLM inference while preserving generation quality. Extensive experiments on two real-world advertising scenarios demonstrate that our framework achieves significant speedup with acceptable quality degradation, making it operationally viable for practical deployments.

---


### 84. [Learning Weakly Communicating Average-Reward CMDPs: Strong Duality and Improved Regret](https://arxiv.org/abs/2605.11586)

**<font color=#1a73e8>作者：</font>** Kihyun Yu, Beomhan Baek, Dabeen Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study infinite-horizon average-reward constrained Markov decision processes (CMDPs) under the weakly communicating assumption. Our contributions are twofold. First, we establish strong duality for weakly communicating average-reward CMDPs over stationary policies with finite state and action spaces. Despite the absence of a linear programming formulation and the resulting nonconvexity under the weakly communicating setting, we show that strong duality still holds by carefully exploiting the geometric structure of the occupation measure set. Second, building on this result, we propose a primal--dual clipped value iteration algorithm for learning weakly communicating average-reward linear CMDPs. Our algorithm achieves regret and constraint violation bounds of $\widetilde{\mathcal{O}}(T^{2/3})$, improving upon the best known bounds, where $T$ denotes the number of interactions. Our approach extends clipped value iteration to the constrained setting and adapts it to a finite-horizon approximation, which stabilizes the dual variable and is crucial for achieving improved regret bounds. To analyze this, we develop a novel approach based on strong duality that enables the decomposition of the composite Lagrangian regret into separate bounds on regret and constraint violation.

---


### 85. [Logit-Attention Divergence: Mitigating Position Bias in Multi-Image Retrieval via Attention-Guided Calibration](https://arxiv.org/abs/2605.11591)

**<font color=#1a73e8>作者：</font>** Mingtao Xian, Yifeng Yang, Qinying Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have shown strong performance in multi-image cross-modal retrieval, yet suffer from severe position bias, where predictions are dominated by input order rather than semantic relevance. Through empirical analysis, we identify a phenomenon termed Logit-Attention Divergence, in which output logits are heavily biased while internal attention maps remain well-aligned with relevant visual evidence. This observation reveals a fundamental limitation of existing logit-level calibration methods such as PriDe. Based on this insight, we propose a training-free, attention-guided debiasing framework that leverages intrinsic attention signals for instance-level correction at inference time, requiring only a minimal calibration set with negligible computational overhead. Experiments on MS-COCO-based benchmarks show that our method substantially improves permutation invariance and achieves state-of-the-art performance, enhancing accuracy by over 40\% compared to baselines. Code is available at this https URL.

---


### 86. [HorizonDrive: Self-Corrective Autoregressive World Model for Long-horizon Driving Simulation](https://arxiv.org/abs/2605.11596)

**<font color=#1a73e8>作者：</font>** Conglang Zhang, Yifan Zhan, Qingjie Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Closed-loop driving simulation requires real-time interaction beyond short offline clips, pushing current driving world models toward autoregressive (AR) rollout. Existing AR distillation approaches typically rely on frame sinks or student-side degradation training. The former transfers poorly to driving due to fast ego-motion and rapid scene changes, while the latter remains bounded by the teacher's single-pass output length and thus provides only a limited supervision horizon. A natural question is: can the teacher itself be extended via AR rollout to provide unbounded-horizon supervision at bounded memory cost? The key difficulty is that a standard teacher drifts under its own predictions, contaminating the supervision it provides. Our key insight is to make the teacher rollout-capable, ensuring reliable supervision from its own AR rollouts. This is instantiated as HorizonDrive, an anti-drifting training-and-distillation framework for AR driving simulation. First, scheduled rollout recovery (SRR) trains the base model to reconstruct ground-truth future clips from prediction-corrupted histories, yielding a teacher that remains stable across long AR rollouts. Second, the rollout-capable teacher is extended via AR rollout, providing long-horizon distribution-matching supervision under bounded memory, while a short-window student aligns to it with teacher rollout DMD (TRD) for efficient real-time deployment. HorizonDrive natively supports minute-scale AR rollout under bounded memory; on nuScenes, HorizonDrive reduces FID by 52% and FVD by 37%, and lowers ARE and DTW by 21% and 9% relative to the strongest long-horizon streaming baselines, while remaining competitive with single-pass driving video generators.

---


### 87. [Targeted Tests for LLM Reasoning: An Audit-Constrained Protocol](https://arxiv.org/abs/2605.11599)

**<font color=#1a73e8>作者：</font>** Hongmin Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fixed reasoning benchmarks evaluate canonical prompts, but semantically valid changes in presentation can still change model behavior. Studies of prompt variation can reveal such failures, but without audit they can mix genuine model errors with invalid perturbations, extraction artifacts, and unmatched search procedures. We propose an audit-constrained protocol for targeted reasoning evaluation. Prompt variants are generated from a finite component grammar, rendered deterministically, evaluated under a fixed query budget, and counted as model errors only after semantic and extraction audit. Within this protocol we instantiate Component-Adaptive Prompt Sampling (CAPS), a score-based sampler over prompt components, and compare it with equal-budget uniform component sampling under the same task bank, renderer, model interface, decoding settings, and audit procedure. Across three audited slices, the protocol identifies confirmed model-error prompt keys while excluding formatting and extraction artifacts, but matched comparisons do not show that CAPS improves audited yield or unique prompt-key discovery over uniform sampling. The contribution is methodological: targeted prompt variation can be studied under a reconstructable, reviewable, budget-matched protocol, and proxy-guided policies should be judged by audited yield rather than raw mismatch counts or selected examples alone.

---


### 88. [GAR: Carbon-Aware Routing for LLM Inference via Constrained Optimization](https://arxiv.org/abs/2605.11603)

**<font color=#1a73e8>作者：</font>** Disha Sheshanarayana, Rajat Subhra Pal, Manjira Sinha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing deployment of large language models (LLMs) makes per-request routing essential for balancing response quality and computational cost across heterogeneous model pools. Current routing methods rarely consider sustainable energy use and CO2 emissions as optimization objectives, despite grid carbon intensity varying by time and region, and models differing significantly in energy consumption. To address this gap, we introduce Green-Aware Routing (GAR), a constrained multi-objective optimization framework that minimizes per-request CO2 emissions subject to explicit accuracy floors and p95-latency service-level objectives (SLOs). GAR employs adaptive constraint optimization through per-dataset floor tuning and incorporates lightweight estimators for correctness, tail latency, and carbon emissions, enabling real-time routing decisions without additional inference passes. We present GAR-PD, a practical online primal-dual routing algorithm for rolling carbon budgets, alongside heuristic variants that achieve high feasibility coverage while limiting accuracy degradation. Comprehensive experiments across standard NLP benchmarks with heterogeneous LLM pools (7B-70B) demonstrate that GAR achieves substantial carbon reductions while maintaining competitive accuracy and p95 latency guarantees, providing a practical, theoretically grounded approach to sustainable LLM inference.

---


### 89. [Keep What Audio Cannot Say: Context-Preserving Token Pruning for Omni-LLMs](https://arxiv.org/abs/2605.11605)

**<font color=#1a73e8>作者：</font>** Chaeyoung Jung, Kyeongha Rho, Joon Son Chung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnimodal Large Language Models (Omni-LLMs) incur substantial computational overhead due to the large number of multimodal input tokens they process, making token reduction essential for real-world deployment. Existing Omni-LLM pruning methods typically reduce this cost by selecting tokens that are important for the current query or strongly aligned with cross-modal cues. However, such strategies can discard evidence that falls outside these criteria, even when needed for different questions or for understanding context beyond aligned audio-visual cues. To address this limitation, we reframe Omni-LLM token reduction as preserving broad audio-visual context while removing cross-modal redundancy. We propose ContextGuard, an inference-time token pruning framework built on this principle. ContextGuard predicts coarse visual semantics from audio and prunes video tokens whose coarse semantics are likely recoverable from audio, while retaining additional video tokens to preserve localized visual details that audio alone cannot specify. For further compression, our method merges temporally similar video tokens. The framework requires no downstream LLM fine-tuning and uses only an independently trained lightweight predictor. On Qwen2.5-Omni and Video-SALMONN2+ at 3B and 7B scales across six audio-visual benchmarks, ContextGuard outperforms prior inference-time pruning methods while pruning more tokens. Notably, on Qwen2.5-Omni 7B, ContextGuard achieves full-token-level performance on five of six benchmarks while pruning 55% of input tokens.

---


### 90. [CuSearch: Curriculum Rollout Sampling via Search Depth for Agentic RAG](https://arxiv.org/abs/2605.11611)

**<font color=#1a73e8>作者：</font>** Jianghan Shen, Siqi Luo, Xinyu Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a promising paradigm for training agentic retrieval-augmented generation (RAG) systems from outcome-only supervision. Most existing methods optimize policies from uniformly sampled rollouts, implicitly treating all trajectories as equally informative. However, trajectories differ substantially in search depth and are therefore not equally informative: deeper-search trajectories contain more retrieval decision points and provide denser direct supervision for the retrieval sub-policy. Moreover, this heterogeneity grows over training as the within-batch depth distribution shifts toward higher values, yet uniform rollout sampling remains blind to this shift. To address this, we propose CuSearch, a curriculum rollout sampling framework built on Search-Depth Greedy Allocation (SDGA), a batch-level operator that reallocates a fixed update budget toward deeper-search trajectories. SDGA-Auto always targets the deepest available trajectories in the current batch, yielding an implicit training-aligned curriculum as the depth distribution shifts upward. SDGA-Phase explicitly advances the curriculum threshold as deeper trajectories become sufficiently abundant. Experiments across model types and retrieval frameworks show that CuSearch consistently improves performance, achieving up to 11.8 exact-match points over standard GRPO on ZeroSearch. These results establish per-trajectory search depth as a reliable, annotation-free proxy for retrieval supervision density in RLVR-based agentic RAG training. The code is available at this https URL.

---


### 91. [When Emotion Becomes Trigger: Emotion-style dynamic Backdoor Attack Parasitising Large Language Models](https://arxiv.org/abs/2605.11612)

**<font color=#1a73e8>作者：</font>** Ziyu Liu, Tao Li, Tianjie Ni 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Backdoor vulnerabilities widely exist in the fine-tuning of large language models(LLMs). Most backdoor poisoning methods operate mainly at the token level and lack deeper semantic manipulation, which limits stealthiness. In addition, Prior attacks rely on a single fixed trigger to induce harmful outputs. Such static triggers are easy to detect, and clean fine-tuning can weaken the trigger-target association. Through causal validation, we observe that emotion is not directly linked to individual words, but functions as an overall stylistic factor through tone. In the representation space of LLM, emotion can be decoupled from semantics, forming distinct cluster from the original neutral text. Therefore, we consider the emotional factor as the backdoor trigger to propose a pparasitic emotion-style dynamic backdoor attack, Paraesthesia. By mixing samples with the emotional trigger into clean data and then fine-tuning the model, the model is able to generate the predefined attack response when encountering emotional inputs during the inference stage. Paraesthesia includes two the quantification and rewriting of emotional styles. We evaluate the effectiveness of our method on instruction-following generation and classification tasks. The experimental results show that Paraesthesia achieves an attack success rate of around 99\% across both task types and four different models, while maintaining the clean utility of the models.

---


### 92. [OmniThoughtVis: A Scalable Distillation Pipeline for Deployable Multimodal Reasoning Models](https://arxiv.org/abs/2605.11629)

**<font color=#1a73e8>作者：</font>** Yuanhao Yue, Chengyu Wang, Yuanjie Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) have shown strong chain-of-thought (CoT) reasoning ability on vision-language tasks, but their direct deployment in real-world systems is often limited by latency and resource constraints. In practice, smaller MLLMs are preferred for online serving, yet their reasoning performance is bottlenecked by the lack of large-scale, high-quality multimodal CoT supervision. In this paper, we present OmniThoughtVis, a scalable data curation and distillation pipeline for transferring multimodal reasoning capabilities from high-capacity teacher models to smaller, deployment-oriented MLLMs. Starting from a diverse open-source seed pool, our pipeline generates structured CoT traces and performs joint annotation of reasoning difficulty, answer quality, and semantic task tags. To maintain data quality at scale, we combine rule-based filtering, difficulty-aware selection, and tag-based diversity sampling, resulting in a curated corpus of 1.8M samples that supports controllable subset construction for downstream training. We use OmniThoughtVis to distill Qwen3-VL models from 2B to 8B parameters and evaluate them on nine multimodal reasoning benchmarks. The resulting distilled models show consistent gains across model scales, including improvements of up to +16.8 points on MathVerse and +5.6 points on MMMU-Pro for the 4B model. Notably, the distilled 4B model matches or surpasses the undistilled 8B baseline on several tasks, highlighting the practical value of scalable reasoning distillation for deployment-oriented MLLMs.

---


### 93. [Enhancing Multilingual Counterfactual Generation through Alignment-as-Preference Optimization](https://arxiv.org/abs/2605.11632)

**<font color=#1a73e8>作者：</font>** Yilong Wang, Qianli Wang, Bohao Chu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-generated counterfactual explanations (SCEs) are minimally modified inputs (minimality) generated by large language models (LLMs) that flip their own predictions (validity), offering a causally grounded approach to unraveling black-box LLM behavior. Yet extending them beyond English remains challenging: existing methods struggle to produce valid SCEs in non-dominant languages, and a persistent trade-off between validity and minimality undermines explanation quality. We introduce Macro, a preference alignment framework that applies Direct Preference Optimization (DPO) to multilingual SCE generation, using a composite scoring function to construct preference pairs that effectively translate the trade-off into measurable preference signals. Experiments across four LLMs and seven typologically diverse languages show that Macro improves validity by 12.55\% on average over the chain-of-thought baseline without degrading minimality, while avoiding the severe minimality violations of the translation-based baseline. Compared to supervised fine-tuning, Macro achieves superior performance on both metrics, confirming that explicit preference optimization is essential for balancing this trade-off. Further analyses reveal that Macro increases cross-lingual perturbation alignment and mitigates common generation errors. Our results highlight preference optimization as a promising direction for enhancing multilingual model explanations.

---


### 94. [Can LLM Agents Respond to Disasters? Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations](https://arxiv.org/abs/2605.11633)

**<font color=#1a73e8>作者：</font>** Junjue Wang, Weihao Xuan, Heli Qi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Operational disaster response goes beyond damage assessment, requiring responders to integrate multi-sensor signals, reason over road networks, populations and key facilities, plan evacuations, and produce actionable reports. However, prior work largely isolates remote-sensing perception or evaluates generic tool use, leaving the end-to-end workflows of emergency operations underexplored. In this paper, we introduce Disaster Operational Response Agent benchmark (DORA), the first agentic benchmark for end-to-end disaster response: 515 expert-authored tasks across 45 real-world disaster events spanning 10 types, paired with expert-verified, replayable gold trajectories totaling 3,500 tool-call steps. Tasks span five dimensions that cover the operational disaster-response pipeline: disaster perception, spatial relational analysis, rescue and evacuation planning, temporal evolution reasoning, and multi-modal report synthesis. Agents compose calls from a 108-tool MCP library over heterogeneous geospatial data: optical, SAR, and multi-spectral imagery across single-, bi-, and multi-temporal sequences (0.015-10m GSD), complemented by elevation and social vector layers. We comprehensively evaluate 13 frontier LLMs on our benchmark, revealing three persistent challenges: 1) disaster-domain grounding exposes unique failure modes (damage-semantic grounding, sensor-modality mismatch, and disaster-pipeline composition); 2) agents are doubly bottlenecked by tool selection and argument grounding, where gold tool-order hints improve accuracy by only 1.08-4.40%, and alternative scaffolds yield at most a 3.24% gain; 3) compositional fragility scales with trajectory length, the agent-to-gold gap widening from 7% to 56% on long pipelines. DORA establishes a rigorous testbed for operationally reliable disaster-response agents.

---


### 95. [Unlocking UML Class Diagram Understanding in Vision Language Models](https://arxiv.org/abs/2605.11634)

**<font color=#1a73e8>作者：</font>** Artem Naboichenko, René Peinl  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although Vision Language Models (VLMs) have seen tremendous progress across all kinds of use cases, they still fall behind in answering questions regard-ing diagrams compared to photos. Although progress has been made in the area of bar charts, line charts and other diagrams like that there is still few research concerned with other types of diagrams, e.g. in the computer science domain. Our work presents a benchmark for visual question answering based on UML class diagrams which is both challenging and manageable. We further construct a large-scale training dataset with 16.000 image-question-answer triples and show that a LoRA-based finetune easily outperforms Qwen 3.5 27B, which is a recent and well-performing VLM in many other benchmarks.

---


### 96. [Seirênes: Adversarial Self-Play with Evolving Distractions for LLM Reasoning](https://arxiv.org/abs/2605.11636)

**<font color=#1a73e8>作者：</font>** Chi Zhang, Haibo Qiu, Qiming Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Seirênes, a self-play RL framework that transforms contextual interference from a failure mode of LLM reasoning into an internal training signal for co-evolving more resilient reasoners. While RL with verifiable rewards has significantly advanced reasoning capabilities, models can still exhibit fragility when encountering non-idealized contexts: scenarios characterized by superfluous information, tangential instructions, or incidental correlations that differ from the clean distributions typical of standard benchmarks. Seirênes harnesses this vulnerability through a parameter-shared and adversarial self-play loop. Within this framework, a single model is trained to both construct plausible yet distracting contexts that expose its own reasoning blind spots, and solve problems by discerning the essential task from these perturbations to recover the core underlying logic. By pitting these competing objectives against each other, Seirênes compels the model to move beyond superficial pattern matching and anchors its capabilities in robust underlying reasoning. This continuous interaction sustains an informative co-evolutionary curriculum as the model improves. Across seven mathematical reasoning benchmarks and model scales from 4B to 30B, Seirênes achieves average gains of +10.2, +9.1, and +7.2 points. Besides, distracting contexts produced by the 4B Seirênes model reduce the accuracy of top-tier closed-source models (GPT and Gemini) by roughly 4--5 points, revealing Seirênes' general ability to uncover reasoning models' blind spots.

---


### 97. [Hide to See: Reasoning-prefix Masking for Visual-anchored Thinking in VLM Distillation](https://arxiv.org/abs/2605.11651)

**<font color=#1a73e8>作者：</font>** Seonghoon Yu, Dongjun Nam, Byung-Kwan Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent think-answer approaches in VLMs, such as Qwen3-VL-Thinking, boost reasoning performance by leveraging intermediate thinking steps before the final answer, but their high computational cost limits real-world deployment. To distill such capabilities into compact think-answer VLMs, a primary objective is to improve the student's ability to utilize visual evidence throughout its reasoning trace. To this end, we introduce a novel think-answer distillation framework that encourages the student to anchor its thinking on visual information by masking the student's salient reasoning prefixes. To compensate for such masked textual cues, the student is encouraged to rely more on visual evidence as an alternative source of information during distillation. Our masking strategies include: 1) token-wise salient reasoning-prefix masking, which masks high-influence reasoning prefixes selectively for each next-token prediction, and 2) self-paced masking budget scheduling, which gradually increases the masking scale according to distillation difficulty, {measured by discrepancy between teacher--student distributions. In the distillation phase, the student is guided by our salient reasoning-prefix mask, which blocks both future tokens and salient reasoning cues, in place of the standard causal mask used for auto-regressive language modeling. Experimental results show that our approach outperforms recent open-source VLMs, VLM distillation, and self-distillation methods on multimodal reasoning benchmarks, while further analyses confirm enhanced visual utilization along the student thinking process.

---


### 98. [Reviving In-domain Fine-tuning Methods for Source-Free Cross-domain Few-shot Learning](https://arxiv.org/abs/2605.11659)

**<font color=#1a73e8>作者：</font>** Yaze Zhao, Yicong Liu, Yixiong Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-Domain Few-Shot Learning (CDFSL) aims to adapt large-scale pretrained models to specialized target domains with limited samples, yet the few-shot fine-tuning of vision-language models like CLIP remains underexplored. By establishing multiple fine-tuning baselines of CLIP for CDFSL, we find adapter-based methods (e.g., LoRA) consistently outperform prompt-based ones (e.g., MaPLe), contrary to in-domain scenarios. To make those effective in-domain methods competitive again in CDFSL, we analyze this phenomenon and discover LoRA's superiority stems from rectifying the collapsed attention of visual CLS token, enhancing modality alignment and class separation by focusing on text-related visual regions. Further, we find textual EOS token exhibit much better attention to visual samples, and CLIP's standard contrastive loss weakly constrains modality alignment. Based on these insights, we propose Semantic Probe, a plug-and-play attention rectification framework for both adapter- and prompt-based methods. Extensive experiments on four CDFSL benchmarks validate our rationale, achieving state-of-the-art performance and benefiting both fine-tuning paradigms. Codes will be released.

---


### 99. [Human-Grounded Multimodal Benchmark with 900K-Scale Aggregated Student Response Distributions from Japan's National Assessment of Academic Ability](https://arxiv.org/abs/2605.11663)

**<font color=#1a73e8>作者：</font>** Kyosuke Takami, Yuka Tateisi, Satoshi Sekine 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Authentic school examinations provide a high-validity test bed for evaluating multimodal large language models (MLLMs), yet benchmarks grounded in Japanese K-12 assessments remain scarce. We present a multimodal dataset constructed from Japan's National Assessment of Academic Ability, comprising officially released middle-school items in Science, Mathematics, and Japanese Language. Unlike existing benchmarks based on synthetic or curated data, our dataset preserves real exam layouts, diagrams, and Japanese educational text, together with nationwide aggregated student response distributions (N $\approx$ 900{,}000). These features enable direct comparison between human and model performance under a unified evaluation framework. We benchmark recent multimodal LLMs using exact-match accuracy and character-level F1 for open-ended responses, observing substantial variation across subjects and strong sensitivity to visual reasoning demands. Human evaluation and LLM-as-judge analyses further assess the reliability of automatic scoring. Our dataset establishes a reproducible, human-grounded benchmark for multimodal educational reasoning and supports future research on evaluation, feedback generation, and explainable AI in authentic assessment contexts. Our dataset is available at: this https URL

---


### 100. [Evolutionary Task Discovery: Advancing Reasoning Frontiers via Skill Composition and Complexity Scaling](https://arxiv.org/abs/2605.11666)

**<font color=#1a73e8>作者：</font>** Liqin Ye, Yanbin Yin, Michael Galarnyk 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The reasoning frontier of Large Language Models (LLMs) has advanced significantly through modern post-training paradigms (e.g., Reinforcement Learning from Verifiable Rewards (RLVR)). However, the efficacy of these methods remains fundamentally constrained by the diversity and complexity of the training data. One practical solution is data synthesis; yet, prevalent methods relying on unstructured mutation or exploration suffer from homogeneity collapse, failing to systematically expand the reasoning frontier. To overcome this, we propose Evoutionary Task Discovery (EvoTD), a framework that treats data synthesis as a directed search over a dual-axis manifold of Algorithmic Skills and Complexity Attributes. We introduce structured evolutionary operators to navigate this space: a Crossover operator that synthesizes novel skill compositions to enhance diversity, and a Parametric Mutation operator that scales structural constraints (e.g., input size, tree depth) to drive robust generalization. Crucially, we integrate a dynamic Zone of Proximal Development filter, ensuring tasks lie within the learnable region of the model. Empirically, EvoTD delivers substantial reasoning gains that generalize consistently across model architectures, pretraining regimes, and scales, demonstrating that structured evolutionary curricula can effectively support reasoning improvement. We release our code on this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-223](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
