# 🧠 大模型相关研究 | 2026年08月17日

> 本类共 **183** 篇论文：已确认 **168** 篇，待复核 **15** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-183**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-183**

---

### 151. [RAIL: An Automatic Classifier of the Artificial Intelligence Readiness Level](https://arxiv.org/abs/2608.13428)

**<font color=#1a73e8>作者：</font>** Juan Irving Vasquez, Juan Terven, Laura-Ivoone Garay-Jimenez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Assessing the maturity of artificial intelligence technologies is essential for investment decisions, project management, and policy monitoring, yet the available readiness frameworks are heterogeneous and difficult to apply automatically: the adaptation of Technology Readiness Levels to AI lacks AI-specific gating criteria, the Machine Learning Technology Readiness Levels presuppose access to internal process artifacts, and AI/data readiness dimension models employ scales that resist direct comparison. This paper makes two contributions. First, we unify these three frameworks into the Unified AI Readiness Level (AIRL), a nine-level ordinal scale built on an environmental evidence ladder and complemented by dimensional caps (covering specification, data existence, data quality, data legality, expert knowledge, and algorithmic maturity) together with a generality-anchoring rule and explicit assignment disciplines, so that a readiness level becomes decidable from a natural-language description of the work alone. Second, we propose RAIL (Readiness Assessment via Independent LLM-experts), a panel-of-experts classifier that operationalizes the scale: one evidence agent and six independent dimension agents, each a large language model with a narrowly scoped mandate, deliver verdicts that a deterministic minimum rule aggregates and a chief expert reviews under asymmetric authority, confirming or lowering the panel's recommendation but never raising it above the caps. The method was tested in the analysis of several research works showing consistency and avoiding overestimation from monolithic LLM classifiers.

---


### 152. [Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence and Lexical Diversity](https://arxiv.org/abs/2608.13430)

**<font color=#1a73e8>作者：</font>** Irina Proskurina, Mayank Kumar, Oyindolapo O. Komolafe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction-tuned language models achieve strong performance across a range of generation tasks, but have also recently been shown to exhibit verbalized overconfidence. In question answering, verbalized model overconfidence may be associated with the consistency of the generated supporting rationales. In this paper, we study whether corresponding changes in the lexical diversity of generated answer rationales accompany changes in model confidence induced by instruction tuning. We evaluate three matched base and instruction-tuned models across question-answering benchmarks and find that instruction tuning consistently alters answer confidence, despite limited changes in predictive accuracy and decreases in likelihood-based calibration. Secondly, we observe a non-uniform effect of instruction tuning on rationale diversity: cross-rationale diversity consistently decreases, whereas surface-level lexical diversity varies in both direction and magnitude across models and benchmarks. Finally, we find that these differences persist after controlling for answer selection and rationale length, confirming that confidence and rationale diversity capture distinct effects of instruction tuning.

---


### 153. [Edit2TikZ: A Comprehensive and Challenging Benchmark for Scientific Figure Editing with TikZ](https://arxiv.org/abs/2608.13441)

**<font color=#1a73e8>作者：</font>** Zongyun Zhang, Jiacheng Ruan, Xian Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although multimodal large language models (MLLMs) have shown substantial potential in visual understanding and graphic code generation, editing scientific figures through code presents a greater challenge: a model must jointly recover visual structure, ground the requested change, generate compilable code, and preserve all unrelated content. While existing TikZ benchmarks mainly focus on figure reconstruction and generation, few systematically evaluate instruction-guided scientific figure editing with compilable code. We introduce Edit2TikZ, a comprehensive benchmark for scientific figure editing tasks, featuring 1,548 diverse and high-quality samples. Edit2TikZ combines real-world and controlled synthetic edit cases, supports both textual and visual localization request, and contains multi-step editing, each with step-level annotations. We further construct a human-aligned evaluation framework to measure whether a requested edit is completed while irrelevant content is preserved. Utilizing Edit2TikZ, we evaluate 14 mainstream MLLMs and find that current systems remain unreliable: on average, proprietary models achieve a compilation success rate of merely 75% and remain limited in both figure restoration and edit correctness, while compact models below 9B struggle further with instruction following and complete figure generation. Therefore, we build a mixed training set TikZEditMix and adopt reconstruction-then-editing curriculum learning for compact models. On Qwen3.5-4B, this training improves the compilation success rate from 45.35% to 83.40% and yields an average improvement of 18.7 points across our proposed evaluation metrics. The code and data will be released at this https URL.

---


### 154. [UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models](https://arxiv.org/abs/2608.13453)

**<font color=#1a73e8>作者：</font>** Yukun Dai, Mingzhe Dai, Tianshi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have emerged as generalist robotic policies capable of following diverse language instructions and performing a wide range of manipulation tasks. However, their direct control over embodied agents also exposes them to adversarial interference that may cause unsafe physical behaviors. Existing attacks on robotic policies are typically optimized for a single task or instruction, leaving the cross-task vulnerabilities of multitask VLAs largely unexplored. We introduce UniTexture, a cross-task universal adversarial texture attack that uses a single textured 3D object to induce targeted deviations in VLA action predictions across multiple tasks. UniTexture backpropagates gradients from the policy's action outputs to surface texture parameters through a differentiable renderer. It jointly optimizes the shared texture over a distribution of tasks, instructions, states, and viewpoints using a targeted action-space objective, steering predicted actions toward attacker-defined targets without optimizing a separate texture for each task. We evaluate UniTexture on OpenVLA and $\pi_{0.5}$ across diverse manipulation tasks and multiple evaluation settings. UniTexture reduces the mean task success rate from 90.0% under benign conditions to 48.4% under attack, induces target-aligned action shifts, and further exhibits cross-suite and cross-model transfer without re-optimization. Together, these findings reveal shared cross-task vulnerabilities in multitask VLAs that can be systematically exploited through a single adversarial surface texture.

---


### 155. [Before You Say It: Anticipating Verbal Behavior from Longitudinal Everyday Conversations with LLMs](https://arxiv.org/abs/2608.13454)

**<font color=#1a73e8>作者：</font>** Yasith Samaradivakara, Valdemar Danry, Paul Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Knowing someone deeply means not just understanding what they say or do but also how they will likely think, react, and engage across situations. Such predictions could eventually inform systems to anticipate when the individual is about to deviate from their goal, catch regrettable behaviors before they are made, and surface blind spots before they take hold. While many interactive systems model users to enable more personalized interactions, most cannot make such behavioral predictions, as this often requires longitudinal observation and inference of how the individual's behaviors unfold across various everyday situations. In this work, we introduce a novel LLM-based predictive behavioral modeling approach that anticipates a user's likely behavior across everyday conversational situations. We (1) collect a longitudinal dataset of over 1000 hours of naturalistic conversations from 14 participants using a wearable smartwatch; (2) evaluate LLM-based predictions against ground truth behaviors; and (3) use semi-structured interviews to explore participants perceptions of behavioral predictions and their views on possible forms of future behavioral support. Altogether, our findings provide evidence that person-specific verbal behavior can be predicted from longitudinal conversational data. This opens up new possibilities for potential future context-aware, anticipatory, proactive and personalized AI systems.

---


### 156. [MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification](https://arxiv.org/abs/2608.13463)

**<font color=#1a73e8>作者：</font>** Daniel Perkins, John Squires, Janou Milligan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image classification models excel when trained on single task-specific datasets but often struggle to generalize across domains and difficulty levels. We propose ARMDIL, an Adaptive Router for Multi-Domain Image classification with LLMs. ARMDIL is an ensemble that uses a multimodal large language model (MLLM) agent to dynamically route each image to the most suitable vision backbone. Our diverse ensemble employs convolutional neural networks (ResNets), self-supervised representation learners (SSL), and vision-language models (VLMs), each trained on a unified label space constructed from multiple image datasets with differing distributions and characteristics. Empirical evaluations illuminate the distinct capabilities and vulnerabilities of each architecture across disparate visual domains. Crucially, we show that ARMDIL effectively navigates these trade-offs, performing competitively with specialized training-based routers. Furthermore, it drastically improves adaptability by allowing new information to be integrated via simple prompt modifications, while enhancing interpretability through natural language reasoning traces. These advances in cross-dataset image classification pave the way for more reliable general-purpose vision systems such as AI assistants and autonomous robots.

---


### 157. [MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination](https://arxiv.org/abs/2608.13476)

**<font color=#1a73e8>作者：</font>** Saisha Shetty, Satvik Tripathi, Austin Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Multi-Agent Reasoning and Coordination (MARC), an open-source framework that replaces monolithic LLM prompting with deterministic multi-agent orchestration for clinical reasoning. MARC coordinates role-specialized agents for extraction, reasoning, answer generation, and evaluation, with explicit context passing and traceable intermediate outputs, enabling stage-wise failure attribution. We additionally introduce a Decomposer module that generates task-specific agent prompts from a plain-language description, eliminating manual prompt engineering. The framework supports both API-based and local CPU-compatible deployments and is entirely configurable via YAML, without code modifications. MARC is designed to be model-agnostic, interpretable, and accessible to clinical domain experts without programming expertise. The full framework is available at this https URL.

---


### 158. [Synthetic Persona Pretraining: Alignment from Token Zero](https://arxiv.org/abs/2608.13482)

**<font color=#1a73e8>作者：</font>** Julian Minder, Viktor Moskvoretskii, Raghav Singhal 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As language-model-based AI is increasingly deployed in autonomous settings, aligning its goals and values with those of humans becomes critical. Today, alignment, and the assistant identity itself, are typically introduced only after pretraining, once behavioral priors are already established. This can make values a thin overlay, rather than deeply rooted, and facilitate subsequent misalignment. Pursuing a different paradigm, we introduce Synthetic Persona Pretraining (SPP), which installs the desired assistant persona from token zero in pretraining. First, we annotate pretraining documents with value-aligned first-person reflections derived from a normative value constitution. Second, we pretrain via the standard cross-entropy loss on standard pretraining documents as well as their reflections, which installs the desired persona among a multitude of other personas. Finally, we post-train on user-assistant dialogue data, which binds this desired persona to the assistant identity, a process we call persona binding. By pretraining models up to 3B parameters on 500B tokens, we show that SPP improves constitution following and jailbreak robustness, and reduces the misalignment rate in out-of-distribution moral dilemmas, while preserving capabilities. Early intervention matters: compared with alignment from token zero, introducing SPP only at the end of pretraining yields weaker constitution adherence, does not shift value priorities, and leads to less aligned choices in dilemmas. This advantage depends on persona binding and, importantly, increases with pretraining budget. Overall, our results show that shaping values early is critical for alignment and establish pretraining-time persona interventions as an effective approach to do so.

---


### 159. [Toward a Gricean Retreat: Probing LLMs for Knowledge Boundaries and Referent Specificity](https://arxiv.org/abs/2608.13484)

**<font color=#1a73e8>作者：</font>** Dananjay Srinivas, Saksham Khatwani, Maria Pacheco  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When asked about entities outside their knowledge boundary, LLMs routinely fabricate plausible-sounding details rather than backing off to safer, more general claims. We frame this failure through a Gricean lens: a cooperative speaker who is uncertain about a referent retreats up the specificity hierarchy, trading informativeness for truthfulness. We ask whether LLMs have the ingredients to perform this retreat. Using a T-REx-based benchmark that varies entity familiarity and referent specificity, we probe models to answer two questions: (i) do their activations encode whether a referent falls inside the knowledge boundary, and (ii) do they anticipate the specificity of the referent they are about to generate? We find that the answer to both is yes, but the two signals are not reconciled in generation. Models overwhelmingly prefer specific referents even when the entity is unknown to them, and do so even when offered correct generic alternatives. The substrate for a Gricean retreat is present, but the policy that would act on it is not. We position our findings as a first step toward Gricean alignment, training or steering objectives that couple knowledge-boundary awareness to referent-specificity during generation.

---


### 160. [TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval](https://arxiv.org/abs/2608.13495)

**<font color=#1a73e8>作者：</font>** Yi-Chung Chen, Philip Jacobson, Tom Lampo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficiently retrieving relevant clips from large-scale driving logs is essential for data curation, model development, and safety analysis. Structured and rule-based retrieval systems can explicitly target driving events, but typically require expert-defined rules, auxiliary data, and multi-stage perception pipelines. Multimodal embedding models offer a simpler and more efficient alternative by representing each video with a single searchable vector. However, general-purpose models often rely on shortcuts from static scene context and struggle to distinguish motion-centric events, such as turning left versus right or accelerating versus decelerating. In this work, we study how to adapt a general-purpose multimodal embedding model to driving-video retrieval. We first fine-tune Qwen3-VL-Embedding on paired clips and reasoning traces from nuReasoning using an InfoNCE objective. While this stage substantially improves overall retrieval, caption supervision alone remains insufficient for fine-grained motion understanding. We therefore introduce TraVEL (Trajectory-Guided Video Embedding Learning), a motion-aware fine-tuning framework that uses ego-trajectory similarity as a reward within Group Relative Policy Optimization. Trajectories serve only as privileged training supervision; retrieval still operates on single-vector video embeddings without ego poses, expert rules, or auxiliary perception outputs. We further construct a driving-video retrieval benchmark from nuReasoning. Experiments show that TraVEL improves motion-centric retrieval across model scales: relative to SFT, it raises longitudinal and lateral mAP by 9.8 and 4.7 points at 2B, with corresponding gains of 7.2 and 1.5 points at 8B. TraVEL thus combines physically grounded supervision with efficient embedding-based search.

---


### 161. [Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining](https://arxiv.org/abs/2608.13515)

**<font color=#1a73e8>作者：</font>** Yuto Nishida, Hirokazu Kiyomaru, Yusuke Oda 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Measuring training data influence consistently across language model pretraining is challenging. It is difficult to select downstream tasks or validation sets representative of a model's general capabilities, and reliance on task performance at intermediate checkpoints complicates comparisons across training. We propose a measure of training data influence that does not require selecting a downstream task or validation set as the attribution target. Specifically, we define an example's influence by how much its gradient update reduces the squared distance to the final parameters of a given pretraining run, and estimate this quantity from intermediate checkpoints without retraining. Applying the method to 18 configurations from the Pythia and PolyPythia suites, we find systematic temporal changes in influential data. Early in training, literature-related data are more strongly aligned with the trajectory toward the final parameters, whereas STEM data become more strongly aligned in later stages. This qualitative crossover is broadly consistent across model configurations. Our results provide a tractable trajectory-level view of how influential data change throughout pretraining, complementing influence analyses defined with respect to specific downstream tasks or validation sets.

---


### 162. [DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters Using Only Permissible Post-Training Data](https://arxiv.org/abs/2608.13517)

**<font color=#1a73e8>作者：</font>** Peter Schneider-Kamp, Jacob Nielsen, Gianluca Barmina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current large language model development relies on massive, often non-permissible datasets, creating a high barrier for researchers committed to open-source and ethically sourced data. We introduce Mimir v1, a 1-billion-parameter language model based on the Hierarchical Reasoning Model (HRM) architecture, that is trained from scratch and delivers highly competitive performance for English and sets a new state of the art for Danish using only permissible post-training data. Trained on a mixture of 161 datasets, Mimir v1 outperforms the original HRM-Text 1B and competes with larger frontier models like Qwen 3.5 4B and Gemma 4 E2B, tested across 20 benchmarks for English, Math & Code and Danish. The model is available on the Hugging Face Hub: this https URL

---


### 163. [Vero: Can AI Agents Build Formally Verified Software Repositories?](https://arxiv.org/abs/2608.13522)

**<font color=#1a73e8>作者：</font>** Zhe Ye, Hantao Lou, Yuechun Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly used for programming, but do not provide any guarantee on the correctness of generated code. Verified code generation, in which an agent produces both an implementation and a machine-checked proof of its specification, offers a stronger path toward trustworthy AI-generated software. Existing benchmarks in this direction either focus on individual functions or only evaluate proof generation with provided implementations. It is still an open question whether agents can make coherent implementation and proof choices across real multi-module codebases. To bridge this gap, we introduce Vero, the first benchmark to evaluate joint implementation and proof synthesis at the repository level. Vero contains 43 multi-module instances sourced from real-world repositories spanning Python, Dafny, Verus, and Coq, and covering diverse domains from cryptographic protocols to distributed systems. Each instance consists of a multi-module Lean 4 repository with predetermined API interfaces, manually curated formal specifications, and reference implementations, supporting both proof-only and code-and-proof evaluation modes. To improve benchmark reliability, Vero also includes an audit mechanism where agents are allowed to formally prove unsatisfiability of provided specification or incorrectness of reference code, which surfaces and corrects latent code and specification errors during curation. We evaluate frontier coding-agent configurations with Lean toolchain access. The strongest agent fully solves only 27 of 43 instances and closes no specifications on the hardest repositories. Vero provides a concrete testbed for measuring progress toward repository-scale verified software synthesis, where current agents still fall short. We release the benchmark, curation pipeline, and evaluation harness at this https URL.

---


### 164. [DARTree: Speculative Diffusion Decoding with Autoregressive Draft Trees](https://arxiv.org/abs/2608.13524)

**<font color=#1a73e8>作者：</font>** Tianyi Li, Yaxin Luo, Xinyi Shang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding losslessly accelerates autoregressive language models by verifying multiple draft tokens in parallel. Diffusion-based drafters further reduce proposal latency by predicting an entire token block in parallel, but their position-wise distributions are marginal rather than conditioned on tokens selected along each draft path. Existing recurrent correction incorporates causal information along a single draft chain, whereas diffusion-based tree construction broadens candidate coverage without carrying this correction along individual branches. We introduce DARTree, a training-free speculative decoding method that extends a pretrained AR correction head from chains to trees. DARTree first constructs a fixed-width candidate tree by expanding and scoring all nodes at each depth in a single batch, and then only applies best-first pruning to select the verification tree, decoupling AR-head inference from sequential heap operations. Across seven math, code, and chat benchmarks, DARTree achieves the highest average acceptance length and speedup in all four model--temperature configurations, accepting up to 12.97 tokens per verification round, 98.6\% more than DFlash and 27.9\% more than Domino in the same setting, and reaching up to 9.73$\times$ lossless speedup over locally measured autoregressive decoding.

---


### 165. [SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via Representation Verbalization](https://arxiv.org/abs/2608.13538)

**<font color=#1a73e8>作者：</font>** Weihan Meng, Hongzhu Guo, Yi Jing 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are proposed to extract numerous features from large language model (LLM) representations, yet explaining these features still relies primarily on external observation. This reliance leads to superficial explanations inferred from observed model behavior and computational inefficiency from collecting such behavioral evidence at scale. We introduce SAEVerbalizer, a framework that injects SAE decoder directions into an LLM's representations and fine-tunes the LLM's downstream layers to generate natural-language explanations of the injected features. Once trained, the resulting verbalizer explains SAE features directly from decoder directions, addressing both limitations. Our experiments show that the learned verbalization capability generalizes to unseen features, transfers across separately trained SAE dictionaries, and, with a lightweight adapter, extends to SAE features from different LLMs. Intervention experiments show that injecting multiple directions yields an explanation combining their meanings, while reversing individual directions produces corresponding meaning shifts.

---


### 166. [LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure](https://arxiv.org/abs/2608.13545)

**<font color=#1a73e8>作者：</font>** Fanfei Li, Jana Zeller, Manuel Prada-Corral 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern language models are trained on heterogeneous web-scale text corpora. Consequently, studying knowledge and skill acquisition is difficult, as prior exposure to related content is hard to characterize. To address this challenge, we introduce LITTLECURRICULUM, a curated 88B-token pretraining corpus tailored to U.S. elementary school material, explicitly excluding concepts, facts, and vocabulary taught above Grade 5. Training a 5B-parameter LLM from scratch on LITTLECURRICULUM yields LITTLELEARNER, a model with sufficient language competence for open-ended evaluation, yet with clear knowledge and capability boundaries mapped to interpretable curriculum guidelines. We release LITTLECURRICULUM and LITTLELEARNER as a developmentally restricted sandbox to study how models acquire, represent, and use data under a well-defined training scope. We illustrate the sandbox's utility in a first suite of experiments on injecting new knowledge through post-training and in-context learning. These methods let LITTLELEARNER better utilize existing knowledge, but do not raise out-of-scope capabilities. Our findings underscore the value of this controlled environment for future investigations.

---


### 167. [QuoteBench: How Matched Scores Can Hide Command-Path Failures](https://arxiv.org/abs/2608.13547)

**<font color=#1a73e8>作者：</font>** Shangao Li, Yao Zhang, Volker Tresp 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM coding agents issue Bash commands through interfaces that may serialize, wrap, and reparse model output. Matched execution scores alone cannot distinguish command-generation errors from failures introduced after generation. QuoteBench measures this boundary with exact final-state validation on 56 one-shot tasks from 14 incident-derived families, crossing the generation contract with the execution transport around one deliberately unescaped added parser. Escaping at the interpolation point reproduces each replayed reply's raw-path outcome, so any recovery under a disclosed boundary must come from the model changing its generation. Across eight same-window configurations, replaying the same reply through the added parser lowers success by 55.4 to 73.2 percentage points; disclosure recovers 30.4 to 60.7 points for six configurations, and zero or slightly negative for the other two. Raw generation is nearly saturated at the frontier; boundary adaptation is what still separates models. GPT-5.6-sol's matched gap of -3.6 points hides -64.3 points of damage and +60.7 points of compensation. The deployment configuration reorders models: one reversal among 26 comparable pairs is unambiguous and four more sit on single-task margins. Evaluations of command-issuing agents should report the model configuration, generation contract, execution path, operating point, and final-state validator rather than treat a matched score as an intrinsic model property.

---


### 168. [AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design](https://arxiv.org/abs/2608.13560)

**<font color=#1a73e8>作者：</font>** Yaxin Luo, Haobin Jiang, Jialv Zou 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transforming multimodal sources into condensed and structured media outputs can be fundamentally conceptualized as a long-horizon agentic process centered on a model-harness system. While an ideal harness system should align with human design priors and accumulate reusable experience through empirical exploration to drive recursive self-improvement, existing paradigms remain static and fall short of this capability. In this paper, we present AutoDesign, a framework that aligns with human design priors, where a meta-harness optimizer guides a code agent to recursively improve harness based on rollout feedback. To instantiate and evaluate this framework, we focus on the academic paper-to-poster generation task and introduce PosterBench, comprising a 100-paper Main Track spanning five disciplines and PosterBench-mini, a shared 10-paper subset for controlled evaluation. On the PosterBench Main Track, AutoDesign achieves the highest score of 78.32, surpassing the closed-source commercial system Claude Design by 7.45 points. Across seven controlled code-agent-model configurations, integrating the learned DesignHarness consistently improves performance, increasing the average PosterBench Score from 54.99 to 67.39 (+12.4%). In a fully autonomous long-horizon loop, it executes 253 tool calls and 11 editing turns within 40 minutes for under $3, reaching average conference-poster quality in human evaluation. A system-blind human study further demonstrates that AutoDesign achieves the highest human preference among evaluated systems.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 169. [Geometric and Behavioral Stratification in Transformer Residual Streams](https://arxiv.org/abs/2608.12447)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nelson Guda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trained transformer models develop privileged bases: coordinate axes whose statistics differ from the rest of the residual stream. But what kind of direction does such a basis select? We investigate the prediction direction, the unembedding direction of the token a model currently predicts, and find that it functions as a content-defined privileged anchor. Measured with respect to this anchor, residual-stream variation is geometrically and behaviorally stratified by proximity to the prediction.
The stratification holds in all eighteen models tested (dense and mixture-of-experts, 7B-120B, base and instruction-tuned). A narrow, scale-invariant prediction interface concentrates readout-relevant structure, while the vast prediction-distal complement expands with model scale. Because the prediction direction sits nearly orthogonal to the principal variance axes, variance-based analyses recover this organization only partly, and the shortfall grows with prompt heterogeneity.
Anchoring reveals a steep geometric gradient: prediction-proximal regions are highly structured and cluster related prompts, while the complement is flatter and anti-discriminates among prompt groups. The interface is a narrow slice but functionally decisive. Disrupting the variance directions closest to the prediction causes immediate divergence and frequent task-frame shifts; disrupting the next level down delays divergence and preserves framing. The complement is weakly readout-aligned per direction yet causally and temporally load-bearing, and behavior is driven by direction rather than magnitude.
These results establish the prediction direction as a privileged anchor distinct from previously described coordinate axes, and give a geometric account of how high-dimensional computation coexists with linear readout.

---


### 170. [@skills: Attention is all you have](https://arxiv.org/abs/2608.12610)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Li Yin, Zhi Li, Zhan Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There are 56,804 public agent skills today, and teams write many more privately. The dominant delivery model is installation: once installed, a skill's description remains in the system prompt, competing for fewer than 100 reliable trigger slots. This leaves the long tail with no practical path to use and forces teams' own playbooks to compete for the same scarce space. We observe that installation bundles three separable functions: content, persistence, and automatic triggering. Only the last requires prompt residency. We therefore propose @skills, an open protocol that separates them. A path addresses any skill, subtree, or collection, and reading a skill is sufficient to use it, so nothing is installed or made resident. The operation vendors a copy at the same path into a project's Git-tracked tree for adaptation and ownership. The operation adds one .gitignore-style line, the only element that costs prompt residency. A directory is a menu, making bundles ordinary directories rather than all-or-nothing units. The protocol requires no manifest, lockfile, or registration, and this http URL remains unchanged. @skills is additive, ships as an installable package, and turns any agent that can read files and run commands into a client through a single instruction file. Its open specification is at this https URL and it is implemented in the AdaL CLI at this https URL . Because paths address skills well but cannot find them, the protocol is paired with a free hub at this https URL for corpus-wide search and ranking, repository-free hosting, private and team collections, and one-screen authoring. The hub is optional: gh: and local paths resolve without it, and indexed GitHub skills retain their gh: identities. Install less, use more.

---


### 171. [CW-BASS v2: Saturation-Aware Pseudo-Label Selection for Semi-Supervised Segmentation under Foundation-Model Teachers](https://arxiv.org/abs/2608.12773)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ebenezer Tarubinga  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised semantic segmentation has long turned on one question, which pseudo-labels to trust, and a generation of selection rules, dynamic thresholds, per-class curricula, soft confidence weights, answered it for the noisy, under-confident ResNet teachers of their day. Self-supervised foundation encoders change the regime: with a DINOv2 teacher, confidence saturates, so the filtering that helped a weak teacher can hurt a strong one. We propose CW-BASS v2, a saturation-aware pseudo-label selection method that reads the teacher's confidence regime rather than committing to one rule. It pairs held-out calibration, an unbiased per-class noise estimate, with a self-adaptive confidence floor that provably bounds retention away from 1, and combines them in a one-pass gate: measure the reliability of the teacher's confident set, pi_kept = Pr[correct | c >= tau], on a held-out slice, and filter strictly when it meets the confidence demanded (pi_kept >= tau), falling back to the adaptive floor otherwise. The boundary is the pre-existing operating threshold, not a value tuned to mIoU, and across six DINOv2 teachers it makes the correct strict-vs-floor call blind. CW-BASS v2 thus recovers the UniMatch V2 operating point on the saturated benchmarks by selecting strict (Pascal VOC 1/8 87.4 against its reported 87.9; Cityscapes within 0.5), and improves on it where the confident set is unreliable (pi_kept ~ 89%, ADE20K), where the floor edges ahead (+1.5 mIoU, single seed). The gate is principled because the failure it avoids is measured, not assumed: on a reliable, saturated teacher the confidence distribution's dynamic range collapses (98% of Pascal pixels >= 0.95), so an adaptive cutoff floods the retention mask and self-training decays into confirmation bias.

---


### 172. [I-SDPO: Instance-Level Adaptive Self-Distillation Policy Optimization](https://arxiv.org/abs/2608.12957)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yubo Zhang, Xinhong Ma, Zezhong Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) learns from reward differences within a rollout group, but receives no useful relative signal when every sampled response is incorrect. Privileged self-distillation can fill this gap with dense token supervision, yet applying it throughout training creates a different failure mode: the teacher is a biased, low-variance surrogate for the reward objective, so persistent imitation can oppose reward-improving updates after the policy becomes capable of producing successful trajectories. We introduce I-SDPO (Instance-Level Adaptive Self-Distillation Policy Optimization), which treats teacher reliance as capability-dependent. I-SDPO makes one routing decision per input instance and shares it across that instance's rollout group: all-incorrect groups use a privileged self-distillation objective, whereas any-success groups remain intact for GRPO. This design uses imitation only where group-relative rewards are uninformative. A local analysis characterizes when teacher and reward directions align and shows that a non-vanishing biased distillation weight induces an optimization bias floor. The routing rule automatically reduces the expected distillation rate as success probability rises, withdrawing teacher influence without a hand-designed schedule. On SciKnowEval, I-SDPO obtains the best result in all four scientific domains and improves average mean@16 accuracy from 56.67% with GRPO to 70.31%, with a maximum domain gain of 18.24 points.

---


### 173. [Latent On-Policy Self-Distillation](https://arxiv.org/abs/2608.13040)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Guibin Zhang, Jiayang Lyu, Ran Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enabling agents to learn from experience and internalize it into their policy has become a central problem in self-evolving AI. On-policy self-distillation (OPSD) offers an effective pathway by using a privileged self-teacher to provide dense supervision on the student's own trajectories; however, existing methods still rely heavily on designer-specified privileged artifacts (e.g., answers, feedback, skills, or trajectories), limiting the end-to-end learnability and scalability required for continual self-improvement. In this work, we introduce Latent On-Policy Self-Distillation (LOPD), which, rather than proposing another hand-crafted OPSD variant with a newly prescribed form of privileged context, makes the teacher's privileged context itself learnable end-to-end from experience. Technically, LOPD retrieves relevant experiences and composes them into continuous latent tokens that condition a self-teacher, while the student generates trajectories from the task and interaction history and receives dense token-level supervision at every visited prefix. We further introduce a privileged-margin objective to stabilize and regulate the learning of latent context. Empirically, LOPD demonstrates (I) strong performance, outperforming RLVR and representative OPSD methods including OPSD, SDPO, and Skill-SD across both agentic tool use and code generation; and (II) high learning efficiency, surpassing GRPO and Skill-SD with less than 30% of their rollout budget. Ablation studies further provide direct evidence that making privileged context learnable is necessary for realizing these gains. Together, these results position LOPD as a step toward a more scalable and self-directed paradigm for agent evolution.

---


### 174. [VALG: An Agentic System for ML Theory Research](https://arxiv.org/abs/2608.13060)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dechen Zhang, Xuan Tang, Xinxiang Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning theory studies learning procedures through mathematical setups in which the data model, training protocol, oracle access, loss, metric, and randomness define the phenomenon that a theorem is meant to explain. Solving an open problem therefore requires the problem formulation, theorem target, and proof mechanism to be developed in concert. Researchers formulate hypotheses, test them through preliminary theoretical or empirical analysis, and refine both assumptions and proofs. We investigate whether this process can be organized as an autonomous agentic workflow for ML theory research.
We develop VALG, an agentic system that combines multi-level Verification, Adaptive formulation of Learning-theory problems, and Graph-structured proof development. Within each source-relative theorem branch, VALG maintains a fixed mathematical specification, checks the theorem-level composition of a typed proof-dependency graph, and constructs and reviews local proofs in dependency order. When a proof attempt fails, VALG identifies whether the obstruction lies in a derivation, the proof structure, or the theorem formulation and routes the next attempt accordingly. Formulation-level obstructions initiate an explicitly related variant or relaxation, preserving the mathematical relation between the resulting theorem and the source problem.
We evaluate VALG on nine subproblems from five COLT 2026 open problems. Two runs produce internally finalized theorem candidates that match the scope of their source briefs; the remaining seven yield restricted-method results, special cases, or conditional theorems. These case studies show how VALG keeps source-scope matches, relaxations, conditional results, and blocked attempts mathematically distinct. VALG is open source at this https URL.

---


### 175. [EEG-PRIME: Prototype-Aligned Representation Learning with Multi-Level Conditioning for EEG Decoding](https://arxiv.org/abs/2608.13072)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shuailei Zhang, Muyun Jiang, Wei Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) decoding models often generalize poorly across datasets and subjects due to domain shifts in acquisition protocols and individual neurophysiology. We propose EEG-PRIME, a two-stage EEG foundation model for cross-dataset multi-task decoding. EEG-PRIME combines masked pretraining with prototype-aligned instruction tuning to enable instruction-aware and subject-invariant decoding across diverse BCI paradigms. During pretraining, an EEG encoder learns transferable representations through masked reconstruction with frequency-cutoff spectral augmentation. During instruction tuning, EEG-PRIME incorporates task-semantic, dataset-specific, and subject-invariant conditioning. The resulting conditioning signal modulates the Q-Former through Layer-wise Query Modulation, while frozen text embeddings of class labels serve as prototypes for cosine-similarity-based prediction across heterogeneous label spaces. Experiments on sixteen datasets covering motor imagery, emotion recognition, ADHD detection, covert speech, and mental workload show consistent improvements over state-of-the-art baselines and prior EEG foundation models under cross-subject settings. On two additional held-out datasets, EEG-PRIME achieves balanced accuracy comparable to within-session calibration models without target-domain optimization, calibration, or linear probing, demonstrating promising zero-shot transfer capability.

---


### 176. [Towards Physics-Faithful Generation of Scientific Diagrams](https://arxiv.org/abs/2608.13112)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Minghui Zhang, Jinxin Shi, Yifan Chang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image generation has reached photorealistic quality, yet state-of-the-art systems remain unreliable at producing scientific diagrams, whose value depends not on appearance but on physical faithfulness: correct force directions, valid coordinate systems, consistent thermodynamic states, and equations matching the depicted scenario. Trained on web imagery with physically shallow captions, generic models produce diagrams that look plausible but are physically wrong, harmful in education and scientific communication. We present Princigram, a physics-faithful scientific-diagram generator, and its data pipeline. Our central advance is Structured Physical Chain-of-Thought (SP-CoT): a per-subdiscipline schema that decomposes a physics diagram into an explicit multi-step reasoning chain across six subdisciplines, from scene identification through force or process analysis to governing laws and synthesis. Unlike free-form chain-of-thought, SP-CoT follows a fixed schema with strict fidelity rules that separate visually grounded facts from physically inferred reasoning and type all mathematics symbolically; it serves both as dense training supervision and, at inference, as a structured "thinking" prompt. With it we curate and structurally annotate 4.3 million physics images, of which 115,037 carry expert-level annotation, and adapt a unified multimodal backbone. We further introduce VeriphyT2IBench, whose questions are derived from each held-out diagram's own structured annotation: each diagram becomes an item-specific bank of binary questions about its objects, forces, and states, so a judge model's score decomposes into named physical facts rather than one holistic number. On the physics subset of GenExam and on VeriphyT2IBench, Princigram shows that explicit physics-structured supervision improves the physical faithfulness of generated scientific diagrams.

---


### 177. [HPSD: Hybrid-Policy Self-Distillation for Text-Image-to-Video Diffusion Models](https://arxiv.org/abs/2608.13205)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiazi Bu, Pengyang Ling, Yujie Zhou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-Image-to-Video (TI2V) models are an emerging unified architecture, where a single model simultaneously supports text-to-video (T2V) and image-to-video (I2V) generation. Given a high-quality first frame or a detailed textual prompt, TI2V models unlock substantially better visual quality than their T2V mode, raising a natural question: can the capability elicited by such privileged conditions be internalized into the model's own base generation ability? A common approach toward this goal is model self-distillation. However, the most straightforward solution, supervised fine-tuning, follows an off-policy strategy: its supervision is confined to teacher-generated endpoints from a fixed offline distribution rather than student-visited states, lacking precise correction tailored to the evolving policy. Recent on-policy distillation methods instead suffer from condition-state mismatch, where supervision is steered toward the given first frame instead of the student's actual content, misleading the correction. To achieve self-distillation that absorbs the teacher's privileged prior while retaining precise policy correction, in this work, we propose Hybrid-Policy Self-Distillation (HPSD), a novel self-distillation framework where a single TI2V model acts as both teacher and student under different conditions: the teacher operates in TI2V mode with a high-quality first frame and an enhanced prompt, while the student runs in the base T2V mode with only the vanilla prompt. Specifically, the student inherits off-policy teacher trajectory points as anchors, locally refines them toward its own policy, and finally receives velocity-level supervision on these self-generated roll-outs. Extensive experiments demonstrate that HPSD significantly improves T2V performance while also delivering notable TI2V gains, effectively strengthening the model's base generation ability.

---


### 178. [Into the ORBIT for Time Series: Training Regimes for Foundation Models](https://arxiv.org/abs/2608.13262)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hongjie Xia, Yiding Liu, Yifan Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) have advanced primarily through architectural innovation, while training regimes for large-scale heterogeneous corpora remain under-explored. As a result, pre-training distributions are often poorly controlled with respect to domain imbalance, context requirements, prediction horizons, and missingness. We introduce ORBIT (Omni-Range Bootstrap Incremental Training), a training paradigm that makes this distribution explicit and controllable. ORBIT combines Bootstrap Multi-Level Sampling, which controls dataset exposure and samples records, target variables, context windows, and prediction horizons, with Omni-Range Incremental Training, which varies context lengths and prediction horizons throughout a single training stage. Under ORBIT, we train Falcon-2.0, a simple univariate encoder-only Transformer with missingness-aware triple-channel patch tokenization and parallel patch prediction. We further introduce Rank-Guided Cross-Depth Alignment, a training objective that uses late-layer representations as stop-gradient teachers for shallow layers without additional inference cost. Evaluations on GIFT-Eval and fev-bench demonstrate strong zero-shot forecasting performance across diverse domains and frequencies.

---


### 179. [Rules or Character? Scaling Laws for AI Safety Design](https://arxiv.org/abs/2608.13345)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Satoshi Takahashi, Nobuji Kouno, Masaaki Komatsu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) safety systems combine character shaping (e.g., Reinforcement Learning from Human Feedback [RLHF], Constitutional AI), which modifies behavioral distributions at training time, with rule enforcement (e.g., output filters, safety classifiers), which blocks harmful outputs at inference time, yet little formal analysis exists on how their optimal balance should change as deployment scales increase. We introduce a stylized comparative-statics model that parameterizes safety design as a resource allocation alpha in [0,1] between these two approaches, incorporating scale-dependent filter degradation, common-mode failures, and character fragility -- the risk that shaped behavior degrades or collapses under novel conditions. Under a multiplicative Pareto damage model, we derive closed-form expected harm and supplement it with tail-risk (CVaR) analysis via Monte Carlo simulation. Across three scenarios (optimistic, moderate, pessimistic), the optimal alpha* is interior or at the rules-only boundary and shifts weakly toward character shaping as deployment scale T grows, from negligible (Delta alpha* = +0.01) to pronounced (Delta alpha* = +0.21) depending on scenario. The dominant parameter is the baseline character fragility rate p^(0)_frag, which shifts alpha* by 0.50 across its range -- far exceeding the effect of tail severity, filter quality, or common-mode failure probability. CVaR and expected-harm optima converge at large T. These results suggest that safety architecture decisions depend less on deployment scale per se than on the reliability of character shaping under distributional shift.

---


### 180. [When Is a Task Vector Enough? An Empirical Theory of Implicit Multimodal ICL](https://arxiv.org/abs/2608.13385)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiaqian Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit multimodal in-context learning compresses demonstrations into internal interventions, ranging from static task vectors to query-conditioned transformations and attention routing. Despite their common goal, these methods differ substantially in how the intervention depends on the query and where it modifies the model, leaving unclear which additional complexity is necessary for a given task. We propose the Selection--Realization Hypothesis. It views demonstrations as inducing a compact family of internal changes from which the query selects, while the model's computation constrains how the selected change can be implemented. We evaluate this account using controlled multimodal tasks in which query dependence varies without changing the underlying task primitives or prompt format. By contrasting correct demonstrations with matched counterfactuals, we measure the structure of explicit M-ICL and test whether it predicts intervention behavior. We find that the success of a static task vector is closely tied to how much of the demonstration-induced change is shared across queries. Additional intervention complexity becomes useful when explicit M-ICL contains query-specific or distributed structure that a local additive shift cannot recover. These relationships extend to natural VQA benchmarks and support cost-aware method selection without access to test performance. Our results provide a unified empirical theory of when demonstrations can be compressed into a task vector and when a more expressive intervention is warranted.

---


### 181. [Evaluation of Clinically Steerable Retinal Image Generation from Foundation Model Latent Spaces](https://arxiv.org/abs/2608.13455)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zuzanna A. Wakefield-Skórniewska, Bartłomiej W. Papież  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical foundation models learn latent representations of clinically meaningful phenotypes, yet their ability to support controllable image generation remains largely unexplored. We evaluate four retinal foundation models within the representation tokenizer framework and examine whether demographic and clinical information encoded in latent representations from foundation models is preserved during synthetic image generation. We show that generated representations and images faithfully inherit phenotype information when evaluated within their originating foundation models, consistently outperforming conventional latent diffusion on multiple downstream prediction tasks. However, these gains largely disappear when evaluated using classifiers trained on real images, revealing a previously uncharacterised synthetic-to-real representation gap. These findings demonstrate that foundation-model latent spaces provide a powerful substrate for controllable retinal synthesis while highlighting the need to better align synthetic representations with real-image distributions.

---


### 182. [Fine-Grained Action Recognition with Cross-Attentive Latent Sparse Experts](https://arxiv.org/abs/2608.13458)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Imtiaz Ul Hassan, Tasweer Ahmad, Nik Bessis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained human action recognition (FHAR) must distinguish visually similar actions that differ mainly in body configuration, timing, or local appearance. RGB representations retain visual context but often suppress joint-level geometry, whereas skeleton representations encode kinematics but discard dense spatial detail. We introduce FineX, which factorizes fine-grained cues into RGB appearance, pose heatmap geometry, and skeletal-graph topology. Pairwise cross-attention enables symmetric, stream-preserving information exchange, followed by a streamwise latent sparse Mixture-of-Experts that routes each representation to a content-dependent subset of shared experts, regularized by a load-balancing objective. FineX achieves state-of-the-art results on Gym99, Gym288, and Diving48. On the long-tailed Gym288, it raises mean class accuracy from 68.6% to 76.2% (+7.6 points) without textual supervision or large-scale vision-language pre-training, demonstrating the benefit of structured visual-pose-graph fusion and conditional expert refinement for FHAR.

---


### 183. [Intern-S2-Preview: Scientific Agentic Foundation Model](https://arxiv.org/abs/2608.13505)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lei Bai, Jiaqi Cao, Chiyu Chen 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific discovery increasingly requires AI systems that can reason over scientific evidence of heterogeneous modalities, interact with scientific tools and environments, and sustain progress across long task horizons. We present Intern-S2-Preview, a series of scientific agentic foundation models designed to support multimodal scientific understanding, reasoning, generation, and long-horizon tasks. The training pipeline begins with scientific multimodal pre-training over rendered scientific documents, interleaved image-text data, and diverse scientific corpora. Starting from the pretrained checkpoint, we apply a unified post-training pipeline consisting of supervised fine-tuning, scalable multi-task reinforcement learning (RL), black- and white-box agentic RL, and on-policy distillation. This pipeline is supported by practical techniques that improve rollout and training stability and efficiency, including partial rollout with off-policy correction, adaptive length regularization, online speculative decoding, robust multi-task optimization, and trace-aware experience assembly for agentic tasks. At the architecture level, Intern-S2-Preview-397B extends time series modelling from efficient long-sequence understanding to numerical forecasting, while Memory Decoder is studied as a separate memory-augmented path for rapid scientific specialization without modifying the frozen 397B backbone. Evaluations across scientific, multimodal, agentic, and general-purpose benchmarks show that Intern-S2-Preview-397B achieves competitive or leading results in multiple settings. The time series modules improve scientific signal understanding and forecasting on SciTS, while the separate Intern-MemDec-4B extension improves the Biology-Instructions average score from 56.92 to 60.32 without modifying the frozen 397B backbone.

---


> [!TIP]
> 当前位于：**151-183**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-183**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
