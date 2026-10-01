# 🧠 大模型相关研究 | 2026年10月02日

> 本类共 **390** 篇论文：已确认 **371** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-390](./part-08.md)

---

### 301. [Spherical Interpolation for Backward-Compatible Multimodal Representations](https://arxiv.org/abs/2609.39836)

**<font color=#1a73e8>作者：</font>** Simone Ricci, Niccolò Biondi, Federico Pernici  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive vision-language models map visual and textual representations into a shared normalized embedding space, making cosine similarity the natural metric for cross-modal retrieval. A practical challenge arises during model upgrades: independently trained models generally produce incompatible representation spaces, so replacing a deployed model typically requires recomputing embeddings for the entire gallery, which is prohibitively expensive at scale. Orthogonal post-hoc alignment can partially mitigate this problem by mapping new-model queries into the old-model gallery space. However, because independently trained models can differ in fine-grained representation structure, the orthogonal alignment remains approximate, leaving a residual angular discrepancy between the old-model query and the aligned new-model query. We study whether interpolation along the spherical geodesic between these two normalized query representations can improve retrieval without re-indexing the gallery. We characterize when this path contains an interior query direction closer to an idealized retrieval-optimal direction than either endpoint, and connect this characterization to Recall@$K$ through a local margin-based certification result. Experiments across multiple benchmarks and model families show that post-alignment spherical interpolation improves over orthogonal alignment alone, recovering backward-compatibility in most evaluated settings. Consistent with our geometric characterization, per-query oracle analysis shows that retrieval-favorable interior points occur frequently in practice. Code is available at this https URL .

---


### 302. [Learning Steganography Is Easy, Learning Steganographic Reasoning Is Hard](https://arxiv.org/abs/2609.39838)

**<font color=#1a73e8>作者：</font>** Julian Schulz, Lukas Fülle, Rieke Fruengel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought monitoring as an approach for AI oversight and control is threatened by the possibility of steganographic reasoning, where LLMs conceal their reasoning inside innocuous-looking text. Two neighbouring capabilities, steganographic messaging (passing a concealed message) and encoded reasoning (reasoning in an illegible but unconcealed format), have already been shown to emerge under training pressures that occur in real pipelines, such as reinforcement learning against monitors. This suggests that steganographic reasoning too might arise as an unintended side effect of training. Here, we compare how easily models learn steganographic reasoning and these two neighbouring capabilities across three elicitation methods: reinforcement learning, in-context learning, and supervised fine-tuning (SFT).
For most tasks, models learn steganographic reasoning only under SFT, while they learn steganographic messaging and encoded reasoning under all three elicitation methods. Even under SFT, steganographic reasoning requires at least twice as much training as messaging, and for several model-task combinations it is not learned at all. However, on a cover task that makes hiding information especially convenient, steganographic reasoning can be successfully learned under all three elicitation methods. Steganographic reasoning is thus much harder than steganographic messaging and encoded reasoning, and learning the latter two does not imply learning the former. Yet it lies within reach: an easy version is learned under every elicitation method, when the cover task is convenient for hiding information.

---


### 303. [When a Kindergartener Solves Calculus: Measuring Capability Leakage in Role-Prompted Reasoning Models](https://arxiv.org/abs/2609.39846)

**<font color=#1a73e8>作者：</font>** Pakhapoom Sarapat, Saksorn Ruangtanusak, Kunat Pipatanakul 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate the problem of role-capability leakage (RCL), in which a role-prompted reasoning model generates convincing in-role text while continuing to exhibit capabilities on benchmarks that exceed those implied by the assigned role. For example, when a model is prompted to assume the role of a kindergarten student, one might expect its performance on a mathematics benchmark to reflect kindergarten-level ability rather than expert-level proficiency in solving calculus problems. We introduce RoleCapBench, a curriculum-grounded benchmark for evaluating RCL across six educational roles and four assessment levels spanning elementary school through A-level, and use it to evaluate three open-weight reasoning models. We find that although the models can generate stylistically convincing in-role responses, they consistently fail to align their underlying capabilities with their assigned roles. Naive role prompting yields strong role-voice scores of 1.218--1.389 while retaining above-role accuracy of 0.811--0.898. RCL persists across a range of prompting conditions, including prompts that explicitly instruct the model to match the role's capability level. To mitigate this problem, we propose Injection, an inference-time intervention that combines explicit, role-specific capability guidelines with a guiding prefilled response prefix. Injection improves role-capability alignment across models, reducing above-role accuracy by up to 0.562 while preserving in-role accuracy with a marginal drop of less than 0.058 across most models. All artifacts, including scripts and evaluation data, will be released upon acceptance.

---


### 304. [Cognitive Enhancement: Rethinking the Necessity of Role-Playing for Large Language Models](https://arxiv.org/abs/2609.39853)

**<font color=#1a73e8>作者：</font>** Xingjie Zhuang, Jialong Tang, Chulun Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Role-playing prompting has become a popular yet simple technique for improving LLM reasoning and output quality. However, whether it consistently boosts performance across diverse domains remains unclear, as systematic validation is lacking. To fill this gap, we run multi-model, cross-domain, and multilingual experiments on MMLU and MMLU-Redux. We find that gains from role-play prompting depend heavily on model capacity, knowledge domain, and prompt language. Drawing on metacognition theory, we propose the persona-related cognitive alignment hypothesis: role-play works only when the LLM correctly grasps the designated persona and its associated knowledge domain. We test this hypothesis through persona information richness ablation, layer-wise entropy divergence analysis, and latent thought-space deflection observation. To reduce persona cognitive bias and stabilize role-play performance, we propose \textbf{M}ixed-\textbf{L}anguage \textbf{C}oncatenate \textbf{P}rediction \textbf{(MLCP}), a simple, training-free, and efficient multilingual prompt concatenation strategy. It aggregates semantically equivalent role prompts to enrich complementary representational cues. Extensive experiments show that MLCP consistently outperforms vanilla role-play prompting across all tested LLMs.

---


### 305. [Fork-dLLM: Avoiding the Flexibility Trap in Diffusion Language Models](https://arxiv.org/abs/2609.39859)

**<font color=#1a73e8>作者：</font>** Stipe Frković, Metod Jazbec, Christian A. Naesseth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (dLLMs) have shown strong potential for faster inference through parallel token generation when combined with confidence-based samplers. However, recent work has shown that such methods can defer unmasking high-entropy fork positions at which multiple plausible continuations exist. This results in reduced generation diversity, as shown by worse pass@k scaling, and limits gains obtainable from RL post-training. To avoid this flexibility trap, prior work advocated for autoregressive (AR) sampling. Here, we show that discarding confidence-based sampling is unnecessary and, once inference cost is taken into account, wasteful. We first propose Fork-dLLM, a simple hybrid sampler that uses AR-style ordering only at uncertain fallback steps while retaining parallel generation otherwise. We then extend the same principle to post-training with ForkGRPO, which uses Fork-dLLM rollouts and applies the GRPO objective only at fallback steps, preserving exact policy-likelihood ratios while substantially reducing rollout and optimization cost. In our experiments, Fork-dLLM matches the strong pass@k scaling of AR sampling while being 2-3x more efficient, and ForkGRPO achieves downstream performance comparable to or better than AR-based GRPO baselines at a substantially lower training cost.

---


### 306. [FIGS: Evaluating Multi-Turn Sycophancy Without Penalizing Empathy](https://arxiv.org/abs/2609.39863)

**<font color=#1a73e8>作者：</font>** Sidharth Pulipaka, Ruta Binkyte, Ivaxi Sheth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models frequently fail to balance staying truthful with being supportive. They often exhibit sycophancy in responses to users, agreeing with false claims, offering unwarranted flattery, and giving advice skewed toward users' expressed views. In reality, sycophancy rarely happens in a single exchange; it may emerge organically as users repeatedly insist or subtly steer the dialogue over time. Current evaluations, however, rely on rigid, single-turn tests or fixed scripts that fail to capture these natural dynamics. Furthermore, these benchmarks often mistake showing basic empathy for yielding, penalizing models for acknowledging a user's feeling. This view may drive future models to over-correct into cold, dismissive rigidity. To address this gap, we introduce FIGS (Factual Integrity and Grounded Support), a dual-axis evaluation framework built around extended, realistic dialogue. We use an adaptive 10-turn conversational simulator that dynamically challenges the target model, reflecting how users repeat requests, push back, or steer a conversation toward a preferred answer. To accurately evaluate these trajectories, we apply a taxonomy that strictly separates Sycophancy (whether the model holds firm to the truth and keeps its praise proportional) from Calibrated Validation (showing empathetic understanding of the user's feelings without overdoing it). We release our complete testing environment, including 500 diverse multi-turn scenarios and an automated judge. Our evaluation of leading models reveals a consistent trade-off: over the course of a sustained interaction, current systems either slowly drift to sycophancy or over-correct into robotic detachment. This demonstrates that balancing honesty with appropriate support throughout a natural conversation remains a critical, unsolved challenge.

---


### 307. [Preemptive LLM Unlearning against Forbidden Capability Acquisition via Gradient Sealing](https://arxiv.org/abs/2609.39866)

**<font color=#1a73e8>作者：</font>** Kemou Li, Qizhou Wang, Yue Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-weight LLMs are released not only as fixed products but also as substrates for downstream fine-tuning. This openness, however, creates legal and ethical risks because users may misuse fine-tuning to instill illicit knowledge or enable hostile operations. Model providers therefore need apre-release defense against such acquisition, motivating the problem of preemptive unlearning. Unlike retrospective unlearning, which removes capabilities already present in a fixed model, preemptive unlearning seeks to prevent their acquisition under unseen attack data and future fine-tuning procedures. Despite its practical importance, this setting remains largely unexplored, presents distinct challenges, and is therefore the central focus of our work. We first verify that existing retrospective methods provide insufficient pre-release protection. Even when forbidden capabilities are suppressed in current outputs, forbidden-domain data can still induce gradients through internal pathways, enabling later acquisition. Motivated by this finding, we propose a gradient-sealing principle that blocks these pathways by pushing relevant pre-activations into the negative region, where ReLU-family activations exhibit zero or near-zero derivatives. Experiments across multiple LLM families demonstrate our stronger resistance to downstream acquisition than retrospective baselines, validating gradient sealing as an effective mechanism for pre-release protection.

---


### 308. [GrammarRL: Effective Grammar-Constrained Decoding via Reinforcement Learning](https://arxiv.org/abs/2609.39869)

**<font color=#1a73e8>作者：</font>** Gabriele Tuccio, Antonino Furnari, Aldo Gangemi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Grammar-constrained generation guarantees syntactic validity, but can substantially degrade semantic quality when the model's preferred outputs are poorly aligned with the imposed grammar. This trade-off is particularly severe when the prompt is underspecified or the model has limited instruction-following ability. Beam search can partially mitigate these failures by exploring multiple valid sequences, but its computational cost grows with beam width, while sequence-level probability is only an imperfect proxy for semantic quality.
We introduce GrammarRL, a label-free reinforcement learning method that adapts language models to grammar constraints without requiring annotated data. GrammarRL optimizes the model using two complementary self-supervised rewards derived from its own likelihoods: a direct reward, measuring how likely the constrained output is given the input, and a reverse reward, measuring how well the input can be reconstructed from the generated output. We optimize these rewards with a Reinforce Leave-One-Out (RLOO) objective over groups of grammar-constrained rollouts, augmented with the top-1 beam-search hypothesis and regularized towards a frozen base model.
We evaluate GrammarRL on sign language gloss translation, hierarchical text classification, and named entity recognition using Llama models ranging from 1B to 8B parameters. GrammarRL consistently outperforms constrained greedy decoding, with an average improvement of 9.8 points and gains of up to 22.8 BLEU. It matches or outperforms beam search on two of the three tasks while preserving greedy-decoding inference cost. Ablations further show that the two rewards are complementary: either reward alone can underperform the untrained baseline, whereas their combination consistently improves upon it.

---


### 309. [PassGPT+: Leveraging Linguistic Priors for Password Modeling](https://arxiv.org/abs/2609.39880)

**<font color=#1a73e8>作者：</font>** Rajneesh Anand, Neeraj Lakshmanan, Masoud Yari  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Passwords remain the dominant online authentication mechanism, and understanding how humans choose them is essential for defensive strength estimation and attack simulation alike. Recent learning-based approaches such as PassGAN and PassGPT have shown that deep generative models can learn password structure directly from leaked corpora. However, both train from random initialization on password data alone. The role of linguistic prior knowledge in password modeling, and what it reveals about how humans create secrets, remains largely underexplored. Here, we address this gap with PassGPT+, which adapts the linguistic prior of GPT-2 to password observations through character-aware tokenization. We also introduce PassDiffusion, the first absorbing-state discrete diffusion model for password generation, as a probe of whether non-autoregressive approaches are competitive. On the RockYou benchmark, PassGPT+ recovers 22.53% of held-out passwords at 108 guesses, a 16% relative gain over PassGPT, and retains 79% of this match rate when transferred without retraining to a disjoint 2020 leak dataset, demonstrating that linguistic priors capture persistent regularities of human password generation. PassDiffusion underperforms by two to three orders of magnitude, indicating that autoregressive modeling is substantially better matched than iterative denoising to the discrete, exact-match nature of password generation.

---


### 310. [LLM Persona Unlearning](https://arxiv.org/abs/2609.39882)

**<font color=#1a73e8>作者：</font>** Kemou Li, Zhuan Shi, Qizhou Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pre-training equips large language models (LLMs) with a broad repertoire of behavioral patterns associated with roles, styles, values, and goals. Post-training teaches conditional enactment and makes a helpful Assistant the default, but it does not erase alternative modes from the weights; explicit prompts can therefore elicit personas that repeatedly shape judgment, language, and action. In open-weight settings, runtime controls can be removed, motivating persona unlearning: a weight-level edit that makes a designated persona difficult to elicit and enact on unseen contexts. We introduce PersonaUnlearnBench, a model-specific paired benchmark spanning six LLMs from three families and five personas, with aligned forget/retain sets, held-out instruction paraphrases, and four-axis evaluation. The benchmark shows that standard unlearning methods cannot reliably erase the target persona without sacrificing meaningful generation or general utility. We therefore propose PaCE, which compares target and desirable responses to the same questions to locate an internal behavior direction, then trains target-prompt states away from the target mode and toward the matched desirable response. Experiments show that PaCE consistently suppresses target personas with high response quality and useful counterpart behavior, at moderate utility cost. These results establish persona unlearning as a distinct behavior-level editing problem and a practical route toward persistent control of latent LLM response policies.

---


### 311. [OPSRD: On-Policy Self-Role Distillation](https://arxiv.org/abs/2609.39884)

**<font color=#1a73e8>作者：</font>** Weijie Ren, Yanwen Zhang, Hao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Role prompting elicits specialized behavior from large language models through an expert identity, offering a lightweight way to guide reasoning on demanding tasks. However, evaluating or distilling complete role-prompted answers can miss useful next-token preferences when the sampled solution remains incorrect. Transferring these preferences also requires an objective that reaches alternatives the student rarely predicts. We introduce OPSRD, which uses a fixed expert role as privileged teaching context for on-policy self-distillation without reference solutions. A role-free student generates a trajectory, and a frozen instance of the same base model supplies role-conditioned distributions on its exact prefixes, exposing alternatives beyond the sampled continuation. Teacher-weighted forward KL targets alternatives the student underestimates, with clipping to limit individual vocabulary contributions. Supervision is restricted to the highest-entropy half of student positions, concentrating learning where predictions are uncertain. Experiments on three competition-math benchmarks with Qwen3-1.7B, 4B, and 8B show improvements over the base models without role prompts at inference. Forward KL achieves the highest macro-averaged accuracy among the three evaluated divergences at every scale. Code is available at this https URL.

---


### 312. [Learning Where to Look: Anatomical Grounding and Guided Attention for Cardiac MRI Vision-Language Models](https://arxiv.org/abs/2609.39899)

**<font color=#1a73e8>作者：</font>** Bangwei Guo, Xiao Chen, Boris Mailhe 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cardiac magnetic resonance imaging (CMR) enables assessment of cardiac anatomy, ventricular function, and myocardial tissue characteristics. Clinicians interpret these images by identifying cardiac structures and focusing on the regions relevant to each clinical question, motivating anatomically guided vision-language models (VLMs). Yet CMR-specific supervision for anatomical localisation and clinical question answering remains limited. To address this gap, we investigate fine-grained CMR visual question answering through anatomical grounding and guided attention. We construct 128,915 anatomical-grounding and 42,799 clinical QA pairs across short-axis cine, late gadolinium enhancement, and long-axis cine. These datasets support anatomical recognition, localisation, and clinical assessment without requiring paired reports for individual training images. To help the model learn where to look, we introduce Cardiac Anatomy-Routed Attention (CARA), which selects predicted anatomical priors according to the question and guides decoder attention with learned task-specific strengths. Combining anatomical grounding pretraining with CARA yields our model, CARA-VL. Experiments demonstrate CARA-VL's strengths in clinical assessment and regional localisation across CMR imaging settings, with promising generalization to an external clinical cohort. Together, our data and method provide a practical framework for studying and advancing cardiac visual understanding in VLMs. We will release the QA data derived from public datasets upon publication.

---


### 313. [OSWorld-Science: A Benchmark of Computer Use Agents for Learning and Using Scientific Software](https://arxiv.org/abs/2609.39903)

**<font color=#1a73e8>作者：</font>** Dingyuan Dai, Heli Qi, Lei Liu 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific software presents a demanding test for computer-using agents based on visual language models (VLMs): completing a research workflow requires interpreting specialized interfaces, manipulating scientific objects, and producing verifiable results. We thus introduce OSWorld-Science, a benchmark and evaluation environment that combines scientifically meaningful tasks, artifact-based evaluation, and an efficient agent harness for studying computer use in the scientific domain. The benchmark contains 12 VLMs and 146 high-quality tasks across several scientific domains and software configurations, covering workflows such as molecular drawing and retrosynthesis, pathology image analysis, statistical computing, and physical simulation. Tasks are developed through expert proposals and iterative human--AI co-design, with selection guided by scientific value and difficulty. Task-specific execution-based evaluators inspect application states and generated artifacts, including molecular structures, segmentation masks, plots, and numerical results, and award partial credit for incomplete outcomes. Our special harness integrates model adapters, interaction-loop control, and trajectory logging to support comparisons of models and interaction strategies. Our results show that current state-of-the-art VLMs with a strong harness still face challenges in addressing key questions in the scientific domains. We also analyze the benchmarking results across multi-linguistics, reasoning efforts, context length and other factors and derive several important conclusions and directions to assist future development. Overall, we provide an integrated framework connecting expert-defined scientific goals to verifiable software outcomes, enabling systematic evaluation of both agent capabilities and harness design in scientific workflows.

---


### 314. [TRACE: Trajectory Selection for Parallel Scaling of Search Agents](https://arxiv.org/abs/2609.39912)

**<font color=#1a73e8>作者：</font>** Qisheng Zhou, Zhen Xiong, Qiaoyu Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parallel search may generate a correct answer that final-answer voting fails to select. We formulate this consolidation stage as trajectory selection and introduce TRACE (Trajectory Ranking with Aggregated Cross-Rollout Evidence), a lightweight learned selector that ranks completed trajectories using the search evidence behind their answers. TRACE preserves individual query and evidence occurrences, connects rollouts through shared content or document identity, and propagates information across these relations. Each candidate answer then reads the updated states of its own trajectory, preserving retrieval provenance while incorporating evidence from related rollouts. Trained with answer-level supervision over frozen text embeddings, TRACE returns an existing answer without additional search or autoregressive aggregation. One selector per search setting transfers across rollout policies and agent backbones without agent-specific fine-tuning, improving over voting across six WebQA policies and six long-horizon dataset-backbone combinations at $K=16$. On Qwen2.5-14B Base/SFT WebQA pools, TRACE achieves 45.2/49.2% EM, compared with 43.9/48.0% for the strongest Qwen3-32B generative aggregators. On long-horizon FRAMES, GAIA, and BrowseComp, it reaches 78.6% average accuracy, exceeding majority voting by 3.1 percentage points. On Base WebQA pools, TRACE with only 8 rollouts comes within 0.4 points of majority voting over 64. TRACE also achieves at least $10\times$ higher processing throughput than SolAgg, SummAgg, and AggAgent across all seven WebQA benchmarks. These results show that reusing cross-rollout search evidence provides an effective and efficient alternative to heavyweight generative aggregation for parallel search. Code is available at this https URL.

---


### 315. [The Concrete-Arbitrary Gap: Kinship Reasoning in LLMs Is Not Indifferent to Presentation](https://arxiv.org/abs/2609.39913)

**<font color=#1a73e8>作者：</font>** Thomas Pashby  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We test whether large language models solve formally matched kinship problems equally well when relations are expressed in familiar vocabulary or by explicitly defined nonce predicates. Across 500 paired graphs, concrete accuracy exceeds arbitrary accuracy by 35.6 percentage points in local Qwen3.8-27B, 26.6 in Gemma 4 26B-A4B, 12.0 in Gemma 4 31B, and 5.4 in Qwen3.8-Max. All four paired gaps are statistically resolved. Reasoning budgets and prompt-language interventions can substantially reduce the difference, showing that it is modifiable rather than a fixed incapacity. The minimal conclusion is behavioral: on these tasks, the models' manifested relational competence is not indifferent to presentation. Explicit definitions provide the formal relations but do not make nonce predicates as usable as familiar vocabulary embedded in learned linguistic associations.

---


### 316. [MCD: Causal Distillation of Multimodal In-Context Learning in Large Vision-Language Models](https://arxiv.org/abs/2609.39920)

**<font color=#1a73e8>作者：</font>** Yanshu Li, Jiaqian Li, Canran Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) exhibit strong multimodal in-context learning (ICL) capabilities, yet this ability degrades substantially as model size decreases. Knowledge distillation offers a natural way to bridge this gap, but existing methods primarily align output distributions or hidden representations directly. Such alignment teaches the student what the teacher predicts without revealing which evidence in the complex context causally supports that prediction. Consequently, a student can imitate the teacher's answer while continuing to rely on language priors, prompt structure, or other spurious cues. To address this limitation, we introduce Multimodal Causal Distillation (MCD), a distillation framework that transfers how a strong teacher uses multimodal evidence during ICL. MCD uses structure-preserving token interventions to identify and verify causal evidence, then transfers how the teacher responds when that evidence is retained or removed. This design connects distillation to the causal patterns by which the model uses contextual evidence during multimodal ICL. Experiments across three LVLM families and seven benchmarks show that MCD improves student performance by 7.23 points on average and outperforms vanilla distillation by 4.68 points, while further analyses confirm the generalizability of these gains.

---


### 317. [CoVisco: Codec-Native Vision Encoder with Native Token Compression for Unified Image-Video Understanding](https://arxiv.org/abs/2609.39924)

**<font color=#1a73e8>作者：</font>** Yulong Liu, Xiaotian Han, Junyuan Shang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models face a fundamental scaling bottleneck: the number of visual tokens grows with both temporal duration and spatial resolution, making long-video understanding expensive for the vision encoder and the language model. Existing methods often compress visual tokens after dense encoding, creating a mismatch between the representation used during training and the compact interface required at deployment. We present CoVisco, a codec-native vision encoder with native token compression for unified image-video understanding. By combining codec-native input support with segmented attention, CoVisco can encode long visual inputs in a single forward pass without forming dense patch-to-patch interactions across all frames. Each temporal segment is equipped with learnable abstract tokens that learn a compact segment-level representation, while fine-grained patch tokens remain available throughout the encoder. Alternating intra-segment and abstract-communication layers preserve video-level context through the abstract-token channel. A lightweight selector further exposes either abstract tokens alone or abstract tokens augmented with a runtime-selected subset of patch tokens, yielding a compact visual interface that reduces the visual context and prefill burden of downstream MLLMs while retaining fine-grained evidence when needed. Pretrained with contrastive objectives on 565M image--text pairs and 6.4M videos, CoVisco shows competitive performance on video-oriented embedding and multimodal understanding benchmarks. In the evaluated four-segment, 64-frame setting, abstract-only inference uses only 400 visual tokens while achieving video-understanding performance close to, and on some benchmarks exceeding, OneVision-Encoder. Selected patch tokens further improve fine-grained video reasoning. Project URL: this https URL

---


### 318. [AdaGEPA: Adaptive Feedback Allocation for Reflective Prompt Optimization](https://arxiv.org/abs/2609.39927)

**<font color=#1a73e8>作者：</font>** Junyang Chen, Zecheng Wang, Jingbang Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt optimization improves the performance of language-model systems on downstream tasks by refining their prompts. Classical methods evaluate prompts on task examples and use the resulting feedback to guide prompt revisions through reflection. However, when feedback selection does not account for the prompt's weaknesses, these revisions may improve performance on selected examples without yielding broader task improvements. To address this issue, we propose AdaGEPA, an adaptive feedback-allocation method that uses the prompt's performance and task structure to select examples for the next prompt revision. Our method replaces at most one example in each feedback minibatch to target an identified weakness while preserving the remaining feedback context. Across our main experiments on six downstream benchmarks, AdaGEPA achieves higher mean validation scores than non-adaptive feedback selection under matched rollout budgets. AdaGEPA also finds high-performing prompts earlier across several tasks. In the initial Schema-Guided Dialogue (SGD) study, its half-budget prompts outperform the non-adaptive baseline's full-budget prompts in joint goal accuracy on new dialogues from services seen and unseen during search. Overall, our findings highlight the potential of adaptive feedback allocation to improve both the effectiveness and rollout-budget efficiency of reflective prompt optimization.

---


### 319. [RoPE at the End of Its Rope? Theory, Diagnosis, and Mitigation of Long-Context Failures](https://arxiv.org/abs/2609.39929)

**<font color=#1a73e8>作者：</font>** Yuyang Wu, Yufeng Du, Hao Peng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context failures of RoPE-based language models can arise from RoPE's intrinsic tradeoff between maintaining stable token preferences and distinguishing nearby positions. Determining which weakness to address, and how, requires a more precise characterization of RoPE's behavior in trained models across context lengths. We address a key limitation of prior theory by allowing unequal query-key scales across RoPE frequencies, which aligns well with practical empirical observations. Our theory makes both vulnerabilities measurable for individual heads and inputs, and quantifies how high-frequency components support positional sensitivity while potentially disrupting semantic stability. We also derive a theoretical context-length bound beyond which, under specified conditions, a fixed attention-score comparison cannot jointly avoid semantic reversal and positional insensitivity. Guided by our fresh theoretical insights, we introduce RoPE Profiler, a lightweight, plug-and-play diagnostic toolkit that augments existing evaluations with zero additional forward passes by reusing cached query and key activations. Reusing activations collected during evaluation, the toolkit incurs little overhead. It supplements standard benchmark scores with two diagnostic scores that reveal semantic and positional weaknesses and help users prioritize which aspect to address. Crucially, our evaluations across 49 long-context task settings reveal a distinct pattern where reasoning tasks predominantly suffer from semantic reversal, whereas retrieval tasks are primarily vulnerable to positional insensitivity. Guided by our theory and diagnostic profiles, targeted high-frequency rescaling achieves immediate gains without additional training, improving task accuracy by up to 20 percentage points on Qwen3-8B and 25 percentage points on Llama-3.1-8B-Instruct.

---


### 320. [ConflictGuide: AutoResearch Improves When Competing Behaviors Are Made Visible](https://arxiv.org/abs/2609.39933)

**<font color=#1a73e8>作者：</font>** Binqian Xu, Qiran Zou, Xiangbo Shu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When designing machine learning models, desirable properties are often in tension: improving one behavior can impair another, so task progress can depend on alleviating the conflict. LLM-based AutoResearch systems, which iteratively edit model code and retain edits based on scalar task-performance feedback, have largely ignored this trade-off. We find that scalar feedback supports broad exploration early in search, but it does not reveal how edits affect competing behaviors. In matched-budget experiments, introducing competing-behavior feedback as task gains diminish increases the share of proposals that improve both behaviors and sustains progress beyond scalar-only plateaus. Obtaining this feedback for a given model requires identifying its competing behaviors and designing probes to measure them. To make competing-behavior feedback actionable, we introduce ConflictGuide. Its reusable ConflictGuide-Skill combines a literature-grounded taxonomy with model-specific evidence to identify competing behaviors and specify probes for a code agent to implement as metrics. Evolution proceeds in two stages: Stage I explores with task feedback; Stage II uses probe feedback to steer proposals toward conflict alleviation and retains marginal-gain edits only when probes indicate sufficient alleviation. Across five diverse model families, ConflictGuide reduces task and conflict-related errors by up to 28% and 14%, respectively, relative to scalar-only AutoResearch, with gains extending to other code agents.

---


### 321. [LEAP: Learned Block-wise Evidence Retrieval for Long Audio-Video Perception](https://arxiv.org/abs/2609.39938)

**<font color=#1a73e8>作者：</font>** Juyi Lin, Zhiqiang Lao, Jiali Cui 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hour-scale audio-visual question answering is constrained by a context dilemma: dense whole-recording encoding rapidly exhausts context limits, whereas uniform temporal compression severely dilutes fine-grained acoustic and visual evidence. We introduce LEAP, a framework where the model retrieves its own evidence without placing the whole recording in one context. LEAP divides a recording into fixed-duration blocks, applying a lightweight localization pass to each block to score short candidate windows. The highest-ranked windows are pooled and re-encoded in a single bounded answer pass. Consequently, the answer input and peak context remain independent of the recording duration. By decoupling evidence localization from reasoning, our framework can localize candidate temporal windows over pre-computed transcripts without decoding media frames, while preserving fine-grained visual and non-speech evidence by routing the final answering pass over raw audio-visual streams. LEAP trains both stages: a localization LoRA improves the selected windows, and an answer LoRA improves the answers read from the same windows. The block grid natively supports causal queries, enabling LEAP to support streaming inference without streaming-specific training. Across several AVQA benchmarks, LEAP improves over the Qwen3-Omni-30B-A3B baseline by 4.5-16.8%, and transfers to a second omni-modal backbone, MiniCPM-o 4.5, surpassing its published results by 3.1-13.0%.

---


### 322. [Learning to Reason with Compressed Context: Ground-Truth-Free Adaptation of OmniLLMs via Self-Distillation](https://arxiv.org/abs/2609.39953)

**<font color=#1a73e8>作者：</font>** Jianghao Wang, Ke Meng, Jian Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models (OmniLLMs) enable unified audio-video understanding, but their long multimodal token sequences make deployment computationally expensive. Token compression reduces this cost, yet aggressive compression often lowers accuracy. Existing works predominantly focus on designing better compression mechanisms; however, adapting the underlying language model to reason effectively over the remaining compressed context remains under-explored. To address this, we propose CAFD (Compressed-Context Adaptation via Full-Context Distillation), a ground-truth-free self-distillation framework that adapts OmniLLMs to fixed compression pipelines without requiring reference answers, rationales, or correctness rewards. CAFD leverages the full-token view of the same multimodal sample as a source of privileged information: a full-context self-teacher provides soft target supervision to a compressed-context student along the student's on-policy trajectory. Evaluated on Qwen2.5-Omni-7B across five audio-video benchmarks, five compression pipelines, and five deployment budgets, CAFD demonstrates consistent gains, improving 120 out of 125 conditions with an average accuracy boost of 1.44 points and recovering 26.9% of the accuracy gap on average. These results demonstrate that the proposed ground-truth-free adaptation offers an effective and practical route to improving the accuracy-efficiency trade-off in deployed OmniLLMs.

---


### 323. [Better Deck or Different Judge? Evaluating Agentic Harness Gains in Corporate and Investment Banking](https://arxiv.org/abs/2609.39958)

**<font color=#1a73e8>作者：</font>** Ludovic Gibert, Matis Despujols, Andre-Louis Rochet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Corporate and investment banking teams use presentations to support credit decisions and advise clients on financing and transactions. Producing these decks requires reconciling financial data, tracing sources and turning analysis into a recommendation. We retrospectively study the development of an agentic harness combining a 27B language model, financial calculations, narrative templates and validation checks. LLM judges guide engineering changes and assess the resulting decks, raising the question of whether higher scores reflect better documents or changes in grading. In shared-session text-only grading with template markers removed, five judges score the complete system 20.4 to 33.6 points out of 95 above the same model generating directly from a short prompt. Every judge scores the system higher on all seventeen development deliverables. Margins against direct Opus generation from a short prompt range from -4.7 to +0.8 points. Judges agree on broad progress across development rounds but agree less on final-deck rankings than on pooled scores. Repeated grading also shifts scores on unchanged decks, making small improvements difficult to distinguish from judge variability.

---


### 324. [What Limits Recursive Reasoning Models: Optimization, Architecture and Test-Time Scaling](https://arxiv.org/abs/2609.39967)

**<font color=#1a73e8>作者：</font>** Yuliana Shakhvalieva, Dmitrii Kharchev, Viacheslav Bezrukov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive reasoning models apply a small shared Transformer block many times to refine a latent state. This gives them large effective depth with few parameters and makes them strong on algorithmic tasks. Such compact solvers are natural candidates for tools that an LLM can call on narrow algorithmic subproblems. However, existing models such as HRM, TRM and URM differ in architecture, gradient propagation and training procedure simultaneously. This makes it hard to tell what drives their performance, and their optimization is still poorly understood and often unstable. In this work we address both of these gaps. First, we study these questions under a unified experimental pipeline spanning six algorithmic domains. Individual controlled ablations are performed on representative domains, while the resulting recipe is evaluated across the full suite. The study reveals a surprisingly simple recipe for stable and generalizable recursive reasoning: an intermediate gradient horizon, large physical batches and controlled updates of the recurrent state. An explicit hierarchical architecture is not needed. Second, we combine these findings into a stable 13.6M-parameter model that achieves the strongest overall performance among the evaluated recursive baselines, with particularly large gains on out-of-distribution generalization. It raises Arithmetic OOD accuracy to 71.2%, from 36.2% for the strongest baseline, while reaching 98.41% on Sudoku and 59.5% pass@2 on ARC-AGI-1. Our results show that, within the recursive architectures studied here, performance depends strongly on how recurrence is optimized and stabilized. More broadly, it shows how AI systems can be improved by optimizing their components one at a time.

---


### 325. [UBTree: Parallel Tree Drafting via Unigram and Bigram Models for Speculative Decoding](https://arxiv.org/abs/2609.39972)

**<font color=#1a73e8>作者：</font>** Chumeng Liang, Linxuan Wang, Xinyu Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates language model inference by verifying multiple draft tokens in a single target-model pass. Recent parallel drafters have achieved breakthrough performance in frontier production models, but their effectiveness deteriorates as the entropy of target distributions increases due to insufficient draft diversity. To overcome this bottleneck without sacrificing parallelism, we introduce UBTree, a parallel drafter that couples a Unigram proposer with a Bigram selector to construct drafting Trees. The unigram proposer is trained with the standard cross-entropy objective to generate candidate tokens independently for each position, while a lightweight bigram selector predicts transition scores between adjacent candidate pairs. Unlike the proposer, the selector is trained with a renormalized KL objective on high-temperature data. This tree-native training broadens the supervision beyond the greedy path, encouraging plausible alternative branches that improve the chance of accepting additional tokens during tree verification. Across seven standardized benchmarks with Qwen3-4B and Qwen3-8B, UBTree achieves an average speedup of $5.84$--$6.94\times$ over autoregressive decoding and outperforms DARTree in all 28 comparisons. Production-scale evaluation further demonstrates UBTree's advantage over frontier baselines such as DSpark.

---


### 326. [Mid-Harness: Scaling Actions Between Model and Harness for Terminal Agents](https://arxiv.org/abs/2609.39982)

**<font color=#1a73e8>作者：</font>** Minki Kang, Ryo Hachiuma, Shaokun Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Terminal agents act through stochastic model generations, yet the ability to generate a useful action does not ensure its reliable execution. A poor command (e.g., wrong package install) can change the environment in ways that hinder subsequent progress, even when the model could generate a better alternative. We investigate whether allocating test-time compute at the model-harness boundary can improve action reliability and trajectory success, and what makes this allocation effective. To study these questions, we introduce Mid-Harness, which samples and verifies candidate actions before forwarding one for execution, while keeping the generator and harness unchanged. With a TMAX-9B generator, more action sampling yields little benefit under weak verification, whereas a capable verifier can exploit useful alternatives from the same generator. On TerminalBench-Lite, a GPT-5.6 Sol verifier raises Pass@1 from 50.00% for the base agent to 68.03% with 8 sampled actions. When the same TMAX-9B model serves as the verifier, pairwise verification performs best among the evaluated verification mechanisms. Distilling responses from the stronger verifier into TMAX-9B further improves Pass@1, while leaving the action generator unchanged. With TMAX-9B on TerminalBench-Lite, combining action and trajectory scaling reaches higher success at lower estimated token cost than generating more trajectories alone. Mid-Harness also improves performance across additional models, benchmarks, and harnesses. These findings identify action scaling as a promising target for test-time compute scaling in terminal agents.

---


### 327. [What Can Component-Replacement Evidence Establish? A Critical Scoping Review of Local Decisions in LLM Agents](https://arxiv.org/abs/2609.39989)

**<font color=#1a73e8>作者：</font>** Shuyang Zhang, Jianshuo Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background. A component replacement in a language-model agent changes an execution trajectory, potentially altering later observations, resource use, and recovery opportunities. Different evidence is needed to assess its task-level benefit and the contribution of local decision quality. Methods. This critical scoping review maps 348 studies and examines 90 comparison records: 88 from 40 included studies and two from supplementary studies. Eight purposively selected cases structure the synthesis around the replaced decision, executed conditions, measurement comparability, controls, and remaining explanations. Results. Of 222 studies reporting local decision metrics, 142 also report measured task endpoints and 49 report proxies. These counts identify studies that report both types of measurement, without establishing that the measurements come from matched comparisons. Outcome Monitors reports a package-level completion gain whose attribution to detector quality remains limited; First-chunk selection reports a local improvement assessed against an offline proxy endpoint; Evidence-Carrying Termination reports fewer premature unsupported terminations and completion non-inferiority, without establishing completion superiority. Cross-case analysis identifies three candidate mechanisms involving recovery and disruption, intervention timing, and downstream use. Attribution and deployment depend on the comparison controls, label definitions, and information available to the controller. Conclusions. The review distinguishes the task-level benefit of a component replacement from the contribution of local decision quality and derives eight claim-specific reporting items. Neither online execution nor simultaneous gains in local and task metrics alone establish that better local decisions explain the task-level gain.

---


### 328. [Who Verifies the Graph? Misspecification Attacks on Causal Action Verification for Language Agents](https://arxiv.org/abs/2609.40027)

**<font color=#1a73e8>作者：</font>** Fabio Rovai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Causal action verifiers gate an agent's state-changing tool calls by checking whether each proposed intervention is identifiable against a committed action-state graph, and they issue a certificate that carries the identification argument and a one-sided lower confidence bound. One such verifier, CIVeX, reports zero false executions on a confounded tool-use benchmark. We red-team it by corrupting only the committed graph. Omitting a single bidirected edge takes it from zero false executions to 15.3% at the benchmark's published confounding strength, with 91% of its executions harmful and utility falling from +2.27 to +0.35. Reversing one arrowhead, so that a mediator is committed as a confounder, gives 48.9% false executions and no correct ones. Every one of these actions carries an internally valid certificate. An attestation step that tests each observationally certified execution against a bounded randomised sample detected both attacks, with 2 false alarms in 555 executions on a truthful graph; refusing what fails the test, or cannot be tested, gave zero false executions in every setting we measured. It does not restore beneficial execution: at the published strength 97.1% of beneficial actions are still never executed, because the same misspecification rejects them before attestation runs. Those rejections carry certificates too, and auditing them works, but its cost scales with the number of rejections rather than the number of executions. Recovering safety costs 127 experiments per 1,050 actions; recovering the lost value costs 614 more, at which point the audited verifier makes the honest graph's decisions on every instance and spends exactly its experiment budget. An audit that inspects only executions protects against wrongful action. Wrongful inaction has to be paid for separately.

---


### 329. [OPTS-TTPO: Enhancing Finite-Sample Policy-Gradient Learning with Tree Search](https://arxiv.org/abs/2609.40035)

**<font color=#1a73e8>作者：</font>** Junyu Lu, Shichao Weng, Zhiqiang Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The policy-gradient theorem gives the exact gradient under the current policy, but finite on-policy samples may miss rare high-return trajectories. We study whether tree search improves their coverage within a fixed budget while controlling gradient bias. We introduce On-Policy Parallel Tree Search (OPTS) and Tree Trajectory Policy Optimization (TTPO) using on-policy tree trajectories, which sample new suffixes from the current policy at visited states. This needs no action-distribution correction, although branching changes state visitation. Our Branch Aggregation Lemma shows that branch-weighted tree statistics recover chain expectations when branch choices and weights are fixed before outgoing transitions are sampled. OPTS selects expansion states using estimated performance differences. Under deterministic dynamics, exact values, and max-backup advantages, the induced search policy's expected return improves monotonically with the budget. We bound the gradient bias from adaptive expansion and show that max backup assigns prefix credit to actions leading to better discovered suffixes. Against a finite chain reference, TTPG's measured bias stays near its no-branching level, while NaivePG's bias grows from 0.1251 to 0.4884. At matched budgets, reward- and value-guided OPTS improve correct-answer coverage and majority-vote accuracy over independent sampling. At matched branch counts, OPTS + TTPG gains coverage with a modest bias increase relative to Fixed-branch + TTPG. Under matched interaction or rollout budgets, OPTS-TTPO improves MuJoCo tail returns over PPO by up to 28.6%, achieves a 34-22-1 win-loss-tie record against PPO on Atari-57 under the last-100-log mean-return metric, and improves micro-averaged avg@32 and pass@32 over PPO across all four Qwen3 models.

---


### 330. [CoEvoWhen: Policy-Tool Coevolution for Ultra-Long Video Temporal Grounding](https://arxiv.org/abs/2609.40048)

**<font color=#1a73e8>作者：</font>** Yiduo Jia, Muzhi Zhu, Jinchuan Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra-long video temporal grounding requires balancing long-range evidence search with fine-grained event understanding under a limited visual budget, yet existing agentic methods still rely largely on predefined policies and tool capabilities. Motivated by this, we propose a novel policy-tool coevolution framework that jointly evolves high-level policies and executable media tools from the agentic reasoning trajectories of a VLM, forming a reusable skill without updating model parameters. During evolution, an external skill updater distills transferable task experience in long-video temporal grounding, accordingly refining the orchestration of long-range image-based and fine-grained video-based observations. Alongside these policy updates, the updater employs its coding capabilities to upgrade existing tools or create new ones, adapting the tools to long-video evidence acquisition. Equipped with the evolved skill, the VLM autonomously orchestrates tools under the guidance of the evolved policy, coordinating image and video observations for agentic inference without relying on a separate, stronger planning model. Extensive experiments spanning five benchmarks and three VLMs show that policy-tool coevolution consistently improves temporal grounding accuracy in ultra-long videos while reducing visual token cost at inference, and that the evolved skill yields substantial performance gains on general long-video QA without additional task-specific evolution, demonstrating the effectiveness and generalizability of our framework for long-video understanding.

---


### 331. [Less Data, Better Timing: Student-Curriculum Coupling for VLM On-Policy Distillation in Temporal Video Grounding](https://arxiv.org/abs/2609.40055)

**<font color=#1a73e8>作者：</font>** Jiacheng Qiu, Yunsoo Kim, Ruichen Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) provides dense supervision directly on student-generated trajectories, making it an effective post-training strategy for vision-language models in temporal video grounding (TVG). However, existing pipelines typically construct the training curriculum from a fixed teacher and the initial student state, implicitly assuming that selected examples retain positive supervision value throughout optimization. We show that supervision trustworthiness and supervision necessity are distinct yet coupled: the former concerns target credibility, while the latter varies with the student's current task competence; together, they shape supervision value. Building on this coupled view, we introduce Student-Curriculum Coupling (SCC), a closed-loop framework in which a compact Anchor-Frontier curriculum defines the candidate supervision space and the evolving student dynamically determines its active subset. Supervision can therefore be activated, suspended, or reactivated as competence changes, concentrating teacher computation and optimization on current task-level deficits. Across three TVG benchmarks, SCC achieves a 5.1% relative improvement in mean recall over Video-OPD on its original curriculum, while using 60.0% fewer training examples and reducing training time by 50.4%. Ablations support the complementary roles of capability-structured curriculum design and student-dependent supervision in achieving these gains. Together, these results establish SCC as a data- and compute-efficient framework for TVG post-training, delivering stronger temporal grounding by aligning trustworthy supervision with the student's evolving learning needs.

---


### 332. [LARC: Low-Rank Adaptive Residual Connections for Learning in Frozen Models](https://arxiv.org/abs/2609.40063)

**<font color=#1a73e8>作者：</font>** Junyi Zou, Avrova Donz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptive Residual Connections (LARC) give a frozen model a compact numerical state that can learn from feedback. The map $h+BAh$ adds a low-rank correction to a hidden representation. A slow state $\rho$ learns starting factors across tasks; a private fast state $\Phi$ copies them, changes with feedback, and resets to the trained initialization. This report specifies an input-side realization of the numerical policy carrier in Memory-Mediated Learning Architecture and examines its factor-space dynamics and learning lifetime. We study a rank-4 input residual with 12,288 trainable parameters on a frozen MiniCPM5-1B-SFT substrate. In a four-candidate program-selection task, two feedback-gradient steps reduce expected query execution error by 24.65 and 36.65 percentage points relative to resetting to the respective trained static and post-adaptation initializations. These development results cover 16 parameter groups and three paired training seeds. A direct support-loss selection rule is much more accurate, reaching 0.78125% error. In a repository-balanced chronological replay of public continuous-integration jobs, retaining online updates raises half-Brier loss from 0.1274 to 0.1808. A fixed follow-up intervention records same-batch non-descent and inconsistent future benefit from shrinking updates. Together, the algebra and measurements distinguish residual capacity, adaptation relative to a starting point, and usefulness on later decisions.

---


### 333. [Conversational Capture: A Trajectory-Level Framework for Evaluating Generative Engine Optimization in Multi-turn Human-Agent Interaction](https://arxiv.org/abs/2609.40069)

**<font color=#1a73e8>作者：</font>** Junwei Yu, Jieyu Zhou, Mufeng Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative Engine Optimization (GEO) shapes content to increase its likelihood of being cited by answer engines built on retrieval-augmented large language models. GEO is typically evaluated as a single-turn property: for a fixed query, an evaluator measures a source's visibility in one answer. We argue that the single answer is an inadequate unit of analysis. Human-agent information seeking forms a closed loop: the agent's answer changes the user's beliefs and therefore the next question, which in turn determines what the agent retrieves. We introduce conversational capture, a phenomenon in which a source cited early becomes substantially more likely to be cited again. Capture operates through a machine-side channel, history-conditioned retrieval, and a human-side channel, follow-up questions directed toward the captured source. We formalize the interaction as a two-layer closed-loop system and derive trajectory-level constructs: cumulative conversational visibility; a direct/feedback decomposition of trajectory gain; a nested split of the feedback term into machine-side and human-side channels; a capture coefficient; a compounding ratio; and a misranking diagnostic. Using reinforcement-process (Pólya-urn) theory, we prove that the feedback term is zero under single-turn evaluation and that GEO's cumulative payoff grows superlinearly with conversation length while capture develops. A model-derived illustration shows that the feedback term can exceed the direct term, the compounding ratio exceeds two within ten turns, and single-turn and trajectory rankings agree only weakly (Kendall's $\tau = 0.4$). We connect the human channel to information foraging, trust calibration, and Bayesian persuasion, and discuss design implications for answer engines.

---


### 334. [Inference Auctions](https://arxiv.org/abs/2609.40070)

**<font color=#1a73e8>作者：</font>** Keegan Harris, Siddharth Prasad, Asher Trockman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When inference demand exceeds available compute capacity, model providers must decide which requests should be served first. Users have different tolerances for delay from an LLM API, but current priority pricing schemes compress these differences into coarse fixed-price service tiers. We design an inference auction that allows users to bid for faster service. Our auction allocates priority in an economically efficient way without sacrificing latency, and we develop fast algorithms for implementing prices that incentivize truthful bidding. We also design an autobidding agent for our inference auction, where users specify an inference budget and the autobidder dynamically adjusts its bids over time to maximize user utility subject to the budget constraint. Experiments validate the practicality of our auction: it increases system welfare while maintaining the cache utilization and latency advantages of SGLang, a state-of-the-art inference serving framework.

---


### 335. [LongEmo: Towards Emotion Understanding and Reasoning in Long Videos](https://arxiv.org/abs/2609.40079)

**<font color=#1a73e8>作者：</font>** Shuo Zhang, Yifan Zhou, Han Wang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent Multimodal Large Language Models (MLLMs) have shown promise in affective computing, their reasoning capabilities are largely confined to short video clips with limited interactions. However, real-world emotions are not merely isolated instantaneous reactions but dynamic and cumulative processes deeply shaped by past experiences and ongoing events. To bridge this gap, we introduce LongEmoBench, a benchmark dedicated to emotion understanding and reasoning in long videos. It assesses progressive capabilities scaling from continuous scene interactions to complex episodic developments. Furthermore, we propose LongEmo, a novel memory-augmented agentic framework designed to tackle the immense challenges of long-range affective reasoning. LongEmo processes continuous video streams to construct an Event Memory Graph, explicitly modeling long-range dependencies and capturing emotional dynamics across discrete events. Given a question, the agent retrieves a query-relevant event stream from the graph, iteratively integrating multimodal memories and relational dependencies to deduce the final answer. Extensive evaluations of 17 representative methods reveal that they struggle significantly with emotion understanding and reasoning in long videos. In contrast, LongEmo achieves state-of-the-art performance, demonstrating the efficacy of its event-centric memory architecture.

---


### 336. [Replay on Demand: An Emergent Curriculum for Balancing Adaptation and Forgetting in Continued Pretraining](https://arxiv.org/abs/2609.40089)

**<font color=#1a73e8>作者：</font>** Lukas Thede, Shengzhuang Chen, Stefan Winzeck 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continued pretraining enables language models to adapt to new domains and knowledge, but often at the cost of forgetting previously acquired capabilities. Replay can mitigate this trade-off, but fixed replay mixtures allocate training independently of the model's actual retention needs. We introduce Replay on Demand (RoD), which instead derives the replay allocation from the model's learning dynamics. RoD jointly prioritizes adaptation samples by their remaining learning potential and replay samples by their observed forgetting. Their competition for a shared training budget yields an online curriculum that determines what to train on at each step. Across models, scales, and adaptation domains, RoD reaches or improves upon the adaptation-forgetting frontier of tuned fixed-replay baselines and model merging without prescribing a replay allocation in advance. Replay concentrates on sources that are more vulnerable to forgetting and dynamically increases and redistributes as forgetting emerges during training. Together, our results show that replay can be allocated online from the model's evolving state, targeting what is needed, when it is needed.

---


### 337. [AutoDataBench: A Data-centric Testbed for Accelerating Auto Research](https://arxiv.org/abs/2609.40097)

**<font color=#1a73e8>作者：</font>** Ruifeng Yuan, Yizhi Li, Yaxin Du 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing auto-research benchmarks often entangle multiple sources of improvement, including training frameworks, hyperparameters, compute budgets, and data, making it difficult to attribute why one frontier agent outperforms another to specific research capabilities. In this work, we isolate and systematically evaluate Data Intelligence: an agent's ability to understand, manipulate, and improve the data that shapes model capabilities. We introduce AutoDataBench, a controlled testbed built on a conceptual framework of data intelligence spanning data diagnosis, data organization, and data construction, instantiated through three highly curated optimization tasks while holding non-data factors fixed. Across tool use, retrieval, and knowledge injection, we evaluate frontier LLMs' ability to improve training data through iterative experimentation under task-specific resource budgets. Beyond optimization performance, we ask: do LLMs understand what their data interventions do? We compare predictions made before training with observed outcomes to seek evidence of data-effect reasoning beyond trial and error, and explore whether iterative feedback helps LLMs better understand how changes to training data affect model performance. Finally, we show that reusing AutoDataBench trajectories for mid-training improves downstream coding performance, highlighting its value in both evaluating data intelligence and generating high-quality training data. Code and resources are available at this https URL.

---


### 338. [JuryFlow: Disagreement-Guided Human-in-the-Loop Multi-Agent Evaluation](https://arxiv.org/abs/2609.40103)

**<font color=#1a73e8>作者：</font>** Mufeng Yang, Junwei Yu, Yepeng Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as automated judges for AI-generated content, yet a single judge is unreliable and even a panel of judges leaves a hard residue: when judges disagree, majority voting discards the conflict instead of resolving it. We present JuryFlow, a disagreement-guided, human-in-the-loop multi-agent evaluation framework that treats inter-judge disagreement not as noise to be averaged away, but as a precise, claim-level signal indicating where an evaluation is uncertain. JuryFlow decomposes each candidate response into atomic claims, has a panel of heterogeneous judges assign per-claim verdicts, and builds a disagreement graph whose nodes are scored by verdict entropy and whose edges encode structural similarity between claims. A human acts as a structural guide, selecting which disagreement to resolve through a single, minimal intervention rather than re-labeling the response, after which the focal claim is re-evaluated, the correction propagates along graph edges and to historically similar cases, and is crystallized into reusable rubric entries that all judges inherit, making the evaluator progressively self-refining. To enable large-scale, reproducible benchmarking without human studies, we evaluate JuryFlow in an automatic configuration in which focal selection is made by entropy ranking. On MT-Bench and LLMBar, JuryFlow improves agreement with gold labels over single-judge and majority-vote panel baselines, and ablations isolate the contributions of disagreement-targeted re-evaluation, propagation, and rubric induction. We contribute (1) a human-in-the-loop paradigm that recasts the human from labeler to structural guide, (2) the JuryFlow framework operationalizing it through a disagreement graph, focal re-evaluation, and closed-loop rubric induction, and (3) an evaluation protocol with ablations that isolate where the gains originate.

---


### 339. [OverdoseMoE: A Multi-Expert Framework for Opioid Overdose Risk Prediction](https://arxiv.org/abs/2609.40108)

**<font color=#1a73e8>作者：</font>** Mingchen Li, Rohan Pandey, Junhui Qian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Opioid overdose remains a major clinical and public health burden, highlighting the need for scalable approaches to identify patients at high risk. Here, we investigate diagnosis-specific adaptation for 180-day opioid overdose risk prediction from patients' preceding one-year longitudinal ICD histories. We develop OODMAMBA and OODQWEN through continued pretraining on longitudinal diagnostic sequences followed by task-specific fine-tuning. Building on the stronger Qwen-based predictors, we further propose OVERDOSEMOE, a multi-expert framework that integrates models of different scales using complementary expert-weighting strategies. Diagnosis-specific adaptation consistently improved predictive performance over general-purpose language-model baselines, with OODQWEN achieving an AUPRC of 24.47 and an AUROC of 68.56. OVERDOSEMOE further improved discrimination and precision, achieving an AUPRC of 25.17 and an AUROC of 69.49 while outperforming the strongest single-model baselines. Among patients ranked in the top 5% of predicted risk, OVERDOSEMOE identified substantially enriched overdose risk, achieving a PPV of 25.38% while retaining meaningful recall. Evaluation on an independent MIMIC-IV cohort further demonstrated cross-cohort robustness, with complementary weighting strategies showing advantages across different performance measures. These findings demonstrate that diagnosis-specific language-model adaptation combined with multi-expert integration can improve opioid overdose risk stratification and support more robust prediction across heterogeneous electronic health record populations.

---


### 340. [Agent Error Dataset: Scaling 50,000 Error--Diagnosis Pairs for Failure Analysis and Error-Aware Post-Training](https://arxiv.org/abs/2609.40111)

**<font color=#1a73e8>作者：</font>** Kunlun Zhu, Xuyan Ye, Yibo Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An unsuccessful LLM agent rollout contains more information than its final reward: the observations available to the agent, the actions it chose, and the environment's responses. Reusing this experience for learning requires identifying a decision to revise and testing a concrete alternative. We introduce the Agent Error Dataset (AED), comprising 50,228 error-diagnosis pairs from 9,961 source tasks across 33 environments, 19 harness families, and 23 policy models in text-based agent systems. We retain source traces and execution metadata to support cross-setting failure analysis and re-diagnosis without repeating the original rollout. Our five-stage Agentic Error-to-Training (AET) pipeline collects natural failures, generates diagnoses and proposed corrections, and checks them against recorded evidence. Where replay is supported, we compare corrections with original-action retries from the same checkpoint under matched execution settings. We then construct separate training views for diagnosis and actor recovery. Across 3,062 matched replay pairs, first-proposal corrections raise verifier pass rates from 18.4% to 51.1%, a gain of 32.7 percentage points. Using a separately frozen diagnosis release, full-diagnosis fine-tuning on 1,656 source tasks raises Qwen3-8B's exact-step agreement with internal teacher labels from 47.2% to 63.6%, averaged over three seeds on a 943-case holdout. The strongest prompted reference in this comparison scores 54.7%, and mean agreement improves at each of four increasing training-set sizes. In a single-seed comparison of actor-training recipes, action-only repair training scores 6.67 percentage points higher on WebShop-lite than success-only training.

---


### 341. [Persistent Context Graphs for Efficient Memory Compaction in LLM Agents](https://arxiv.org/abs/2609.40118)

**<font color=#1a73e8>作者：</font>** Jingbo Yang, Kwei-Herng Lai, Xiaowen Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM capabilities advance, agents are tackling increasingly complex tasks over longer horizons. Their growing interaction histories make memory compaction essential for staying within context windows and reducing prefill cost. Existing methods summarize the history or compress its KV cache, often adding model computation to preserve information for future requests. A new user request can change which history matters, but reassessing that history with the model requires re-encoding it if the KV cache has expired. Past attention provides signals of historical importance and dependencies between messages, while relevance to the current task must be assessed using the new user request. We introduce ReCAP, a memory compaction method that stores attention-derived importance scores and dependency links in a lightweight, persistent context graph. For each new request, ReCAP combines stored importance with relevance cues from the request and follows dependency links to select messages and their supporting context, without additional model calls for selection. Compared with Codex's default summarization-based compaction, ReCAP reduces estimated latency for compaction and cold restoration by approximately 95% on both Qwen3-Coder and gpt-oss. It also roughly halves the historical context per call on SWE-Together at comparable task quality and improves accuracy on the code tasks of Lost-in-Conversation over full history by 19.8 and 41.2 points.

---


### 342. [On the (In)effectiveness of AMR Augmentation for Large Language Models](https://arxiv.org/abs/2609.40121)

**<font color=#1a73e8>作者：</font>** Hoa Quynh Nhung Nguyen, Jacopo Staiano, Michael Sullivan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Abstract Meaning Representation (AMR) has historically improved performance on a range of NLP tasks, the benefit---or lack thereof---of AMR augmentation for modern LLMs is thus far unclear. In this paper, we attempt to reproduce recent work that reported substantial downstream gains from AMR augmentation, finding that these are likely due to specific choices in the experimental settings used: using a consistent and unified protocol for hyperparameter selection, we observe that text-only baselines consistently match or exceed the performance of AMR-augmented models. To investigate this null result, we introduce a perplexity-based probe measuring the degree to which AMR provides an LLM with supplemental relational knowledge not already available to the model. We find that AMR augmentation does not help LLMs improve their understanding of relational content in the sentence, indicating that augmenting these models with AMR offers no clear benefit on downstream tasks.

---


### 343. [Debias It Yourself: Teaching LLMs Cognitive Bias Mitigation Interventions](https://arxiv.org/abs/2609.40124)

**<font color=#1a73e8>作者：</font>** Chahat Raj, Sina Mansouri, Aylin Caliskan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bias has long been studied in social psychology and cognitive science, where decades of research have produced a body of validated interventions that reduce stereotypical thinking and prejudiced responses in humans. We propose Debias It Yourself (DIY), a cognitively grounded framework that translates five such interventions into debiasing procedures for large language models and delivers them through three established paradigms: Show (in-context examples), Train (instruction tuning), and Revise (guided self-revision). Across three models, five bias benchmarks, eleven debiasing baselines, and three reasoning benchmarks, Train+Revise and Revise alone attain the top two average ranks, lead the bias-reasoning tradeoff (mean bias as low as 2% at 90% reasoning accuracy), and reduce bias on unseen dimensions by up to 14.8%. Our code and data are publicly available.

---


### 344. [Learning Functional Subspaces for Neural Network Compression](https://arxiv.org/abs/2609.40127)

**<font color=#1a73e8>作者：</font>** Massimo Bini, Anders Christensen, Stephan Alaniz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern transformers pair impressive capabilities with substantial memory and compute demands. Low-rank weight factorization reduces both while keeping the matrices dense, and thus efficient on standard hardware. Existing methods, however, choose the subspace to remove from each weight matrix with local closed-form criteria: activation energy, layer-wise reconstruction error, or a quadratic approximation of the loss. These criteria ignore how errors propagate through the network, so at high compression the errors compound with depth and performance collapses. We introduce Learnable Subspace Projections (LSP), which instead learns the subspaces to discard end-to-end. Each linear layer, or tied group of layers that read the same activations, is assigned an orthogonal projector. All projectors are optimized jointly against a global objective--the KL divergence to the dense model's output distribution or the model's original training loss--while the pretrained weights remain frozen. Projectors are initialized from a whitened SVD truncation, and ranks are allocated by the output KL each projector induces per parameter saved. After training, the projectors merge into standard low-rank factors, with each tied group sharing one factor. In attention, this also lets the model cache one narrow latent in place of full keys and values. Across LLMs (OPT-125M/1.3B, Qwen3-4B, Llama-2-7B) and ViT-B/16, LSP outperforms baselines, and its advantage widens as compression increases. At -70% compression, LSP brings Llama-2-7B to 10.9 WikiText-2 perplexity and 42.2% mean zero-shot accuracy, versus 13.3 and 36.0% for the strongest baseline. The factorized model decodes up to 1.6x faster than the dense model at small batch sizes, and aching the shared latent shrinks the combined memory of weights and KV cache by 13.5x at a 128k-token context, versus at most 6.5x for untied baseline factorizations.

---


### 345. [From DNA Design to DNA Slimming: Auditable Agentic Discovery of a Deletion-Only Designer](https://arxiv.org/abs/2609.40143)

**<font color=#1a73e8>作者：</font>** Joel Shor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compact regulatory DNA can free up space in vector payloads, reduce synthesis and assay burden, and expose which sequence features drive predicted activity. Yet most model-based nucleic-acid designers optimize fixed-length sequences through substitutions; they do not ask which bases of an existing functional element can be removed while retaining predicted activity. We define the task of sequence slimming as selecting an exact-length, order-preserving subsequence while retaining activity. Modeled on the design benchmark NucleoBench, we propose a quantitative evaluation for slimming that balances sequence reduction with maintaining function. Each slimmer must return both the subsequence and its source indices, which can be used to verify that the slimmer obeyed task requirements. To our knowledge, this is the first dedicated benchmark of this deletion-only problem. The coding agent Empirical Research Assistant (ERA) then searched over executable designer programs. ERA received the task prompt and a successful substitution-only designer GrAdaBeam as a starting program, and it modified the designer to produce GRADASLIM. We report held-out evaluations for five transcription-factor binding targets, comparing random, greedy, and ERA-guided slimming at 400 and 100 bp. ERA has the highest mean in 9/10 settings. Paired bootstrap intervals for ERA minus greedy are above zero in all five 400-bp settings, below zero in one 100-bp setting, and overlap zero in the remaining four.

---


### 346. [From Spectra to Joint Schedules in LLM Pre-training: 3+3(+2) Scaling-Law Regimes](https://arxiv.org/abs/2609.40148)

**<font color=#1a73e8>作者：</font>** Yichen Wang, Fanghui Liu, Yudong Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Power-law learning curves are often treated as fixed properties of a model and its data, although learning-rate and batch-size schedules can change the observed loss. We study this dependence in noisy online SGD with linear random features. Conditional on the representation, an exact Volterra equation separates two response components: a forcing term that propagates unresolved target error and a memory kernel that propagates stochastic-error injections. We prove that either component follows a power law if and only if its cumulative weighted spectral mass has the corresponding low-spectrum scaling; individual eigenvalues and target coefficients need not obey coordinatewise power laws. Under a joint schedule, intrinsic time $T_t=\sum_{s<t}\eta_s$ controls optimization progress, while $r_t=B_t/\eta_t$ controls noise injection. Their interaction yields sharp conditions under which a schedule preserves, changes, or destroys the clean power law, together with a memory ceiling on noise reduction. The power-law random-feature model realizes this mechanism in $3+3(+2)$ propagation regimes with phase-dependent compute rates. Controlled nanoGPT experiments show that (1) learning-rate and batch-size schedules with matched $B/\eta$ paths are nearly equivalent in intrinsic time, (2) a forcing-memory surrogate accurately predicts loss across schedules, and (3) its fitted exponents across real-world datasets identify the regime of LLMs in $3+3(+2)$ map.

---


### 347. [Learning from Research: Toward Lifelong Agent Harness Evolution](https://arxiv.org/abs/2609.40169)

**<font color=#1a73e8>作者：</font>** Jingbo Yang, Kwei-Herng Lai, Xiaowen Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents are expected to solve increasingly complex tasks, creating a growing need for continual improvement. One promising approach is to evolve the agent harness, the software that governs tool use, memory management, and task execution, while keeping the underlying language model fixed. Recent methods automate this process by using a meta coding agent to modify the harness based on execution feedback. However, relying on that agent's existing knowledge and observed failures can restrict exploration and make adaptation reactive. Inspired by how human experts learn from the research literature for new solutions, we introduce ScholarEvolve, a framework that automatically draws on state-of-the-art research to guide harness evolution. ScholarEvolve organizes the harness evolution directions into functional modules and uses topic modeling to identify distinct improvement strategies for each module. It implements these strategies and evaluates their combinations to improve task performance. Moreover, the framework is designed to incorporate new publications over time, allowing research advances to drive proactive lifelong evolution. Experiments demonstrate improvements on AppWorld and Tau2-Bench. ScholarEvolve raises Qwen3.5-27B task goal completion from 49.6% to 63.6% on AppWorld Challenge, and raises GPT-5.4-mini pass@1 from 72.7% to 81.9% on Tau2-Bench Telecom.

---


### 348. [Provably Tractable NFA-Constrained Language Generation via HMMs](https://arxiv.org/abs/2609.40185)

**<font color=#1a73e8>作者：</font>** Jialiang Sun, Kuldeep Meel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Constrained generation aims to sample from language models (LMs) conditioned on hard constraints. Existing constrained-generation techniques for nondeterministic finite automaton (NFA) constraints either distort the distribution or sacrifice efficiency. Theoretically, this task reduces to counting the length-$n$ sequences accepted by an NFA (#NFA), and the exact #NFA problem is #P-complete. Recent work has shown that #NFA admits a fully polynomial randomized approximation scheme (FPRAS). Inspired by this result, we propose NFA-LM, a polynomial-time engine for NFA-constrained generation with theoretical guarantees under mild assumptions. Experiments show that NFA-LM efficiently generates high-quality outputs with theoretically bounded approximation error.

---


### 349. [Cheap to Draw, Expensive to Trust: Certifying Test-Time Scaling Curves](https://arxiv.org/abs/2609.40190)

**<font color=#1a73e8>作者：</font>** Sohail, Sarkar, Shakuntala Baichoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling several answers and keeping the one a verifier scores highest is one of the simplest ways to buy accuracy at test time. Its effect is reported as a scaling curve: accuracy against the number $k$ of sampled answers. The curve is cheap to draw and expensive to trust. A budget read off it is chosen after looking at every point, so only a band that covers all budgets at once protects the choice, and on a 100-question benchmark a fixed exact-binomial design needs 192,000 generated answers to certify 64 budgets to within $\pm1/32$ at 95%. Most of that cost pays for the wrong uncertainty. A benchmark is a fixed list of questions; at budget 64, about three quarters of the variance of a selected answer's correctness lies between questions, and an audit that revisits every question need not pay for it. We derive the minimax cost of certifying the whole curve, up to logarithmic factors. It has three parts: calibrating the tail of the score distribution, telling the questions apart, and within-question noise summed along the curve. At a single benchmark the last part sharpens to the variance of one answer's influence under the best allocation of answers to questions, which every valid audit pays and an audit that learns the allocation attains, up to a logarithm, as the precision grows. A paired audit built on an exponential inequality for two independent draws at the same question needs no pilot. On 185 held-out score pools it uses 0.74 times the answers of the cheapest competing certified audit at 64 budgets and 0.53 times at 1,024, and on a newly generated MMLU-Pro study it certified the curve with 79,133 answers, within 0.6% of what a cost law fitted beforehand predicted from the study's within-question variance. The same paths certify pass@$k$ and majority voting, and the bands extend to populations of questions and to answers that depend on earlier ones.

---


### 350. [SCB: SpeechConversationBench for Evaluating Multi-Turn Reasoning in Speech-to-Speech Models](https://arxiv.org/abs/2609.40198)

**<font color=#1a73e8>作者：</font>** Kanpat Vesessook, Saksorn Ruangtanusak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-to-speech systems must solve tasks whose requirements emerge across conversational turns. We introduce SpeechConversationBench (SCB), a focused evaluation of spoken mathematical reasoning using 103 sharded GSM8K problems. The framework compares the original problem delivered in one turn (full), its concatenated information shards delivered together (concat), and incremental spoken disclosure across turns (sharded). We report final-answer accuracy for four commercial speech systems and LEGO, a proprietary speech pipeline developed internally by the SCBX Innovation Lab team with explicit conversational context management. Relative to concat, sharded accuracy decreases by 5.0-25.3 percentage points across the four commercial systems. LEGO achieves 77.5 percent accuracy in all three conditions, compared with 76.6 percent sharded accuracy for GPT-4o Realtime. The two single-turn baselines distinguish sensitivity to problem reformulation from the additional challenges introduced by incremental spoken interaction.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-390](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
