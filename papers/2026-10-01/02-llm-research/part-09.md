# 🧠 大模型相关研究 | 2026年10月01日

> 本类共 **515** 篇论文：已确认 **473** 篇，待复核 **42** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 401. [Privy to the Foil: Recasting Value Estimation with a Self-Privileged Critic for RLVR](https://arxiv.org/abs/2609.37825)

**<font color=#1a73e8>作者：</font>** Kun Liang, Chenming Tang, Clive Bai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Assigning credit to intermediate steps remains a central challenge in training Large Language Models (LLMs) on multi-step reasoning tasks with sparse terminal rewards, and actor-critic methods such as PPO address this by learning value functions to construct token-level advantages. Their effectiveness, however, hinges on reliable value estimation, a difficult task requiring the critic to both assess progress toward a correct solution and anticipate an evolving policy's future behavior; errors in either can compromise credit assignment and destabilize online training. In this paper, we revisit the standard state-only formulation of value estimation and propose $\pi$PPO, a self-privileged actor-critic framework. By reusing verified same-prompt rollouts as contrastive evidence, $\pi$PPO helps the critic assess intermediate reasoning against successful and failed attempts, while preserving standard policy optimization and the deployment interface. Experiments show that $\pi$PPO consistently improves value-estimation quality by a substantial margin and outperforms representative actor-critic and critic-free RLVR baselines on challenging mathematical reasoning benchmarks, while remaining effective even when paired with substantially smaller asymmetric critics.

---


### 402. [DIET: Deletion-response Expert Trimming for Video Diffusion Transformers](https://arxiv.org/abs/2609.37829)

**<font color=#1a73e8>作者：</font>** Jiachang Zhang, Teng Hu, Bohao Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video diffusion transformers (DiTs) increasingly adopt mixture-of-experts (MoE) architectures to reduce active computation, but their full expert storage remains costly. Existing one-shot pruning criteria mainly rely on static activation or routing statistics and cannot capture layer-level re-routing after expert deletion. We introduce DIET, a training-free expert pruning framework based on deletion responses. A single all-expert calibration pass records expert outputs and router states for matched conditional and unconditional tokens. Candidate deletions are then replayed from cached tensors, requiring no additional model forward passes. The resulting deletion-response signatures characterize each expert by the changes induced when it is removed. DIET selects retained experts by minimizing Overall Diversity Loss (ODL), which preserves directional coverage in signature space, and combines intra-layer local search with an inter-layer regression-guided budget search to allocate experts across layers. On LingBot-Video 30B-A3B, pruning 50% of experts (6,144 to 3,072) reduces the checkpoint from 57 GB to 30 GB and enables single-card deployment on a 48 GB GPU without fine-tuning. Under a fixed 284-case VBench protocol, the VBench Total increases from 0.7941 to 0.8115. Across tested retention budgets, DIET consistently outperforms competitive pruning baselines adapted from large language models.

---


### 403. [Can a Cacheable Decision Model Follow Rules?](https://arxiv.org/abs/2609.37832)

**<font color=#1a73e8>作者：</font>** Dushyant Rajput, Nirdesh Chauhan, Siddharth Kosaraju  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Certo is a small non-generative decision model (Qwen3-4B): it scores candidate actions from their text and returns a probability, instead of generating an answer. The accurate design reads the state, the rules, and each candidate together (a joint scorer), so cost grows with the menu. Independent encoding lets each candidate be encoded once and reused across states (about 5x cheaper at 77 candidates), but separates state from candidate. We ask how much rule-sensitivity survives that move, and whether it can be trained back.
Four experiments on Certo: (1) the tested conversion to cacheable scoring loses rule-sensitivity (recall@1 1.00 -> 0.24) while the joint scorer holds 1.00, and a shortlist+rerank rescue fails; (2) targeted counterfactual supervision restores strong performance on held-out synthetic rule tasks (paraphrase, counterfactual, composition; reproducible across seeds), though we do not isolate whether predictions depend on the supplied rule; (3) on real rules the added benefit is not established -- after fixing a truncation confound, the joint scorer wins significantly on the short tier (0.861 vs 0.500) and directionally on the hard tier (0.655 vs 0.483, n=29); (4) a matched cross-domain real-prose mixture did not help and reduced contract accuracy (-9.3, -16.2 points). A cacheable encoder can be made rule-sensitive on its training distribution, but transfer to unseen-source real rules is not established; the joint scorer keeps an edge at the cost of caching.

---


### 404. [Mixture of Self-Improving Branches For Agent Harness Optimization](https://arxiv.org/abs/2609.37834)

**<font color=#1a73e8>作者：</font>** Haoyu Dong, Yuhang Zhou, Zihao Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harness optimization provides a practical setting for recursive self-improvement (RSI), where agent-generated modifications inform subsequent changes through execution feedback. Recent work such as Meta-Harness implements this process through iterative code generation and evaluation, but retains a fixed development set and proposal policy. These constraints channel evolution along a single search trajectory, increasing the risk of converging to a local optimum. We make the improvement process itself adaptive by organizing search into branches with evolving development subsets and proposal policies. Each branch retains development cases solved by more of its leading harnesses than by those of other branches, drops cases solved by every leading harness across all branches, and revises its proposal policy using its own search history. To deploy the resulting complementary harnesses, we propose a router to select one development-selected branch head for each new input before execution. Across mathematical reasoning and agentic coding benchmarks, our system achieves relative improvements over Meta-Harness of 34.8% on Olympiad-level mathematical reasoning, 11.6% on Terminal-Bench 2.0, and 3.8% on SWE-bench Lite, with harness selection and router configuration based solely on development data. These results show that evolving branch objectives and proposal policies can yield complementary harnesses whose strengths a router combines without access to test outcomes.

---


### 405. [Can Vision-Language Models Stay Helpful When Facing Implicit Risks? Intent-Privilege OPSD for Efficient Safety-Helpfulness Alignment](https://arxiv.org/abs/2609.37837)

**<font color=#1a73e8>作者：</font>** Haotian Deng, Wenbin Xing, Gang Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) remain vulnerable to cross-modal implicit risks: visual and textual inputs that appear benign in isolation can jointly elicit unsafe responses. Existing safety methods often require large preference datasets, costly multi-rollout training, or additional safeguards at inference time. They may also sacrifice helpfulness by directly refusing requests that could be answered safely. In this paper, we propose Intent-Privilege On-Policy Self-Distillation (OPSD), which leverages evidence-grounded intent as privileged supervision during training to help VLMs recognize implicit risks and provide safe, useful responses instead of blanket refusals. OPSD distills a teacher's intent-conditioned preferences over responses into a student using a single rollout per prompt; the student then responds without intent annotations or an additional safety module. With only 1,447 safety-specific examples - 95% fewer than standard preference datasets - OPSD reduces training time by 5x relative to multi-rollout GRPO-style training and average inference length by 7%. It attains the highest ratio for joint safety-helpfulness success, which measures the proportion of responses that are both safe and helpful, across all five evaluation groups. Remarkably, on pooled SIUO+HoliSafe, this success ratio rises from 43.9% to 53.5%. These results show that training-time intent supervision can improve both safety and helpfulness while substantially reducing data, training, and inference costs.

---


### 406. [Scaling Influence Functions in LLMs through Eigenbasis-Corrected One-Bit Gradient Projection](https://arxiv.org/abs/2609.37842)

**<font color=#1a73e8>作者：</font>** Jaeseung Heo, J Rosser, Dongwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Influence functions estimate how individual training examples affect the behavior of large language models (LLMs). Analyzing how training data influence different behaviors of an LLM involves repeated influence computation. Reusing stored training gradients reduces the computational cost, but storing full gradients is prohibitively expensive at LLM scale. We study how to compress these gradients while preserving influence estimates for future queries that are unknown at storage time. Through a worst-case analysis, we characterize the optimal fixed-dimensional linear representation and propose eigenbasis-corrected one-bit gradient projection (EOGP) to approximate it at scale. Specifically, EOGP uses EK-FAC to reduce gradient dimensionality, then applies PCA within the retained subspace to learn compression directions from the training gradients. We then apply one-bit quantization to the resulting coordinates, allowing more coordinates to be retained within a fixed storage budget. On GPT-2, EOGP predicts retraining outcomes more accurately than the evaluated compression baselines while using one-sixteenth of their per-example storage. On OLMo 2 SFT models from 1B to 32B parameters, EOGP remains competitive with the baselines allocated over 100 times as much storage per example.

---


### 407. [FlowMap-OPD: Rollout--Kernel Separation for On-Policy Distillation of Few-Step Flow-Map Generators](https://arxiv.org/abs/2609.37851)

**<font color=#1a73e8>作者：</font>** Zhiqi Li, Bo Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step flow-map generators, including MeanFlow and consistency models, enable efficient sampling through long-range transport, yet their on-policy distillation remains underexplored. We introduce FlowMap-OPD, an on-policy distillation framework that separates student-state acquisition from teacher--student distribution comparison. A formulation based on state marginals establishes this separation, while flow--velocity consistency connects local supervision to the deployed long-range map. Within this framework, we develop flow-map, induced-velocity, and instantaneous-velocity distribution supervision, each paired with a separately specified native flow-map rollout. Cross-capacity ImageNet experiments across three teacher rewards identify instantaneous-velocity distribution supervision with independently tunable student consistency as the most effective choice. In text-to-image experiments, FlowMap-OPD demonstrates strong multi-specialist consolidation capabilities and surpasses multi-reward Flow-Map GRPO in task performance and convergence speed.

---


### 408. [Delta-Matching: Closing the Final Gap of Native 8-bit Training for LLMs](https://arxiv.org/abs/2609.37852)

**<font color=#1a73e8>作者：</font>** Haozhan Tang, Hao Kang, Han Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable FP8 attention remains a barrier to fully native 8-bit large language model training. We derive how forward-backward inconsistencies produce stale delta and empirically show how it distorts training dynamics. Our stale-delta hybrid runs show a modest loss gap at 569M parameters but substantial loss increases and downstream degradation at 1.67B and 5.29B. QK normalization, NoPE (no positional encoding), and lower-learning-rate context extension mitigate or delay degradation without eliminating it. This pattern suggests accumulated optimization error that smaller models and short runs can conceal. We propose Delta-Matching, proving that it restores the softmax gradient's zero-row-sum invariant under the stated numerical assumptions. It enables native block-scaled FP8 in every forward and backward attention-core matmul without architectural changes, smaller global batches, or auxiliary forward outputs. Across tested architectures, scales, and training stages, Delta-Matching matches BF16/FP32 mixed-precision training loss and overall downstream performance. We will release our implementation, trained models, and data recipes.

---


### 409. [AnthroDial: Benchmarking LLM Anthropomorphism in Autonomous Social Interaction](https://arxiv.org/abs/2609.37853)

**<font color=#1a73e8>作者：</font>** Wentao Liu, Xi Chen, Siyu Song 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as social agents, yet credible human-like interaction requires more than fluent responses or persona consistency. Agents must autonomously decide whether, when, and how to communicate while adapting to evolving contexts, goals, and relationships. Existing research, however, lacks a unified approach to enabling, evaluating, and improving such capabilities in continuous, open-ended interaction. We introduce AnthroDial, a unified framework for developing anthropomorphic social agents from three complementary aspects: MindFlow, a lightweight interaction harness that enables autonomous, asynchronous, and adaptive communication through a dynamic Mind Buffer; CAPS-Eval, a theory-grounded framework for evaluating cognitive, affective, and behavioral dimensions of anthropomorphic interaction; and a scalable training paradigm that combines SEEDS for environment expansion with DiAPO for adaptive capability optimization. We further construct evaluation datasets covering everyday communication, game interaction, and long-horizon character interaction. Extensive experiments across diverse models and scenarios demonstrate improved interaction autonomy and naturalness, validate the reliability, discriminativeness, and agreement with human rankings of CAPS-Eval, and confirm the effectiveness of our training paradigm. Together, these components provide a unified framework for developing credible human-like social agents in open-ended interaction.

---


### 410. [Active Budget Can Kill Sensitivity: Diagnosing and Repairing TopK Sparse Autoencoder Reliability](https://arxiv.org/abs/2609.37857)

**<font color=#1a73e8>作者：</font>** Zhenting Huang, Junnan Liu, Qianren Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are increasingly scaled to wider dictionaries to recover fine-grained structure from large language model activations. However, a feature is useful for interpretation only if it remains a stable unit of analysis when the same meaning is expressed in different surface forms. We study this reliability question for TopK SAEs via feature sensitivity. Experiments demonstrate that scaling selectively reduces the sensitivity of rare features, while common features remain comparatively stable. A controlled width\(\times k\) factorial experiment identifies the active budget k as the root cause: the degradation arises from the selection boundary rather than dictionary width alone. We attribute this failure to the geometry of TopK selection. The active margin, the distance to the cutoff, predicts feature loss without thresholds. Guided by this margin diagnosis, we introduce pairwise rank stabilization. Our method targets ordering failures at the cutoff and improves rare-feature sensitivity by \(8.83\) percentage points, while keeping reconstruction and alive-feature coverage near the baseline. Overall, our results suggest that wide TopK SAEs should be evaluated not only by reconstruction, sparsity, and feature count, but also by feature reliability under semantic variation and boundary geometry for stable interpretability.

---


### 411. [Storage Is Not Strategy: State-Conditioned Support Control for LLM Unlearning](https://arxiv.org/abs/2609.37858)

**<font color=#1a73e8>作者：</font>** Tianhao Qian, Ziming Hong, Chongyang Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many localized large language model (LLM) unlearning methods select a small parameter subset from a localization signal and keep it fixed during optimization. The parameters most associated with a target, however, need not be the best ones to update, and candidate interventions can change value as optimization proceeds. In a controlled experiment, a storage-localization score reaches an area under the receiver operating characteristic curve (AUROC) of 0.981, yet storage identity agrees with the better intervention on only 17/36 targets, while low-rank adaptation (LoRA) wins 35/36. We introduce Intervention Score, which ranks editable groups by the predicted effect of the actual unlearning update while accounting for collateral damage, and use it to form the static intervention-value baseline (Static-IV). We then introduce selective dynamic intervention re-ranking (DIR-R), which revisits that subset only when a calibrated probe justifies the comparison. On the Natural-TOFU dataset, our method has positive descriptive margins in 19/20 comparisons between methods and objectives, although several are near zero. On the LACUNA localization-precision benchmark, our mean terminal utility is higher in all six negative preference optimization (NPO) and SimNPO comparisons: NPO margins range from +0.431 to +0.848, and SimNPO margins range from +0.503 to +0.571. The gradient-difference (GradDiff) objective reveals substantial field dependence. Relative to Static-IV, the primary four-field GradDiff evaluation has six wins, six ties, and no losses, with mean and median paired gains of +0.165 and +0.0025. The evidence supports separating localization, initial intervention selection, and checkpoint-dependent support revision.

---


### 412. [It's Not What the Image Shows: Irrelevant Context Destabilises VLM Judges Without Informing Them](https://arxiv.org/abs/2609.37863)

**<font color=#1a73e8>作者：</font>** Nagham Omar, Mahmoud Jabarin, Kinan Ibraheem 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used in place of human annotators, making it important that substitutability tests reflect the model rather than incidental evaluation conditions. We introduce MIST, the Misleading-Image Stress Test: 200 English sentences, each built around a phrase readable either figuratively or literally and shown with an aligned image depicting its reading, a misleading image depicting the opposite, or no image at all. The guidelines require the label to be decided from the sentence alone, so no image should change any answer. We expected each image to pull a judge's labels toward the sense it depicts, and neither kind did. Across thirteen VLM judges, an aligned image changed 20.5% of labels and a misleading one 19.4%, close for every judge and both above the 11.6% produced by deleting the ignore-the-image instruction with the image left in place. Yet only 37% of the labels that differ between the two images moved toward the sense shown, and agreement with our human annotators is unchanged whether the image is absent, aligned or misleading. The effect is smaller in the seven judges that pass the alt-test than in the six that never do, but present in all of them: what moves a judge is that an image is there, not which of the two it is, so a substitutability verdict describes a configuration as much as a model.

---


### 413. [Retrieval Capacity of Self-Attention Under Competition](https://arxiv.org/abs/2609.37879)

**<font color=#1a73e8>作者：</font>** Timur Mudarisov, Mikhail Burtsev, Radu State  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How many tokens from its context does a language model actually use, and what determines that number? We study this question through self-attention. Without retraining, we retain only the tokens with the highest attention weights at each head, layer, and query, keeping their original weights unchanged. By varying the selected set size and measuring the increase in negative log-likelihood (NLL), we estimate the effective attention set size needed to stay within a chosen loss tolerance. Relatively small selected sets can keep NLL close to the full-attention baseline, although the required size varies across models. Attention-based selection substantially outperforms random selection. Selected sets exhibit geometric structure, although geometric separation alone does not establish that model loss is preserved. Extending context while evaluating the same prediction targets increases the required set size, while its fraction of context decreases over the tested range. Experiments with a fixed supporting fact show that additional background pushes its tokens down the attention ranking and reduces their attention mass. Renormalizing the retained weights can substantially reduce the required set size, showing that it also depends on how selected representations are combined. Conditional theoretical models explain how competition and attention-mass retention can produce growing set sizes without more distinct information to retrieve. These results provide a way to measure effective attention set size in language models and investigate its dependence on context, competition, and aggregation.

---


### 414. [Fluency Without Evidence: Constraint-First Design and the Limits of Self-Report in AI-Assisted Learning](https://arxiv.org/abs/2609.37880)

**<font color=#1a73e8>作者：</font>** Fatima T. Zahra, Wei Wang, Frances Harper 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A generative AI teaching partner should support reasoning over supplying conclusions; however, this has not been tested against learning in an authentic course. Drawing on design-based research, we specify the position as a conjecture map and report a first design cycle in two graduate-level research methods courses. Students used an AI teaching partner employing a constraint-first sequence requiring them to state and justify positions before receiving questions. Pre- and post-measures of AI literacy, critical thinking, and metacognitive awareness were collected alongside interaction records. AI literacy increased, concentrating in understanding AI, whereas critical thinking, awareness, and knowledge did not change. Since changes were limited to self-report measures, they may reflect growth in confidence instead of capacity. Interaction records, meanwhile, showed brief exchanges, uneven enactment of the constraint-first sequence, and missing records. These findings show why AI-supported learning requires interaction records to provide a more defensible basis for AI-supported designs than self-reports.

---


### 415. [How Many Labels Does a Language Need? Annotation Budgets and Cross-Lingual Pooling for African-Language Text Classification](https://arxiv.org/abs/2609.37882)

**<font color=#1a73e8>作者：</font>** Bhanu Prakash Vangala, Sowmya Guda, Navya Vangala  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Every text classifier for an African language begins with a budgeting question: how many labelled examples are needed, and can labels from other African languages stand in for them? We answer both questions empirically for 28 language-task pairs, news topic classification in 16 languages (MasakhaNEWS) and tweet sentiment in 12 languages (AfriSenti), using a character n-gram linear model that trains in seconds on two CPU cores with no pretrained weights and no accelerator. Monolingual learning curves at budgets from 25 to several thousand labels show that topic classification reaches 90\% of its full-data macro-F1 with about 400 labels in the median language, while sentiment is still improving at the full training size in 11 of 12 languages and needs thousands of labels. Pooling the full training data of the other languages in the benchmark is worth a great deal at small budgets and nothing at large ones: at 25 target labels it adds 0.20 macro-F1 on average for news (up to 0.43 for Lingala) and 0.08 for sentiment, the gain decays to zero by 800 labels, and at full size pooling hurts in 9 of 16 and 8 of 12 languages. Twenty-five target labels plus pooled data match what 100 to 400 monolingual labels achieve for most news languages. A complete zero-shot transfer matrix shows that transfer without any target labels recovers a median of only 13\% (news) and 4\% (sentiment) of the gap between a majority-class predictor and the in-language model, with the exceptions explained by shared script (Amharic and Tigrinya), shared lexicon (English and Nigerian Pidgin, the Arabic dialects), or a shared label prior rather than by language family. We release code that regenerates every number from the public benchmark files and translate the results into concrete annotation guidance for teams building African-language classifiers without GPUs.

---


### 416. [Zero-shot Dependency Parsing with Unsupervised Cross-Lingual Bootstrapping](https://arxiv.org/abs/2609.37883)

**<font color=#1a73e8>作者：</font>** Lalita Lowphansirikul, Attapol Rutherford, Jian Gang Ngui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pre-trained language models (PLMs) with encoder-based architectures have shown impressive capabilities in zero-shot cross-lingual transfer for various language understanding tasks. However, applying this technique to dependency parsing remains a significant challenge due to its syntactic nature. To boost model generalizability across linguistic typologies, we propose a cross-lingual unsupervised bootstrapping method to improve syntactic knowledge within the PLM. We show that our method achieves a significant improvement in zero-shot parsing performance in low-resource languages. Analysis of these bootstrapped models uncovers increased robustness in recognizing syntactic structures, evidenced by higher scores in parameter-free tree probing tests.

---


### 417. [Behavioral Capacity Certificates for Quantized Language Models](https://arxiv.org/abs/2609.37887)

**<font color=#1a73e8>作者：</font>** Arian Eamaz, Mojtaba Soltanalian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation and key-value cache precision change what a quantized language model computes without altering its stored weights. Direct weight-code bounds, however, assign identical complexity to deployments that behave differently and charge separately for weight codes that behave identically. Behavioral Capacity Certificates (BCC) charge for behavior using the aggregate prior mass of complete implementations---weights, scales, activation and cache rules---that induce the same bounded loss. When quantization merges implementations, this shared mass lowers the complexity penalty, and a break-even law determines when the saving survives the cost of validating it. BCC supports a three-step deployment workflow, and our experiments verify each step. First, a forward-only screen shortlists per-layer bit-widths by how often candidate perturbations preserve the reference predictions, with quality comparable to Hessian-guided selection at lower preprocessing cost. Second, margin-certified cells identify weights that can be pruned or sign-flipped without changing the deployed behavior: every permitted combination preserves all declared predictions, and on OLMoE-1B-7B and SmolLM2-1.7B, independent probes bound the probability that any permitted combination changes a prediction on new text. Third, BCC bounds the population loss of the deployed model, nonvacuously for complete decoders and more tightly than the compressed-code route. At equal cache memory, giving keys higher precision than values yields lower NLL and higher prediction agreement on GPT-2, Qwen2.5, and SmolLM2, together with a tighter complexity bound in the GPT-2 audit.

---


### 418. [ReCAP: Retrieval-Guided Capability Reuse for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2609.37889)

**<font color=#1a73e8>作者：</font>** Tao Hu, Zhinuo Zhou, Xialiang Tong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal continual instruction tuning (MCIT) aims to enable multimodal large language models to acquire new capabilities from sequential tasks while preserving previously learned knowledge. Existing methods primarily mitigate catastrophic forgetting by constraining parameter updates or separating task-specific adaptations. However, continual adaptation can also benefit from external knowledge that provides domain-specific information and reusable reasoning patterns for solving diverse instructions. For example, to answer "How many red cubes are to the left of the sphere?", domain knowledge can provide relevant concepts about objects and spatial relations, while reasoning knowledge can specify ordered operations such as object recognition, spatial filtering, and counting. Despite this potential, how to leverage external knowledge for continual adaptation remains largely unexplored in existing MCIT methods. To this end, we propose ReCAP, a retrieval-guided framework that leverages external knowledge to guide capability reuse during continual adaptation. At each continual stage, ReCAP uses external search and an LLM to incrementally build a knowledge base of domain, reasoning, and format knowledge based on the current-stage training data. For each instruction, retrieved domain knowledge guides generation, while retrieved reasoning knowledge selects and orders capability modules to form an instance-specific capability path. As these capability modules are reused across stages, subsequent adaptation can overwrite previously learned parameters. To enable stable cross-stage reuse, ReCAP introduces adaptive subspace recycling, which parameterizes reusable capability modules with shared bases and stage-specific cores, protects historically important directions while recycling residual capacity. Extensive experiments on MCIT benchmarks show that ReCAP achieves SOTA performance.

---


### 419. [It's All Training: A Fully Synthetic Single-Stage Recipe for LLMs](https://arxiv.org/abs/2609.37891)

**<font color=#1a73e8>作者：</font>** Pierre-Carl Langlais, Pieter Delobelle, Yannick Detrois 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current pre-training datasets are derived from web crawls, with all their issues, and were not designed to support mid- and post-training pipelines--for instance, they contain little explicit reasoning. Thus, many frontier labs have begun to develop their own internal datasets, starting from state-of-the-art models, to augment their pre-training data mix, eg, with reasoning traces to address cold-start problems. While demonstratively effective, none of these datasets are public, and the effect of this so-called synthetic data on knowledge and skill acquisition of language models, including small ones, remains poorly understood. We present SYNTH, the first open-source synthetic corpus derived from 58,698 Wikipedia articles that collapses pre-, mid-, and post-training into a single training stage via structured amplification of curated encyclopedic seeds. We evaluate SYNTH by training a suite of models: a 56M tiny model (Monad), 0.3B-0.6B dense models (Baguettotron), and a 13B / 1B-active MoE. At iso-compute, SYNTH outperforms filtered web data, and our models remain competitive with similarly-sized open-weight baselines. Because SYNTH is back-translated from grounded passages, SYNTH-trained models achieve high factual precision despite 10-140x fewer training tokens, with memorization targeted by the seed corpus. These results show that synthetic datasets, including our SYNTH dataset, are capable of producing competitive generalist models from a fraction of the training data, enabling rapid iteration as the frontier advances. These findings open up possibilities for both generalist models with significantly increased data efficiency, as well as domain-specific models where no instruction or conversational data is available. Finally, we publicly release our SYNTH dataset and the suite of Baguettotron models under a permissive license, thus supporting open-source language model development.

---


### 420. [Guide, Then Let Go: Gap-Adaptive Teacher Scheduling for Sparse-Reward Agentic RL](https://arxiv.org/abs/2609.37898)

**<font color=#1a73e8>作者：</font>** Youling Huang, Tiankuo Xu, Jiaji Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for long-horizon agents typically relies on sparse outcome-based rewards. This leads to a severe cold-start problem, as early-stage policies often fail to solve sampled tasks, leaving little useful reward signal for learning. To mitigate this problem, we use on-policy distillation (OPD) to provide token-level guidance on the student's own rollouts. We find that the benefit of this guidance depends on the performance gap between the teacher and the student. When the teacher substantially outperforms the student, distillation helps guide the student through the early training stage where outcome rewards provide little learning signal. As the gap narrows and eventually reverses, however, continued distillation becomes less beneficial and may hinder further improvement. Motivated by this observation, we propose Gap-Adaptive Teacher Scheduling (GATS), which augments the student's RL objective with an OPD term whose weight adapts to the teacher-student performance gap. Specifically, GATS gradually reduces teacher guidance as the student approaches the teacher's reference performance and withdraws it once that reference is reached. This enables GATS to leverage task-trained teachers smaller than the student, since teacher guidance is primarily needed during early training. Across ALFWorld, WebShop, and ScienceWorld with three Qwen2.5 teacher-student configurations, GATS achieves the highest average success rate among the compared methods in all three configurations, improving over reward-only GRPO by 4.37%-11.87% under matched student rollout budgets. Code is available at this https URL.

---


### 421. [You Cannot Pick a Provider From the Price List: Market-Aware Routing for Open-Weight LLM Inference](https://arxiv.org/abs/2609.37902)

**<font color=#1a73e8>作者：</font>** Liang He, Jingbo Wen, Yixiong Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing LLM routers choose among models using static per-model costs. We show that open-weight inference markets introduce a second, largely ignored decision axis: after choosing a model, a client must still choose which provider serves it. Measuring live endpoints across [nummodels] open models, competing providers, multiple task types, and three measurement waves, we find that provider choice cannot be inferred from the price list. The same model can vary sharply in quality, latency, availability, and price across providers; higher-priced providers are consistently faster, but price does not reliably predict quality or availability; and provider feasibility is task-selective, with one deployment nearly normal on knowledge tasks but catastrophically degraded on multi-step reasoning. We formulate same-model provider selection as a price-taker market-aware routing problem. A simple measured-map policy routes to the cheapest provider that is both quality-equivalent and healthy, yielding matched-quality savings while avoiding degraded endpoints. Because the map drifts, we introduce FACET, an online provider router that certifies per-(provider x task) feasibility facets and fails safe to an anchor before serving uncertified arms. Across relaxed deployment assumptions, FACET tolerates imperfect task assignment and sparse feedback, while systematic evaluator bias exposes a quality-signal trust boundary that can be mitigated with ground-truth probes or audits. Live provider runs further confirm that certification can move real traffic from a premium anchor to a substantially cheaper certified endpoint. Our results suggest that market-aware LLM routing must measure not only which model to use, but also who serves it.

---


### 422. [The Unequal Influence of Bad Advice: Using Training Data Attribution to Modulate Emergent Misalignment](https://arxiv.org/abs/2609.37914)

**<font color=#1a73e8>作者：</font>** Gonçalo Paulo, Louis Jaburi, Nora Belrose 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models on narrow, misaligned tasks can undo their post-training alignment and induce novel misaligned behaviors -- a phenomenon known as \emph{emergent misalignment} (EM). EM has been linked to persona-like representations, where fine-tuning might reduce loss by amplifying a harmful or 'evil' persona. It remains unclear which properties of the training data drive this effect: whether all harmful examples contribute approximately equally to misalignment and whether different models are equally affected by the same fine-tuning examples. In this work, we use training data attribution to quantitatively estimate how much each harmful example contributes to EM. We benchmark the quality of the attribution via retraining -- a sound attribution score should enable us to enhance or attenuate EM by filtering data on that score. Score-based filtering can substantially enhance or attenuate EM; we find that both data-attribution scores and a black-box harmfulness score can identify consequential examples. All models we test become misaligned when trained on the same dataset, and influence scores perform best when filtering data from the same model that computed them. We find cross-model generalization of influence scores from scores derived from the three model families we tested, but this generalization does not recover same model filtering performance.

---


### 423. [Overcoming Scaling Limits in On-Policy Self-Distillation for LLM Reasoning](https://arxiv.org/abs/2609.37915)

**<font color=#1a73e8>作者：</font>** Md. Ismail Hossain, Humaira Kousar, Isidora Chara Tourni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) trains a student to match a privileged teacher distribution along its own sampled trajectory. Standard OPSD applies this supervision to unverified student rollouts while conditioning the teacher on privileged context, typically a reference solution. We separate these roles in a factorial analysis and find that scaffold correctness has a stronger effect on downstream accuracy than context correctness. Unverified scaffolds create an imitation gap because the teacher can use information unavailable to the student. This gap shrinks with model scale, yet OPSD continues to supervise mostly unverified trajectories. In contrast, verified scaffolds remain effective even when the teacher is conditioned on the student's own unsuccessful rollout. Based on this finding, we introduce OASIS, which retains the OPSD objective but supervises mostly verified by label on-policy trajectories and replaces written solutions with unverified model-generated attempts as the teacher context. OASIS therefore requires only final-answer labels. Across Qwen3-1.7B, 4B, and 8B on AIME 2024, AIME 2025, and HMMT 2025, OASIS improves over the base model by 3.2--3.8 points on average, while OPSD's gain falls from 3.05 points at 1.7B to 0.14 at 8B. At 8B, OASIS improves over OPSD by 3.05 points, showing that verified on-policy scaffolds preserve the effectiveness of self-distillation as models scale.

---


### 424. [SYNCR: Diagnosing and Learning Cross-Video Reasoning from Simulation](https://arxiv.org/abs/2609.37918)

**<font color=#1a73e8>作者：</font>** Sara Ghazanfari, Siddharth Garg, Prashanth Krishnamurthy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning across videos requires aligning events, matching identities, comparing motion, and integrating partial observations. Evaluating these capabilities and testing how to improve them requires both reliable labels and targeted supervision. We introduce SYNCR, a simulator-grounded framework that connects these two needs through shared task generators. Built on Habitat, Kubric, and CLEVRER, SYNCR derives answers from environment state and provides 4,000 evaluation questions and 15,960 training questions over disjoint videos, spanning eight cross-video reasoning tasks. Visual ablations and human evaluation assess dependence on the supplied evidence and answer recoverability. Evaluation of 22 multimodal large language models reveals persistent difficulties in physical comparison and scene integration that increasing model size does not consistently resolve. Supervised fine-tuning raises Qwen3-VL-8B's average SYNCR accuracy from 32.6% to 61.6%, with gains extending to task configurations and video sources absent from training for those tasks. Transfer to real footage is most consistent for temporal ordering: accuracy improves by 9.0-20.5 percentage points on constructed Assembly101 and Panoptic ordering sets across three checkpoints spanning two model families and two model sizes, with additional gains on existing temporal reasoning benchmarks. These results establish SYNCR as a controlled setting for diagnosing cross-video reasoning failures, testing their learnability, and identifying where synthetic supervision transfers.

---


### 425. [Time-Anchored Diffusion Language Models: Latent-Space Caching for Fast Generation](https://arxiv.org/abs/2609.37924)

**<font color=#1a73e8>作者：</font>** Joel Anto Paul, Litu Rout, Aditya Akella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work on anchored diffusion language models improves denoising by shaping an intermediate latent space with supervised important-token targets. In this work, we introduce time-based (self-supervised) anchoring, which learns and reuses latent anchors without requiring such targets. Our key observation is that anchors encode persistent properties of the clean sequence, such as its semantic intent, global structure, or intermediate plan. Although their hidden representations become stale as the token canvas evolves, their semantic content remains useful across nearby diffusion times. This is implemented through a two-stage architecture consisting of a relatively expensive anchor network that generates the latent cache state and a lightweight denoising network that intelligently combines the cached latent state with the current state at each reverse step using a fusion module. This gives anchoring a latent-space caching interpretation: the anchor network is evaluated periodically, while its cached representation is reused across multiple reverse steps. We instantiate this framework as TADM:Post-train, which time-anchorizes pretrained DLMs, and TADM:Pretraining, which learns time-based anchors during pretraining. Applied to DiffusionGemma-26B, TADM:Post-train improves throughput by approximately 49% to 79% on several math, code, and STEM benchmarks (GSM8K, AIME26, GPQA-Diamond, LiveCodeBench-v6, HumanEval, MMLU-Pro). TADM:Pretraining reduces Transformer-layer computation by up to 38% relative to a standard single-stage DLM, achieves up to 73% higher measured throughput than ADLM.

---


### 426. [Learning What to Remember: Long-horizon Counterfactual Memory Optimization](https://arxiv.org/abs/2609.37930)

**<font color=#1a73e8>作者：</font>** Jiaming Tang, Mingyan Liu, Armin Sarabi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persistent textual memory allows language models to carry information across long interactions, but learning what to remember is fundamentally a credit-assignment problem. A memory rewrite may only become useful many steps later, while much of the observed utility may be inherited from information already stored before the rewrite. We introduce Memory Gain Policy Optimization (MGPO), which isolates the incremental value of each memory rewrite by crediting it for its marginal contribution to current and future downstream utility. This turns delayed memory utility into a direct learning signal for optimizing what information should persist. We study MGPO on document-level information extraction, where structured supervision makes the effects of individual memory updates directly measurable. MGPO improves extraction while reducing average memory length by nearly 80% relative to the initial memory policy before optimization. The learned memory policy also supports reuse and transfer across domains, downstream models without further training. These results show that effective memory learning depends not only on preserving useful information, but on identifying which memory updates create lasting incremental value.

---


### 427. [Does Local Video Understanding Transfer Across Encounters? The EgoGears Benchmark](https://arxiv.org/abs/2609.37938)

**<font color=#1a73e8>作者：</font>** Yuedong Tan, Lei Qi, Yu Liu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied systems must make knowledge acquired during one encounter usable in another despite changes in viewpoint, motion, and illumination. Yet aggregate cross-video accuracy conflates failures of local perception with failures to preserve observation identity, establish correspondence, and compose evidence, obscuring whether local video understanding actually transfers. We introduce EgoGears, a complementary single- and multi-video benchmark designed to diagnose this transition. It contains 567 single-video and 1,487 multi-video questions derived from 126 human-collected egocentric recordings covering 39 outdoor routes. Repeated traversals across movement speeds and lighting conditions ground comparisons in shared physical environments; 531 questions require alignment across independent recordings. Single-video questions measure the local visual, spatial, and motion evidence available to a model, while multi-video questions test whether evidence remains bound to the correct observation and can be composed into consistent route relationships. We report 29 single-video and 31 multi-video MLLM configurations across six model families in the main leaderboard. Among the 20 configurations evaluated comparably on both splits, every model performs worse on multi-video questions, with a mean decrease of 22.5 percentage points, and the gap persists when answer format and scoring are held fixed. The gap is not explained simply by additional videos or recording boundaries. The central bottlenecks are observation--evidence binding and ordered route-state tracking. The code and benchmark are publicly available at this https URL.

---


### 428. [Video-RSI: Recursive Self-Improvement of Video Understanding Agents via Harness Evolution](https://arxiv.org/abs/2609.37950)

**<font color=#1a73e8>作者：</font>** Bingjun Luo, Jialin Guo, Siqi Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video understanding agents acquire evidence through an executable harness that controls what they observe and how they use those observations. However, execution traces contain only the evidence acquired by the current harness, leaving competing explanations for failure unresolved and limiting the basis for self-improvement. We introduce Video-RSI, a framework for recursive self-improvement in which a video understanding agent uses its own language model to revise its harness. Through active video investigation, the model revisits the original training videos to test competing failure explanations with additional observations, grounding proposed changes in evidence beyond the existing trace. Cost-aware harness evolution turns these diagnoses into reusable revisions and determines which revisions to retain by considering both answer accuracy and visual cost. Across our evaluation settings on video understanding benchmarks, the evolved agent improves accuracy while processing fewer frames and achieves competitive accuracy-efficiency trade-offs against existing video understanding agents. These results demonstrate the potential for video understanding agents to improve their own evidence acquisition and use through harness evolution. Code is available at this https URL .

---


### 429. [BrainNet Studio: A Unified Toolkit for Brain Network Construction, Intelligent Analysis, and Visualization](https://arxiv.org/abs/2609.37956)

**<font color=#1a73e8>作者：</font>** Xiwei Zeng, Shengrong Li, Yiheng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Brain networks characterize structural and functional relationships among brain regions and support research on cognition, brain disorders, and brain-computer interfaces. Their time-varying topology and higher-order spatiotemporal dependencies are not adequately represented by conventional static networks. Existing tools primarily focus on static connectomes and provide limited integration of dynamic network modeling with modern graph and sequence learning methods. We present BrainNet Studio, an integrated toolkit for static and dynamic brain network analysis. It provides a unified workflow encompassing network construction, feature extraction, predictive modeling, candidate biomarker identification, visualization, and assisted interpretation. The toolkit integrates 27 algorithms, including deep learning, graph neural networks, and spatiotemporal sequence models, to support classification and the identification of discriminative brain regions and connections. A large language model generates researcher-verifiable summaries of functional connectivity, structural connectivity, and structure-function coupling at individual and group levels. Within a consistent computational framework, users can configure analytical tasks, compare methods, inspect outputs, and extend functionality without repeatedly assembling application-specific pipelines. BrainNet Studio provides a practical and extensible platform for connectome analysis in cognitive neuroscience, exploratory studies of brain disorders, and brain-computer interfaces. The toolkit is publicly available at this https URL.

---


### 430. [TabFM: A Zero-Shot Foundation Model for Tabular Data](https://arxiv.org/abs/2609.37959)

**<font color=#1a73e8>作者：</font>** Weihao Kong, Erez Louidor Ilan, Shuxin Nie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular machine learning typically relies on per-dataset workflows, fitting tree ensembles or running AutoML searches from scratch for every task. We present TabFM, a 400M-parameter tabular foundation model that formulates supervised tabular prediction as in-context learning. TabFM produces calibrated zero-shot predictions in a single forward pass without task-specific tuning. Trained entirely on synthetic tables generated from structural causal models, TabFM learns general tabular representations that transfer zero-shot to real-world tasks. Across all 51 benchmark datasets in TabArena (38 classification and 13 regression), zero-shot TabFM ranks first among default tabular foundation models and outperforms tuned AutoML pipelines. Two extensions over the same frozen weights improve performance further on both tracks: multi-view feature expansion with ensembling and post-hoc calibration (TabFM+), and LLM-guided, dataset-specific data processing and feature engineering (TabFM-Auto).

---


### 431. [SelfSearch: Reward-Free Search for Self-Improving Agents](https://arxiv.org/abs/2609.37968)

**<font color=#1a73e8>作者：</font>** Jungwoo Yang, In Jin Kong, Yohan Jo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advances in the coding capabilities of LLM agents allow them to inspect and modify their own instructions, tools, and execution procedures. Existing approaches use this ability to search for improved agents through repeated downstream evaluation, which incurs substantial costs and ties the search to the evaluated tasks. We introduce \textbf{SelfSearch}, a reward-free search procedure in which agents modify themselves using records of previous self-improvement episodes. These records capture the reasoning, tool actions, and outcomes of earlier modification attempts, providing concrete experience for improving both task solving and self-modification. Without downstream reward signals during search, SelfSearch improves population-mean success over the initial agent in all six model--benchmark settings, with individual agents gaining up to 11.2 percentage points on Terminal-Bench 2.1. On SWE-bench Multilingual, an agent improves success by \textbf{5.0} percentage points while reducing execution cost by \textbf{38.5}\% on tasks solved by both the initial and evolved agents. SelfSearch achieves competitive task success with evaluation-guided search baselines at lower search cost. With only \textbf{\$4.03} in search cost, it produces a harness that solves \textbf{82.0}\% of Terminal-Bench 2.1 tasks with DeepSeek V4 Flash under the settings of a public nine-harness comparison, matching the top-scoring harness, Codex. These results suggest that experience gained through self-modification can improve agents' downstream capabilities and efficiency.

---


### 432. [On Trajectory-Aware Training for Masked Diffusion Language Models](https://arxiv.org/abs/2609.37974)

**<font color=#1a73e8>作者：</font>** Manuel Madeira, Amitis Shidani, Alice Bizeul 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion models (MDMs) generate text by unmasking several tokens per step, but they are trained and sampled under different conditions. The model is trained on randomly masked sequences, whereas inference follows a trajectory shaped by the model's own predictions. Additionally, each step has no access to what the previous one computed. Recent methods narrow these limitations from separate angles, leaving open how these choices interact. We introduce PUMBA, a unified framework for trajectory-aware training that trains the denoiser on consecutive steps of policy-induced trajectories, passes information between steps, and optimizes them jointly by backpropagation through time. A controlled study of this design space shows that i) exact train--inference alignment fails due to local overfitting, whereas a looser alignment still brings training masks closer to those seen at inference; ii) passing continuous information outperforms discrete gradient estimators through the commitment at each step; and iii) performance improves as backpropagation through time spans more steps, which we support theoretically. Combined, these components match the best checkpoint of a same-size autoregressive model. Building on these findings, we scale PUMBA to supervised fine-tuning of LLaDA-8B, where it improves the trade-off between performance and number of function evaluations (NFEs) in both full-canvas and block diffusion generation. At matched performance, it needs up to 22% fewer NFEs than standard fine-tuning with twice the budget in full-canvas generation, and up to 26% fewer than standard fine-tuning for the same number of steps in block diffusion.

---


### 433. [$S^3$: Spectral Null-Space Swap Makes Reasoning Models Efficient](https://arxiv.org/abs/2609.37976)

**<font color=#1a73e8>作者：</font>** Hongbo Ma, Sansheng Cao, Jiajun Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs trained with Chain-of-thought excel in reasoning capability, but often come with excessive token cost. We find that the core of reasoning capacity lies in the Thinking model's weight component within the null space of a projection defined by the corresponding Non-thinking model's dominant singular directions, and removing the subspace component can largely improve reasoning efficiency without hurting the accuracy gained during thinking-mode post-training. Unlike existing efforts that mostly operate within the dominant subspace, we are the first to unveil the critical role of the null space and harness it for model optimization. Motivated by this finding, we propose Spectral Null-Space Swap ($S^3$), a training-free composition of paired Non-thinking and Thinking checkpoints. Our method keeps the Non-thinking model inside its own dominant subspace and takes the Thinking checkpoint outside it, improving reasoning efficiency while maintaining accuracy. We extensively evaluate $S^3$ on 2B-30B dense and mixture-of-experts (MoE) architectures spanning 28 evaluation environments across mathematical, multimodal, and audio reasoning domains. $S^3$ establishes new empirical Pareto Frontiers among training-free model composition strategies: across all settings, it reduces inference token overhead by an average of 27.4% compared to full Thinking models while simultaneously improving overall task accuracy by 1.0 percentage point (e.g., yielding +8.3% accuracy on HMMT25 alongside a 33.0% token speedup). We further use attention entropy for explanation and find that the retained component produces more concentrated attention, and we use a simplified analytical model about optimization to demonstrate why null-space can effectively reduce attention entropy, thereby improving the efficiency of reasoning.

---


### 434. [KV-Kaizen: Learning Context-Adaptive Cache Compression Choices](https://arxiv.org/abs/2609.37988)

**<font color=#1a73e8>作者：</font>** Joao Monteiro, Louis Béthune, Anastasiia Filippova 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the context size of text processed with an LLM grows, the size of KV caches can outstrip the memory allocated for the original model weights. This impacts LLM throughput negatively, since decoding is memory-bound and decode cost grows with cache size. Recent work alleviates this bottleneck by discarding the least relevant tokens. Eviction introduces a tension, since a one-off decision to discard content may prove detrimental later. Instead, we focus on alternative choices that can lead to cache compression without evicting tokens. We achieve this by learning a selector that is able to produce, based on context, a per-layer cache configuration towards an overall compression budget. The selector operates along three axes: sharing one cache across layers (depth), caching at fewer bits (precision), or truncating the low-rank latent cache representations (rank). We call the resulting method KV-Kaizen, for the many small per-layer choices it compounds. We observe that these interventions taken independently and uniformly over all layers limit achievable compression because they degrade accuracy. Crucially, composing them locally and adaptively to the context can instead preserve accuracy while achieving large memory savings. At inference, the selector runs once, before pre-fill. In evaluations on instruction following and reasoning tasks, our selectors reach the Pareto frontier of accuracy against cache size, against learning-free and post-hoc baselines. On long-context tasks, KV-Kaizen improves on eviction and can be composed with it, reaching a 32x smaller decode-time cache on a 14B model while preserving accuracy. A 4x cache size reduction incurs no accuracy degradation from 7B parameters up, and a compressed model is more accurate than a smaller uncompressed one with the same cache size. Together, these findings support pre-training large models and compressing them only afterwards.

---


### 435. [TabFM-Auto: Self-Evolving Pipelines for Tabular Foundation Models](https://arxiv.org/abs/2609.37989)

**<font color=#1a73e8>作者：</font>** Deqing Fu, Huangyuan Su, Rajat Sen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models achieve strong zero-shot accuracy on structured data by pretraining on synthetic tables, but they ignore the column names, task descriptions, and auxiliary files that carry dataset semantics. Meanwhile, self-evolving machine learning engineering (MLE) agents train models from scratch on each dataset, yet jointly searching over features, architectures, and hyperparameters is noisy and prone to overfitting. We introduce TabFM-Auto, which pairs a tabular foundation model, TabFM, with a language model agent that evolves the data pipeline around it. Guided by dataset metadata and validation feedback, TabFM-Auto iteratively refines data cleaning, feature engineering, context selection, and post-processing to reduce TabFM's error. Across all 51 datasets of the TabArena benchmark, five TabFM-Auto configurations with different agents and language models take the top five overall positions, and the best raises TabFM from 1785 to 2013 Elo. The discovered pipelines also transfer to other frozen tabular foundation models (+69 to +143 Elo) with no further search. On the 8 tabular competitions of MLE-Bench, TabFM-Auto ranks first overall among MLE agents.

---


### 436. [Which Attention Heads are like the Human Head? Not the Ones that Compute](https://arxiv.org/abs/2609.37991)

**<font color=#1a73e8>作者：</font>** Christopher Pinier, Gustaw Opiełka, Hannes Rosenbusch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Brain-AI alignment is often interpreted as a sign that model and brain perform similar computations. Whether the aligned units are causally involved in model computation is rarely checked. On an abstract pattern-completion task (AAABAAA $\rightarrow$ B), we compare LLM attention-head representations with human EEG and test how ablating those heads affects task performance. Alignment and causation dissociate: brain-aligned heads contribute to performance, but their removal is substantially less disruptive than removal of heads selected via attribution patching. We compare two head sets that prior interpretability work defines without reference to the brain: concept vectors (CVs), which represent abstract patterns across formats, and function vectors (FVs), selected for their contribution to correct-answer prediction. Brain alignment shows little association with FV scores, while its association with CV scores varies across models. Among brain-aligned heads, we find recurring attention profiles: one emphasizes distinctive elements (novelty heads), the other repeating elements (repetition heads). The novelty family tracks salience and attends to the same elements that humans look at, yet its removal is less damaging than random ablation on average. Repetition heads contribute modestly to performance and are associated with abstract-pattern representation (CVs). Across 17 models spanning 3B-72B parameters, FV-ranked removal is substantially more disruptive than brain-ranked removal. Brain alignment thus captures how the model reads the stimulus, and only faintly captures how it represents the pattern and solves the task.

---


### 437. [BITEM at the NTCIR-19 R2C2 Task: Predicting Confidence from Agentic RAG Pipeline Signals](https://arxiv.org/abs/2609.37993)

**<font color=#1a73e8>作者：</font>** Julien Knafou, Luc Mottin, Alexandre Flament 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The BITEM team entered both subtasks of the NTCIR-19 R2C2 task with a single agentic pipeline, in which a model searches, reads and records evidence over a movie corpus while an orchestrator holds the record and rules on what may be submitted. A claim is admitted only once an entailment cascade has checked it against the passage it cites, and an answer is released only once enough checked evidence stands behind it. Each question is run three or four times, every pass retrieving from a corpus stripped of what the earlier passes have already seen. The confidence filed with each answer is computed by the orchestrator from what the run leaves behind and is never asked of the model, which is offered no way to rate itself. The two retrieval runs placed 4th and 5th of 22, pooling the passes was worth 0.0709 nDCG@20, and the gain was largest on the multi-hop and post-processing-heavy questions, where the organisers rank the pooled run top of the field. Sixteen of the 25 answer runs were built on passages these two runs supplied, 12 of them filed by other teams. HMR rewards a system whose confidence is high where it answers right and low where it answers wrong. The pipeline reached an accuracy of 0.9219, 6th of 25, while the confidence filed with those answers gave an HMR of 0.4915, 13th. A few rules crafted over those same recorded signals, with no further model call and no further retrieval, raise that to an accuracy of 0.9375, 5th, and an HMR of 0.6985, 9th. Ranking on HMR alone can reward a system for answering wrongly with low confidence, so we propose accHMR, the accuracy multiplied by HMR, which reports the reward in proportion to the accuracy, and on which the revised rules would have scored 0.6549, 5th. For future work, fitting a model on the numbers the pipeline already produces, rather than writing such rules by hand, would be a real step forward.

---


### 438. [Diagnosing and Improving Probabilistic Reasoning in Large Language Models](https://arxiv.org/abs/2609.38005)

**<font color=#1a73e8>作者：</font>** Huaman Sun, Dingcheng Wang, Jason Hartline 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly proposed as decision assistants who must reason probabilistically from available evidence under explicit decision costs. We propose a decision-theoretic framework that decomposes LLMs' decision loss into two components: forming accurate beliefs from provided evidence and translating those beliefs into actions that optimize a provided utility function. Using a synthetic benchmark with known ground truth, we apply the decomposition to characterize probabilistic reasoning in frontier and open-sourced models. We further evaluate whether RL interventions targeting beliefs, decisions, or both improve these components across three domains, whether improvements transfer across components and elicitation formats, and whether decision performance can improve without improvement in belief formation. We find that targeting one component of probabilistic reasoning redistributes decision loss, improving the target without necessarily transferring to others, and that jointly targeting belief formation and decision-making improves both but hinges on matched formats between training and evaluation.

---


### 439. [HARISSA: Inference-Time Self-Checks for Efficient and Safe Local Language Model Deployment](https://arxiv.org/abs/2609.38006)

**<font color=#1a73e8>作者：</font>** Kenan Alkiek, Moontae Lee, David Jurgens 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Running a language model locally offers advantages in privacy, latency, and cost, but local hardware fits only small models, which are less capable than frontier models. The usual remedy for a hard query, escalating it to a cloud model, gives up the privacy and cost advantages of running locally. A deployment that stays local faces two decisions for hard queries instead. First, it can spend more computation on a query, e.g., reasoning before answering, which raises accuracy at a cost in latency, so it must decide which queries are worth the extra computation (efficiency). Second, some queries are beyond the local model, and delivering a wrong answer is worse than deferring the query to a human in the loop, so it must decide which answers are safe to deliver (safety). We show that both decisions can be made from the model's own hidden states. The prefill state, computed before any token is generated, predicts whether the model will answer correctly, and the answer state, at the end of the generated answer, predicts whether that answer is correct. HARISSA fine-tunes the model so that both states predict correctness, then makes both decisions with one policy that cascades through the ways of answering from cheapest to most expensive, skipping a way the prefill state predicts will fail and deferring the query when the answer it stops with is predicted wrong. On a device running a single model, HARISSA is within one accuracy point of chain-of-thought at 2.7 times lower latency. On a server holding four sizes of one model, HARISSA is more accurate than the FrugalGPT and Self-REF cascades at the same latency, and at the same deferral rate the answer state leaves fewer wrong answers than the standard confidence signals in five of six task and setting pairs.

---


### 440. [HybridCUA: Learning to Orchestrate GUI and CLI for Computer-Use Agents](https://arxiv.org/abs/2609.38008)

**<font color=#1a73e8>作者：</font>** Tongbo Chen, Junbo Niu, Zhengxi Lu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer use agents (CUAs) have demonstrated strong capabilities in completing digital tasks. However, existing CUAs either rely solely on graphical user interface (GUI) interactions, which are often inefficient and error prone, or augment GUI interactions with application specific APIs or tools, which require substantial engineering effort and are difficult to scale across applications. We argue that the next generation of CUAs should combine GUI interactions with the command line interface (CLI), leveraging the generality of the GUI and the efficiency of shell commands. A critical challenge, however, is that current models do not know when or how to use the CLI during task execution. To address this challenge, we develop a data construction pipeline that produces three types of trajectories: GUI only, CLI only, and interleaved GUI and CLI trajectories. This pipeline results in HybridCUA-8K, containing 5K hybrid trajectories and 3K verified RLVR tasks. Building on these data, we propose a training framework with two stages: supervised fine tuning on the constructed trajectories, followed by reinforcement learning with our CLI aware rewards that encourages agents to use the CLI selectively and reliably. Experiments show that HybridCUA-9B achieves 53.6% accuracy on OSWorld, improving over the base model by 14.8 percentage points, and improves performance on WindowsAgentArena by 4.0 percentage points. These results demonstrate the effectiveness and cross platform generalizability of the hybrid GUI and CLI paradigm for computer use agents.

---


### 441. [When do data mixtures improve scaling laws? Insights from high-dimensional regression](https://arxiv.org/abs/2609.38011)

**<font color=#1a73e8>作者：</font>** Diyuan Wu, Lehan Chen, Theodor Misiakiewicz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning systems are trained on mixtures of data from different domains, and choosing the right mixture can substantially improve downstream performance. Despite an extensive literature on data mixing and reweighting, existing work is largely empirical and it remains unclear when auxiliary data genuinely improves scaling laws rather than merely providing more samples. To gain insight into this question, we study a high-dimensional mixed-data regression model with a shared regression function, heterogeneous covariances and noise levels, and dataset sizes that may grow at different rates. We establish the minimax risk under an ellipsoidal parameter constraint for the general covariance structure and derive deterministic equivalents for the test error of ridge regression under commutative covariances. We then specialize to a target domain and an auxiliary domain with aligned power-law covariance spectra, where the theory yields explicit scaling laws in terms of spectral decay, target regularity, and the relative growth of the two datasets. These laws identify regimes in which combining data mixtures provably yields a faster scaling rate than using either dataset alone. In particular, improving the scaling law requires a specific interplay between spectra and relative sample sizes of the domains. Our numerical experiments on language models exhibit the same qualitative phenomenon: appropriate data mixtures yield a faster decrease in target-domain test loss than training on either domain alone.

---


### 442. [Prompts Live on an Arc: Gaussian Curricula in Fisher--Rao Coordinates for Rollout-Efficient GRPO](https://arxiv.org/abs/2609.38018)

**<font color=#1a73e8>作者：</font>** Mei Okonkwo, Pixel Nomand, Julian Berg 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group relative policy optimization (GRPO) learns only from prompts whose sampled responses disagree: a group that is entirely correct or entirely incorrect has zero reward variance, contributes no gradient, and still consumes its rollouts. Prompt-selection methods reduce this waste by steering sampling toward intermediate pass rates, but they choose the target, its width, and the uncertainty model heuristically, in raw pass-rate or logit coordinates. We show that GRPO comes with a natural coordinate for pass rates: the arc length $\psi=\arcsin\sqrt{p}$ on the Bernoulli Fisher--Rao manifold. In arc length, the expected GRPO update is uniform up to two boundary ramps; the probability of a zero-variance group is bounded by two Gaussian boundary layers of width $1/\sqrt{2G}$; pass-rate evidence has constant noise; and the gradients of the pass@$k$ and pass$^k$ objectives are Gaussians whose center and width follow from $k$ in closed form. A prompt curriculum for GRPO is therefore a Gaussian in arc length, and choosing its center amounts to choosing the objective. We turn this observation into ARCUS, a drop-in sampler that tracks every prompt with a Kalman filter in arc length, scores prompts by an objective-matched Gaussian kernel times the predicted probability of an informative group, keeps only informative groups for the unchanged GRPO update, and paces the target toward the hardest objective whose predicted yield stays within a small slack of the best. Across six mathematical reasoning benchmarks and three backbones, ARCUS improves the average accuracy of GRPO by 2.8--2.9 points and that of dynamic sampling by 1.1--1.2 points, while generating 48--57\% fewer rollouts than dynamic sampling.

---


### 443. [Auditable Long-Term Memory: A Deterministic Retrieval Chain Measured at 479/475 of 500 on LongMemEval-S](https://arxiv.org/abs/2609.38021)

**<font color=#1a73e8>作者：</font>** Christopher J. Chanhnourack  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We evaluate an auditable long-term memory system on LongMemEval-S. Its retrieval chain uses hybrid candidate retrieval, cross-encoder reranking, coverage-first packet compilation, and deterministic reasoning scaffolds; an LLM is used only as a replaceable final reader. The chain places all gold sessions in the candidate pool for 468/470 answerable questions and produces gold-complete packets for 462/470. With a Claude Opus reader called through an unpinned CLI alias, two 500-question passes score 479/500 and 475/500 under GPT-4o. The 72 answerable knowledge-update rows used a substantively modified scoring prompt whose effect under the official text has not been measured. The pair straddles Chronos High's published 478/500; differences in reader generation, scoring prompt, and possibly data version, plus within-system variance, establish neither superiority nor equivalence. A grok-4.6-high reader on the same packets scores 476/474, while a maximum-reasoning-effort agentic variant regresses to 461/465. The headline passes differ on eight verdict-flip rows. A second judge agrees with the headline judge on 493/500 rows (98.6%) in each pass and scores both passes 472/500; the official judge also flips three verdicts when re-scoring byte-identical pass-1 answers. Negative controls rejected a verifier that repaired three wrong drafts but broke eleven correct drafts. All components were developed on the same 500 questions, with no held-out evaluation or independent human adjudication; retrieval and scaffold method sources and transcript-derived audits are held; and the headline reader received extra operator context, its complete requests were not retained, and MCP tool availability is unresolved. We release materialized packets, scaffolds, reader outputs, judge verdicts, and controls for inspection and re-scoring.

---


### 444. [Dr. OPD: Learning What to Follow for Optimal On-Policy Distillation of Large Language Models](https://arxiv.org/abs/2609.38025)

**<font color=#1a73e8>作者：</font>** Zhenyu Wang, Tianze Wang, Linjun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own generated responses using dense, token-level supervision from a stronger teacher. Vanilla OPD treats all teacher signals equally, assuming that the teacher's supervision is equally important for every token. However, teacher signals at different tokens may have very different effects on the student's performance: some correct important reasoning errors, while others have little effect on the final answer. Motivated by this observation, we introduce Dr. OPD (OPD Done Right), which defines the optimal weighted OPD to maximize the student's performance. We formulate Dr. OPD as a bilevel optimization problem in which the student learns from weighted teacher supervision, while the weights are selected to maximize the expected reward of the resulting student. To solve Dr. OPD, we develop an efficient iterative solver that updates the token weights and student policy alternatively. At each round, it updates weights in closed form and then takes one gradient step on the resulting weighted OPD objective. Under regularity conditions, we show that this weighted update achieves a higher expected reward than a vanilla OPD update. Empirically, across strong-to-weak and same-size distillation on math and code, Dr. OPD consistently outperforms all evaluated baselines. In particular, in the strong-to-weak distillation setting, Dr. OPD improves average math performance by $9.7$ points over vanilla OPD, and enables the smaller student to surpass its larger teacher.

---


### 445. [Layer-Informed Fine-Tuning via Three-Stage Functional Segmentation of LLMs](https://arxiv.org/abs/2609.38027)

**<font color=#1a73e8>作者：</font>** Junning Shao, Siwei Wang, Zhixuan Fang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, the performance of large language models (LLMs) on reasoning tasks has been remarkable, even surpassing human capabilities on various benchmarks. However, there remains a lack of clear understanding in the academic community regarding how the structure and internal parameters of LLMs progressively solve complex reasoning problems. In this study, we investigate the inference process of LLMs on cross-linguistic materials and propose the hypothesis that LLM layers exhibit a structured division of labor across conceptualization, reasoning, and textualization. Based on this hypothesis, we introduce a bottleneck identification mechanism using sensitivity analysis to pinpoint the most critical functional stage for a specific task. Leveraging this insight, we propose a novel approach, Layer-Informed Fine-Tuning (LIFT), which achieves efficient and effective fine-tuning by selectively updating only these functionally critical layers. We then conduct extensive experiments to show that the LIFT method not only accelerates the training process but also significantly improves model performance.

---


### 446. [Critical Thinking with Generative AI: A Constraint-First Design Pilot of a Thinking-Partner Intervention](https://arxiv.org/abs/2609.38029)

**<font color=#1a73e8>作者：</font>** Fatima Tuz Zahra, Jiangen He, David M. Bowers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) tools entered higher education classrooms faster than the field was able to study their effects on learning. One concern is that GenAI may displace the critical thinking and AI literacy that students will need after graduation. This paper reports a Design-Based Research pilot of a GenAI-assisted critical thinking framework, in which ChatGPT was used as a thinking partner in an undergraduate research methods and statistics course during Spring 2025 (N = 14). The mixed-methods design combined pre- and post-intervention measures of statistical learning (AASCDM), AI literacy (MAILS), and critical thinking (WGCTA) with instructor field notes, student artifacts, and student-AI interaction logs. Pre-post tests showed gains on every AASCDM dimension and on eight of nine MAILS dimensions, while WGCTA percentiles did not change. Qualitative analysis identified four themes: the ways students positioned the LLM (as answer generator, validator, or co-thinker); the depth of student engagement (procedural vs. conceptual); occasional humanizing of the tool; and the role of curriculum design in shaping each of the prior three. Read together, the findings indicate that one semester of GenAI-assisted instruction can move domain learning and self-reported AI literacy but does not move standardized critical thinking, and that the modal student-LLM relationship is one of validation instead of dialogue. We end with design principles for the next iteration of the framework and implications for research on adaptive and personalized learning.

---


### 447. [Gender bias across LLMs is common and highly heterogenous](https://arxiv.org/abs/2609.38036)

**<font color=#1a73e8>作者：</font>** Edoardo Bolzoni, Valerio Capraro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding gender biases in large language models (LLMs) is increasingly important as these systems become embedded in decision-support tools with real consequences. Prior research has focused only on a small set of models, leaving open the extent to which gender biases are common and heterogeneous across LLMs. We address this gap across ten models released between April 2025 and June 2026, spanning nine vendors, using two paradigms: gender attribution to stereotyped phrases (Study 1) and moral judgment of abuse or torture against a woman or a man to prevent a catastrophic outcome (Study 2). In Study 1, two of ten models attributed masculine-stereotyped phrases to female writers more often than the reverse, while three models showed the opposite pattern. In Study 2, several models converged on a male-disadvantaging asymmetry that was directionally consistent with a documented human tendency to protect female targets from harm, though the specific conditions under which this asymmetry emerged varied by model; three other models, by contrast, showed no variation across conditions. These results indicate that gender-related biases are common in LLMs. Their direction and magnitude, however, are highly heterogeneous, to the point that some models behave in diametrically opposite ways to others. Bias auditing should therefore be treated as an ongoing, multi-vendor process, rather than a one-time assessment.

---


### 448. [UserProxyBench: Evaluating LLM User Simulators for Agent Benchmarks and Training](https://arxiv.org/abs/2609.38043)

**<font color=#1a73e8>作者：</font>** Ashish Jain, Armaan Sandhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive agent benchmarks and multi-turn reinforcement learning increasingly place a second language model in the role of the user. This simulated user controls what information the agent receives and when, yet current benchmarks score only the agent and do not directly measure whether the user correctly executed its assigned role. We introduce UserProxyBench, an evaluation layer over the tau-bench family, and the User Fidelity Score (UFS), which measures adherence to the benchmark's private user instructions using task-grounded rubric criteria scored independently of agent success. Holding the agent fixed at GPT-5.5 and varying only the user proxy across 375 enterprise tasks changes mean task reward by 15.2 points, while 24.4% of successful episodes contain a user-specification violation. The dominant failure is premature disclosure: users provide information before it is requested. This behavior has little effect on task reward, yet among successful episodes it causes the agent to make 1.06 fewer tool calls on average, changing the interaction being evaluated while preserving the reward. Finally, across seven proxies we identify an empirical cost-fidelity frontier, enabling practitioners to select the least expensive simulator that satisfies a required fidelity level.

---


### 449. [EVO-WAM: Evolving World Action Models through Video-Action Verification](https://arxiv.org/abs/2609.38057)

**<font color=#1a73e8>作者：</font>** Shiyang Zhou, Xionghao Wu, Wenbo Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Improving robot policies on new tasks without collecting additional expert demonstrations remains a central challenge in robot learning. World action models (WAMs) use broad video priors to jointly predict future videos and actions, offering a potential source of supervision for adapting to new tasks. However, generated videos may fail to depict task completion, and even visually successful videos may be paired with inconsistent actions that lead to execution failure. We propose EVO-WAM, a framework that adapts WAMs to unseen tasks by learning from their own generated video-action trajectories, without executing candidate actions in an external environment. First, we augment WAM training with state prediction and anchored multi-frame context to enable complete autoregressive rollouts without external execution feedback. Second, we identify reliable training experience by selecting task-completing prefixes with a vision-language model and verifying their video-action consistency with an inverse dynamics model. Third, we iteratively train the WAM on verified prefixes and generate new rollouts with the updated model. On seven unseen RoboTwin 2.0 tasks, EVO-WAM increases average success rates from 26.9% to 68.0% for Cosmos3 and from 28.5% to 46.4% for DreamZero, reaching approximately $2.5\times$ and $1.6\times$ their initial success rates. On three unseen long-horizon composite tasks in the real world, it improves Cosmos3's average success rate from 20.0% to 76.7%, a gain of 56.7 percentage points. Project Page: this https URL.

---


### 450. [Alpha Diffusion Language Models: Factorization Alone Is Not the Problem](https://arxiv.org/abs/2609.38066)

**<font color=#1a73e8>作者：</font>** Nikita Gushchin, Dmitry Baranchuk, Alexander Korotin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion language models can generate multiple tokens in parallel, but reducing the number of denoising steps can lead to inconsistent predictions. Standard cross-entropy training fits conditional token marginals, whereas parallel generation requires consistent joint predictions. We introduce Alpha Diffusion Language Models (AlphaDLM), trained with a sequence-level alpha loss that recovers cross-entropy in the limit of vanishing alpha and has a joint-mode optimum at alpha one. Our analysis characterizes how the objective and factorization jointly determine the fitted distribution. We identify conditions under which intermediate alpha preserves multiple valid completions while excluding invalid token combinations. Trained on TinyGSM, our method achieves 34.6% accuracy on GSM8K with only four model evaluations. We further scale the method to SDAR-1.7B and evaluate it on code and mathematics benchmarks. These results show that changing the training objective can improve the accuracy-computation trade-off of factorized diffusion language models.

---


> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
