# 🧠 大模型相关研究 | 2026年11月27日

> 本类共 **267** 篇论文：已确认 **249** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-267**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-267**

---

### 251. [CovNovBench: A Benchmark for Evaluating Time Series Foundation Models under Covariate Novelty](https://arxiv.org/abs/2611.33732)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wenhao Pan, Ravi Kiran Selvam, Michael W. Mahoney 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Covariate-aware time-series foundation models (TSFMs) condition their forecasts on additional input variables, called covariates, that are supplied over the future horizon. This capability makes them appealing for interventional forecasting, in which a target is predicted under a planned action such as a new product pricing policy or a new patient treatment schedule. We refer to covariates that encode such actions as treatment covariates. Current covariate-aware TSFMs, however, are trained on observed patterns, and their behavior is unclear when future treatment covariates fall outside the range seen in the history. Examples include a numerical treatment that leaves its historical range and a categorical treatment that takes a previously unseen policy. We call this practically common setting covariate novelty, and note that it is not systematically represented in existing benchmarks. We introduce an operational definition of covariate novelty and use it to construct CovNovBench, a benchmark of 88,476 evaluation series generated or filtered from four simulator-based and real-world datasets. The benchmark spans categorical and numerical treatment covariates as well as stable and trending targets. We evaluate six covariate-aware TSFMs zero-shot using point and directional accuracy metrics. No model is consistently reliable in our benchmark: point error almost always increases under covariate novelty, directional performance changes non-uniformly, and the best observed model varies across datasets and metrics. CovNovBench provides a systematic testbed for developing TSFMs that forecast more reliably under covariate novelty.

---


### 252. [Teaching Students to Stand on Their Own: Distilling Vision Foundation Models for Fine-Grained Few-Shot Class-Incremental Learning](https://arxiv.org/abs/2611.33749)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junsu Kim, Seungryul Baek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained few-shot class-incremental learning (FG-FSCIL) aims to incrementally learn visually similar new classes from limited images without catastrophic forgetting. Prior work typically learns strong representations on base classes or leverages vision foundation models (VFMs) directly as backbones or via knowledge distillation. However, VFM backbones incur high computational costs and do not guarantee fine-grained recognition. Although knowledge distillation reduces inference cost, our preliminary experiments reveal that distilled students still lag substantially behind their VFM teachers, particularly on new classes. To address this limitation, we propose STAND, a systematic VFM-to-student distillation design tailored for FG-FSCIL. Specifically, STAND connects the teacher and student by equipping the student with a fixed copy of the teacher's classifier, aligning their outputs via projectors, and feeding both models composite images that combine different training images. On these composite images, relation distillation matches how the teacher and the student relate each image to other images, while difference distillation matches how this relation changes between two composite images. Finally, we freeze the student and classify new classes using length-calibrated prototypes, which restore the reduced similarity of few-shot prototypes. Extensive evaluations demonstrate that STAND achieves state-of-the-art performance across FG-FSCIL datasets at low computational cost, while generalizing across student backbones and broader datasets.

---


### 253. [Spectral Colorimetry Based on GMoE for Temperature Measurement in Explosion Fields](https://arxiv.org/abs/2611.33750)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jie Fang, Wenhao Li, Jianning Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spectroscopic thermometry in explosion fields has attracted considerable attention in related engineering domains, primarily because it can mitigate the interference of traditional contact methods with temperature distributions and address the limitations of high-temperature measurement scenarios. However, existing physics-model-driven methods typically rely on regressing a single radiance-ratio pair, which limits their adaptability to wide-range temperature estimation. This limitation arises from notable variations in the mapping between grayscale ratios and radiance ratios at different temperatures. In contrast, existing data-driven methods often suffer from limited performance due to the scarcity of training data, a challenge exacerbated by the sensitivity of explosion fields. In this work, we propose a gated mixture of experts (GMoE) framework that integrates a divide-and-conquer strategy in deep learning with physical prior knowledge for temperature estimation, thereby decomposing the complex task into multiple expert-specific subtasks. Specifically, each expert is developed using physically calibrated polynomial functions to model the relationship between grayscale ratios and radiance ratios for a given pair of spectral bands, with temperature then estimated using a physical model incorporating the corresponding parameters. Additionally, a gating network is designed to adaptively weight the outputs of different experts and generate the final temperature estimate. Experimental results demonstrate that the proposed framework achieves the best performance when implemented with the Transformer-based gating network, yielding a mean RMSE of $12.70 \pm 1.32$ K and a mean MAE of $7.96 \pm 0.86$ K. Compared with conventional spectral colorimetry, the proposed framework reduces the mean RMSE and MAE by 63.4\% and 70.8\%, respectively.

---


### 254. [Hybrid Reinforcement Learning for One-step Degraded Infrared and Visible Image Fusion](https://arxiv.org/abs/2611.33857)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hongwei Yu, Daoqing Zha, Jiawei Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared and visible image fusion (IVIF) is essential for robust perception, yet existing methods remain limited under complex degradations. While diffusion models (DMs) offer powerful modeling capabilities to combat such degradations, their iterative process incurs high computational cost. One-step distillation effectively accelerates inference but typically leads to over-smoothed results. To resolve these limitations, we propose a one-step fusion framework with hybrid reinforcement learning, termed OneHRL. We treat degraded inputs as intermediate noisy states along a generative trajectory, enabling a distilled one-step generator to rectify them directly to the clean fusion results. Concurrently, to mitigate the over-smoothed results in distillation, we incorporate the Flow-GRPO paradigm to introduce stochasticity into the deterministic one-step generation. This restores the stochastic exploration necessary for sampling-based reinforcement learning. Furthermore, we design a coarse-to-fine reward that integrates a global semantic reward with an object-level reward. This hybrid reward ensures that the generator captures both naturalness and fine-grained texture. Extensive experiments demonstrate that our method achieves superior fusion quality and efficiency.

---


### 255. [DuoMI: Dual Mutual Information Regularization for Expert Reuse in Looped Transformers](https://arxiv.org/abs/2611.33952)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xinlai Kang, Zhenhe Wu, Haoyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Dual Mutual Information Regularization (DuoMI), a method for regulating expert routing across rounds in looped mixture-of-experts (MoE) Transformers. When two rounds of computation share an expert pool, their routers may favor different expert subsets, limiting the reuse of individual expert parameters across rounds. Even when aggregate expert usage is identical across rounds, we would still prefer each token to retain some experts while switching to others. DuoMI addresses both aspects of routing: it uses round-level marginal mutual information to limit the dependence of aggregate expert usage on the round, and token-level conditional mutual information to penalize average cross-round routing changes that fall outside a target interval. During training, DuoMI computes differentiable penalties from soft routing distributions over all experts. It adds no model parameters and leaves sparse Top-$k$ routing strategy unchanged at inference. On a looped OLMoE backbone in which paired adjacent layers share experts, DuoMI improves the average score across $15$ downstream tasks from $50.08\%$ to $51.82\%$, a gain of $1.74$ percentage points over the looped baseline.

---


### 256. [geo-eval-harness: An Evaluation Harness for Geospatial Foundation Models](https://arxiv.org/abs/2611.33990)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nils Lehmann, Caleb Robinson, Isaac Corley 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation model (GFM) research papers are plagued by inconsistent evaluation settings (e.g., different pre-processing and probes), making it difficult to separate performance from evaluation choices. We propose geo-eval-harness}, an open-source framework for controlled model comparisons. We use this harness to evaluate 100 GFMs and general vision models on 6 classification and 14 segmentation datasets, using multiple probes on frozen or low-rank-adapted encoders. We show that under controlled evaluation, general vision backbones are competitive on RGB classification and high-resolution segmentation, but GFMs shine on multispectral tasks. When we compare any two of the top-ten classification models on a single dataset, their 95% confidence intervals overlap 73% of the time. We show that bigger models are not always better: inference FLOPs correlate weakly with segmentation performance. Moreover, translating inference compute into large-area mapping workloads shows how small accuracy differences have outsized deployment cost differences: with frozen encoders on SpaceNet2, a 0.9-point mIoU difference corresponds to 5.9x the compute and days of additional projected GPU time. Our findings stress the importance of comparing models under explicit and fixed settings, and reporting uncertainty and deployment compute alongside accuracy. Our geo-eval-harness makes controlled experiments easy, fast, and fully reproducible. We release the code, configurations, and results at this https URL.

---


### 257. [MoSk: A Unified Motion-Skeleton Foundation Model for Human Motion Understanding and Generation](https://arxiv.org/abs/2611.34022)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yun Chen, Munchurl Kim, Jeonghyeok Do  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models (FMs) have advanced visual understanding and generation by providing semantically rich representations. However, this role of FMs remains underexplored in human motion. Large motion datasets offer diverse movements at scale, but often lack action labels for systematically evaluating learned representations on understanding tasks. Skeleton datasets enable such evaluation through established recognition protocols, yet are typically smaller and focus on predefined actions captured in controlled environments. To combine these strengths, we present MoSk, to the best of our knowledge, the first Motion-Skeleton foundation model to integrate motion and skeleton datasets. MoSk learns shared representations through self-supervised masked motion modeling. We incorporate joint-name embeddings to provide a common anatomical reference across various skeleton formats. A cross-attention decoder reconstructs masked motion from the encoder's features, with joint-name embeddings specifying the target joints. Experiments demonstrate strong action-recognition performance across diverse settings, including linear evaluation and fine-tuning. MoSk also substantially improves motion generation across multiple backbones through representation alignment, reducing FID on MotionMillion by up to 9.75 for unconditional generation and 3.83 for text-to-motion generation.

---


### 258. [Text-Conditioned Low-Rank Adaptation of Time-Series Foundation Models for Multimodal Forecasting](https://arxiv.org/abs/2611.34206)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kunqi Li, Bin Liang, Zhidong Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models (TSFMs) provide transferable numerical forecasting priors. However, forecast-relevant information may be conveyed in text without being reflected in the observed series. Many multimodal forecasting methods integrate such context through model inputs or intermediate representations. We investigate a complementary mechanism: text-conditioned parameter adaptation. We propose Context-to-LoRA for Time Series (C2LoRA-TS), which encodes text and generates temporary Low-Rank Adaptation (LoRA) updates for selected weight matrices of a frozen TSFM. Both the numerical backbone and text encoder remain frozen, and the method exactly recovers the frozen TSFM output when context is absent. Evaluated on Time-MMD across nine domains and three TSFM architectures, C2LoRA-TS achieves lower aggregate forecasting error than the frozen-TSFM and Static LoRA baselines for every architecture and seed. Replacing the instance-specific text with a single globally fixed context degrades performance for every architecture. These results support text-conditioned parameter generation as a viable strategy for multimodal forecasting with frozen TSFMs.

---


### 259. [Analemma $\infty$: A Temporal Benchmark for Geospatial Foundation Models](https://arxiv.org/abs/2611.34240)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alex López-Cifuentes, Laura Martínez-Ferrer, Juan Ignacio Bravo Pérez-Villar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite time series capture how land surfaces change over time. Pixel-wise temporal foundation models read a year of satellite observations per pixel, yet public benchmarks lack a temporal axis or subsample it to a few dates. We introduce Analemma, a temporal benchmark of six datasets that carry every 10 and 20 m Sentinel-2 band and a time series spanning a growing season, completed where their releases omit geometry, dates, or cloud masks. One frozen-encoder protocol evaluates all models across label ratios and three seeds, with two baselines without pretraining. The TESSERA model ranks first overall. A from-scratch model on monthly composites outranks every foundation model except OlmoEarth v1.3-Base, suggesting that temporal input explains most of the performance. Three evaluation choices left unstated by the source publications each shift TESSERA v1 by 7.6 to 18.6 mIoU, against top-two gaps of 0.6 to 2.8. Data, harness and leaderboard will be publicly released soon.

---


### 260. [StateWeaver: Multi-Agent Coordination of Story-State Transitions for Long-Horizon Video Generation](https://arxiv.org/abs/2611.34290)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Modi Jin, Xuying Zhang, Yijing Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video foundation models generate high-quality short clips, but preserving long-video consistency and correctly depicting event-driven state changes remain challenging. Existing agentic workflows face these challenges because continual planning and repair accumulate context, while reference updates remain limited. We introduce StateWeaver, which combines Active States and Hierarchical Collaboration to connect review-driven visual reference updates with cross-shot state inheritance. Active States translate state discrepancies identified during review into concrete visual asset requirements that guide reference construction, validation, and regeneration, preserving identity and already-correct content while repairing target attributes. Confirmed generation results are linked to the corresponding asset states, story time, and reference versions for verification and reuse by subsequent shots. Hierarchical Collaboration isolates execution contexts by task, clip, and repair round, and uses hierarchical memory to organize this process across multiple sets. Across multiple benchmarks, StateWeaver outperforms existing methods and produces long videos with sustained cross-shot consistency under predefined and autonomously planned storyboards.

---


### 261. [Learning from Unreliable Operator References: Claim-Level Rewards for Customer Support Agents](https://arxiv.org/abs/2611.34341)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dmitrii Stoianov, Olga Tsymboi, Danil Taranets 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Even a correct operator reply can be an unreliable training target for a customer-support agent. About a quarter of the factual claims in these replies lacked full support in the agent's knowledge base and tool records. We treat operator replies as claims to verify rather than answers to imitate. Unverified claims guide revisions to the knowledge base and tools. Verified claims serve as coverage targets in a claim-level GRPO reward that scores factual precision against the evidence the agent retrieved for its answer. On an offline benchmark, 8.6% of the GRPO agent's text answers were flagged for hallucinations, compared with 13.6% for the supervised fine-tuning baseline. In a randomized A/B test against the existing procedural bot, the deployed system increased the share of conversations closed without a human operator from 63.3% to 80.8%.

---


### 262. [Single-Database Rewards Are Hackable: Counterfactual Execution for Trustworthy Text-to-SQL RL](https://arxiv.org/abs/2611.34363)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shreshth Rai, Rishii Kumar Singh, Aksh Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for text-to-SQL agents pays a query when its result matches the reference on one database. However, a wrong query can match by luck when the data lack the rows that expose its bug. We study a counterfactual-database (CF) reward that also runs the final query on a few hidden, code-generated copies of the database and pays only if all results match (strict form) or by the share matched (mean form). On 1,302 synthetic audit questions, the strict form lowers the share of buggy queries paid in full from 29.5% to 16.8% and of reward hacks from 54.1% to 1.9%, rejecting 0 of 2,847 correct queries; copies from a family-blind generator do about as well. In a controlled GRPO comparison on a 3.35B model with three seeds per arm, training on the mean form did not improve in-domain accuracy (8.4% vs 11.7%), because the two rewards disagreed on only 5-7% of rollouts; on Spider it gained 1.6 points. One seed reverses both signs, so single-seed reward comparisons mislead. Code: this https URL ; data, models, demo: this https URL

---


### 263. [When to Trust a PFN: Detecting Harmful Shift in Tabular Foundation Models](https://arxiv.org/abs/2611.34767)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Viet Nguyen, Herman Bergström, Stephan Rabanser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular prior-fitted networks (PFNs) work well across tabular classification problems but can fail silently at deployment when distributions shift. We propose CALD (Calibrated Anchor-Loss Disagreement), a lightweight unsupervised monitor that triggers an alarm to warn when a PFN might fail. By finetuning the decoder to maximize disagreement with the test-set prediction while maintaining accuracy on an ID anchor set, CALD identifies harmful OOD batches through the resulting anchor loss, requiring no labels on test batches. We prove that the post-finetune anchor loss has a strictly lower expectation under sufficiently severe shift than under ID eval, yielding a one-sided test. Across 14 datasets covering tabular and structured distribution shift, on both TabPFN and TabICL, CALD matches or outperforms baselines on harmful shifts and is markedly more resilient to benign-shift false alarms.

---


### 264. [When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon Agent RL](https://arxiv.org/abs/2611.34777)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haowen Hou, Yicheng Liu, Zhen Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning with verifiable rewards often yields all-fail groups on long-horizon agent tasks: every sampled trajectory receives zero reward, leaving group-relative methods without a reward-based policy gradient. A common remedy supplies complete solutions from a stronger model, but full trajectories are expensive and expose the learner to long off-policy histories. We introduce SPLICE, which constructs local training targets from failed current-policy trajectories online. For each all-fail group, a proposal model selects a splice point in a current-policy trajectory and generates several bounded options from that point. We estimate each option's value using repeated current-policy continuations, convert positive estimates into a return-weighted local target, and fit the current policy on the options. We evaluate SPLICE across two policy families on two long-horizon agent tasks, Software Engineering with SWE-bench Verified and Deep Research with BrowseComp-Plus. SPLICE outperforms GRPO and full-trajectory guidance baselines in all four settings, improving over GRPO by 2.8--9.8 percentage points. On initially failed SWE tasks, it raises GRPO's graduation rate by 10.8 percentage points. Further experiments show that SPLICE improves performance while reducing costly proposal-model computation.

---


### 265. [From Prediction to Decision: Decision-Focused Fine-Tuning of Autoregressive Tabular Transformers for Cost-Sensitive Financial Events](https://arxiv.org/abs/2611.34858)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ashkan Golgoon, Giacomo Domeniconi, Samuel Atkins 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive transformers trained on tokenized tabular event streams are a simple and strong baseline for predicting financial events such as fraud. Yet institutions do not act on probabilities; they act on decisions whose consequences are asymmetric and heteroscedastic: the cost of a missed high-value fraud and that of a wrongly declined small purchase are not the same. The standard bridge is post-hoc Bayes-optimal thresholding of calibrated probabilities under a cost matrix. We ask whether fine-tuning the model to the decision objective can do better. We fine-tune the same pretrained model so that its restricted softmax over label tokens (already a distribution over business actions) maximizes expected utility under an institution-specified, amount-scaled cost matrix. Because the reward is a known function of (action, outcome, amount) and the outcome is observed in the data, the expected-utility objective and its gradient are available in closed form. This is example-dependent cost-sensitive learning whose per-example loss is linear in the predicted probability, with no sampling, critics, or advantage estimation. A KL anchor to the pretrained model and an auxiliary language-modeling term preserve calibration and the generative event model. A sampled, group-normalized (GRPO-style) variant provides the extension point to trajectory-level rewards.

---


### 266. [LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE](https://arxiv.org/abs/2611.34912)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiachen An, Sijie Zhao, Le Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While video diffusion models have grown faster and increasingly streamable, the video VAE remains a primary latency bottleneck across interactive generation and editing pipelines. Existing VAEs and their acceleration methods rely mainly on heavy convolutions or full frame attention, and most focus only on decoding, leaving encoding costly for streaming conditional generation and editing. This raises a natural question: Do video VAE encoding and decoding actually require such global spatiotemporal modeling? By analyzing the effective receptive fields of pretrained video VAEs, we find that both encoding and decoding a patch rely almost entirely on its spatial and temporal neighbors. To exploit this strong locality, we introduce LiveVAE, a streaming encoder and decoder built on causal window attention, which cuts per frame compute while keeping the temporal KV cache bounded for streaming. Decoupled encoder/decoder distillation followed by joint finetuning preserves the pretrained latent space, making LiveVAE a drop-in replacement for the original VAE. On MiniMax-H3, LiveVAE achieves 5.2-6.2x faster encoding and 3.0-3.3x faster decoding than the official VAE with higher PSNR. Paired with our dedicated inference infrastructure, LiveVAE pushes the speedup to 13.4x with almost no quality loss. Code and models will be released.

---


### 267. [A gene informed benchmark for BioScoring of pathology foundation models](https://arxiv.org/abs/2611.34930)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Paul Vilars, Vincent Quoc-Huy Trinh, Maria Vakalopoulou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models are usually compared by their performance on downstream tasks such as classification and retrieval. While such benchmarks measure how useful a model is, they provide no insight into the biology it represents. We introduce BioScore, a benchmark that quantifies how well an image encoder captures cell identities, with spatial transcriptomics of the same tissue as the reference. A sparse autoencoder splits the encoder's patch embeddings into sparse features, which we cluster into a fixed number of groups. BioScore then measures, for each of 52 cell identities defined by marker genes, how specifically one group follows the identity's expression over the tissue. Because the autoencoder training is fully unsupervised, a match shows that the model represents the cell identity from the image alone. We score 8 pathology foundation models and 3 natural-image models. Every pathology model scores above every natural-image model (0.299--0.371 \vs 0.214--0.232), and paired tests separate three tiers among the pathology models. Unlike a supervised probe, BioScore needs no labels, builds its reference from the data and scores even from few sections, yet it ranks the encoders as a probe does. Its per-identity breakdown indicates which cell identities each encoder captures or misses.

---


> [!TIP]
> 当前位于：**251-267**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-267**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
