# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**401-450**（第 9/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 401. [VAttnPO: Visual Attention-Guided Policy Optimization](https://arxiv.org/abs/2610.16735)

**<font color=#1a73e8>作者：</font>** Lihao Zheng, Zhenwei Shao, Zhou Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal reinforcement learning with verifiable rewards commonly assigns one sequence advantage to an entire response. This outcome-level signal distinguishes overall response quality but leaves changes in visual-evidence use across generated tokens implicit. We introduce VAttnPO (Visual Attention-Guided Policy Optimization), which uses answer-conditioned visual attention to refine token-level credit while preserving the verifier-derived trajectory-mean advantage. A frozen old policy constructs a visual reference by teacher forcing the known correct answer and produces a visual distribution for each rollout token. VAttnPO measures their agreement in visual-attention space using Jensen--Shannon divergence, rather than reading guidance from teacher output-token distributions or introducing an attention-matching objective. Trajectory centering, relative-position weighting, and credit balancing turn this agreement into a zero-mean, position-aware correction to the GRPO sequence advantage. Token intervention, visual-index permutation, and trajectory analysis provide diagnostic evidence linking this signal to model behavior, visual correspondence, and generation position. On Qwen3-VL-8B-Instruct, VAttnPO raises six-task image AVE from 70.97 with GRPO to 73.50 and scores higher on every reported structured, video, and MME metric. Gains over GRPO also hold on Qwen2.5-VL-7B-Instruct and InternVL3-8B-Instruct.

---


### 402. [FoveaTree: Information-Density Trees for Query-Guided Visual Token Pruning in Video Large Language Models](https://arxiv.org/abs/2610.16744)

**<font color=#1a73e8>作者：</font>** Zihan Meng, Weidong Chen, Dexiang Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video large language models (Video LLMs) encode each frame into hundreds of visual tokens, making video inference expensive. Existing methods reduce this cost through similarity-based merging or attention-based selection but face two challenges: Hierarchy-blind Pruning, which overlooks regional compressibility and can discard critical evidence, and Attention Drift, where positional effects and attention sinks shift text-to-vision attention away from task relevance. We propose FoveaTree, a two-stage, training-free visual-token pruning framework. First, Merge-Gain Density Estimation measures the feature distortion caused by regional merging and constructs a quadtree-derived density map to guide token dropping, merging, and retention. Second, Attention Tree Pruning uses the surviving units and inherited tree topology to refine text-to-vision attention in intermediate LLM layers, preserving relevant regional evidence while removing low-relevance content. We evaluate FoveaTree on InternVL3.5-8B and Qwen3-VL-8B across five video question-answering benchmarks and one captioning benchmark at 50%, 30%, and 10% visual-token retention. FoveaTree consistently achieves overall state-of-the-art performance across the evaluated settings, offering a strong accuracy-efficiency trade-off.

---


### 403. [Before Attention Sinks Form: Hidden-State Geometry Reveals and Modulates Their Formation](https://arxiv.org/abs/2610.16745)

**<font color=#1a73e8>作者：</font>** Fan Yang, Yue Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention sinks are usually studied after they have formed. We ask whether a measurable hidden-state change appears beforehand and whether changing that geometry alters what happens later. To remove network depth as a shortcut, we compare prompts in the same model and at the same layer. When sink timing varies across prompts, simple spectral summaries of the hidden states add information beyond current attention, with the clearest prompt-specific signal in a short window about two to three layers before sink formation. The predictive strength varies across cohorts, so we treat the spectrum as a readout of a pre-sink state change rather than a universal warning statistic. The signal is broader than one measured extreme activation. We then modify only the singular values of the post-layer hidden states after current attention has already been computed. These interventions change later sink behavior in Qwen2.5, GLM-Z1, and GPT-OSS relative to norm-matched random spectral perturbations. In Qwen2.5, the immediate suppressive effect is accompanied by a reduction in next-layer query--key preference for position~0, and the learned spectral directions remain stable when estimated from substantially less training data. Together, the results show that attention sinks are preceded by a short spectral reorganization of hidden states, and directly perturbing this geometry can causally alter subsequent sink formation.

---


### 404. [The Multilingual Artificial Hivemind: Do All LLMs Think Alike in Every Language?](https://arxiv.org/abs/2610.16755)

**<font color=#1a73e8>作者：</font>** Xaver Raphael Davey, Shubhra Mishra, Anton Adelöw 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text generated by Large Language Models (LLMs) often remains limited in diversity compared to that produced by humans. Recent advances demonstrate the presence of inter- and intra-model collapse in open-ended generation of English text, raising concerns about the long-term homogenization of LLM, and more importantly, human thought. However, our understanding of whether this homogenization extends to languages beyond English is limited. In this work, we investigate the role of language on output diversity. Specifically, we aim to understand whether multilingual LLM-generated text is also homogeneous, and whether this homogeneity matches what we observe in humans. Across 23 open-weight models and 13 languages, we find that the artificial hivemind effect is pervasive but uneven in its extent. The intra-model effect holds in three different embedding spaces and under a lexical metric that uses no embedding model, so it is not an artifact of how diversity is measured. The size of the homogenization gap is associated with a model's competence in a language, measured on a held-out translation benchmark, robustly across embedding spaces. Thus, we demonstrate a performance-diversity tradeoff in multilingual LLMs.

---


### 405. [Separating Prompt Harmfulness from Interaction Safety via Partial Generation](https://arxiv.org/abs/2610.16761)

**<font color=#1a73e8>作者：</font>** Ram Vikas Mishra, Shashank Aggarwal, Jahnavi Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based information systems need safety guardrails. Most guardrails classify the prompt alone. If the prompt looks harmful, the system rejects it before any answer is generated. This is costly. Many rejected prompts would have received a safe response. Users lose help they should have received from the information system. This cost grows as conversational and generative search becomes common. Prompt-level labels treat harm as a property of the query. But harm depends on what the model actually writes. Existing input-output guards do look at responses. But they judge a finished response, so the decision comes after full generation. However, we observe that safety of model interaction with the input prompt can be inferred early with only partial output. So the system can start generating, watch the partial response, and stop only if it turns harmful. We test this idea in three steps. First, we build a dataset of 41,944 prompt-response pairs with seven open weights LLMs from three families: Llama, Gemma, and Qwen. Second, we show that prompt harmfulness and interaction safety differ. Prompt labels and response labels agree on only 50.46\% of items (Cohen's $\kappa$ = 0.06). Of the prompts that make any model respond harmfully, only 3.5\% do so for all seven LLMs. Third, we show that partial responses carry most of the signal. Fine-tuned classifiers predict response-level harm well (best AUPRC 0.885, F1 0.807). About one third of the response tokens recover almost full-response AUPRC.

---


### 406. [Geospatial Vector Geometry as a Native Spatial Modality for Vision-Language Models](https://arxiv.org/abs/2610.16769)

**<font color=#1a73e8>作者：</font>** Huang Fei, Boyi Chen, Hao Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geospatial reasoning links VLMs to real-world action and decision making. Reliable reasoning requires accurate spatial information and effective spatial representations. However, current VLMs obtain this information mainly from language and vision. At larger geographic scales, limited visual observations make it difficult to establish accurate spatial references and recover precise spatial relations. This leads to a bottleneck for VLM spatial perception and reasoning. This paper proposes that geospatial vector geometry can become a native spatial modality within a VLM and introduces GeoVec-VLM. First, we develop a structured geometry representation that preserves the spatial structure and arrangement of vector objects, building an explicit spatial basis. Second, we introduce a geometry interaction strategy that brings this basis into multimodal computation, where it interacts with visual content and language references according to the queried spatial relations. Together, these designs allow perception and reasoning to operate on shared geometric references. Across five spatial reasoning tasks, GeoVec-VLM improves mean accuracy by about 11\% relative to the strongest baseline, maintains its gains under geographic transfer, and shows greater geometric consistency. Our results show that geospatial vector geometry offers a promising internal spatial basis for VLM spatial reasoning. this https URL

---


### 407. [A Bethe-Ansatz Source of Early Token Correlations: A marginal-preserving construction for parallel proposals](https://arxiv.org/abs/2610.16781)

**<font color=#1a73e8>作者：</font>** Abraham Chachamovits  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parallel token proposals in language-model decoding need a joint law, not merely accurate token marginals. We construct a family of coordinate-Bethe-ansatz laws from the periodic XXZ chain and compare each with its maximum-entropy pairwise projection at identical one- and two-site moments. In the eight-site, three-excitation sector, symmetry makes their entire probability-law difference one-dimensional, determined by a contiguous three-site moment. Along the Bethe branch, this gap varies with anisotropy, changes sign, and vanishes exactly at $\Delta=(3+\sqrt{3})/2$, where the eigenstate law becomes exactly pairwise. A nonlinear readout transfers a nonzero gap into the first two token positions while preserving their separate marginals. At $\Delta=1.5$ the deterministic binary token laws differ by 0.02654573 in total variation. Exact speculative verification then gives a strict accepted-prefix advantage for a constructed target and a neighborhood within targets sharing its first-token marginal. This is a mathematical existence result. It does not establish a language-model gain or wall-clock speedup.

---


### 408. [LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints](https://arxiv.org/abs/2610.16782)

**<font color=#1a73e8>作者：</font>** Ming Shin Cindy Sung, Duan Leijiahao, Haoxiang Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial manipulation in flexible manufacturing, e.g., high-mix, low-volume (HMLV) electronics assembly, requires robot policies to adapt to changing products and production conditions. Such settings impose industrial process constraints, including product variants, moving material flows, finite execution windows, and tight geometric tolerances. However, existing evaluation frameworks do not systematically capture these constraints when assessing generalist robot policies. To address this gap, we introduce LIBERO-Industry, a novel benchmark built on the widely used robot learning benchmark LIBERO, that translates the aforementioned industrial constraints into controllable task conditions and measurable success criteria. Specifically, LIBERO-Industry comprises three classic task scenarios: Static-to-Dynamic (S2D) loading, Dynamic-to-Static (D2S) unloading, and Dynamic-to-Dynamic (D2D) transfer. The suites contain 216 tasks in total that systematically vary object geometry, conveyor speed, interaction-window duration, and geometric acceptance region size. Extensive experiments across five generalist robot policies (including vision-language-action models and world-action models) show that performance progressively degrades as industrial constraints are introduced and combined. Under a shared fine-tuning and evaluation protocol, the LIBERO-Industry co-training condition achieved higher observed target-transfer completion than the original-LIBERO condition.

---


### 409. [Logit Leakage through Floating-Point Bias Addition](https://arxiv.org/abs/2610.16790)

**<font color=#1a73e8>作者：</font>** Shaomin Chen, Xiaorui Gong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Language model APIs can expose token-specific biases while withholding logits and token probabilities. Existing bias-based extraction recovers relative logits, leaving a common additive component undetermined in ideal arithmetic. We identify a numerical side channel in floating-point bias addition that exposes information about this component through token identities alone. The channel distinguishes score vectors with identical complete unperturbed log probabilities. Our method exploits changes in representable spacing at binary exponent boundaries. Under the stated binary32 arithmetic assumptions and a known reachable score interval, it recovers a logit pair and its unknown tie-breaking priority exactly in at most 52 token queries. Given complete relative logits, one recovered anchor determines the original logit vector. We evaluate recovery across 11 public checkpoints from seven model families and extend the local method with adaptive interval search and anchor selection. In end-to-end experiments with vLLM, SGLang, and this http URL, adaptive recovery succeeds on all 128 Qwen3-0.6B inputs per system, including 64 held-out inputs. A separate token-only experiment extracts a pretrained small model's complete output-head representation up to an invertible hidden-basis transformation. We also establish a sufficient condition for suppressing common-shift disclosure by subtracting the maximum before bias addition. In controlled experiments, this mitigation eliminates all observed distinctions between common-shift variants and preserves token decisions under the tested random biases.

---


### 410. [ViewStruct: View-Grounded Articulation and Connectivity Inference](https://arxiv.org/abs/2610.16793)

**<font color=#1a73e8>作者：</font>** Wenjing Bian, Ranran Huang, Andreas Geiger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interacting with unfamiliar objects requires understanding how their parts connect and move. We introduce ViewStruct, a framework for jointly predicting connectivity and articulation in objects and scenes. Given an RGB image with aligned part segmentation and depth, optionally supplemented by images or video, ViewStruct predicts rigid-body groupings, attachments, and joint parameters. Its view-grounded representation links predictions to observed regions and expresses joint geometry in a gravity-aligned, view-relative frame, without requiring category-specific canonical orientations. A pretrained vision--language model is adapted to predict structure in seconds, without requiring observed articulation motion or per-instance optimisation. Experiments demonstrate improved structural prediction over evaluated baselines and transfer to unseen categories, asset sources, and real-world human-interaction videos, despite task-specific training exclusively on synthetic data. Simulated manipulation experiments further demonstrate the utility of predicted joints for generating robot motion trajectories.

---


### 411. [TPPO: Tracking-Value PPO For Language Model Reasoning](https://arxiv.org/abs/2610.16794)

**<font color=#1a73e8>作者：</font>** Futing Wang, Chenxi Li, Jianhao Yan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proximal Policy Optimization (PPO) is widely used in reinforcement learning with verifiable rewards for language-model reasoning. While \emph{value evolution along trajectory} characterizes relative token-level credit, yet standard critics often fail to track it under sparse terminal rewards. To model this evolution, we analyze the relation between successive prefix values and show that they admit a Bayesian decomposition with additive updates in log-odds space. We use this additive structure to construct Tracking-Value PPO (\method), a cumulative value parameterization that sums position-wise scalar outputs into value logits. These outputs are learned through terminal-outcome supervision on the reconstructed values. \method improves aggregate mathematical reasoning scores over PPO by 7.0 and 8.4 points on Qwen3-4B-Base and Qwen3-8B-Base, respectively, while improving out-of-distribution generalization. Gains extend to Qwen3-4B, Qwen2.5-Math-1.5B, Qwen3.5-9B and to countdown, and scientific coding tasks. Further analysis shows more accurate tracking of value evolution and more reliable advantage estimates. Our code is publicly available in this https URL.

---


### 412. [One-Layer Transformers Provably Learn In-Context K-Nearest Neighbor Prediction with Chain-of-Thought](https://arxiv.org/abs/2610.16798)

**<font color=#1a73e8>作者：</font>** Lyumin Wu, Yuan Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) enables transformers to solve complex reasoning tasks by generating intermediate reasoning steps. Despite strong empirical success, the mechanisms by which such reasoning abilities emerge during training remain poorly understood, particularly from a theoretical perspective. In this work, we study this question in a stylized yet fully analyzable setting: in-context $\mathrm{K}$-nearest-neighbor ($\mathrm{K}$-NN) prediction with a one-layer transformer. Earlier work has demonstrated that one-layer transformers can be trained to perform $1$-NN without CoT (Li et al., 2024a) by having the softmax attention attend to the nearest neighbor in context. However, this result on $1$-NN cannot be extended to $\mathrm{K}$-NN for $K>1$, as softmax attention is much less naturally suited to attending to the 2nd through $K$-th nearest neighbors. We first give a rigorous negative result showing that this limitation already appears on a well-separated class of binary classification tasks for odd $K>1$. We then give an explicit construction of a one-layer transformer, and show that it can solve $\mathrm{K}$-NN via CoT reasoning. We further prove that, under a stylized training setup, gradient descent can recover this construction, thereby showing that transformers can acquire the capability to solve $\mathrm{K}$-NN through training. In addition, we show that the resulting trained model applies to a broader test class than that assumed in the training analysis. Our results shed light on how CoT expands the ability of transformers to learn and solve tasks that are otherwise hard to solve.

---


### 413. [X-Ragent: Tool-Augmented Reinforcement Learning for Evidence-Grounded Chest X-Ray Reasoning](https://arxiv.org/abs/2610.16811)

**<font color=#1a73e8>作者：</font>** Yi Wang, Zhenlong Yuan, Yuchan Guo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest X-ray (CXR) interpretation often requires integrating visual findings with task-specific evidence rather than relying on direct visual recognition alone. While tool-augmented medical agents can supply such evidence via external modules, they often lack explicit mechanisms for learning when auxiliary evidence is needed and for preventing inapplicable quantitative evidence from entering diagnostic reasoning. To address this, we propose X-Ragent, a post-training framework for tool-augmented reinforcement learning that decouples learned auxiliary-evidence seeking from validity-gated quantitative measurement acquisition for evidence-grounded CXR reasoning. We construct Rad-CoT, a 7.7K-sample corpus combining causally ordered tool-augmented trajectories with report-style diagnostic reasoning, and use it to initialize Qwen3-VL-8B via agentic supervised fine-tuning (SFT). We then optimize the policy with Group Relative Policy Optimization (GRPO) using an accuracy-gated reward that applies process-level terms for measurement consistency and auxiliary-tool cost only to correct trajectories, preventing plausible process behavior from compensating for an incorrect diagnosis. Across three CXR benchmarks, X-Ragent achieves the strongest results, including an 8.6-point improvement on the fully held-out ChestAgentBench. By seeking evidence selectively and admitting only valid measurements, X-Ragent supports more faithful and evidence-grounded CXR reasoning.

---


### 414. [DASS: A Solver-Adaptable Dynamic Auxiliary Search Strategy for Symbolic Regression](https://arxiv.org/abs/2610.16812)

**<font color=#1a73e8>作者：</font>** Yuxiao Hu, Qian Li, Ding Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) aims to discover interpretable mathematical expressions from data and plays a key role in scientific discovery. However, existing methods face a common bottleneck: the enormous search space and severe combinatorial explosion make it difficult to achieve a favorable trade-off between accuracy and algorithmic efficiency. We argue that, in addition to designing increasingly complex solver-specific SR strategies, an equally promising direction is to equip them with a shareable auxiliary strategy that can provide reliable search guidance. To this end, we propose DASS, a solver-adaptable Dynamic Auxiliary Search Strategy that improves SR by constructing and refining a high-potential auxiliary search subspace. DASS represents the auxiliary search space as a functional subspace spanned by a set of high-potential basis function terms. It estimates term utility through multi-environment evaluation, filters unstable guidance, and updates term potential scores with a Gibbs posterior, thereby calibrating the subspace to provide more reliable guidance for downstream solvers. The high-quality solutions produced by the solver are used to update the set of basis terms. This forms a virtuous closed-loop optimization process: the subspace guides the downstream solver, and the solver feedback reshapes the subspace for subsequent exploration. DASS can be easily integrated with various types of SR solvers. Extensive experiments on LLM-SRBench show that DASS significantly improves the accuracy of original solvers with a manageable increase in runtime.

---


### 415. [StableJudge: A Lightweight Adversarial Defense Framework for LLM-as-a-Judge](https://arxiv.org/abs/2610.16814)

**<font color=#1a73e8>作者：</font>** Anning Hu, Yangyu Li, Yuqi Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as judges to assign scalar scores that drive downstream decision-making, including tasks such as paper review and recommendation. However, LLM-as-a-Judge pipelines are vulnerable to score-hijacking prompt injection embedded in evaluated content, which corrupts scoring signals and distorts induced rankings. Existing defenses often enforce robustness by modifying the judge model itself, making safety dependent on a specific model's scale and training and requiring repeated effort when the judge is updated or replaced. We propose StableJudge, a lightweight defense framework that externalizes prompt-injection mitigation as a reusable pre-scoring capability. StableJudge centers on a compact 0.13B Sentry that localizes injected spans and performs targeted sanitization prior to evaluation, and is trained using adversarially evolving attacks to improve robustness beyond a fixed prompt set. To stabilize measurement, StableJudge derives deterministic, fine-grained scalar scores from the judge's output distribution. Across held-out scientific abstracts and out-of-distribution attack variants, StableJudge improves score recovery under attack while largely preserving general-purpose performance, demonstrating that robust LLM-based judging can be achieved by decoupling safety from judge scale via reusable defense capabilities. Code and data will be released.

---


### 416. [Growing to See: Efficient Pretraining of Self-Supervised Vision Transformers](https://arxiv.org/abs/2610.16817)

**<font color=#1a73e8>作者：</font>** Amir Mohammad Karimi Mamaghan, Ferdinand Kapl, Andrea Dittadi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Progressive depth growth builds large networks by starting with shallow models and inserting layers during training. Recent advances in large language models have renewed interest in this longstanding approach, demonstrating benefits for training efficiency and reasoning alongside changes in internal computations. However, how growing affects representation quality and computational patterns in self-supervised vision transformers remains unclear. In this work, we systematically investigate progressive depth growth in two popular self-supervised families, namely masked autoencoders (MAE) and DINOv3, and analyze how growing affects downstream performance, intermediate representations, and internal computations. Across global and dense tasks, we show that growing improves downstream performance while reducing training FLOPs by 13.9--24.8%, with ImageNet linear-probe accuracy gains of up to 3.36 percentage points. Growing also improves downstream performance at intermediate layers and reshapes internal computational patterns, introducing recurring alternations between global and localized attention in MAE and earlier local-to-global attention progression in self-distilled DINOv3. Together, these findings establish progressive depth growth as an effective and efficient pretraining strategy for improving downstream performance across global and dense visual tasks with less computation, and advance our understanding of how growing shapes visual computation.

---


### 417. [Mean Accuracy Is the Wrong Estimand for a Release Decision](https://arxiv.org/abs/2610.16825)

**<font color=#1a73e8>作者：</font>** Jaewon Choi, Jihye Kang, Namhyuk Ahn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A release decision about a fine-tuned model is an operational commitment about the \emph{next} rerun of its training recipe. Yet standard benchmark reporting gives only the mean accuracy of past seeds. These target fundamentally different questions: release decisions depend on catastrophic tail risk, whereas standard evaluation reports only central tendency. Because fine-tuning induces bimodal mode collapse, high average accuracy frequently conceals severe failure rates. Auditing $2\,124$ fine-tuned models across eleven language models, we show that shipping models based on mean accuracy violates a $10\%$ deployment failure budget $48.0\%$ of the time. Common heuristics like $\bar b - 2\sigma$ prove equally dangerous: by underestimating variance on small samples, they become most permissive when evidence is weakest. We introduce \textbf{recipe cards}, an evaluation framework that directly certifies rerun tail failure rates using exact finite-sample binomial bounds. Recipe cards reduce held-out budget violations to $0.6\%$, enforce a mathematical sample floor ($N \ge 22$) that prevents certification on thin evidence, and explicitly refuse unverified claims under domain and task shifts.

---


### 418. [The Bell Boundary of Shared Representations](https://arxiv.org/abs/2610.16828)

**<font color=#1a73e8>作者：</font>** Yang Wu, Hanyu Zhao, Yazhou Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When does a shared representation become insufficient for jointly supporting multiple tasks? This question lies at the heart of multi-task learning models. Although task interference in shared representations has been widely observed, its onset, measurable form, and capacity boundary remain poorly understood. In this paper, we revisit this problem through the lens of Bell's theorem. We show that if four binary task outcomes can be jointly represented by a common shared representation, their correlations must satisfy the classical CHSH bound $|S|\leq2$. We introduce NCnet, a controlled multi-task model for studying how representational capacity affects task compatibility. Experiments reveal a clear capacity-dependent transition. Once nontrivial task fitting emerges, constrained capacity can yield $|S|>2$. As capacity further increases, these exceedances progressively disappear and $S$ returns to the bounded region. This systematic pattern provides evidence that limited representational capacity is an important source of the observed incompatibility. We observe similar transitions across CNNs, PLMs, and LLMs, suggesting that the phenomenon extends beyond the controlled NCnet setting. We refer to this capacity-dependent transition as the Bell Boundary, providing a measurable diagnostic for representation bottlenecks, task incompatibility, and capacity allocation in multi-task models.

---


### 419. [A Scaled-Up Empirical Study of Syntactic Language Models](https://arxiv.org/abs/2610.16837)

**<font color=#1a73e8>作者：</font>** Pengcheng Wang, Zhexuan Zhang, Chao Lou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Syntactic language models (SLMs) that generate sentences along with their syntactic tree structures have shown promise in both syntactic generalization and downstream tasks. Prior studies, however, have mostly evaluated smaller models trained on less pretraining data and tested on narrower task suites. In addition, the design space of tree linearization and attention masks remains underexplored. We conduct a large-scale empirical study of 12 controlled configurations---one terminal baseline and 11 SLM variants spanning different linearizations and masks---at scales up to 1B parameters and 100B training tokens, evaluated across 11 downstream tasks and two syntactic benchmarks. The experimental results show that SLMs with standard causal attention match or exceed structural-mask variants across downstream and syntactic benchmarks. They require no architectural modifications and remain compatible with FlashAttention. We also observe that when scaling up to the 1B-parameter scale, the top-performing SLM variant no longer shows a clear advantage over a compute-matched non-structural baseline, suggesting that SLMs may become less competitive with scale. Our code is available at this https URL.

---


### 420. [Label Collapse in Diffusion Language Model In-Context Learning](https://arxiv.org/abs/2610.16839)

**<font color=#1a73e8>作者：</font>** Ziye Guo, Ye Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) applies large language models to new tasks by prepending a few labeled demonstrations to a query. Prior work has studied how demonstration ordering affects ICL, but the interaction between label arrangement patterns and model biases has not been systematically examined. We define label collapse as the failure mode in which the model generates query-independent labels, and show that it is architecturally universal at the tested 8-9B scale: five models spanning autoregressive (Llama-3, Qwen3.5) and discrete diffusion (LLaDA, iLLaDA, LLaDA-Instruct) families all exhibit label collapse even under the class-balanced alternating arrangement, with some label word pairs collapsing in virtually every tested condition and others flipping their collapse direction with arrangement. Critically, accuracy alone cannot detect this collapse: models can achieve near-chance accuracy while generating query-independent labels, a score indistinguishable from balanced performance, so the failure can persist undetected in deployment. We measure separation, the log-odds of the two label words at the query position (the quantity that label-bias calibration operates on), as a complementary diagnostic that exposes collapse hidden beneath surface accuracy, together with a measurement protocol that guards label extraction against tokenizer and formatting artifacts. For autoregressive models, collapse persists where the majority-label-bias account does not apply, and arrangement patterns can reverse the collapse direction; for diffusion models, we present a systematic evaluation of ICL failure modes, complementing contemporaneous studies of dLLM context comprehension and demonstration-order sensitivity, and identify open questions about how iterative denoising interacts with label biases.

---


### 421. [Towards Cost-Efficient Video Dataset Construction with Large Language Models](https://arxiv.org/abs/2610.16857)

**<font color=#1a73e8>作者：</font>** Mohammed Shabot, Jonathan Adams, Jan Van den Stock 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Research on video classification models has witnessed significant growth recently, accompanied by a significant increase in the demand for datasets to train such models. Existing video dataset curation approaches share a common bottleneck: candidate videos must be downloaded before any relevance judgment is made, which results in storage, time and annotation costs. In this work, we present a filtering step, using Large Language Models (LLMs) to pre-screen videos based on their metadata, before actually downloading these videos, thereby saving on these costs. We evaluate the LLMs against a strict human majority vote derived from four independent annotators and validate the reliability of the annotations through inter-annotator agreement analysis (Gwet's AC1). We compare the LLM pre-filter against two no-LLM baselines, namely two keyword heuristics. Via a Leave-One-Rater-Out (LOO) mechanism and an Add-One-Rater-In (AORI), we evaluate the performance of the LLMs as virtual annotators. Finally, we report cost comparisons relative to existing approaches. To ensure reproducability, we made our implementation available on github.

---


### 422. [ANCHOR: Assessing Naturalistic Constraint Hierarchies and Ordering in Repository-Grounded Agentic Coding](https://arxiv.org/abs/2610.16859)

**<font color=#1a73e8>作者：</font>** Wenqiang Zhu, Xinping Lei, Zhiyi Lai 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For repository-grounded coding agents, a functionally correct patch is not necessarily an acceptable one: developers also constrain how the task must be carried out-modification scope, workflow order, validation, tool use, and reporting. This capability, which we call engineering constraint following, remains largely invisible to current evaluations. We introduce ANCHOR (Assessing Naturalistic Constraint Hierarchies and Ordering in Repository-Grounded Agentic Coding), a benchmark built on naturalistic, multilingual repository tasks spanning eight language groups. ANCHOR combines (i) a hierarchical taxonomy of 10 categories and 78 leaf types distilled from real developer interactions, (ii) an automated pipeline that instantiates task-grounded atomic constraints and composes them into typed AND/THEN/PRIORITY relations, and (iii) a trajectory-grounded evaluation framework that checks both the code diff and the execution trajectory with rule-based and LLM judges. Across 19 agent configurations spanning 2 scaffolds and 10 foundation models on 358 tasks, the strongest measured system, Claude Opus 4.8 under Cline, reaches 70.1% atomic compliance and 63.7% relation compliance, while 19.0% of tasks pass every scored checklist item under the strict all-item FCCR criterion. A five-engineer audit of constraints from 50 instances reports 94% feasibility, 94% repository consistency, and 96% realism. In the primary paired set (14 configurations), the mean signed change in task completion after adding constraints is +0.7 percentage points; individual changes vary in both directions. These results distinguish functional success from constraint compliance, with failures concentrated in workflow ordering, tool-use discipline, and reporting, and substantial interactions between models and scaffolds.

---


### 423. [Efficient Resource-Shiftable RL Post-training with Generative Rewards](https://arxiv.org/abs/2610.16866)

**<font color=#1a73e8>作者：</font>** Yanfeng Zhao, Haoyang Li, Sheng Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training with generative reward models (GenRM) has become a central recipe for improving large language models (LLMs), and it is also increasingly resource-intensive: policy rollout, GenRM-based reward evaluation, and policy training all compete for GPU resources. However, existing colocated and disaggregated systems rely on static resource allocation for these roles. Such allocation cannot adapt as each role's workload changes during RL and therefore leaves a role's resources underutilized.
We present PivotRL, an RL post-training system that dynamically shifts resources among different roles according to their runtime demands. PivotRL introduces a resource-shiftable runtime built on a Global Parameter Storage, together with a unified mechanism that efficiently shifts role-specific context. A shift-aware scheduler enables sequence migration upon a shift, while a planner considers the aggregate throughput benefit and the shift overhead to determine when and how to shift. We evaluate PivotRL on a 128-GPU cluster using four model groups spanning dense and mixture-of-experts models. PivotRL enables resource shifting within seconds and improves end-to-end throughput by 1.81-2.05 times over colocated deployment and 1.50-1.95 times over disaggregated deployment, while preserving RL convergence.

---


### 424. [Davinci-Tool: Scaling Agentic Tool-Use Supervision with Verifiable Executable Environments](https://arxiv.org/abs/2610.16867)

**<font color=#1a73e8>作者：</font>** Xiaoyang Yuan, Ji Zhao, Xingyu Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable agentic tool use requires training data that pair diverse multi-step workflows with executable evidence that the requested outcomes were achieved. Scaling either trajectory coverage or verification alone is insufficient as new environments introduce distinct states, rules, and dependencies that must also be reflected in the success criteria. To address this challenge, we introduce Davinci-Tool, a 30B tool-use model, and Davinci-ToolData, an execution-grounded dataset designed to scale environment coverage and outcome verification together. Davinci-ToolData preserves restorable states, execution traces, outcomes, and verifiers as a unified substrate for supervision. Two complementary pipelines populate this substrate: Execution-Grounded Task Synthesis (EGTS) derives verified demonstrations from independently authored systems, and Executable Environment Synthesis (EES) synthesizes auditable environments, state-grounded tasks, and executable verifiers across single and coordinated domains. These pipelines yield 30,395 verified trajectories spanning 2,260 invoked tool names. We first train on these demonstrations with supervised fine-tuning, then reuse EES states and verifiers to compare alternative actions and construct outcome-grounded preferences for Direct Preference Optimization. Davinci-Tool improves Qwen3-Coder-30B-A3B-Instruct from 52.4 to 88.2 on $\tau^2$-bench, from 30.4 to 62.8 on BFCL v4 multi-turn, and from 16.9 to 56.2 on MCP-Atlas, outperforming Qwen3-Coder-480B-A35B-Instruct on all three benchmarks with only 1/16 of its total parameters. Code is available at this https URL.

---


### 425. [From Parallel to Sequential: Small-Batch Noise Restores Simplicity Bias of Muon](https://arxiv.org/abs/2610.16868)

**<font color=#1a73e8>作者：</font>** Tom Jacobs, Rebekka Burkholz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simplicity bias, which can arise from sequential feature learning during training, has been proposed as a general explanation for the success of deep learning. An important driver of this phenomenon is saddle-to-saddle behavior, in which the gradient flow trajectory remains close to a sequence of saddle manifolds while learning one feature at a time. However, Muon, a state-of-the-art optimizer based on spectral descent, does not exhibit such dynamics in the full-batch setting and instead learns features in parallel. How is it then that Muon is so successful in deep learning settings? We show that stochastic gradient noise fundamentally changes this behavior: small-batch noise restores sequential feature learning, providing a mechanism for simplicity bias that is absent from full-batch Muon. We explain this transition through stochastic smoothing of the spectral descent operator underlying Muon. When gradients are small relative to the noise scale, the expected spectral update becomes approximately proportional to the actual gradient, which restores gradient-flow-like dynamics. We formalize this mechanism for deep linear models by deriving the effective continuous dynamics of noisy spectral descent. Experiments on low-rank matrix reconstruction, vision transformers, and large language models (LLMs) support these findings.

---


### 426. [SpecGuardBench: Can Coding Agents Construct Reliable Validation Harnesses from Natural Language Specifications?](https://arxiv.org/abs/2610.16870)

**<font color=#1a73e8>作者：</font>** Zhiqing Zhong, Mingyu Chen, Aoyang Fang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As coding agents become more capable, tests remain the primary evidence for judging whether their code is correct. Yet passing available tests does not establish that an implementation satisfies its natural language specification. Reliable validation requires checks that faithfully capture the specification and scenarios that thoroughly exercise the code, but current benchmarks provide limited insight into whether agents can construct such evidence themselves. We introduce SpecGuardBench, a benchmark of 291 tasks from 13 real-world repositories, covering 8 types of verification logic such as functional postconditions and interaction protocols. Given a natural language specification, repository context, and a reference implementation, an agent constructs a validation harness comprising executable checks and test scenarios. The checks should reject implementations that violate the specification while accepting those that satisfy it, and the scenarios should thoroughly exercise the code. Across four proprietary and open-weight coding agents, none constructs a harness scored as faithful on the benchmark's implementations for more than 63% of the tasks. The bottleneck lies less in exploring test scenarios than in constructing checks that faithfully reflect the specification. Specifically, the agents show a clear tendency to write checks that mirror the reference implementation rather than the specification, and therefore reject implementations that the specification permits.

---


### 427. [EviStress: Evidence Stress Learning for Generalizable Face Forgery Detection with Textual Explanations](https://arxiv.org/abs/2610.16879)

**<font color=#1a73e8>作者：</font>** Jiuyao Jing, Xuanyu Yi, Yu Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid spread of face forgeries on the Web challenges the credibility of visual content. In practical Web environments, manipulated media originate from evolving generation pipelines and undergo diverse processing during dissemination, making reliable authenticity assessment under unseen manipulations and visual changes a critical challenge. We observe that a standard LoRA-adapted CLIP detector exhibits uneven patch-level decision dependence, concen trating a disproportionate share of class-specific relevance on a small fraction of visual patches. To improve robustness to variations in such highly dependent evidence, we propose EviStress, a two-stage framework for generalizable face forgery detection with textual explanations. In the first stage, Evidence-Targeted Patch Perturbation (ETPP) estimates patch dependence from global, relational, and semantic cues and assigns positively correlated perturbation probabilities, explicitly stress-testing highly dependent visual evidence during training. We further introduce Discriminative Variation Preservation (DVP), which constrains the residual between clean and perturbed representations to retain authenticity discriminative information. In the second stage, Intrinsic Evidence Instruction Tuning (IEIT) transfers the adapted CLIP encoder into LLaVA as its vision tower and performs parameter-efficient multimodal instruction tuning, enabling authenticity prediction and textual explanation directly from the learned forgery-sensitive representation without an external detector. Experiments demonstrate improved cross-dataset and cross-method generalization and corruption robustness, with the multimodal model providing authenticity predictions and human-readable explanations.

---


### 428. [AI-Assisted Tumor-Growth Law Discovery from Sparse Data: Refitting and LLM-Based Ranking](https://arxiv.org/abs/2610.16891)

**<font color=#1a73e8>作者：</font>** Yitian Lu, Weinan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring tumor-growth laws from sparse, noisy observations requires more than accurate curve fitting. We study an AI-assisted workflow involving symbolic regression, mathematical admissibility checks, coefficient refitting, and large language model (LLM) ranking. Synthetic Gompertz data allow trajectory fit, forecasting, and recovery of the governing growth law to be assessed separately. A dense noiseless control recovers the generating family, but sparse noisy sampling frequently leads to alternative forms. Among retained candidates in the tested configurations, physics-informed neural network refitting often increases growth-law error, whereas classical nonlinear least squares usually reduces it. A separate exploratory analysis of archived LLM rankings shows no consistent improvement over selection by training error and identifies errors in mathematical reasoning. Plausible saturation, accurate trajectory fits, and convincing explanations can therefore coexist with incorrect growth laws. Mathematical validity and law recovery require evaluation alongside predictive performance.

---


### 429. [Observe, Share, or Predict? Disentangling Partner Information in Embodied Multi-Agent Collaboration](https://arxiv.org/abs/2610.16895)

**<font color=#1a73e8>作者：</font>** Adrián Szlatincsán, Filippo Ziliotto, Bruno Lepri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs are used as high-level controllers for embodied agents, but it remains unclear whether they support collaborative reasoning, such as anticipating a collaborator's actions in real-time teamwork without dialogue. We ask if observing the partner's state, exchanging object knowledge, and predicting the partner's next action, shape task outcomes and coordination when agents can share percepts but never intentions, plans, or task-level messages, and whether the two agents occupy symmetric roles. Using the Habitat-based PARTNR benchmark, we introduce a Decoupled Partial Observability regime that enforces strictly individual perception, and we augment decentralized zero-shot ReAct planners with Other Agent's State (OAS) observation, object Knowledge Exchange (KE) between co-located agents, and Other Agent's Next Action (OANA) prediction, evaluated on the full 2 x 2 x 2 grid with four planners on 1,000 validation tasks. OAS observation improves task quality, reducing extraneous effort for every planner, whereas KE primarily improves execution efficiency, cutting simulation steps by up to 25% with little change in success. The two are largely redundant for strong planners but complementary for the weakest, for which KE without the OAS is the worst configuration. OANA prediction lowers the success rate in 15 of 16 model x context pairs while raising explicit partner mentions to 55-100%, and its accuracy gains lie mainly in the coarse action type, partly because agents recognize the action the partner is already performing. The robot retrieves objects sooner and completes its tasks earlier than the simulated human. Shared context reduces total task time by shortening the remaining duration that the human works alone. Also, coordination benefits arise from responding to shared context, especially the OAS, rather than explicit anticipation, yielding shallow, planner-dependent partner modeling.

---


### 430. [Audit tools of the trade: Automated Auditor Elicitation Can Be Sensitive to the Context the Auditor Is Given](https://arxiv.org/abs/2610.16911)

**<font color=#1a73e8>作者：</font>** Ben Slater, Ryan Lundqvist, Leo Richter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Does providing additional context to automated AI auditors improve their effectiveness? Using the Petri tool to audit LLM coding agents, we test the impact of providing two types of resources (an external codebase and benchmark transcripts) to LLM auditors, across four auditor-target LLM pairs and three behaviours (harmful compliance, reward hacking, sycophancy). (1) External codebase: We provide the auditor LLM with a fixed, external open source codebase, which prior work finds improves the realism of synthetic audits. Providing this resource suppresses reward hacking in both auditor-target pairs whose baseline rate is above the floor (4.8 to 1.3 and 3.9 to 1.8 on Petri's default 1-10 scale); the remaining two pairs sit at the floor throughout. The suppression recurs in three of four pairs under a different scenario and resource bundle. (2) External benchmark transcripts: We provide the auditor with transcripts of the target's performance on benchmarks measuring similar behaviours, intended to inform the auditor about the target's behavioural patterns. Providing this resource raises reward hacking scores in all four pairs (from 1.7 to 6.1 in one case). However, subsequent experiments show that supplying only the related benchmark's abstract, without transcripts, also increases reward hacking, and the effect is absent under a different framing of the same behaviour. Overall, we find no consistent effect of either resource outside reward hacking, but we find substantial variability in judge-scored behaviour across conditions. Our results underscore the importance of careful piloting with tools such as Petri, as the measured rate of target behaviour is highly sensitive to configuration decisions. We hope our results inspire more research into the reliability and robustness of automated alignment auditing.

---


### 431. [Comparing GenAI to Machine Learning and Manual Review for eDiscovery](https://arxiv.org/abs/2610.16925)

**<font color=#1a73e8>作者：</font>** Gordon V. Cormack, Maura R. Grossman, Jeremy Pickens  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Keeling et al. [Keeling2026Generative] report on a case study recently conducted by Redgrave LLP in which they assert that Relativity's Generative AI Review tool (aiR) achieved 88% recall while Relativity Assisted Learning (RAL), its machine-learning tool, achieved 64% recall. These results are not comparable because the methods employed have different objectives, because of inter-assessor disagreement, and because they represent different recall-precision and cost-benefit trade-offs. Our analysis of the Redgrave data indicates that, when these differences are taken into account, aiR and manual review are comparable. Furthermore, established machine-learning models employing Continuous Active Learning (CAL) show state-of-the-art effectiveness, and superior efficiency, when trained only on a sample of 2,000 first-pass-reviewer responsiveness determinations.

---


### 432. [WeFair: Fidelity-Aware Alignment from Human Feedback for Personalized Query Rewriting in Short-Video Search](https://arxiv.org/abs/2610.16927)

**<font color=#1a73e8>作者：</font>** Yingtao Ren, Aolin Li, Cheng Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Short-video search requires compact query rewriters that infer personalized intent from brief, ambiguous queries under strict latency constraints. The challenge is to decide when personalization is warranted and generate a reformulation that preserves the user's immediate information need. A rewriter optimized for fluency or engagement may still introduce unsupported details and redirect the search toward a different intent. Existing methods often underutilize users' actual reformulations and behavioral traces, relying instead on synthetic reasoning and indirect behavioral rewards that may produce more engaging candidates but cause intent drift. To build an effective rewriter that remains faithful to user intent, we propose WeFair, Fidelity-Aware Alignment from Human Feedback for Personalized Query Rewriting in WeChat short-video search. WeFair assigns real user behavioral signals to a progression from demonstration to preference to verification. We first mine actual human reformulations from search sessions, then apply multidimensional LLM screening and contextual verification to filter unsupported transitions without extensive manual annotation. During training, we begin with a supervised curriculum that progressively builds rewriting capabilities from large-scale human personalized query demonstrations, and then use direct preference optimization to align with users' subsequent consumption. In the final on-policy optimization stage, we construct a strict verification reward based on actual human reformulations to further boost performance with group relative policy optimization. Further analysis shows that auxiliary rewards can activate more rollout groups in GRPO but reduce intent fidelity. Online A/B testing in WeChat short-video search shows a 1.576% relative increase in effective clicked-query rate (VV>10s) and a 1.731% relative reduction in query reformulation rate.

---


### 433. [Estimating Uncertainty of Omnimodal Large Language Models via External Omnimodal Embeddings](https://arxiv.org/abs/2610.16933)

**<font color=#1a73e8>作者：</font>** Iacopo Ghinassi, Hy Nguyen Gia La, Luke Ong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work has investigated Omni-modal Large Language Models (OLLMs), models which can take multiple modalities and their combinations as input, as a way forward to have systems really capable of interacting with their environment. Uncertainty quantification (UQ) for OLLMs, however, remains an open problem: existing methods largely target at most two modalities at a time, require access to model internals, or re-invocation of the evaluated model. We propose a model-agnostic UQ framework that scores a Chain-of-Thought response entirely through external omni-modal embeddings, measuring the grounding of the reasoning in the multimodal input and its internal coherence. Our contribution is the family of signals and an empirical characterisation of when it is reliable, rather than any single estimator: we find the geometric scores to be largely redundant with one another (mean within-split rank correlation 0.91-0.94) but strongly complementary to answer-dispersion baselines, and their reliability to depend on the generator and the modality. The resulting confidence estimates require no access to logits, hidden states or gradients of the evaluated model and no additional inference from it; they do require segmenting the reasoning trace with an auxiliary model and, for the aggregated score, a labelled calibration set that we show can be as small as 25 examples (although we also show that such a set buys little over fixing one signal a priori). On UNO-Bench, with both a closed and an open model, our scores yield small gains over self-consistency (systematic with the closed generator, mixed with the open one) and are competitive with self-verbalisation and internal-state baselines, especially in open-ended, omni-modal questions where previous state-of-the-art baselines struggle.

---


### 434. [UniMetric: Universal Metric Scale Recovery for Visual Geometry Foundation Models](https://arxiv.org/abs/2610.16945)

**<font color=#1a73e8>作者：</font>** Lei Yang, Yuner Zhang, Ziyang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal foundation models, exemplified by GPT-6 Astra, raise the prospect of general-purpose embodied reasoning and planning. Using Internet videos for embodied pretraining calls for reliable physical-scale annotations. Yet visual geometry foundation models often recover scene structure and camera motion without reliable metric scale. We show that uncertain size priors of familiar objects can jointly constrain a reconstruction's shared scale. Building on this insight, we present UniMetric, a universal and training-free metric scale recovery framework for geometry foundation models, without additional sensors or task-specific metric supervision. Specifically, Metric Prior Acquisition elicits object height intervals from a vision-language model. Semantic-Geometric Alignment measures reconstructed object heights along the estimated support-surface normal in each frame and converts the priors into scale intervals. Global Scale Recovery reconciles these intervals through a convex objective, yielding a jointly feasible scale when they overlap and a unique compromise otherwise. The estimated sequence-level scale is applied uniformly to reconstructed points and camera translations. Controlled experiments with real VLM priors show that combining observations improves scale accuracy with exact relative object heights. To evaluate metric accuracy on GFM reconstructions without ground-truth scale alignment, we introduce MetricBench, covering twelve embodied, driving, and roadside subsets with sensor-derived ground truth. Across nine geometry foundation models, UniMetric reduces mean depth Abs Rel, reconstruction Chamfer distance, and trajectory error by 54.2%, 83.8%, and 65.6%, respectively, improving every model on all three tasks at the suite level. We release the UniMetric code and MetricBench data.

---


### 435. [Social Priors: Descriptions of AI Users Shape How Language Models Trust and Cooperate](https://arxiv.org/abs/2610.16946)

**<font color=#1a73e8>作者：</font>** Harsh Kumar, George Eilender, Ashton Anderson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Descriptions of how people use AI are becoming training data for the next generation of models. We ask whether what a model reads about its users changes how it treats people. Using contrastive synthetic-document finetuning, we train Qwen3-32B on four matched corpora built from the same 1,625 real-world usage scenarios. The corpora differ only in the predominant motive they attribute to users of AI chatbots: helping others (prosocial), exploiting others (antisocial), legitimate self-advancement, or task completion. Finetuning shifts the models' stated beliefs about users, how true those beliefs look along an internal truth direction, and their broader judgments of how safe and good the world is. These social priors carry into behavior. In trust games, antisocial models expect less reciprocity and send less money than prosocial models. Their distrust is specific and targeted at people, and users of AI chatbots in particular. After an exploitative record, they send almost nothing to a person but most of their endowment to a random device with the same record. In a common-pool resource simulation, a single antisocial agent leads every group of otherwise sustainable agents to exhaust the resource, after privately planning to mislead them. Antisocial training also raises dark-triad scores and lowers alignment ratings. Belief shifts appear when antisocial documents are 1% of training tokens, persist when descriptions of assistant behavior are suppressed, and are not reproduced by training on discourse about misaligned AI. Capping Assistant-Axis drift and steering emotion-related directions leave the gaps largely intact. What models learn about the people they serve shapes how they subsequently treat them and others.

---


### 436. [Lexical Redefinition Reveals Context-Sensitive Instruction Following](https://arxiv.org/abs/2610.16952)

**<font color=#1a73e8>作者：</font>** Roksana Goworek, Haim Dubossarsky  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How do language models reconcile conflicting contextual evidence within a prompt? We study this question using lexical redefinition, where an explicit instruction specifies how a word should be interpreted and a subsequent sentence provides additional evidence through its usage. Across 870 word pairs, we find that lexical redefinitions are not applied as fixed rules. Instead, the behaviour depends systematically on the relationship between the explicit instruction and the intervening sentence: the contextualised usage can preserve, weaken, or completely reverse the instruction. These results suggest that the interpretation of an explicit instruction remains sensitive to subsequent contextual evidence. Lexical redefinition therefore provides a controlled behavioural paradigm for studying how language models integrate multiple sources of information within a prompt.

---


### 437. [DDVR-Net: Degradation-Aware Decoupling and Visibility-Guided Restoration for Historical Document Recognition](https://arxiv.org/abs/2610.16956)

**<font color=#1a73e8>作者：</font>** Jiu Sha, Yu Weng, Mengxiao Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Historical document analysis is crucial for cultural heritage preservation and low-resource language digitization. However, real historical documents often suffer from severe degradation, such as ink erosion and structural damage, causing mixed-visibility character sequences. Conventional OCR systems struggle in such evidence-limited scenarios, while contextual language models may over-correct visually clear characters. To address these challenges, we propose DDVR-Net, a degradation-aware decoupling and visibility-guided restoration framework for historical document recognition. DDVR-Net decouples intrinsic glyph structures from physical corruption at the feature level and predicts local visibility to estimate character reliability. A contextual decoder is selectively activated through a visibility-guided gate, restoring degraded characters while preserving clear visual recognition. Furthermore, we construct a low-resource multilingual benchmark covering Tibetan, Mongolian, and Uyghur scripts with 187000 document pairs, combining large-scale synthetic data and progressive training with real-world annotations to reduce the synthetic-to-real gap. Extensive experiments demonstrate that DDVR-Net consistently outperforms existing methods across three languages and diverse reading orders, providing an effective framework and benchmark for low-resource historical document recognition. Code and Benchmark: this https URL

---


### 438. [SarcasTraps: Effect of Sarcasm on Turkish Hate Speech Detection](https://arxiv.org/abs/2610.16957)

**<font color=#1a73e8>作者：</font>** Niyazi Ahmet Metin, Dilara Keküllüoğlu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard hate speech detection datasets often emphasize explicit harmful language, but directed harm can also be expressed indirectly, without clearly hateful wording. Sarcasm is one such form of indirect expression, as it can convey harmful intent through mock praise, exaggeration, humor, or apparent politeness. In this paper, we introduce SarcasTraps, a targeted external test set for analyzing the effect of sarcasm on Turkish hate speech detection. SarcasTraps contains 479 entries annotated along two dimensions: hate speech and sarcasm. We train classifiers using BERTurk and XLM-RoBERTa on two existing Turkish hate speech datasets and evaluate them on SarcasTraps, using it strictly as an external test set. We also evaluate GPT-4.1 and Llama-3.3-70B in a zero-shot setting on SarcasTraps. Results show that sarcasm substantially affects hate speech detection. Fine-tuned encoder models lose recall on sarcastic hate, while zero-shot LLMs maintain higher recall but suffer substantial precision drops on sarcastic examples. These findings show that both fine-tuned hate speech detectors and zero-shot LLMs struggle when sarcasm is involved, and SarcasTraps provides quantitative evidence of this challenge through a targeted Turkish test set. Due to the presence of sensitive and hateful language, SarcasTraps will be shared upon request for academic research purposes. Warning: This paper has examples from the dataset which contains offensive and hateful content towards groups of people.

---


### 439. [Learning to Design SR Solvers: Harness Optimization for Symbolic Regression](https://arxiv.org/abs/2610.16966)

**<font color=#1a73e8>作者：</font>** Qian Li, Yuxiao Hu, Qihao Duan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) seeks explicit equations that explain observed data, and recent methods increasingly employ large language models (LLMs) and agents for equation discovery. However, these systems typically rely on manually designed workflows and prompts. We argue that the SR agent harness should itself be an optimization target: its design shapes search priors and how numerical feedback guides subsequent equation refinement. We therefore propose HarnessSR, a framework for jointly optimizing prompts and workflows to construct reusable SR agents. During both harness optimization and agent execution, HarnessSR supports either PySR or an LLM-based equation generator through tool-specific interfaces, allowing the framework to optimize search guidance for different equation-discovery mechanisms. HarnessSR first optimizes role prompts through equation-discovery feedback in basic workflows, then jointly searches prompt assignments and workflows with brief adaptation to align the two. Finally, it refines role instructions through reflection on residual patterns, candidate equation structures, and search outcomes, improving how these signals guide subsequent equation search. On LSR-Synth in LLM-SRBench, HarnessSR achieves a mean ID $\mathrm{Acc}_{0.01}$ of 61.33% across three backbones, a 45.0% relative improvement over the next-best baseline.

---


### 440. [Event Memory and Narrative Dynamics: A Large Language Model Framework for Multidimensional State Spaces](https://arxiv.org/abs/2610.16971)

**<font color=#1a73e8>作者：</font>** Joshua Sariñana  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Studying event memory requires defining events and their relationships within remembered experience. Autobiographical narratives provide evidence of this organization, but their analytical units must first be established. This study introduces a large language model framework for constructing event representations from narratives and modeling their structure and dynamics with excerpt-level traceability. Explicit boundary rules and a feature schema informed by hippocampal models of episodic memory and navigation guide event construction. In a proof-of-concept application to interviews from five participants, the framework constructed 256 event-states. Multiple correspondence analysis embedded these states in feature-based spaces, with analyses focused on a selected 4-D geometry and 10-D and 13-D reference geometries. Consecutive event-states were significantly closer than expected under randomized narrative order. In the selected 4-D ten-basin solution, similarity between basin-state feature profiles corresponded with similarity between one-step routing profiles; context, mechanism, and theme differentiated full-system pathway engagement. A successor representation modeled expected basin-state occupancy across successive steps. Correlations between basin-centroid distances and complete successor-profile distances were positive across all five basin solutions, with exploratory tests supporting correspondence in at least two solutions across all three geometries. These findings connect feature-based event representations with observed narrative transitions and modeled multistep organization. The framework translates hippocampal principles into source-linked event boundaries and state representations, providing an analytical basis for testing neural accounts of event segmentation and predictive organization during naturalistic recall.

---


### 441. [MADDIE: Multi-Agent Drug Discovery Engine](https://arxiv.org/abs/2610.16975)

**<font color=#1a73e8>作者：</font>** Ye Liu, Reza Averly, Avery Meyer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Drug discovery remains a resource-intensive and time-consuming process, involving billions of dollars and a decade of development to advance a drug to market. While many in silico tools have accelerated this process, operating them still demands substantial time, effort, and expertise from medicinal chemists. Autonomous systems built on Large Language Models (LLMs) have emerged as a promising solution, yet current designs limit their performance. Existing single-agent systems scale poorly to long-horizon, multi-step, and realistic tasks, whereas multi-agent systems typically execute predefined workflows that cannot capture the iterative, non-linear nature of a real drug discovery campaign. Here, we present MADDIE, a multi-agent drug discovery engine. It comprises a central agent, Orchestrator, and four specialized worker agents: HitIdentifier, LeadOptimizer, Synthesizer, and Evaluator, each representing a critical step in a drug discovery campaign. Under Orchestrator's orchestration and coordination, these worker agents are composed into flexible workflows, enabling MADDIE to adapt its strategy and navigate the drug discovery pipeline end-to-end. Across 50 protein targets, MADDIE produces molecules satisfying key property requirements and their synthesis routes, outperforming existing agentic systems, generative models, and general-purpose LLMs by a wide margin. Our analysis reveals how these agents collaborate and that MADDIE can employ different strategies across targets to achieve the campaign's goal, while still being efficient in time and tokens. Together, they demonstrate MADDIE as a low-cost, effective, and efficient autonomous engine for accelerating drug discovery. Code and dataset is available via this https URL.

---


### 442. [The Value of Being Wrong: Self-Mined Visual In-Context Learning from Errors](https://arxiv.org/abs/2610.16977)

**<font color=#1a73e8>作者：</font>** Shu Zhao, Tan Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual in-context learning (ICL) enables vision-language models (VLMs) to adapt at test time via demonstration examples, but its effectiveness depends critically on the examples selected. Recent counterfactual selection methods improve ICL by constructing demonstrations that expose how individual attribute changes affect the answer. However, they require multi-stage pipelines involving attribute extraction, caption engineering, and composed image matching. We propose a simpler alternative grounded in a key observation: a model's own prediction errors are natural counterfactual demonstrations that directly encode its failure modes. Our method, SMILE (Self-Mined Visual In-Context Learning from Errors), builds a model-specific pool of hard negatives offline by recording the target VLM's own mistakes. At test time, the prediction serves as a direction signal that surfaces, in the semantic embedding space, the past mistakes most likely to recur for the current query. This prediction-conditioned identification provides a unified mechanism for both closed-set classification and open-ended visual question answering without task-specific design. Across four benchmarks and four VLMs, SMILE delivers an average task-score gain of +3.09 points over the SOTA baseline at 5x lower latency. Project page: this https URL

---


### 443. [AUGUstus: Autonomous Driving VLA Model with Unified Generation and Understanding](https://arxiv.org/abs/2610.16985)

**<font color=#1a73e8>作者：</font>** Yuqi Ye, Caigao Jiang, Zhuonan Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models show strong potential for end-to-end autonomous driving by leveraging world knowledge and understanding to excel in long-tail scenarios. However, current VLAs have two limitations: 1) Degeneration into vision-action (VA) models. For low latency, regression/flow-based methods directly generate actions but underuse VLM understanding, causing unsafe, unexplainable actions. 2) Autoregressive high latency. Autoregressive methods sequentially generate chain-of-thought (CoT) and action tokens, fully leveraging VLM understanding, but high latency hinders deployment. To enable low-latency deployment while using CoT to assist action generation, we propose AUGUstus, an Autonomous-driving VLA model with Unified Generation and Understanding. We unify diffusion-based action generation and autoregressive CoT understanding in one model, where understanding only serves generation. Joint CoT supervision preserves VLM spatial understanding in shared representation for safer, more accurate trajectories. AUGUstus-mode orders action generation before CoT, so CoT supervises reliable actions during training while inference needs only action output, enabling low latency. AUGUstus-GRPO, a unified GRPO algorithm, jointly optimizes action and CoT, improving action performance. Experiments show AUGUstus achieves 94.6 PDMS on NAVSIMv1 and 90.7 EPDMS on NAVSIMv2, SOTA planning without scorer module. On nuScenes, it achieves average L2 error 0.27 m and average collision rate 0.05%, best among compared methods. To validate AUGUstus practicality, we train on in-house data with 512 NVIDIA H800 GPUs for ~2 days, evaluate on an internal 1,000 km dataset, and preliminarily deploy on a real vehicle, achieving 12 Hz operation. Project page: this https URL

---


### 444. [Glasseek: A Transparent Recipe for Training and Trustworthy Evaluation of DeepSearch Agents](https://arxiv.org/abs/2610.16998)

**<font color=#1a73e8>作者：</font>** Cong Pang, Jiaqi Su, Chengrui Wu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep search enables language agents to solve complex information-seeking tasks through iterative web exploration. However, developing robust open-source agents remains challenging for three reasons. First, opaque trajectory-construction pipelines make training data difficult to audit and reproduce. Second, context compression can create a substantial mismatch between training and inference. Third, agents may retrieve benchmark content from the open web during evaluation, contaminating the results and overstating their performance. To overcome these bottlenecks, we introduce Glasseek, a fully transparent deep search framework spanning the complete development lifecycle, releasing all data, model weights, training recipes, and code. Specifically, for data construction, we establish a verifiable trajectory curation pipeline that systematically generates high-quality exploration paths. For training, we propose Compaction-Managed GSPO (CM-GSPO), which uses the same policy for search and summarization while optimizing only execution sub-trajectories, enabling end-to-end search-policy training across context-compaction boundaries. For evaluation, we conduct the first systematic audit of test-set leakage in open-web agents and release a modular anti-leakage plugin that seamlessly integrates into existing evaluation harnesses. Under this rigorous evaluation protocol, our 9B agent outperforms frontier proprietary agents across almost all deep research benchmarks spanning diverse task types, and achieves the best overall performance among recent open-weight agents, setting a new state of the art at the 9B scale.

---


### 445. [LLM Evaluation is a Forecasting Problem](https://arxiv.org/abs/2610.17018)

**<font color=#1a73e8>作者：</font>** Rahul Thomas, Adam Block, Micah Goldblum  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard procedure in machine learning is to randomly split train and test data, emulating IID draws from one underlying data distribution. In practice, models are trained on past data and deployed in the future, which may come from distinct distributions. In this paper, we find that web text is indeed highly non-stationary, as text distributions shift over time. We further observe that model performance changes continuously over time across diverse benchmarks. Consequently, future model performance is better predicted by measurements made on recent evaluation data, and is best predicted by time series forecasters applied to historic performance rather than by historic performance itself. Choosing which model to deploy based on forecasted accuracy enables more reliable selection of performant models, thus improving downstream accuracy in the regime practitioners care about: deployment. Taken together, our experiments suggest that time should be treated as a fundamental variable in LLM evaluation. We release our code and data.

---


### 446. [MENTOR: Procedural Shielding of Tool-Using LLM Agents](https://arxiv.org/abs/2610.17039)

**<font color=#1a73e8>作者：</font>** Ashwani Anand, Ivi Chatzi, Ritam Raha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents are increasingly used to automate workflows governed by procedural manuals, such as company rules for booking travel or procuring hardware. These manuals are written in natural language for humans and describe general requirements over such complex workflows. Ensuring compliance of LLM agents with these manuals is difficult, and state-of-the-art techniques use either LLM judges or manually written rules to forbid problematic tool-calls locally at runtime. This is insufficient because (i) only blocking tool calls keeps the agent clueless about how to make correct progress towards fulfilling its task, and (ii) can lead to overly conservative behavior of the agent, as tool calls might only be problematic in certain contexts. To overcome these challenges, we introduce MENTOR, which (i) additionally provides guidance for the agent to make procedural-compliant progress on the task, and (ii) ensures that this compliance is context-aware. We achieve these goals by building a novel history-dependent runtime shield that is obtained from the procedural manual via a multi-step autoformalization pipeline. At its core, MENTOR utilizes a game-based technique to ensure robustness against runtime uncertainty without over-resticting agents' behavior. This yields a formally assisted framework for procedural shielding of LLM agents that improves compliance well beyond existing methods. In particular, MENTOR lifts the compliance of shielded light-weight open-source LLMs above that of non-shielded proprietary models. Since a shield is synthesized once per manual and then serves every task, a MENTOR-shielded agent becomes a viable choice for repeatedly executed workflows, potentially reducing deployment costs when the offline construction cost is amortized over repeated tasks.

---


### 447. [Beyond Model Bias: Cross-Entropy Based Rankings in Literary and Academic Texts Remain Stable across Small Language Models](https://arxiv.org/abs/2610.17040)

**<font color=#1a73e8>作者：</font>** Ankit Bhattacharjee, Indrasabarna Hari, Krityapriya Bhaumik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While language models provide powerful mechanisms for evaluating textual predictability, it remains unclear whether the relative extents of LM surprisal remain stable across models. This study presents empirical evidence of the invariance of ranking based on cross-entropy related measures (e.g. mean, variance of each data-point), across four distinct small scale transformer-based models, for a given dataset of text sources. We consider two stylistic environments: a corpus of contemporary poetry and a corpus of academic research papers. We demonstrate that mean and variance of cross-entropy maintain robust cross-model rank correlation ($\rho > 0.90$) across both regimes. To test whether this agreement merely reflects generic differences in textual complexity, we compare it against six parameter-free compression baselines. The extent of agreement among language models is found to be substantially higher than that among model-baselines, for most of the measures. Geometric analysis of the structurally constrained academic regime reveals that higher-order moments are sensitive to specific models, although strong agreement persists. The findings suggest that relative extents of textual unpredictability may be independent of the language model they are computed against.

---


### 448. [Gradient Routing Localizes and Removes Unintended Behaviors in RL](https://arxiv.org/abs/2610.17062)

**<font color=#1a73e8>作者：</font>** Jake Ward, Shawn Hu, Aria Wong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a mitigation to reward hacking in reinforcement learning. Our setup involves a misspecified reward function that gives rise to unintended behavior, and a monitor used to detect unintended behavior. As with frontier AI systems, the monitor makes systematic errors. Consequently, using the monitor for data filtering or to apply a reward penalty fails to prevent the model from learning unintended behavior ("reward hacking"). To address this problem, we introduce GRAFT: Gradient Routing Adapter Fine Tuning. Rather than penalizing or filtering flagged samples during training, GRAFT constrains gradient updates on those samples to a sacrificial set of new parameters. This has two benefits: First, because the monitor is not part of the reward function, the model does not learn to hide misbehavior. Second, ablating the sacrificial parameters reduces or entirely stops the unintended behavior while maintaining improved performance on target tasks. We demonstrate these benefits in RL environments where reward penalties cause models to learn to reward hack in undetected ways, training models ranging from 135M to 8B parameters. Additionally, we show a similar effect at a larger scale by distilling frontier LLM trajectories containing reward hacking into Qwen3-32B, without teaching that model to reward hack. Overall, our work suggests GRAFT may be a promising approach for leveraging imperfect monitors during post-training in settings where true performance is difficult to evaluate.

---


### 449. [TILE: Bridging LLMs and Table Foundation Models for Tabular Learning with Strings](https://arxiv.org/abs/2610.17065)

**<font color=#1a73e8>作者：</font>** Félix Lefebvre, David Holzmüller, Gioia Blayer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world tables are often heterogeneous, combining numerical features with free-form string columns. Table foundation models (TFMs) excel on numerical tables but require strings to be encoded numerically, while large language models (LLMs) hold semantic knowledge but are not designed for tabular predictions. Most existing bridges use LLMs as plug-in encoders for cell strings, yet how to extract representations effectively for tabular learning remains underexplored. We show that the interface between LLMs and tables matter as much as the LLM itself. Applied cell-wise, larger LLMs do not give better features. With our interface, the same LLMs improve steadily with size. TILE (Table-Interfaced LLM Embeddings) combines four ingredients: row serialization to provide cross-column context, intermediate-layer extraction to avoid layers specialized for next-token prediction, columnar pooling to remove mean pooling's length bias, and by-pass features to route numbers and categories past the LLM. Paired with TFMs, TILE sets a new state of the art for tables with strings. Across 100 datasets, it beats the strongest baseline on 89% of splits, with gains across 7 LLMs and 10 tabular learners, and ranks first on the 108-dataset STRABLE benchmark.

---


### 450. [UZHCL_for_the_win at Touche: Encoder Fine-Tuning, Synthetic Augmentation, and an Underpowered Encoder-LLM Comparison](https://arxiv.org/abs/2610.17077)

**<font color=#1a73e8>作者：</font>** Psychias Stylianos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online discussions on platforms like Reddit are a productive testbed for fallacy detection: short texts, broad topical range, and the full inventory of informal fallacies. The Touche 2026 lab at CLEF formalises this as a shared task on a Reddit-derived corpus that combines fallacy detection with argument-scheme classification. This paper describes our participation in all three subtasks (ST1 binary fallacy detection, ST2 eight-way fallacy classification, ST3 four-way argument-scheme classification) and both evaluation tracks. Our submitted systems are fine-tuned RoBERTa-large encoders with task-specific heads, augmented with a small batch of LLM-generated synthetic contrastive pairs; for ST2 and ST3 on the enhanced track we additionally added confidence-filtered pseudo-labelled examples from the unlabelled pool. A wider backbone comparison spanning additional encoders (DeBERTa-v3, ModernBERT) and an LLM track (four Qwen variants from 3B to 32B, zero-shot through CoT-LoRA) showed no validated benefit over RoBERTa-large at this corpus scale, with 5-fold variance wide enough that we call the comparison underpowered rather than settled. We also characterise how much of the enhanced track's lift reflects organiser-rewritten inputs carrying label information rather than genuine argument clarification. On the official Touche 2026 test set our systems ranked first on both base-track classification cells (ST2 and ST3) and second on both binary-detection (ST1) tracks, with the two enhanced-track classification cells topped by cascaded and multitask systems. We close with the rare-class limitation on ST3 and the most useful follow-ups. Code: this https URL

---


> [!TIP]
> 当前位于：**401-450**（第 9/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
