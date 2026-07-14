# 📦 其他研究 | 2026年07月15日

> 本类共 **420** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-420](./part-09.md)

---

### 351. [Enhancing Query Efficiency for d-DNNF Representations Through Preprocessing](https://arxiv.org/abs/2607.11492)

**<font color=#1a73e8>作者：</font>** Jean Marie Lagniez, Emmanuel Lonca  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we investigate preprocessing techniques aimed at improving the efficiency of accessing models of propositional formulas represented in conjunctive normal form (CNF). We focus on three fundamental tasks: uniform sampling, direct model access, and model enumeration. Our analysis reveals that most state-of-the-art preprocessors, when they do not preserve formula equivalence, are generally unsuitable for these tasks. In contrast, we demonstrate that preprocessors which preserve model counts can be effectively leveraged, provided relevant preprocessing information is maintained. To validate our approach, we perform extensive experiments on a diverse suite of benchmarks from multiple domains. The experimental results show that our preprocessing methods are both efficient and robust, yielding significant performance improvements for model access queries when CNF formulas are compiled into d-DNNF representations.

---


### 352. [Time Is Money: Incentivized Causal Transaction Ordering](https://arxiv.org/abs/2607.11496)

**<font color=#1a73e8>作者：</font>** Hongyin Chen, Xu Zheng, Jichen Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Front-running is a subtle and persistent problem for blockchains. A blockchain is a stateful virtual machine executing instructions called transactions. Users earn rewards by publishing functional transactions essential to the system. Attackers observe these transactions and publish their own ahead of the users', seizing the reward and eroding users' incentive to publish functional transactions. Preventing front-running means enforcing causality: If an attacker receives transaction tx_A and then publishes transaction tx_B, then tx_A must be ordered before tx_B. However, this causality is only observed by the attacker. Practical systems order transactions by bid amount, so transactions willing to pay more get executed first, but this only results in a bidding war eroding users' rewards. Though numerous ordering approaches have been proposed, none achieves causality, leaving users vulnerable to front-running.
We present PRECEDE, a mechanism-design approach that enforces transaction causality by removing the economic incentive to front-run. PRECEDE orders transactions by a power-weighted randomized lottery, whose winning probability grows super-linearly in the bid. The user's strategy of publishing a transaction with a deterring bid forms an equilibrium where the attacker refrains from competing. Moreover, PRECEDE prevents the prominent sandwich attack, which relies on front-running. PRECEDE can be directly deployed in any censorship-resistant blockchain with a simple change to its transaction ordering mechanism.

---


### 353. [IG-GAN: A Generative Adversarial Network for Aerodynamic Data Generation Based on Intrinsic Geometry](https://arxiv.org/abs/2607.11497)

**<font color=#1a73e8>作者：</font>** Ying Yan, Liwei Hu, Xiaoming Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing generative models learn data distributions in flat Euclidean space. However, most data in our real world are manifolds embedded in high dimensional Euclidean space. Therefore, we propose an intrinsic-geometry-based generative adversarial network (IG-GAN) for data generation in the field of aerodynamics. The generator of the IG-GAN represents aerodynamic data as a piecewise smooth manifold constructed by Bézier surfaces, and the generator tries to learn the coefficients of each Bézier surface to further combine multiple Bézier surfaces into a smooth manifold automatically. The discriminator in the IG-GAN is a radial-basis-function based discriminator (RBF-D). Experimental results show that IG-GAN achieves lower predicted Mean Squared Errors (MSEs) than those of three baselines. Specifically, on the Burgers' equation dataset, IG-GAN reduces the predicted MSE of velocity u by 97.41% compared with state of the art SSL-Transformer. Additionally, on the ONERA M6 aircraft dataset, IG-GAN reduces the overall MSE of nine aerodynamic coefficients by 82.95% compared with SSL-Transformer.

---


### 354. [HyperGS: Fast and Generalizable Gaussian Video Representation](https://arxiv.org/abs/2607.11500)

**<font color=#1a73e8>作者：</font>** Fatimah Zohra, Chen Zhao, Shuming Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian Splatting has emerged as an effective representation for video, but existing methods rely on per-video optimization. This leads to slow encoding and limits generalization across videos. To amortize this optimization, we propose HyperGS, a feedforward, optimization-free approach that directly predicts Gaussian representations from any video in a single forward pass, speeding up encoding and decoding by orders of magnitude while generalizing to out-of-distribution videos at higher resolutions. In HyperGS, we design a factorized spatiotemporal Transformer to extract tokens from video, and a learnable query-based Transformer to obtain 8-parameter Gaussian representations for each video frame. We find that naively predicting Gaussians across diverse videos induces a needle-like degeneration that collapses training, and address this with a rank-based geometric regularizer whose strength adapts dynamically to stabilize optimization. HyperGS achieves encoding at $10^4$--$10^5\times$ the speed of per-video Gaussian optimization at matched reconstruction quality while generalizing zero-shot to $720p$ video, enabling higher-resolution rendering without re-encoding. HyperGS improves PSNR by +2.9--3.1 dB over the prior video encoders on K400, SSv2, and UCF101 at a smaller video representation size. By predicting explicit 2D Gaussians in a single forward pass, HyperGS combines the fast, flexible rendering of Gaussian Splatting with the speed and generalization of feedforward prediction, advancing Gaussians as a practical direction for fast and generalizable video representation.

---


### 355. [Comparative Analysis of GAT and BERT for Human-Like Playtesting](https://arxiv.org/abs/2607.11501)

**<font color=#1a73e8>作者：</font>** Kleio Fragkedaki, Theodoros Panagiotakopoulos, Matteo Biasielli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurately modeling and understanding player experience is crucial for designing engaging puzzle games. To achieve this, a common approach involves collecting diverse user data to train predictive playtesting models that mimic player behavior. However, existing data-driven methods often lack the ability to capture the full range of player strategies and require extensive feature engineering and network architecture modeling. This limitation becomes particularly evident when new game mechanics or features are introduced, which necessitate continual adjustments to the models. To addrss these challenges, we propose a more generalized representation that reduces - or even eliminates - the need for ongoing feature-engineering maintenance. Specifically, we investigate two general-purpose network architectures: (a) a transformer-based model (BERT) and (b) a graph attention model (GAT), both of which are designed to effectively capture the relational structure of Candy Crush Saga (CCS) game boards. Our experiments compare these approaches to Convolutional Neural Networks (CNN) baselines, revealing better performance on challenging board configurations and underscoring the benefits of our generalizable representation.

---


### 356. [GEIS: A Generation-Evaluation-Improvement Loop of Agent Skills for Long-Form Article Generation](https://arxiv.org/abs/2607.11503)

**<font color=#1a73e8>作者：</font>** Jiale Zhang, Juntao Hu, Zhijian Ou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form article generation remains difficult for large language models because it combines long context, long instructions, and long outputs. Existing multi-agent pipelines such as STORM improve information coverage by simulating role-specialized agents, but their capabilities are often entangled in prompts and fixed procedures, making them hard to inspect, reuse, or iteratively improve. This paper presents GEIS (Generation-Evaluation-Improvement loop of agent Skills), a loop of named and declarative skills for Wikipedia-style long-form article generation. Implemented and evaluated in Tasi Harness, GEIS composes skills for article writing, browser-based evidence and image collection, diagram rendering, PDF-aware pairwise evaluation, and rule-level skill improvement. Its core writing skill follows Request, Plan, Draft, Audit, Refine, and Deliver; the pairwise evaluation skill produces structured quality reports; and the improvement skill maps recurrent findings into permanent patches to the writing skill in our 20-topic experiment. We evaluate GEIS on 20 Wikipedia Featured Article topics. Under the same generation backend, GEIS improves over the Tasi Harness default writer by 8.0 points on a 100-point PDF quality rubric and outperforms STORM on the two comparable writing dimensions, structural quality and content quality. In the 20-topic improvement experiment, the patched writing skill raises the average score from 82.90 to 86.95, with 17 out of 20 topics improved and the gain mainly coming from content quality. These results show that long-form generation can be reframed from a fixed workflow into an inspectable, modular, and evaluation-guided improvement loop.

---


### 357. [SCOPE-RL: Optimizing Reasoning Paths Before and After Success](https://arxiv.org/abs/2607.11506)

**<font color=#1a73e8>作者：</font>** Xiaojian Liu, Han Xu, Jianqiang Xia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) optimizes LLMs using sparse verifiable final-answer rewards. This sparse anchor reliably verifies whether a trajectory succeeds but provides no direct feedback on the reasoning path that produced it. Before success, prerequisite progress on hard problems receives no reward signal; after success, outcome rewards cannot distinguish well-organized correct trajectories from redundant or locally flawed ones. We introduce SCOPE-RL (Scaffolded Chain Optimization with Process Efficiency), a two-stage framework that densifies this anchor while retaining the GRPO update: Adaptive Scaffolded RL adds prefix-decomposed verifiable rewards on answer-hidden sub-question chains before success, and Quality-Aware Process RL applies correctness-gated process-shape rewards to refine correct trajectories after success. An expert-validated Step-Quality Evaluation Protocol evaluates useful-step density, error localization, and token efficiency beyond final-answer accuracy. On Qwen3-8B-Instruct trained on DAPO-Math and Big-Math, SCOPE-RL improves average accuracy by up to 11.2 pp and reduces reasoning tokens by up to 27.1% over outcome-only GRPO; the gains hold under GSPO and on Qwen3-0.6B-Instruct, indicating that reward-signal densification is complementary to policy-update-level RLVR advances. Code and data are available at this https URL.

---


### 358. [CFR-Net:Collaborative Feature Refnement Network for Medical Image Anomaly Detection](https://arxiv.org/abs/2607.11509)

**<font color=#1a73e8>作者：</font>** Zihan Nie, Muhao Xu, Wei Feng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image anomaly detection remains challenging because networks pretrained on natural images often exhibit limited adaptability to medical images, where abnormal patterns appear as fine-grained local shifts, multi-scale contextual mismatches, and orientation-sensitive structural deviations. To address this, we propose the Collaborative Feature Refinement Network (CFR-Net), which combines shared teacher-student feature refinement before decoding with cross-space consistency after decoding. CFR-Net refines frozen teacher features and trainable student features using a Multi-Path Feature Refinement Module (MPFRM) with shared parameters, imposing common multi-path refinement rules on generic visual references and representations adapted to the medical domain, thereby mitigating domain discrepancy while modeling local, multi-scale, and orientation-sensitive feature characteristics. A variance-sensitive objective and dynamic ``homework set'' reorganization further support layer-adaptive consistency learning. Experiments on medical benchmarks show that CFR-Net achieves competitive anomaly classification and strong anomaly localization performance when trained on normal data.

---


### 359. [Toward Inclusive Avatar Design with Limb Differences Through Artificial Intelligence](https://arxiv.org/abs/2607.11512)

**<font color=#1a73e8>作者：</font>** Fernanda Miyuki Yamada, João Paulo Gois, Hiroki Takahashi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As extended reality becomes more popular for social interaction and entertainment, 3D avatars must represent the full diversity of body types. Most 3D avatar systems only support normative bodies and do not accurately depict people with limb differences, amputations, or other morphological variations. This paper reviews emerging technical approaches for inclusive 3D avatar customization for this group and current guidelines that promote respectful and accurate representation. We highlight persistent challenges, including the scarcity of diverse datasets and the limitations in animation for non-normative anatomies. This paper positions artificial intelligence as a promising path to overcoming these limitations and advancing inclusive 3D avatar generation.

---


### 360. [Dzongkha Next Word Prediction System](https://arxiv.org/abs/2607.11515)

**<font color=#1a73e8>作者：</font>** Prerna Chhetri, Tenzin Yoezer, Phuntsho Wangmo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dzongkha, being the national language of Bhutan, is a common and widely spoken language in the country. Official documents, scriptures and other literature products are written in Dzongkha in order to retain the cultural value. However, documenting Dzongkha writing is a challenging and time-consuming process, largely due to the complexity of the script, the need for multiple keystrokes per syllable, and the limited availability of efficient typing tools. An immediate system that can predict and display a list of probable words for Dzongkha is the solution for this problem. The project is mainly aimed to make Dzongkha typing as convenient as possible by reducing the number of keystrokes. Our dataset is acquired from DCDD and has a total of 100000 sentences, 1331282 words and 28344 unique words. The data preprocessing was done by removing all the alphanumeric characters, tokenization, generating N-gram sequences and padding. Three models selected for training are LSTM, Bi-LSTM and GRU. The training process included fine-tuning of the model's hyperparameters. GRU being lightweight and able to handle larger datasets performed best with 74.03% accuracy and also solved the problem of overfitting.

---


### 361. [Vinci2: Providing Proactive Assistance in Continuous Egocentric Videos](https://arxiv.org/abs/2607.11523)

**<font color=#1a73e8>作者：</font>** Gong Sitong, Tianyu Yan, Caixin Kang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When should an intelligent assistant speak up without being asked? Continuous egocentric video offers rich, evolving context that enables a new form of assistance: one that is proactive rather than merely reactive. Yet existing approaches either wait passively for user queries or treat every detected event as requiring a response, without considering the user's history, current activity, or whether assistance would actually be welcome. We reframe proactive assistance as a context-dependent decision problem: the agent must not only perceive what is happening, but reason over accumulated temporal context to determine when and whether to intervene. To this end, we present Vinci2, a proactive egocentric assistance system that advances the on-device assistant Vinci from reactive response toward proactivity. On the evaluation side, we present EgoServe, the first large-scale benchmark for proactive assistance in continuous egocentric video. EgoServe comprises over 3,000 service instances organized along 4 temporal memory horizons, ranging from immediate safety alerts to long-term habit coaching, across 10 service categories. On the modeling side, we propose EgoMemo, a training-free, memory-augmented agent that maintains three complementary memory representations: multi-scale temporal summaries, a semantic knowledge graph, and visual embedding archives. At each timestep, EgoMemo performs retrieval-augmented reasoning to determine whether assistance is warranted and, if so, produces contextually grounded responses. Experiments demonstrate that EgoMemo establishes strong baselines on EgoServe while remaining competitive on existing egocentric benchmarks. Our benchmark and code are publicly available at \href{this https URL}{Vinci2}.

---


### 362. [AutoMatBench: An Automatic Optimization Toolkit for the Acceleration of Material Properties Prediction Benchmarking](https://arxiv.org/abs/2607.11526)

**<font color=#1a73e8>作者：</font>** Hongxiao Li, Wanling Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Material property prediction (MPP) infers key properties from chemical composition and structure, accelerating the discovery and optimization of novel materials. In the realm of MPP, MatBench is a widely accepted benchmarking tool that defines over ten significant problems and provides the paradigm of performance evaluation for AI prediction models. Even though MatBench works well in benchmarking the performances of prediction models on in-distribution (ID) tasks and datasets, it lacks the ability to reflect their performances on out-of-distribution (OOD) material data, resulting failure in new material discovery. By combining the pipelines of MatBench and the existing researches on OOD performance evaluation, this study enables a huge space of benchmarking configurations, comprehensively reflecting the performances, abilities, and disadvantages of various AI prediction models. This work reports that the discrepancy of performances at different configuration values is huge and can be illustrated with prior knowledge and novel insights, therefore consideration of causal effect of configurations on performance results is necessary. In case of the impossibility of enumerative benchmarking at every configuration, this work further proposes AutoMatBench, an automatic toolkit with Bayesian optimization. Experiments with AutoMatBench reports that, within twelve steps of optimization, the similar results with MatBench and former OOD research can be accessed while more than half of the cost are saved. Besides, this tool also yields more essential findings on MPP benchmarking, positively contributing to the cost and efficiency of new material discovery.

---


### 363. [Parse, Search, and Confirmation: Training-Free Aerial Vision-and-Dialog Navigation with Chain-of-Thought Reasoning and Structured Spatial Memory](https://arxiv.org/abs/2607.11529)

**<font color=#1a73e8>作者：</font>** Yu Qi, Hongyu Li, Shaofei Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we tackle the Aerial Vision-and-Dialog Navigation (AVDN) task in the training-free setting for resource-efficient high-altitude UAV this http URL applying MLLMs leads to unreliable navigation due to weak directional grounding and the lack of explicit spatial this http URL address these issues, we propose PSC-AVDN, a training-free framework that tightly couples a three-stage Parsing-Search-Confirmation reasoning pipeline with a Structured Spatial Memory (SSM).The parsing stage uses an LLM to convert ambiguous dialogue instructions into stable geometric directional and destination cues.A Search Chain-of-Thought (S-CoT) then performs stepwise target exploration under high-altitude observations, and a Confirmation Chain-of-Thought (C-CoT) conducts fine-grained verification around candidate regions to resolve visual this http URL, SSM integrates three complementary sources of spatial cues, including multi-scale visual observation, spatial visual memory, and structured geometric memory to provide global spatial context and long-horizon this http URL experiments on ANDH and ANDH-Full show that PSC-AVDN establishes new state-of-the-art performance in the training-free setting, matching or surpassing several finetuned this http URL will be publicly available at: this https URL

---


### 364. [Learning Residual Kinematic Corrections for Continuous Neural Decoding via Reinforcement Learning](https://arxiv.org/abs/2607.11530)

**<font color=#1a73e8>作者：</font>** Jiamian Li, Niall McShane, Attila Korik 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decoding continuous three-dimensional (3D) motor imagery (MI) using non-invasive electroencephalography (EEG)-based brain--computer interfaces (BCIs) remains challenging due to signal variability and residual decoding errors. Deep learning architectures such as convolutional neural network--long short-term memory (CNN--LSTM) models can capture spatial and temporal dynamics for continuous kinematic decoding; however, systematic residual errors persist in predicted trajectories. We propose a two-stage decoding framework that applies reinforcement learning (RL) to perform residual kinematic correction on the outputs of a CNN--LSTM decoder (CNN--LSTM--RL). The RL agent is trained offline without direct EEG input and instead operates on predicted kinematic trajectories to optimize movement accuracy relative to target trajectories. Decoding performance was quantified using Pearson correlation coefficients ($r$) and Root Mean Square Errors (RMSE) along the $x, y$, and $z$ axes. Compared to CNN--LSTM applied alone, CNN--LSTM--RL improved the mean correlation from $0.5076$ to $0.7181$ ($p = 0.0005$) in 2D and from $0.6420$ to $0.7780$ ($p = 0.0059$) in VR, with relative gains of $41.5\%$ and $21.2\%$, respectively. Correspondingly, RMSE was reduced from $0.0890$ to $0.0532$ (2D, $p < 0.0001$) and from $0.0714$ to $0.0441$ (VR, $p < 0.0001$), representing relative reductions of $40.2\%$ and $38.2\%$. These findings demonstrate that this scalable framework enhances 3D BCI MI decoding by correcting kinematic errors via offline residual RL without extra neural data, advancing neurorehabilitation, prosthetics, and virtual interaction.

---


### 365. [Adaptive Routing for Efficient Diffusion Transformer-Based PNI Prediction](https://arxiv.org/abs/2607.11533)

**<font color=#1a73e8>作者：</font>** Youngung Han, Dohyun Kweon, Kyeonghun Kim 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perineural invasion (PNI) is a critical prognostic factor in cholangiocarcinoma. However, its preoperative prediction from magnetic resonance imaging (MRI) remains challenging due to subtle imaging features that extend beyond tumor boundaries into surrounding regions. Conventional convolutional neural networks are limited in capturing long-range spatial dependencies. Transformer-based architectures improve global modeling of volumetric MRI by aggregating spatially distributed contextual cues, yet capturing subtle and noise-sensitive patterns in peritumoral regions remains challenging. Diffusion-based classifiers offer an alternative formulation by leveraging denoising-based class scoring to better capture such subtle patterns. However, these approaches introduce substantial computational overhead due to the combination of transformer-based modeling and iterative denoising processes. To address these challenges, we formulate PNI prediction as a diffusion-based classification problem and implement the denoising network using a transformer-based representation. To improve computational efficiency, we introduce adaptive routing across attention heads, spatial tokens, and MLP width. Experimental results demonstrate that the proposed approach achieves an AUC of 0.731 with 257.57 GFLOPs.

---


### 366. [Random Label Prediction Heads for Studying Memorization in Deep Neural Networks](https://arxiv.org/abs/2607.11541)

**<font color=#1a73e8>作者：</font>** Marlon Becker, Jonas Konrad, Luis Garcia Rodriguez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a straightforward yet effective method to empirically study memorization in deep neural networks for classification tasks. Our approach augments each training sample with auxiliary random labels, which are then predicted by a random label prediction head (RLP-head). RLP-heads can be attached at arbitrary depths of a network, predicting random labels from the corresponding intermediate representation and thereby enabling analysis of how memorization capacity evolves across layers. By interpreting the RLP-head performance as an empirical estimate of Rademacher complexity, we obtain a direct measure of both sample-level memorization and model capacity. We leverage this random label accuracy metric to analyze generalization and overfitting in different models and datasets. Building on this approach, we further propose a novel regularization technique based on the output of the RLP-head, which demonstrably reduces memorization. Interestingly, our experiments reveal that reducing memorization can either improve or impair generalization, depending on the dataset and training setup. These findings challenge the traditional assumption that overfitting is equivalent to memorization and suggest new hypotheses to reconcile these seemingly contradictory results. The source code is available at this https URL

---


### 367. [Condition-Stratified Robustness Analysis of Post-Hoc Calibration Methods for Probabilistic Classifiers](https://arxiv.org/abs/2607.11542)

**<font color=#1a73e8>作者：</font>** Gurdeep Singh Virdee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc calibration is widely adopted to correct probability estimates from trained classifiers, yet most evaluations report aggregate performance without testing whether that performance holds across distinct operating conditions within a single dataset. We present a pre-registered, condition-stratified robustness analysis comparing temperature scaling (TEMP) and isotonic regression (ISO) across four controlled conditions (C1--C4). Four hypothesis groups are evaluated: discrimination deltas with Holm-corrected multiplicity control (H1), Brier score differences (H2), calibration slope outcomes (H3), and AUROC differences under best-condition setups (H4). TEMP-minus-ISO discrimination deltas remain small across all conditions (-0.0155 to 0.0139), with Holm-adjusted p-values of 0.9895 everywhere. TEMP Brier differences are consistently negative (C1: -0.0002 through C4: -0.0074), while ISO shows sign reversals. TEMP calibration slopes stay closer to unity in every condition (range 0.7597--0.9493) than ISO slopes (0.1364--0.2726). AUROC differences shift from near zero in C1 (-0.0004) to positive in C4 (0.0264). These results establish that in-dataset robustness is condition-dependent and metric-specific. No claim of external transportability is made.

---


### 368. [Training-Free Off-Screen Player Imputation for Broadcast-Based Spatial Football Analytics](https://arxiv.org/abs/2607.11548)

**<font color=#1a73e8>作者：</font>** Seongjin Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial football metrics such as pitch control assume access to the positions of all 22 players, yet the most widely available source of positional data -- the broadcast main camera -- shows only 10-16 of them at any moment. We quantify the resulting distortion with an open, reproducible benchmark: a simulated broadcast viewport applied to open full-pitch tracking data (Metrica Sports; three matches, one held out from method development). Ignoring off-screen players -- the visible-only baseline implied whenever a video-based game-state-reconstruction (GSR) pipeline adds no imputation layer -- inflates hidden-zone pitch-control error to 25.1-26.9 percentage points and a mean absolute control-share error of 11.1-13.4 points across the three matches. We then evaluate a ladder of training-free, online imputation baselines that use only observations from the match being analysed. The best overall on these decision-relevant metrics, role-anchored centroid voting (each visible player votes for the full-team centroid by subtracting its running role offset, attenuating the viewport-induced subset bias), roughly halves hidden-zone error (to 12.2-13.8 points) and cuts control-share error to 28-48% of the ignore policy at every viewport width from 36 m to 60 m in all three matches. For occlusions <=9.6 s -- the regime of the closest learned prior work -- it reaches binwise median position errors of 3.3-8.9 m; but 50-57% of hidden-player observations lie beyond that regime. Integrated end-to-end into a broadcast-video GSR pipeline, imputation moves a downstream possession-quality score (Space-Creation Index) by 15.6 and 17.2 points on two real World Cup broadcast windows, flipping the verdict class in one.

---


### 369. [Advancing Optimal Subset Oracle via Learning Relaxation of Neural Set Functions](https://arxiv.org/abs/2607.11555)

**<font color=#1a73e8>作者：</font>** Yongquan Shi, Zijing Ou, Shiping Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning neural set functions is pivotal to a wide range of important applications, including compound selection in AI-driven drug discovery and product recommendation. Recent work has introduced optimal subset oracles to implicitly learn set functions under practical weakly supervised settings, where model parameters are optimized through mean-field variational inference. However, these frameworks rely on Monte Carlo sampling to estimate gradients of the evidence lower bound when updating the variational distribution. Repeated sampling across iterations incurs substantial computational overhead, while the resulting stochasticity can destabilize the optimization trajectory. In this work, we reinterpret the evidence lower bound as a continuous relaxation of the set function and learn a surrogate objective that replaces sampling-based ELBO gradient estimation during variational optimization. The learned surrogate provides stable and efficient gradients throughout the continuous domain, thereby reducing computational overhead and accelerating inference. Furthermore, we establish an approximation guarantee for the proposed framework under submodular maximization and characterize its connection to variational free energy. Experiments on a variety of real-world tasks demonstrate consistent improvements over existing baselines.

---


### 370. [Single-Teacher View Augmentation: Enhancing Knowledge Distillation with Student-Guided Perturbations](https://arxiv.org/abs/2607.11557)

**<font color=#1a73e8>作者：</font>** Xuyi Yu, Yaohua Liu, Ziming Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) typically relies on the fixed perspective of a single teacher, limiting the diversity of supervisory signals. While multi-teacher distillation addresses this by aggregating knowledge from multiple models, it incurs prohibitive computational and storage costs. To balance efficiency and diversity, recent research has focused on generating virtual views from a single teacher. However, existing methods face a trade-off: random perturbation approaches offer efficiency but lack controlled diversity, while structured augmentation methods require multi-stage training and incur linear parameter growth. We observe that this trade-off stems from a common design choice: using the teacher's strong but static features to generate views. Instead, we propose Shift-Augmented Knowledge Distillation (SAKD), a simple yet effective framework that leverages the student's evolving features as a dynamic condition for perturbation generation. This shift in perspective enables single-stage training while producing adaptive, diverse views through a parameter-free cyclic shift. Extensive experiments on CIFAR-100 and ImageNet demonstrate that SAKD consistently outperforms random perturbation methods and achieves accuracy on par with two-stage approaches, while using significantly fewer parameters and eliminating pre-training requirements.

---


### 371. [Technical Report on the CVPR 2026@AdvML Workshop Challenge](https://arxiv.org/abs/2607.11560)

**<font color=#1a73e8>作者：</font>** Tianyuan Zhang, Zonglei Jing, Jiangfan Liu 等 50 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language agents (VLAs) are increasingly used to interpret complex driving scenes and support safety-critical reasoning. This report presents the CVPR 2026@AdvML Workshop Challenge on adversarial multimodal attacks against autonomous-driving VLAs. Built on DriveLM-style multi-view visual question answering, the challenge represents each scene with six synchronized camera images and a structured collection of driving-related question-answer pairs. Participants generate adversarial images and suffix-only textual perturbations that induce model responses to deviate from reference answers while preserving image fidelity and limiting textual cost. The competition comprises two phases, with Phase II adding a hidden black-box model to assess transferability. We describe the task design, submission rules, evaluation protocol, and leaderboard results, and then examine five leading submissions for which technical reports were available. Across these reports, several recurring patterns emerge: image-side attacks are favored by the suffix penalty; scene-level, multi-view optimization is more effective than treating views in isolation; QA types and graph structure provide useful priors for allocating attack budget; feature-space objectives can improve black-box transfer; and typographic content embedded in camera images exposes a persistent vulnerability in driving VLAs. These findings provide a practical reference for future robustness evaluation and defense design in multimodal autonomous-driving systems.

---


### 372. [Linux disk encryption and self-encrypting drives -- A case study on Opal2 drives security](https://arxiv.org/abs/2607.11563)

**<font color=#1a73e8>作者：</font>** Milan Brož, Tamara Čierniková, Ondřej Kozina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Opal2 self-encrypting drives provide hardware-based disk encryption serving as an additional layer of protection, or a replacement, for software-based solutions. This paper presents a case study of real-world Linux integration of Opal2 drives and the security of Opal2 firmware. The study was conducted on a testbed of 38 commercial off-the-shelf Opal2 drives from various vendors using a black-box approach. We identified several firmware security issues and incompatibilities, which we responsibly disclosed to respective vendors. Our findings led to improvements in Linux disk encryption tools used across all major Linux distributions. To enable independent evaluation for the public, we release our test scenarios for Opal2 drives as an open-source toolset.

---


### 373. [Heuristic Learning for Active Flow Control Using Coding Agents](https://arxiv.org/abs/2607.11565)

**<font color=#1a73e8>作者：</font>** Paul Garnier, Jonathan Viquerat, Elie Hachem  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active flow control involves nonlinear dynamics, partial observations, and computationally expensive simulations, making controller design particularly challenging. Deep reinforcement learning (DRL) has emerged as a powerful framework for such problems, but its success typically relies on large numbers of simulator interactions and produces neural-network policies whose decision process often remains difficult to interpret. In this work, we investigate a different paradigm: instead of optimizing neural-network parameters, we use modern coding agents to search directly for explicit executable feedback laws. We introduce a constrained heuristic-learning protocol in which an agent iteratively proposes, evaluates, and revises controller implementations while interacting exclusively through the public benchmark interface. The proposed framework is evaluated on 13 active flow-control benchmarks spanning one, two, and three-dimensional problems and compared against the strongest available DRL baselines under identical simulation budgets. The discovered heuristic controllers match or outperform the best DRL policy in 10 of the 13 environments while remaining compact, interpretable, and directly inspectable. Beyond aggregate performance, the resulting controllers reveal physically meaningful feedback mechanisms, transfer successfully across more challenging configurations, and remain competitive under varying Reynolds and Rayleigh numbers, actuator counts, and observation sparsity. These results suggest that heuristic learning through coding agents constitutes a credible and complementary alternative to conventional reinforcement learning, combining competitive performance with physically interpretable controller representations. Prompts and source code are available at this https URL.

---


### 374. [Structure-Feature Aligned Graph Learning via Alternating Constrained Optimization](https://arxiv.org/abs/2607.11577)

**<font color=#1a73e8>作者：</font>** Chengcheng Yan, Qingsong Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a constrained two-view framework for node prediction that aligns structure-conditioned GNN embeddings with a structure-free feature prior learned by an anchor model. Conventional Graph Neural Networks (GNNs) couple feature transformation and neighborhood aggregation, which renders them vulnerable to topology noise and heterophilous connections. To decouple this dependency, our framework utilizes an independent anchor network to capture intrinsic attribute features via a self-supervised reconstruction objective. Furthermore, we propose a Channel-Split Adaptive Gated GNN (CSAG-GNN) that dynamically routes representations between global spectral smoothing and local spatial discrimination through a node-wise gating mechanism. We propose a stable cyclic alternating optimization strategy to solve the resulting coupled bi-level objective, preventing mutual representation drift during training. Empirical results on both homophilous and heterophilous benchmarks show balanced performance gains and structural robustness over competitive baselines.

---


### 375. [DiffEEG: A Self-Supervised Denoising Diffusion Model for Learning EEG Generic Representations](https://arxiv.org/abs/2607.11578)

**<font color=#1a73e8>作者：</font>** Abdulkader Helwan, Lina Abou-Abbas, Hussein El Amouri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning for EEG-based seizure detection faces critical challenges: severe annotation scarcity and extreme class imbalance, where ictal events comprise less than 10\% of clinical recordings. We present DiffEEG, a 9.6M-parameter self-supervised foundation model that addresses both limitations through denoising diffusion pre-training and reinforcement learning (RL)-based fine-tuning. Pre-trained on 1.3M unlabeled segments from the Temple University Hospital Seizure Corpus (TUHSZ), DiffEEG learns generic neural representations via a 1D U-Net with multi-head self-attention. For downstream adaptation, a reinforced decision layer employs policy gradient optimization to directly maximize F1-score, prioritizing sensitivity to rare seizure events over overall accuracy. Under strict patient-wise evaluation (279 patients, Leave-One-Fold-Out), DiffEEG achieves 61\% accuracy and 59\% F1 for 4-class seizure subtyping, and 81\% accuracy with 85\% weighted F1 for binary detection, maintaining clinically viable seizure recall (59\%) despite extreme imbalance (6.7\% prevalence). Segment-level evaluation establishes an upper bound of 97.6\% accuracy, confirming strong architectural capacity. DiffEEG demonstrates that diffusion-based pre-training combined with metric-aware reinforcement learning enables clinically deployable seizure monitoring with minimal labeled data requirements.

---


### 376. [GB-SVFBP: Gaussian-Based Shift-Variant FBP neural network](https://arxiv.org/abs/2607.11584)

**<font color=#1a73e8>作者：</font>** Chengze Ye, Linda-Sophie Schneider, Yipeng Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a Gaussian-Based Shift-Variant filtered backprojection (FBP) neural network, which is designed for the efficient reconstruction of non-circular trajectory cone beam computed tomography. The traditional differentiable shift-variant FBP model consists of a filtering component and a backprojection process. The filtering component includes operations such as weightings, differentiations, a 2D Radon transform, and a 2D backprojection. The proposed methods build on this framework by introducing a trainable 2D Gaussian model to represent the trajectory-related part in the filtering process, achieving a substantial reduction in the number of trainable parameters. Experimental results demonstrate that the proposed model reduces the parameter count by 99%, while only sacrificing a slight amount of reconstruction quality. Furthermore, the training time for each trajectory is reduced to one-fourth of the original, significantly accelerating convergence. These enhancements demonstrate a considerable augmentation in the model's practicality and effectiveness, making it a valuable asset for real-world applications.

---


### 377. [FoundationGeo: Learning Spatial Pixel-Wise Fields for Monocular Metric Geometry](https://arxiv.org/abs/2607.11588)

**<font color=#1a73e8>作者：</font>** Muxin Liu, Xiaoyang Lyu, Tianhe Ren 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FoundationGeo, a two-stage framework that explicitly bridges relative and metric prediction via spatial calibration and principled data design. Stage 1 learns a high-fidelity, affine-invariant geometry model by initializing with DINOv3 and training on a curated 10.2M-sample multi-domain corpus with complementary local-detail supervision, yielding sharp boundaries and strong cross-domain generalization. Stage 2 moves beyond global scaling by introducing lightweight pixel-wise calibration fields for metric estimation: a scale field for spatially varying metric alignment and a ray-direction correction field that mitigates directional bias in point-map geometry, together producing metrically consistent 3D point maps. Beyond model design, we identify camera intrinsic coverage, especially focal length distribution mismatch between training and test data, as a key bottleneck for zero-shot metric generalization: performance drops sharply when test intrinsics fall outside the training distribution. To address this, we synthesize additional training data across diverse focal lengths using a Blender-based data engine, repairing under-covered focal regimes and improving robustness under intrinsic shift. Extensive zero-shot evaluations across seven benchmarks show that FoundationGeo significantly strengthens cross-domain robustness, staying near the top across diverse domains while avoiding the sharp cross-domain performance drops observed in other methods. This consistency translates into the best overall performance, surpassing heavier baselines by over 5.2% on average.

---


### 378. [Beyond Benchmarks: Exposing the Hidden Crisis in Bangla Hate Speech Detection](https://arxiv.org/abs/2607.11597)

**<font color=#1a73e8>作者：</font>** Faria Afrin Tisha, Fariya Tabassum, Hafsa Binte Kibria 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The spread of hate speech (HS) across different social media platforms (SMPs) poses a major concern for online safety and ethical moderation. Automatic detection of HS remains a challenging task, especially in under-resourced languages like Bangla, due to cultural context, implicit expressions, and informal linguistic patterns. This study aimed to expose the crisis of Bangla HS detection systems by diagnosing how and why benchmark-trained models fail to identify implicit, context-dependent HS. Six architectures (FastText + CNN, FastText + LSTM, FastText + BiLSTM, BanglaBERT, BanglaBERT + CNN, and BanglaBERT + BiLSTM) were trained on benchmark datasets (about 75,000 posts) and a merged multi-source dataset (about 120,000 posts), then externally validated on an annotated dataset (about 200 posts) collected from Facebook, Twitter, and YouTube, labeled as HS and non-HS, where HS was further categorized as explicit and implicit. BanglaBERT achieved an F1-score of 91.4% on benchmark datasets but declined to 75.3% on the external set and 63.4% for implicit HS involving sarcasm and emojis. The accuracy of FastText + CNN dropped from 78.0% to 51.2% under similar conditions. Emoji-aware preprocessing improved implicit HS detection by up to 12%, whereas emoji removal caused a notable decline in performance (F1: 0.75 to 0.63). Frequent misclassifications in politically charged or satirical comments revealed over-policing risks. This study not only exposes the generalization crisis due to implicit, culturally embedded, and emoji-laden expressions but also underscores the need for developing adaptive, emoji-aware, and culturally grounded frameworks that ensure ethical moderation while preserving freedom of expression. Findings of this study provide insights for researchers, SMPs, and policymakers to design more context-sensitive HS detection systems for low-resource languages.

---


### 379. [Interaction Scaling: Grounding the Third Axis of Test-Time Compute](https://arxiv.org/abs/2607.11598)

**<font color=#1a73e8>作者：</font>** Bojie Li, Noah Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There are two standard ways to spend more compute at test time: let a model reason longer, or sample more attempts and keep one. Both share a hidden limit: they are internal. Every extra token comes from the same frozen weights and the same prompt, so neither can tell the model anything it does not already know. We study a third way, interaction: the model proposes an artifact, an external instrument observes how it actually behaves, and the model revises. Each cycle imports a real observation, so interaction breaks through the ceiling the other two hit.
We argue that a single variable governs this third axis, grounding, and that it must hold on both sides of the loop. The feedback that drives revision must come from an instrument that actually observes the flaw, and so must the metric that scores the result. On hard coding tasks at a fixed token budget, reasoning-only and best-of-N sampling both plateau (the latter even when an oracle picks the best sample), while every interaction strategy keeps improving; our proposer-reviewer harness reaches a perfect 100% pass rate with no run-to-run variance, and the gain holds across three model families. On rendered visual artifacts, the usual judge (a vision-language model, or VLM, reading a screenshot) rates 14 of 15 visibly broken figures "perfect," because the screenshot hides the flaws before the judge can see them. A tool that measures the real layout instead shows the loop removing 40-74% of defects across four modalities; and that same VLM, used as the reviewer, makes slide layouts worse where the measuring tool repairs them. Interaction scaling is real and distinct from reasoning and sampling, but only visible when both the feedback and the metric are grounded.

---


### 380. [Privacy-Aware Collaborative and Distributed Bayesian Optimization](https://arxiv.org/abs/2607.11600)

**<font color=#1a73e8>作者：</font>** Aditya Rane, Sathwik Yamana, Paritosh Ramanan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a collaborative meta-learning framework for distributed Bayesian optimization matching centralized performance without raw-data exchange. We show gradient sharing leaks client observations, with leakage worsening as the search converges and queries concentrate near the optimum. We evaluate a differentially private defense and characterize its privacy-utility trade-off.

---


### 381. [Cardano's Voltaire Governance: Complete Specification and Research Program](https://arxiv.org/abs/2607.11601)

**<font color=#1a73e8>作者：</font>** Nimrod Talmon, Oghenekaro Elem  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchain governance, the set of processes by which decentralized protocols evolve, remains a fundamental challenge in balancing adaptability, security, and stakeholder representation. This technical report analyzes Cardano's Voltaire governance system, the on-chain framework introduced via CIP-1694 and enacted through the Chang hard fork in September 2024, and lays down a corresponding research program.
We make two contributions. First, we provide a complete technical specification of Voltaire's mechanisms, including its three-body architecture, seven governance action types, voting rules, and its constitutional framework; this specification is sufficient for implementation or formal analysis. Second, we establish a research agenda for principled governance optimization, including design of an agent-based simulation platform, analysis of delegation dynamics, optimization of multi-objective parameters, and game-theoretic incentive design; we provide preliminary results, including a formal governance kernel: a minimal executable model capturing self-amending governance as a state-transition system and enabling rigorous safety and liveness analysis.
Our report offers a comprehensive technical overview and invites the research community to advance blockchain governance science through rigorous study of Voltaire as a live, large-scale experiment now managing a treasury valued at approximately \$235 million (1.47B ADA as of early July 2026).

---


### 382. [Globally Consistent Coloring Schemes for Language Identification](https://arxiv.org/abs/2607.11606)

**<font color=#1a73e8>作者：</font>** Moses Charikar, Jon Kleinberg, Chirag Pabbaraju  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study how little extra information is needed to make adversarial language learning possible. In Gold's model of language identification in the limit, a learner is given an enumeration of the strings from an unknown language chosen from a countable language collection. The learner guesses the identity of the language over the course of the enumeration, and it succeeds if, eventually, all of its guesses are the correct language. Classical results of Gold and Angluin show that many natural collections cannot be learned in this way. Recent work on trace colorings, motivated by the success of thinking-trace strategies in language learning, overcomes this obstruction by annotating every symbol of every string with a color. We ask whether the learner really needs this whole sequence of colors, or whether one color at the end of each string (a terminal coloring) is enough for language identification.
We show that just one terminal bit per string is enough for every countable collection of infinite languages. In fact, the colorings can be chosen collection-independently: there is a single assignment of a two-color terminal coloring to every infinite language such that the same preassigned colorings identify every countable subcollection. Thus, in this model, an entire color trace can be compressed to one bit attached to the end of each example.
Our global construction uses transfinite recursion, and we prove that this kind of nonconstructivity is unavoidable for any bounded number of colors. As a notion of constructivity, we use the formalism of Borel maps (a regularity condition satisfied by natural explicit constructions); we show that no global terminal coloring with a finite number of colors defined by a Borel map can identify all countable subcollections. By contrast, known trace-coloring constructions are Borel when encoded as terminal colorings, but require infinitely many colors.

---


### 383. [Auditing the Risk Claims of Distributional Reinforcement Learning](https://arxiv.org/abs/2607.11607)

**<font color=#1a73e8>作者：</font>** Hari Prasad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distributional reinforcement learning agents learn full return distributions that are increasingly read at face value: for interpretability, risk-sensitive control, and safety monitoring. We ask a question theory anticipates but that has not been measured directly: are the risk claims of a trained distributional agent true? Our audit combines a decision-relevant screening metric (the excess Wasserstein gap between the top two actions, which equals the mass by which first-order stochastic dominance is violated), ground truth from snapshot-restart Monte Carlo, and a statistical harness (permutation nulls, bootstrap refutation, FDR control) without which the audit itself manufactures false conclusions. Across QR-DQN, C51, and IQN on MinAtar (33 runs), 40-95% of the strongest claimed risk trade-offs are refuted at 95% confidence, the placement of the strongest claims is statistically indistinguishable from truth-blind, and essentially no claim is confirmable: for these agents, the learned "risk" reflects a training artifact rather than environment stochasticity. The artifact is structural (fully formed early in training, uncorrelated with final score, idiosyncratic to each seed) and appears unchanged at full-Atari scale, with every top Breakout claim of a pretrained near-state-of-the-art QR-DQN refuted. Positive controls of known magnitude confirm 96-100% of real claims (correlation 0.89-0.92): the reading measures the agents, not the audit. Acting on the heads' CVaR advice at their most-flagged states ranges from beneficial to significantly worse than chance. Neither training for risk nor ensembling removes the artifact, and recalibration passes the audit only by nullifying the claims: the head is uninformative, not merely miscalibrated. We release the toolkit and document two silent pitfalls that produced convincing but wrong audits of our own.

---


### 384. [Backbone-Agnostic Perturbation-Induced Uncertainty Learning for End-to-End Real-World Image Dehazing](https://arxiv.org/abs/2607.11623)

**<font color=#1a73e8>作者：</font>** Bingcai Wei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world paired image dehazing remains challenging because haze degradation is spatially non-uniform, illumination-dependent, and physically ambiguous even when haze-free references are available. Existing end-to-end restoration networks usually formulate dehazing as a deterministic mapping from a hazy observation to a clean target, leaving the uncertainty hidden in degraded features, haze priors, and cross-domain negative samples insufficiently explored. In this paper, we propose Backbone-Agnostic Perturbation-Induced Uncertainty Learning (BPUL), a plug-and-play uncertainty learning framework for end-to-end real-world image dehazing. BPUL first introduces a Learnable Perturbation-induced Uncertainty Modulator (LPUM) that estimates channel-wise and spatial-wise feature sensitivity through reparameterized stochastic perturbations. It then develops a Prior-informed Uncertainty-guided Reconstruction Module (PURM), which exploits transmission and atmospheric-light priors to reconstruct the hazy observation from the restored result and enforce degradation consistency. Furthermore, we propose a Dual-space Domain-diversified Distribution-aware Contrastive Loss ($D^3$CL) to regularize both clean restoration and hazy reconstruction spaces with real-world and synthetic negatives. Experiments on five real-world paired benchmarks show that BPUL consistently improves multiple representative backbones. Since only LPUM is retained during inference while PURM and $D^3$CL are used as training-time constraints, BPUL brings substantial restoration gains with only marginal additional inference overhead.

---


### 385. [Fundamental Limitations of Fixed-Budget Best-Arm Identification](https://arxiv.org/abs/2607.11635)

**<font color=#1a73e8>作者：</font>** Motti Goldberger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In fixed-budget best-arm identification, also known as ranking and selection, an algorithm has a sampling budget to distribute across $K$ arms. Each sample provides noisy feedback about that arm's mean, and the goal is to identify the arm with the largest mean. A common performance benchmark is the static oracle: a non-adaptive strategy that knows the means in advance and chooses fixed sampling proportions to maximize the exponential decay rate of the probability of incorrect identification. Several adaptive algorithms have been constructed such that their sampling proportions converge to the static oracle proportions. However, it has remained open whether any algorithm could match the static oracle's error decay rate uniformly across all problem instances. We answer this in the negative. For any $K\ge 3$ and for rewards drawn from any one-parameter natural exponential family, we show that for any algorithm, there is at least one instance where the error decay rate is at most $\left(1 + \frac{\log(K)}{8}\right)^{-1}$ times that of the static oracle. This also answers the open question posed by Qin (2022), showing that fixed-budget best-arm identification does not admit a complexity.

---


### 386. [Motion4Motion: Motion Transfer Across Subjects at Inference](https://arxiv.org/abs/2607.11644)

**<font color=#1a73e8>作者：</font>** Ling-Hao Chen, Zixin Yin, Duomin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work explores the motion transfer from one video to another, which is crucial in animation for diverse characters. Previously, video motion transfer has been largely explored between human and human-like characters, enabling a lot of applications in digital creation. However, these approaches encounter a main limitation. Specifically, related technical pipelines heavily rely on a predefined human skeleton structure and accordingly require skeleton-conditional model training. On the one hand, these methods are difficult to generalize to diverse characters, such as animals from different species, while preserving their unique motion styles. On the other hand, labeled data in diverse skeletons is limited, which additionally restricts the large-scale training for the task. In this paper, we jump out of the skeleton-based motion transfer framework and propose a training-free motion transfer framework, named Motion4Motion. Motion4Motionmodels the motion flow of the character in a video instead of skeletons, which makes motion transfer across species easier. Extensive experimental results and novel applications show our methods outperform baselines impressively. Project page is available at this https URL.

---


### 387. [Event-RGB Adaptive Tracking for Nighttime Highway Perception](https://arxiv.org/abs/2607.11646)

**<font color=#1a73e8>作者：</font>** Haidong Wang, Hengxing Cai, Wanlei Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intelligent Transportation Systems deployed on highways predominantly rely on conventional RGB cameras for traffic perception and vehicle tracking. However, highway environments present unique challenges: the absence of artificial lighting infrastructure, combined with high vehicle velocities, results in severely degraded perception performance under low-light conditions. Specifically, nighttime scenarios suffer from motion blur, insufficient exposure, and poor signal-to-noise ratios, which catastrophically impair the reliability of RGB-based sensing systems. To address these limitations, we propose a novel Joint Event-RGB Adaptive Tracking (JEAT) framework. Unlike existing multi-sensor trackers constrained by rigid, hard-coded prioritization, JEAT merges asynchronous event streams and RGB frames into a unified joint data association optimization. By employing an Adaptive Extended Kalman Filter to continuously estimate measurement noise via NIS statistics, the framework dynamically weights and fuses both modalities, optimally harnessing event streams during dark or high-speed motion while leveraging RGB frames under bright or static conditions. Furthermore, given the absence of publicly available datasets tailored for event-based highway perception with diverse environmental conditions, we present SEHN, a large-scale synthetic dataset generated using the CARLA simulator. Our dataset encompasses diverse environmental conditions (daytime, nighttime, nighttime with out artificial lighting) and varying traffic densities, providing synchronized RGB imagery and event streams to facilitate multi-modal fusion research. Our code and datasets will be available at this https URL.

---


### 388. [Closing the Loop: An Access-Control Architecture for Automated, Anomaly-Driven Network Revocation in IoT Deployments](https://arxiv.org/abs/2607.11649)

**<font color=#1a73e8>作者：</font>** Muhammet Emir Korkmaz, Kemal Bicakci, Yusuf Uzunay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network-based anomaly detection for IoT devices has matured to the point of reporting strong detection accuracy, yet most published systems stop at raising an alert and leave the question of automated enforcement to future work or to a programmable data plane that few real networks operate. This paper presents an access-control architecture that closes that loop using only standard, already-deployed protocols. Devices authenticate via IEEE 802.1X with EAP-TLS, and a RADIUS server acts as a continuous policy decision point capable of evicting an active session via a Change-of-Authorization Disconnect-Request and permanently excluding a device through certificate revocation. A central, contextual access policy engine continuously consumes the anomaly detector's output and actuates this response over a narrowly restricted channel to the RADIUS server; the same engine is designed to be extensible to other access types, though this paper evaluates only the network access-control mechanism. This mechanism is driven by an anomaly signal from a one-class detector adapted from a prior MUD/SDN-based design, replacing its per-flow multi-model pipeline with passive traffic capture and a single fused model that combines a cluster-based, a volumetric, and a protocol-signature score. On a single testbed device, the detector reaches an AUC of 0.9964 and detects all 24 evaluated attack scenarios (eight attack types at three intensities) using roughly 43$\times$ less training data than the reference design, and the resulting alerts reliably trigger the automated disconnect-then-revoke response, which we measure to evict a device from the network in 335.8\,ms on average and complete certificate revocation in a further 111.5\,ms. We report this evaluation as a demonstration of the closed-loop architecture rather than of the detector itself, and discuss multi-device generalization as a concrete next step.

---


### 389. [Bet on Features: Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters](https://arxiv.org/abs/2607.11653)

**<font color=#1a73e8>作者：</font>** Ivane Antonov, Sohom Mukherjee, Richard Pibernik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Black-box conditional quantile forecasts are widely used for sequential decisions under asymmetric costs, such as inventory planning in supply chain management. Once deployed, such forecasters must be monitored continuously as data streams drift and regimes change; this invalidates standard, fixed-horizon backtests for calibration. Further, existing backtests do not take into account that the notion of calibration is, in fact, information-dependent: forecasts can look calibrated to an auditor with coarse information while being miscalibrated to an auditor with richer information. We develop a distribution-free and game-theoretic testing framework for continuously auditing black-box conditional quantile forecasters with non-i.i.d. losses, such that the resulting evidence process is powerful against predictably chosen alternatives specified by the features available to the auditor. We first formalize notions of conditional quantile calibration when different sets of features are available to the auditor, establishing that the coarseness of the auditor's information set determines the hardness of the testing problem. We then identify the sets of alternatives for which the auditor can achieve power, and focusing on contextual bets linear in the features, we derive finite-time detection guarantees for such alternatives, all without an i.i.d. assumption. The resulting evidence processes are interpretable at the feature level, as they quantify fine-grained, "feature-aware" evidence for miscalibration. We empirically validate these methods on simulated and real data, finding that a popular time series forecaster (Chronos-2) is highly miscalibrated w.r.t. multiple relevant features.

---


### 390. [Feature-Space Guided Diffusion for Realistic Ultrasound Image Synthesis](https://arxiv.org/abs/2607.11655)

**<font color=#1a73e8>作者：</font>** Marina Domínguez, Nélida Mirabet-Herranz, Valery Naranjo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conditional diffusion models can generate anatomically plausible medical ultrasound (US) images, but anatomical plausibility alone does not ensure realistic B-mode appearance. Most US pipelines adapt standard generative architectures and condition them on anatomical masks, or use guidance mechanisms that reinforce the same anatomical signal. However, B-mode US images are shaped by acquisition-dependent properties such as speckle texture, tissue contrast, and attenuation. Using a frozen US foundation model, we show that standard conditional diffusion baselines remain separated from real images in representation space. In this work, we propose Feature-Space Candidate Guidance (FSCG), a training-free sampling strategy to reduce this gap. At sampling time, FSCG applies local k-NN feature correction and selects the best of multiple stochastic candidates according to their feature-space energy. In this way, the mask defines the anatomy, while FSCG steers samples toward the real US domain. Across three different datasets, FSCG reduces average FID64 by 56\%, FID192 by 57\%, and nearest-neighbour feature distance by 47\% over standard conditional diffusion sampling, outperforming alternative inference-time guidance baselines. The results suggest that domain-aware feature representations can reveal and reduce realism gaps in medical diffusion synthesis without retraining the generator. Our code is available at this https URL.

---


### 391. [How to Tame Grokking: Representation Geometry as a Control Signal](https://arxiv.org/abs/2607.11666)

**<font color=#1a73e8>作者：</font>** Maksim A Kazanskii  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking is a phenomenon in which neural networks initially memorize training data and only later exhibit strong generalization after prolonged optimization. Despite extensive recent study, the factors influencing the emergence and timing of grokking remain incompletely understood. We investigate the relationship between representation geometry and delayed generalization. We find that dimensionality collapse consistently precedes the onset of grokking in all evaluated settings. Motivated by these observations, we introduce Geometric Dimensionality Regularization (GeomDR), a simple spectral regularizer that modifies the effective dimensionality of hidden representations during training. Across modular addition, modular division, and permutation composition tasks, GeomDR consistently alters grokking dynamics and can substantially accelerate the onset of generalization depending on the intervention schedule and target dimensionality. In several settings, grokking is accelerated by up to 52 times relative to standard AdamW training. Similar qualitative effects are observed in both multilayer perceptrons and transformers. Together, these results suggest that representation geometry can serve as an effective control signal for grokking and provide evidence that geometric interventions offer a practical approach for studying and influencing delayed generalization in neural networks.

---


### 392. [Losing My Composure: Predicting Compositionality Over Time](https://arxiv.org/abs/2607.11667)

**<font color=#1a73e8>作者：</font>** Chris Jenkins, Emma Raimundo Schulz, Filip Miletić 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We explore the phenomenon of semantic change of German and English noun compounds, with the objective of investigating and modeling gradual changes of meanings and degrees of compositionality in the past and over time. To do so, we introduce the Compositionality Trend Prediction task, which is evaluated against a novel dataset of in-context compositionality ratings sampled across several decades of diachronic corpora for 23 German and 26 English target compounds, uniquely providing per-decade ratings and corresponding trends over time. These per-decade compositionality ratings allow us to investigate empirically untested hypotheses of generalized trends in compositionality over time, such as the idea that compounds should become less compositional (less transparent) over time. Beyond our empirical observations from the diachronic compositionality annotations, we perform experiments with semantic vector representations of varying complexity, as well as several temporal granularities for training these representations on diachronic data, resulting in about 100 models of each representation type, each covering a different 1--5 decade slice of a diachronic corpus. Contrary to the decisive tendency posited in the literature, we find only a small negative trend in compositionality over time in our target compounds. In our computational experiments, we find that using models trained on narrow time slices of diachronic data (single decades, or incrementally expanding temporal windows) align better with the per-decade compositionality ratings than those trained on an entire half-century window, the latter setting being an analog for the prevalent modeling approach of training representations on an entire half of a corpus' data. Additionally, we find static representations to be competitive with contextual representations in the Compositionality Trend Prediction task.

---


### 393. [A multi-scale feature enhanced graph neural network for fluid dynamics prediction in complex geometries](https://arxiv.org/abs/2607.11672)

**<font color=#1a73e8>作者：</font>** Li Xiao, Tianyu Li, Yiye Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial design in fields such as vehicle and aerospace engineering often relies on large-scale numerical simulations to evaluate fluid dynamics performance, which can incur substantial computational costs. Deep neural networks have shown promise in improving simulation efficiency, especially graph neural networks (GNNs), which demonstrate great potential due to their flexibility with unstructured data. However, GNNs face challenges when dealing with tasks involving complex geometries and large-scale meshes. In this paper, we propose the Multi-scale Feature Enhanced Graph Neural Network (ME-GNN) to tackle these challenges. ME-GNN employs a graph neural network with a two-step message-passing mechanism to capture detailed local features effectively. Additionally, it integrates an Attention U-Net with uniform grid discretization, enabling the extraction of both fine and coarse features. The model also utilizes K-hop sampling to construct subgraphs, facilitating efficient training on large datasets while preserving detailed local features. We evaluated ME-GNN on three benchmark datasets and achieved state-of-the-art results: a relative L2 error of 0.0196 for the velocity field and 0.0556 for the surface pressure on ShapeNet-Car, a normalized mean squared error of 0.0033 for the flow field on AirfRANS, and a relative L2 error of 0.1416 for the surface pressure on DrivAerNet.

---


### 394. [Illuminant-Adaptive 3D Lookup Tables for Camera Color Correction](https://arxiv.org/abs/2607.11681)

**<font color=#1a73e8>作者：</font>** Claudio Rota, Luca Cogo, Simone Bianco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color correction is a key component of camera image signal processing (ISP) pipelines, encompassing illuminant discounting and colorimetric mapping of device-dependent sensor responses to device-independent color spaces, such as CIE XYZ. Despite extensive research, accurate color correction remains challenging due to the non-linear relationship between camera sensor responses and CIE XYZ color space, as well as to the increasing presence of highly chromatic and spectrally complex LED illuminants. We propose a color correction framework based on illuminant-adaptive three-dimensional lookup tables (LUTs), which we call Color Correction LUT (C$^2$LUT). Our method combines a chromaticity-aware illuminant representation with a non-linear color transformation, enabling accurate correction under illuminants spanning a wide range of chromaticities and spectral complexities. We employ Tucker tensor decomposition to represent the LUTs, ensuring that computational requirements remain sufficiently low for deployment in camera ISPs. In addition, we introduce a large-scale illuminants dataset comprising 1,473 spectral power distributions, with different chromaticities and spectral profiles. Experiments across multiple cameras, illuminants, reflectance datasets, and real captured images demonstrate consistent improvements over existing methods for color correction, reducing CIE $\Delta E_{00}$ by up to 20% and angular error by up to 18% while remaining compatible with modern camera hardware constraints. Code and datasets are available at this https URL.

---


### 395. [SVI360: Spherical Video Interpolation](https://arxiv.org/abs/2607.11710)

**<font color=#1a73e8>作者：</font>** Le-Kim Nguyen, Renato Martins, Pascal Vasseur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the problem of omnidirectional video interpolation, which plays an essential role in applications such as virtual reality and immersive video enhancement. Existing video interpolation methods are not well-suited for spherical videos, as they have difficulty handling severe distortions close to the poles. To address this issue, we propose SVI360, a dual-branch framework that combines the image frame and its rotated orthogonal view to deal with these distortions. The core methodological aspect of the approach is to reinforce equivariance of the flow displacements between the original and orthogonal views to improve intermediate frame prediction. Experiments show that our method outperforms state-of-the-art approaches in interpolation quality while maintaining accurate optical flow in four different public benchmarks. Code and pre-trained models are available at: this https URL

---


### 396. [CatRetriever: Contrastive Representation Learning for Slab-to-Bulk Retrieval in Generative Catalyst Discovery](https://arxiv.org/abs/2607.11712)

**<font color=#1a73e8>作者：</font>** Jungho Oh, Woosung Kim, Dong Hyeon Mok 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse design is an emerging data-driven paradigm for efficiently navigating vast chemical spaces to discover new materials with targeted properties, and in the context of heterogeneous catalysis, surface generative models have recently advanced this goal by directly generating catalyst surface-adsorbate structures. However, these models typically operate at the slab level and do not provide the corresponding parent bulk structure, making it difficult to assess bulk-dependent properties such as formation energy, surface energy, crystallographic symmetry, and synthesizability. Here, we address this missing slab-to-bulk connection as a retrieval problem and introduce CatRetriever, a contrastive representation learning model that aligns slab and bulk crystal representations in a shared latent space. From a slab query, CatRetriever accurately retrieves plausible parent bulk candidates with R@1 > 91% and R@3 > 98% on both the in-distribution and holdout evaluation sets. We further extend the CatRetriever framework into an adsorption energy targeted bulk discovery pipeline that combines bulk retrieval, generative search space expansion, and adsorption energy distribution analysis. This workflow evaluates candidates by both structural compatibility with the query slab and their ability to access the target adsorption energy range across diverse surface environments. CatRetriever therefore provides a scalable route for connecting catalyst generative models with physically plausible and adsorption energy compatible bulk catalyst discovery.

---


### 397. [Active Offline-to-Online Reinforcement Learning](https://arxiv.org/abs/2607.11720)

**<font color=#1a73e8>作者：</font>** Alper Kamil Bozkurt, Shangtong Zhang, Yuichi Motai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Offline reinforcement learning (RL) enables effective policies to be trained from large, previously collected datasets and subsequently improved through limited online interaction. This offline-to-online RL (O2O-RL) paradigm is particularly promising in nonstationary domains where interaction is costly or potentially hazardous. Standard O2O-RL pipelines train multiple candidate policies offline, evaluate them using off-policy or online evaluation, and then deploy and fine-tune the policy with the highest estimated value. However, as in offline pretraining, fine-tuning performance is highly sensitive to the choice of algorithm and hyperparameters, making it risky to commit to a single policy. Objectives: We study active policy selection for fine-tuning under a limited interaction budget in O2O-RL settings. To our knowledge, this is the first work to address this problem. Methods: We formulate the problem by identifying a fundamental trade-off between allocating online interactions to policy evaluation, which helps identify high-performing policies, and allocating them to fine-tuning, which improves policy performance. We then propose an approach that balances this trade-off by actively selecting policies for fine-tuning based on upper-confidence bounds on their future performance. These bounds are derived from locally linear performance forecasts fitted to observations obtained through online evaluation. Results: Across a diverse range of experiments, the proposed approach consistently outperforms existing O2O-RL baselines. Conclusions: Actively selecting and fine-tuning policies uses limited online interaction budgets more effectively than either committing to a single policy or dividing the budget equally among all policies. Our framework also advances offline RL toward practical deployment in real-world systems where online interaction is costly or risky.

---


### 398. [Time-Lag-Aware Deep Reinforcement Learning for Flexible Job-Shop Scheduling in PPVC Module Factories](https://arxiv.org/abs/2607.11725)

**<font color=#1a73e8>作者：</font>** Ziheng Zhang, Wei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prefabricated prefinished volumetric construction moves most building work into module factories, whose production floor operates as a flexible job shop. A major complication is decisive: long post-operation time-lags caused by concrete curing, watertightness ponding tests, and paint drying, during which a module is blocked while its workstation stays free. On benchmark instances grounded in an official national prefabrication guidebook, these lags inflate even the optimal reference makespan by about 67% on average, and ignoring them at decision time, then repairing to feasibility, is worse than every dispatching rule. We adapt a state-of-the-art dual-attention deep reinforcement learning solver through three minimally invasive, individually ablatable extensions: lag-aware dynamics with an admissible reward bound, two anticipatory lag feature channels, and liveness-masked operation- and station-type embeddings. With every extension disabled the implementation reproduces the original solver exactly, so all gains are attributable to the adaptations. We release a public, guidebook-grounded benchmark generator. On held-out instances the learned policy is the strongest solver-free scheduler: it reaches within about 4% of a constraint-programming reference and beats every dispatching rule and a genetic-algorithm metaheuristic, with its advantage widening under capacity contention, and a single size-mixed policy carries this lead across the trained range of factory sizes. It needs no solver, model, or license in the loop and re-plans within seconds of a disruption; where an exact solver can be deployed, that solver remains the quality ceiling, a boundary we map explicitly.

---


### 399. [MET: Theory-Grounded and Culture-Aware Multilingual Moral Reasoning](https://arxiv.org/abs/2607.11736)

**<font color=#1a73e8>作者：</font>** Ayoung Lee, Ryan Kwon, Yunxiang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly used for moral decision-making across diverse linguistic and cultural contexts, yet existing work overlooks multilinguality on three aspects: 1) multilingual evaluation benchmarks use direct translation, failing to adapt culture-specific items; 2) inference-time methods for moral reasoning rely on static, English-centric scaffolds and lack grounding in moral theory; 3) training methods for moral decision-making typically require expensive supervision from stronger models or human annotators. We address these gaps with three contributions. First, we introduce MCLASH, a multilingual moral decision-making benchmark to capture culturally situated moral intuitions and social norms across languages. Second, we propose MET (Multilingual Ethics with Theory-grounded reasoning), a two-step prompting method built on expert-curated, theory-based grounds drawn from psychology and philosophy: the model first selects situation- and culture-specific grounds, then reasons over them in the native language of the user. Third, we introduce MET-D (MET-Distillation), which enhances the second step through a self-distillation training stage that requires no external supervision. MET-D improves macro-F1 over the base model on all three models of different sizes and families (Qwen3-4B, Qwen3-8B, Gemma3-4B), by an average of 3.71 points on MCLASH and 4.23 on MMoralExceptQA, with a peak MCLASH gain of 12.94 points for Malay on Qwen3-8B. We further reveal that MET-D increases native-language reasoning by 62.13 points on average, and that beneficial grounds differ systematically across cultures. Together, these contributions open the path for culture-aligned, theory-grounded multilingual moral reasoning.

---


### 400. [Multi-Agent Reinforcement Learning for C-V2X RAT Selection](https://arxiv.org/abs/2607.11744)

**<font color=#1a73e8>作者：</font>** Moritz Schaffenroth, Uwe Kölbel, Heike Lepke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Vehicles are increasingly equipped with advanced V2X communication capabilities. While early V2X apps utilized services such as Cooperative Awareness Messages, recent developments have allowed more advanced applications including cooperative driving, shared perception, and sensor-sharing services. The broader mix of applications leads to heterogeneous requirements for latency and reliability. At the same time multiple communication technologies for V2X are available with pros and cons. Hybrid V2X communication can exploit the distinct advantages at the right moment to fulfill the requirements of the applications. This work studies the decision problem between cellular Uu link, NR-V2X PC5 sidelink, and the simultaneous use of both channels. We address this problem by using the multi-agent reinforcement learning algorithm MAPPO and compare it to five baselines consisting of a deep reinforcement learning (DRL) approach, a static decision tree approach and static channel selection strategies. The methods are evaluated in an urban scenario and with a set of selected communication use cases. The evaluation results show that when compared to the DRL approach, the on-time delivery ratio improves from 0.508 to 0.535 in a single-controlled-vehicle setting and from 0.548 to 0.567 when all vehicles follow the learned policy and reduces the training time by half. The gains result mainly from the advanced applications scenarios, as opposed to scenarios involving exclusively CAM messaging. This indicates future applications will benefit from such adaptive communication strategies and that multi-agent modelling is useful for addressing the underlying decision problem.

---


> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-420](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
