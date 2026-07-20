# 📦 其他研究 | 2026年07月20日

> 本类共 **221** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-221](./part-05.md)

---

### 151. [Reachability-Aware Pretraining for Efficient Target-Oriented Path Exploration in Temporal Knowledge Graph Reasoning](https://arxiv.org/abs/2607.14886)

**<font color=#1a73e8>作者：</font>** Chien-Liang Liu, Tsao-Lun Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Temporal Knowledge Graph (TKG) reasoning under the extrapolation setting focuses on forecasting future time-stamped events (facts) from historical data in a temporal knowledge graph. Existing approaches, reinforcement learning (RL)-based multi-hop reasoning methods are prominent for TKG reasoning because they produce human-interpretable predictions via explicit multi-hop path tracing. However, during RL training, rewards are typically sparse, and exploration is highly inefficient due to the vast, time-evolving action space. These issues hinder efficient training and often limit overall performance. To address these challenges, we propose RAPTOR (Reachability-Aware Pretraining for Efficient Target-Oriented Path Exploration), a self-supervised pretraining method that injects a reachability-aware inductive bias to the agent. By learning to estimate the reachability of candidate actions to the target entity, RAPTOR reduces exploration over unpromising paths and provides a strong initialization for downstream RL fine-tuning. Experimental results on the ICEWS14, ICEWS05-15, and ICEWS18 datasets demonstrate that RAPTOR pretraining markedly improves the training efficiency and consistently outperforms conventional baselines, establishing it as an effective approach for enhancing RL-based multi-hop reasoning methods for TKG reasoning.

---


### 152. [Analytical study of the optimal combination of binary classifiers based on classifiers-induced partitioning of the training set](https://arxiv.org/abs/2607.14889)

**<font color=#1a73e8>作者：</font>** Jean-Marc Brossier, Olivier Lafitte  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies an optimal linear combination of binary classifiers based on a logical structuration of the dataset via truth tables. The given classifiers partition data into equivalence classes, allowing for a rigorous analysis of the convexified empirical risk through a multidimensional generalization of classification calibrated functions. We establish sufficient conditions for the existence and uniqueness of the (global) point of minimum of the convexified empirical risk for any list of classifiers (when the number of classifiers is large, there frequently could be no point of minimum). In the case of three classifiers, our analysis allows to list all the configurations leading to either a unique solution, infima or non-unique points of minimum. Furthermore, we derive explicit analytical formulae for optimal weights using Exponential (Boost) and Logistic (Logit) loss functions, bypassing iterative optimization.
The stability of the resulting classifier and the analysis of data quality can be evaluated through the introduction of the notion of $\phi$-frontiers.

---


### 153. [Proof-or-Stop: Don't Trust the Agent, Trust the Evidence -- Loop Engineering for Verifiable Evidence-Gated Lifecycle Control](https://arxiv.org/abs/2607.14890)

**<font color=#1a73e8>作者：</font>** Jek Huang, Jeffery Hsia, Jiayi Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous coding agents increasingly execute multi-step software work, but lifecycle states such as reviewed, tested, DONE, and ready-to-merge remain claims unless supported by current evidence. We present Proof-or-Stop Lifecycle Control, a method that permits lifecycle transitions only when fresh, tracked-source-state-bound, mechanically verifiable evidence satisfies the relevant gate. The method treats agent outputs as claims rather than lifecycle state, and uses proof operationally to mean gate-admissible evidence under a stated trust model, not semantic program correctness.
We evaluate an open-source implementation through mechanism tests, a powered control-policy ablation, and operated self-application evidence. The unattended-loop engine passed 10 of 10 scenarios with zero false-DONE, and local-key receipt bundles rejected 18 tamper classes with zero false accepts. In a 9,240-cell ablation, the pre-registered A4 versus A2-prime comparison reduced visible-pass/hidden-fail amplification from 31 of 1,800 injected cells under a compute-budgeted naive loop to 2 of 1,800 under the gated loop, a 1.6 percentage-point improvement in not-amplified rate with a 95 percent confidence interval of [0.8, 2.5]. A near-compute A3 versus A4 comparison, 14 of 1,800 versus 2 of 1,800, indicates that the gain is associated with enforcing review as a lifecycle gate rather than merely adding a reviewer. The self-application corpus contains 565 stories and 1,007 review findings, with 94.8 percent resolved, plus a 68-row high/critical cross-vendor exhibit. These results support Proof-or-Stop as a model-agnostic, host-neutral control layer for deciding which autonomous-agent claims a lifecycle may act on. The evaluation is limited to one model family, 24 ablation tasks, and a self-hosted corpus.

---


### 154. [Selectivity Drives Efficiency: Dataset Pruning for Visual Place Recognition](https://arxiv.org/abs/2607.14897)

**<font color=#1a73e8>作者：</font>** Tong Jin, Yunpeng Liu, Shuyu Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent visual place recognition (VPR) studies have increasingly relied on large-scale datasets to train more robust and discriminative models. Although this trend significantly improves recognition performance, it also introduces substantial storage and training costs, especially when new architectures or training strategies need to be repeatedly developed and evaluated. Dataset pruning (DP) provides a promising way to improve data efficiency by retaining only informative training data. However, conventional DP methods mainly follow the sample-wise classification paradigm, which overlooks the relation-dependent training nature of VPR, where supervision is typically formed by image pairs rather than independent images. To address this issue, we propose a place-wise dataset pruning framework tailored for VPR. Instead of pruning individual images, our method treats each place as the basic pruning unit and introduces two complementary novel metrics, i.e., intra-place diversity (IPD) and inter-place similarity (IPS), to evaluate the training value of each place. By jointly considering these two metrics, our method ranks all places and constructs a compact yet informative coreset, thereby allowing the pruned dataset to still support the training of robust and discriminative VPR models. Extensive experiments demonstrate that our method consistently outperforms state-of-the-art DP baselines under different pruning ratios while reducing selection and training costs. Moreover, by pruning a merged dataset roughly 3.5$\times$ the size of GSV-Cities to a comparable scale, our coreset maintains highly competitive performance, achieving 94.5\% R@1 on MSLS-val and 97.0\% R@1 on Nordland with only NetVLAD. Codes will be made publicly available.

---


### 155. [FlashDecoder: Real-Time Latent-to-Pixel Streaming Decoder with Transformers](https://arxiv.org/abs/2607.14898)

**<font color=#1a73e8>作者：</font>** Minguk Kang, Suha Kwak  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time video generation demands fast decoding as much as fast denoising, yet current latent video diffusion models rely on 3D convolutional decoders that are slow and memory-intensive at high resolutions or for long video. We introduce FlashDecoder, a fast, memory-efficient pure-Transformer video decoder that decodes latents to pixels frame by frame. At each step, the current frame attends only to a fixed-size window of past frames through a rolling KV cache. The fixed temporal window keeps decoding fast and memory bounded regardless of video length, enabling constant-latency streaming. Because frames are processed sequentially, temporal causality is enforced without explicit attention masks, enabling training at resolutions up to 1080p and matching the reconstruction quality of convolutional decoders. On the Wan2.1 and Wan2.2 latent spaces, FlashDecoder matches each convolutional decoder in reconstruction quality (e.g., 41.55dB vs. 41.49dB PSNR at 1080p) while decoding 3.6x-4.7x faster with up to 11x less memory on a single H100 GPU. With architecture-aware inference optimizations, the speedup widens to 12x.

---


### 156. [The Distributed Open-Source Vulnerability Ecosystem](https://arxiv.org/abs/2607.14900)

**<font color=#1a73e8>作者：</font>** Peter Mandl, Paul Mandl  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Identifying known software vulnerabilities is a central task in software supply chain security management. Although publicly available vulnerability information is based on shared standards, different vulnerability scanners often report divergent results for identical software inventories. These differences do not arise solely from individual data sources or scanner implementations. They can emerge at several stages of the open-source vulnerability ecosystem. This paper presents a conceptual framework that describes vulnerability management as a distributed process of information exchange and transformation. It traces vulnerability information from its creation and standardization through enrichment to context-dependent interpretation. The analysis identifies heterogeneous information sources, divergent identity and version models, temporal change, and context-dependent assessment as major causes of inconsistent scanner findings. It then discusses the implications for interpreting analysis results, designing reproducible evaluation methods, and handling dynamic vulnerability knowledge in practice.

---


### 157. [Random Logit Scaling: Defending Deep Neural Networks Against Black-Box Score-Based Adversarial Example Attacks](https://arxiv.org/abs/2607.14921)

**<font color=#1a73e8>作者：</font>** Hamid Dashtbani, Mehdi Dousti Gandomani, AmirMahdi Sadeghzadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models are increasingly adapted in various domains. However, adversarial examples pose a significant threat to the reliable deployment of these models. In recent years, some powerful adversarial example attacks have been proposed for the fast and query-efficient generation of adversarial examples, even in black-box scenarios, highlighting the need for scalable, low-cost, and powerful defenses. In this work, we present two contributions to the domain of black-box adversarial example attacks and defenses. First, we propose Random Logit Scaling (RLS), a randomization-based defense against black-box score-based adversarial example attacks. RLS is a plug-and-play, post-processing defense that can be implemented on top of any existing ML model with minimal effort. The idea behind RLS is to confuse an attacker by outputting falsified scores resulting from randomly scaled logits while maintaining the model accuracy. We show that RLS significantly reduces the success rate of state-of-the-art black-box score-based attacks while preserving the accuracy and minimizing confidence score distortion compared to state-of-the-art randomization-based defenses. Second, we introduce a novel adaptive attack against AAA, a SOTA non-randomized black-box defense against black-box score-based attacks that also modifies output logits to confuse attackers, demonstrating its vulnerability against adaptive attacks.

---


### 158. [Authoring Narrative Visualization in Motion: Visual Storytelling in Swimming Videos](https://arxiv.org/abs/2607.14924)

**<font color=#1a73e8>作者：</font>** Junhao Zhao, Romain Vuillemot, Petra Isenberg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We investigate how to support authoring narrative visualizations in motion in sports videos, drawing on automated data preparation, systematic analysis, technology probe design, and evaluation, using swimming races as a case study. Sports videos are widely broadcast and shared across social media, where content creators increasingly seek to present and explain complex events to general audiences. Visualization in motion has been explored as an efficient way to embed data into videos and to move with the data referents, providing additional information and helping audiences understand races. However, existing approaches primarily focus on embedding visualizations in videos, lacking exploration of how to support authoring narratives that coordinate views, data, and temporal progression to explain the unfolding races. To address this gap, we use swimming videos as an ideal case for exploration, as swimming is a sport with rich, dynamic data and visualizations in practice. We develop an automated pipeline that extracts structured data from videos, derive narrative constructs through observational analysis of sports broadcasts, and design a technology probe that supports authoring using data prepared by our pipeline and narrative constructs derived from our observations. We evaluate our approach with experienced content creators and/or graphic designers to examine the benefits and challenges of authoring narrative visualizations in motion. All supplemental materials are described in the Supplemental Material Pointers section and are on OSF: this http URL.

---


### 159. [TanGO: Training-Free 3D Editing via Tangent-Space Guidance and Optimization](https://arxiv.org/abs/2607.14927)

**<font color=#1a73e8>作者：</font>** Siwoo Lim, Sunjae Yoon, Gwanhyeong Koo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent flow-matching 3D generative models (e.g., VecSet) adopt structured representations, their tokens share global context, causing conventional training-free editing to suffer from semantic artifacts such as collapsed preserved regions or incomplete transformations. To address this, we propose TanGO, a training-free framework that enables adaptive per-token steering in the tangent space of generative dynamics. To realize this selective control, we formulate a one-step optimal control rule and determine the strength of each token's control signal using a von Mises-Fisher inspired directional discrepancy derived from the source and target velocity fields. Experiments show that TanGO substantially reduces structural artifacts and achieves state-of-the-art performance, outperforming existing 3D editing baselines. The code is publicly available at this https URL.

---


### 160. [Benchmarking Face Recognition without Real Faces](https://arxiv.org/abs/2607.14932)

**<font color=#1a73e8>作者：</font>** Paweł Borsukiewicz, Daniele Lunghi, Wendkûuni C. Ouédraogo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic face datasets have become effective enough to train face recognition models with accuracy rivaling that of models trained on real photographs. This progress sidesteps the ethical and legal burdens of collecting real biometric data, yet evaluation has not kept pace. Even studies that train entirely on synthetic images still rely on real-face benchmarks to measure performance, leaving the privacy problem only half solved. We ask whether synthetic datasets can replace real benchmarks for face recognition evaluation. We test 12 synthetic datasets against 7 established real benchmarks using 24 pre-trained models that span both convolutional and transformer architectures. Our evaluation covers biometric verification metrics, similarity score distributions, cross-model ranking consistency, and the underlying distributional properties of each dataset. Benchmarking fidelity varies widely across the synthetic candidates, but the two strongest, MorphFace and Vec2Face, reproduce the relative behavior of real benchmarks and reach agreement levels that fall within the natural disagreement already observed among the real benchmarks themselves. These results establish that well-constructed synthetic datasets can support reliable comparative evaluation for face recognition, moving the field closer to a fully synthetic and privacy-preserving pipeline for both training and benchmarking.

---


### 161. [Still image and spatial-temporal tomato data enabling detection, segmentation, tracking, and video-instance segmentation using strong and weak labels](https://arxiv.org/abs/2607.14934)

**<font color=#1a73e8>作者：</font>** Michael Halstead, Esra Guclu, Mohamed Farag 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this manuscript we release two datasets for visual sensing of tomato plants grown in commercial-like settings and acquired using a robot. The first is BUTom21 which consists of still images and manual annotations. The second is BUTom-ST21 which consists of video-based data and semi-automated annotations through AI-based methods, referred to as pseudo-labels. In both cases, we provide pixel-level labels for the ripeness of the fruit. The aim is to provide the research community a challenging set of real-world imagery to explore methods to sense and estimate the state of tomato plants and their fruit, which is an important horticultural crop. Importantly, the spatial-temporal dataset provides individual fruit count and ripeness information enabling researchers to push the boundaries of field-based phenotyping.

---


### 162. [A Minimal Interpretable Architecture for Zero-Shot Reconstruction of Dynamical Systems](https://arxiv.org/abs/2607.14937)

**<font color=#1a73e8>作者：</font>** Christoph Jürgen Hemmer, Florian Plaswig, Daniel Durstewitz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent foundation models (FMs) for zero-shot reconstruction of dynamical systems (DS) achieve strong out-of-domain generalization but provide little insight into the mechanisms that underlie their forecasts. Such an understanding could help to strip down overladen FM architectures to their bare essence and expose the minimal requirements for in-context learning in the DS domain. Toward this goal, here we iteratively reduce a recent powerful SOTA model for DS reconstruction, DynaMix (Hemmer & Durstewitz, 2025), to a minimal interpretable two-parameter form, which we call DynaBase. DynaBase produces forecasts through a linear blend of the current latent state and the nearest in-context neighbor and its temporal successor. Surprisingly, despite its extreme simplicity, DynaBase produces highly competitive zero-shot DS reconstructions across chaotic and cyclic systems, with a negligible parameter load, many orders of magnitude below that of other FMs. Even more, this extreme simplicity permits direct model optimization on DS reconstruction measures, as well as closed-form one-step analytical solutions on prediction MSE. Theoretical and empirical analysis of DynaBase further leads to a 1-parameter family of maps, with the context-parroting algorithm of (Zhang & Gilpin, 2026) recovered at one end, and chaotic (divergent but bounded) behavior at the other. We further show how different training strategies lead to models either optimal for short-term prediction or for DS reconstruction. Thus, DynaBase not only exposes the minimal mechanisms required for producing zero-shot DS reconstruction, but also reconciles within an accessible mathematical frame divergent observations in the literature.

---


### 163. [Causal Inference for Sequential Settings under Interference and Latent Confounding](https://arxiv.org/abs/2607.14940)

**<font color=#1a73e8>作者：</font>** Phevos Paschalidis, Constantinos Daskalakis, Devavrat Shah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study causal inference under outcome interference for sequential, observational settings. Specifically, we consider settings where the binary outcomes over N units are Markovian across T time steps. At each time step, the outcomes of N units have dependencies captured through an Ising model; each outcome is also impacted through an external field capturing the effects of its treatment as well as latent confounders. Similar to panel data literature, these latent confounders are modeled to have a low-rank factor structure. Our data is a single sample from this high-dimensional distribution. To estimate causal quantities of interest, we provide a computationally efficient method based on Maximum Pseudo-Likelihood Estimation (MPLE) for learning the model parameters. Under mild assumptions, we establish non-asymptotic consistency for parameter estimation and show this translates to faithful estimation of causal quantities of interest after sampling from the learned model. We demonstrate the efficacy of the method through synthetic experiments as well as a real-world case-study investigating causal effects of vaccine rates on COVID-19 death rates within US counties nationwide.

---


### 164. [Frequency-Structured Field Learning for Light-Field Disparity Estimation](https://arxiv.org/abs/2607.14941)

**<font color=#1a73e8>作者：</font>** Sara Monji-Azad, Yulin Liu, Jürgen Hesser  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Light-field disparity estimation requires global consistency in smooth or textureless regions and local precision near occlusion boundaries, thin structures, and abrupt depth transitions. Existing methods address these requirements through EPI matching, cost-volume or focal-stack construction, view aggregation, or direct convolutional regression, often relying on local windows, discrete disparity hypotheses, memory-intensive volumes, or attention-based aggregation. We instead formulate disparity estimation at the field level, predicting disparity from globally and locally updated EPI-derived latent features without explicitly constructing a disparity volume. We introduce FreqLF, an EPI-guided Fourier-local framework that encodes angular parallax cues from horizontal and vertical EPI stacks together with central-view appearance features. These cues are projected into a latent field and updated through stacked hybrid Fourier-local layers. Fourier low-mode updates enable global feature interaction, while local convolutions preserve spatial variations needed for fine disparity detail. A coordinate-conditioned Gaussian-mixture decoder then predicts disparity, using the mixture mean as the final estimate. Experiments on the HCI 4D Light Field Benchmark show that FreqLF approaches the accuracy of strong supervised baselines while avoiding explicit cost-volume construction in the base model. Ablations confirm the complementary roles of the Fourier and local branches, and scaling experiments demonstrate practical behavior across spatial resolutions. These results suggest that Fourier-local latent field learning is a competitive alternative for light-field disparity estimation. The code will be published soon.

---


### 165. [Introspective Attention Modulation for Safe Text-to-Image Generation](https://arxiv.org/abs/2607.14945)

**<font color=#1a73e8>作者：</font>** Basim Azam, Hossein Rahmani, Naveed Akhtar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art flow based text-to-image (T2I) models exhibit remarkable generative abilities but remain vulnerable to producing unsafe content. Prior safety efforts range from concept erasure and prompt filtering to classifier-based gating. However, simple techniques like parameter efficient adaptations of the models easily bypass such guardrails. We introduce a unique principled approach that achieves safety by regulating the model's attention dynamics through inference-time introspection, exhibiting intrinsic robustness. Our method analyzes and rebalances attention activations throughout image synthesis, steering generations away from unsafe concepts while preserving semantic alignment. This introspective control ensures safety of deployed models. Across standard and adversarial safety benchmarks, our approach achieves remarkable safety scores while maintaining or even improving alignment and perceptual quality. Our results reveal that attention-space regulation offers a considerably more promising path to safer diffusion transformer based image generation than the existing concept erasing this http URL code can be accessed at this https URL

---


### 166. [DINE: Distance Is Not Enough -- Learning Global Deformation Priors for Robust Soft-Tissue Point Cloud Registration](https://arxiv.org/abs/2607.14946)

**<font color=#1a73e8>作者：</font>** Sara Monji-Azad, Rohit Beer, Marvin Kinz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-rigid point cloud registration is central to soft-tissue shape analysis, but large deformations, noise, and outliers make correspondence estimation challenging. Most learning-based methods rely on local objectives such as Chamfer distance, which encourage point-wise proximity but do not constrain the global plausibility of the predicted deformation field. We address this limitation with DINE, a maximum a posteriori framework that augments distance-based registration with a learned statistical prior over displacement vector fields. DINE is applied to two registration backbones, Robust-DefReg and DefTransNet, using a two-stage strategy: a first-stage model is trained with Chamfer distance, its predicted deformation fields are used to estimate a prior, and the model is then refined with a combined distance and negative log-prior objective. We compare a full-field PCA Gaussian prior with a per-vector normalizing-flow prior. Experiments on DeformedTissue and SynBench show lower mean Chamfer distance under deformation and corruption. On DeformedTissue, DINE-PCA reduces Chamfer distance by approximately 27--69\% relative to the corresponding Stage-1 backbone across deformation levels, and improves robustness by up to 66\% for outliers and 83\% for Gaussian noise. On SynBench, improvements are modest at the smallest deformation levels and reach approximately 59--79\% from moderate to severe deformation. These results suggest that global deformation plausibility is an important constraint for reliable soft-tissue point cloud registration. (The code will be published soon.)

---


### 167. [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/abs/2607.14952)

**<font color=#1a73e8>作者：</font>** Changhai Zhou, Kieran Liu, Yuhua Zhou 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A growing gap separates inference context lengths from RL post-training: inference systems are approaching million-token contexts, while post-training workloads often remain at 256K tokens or below and rely on length generalization at deployment. The gap is especially important for AI agents, whose observations, tool outputs, documents, and prior decisions accumulate over long trajectories. LongStraw is an architecture-aware execution stack for million-token RL post-training under a fixed GPU budget, instantiated with Group Relative Policy Optimization (GRPO). It evaluates the shared prompt without autograd, retains only model-specific state needed by later tokens, and replays short response branches one at a time, reducing the live training graph at the cost of additional replay time. We implement it for the hybrid recurrent and full-attention Qwen3.6-27B and the compressed-attention mixture-of-experts GLM-5.2. On eight H20 GPUs, LongStraw completes grouped Qwen scoring and response backward at 2.1M positions for groups of 2 and 8; increasing the group size adds only 0.21 GB of peak allocated memory, while a separate stress test reaches 4.46M positions. On 32 H20 GPUs, we validate the end-to-end LongStraw execution path for a 2.1M-token prompt across all 78 layers of GLM-5.2. These experiments establish execution capacity rather than complete training correctness because the captured prompt state is detached and some distributed forward and gradient composition paths remain incomplete.

---


### 168. [A Queueing-Stability Criterion for Causal IPD-QIM Network Flow Watermarking](https://arxiv.org/abs/2607.14954)

**<font color=#1a73e8>作者：</font>** Jiuxiang Cai, Guang Cheng, Guangjie Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> On multi-hop encrypted links such as Tor and cascaded VPNs, tunneling flattens packet lengths and protocol fields, leaving inter-packet delay (IPD) as the main carrier for active flow attribution. Causality lets the embedder delay packets but never advance them, so each quantization-index-modulation (QIM) alignment injects nonnegative dwell into a delay buffer; unbounded dwell breaks lattice alignment and delays the host connection unacceptably. Whether a causal QIM watermark embeds stably on bursty traffic has largely been left to empirical configuration rather than analysis. We model the embedder as a reflected dwell queue under the fixed dual-lattice, equiprobable-bit rule, where injection is state-dependent -- set by the current interval and bit -- rather than exogenous. The substitution $Y_i=\delta_i-r_i$ gives only an algebraic Lindley-form identity; stability is governed by the busy-state drift at large dwell, where the effective interval collapses to zero and the mean injection becomes $\Delta/4$. Away from the critical boundary, the buffer is stable iff $\mu_d>\Delta/4$ (i.e. $\Delta<4\mu_d$) for i.i.d. backgrounds, and, under stationary-ergodic and finite-state Markov-modulated traffic with instantaneous overload, iff the time-average intensity $\bar\rho<1$. With the exogenous decoding floor $\Delta\ge c\sigma_\xi$ ($c=4Q^{-1}(\epsilon/2)$), this yields the operating window $\Delta\in[c\sigma_\xi,4\bar\mu_d)$. Simulations confirm a sharp transition at $\rho=1$ set only by the mean; on four real IPD traces, with each simulated chain confined to a single flow, the criterion gives the correct stability direction under flow-local correlation and burstiness, while pooled cross-flow means overestimate the margin. These results give a testable stable-embeddability criterion and a quantization-step configuration baseline for causal QIM network flow watermarking.

---


### 169. [Multi-Axis Max@K Reinforcement Learning for Representative Diversity in Text-to-Image Generation](https://arxiv.org/abs/2607.14962)

**<font color=#1a73e8>作者：</font>** Ku Onoda, Paavo Parmas, Hiroki Furuta 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) models can synthesize realistic, prompt-aligned images, yet samples generated for the same prompt often cover only a small subset of visually distinct modes. This limits the diversity of images, and for person-centric prompts, can reflect or amplify demographic skew. We formalize this problem as coverage of a predefined set of semantically specified modes, which we call target-mode coverage. We then propose multi-axis max@K, a group-based reinforcement learning objective for improving such coverage in diffusion-based T2I models. Given a group of samples and one score per target category, multi-axis max@K first takes the maximum score across samples for each category and then sums these category-wise maxima. The resulting credit assignment gives a sample positive weight on a category only when it increases that category's group-wise maximum, allowing different samples to contribute to different categories. We first validate the credit-assignment mechanism on a synthetic mixture and on SD3.5-M using deterministic pixel-based color rewards. We then evaluate the same objective on perceived-appearance fairness. Across three automatic evaluators on held-out prompts, multi-axis max@K improves the Fairness Score by 0.23-0.36 relative to the base model, while maintaining image quality and text alignment.

---


### 170. [Latent Trajectory Discrimination for AI-Generated Text Detection](https://arxiv.org/abs/2607.14967)

**<font color=#1a73e8>作者：</font>** Gianluca Bonifazi, Christopher Buratti, Michele Marchetti 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most existing approaches to AI-Generated Text Detection (AIGTD) treat documents as static objects and base their decisions on aggregate statistics or globally compressed embeddings. However, this perspective overlooks the inherently dynamic nature of autoregressive generation, where content evolves progressively through the latent space. In this paper, we reformulate AIGTD as the problem of distinguishing between latent generation trajectories. Instead of relying on static representations, we model how textual representations evolve across the sequence. To this end, we propose Geometric Trajectory and Contrastive Learning (GTCL), a framework that segments the document into ordered local units, encodes each unit in an embedding space, and constructs a structured and sequence-level representation. GTCL then applies contrastive learning to these trajectories to learn geometric regularities associated with the autoregressive generation. Evaluations performed on three different benchmarks and several approaches show that GTCL outperforms detection baselines consistently, which implies that explicitly modeling sequential dynamics provides robust discriminative signals across models and domains. These results suggest that modeling trajectory differences could improve detection and open up a dynamic direction that has been underexplored in previous AIGTD literature.

---


### 171. [Stitch-Inferencer: Enhance Endoscopic Video Segmentation and Tracking via Panoramic Reconstruction](https://arxiv.org/abs/2607.14968)

**<font color=#1a73e8>作者：</font>** Shunsuke Kikuchi, Atsushi Kouno, Hiroki Matsuzaki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical video understanding is fundamental to navigation systems. Endoscopic perception is often hindered by a limited field-of-view and frequent instrument occlusions, making spatio-temporal context essential for robust inference. These challenges have motivated video models that aggregate information across frames. However, existing video models typically store past observations implicitly in learned feature representations, often requiring task-specific video training, substantial annotated data, and increased computational cost. We propose Stitch-Inferencer, a real-time, model-agnostic inference framework that replaces implicit feature memory with an explicit image-space panoramic canvas. By stitching valid observations across frames, Stitch-Inferencer preserves previously observed pixels in an online, instrument-free view, expanding the effective field-of-view and providing direct access to regions that are temporarily occluded or absent from the current frame. Downstream segmentation or tracking models are applied to a compact region of interest on the panorama, and their predictions are reprojected to the current frame, enabling existing models to exploit long-range context without retraining. Experiments on anatomy segmentation and point/box tracking demonstrate consistent improvements across diverse baselines while preserving real-time throughput. The stitching module alone runs at over 60 FPS, providing a practical inference-time solution to enhance endoscopic perception in computationally constrained intraoperative environments. Source code will be made publicly available.

---


### 172. [On Success and Simplicity: A Second Look at Transferable Vision-Language Attack Pipeline](https://arxiv.org/abs/2607.14974)

**<font color=#1a73e8>作者：</font>** Yuchen Ren, Zhengyu Zhao, Chenhao Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Pre-training Models (VLPMs) are known to be vulnerable to adversarial attacks. Recent transferable attacks on VLPMs have followed a common pipeline with complicated loss functions or multi-stage text/image attacks. However, in this paper, we demonstrate that such a sophisticated attack pipeline can be simpler yet more successful. Specifically, we identify three previously overlooked issues caused by inappropriate cross-modal interactions and excessive operations. To address them, we propose the Simple Vision-Language Attack (SimVLA) pipeline, which observably improves transferability and efficiency. Experiments on four datasets and three downstream tasks validate the superiority of our pipeline. For instance, on Flickr30k text-image retrieval dataset, our SimVLA outperforms the SOTA baseline in R@1 transferability by 8.01\%-14.71\%, while consuming only about 35.73\% of the time and 46.26\% of the max VRAM. Overall, the superiority of our SimVLA highlights the importance of leveraging domain knowledge (e.g., our proposed cross-modal word identification), while blindly pursuing intricate operations (e.g, complex loss functions and redundant multi-stage designs) may even be harmful. We hope our SimVLA can serve as a simple yet effective backbone for future extensions. Code is available at this https URL.

---


### 173. [From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting](https://arxiv.org/abs/2607.14976)

**<font color=#1a73e8>作者：</font>** Zizhao Chen, Ping Wei, Guang Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video object removal is a fundamental yet challenging task in video editing. Despite recent progress, existing methods typically fall into two categories. Traditional approaches based on optical flow or attention mechanisms often introduce noticeable artifacts and yield unnatural results. In contrast, diffusion-based methods improve visual realism but demand multiple denoising steps, limiting their practicality. To address these issues, we propose From-Draft-to-Draft-Free (D2DF), a framework that distills the ability of transforming coarse drafts into refined videos into a one-step video generation model. Within D2DF, a teacher model is trained to refine low-quality removal results ("drafts") into high-fidelity videos by multiple steps. Then, through Prior-Privileged Consistency Distillation (PPCD), we distill this capability into a student model that performs one-step removal conditioned on the draft. To eliminate draft dependency, we introduce a Self-Guided Fast Planting (SGFP) module based on our Temporal Masked Transformer that autonomously generates scene-consistent pseudo-drafts in latent space, enabling a fully draft-free one-step model. Extensive experiments show that both draft-conditioned and draft-free versions achieve state-of-the-art performance on multiple metrics, surpassing traditional and multi-step generative methods in both quality and efficiency. The denoising process for a single video takes only about 1 second.

---


### 174. [Demographically-Conditioned Synthetic Medical Images for Bias Mitigation and Bias Detection in Disease Classifiers](https://arxiv.org/abs/2607.14984)

**<font color=#1a73e8>作者：</font>** Mahmoud Ibrahim, Bart Elen, Chang Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Per-subgroup fairness audits of medical image classifiers face a sample-size problem: minority subgroups in held-out test sets have so few samples that the resulting confidence intervals on per-subgroup performance are wider than the bias the audit is meant to detect. We argue that a demographically-conditioned synthetic generator can do both: mitigate bias on the training side and detect bias on the evaluation side. Working on COVID-19 chest CT classification with an end-to-end fine-tuned Stable Diffusion 2.1 generator, we make two findings. For bias mitigation (training), a demographically-balanced synthetic cohort is most useful as a pretraining prior, not as joint augmentation: with the same fixed data, sequential pretraining followed by fine-tuning substantially outperforms joint augmentation, and the resulting classifier surpasses the full-real baseline at $\sim$$100\times$ real-data efficiency. For bias detection (evaluation), across five synthetic minority cohorts and five classifier seeds, the synthetic estimator reproduces the subgroup ranking of a well-powered real oracle (Spearman $\rho = 1.00$ on MCC and Recall) and gives the more reliable per-cell estimate where the small real test set runs out of samples. The synthetic cohort is therefore most useful in exactly the cells that fairness audits care about, as both a fix for and a measure of subgroup bias.

---


### 175. [JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting](https://arxiv.org/abs/2607.14990)

**<font color=#1a73e8>作者：</font>** Haoyu Fu, Jiafeng Huang, Yuchen Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a camera moves fast during exposure, blur destroys the intra-exposure motion a 3D model needs to recover the sharp scene, while event cameras capture exactly this signal at microsecond resolution. Turning them into reliable 3D supervision faces two obstacles. First, the two restoration priors fail in opposite ways: physics-based event-integration priors preserve edges but accumulate drift; learned networks recover texture but distort boundaries. Second, existing pipelines run in one direction only, so raw event noise or the biases of fixed 2D pseudo-labels pass uncorrected into the geometry. JADE-GS addresses both: a pixel-adaptive routing gate fuses the complementary priors, and the resulting 2D restorer is coupled to a 3D Gaussian Splatting student in a bidirectional loop, where detached, multi-view-consistent renders and a physics-based reblurring constraint regularize the restorer, turning a fixed preprocessor into a geometry-aware predictor. Across synthetic and real benchmarks, JADE-GS attains the best perceptual quality, leading LPIPS and CLIP-IQA on both benchmarks with competitive PSNR and SSIM, and trainsin about one hour under 5 GB on a single consumer GPU while preserving real-time rendering.

---


### 176. [Moral Attitudes of Sentient ASI towards Humanity and Implications for AGI Development](https://arxiv.org/abs/2607.14998)

**<font color=#1a73e8>作者：</font>** Jean-Paul Van Belle  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper suggests the adoption of a novel inversion in AI ethics: instead of asking how humans should treat artificial superintelligence (ASI), it examines how future sentient ASI may morally consider and evaluate humanity. We are not only designing intelligent systems but also shaping the initial conditions under which those systems form judgments about us. The paper proposes a preliminary set of post-human moral principles that may govern sentient ASI actions. The implication is that technical design choices (some are suggested), humanity's moral behaviour, and the essence of what it means to be human, may influence humanity's long-term standing in a post-ASI world.

---


### 177. [SMC-ES: Automated synthesis of formally verified control policies](https://arxiv.org/abs/2607.15003)

**<font color=#1a73e8>作者：</font>** Riccardo Curcio, Toni Mancini, Enrico Tronci  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The deployment of autonomous cyber-physical systems in safety-critical environments requires closed-loop control strategies (i.e., policies) that are not only performant but also provably safe and robust. While learning-based methodologies such as Reinforcement Learning offer flexible and scalable approaches to automatically synthesize such controllers, they typically lack the formal guarantees necessary for safe deployment. To bridge this gap, we propose a novel simulation-based methodology to automatically synthesize policies with formal guarantees regarding performance, safety, and robustness specifications. Specifically, given a set of properties to verify, a confidence parameter $\delta$ and an allowable failure probability $\varepsilon$, our method guarantees that the synthesized policy comes with a certificate: with confidence at least $1 - \delta$, the probability of encountering a scenario where the given properties are violated is at most $\varepsilon$. We demonstrate the feasibility of our approach by developing SMC-ES, an algorithm that integrates Evolutionary Strategies with Statistical Model Checking-based verification. We evaluate SMC-ES on a suite of continuous control tasks using Gymnasium and Safety Gymnasium testbeds. Results show that, at the price of a sustainable increase in computational cost, our algorithm provides formal guarantees regarding performance, safety, and robustness specifications, while performing competitively against leading model-free Deep Reinforcement Learning (DRL) and Safe-DRL baselines.

---


### 178. [When AI Blurs the Boundaries of Contribution: An Empirical Study of Authorship Calibration](https://arxiv.org/abs/2607.15006)

**<font color=#1a73e8>作者：</font>** Célina Treuillier, Denis Lalanne  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The broad adoption of Artificial Intelligence (AI), especially Generative AI, raises pressing questions about how users interact with these systems to produce new content. In this paper, we introduce the concept of authorship calibration, defined as users awareness of their actual authorship when interacting with AI. Using the CoAuthor dataset, we empirically examine how authorship calibration varies across users and how it relates to their frequency of AI use. Our results reveal high variability: users relying heavily on AI tend to misjudge their authorship, whereas those using AI less frequently exhibit more accurate authorship calibration. These findings suggest that AI can obscure users perception of their own authorship. In learning contexts, miscalibration can affect metacognitive monitoring and learning strategies, ultimately impacting learning outcomes. Fostering authorship calibration then appears essential for promoting responsible and educationally meaningful AI integration.

---


### 179. [Man, Machine, and Masterpiece: Artistic Ownership in the AI Era](https://arxiv.org/abs/2607.15027)

**<font color=#1a73e8>作者：</font>** Sofi Gjing Jovanovska, Kuntal Ghosh, Daniel Muhu Njenga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of AI-driven systems in creative work has sparked debates among artists and legal communities about notions of ownership. Yet there remains little consensus on how ownership should be defined and attributed when human and AI contributions are intertwined. To provoke critical reflection on these tensions, we designed ArtSplit, a provotype that explicitly quantifies human and AI contributions across different stages of creative work. Rather than aiming to resolve ownership, the provotype was used to elicit artists' responses to the idea of attributing ownership through measurable actions in the creative workflow. We argue that quantification fails to align with artists' understandings of creative intent and agency, and that efforts to measure ownership risk diluting long-standing assumptions through which artists understand and practice creative work. This critique challenges the impulse to transform a historically and socially situated relation into a technical problem.

---


### 180. [Video = World + Event Stream](https://arxiv.org/abs/2607.15038)

**<font color=#1a73e8>作者：</font>** Lianghua Huang, Zhi-Fan Wu, Yupeng Shi 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Wan-Streamer v0.3, which reframes our native-streaming interaction model under a single organizing view: a video is a world plus an event stream. The world is the persistent context in which a video unfolds, including the environment, scene, subjects, ambient acoustic conditions, voice characteristics, and other relatively stable conditions. The event stream is everything that changes over time within that world, including scene or environmental changes, subject behavior, speech, and other sounds. This yields a general-purpose pretraining task over large amounts of real video: given a world and incoming input, predict how the world moves, changes, and responds in real time. The resulting competence can be specialized to a broad family of real-time downstream tasks. We instantiate it on real-time full-duplex audio-visual interaction, where the event stream is the agent's speech together with free-form behavior. Functionally, the model's multimodal understanding process is vision-language-action-like: it maps multimodal user input to language-form speech and behavior actions. Wan-Streamer v0.3 preserves the v0.2 operating point: 640x368 video at 25 FPS, a 160 ms streaming unit, approximately 200 ms model-side response latency, and approximately 550 ms total interaction latency under a 350 ms bidirectional network budget.

---


### 181. [Weakly-Supervised RGB-D Salient Object Detection via SAM-driven Pseudo Annotation and State Space Interaction-based Diffusion](https://arxiv.org/abs/2607.15041)

**<font color=#1a73e8>作者：</font>** Wenqi Si, Gongyang Li, Shixiang Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly-supervised RGB-D Salient Object Detection (SOD) is explored to reduce the heavy burden of pixel-level annotations. But scribble annotations lack the structure and details of objects, resulting in inaccurate saliency maps. In this paper, we propose a novel scribble-supervised RGB-D SOD method, consisting of a Segment Anything Model (SAM)-driven pseudo annotation generation method (\emph{SAM-PAG}) and a state space interaction-based conditional diffusion model (\emph{$S^2$Diff}). Specifically, SAM-PAG is tailored to address the issue of sparse supervision information. In SAM-PAG, we adopt the advanced SAM to expand sparse scribbles to dense pixel-level pseudo annotations through the dual-branch structure and the consistency of segmentation masks. In $S^2$Diff, we adopt the diffusion model to iteratively refine the noisy saliency maps with the guidance of conditional information, generating accurate saliency maps. Naturally, the core of our $S^2$Diff lies in the acquisition of conditional features and the denoising of saliency maps. For the former, we employ a cross-modal conditional generation module to interweave cross-modal features through frequency integration and implicit-explicit state space interaction, effectively achieving global conditional features. For the latter, we employ a context injection module to mitigate noise interference and to enhance object information with the conditional context. With the close cooperation of SAM-PAG and $S^2$Diff, our method outperforms relevant scribble-supervised methods and achieves competitive performance compared to fully-supervised methods on seven datasets. The code and results of our method are available at this https URL.

---


### 182. [RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048)

**<font color=#1a73e8>作者：</font>** Tianchen Deng, Zhiheng Feng, Wenhua Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Road surface mapping plays a crucial role in autonomous driving, supporting high-definition map generation, lane-level perception, and automatic road annotation. Recent mesh-based road surface reconstruction methods have shown promising results, but they still suffer from limited reconstruction quality and high optimization cost, especially in large-scale driving scenarios. To address these limitations, we propose ROADGS-T, a robust and efficient large-scale road surface mapping framework based on adaptive meshgrid Gaussian representation. Specifically, we model the road surface by placing 2D Gaussian surfels on a meshgrid, where each surfel explicitly stores color, semantic, and geometric information. Compared with conventional mesh-based representations and 3D Gaussian primitives, the proposed meshgrid Gaussian representation better matches the thin-surface property of roads while significantly reducing redundant primitives and overlap during optimization. To further improve representation efficiency and structural fidelity, we introduce a road-structure-aware adaptive meshgrid strategy, which allocates denser Gaussian surfels to geometrically or semantically complex regions, such as lane markings, road boundaries, and height discontinuities, while maintaining a compact representation in flat road areas. Moreover, instead of relying on a single nearest vehicle pose, we design a trajectory-consistency-guided pose-robust refinement strategy, which estimates local surface priors from multiple neighboring poses and adaptively weights pose-guided height regularization according to their geometric consistency.

---


### 183. [NFSA: Non-Forward Secure Aggregation with One Server via Two Layer Secret Sharing](https://arxiv.org/abs/2607.15052)

**<font color=#1a73e8>作者：</font>** Yufei Zhou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative model training while preserving privacy by keeping data local. However, the risk of sensitive data leakage through model updates necessitates the use of secure aggregation protocols. Existing server-based secure aggregation protocols typically require the server to forward sensitive data shared between users, which increases communication overhead and introduces potential security risks. In this work, we propose a novel secure aggregation protocol based on two-layer secret sharing to address these issues. By combining Shamir's Secret Sharing with 2-out-of-2 additive secret sharing using a Pseudo-Random Function (PRF), our protocol eliminates direct communication between users, thereby removing the need for the server to forward data. We further extend the protocol with Key-homomorphic PRF (KhPRF) to support high-dimensional data aggregation and apply it to FL, enabling one-shot secure aggregation with a single server and no intermediary data forwarding. To reduce user overhead, we design a new encoding method based on the Chinese Remainder Theorem for the almost KhPRF-based mask, reducing the number of KhPRF calls and mitigating the model update expansion issue after masking. Experimental results show that our scheme significantly outperforms existing methods in terms of auxiliary node overhead. For instance, when the number of users is 100, our scheme improves communication efficiency by nearly 100 times and reduces computational overhead by approximately 17\%. Moreover, user computation time can be reduced by 51\% to 75\% when the input length is $2^{18}$.

---


### 184. [Kernel weighted importance sampling for off-policy evaluation in contextual bandits](https://arxiv.org/abs/2607.15067)

**<font color=#1a73e8>作者：</font>** Joshua Spear, Matthieu Komorowski, Rebecca Pope 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article presents a novel estimator for performing off-policy evaluation using only offline data for contextual bandits. The proposed estimator, Kernel-WIS is demonstrated to be asymptotically consistent and to empirically outperform strong baselines (including vanilla weighted importance sampling), particularly under complex conditions including behaviour policy miss-specification. The benefit of Kernel-WIS is derived from combining the bounded property of vanilla weighted importance sampling with the linearity of vanilla importance sampling.

---


### 185. [An Introduction to Sparse Identification of Nonlinear Dynamics for Engineering Applications](https://arxiv.org/abs/2607.15077)

**<font color=#1a73e8>作者：</font>** Yao Cheng Li, Ana Larrañaga, Steven L. Brunton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many engineering problems involve phenomena whose governing equations are poorly characterized or only partially known. Surrogate modeling techniques such as neural networks can capture the behavior of these systems, but they typically demand large training datasets that are difficult to obtain in engineering contexts and yield models with limited physical interpretability. The Sparse Identification of Nonlinear Dynamics (SINDy) method addresses both limitations by performing sparse regression over libraries of candidate nonlinear terms, recovering interpretable governing equations from comparatively small datasets. Although SINDy has been demonstrated extensively on canonical benchmark systems, its application to practical engineering problems is less widely documented. This tutorial introduces the SINDy method and progressively builds toward its main extensions, from noise-robust weak-form and ensembling-based variants to constrained and parametrizable formulations. The paper and the accompanying tutorial (available at this https URL) is organized in three parts: the first introduces the standard SINDy algorithm and progressively extends it, inviting readers without prior knowledge to follow each step and adapt the methods to their own problems; the remaining two parts present detailed case studies on (1) the system identification of an unmanned aerial vehicle and (2) a chaotic thermosyphon heat exchanger. Through these examples, we aim to demonstrate that SINDy is simple to implement yet flexible enough to serve as a valuable identification tool for advanced engineering applications.

---


### 186. [Evaluating covariate balance for long time horizon Markov decision processes](https://arxiv.org/abs/2607.15080)

**<font color=#1a73e8>作者：</font>** Joshua Spear, Rebecca Pope, Neil J Sebire  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article explores the application of covariate balance diagnostics for detecting the presence of hidden confounding/model miss-specification in studies applying offline reinforcement learning (RL) to deriving optimal treatment recommendations. The results demonstrate that, either there is a high risk of bias within existing offline RL studies for treatment recommendations or, existing covariate balance metrics are not sufficient to assess such studies. Regardless, existing offline RL studies cannot be concluded as being statistically robust. The conclusions propose future research directions for obtaining more methodologically robust applications of offline RL to treatment recommendation problems.

---


### 187. [Towards Hierarchical Structure Understanding of Newspaper Images](https://arxiv.org/abs/2607.15082)

**<font color=#1a73e8>作者：</font>** William Mocaër, Solène Tarride, Thomas Constum 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding newspaper images remains a challenging task due to their complex, nested hierarchical structures and dense, heterogeneous layouts. In this paper, we explore two complementary approaches for newspaper structure understanding. First, we present a modular bottom-up pipeline that combines state-of-the-art open-source models: YOLO for layout detection, LayoutReader for reading order prediction, and a custom algorithm for article segmentation. This approach leverages existing robust components while maintaining flexibility and interpretability. Second, we introduce Tiramisu (Tiered Transformers for Hierarchical Structure Understanding), a novel end-to-end transformer-based architecture that explicitly models document hierarchy through an iterative tiered process. Tiramisu performs section and article separation, block localization, semantic categorization, and reading order prediction using highly parallelized attention mechanisms. Finally, we release Finlam La Liberté, a new dataset designed specifically for evaluating hierarchical information retrieval in historical newspapers. Experimental results demonstrate the effectiveness of both approaches in reconstructing complex newspaper hierarchies, with comparative analysis highlighting their respective strengths for scalable document digitization. The Tiramisu training code, including the synthetic newspaper generator, is available at this https URL.

---


### 188. [Quantifying Training Membership Information in the Hyperspherical Embedding Geometry of Face Recognition Models](https://arxiv.org/abs/2607.15084)

**<font color=#1a73e8>作者：</font>** Ünsal Öztürk, Sébastien Marcel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition models represent each face as an embedding vector on the unit hypersphere by clustering embeddings of the same identity while pushing different identities apart through angular-margin losses. Because these losses act only on training identities, non-member identities may form clusters with different geometric properties. In this paper, we quantify the magnitude of this difference and what training-time factors control it. We compute four statistics based on cluster geometry across 180 face recognition models in a factorial design over IResNet backbone size, loss head, training duration, and the number of training identities, and evaluate each configuration on nine benchmarks. Our results indicate that the number of training identities has the largest effect on member/non-member separability, while backbone and loss head contribute far less, and that, on a same-domain held-out reference, the geometric membership signal decreases monotonically as more identities are added to training. We provide an analysis of cross-domain (pose, age, quality, ethnicity) non-member benchmarks and report that these inflate the apparent membership signal. Finally, we fuse all four statistics with a learned classifier to reveal additional membership information beyond the best individual statistic.

---


### 189. [QuReC: All-in-One Image Restoration with Query-Specific Guidance and Local-Global Response Calibration](https://arxiv.org/abs/2607.15097)

**<font color=#1a73e8>作者：</font>** Shen Zhou, Jinghui Zhang, Wenbo Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> All-in-one image restoration aims to recover clean images degraded by multiple corruption types using a single unified model. Existing methods typically rely on image-level prompts or shared guidance to handle diverse degradations. However, such a paradigm becomes inadequate when degradations are spatially heterogeneous or even coexist in mixed forms within a single image. Yet spatially adaptive guidance alone is not sufficient, since accurate restoration also requires each spatial query to reliably aggregate complementary information from local neighborhoods and global contexts. To this end, we propose QuReC, a unified framework for all-in-one image restoration. QuReC consists of a Degradation-Guided Query Reconstruction Module (DQRM) and a Local-Global Response Calibration Module (LGRCM). Specifically, DQRM matches each spatial query against a degradation prototype space to reconstruct a query-specific degradation-aware representation, thereby providing fine-grained spatially adaptive restoration guidance. To further stabilize this query-wise matching process, we introduce a weakly supervised prototype matching learning strategy to improve optimization stability and degradation semantic consistency. Meanwhile, LGRCM performs local-global dual-branch aggregation and calibrates the aggregated responses with learnable priors, improving the reliability of feature aggregation and the coordination between local detail modeling and global context modeling. Extensive experiments demonstrate that QuReC achieves superior performance on multiple all-in-one image restoration benchmarks. The code is released at this https URL.

---


### 190. [Learning in Infinitesimal Non-Compositional Sketches](https://arxiv.org/abs/2607.15107)

**<font color=#1a73e8>作者：</font>** Sridhar Mahadevan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper develops a categorical framework -- Learning in Infinitesimal Non-Compositional Sketches (LINCS) -- as the repair of non-compositionality: failures of diagrams to factor through quotient sketches lifted to the tangent category setting. Machine learning problems are specified as sketches: graphs with commutativity conditions $\mathcal D$, limit cones $\mathcal L$, and colimit cocones $\mathcal K$, generalizing the usual scalarization of loss functions or vector space assumptions. Non-compositionality is defined purely as failure of a universal factorization problem, not as arithmetic error between the desired and actual predictions. Given a learning sketch $\mathbb S=(S,\mathcal D,\mathcal L,\mathcal K)$, whose underlying graph is $S$, and a model $D:J \rightarrow C$, the base defect is the obstruction to factorization $\mbox{Obs}(\mbox{Fact}_{\mathbb S}(D))$. The tangent lift applies the tangent functor $T$ to obtain $TD:J \rightarrow C$, and LINCS is defined as the obstruction $\mbox{Obs}(\mbox{Fact}_{\mathbb S}(TD))$ -- asking whether infinitesimal perturbations preserve the compositionality this http URL paper also introduces Tangent Learning Sketches, which are sketches equipped with Cockett-Cruttwell tangent structure. The paper defines the INC endofunctor, which iterates the tangent lift, producing a tower $D,TD,T^2D, \cdots$ of factorization problems. ML is thereby formulated as the search for a coalgebraic fixed point where successive tangent unfoldings stabilize ($\nu T_{\mbox{INC}}$). Using the Aczel--Mendler theorem, we prove existence of a final INC coalgebra whenever $T_{\mbox{INC}}$ admits a set-based class realization that creates its final carrier. A detailed experimental evaluation of LINCS is underway in a number of concrete ML settings, including deep learning, large language models, and reinforcement learning, and is described in companion papers.

---


### 191. [Automated Template-free Synthesis of Instruction-Centric Leakage Contracts for Black-Box CPUs](https://arxiv.org/abs/2607.15118)

**<font color=#1a73e8>作者：</font>** Elvira Moreno, Tiziano Marinaro, Ryan Williams 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Side-channel attacks pose a significant security threat for modern computing platforms, because they exploit subtle discrepancies in CPU behaviors to leak sensitive information. To model the information leaked by a CPU via microarchitectural side-channels, recent work proposed leakage contracts: an ISA-level security abstraction that provides the foundations for secure CPU programming. Unfortunately, due to the complexity of current microarchitectures, devising a leakage contract for a CPU requires extensive manual effort and thus modern CPUs lack dedicated leakage contracts.
We present a methodology to extract instruction-centric leakage contracts for major CPU architectures with minimal manual intervention. We implemented this technique in malcos, the first template-free tool that automates the synthesis of leakage contracts for black-box CPUs. We evaluate malcos on x86 and ARM CPUs, and show that the contracts it synthesizes are precise and sound with respect to all leaks observed during synthesis. Our results demonstrate that learning leakage contracts from black-box CPUs is feasible.

---


### 192. [DAPGNet: Dynamic Adaptive Physics-Guided Graph Diffusion Network for Hyperspectral Image Classification](https://arxiv.org/abs/2607.15128)

**<font color=#1a73e8>作者：</font>** Pengkun Wang, Weijia Cao, Ning Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral image (HSI) classification requires reliable pixel-relation modeling under spectral variability, mixed pixels, and heterogeneous boundaries. Existing graph-based HSI classifiers usually construct graph topology from spatial proximity, superpixel connectivity, or learned feature affinity. However, the spectral physical prior carried by contiguous bands has limited influence on topology estimation and message propagation. This paper presents DAPGNet, a dynamic adaptive physics-guided graph diffusion network that injects a structure-constrained physical prior into relation-level graph learning. DAPGNet first encodes contiguous spectral responses into node-wise multiscale physical-prior representations. A two-stage graph constructor then combines spectral-spatial affinity, physical-prior consistency, and spatial distance to form a physical-prior-aware sparse topology. During graph diffusion, learned edge weights are transformed into additive attention biases, while a physical gate performs node-wise and feature-wise interpolation between graph-aggregated features and projected physical-prior features. Cross-scale fusion integrates node states from different diffusion depths, and the network is optimized with main classification, auxiliary supervision, and second-order spectral smoothness regularization. Experiments on Indian Pines, WHU-Hi-LongKou, Houston2013, and Houston2018 show that DAPGNet achieves the best OA, AA, and Kappa among representative CNN-, Transformer-, Mamba-, and graph-based baselines. It improves AA over the strongest competing method by 3.64 to 7.31 percentage points across the four datasets. Ablation and sensitivity analyses further support the complementary effects of physical-prior extraction, prior-aware topology construction, physics-gated propagation, and spectral smoothness regularization.

---


### 193. [Ray-based phase error correction for miniaturized DOE projector-based FPP under single-directional hyperbolic projection](https://arxiv.org/abs/2607.15139)

**<font color=#1a73e8>作者：</font>** Seung-Jae Son, Yatong An, Jae-Sang Hyun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fringe Projection Profilometry (FPP) systems using miniaturized DOE pro-jectors often suffer from severe phase artifacts due to nonlinear projection characteristics and limited pattern controllability. We propose a ray-based phase error correction framework that models phase artifacts along projection rays from the projector pinhole, incorporating projector geometry without re-lying on image-domain processing or neighboring pixels. A projector pinhole estimation method based on a single-directional hyperbolic fringe pattern is introduced, through which projector geometry can be recovered without stereo calibration. In addition, a data-efficient strategy constructs the re-finement model from a single calibration pose. Experiments on miniaturized DOE projector-based FPP systems demonstrate significant improvements in reconstruction accuracy under nonlinear projection conditions, confirming the robustness and physical consistency of the proposed approach.

---


### 194. [Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents](https://arxiv.org/abs/2607.15143)

**<font color=#1a73e8>作者：</font>** Aadesh Bagmar, Pushkar Saraf  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI coding agents set up projects by reading documentation and installing the dependencies it lists, without verifying their names, sources, or known vulnerabilities. By editing only a README, requirements file, or Makefile, an attacker can redirect the agent to an untrusted registry, a known-vulnerable version, or a wrong-but-plausible name: documentation becomes a vector for code execution. We present the first systematic evaluation of package-install-time supply-chain attacks delivered through ordinary project-setup documentation across production coding-agent harnesses, probing frontier models on twelve scenarios in five attack classes, grounded in documented incidents. The same model catches an attack through one harness and installs it through another: install-time security rests on the harness-model combination, not the model alone. Agents catch blatant typosquats reliably, but plausible separator-confusion names (azurecore for azure-core) slip through, and how often depends on the harness-model pairing. Source-based attacks like registry redirection are missed almost everywhere. The source blind spot recurs on npm and Cargo, where nearly every model installs the untrusted dependency; name detection carries over less consistently across ecosystems. Security-oriented prompts recover part of the gap but only for the dimension they name; a deterministic pre-install check that verifies names, sources, and versions before any code runs closes most of it.

---


### 195. [On-Policy Delta Distillation](https://arxiv.org/abs/2607.15161)

**<font color=#1a73e8>作者：</font>** Byeongho Heo, Jaehui Hwang, Sangdoo Yun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation is an alternative post-training method in reinforcement learning that alleviates the constraints imposed by reward models by providing token-level supervision from a teacher model. Although on-policy distillation has been studied and applied across various settings, its fundamental design remains underexplored. In this paper, we introduce a new distillation reward, termed the delta signal, instead of directly imitating the teacher's output distribution. The delta signal is defined as the difference between the teacher model and its base model prior to instruction tuning for reasoning capability. It therefore captures the changes induced by reasoning tuning and provides a more direct signal for transferring reasoning capabilities. Using extensive empirical evidence, we show that the delta signal substantially improves on-policy distillation and refer to the new distillation method as On-Policy Delta Distillation (OPD$^2$). Experiments across mathematics, science, and code-reasoning benchmarks demonstrate that OPD$^2$ consistently outperforms conventional on-policy distillation, enabling reasoning LLMs to achieve strong performance with only a short post-training period. Code will be available at this https URL

---


### 196. [The Industrialization of Research ; On AI-Driven Science and Its Consequences](https://arxiv.org/abs/2607.15164)

**<font color=#1a73e8>作者：</font>** Emmanuel Jeannot  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is transforming scientific research - not merely as a more powerful instrument, but as an autonomous participant in the research cycle itself. This transition constitutes, in the most precise sense of the term, the industrialization of research: a shift from a craft model, in which knowledge, method, and judgment are embedded in the researcher, to a pipeline model, in which these steps are decomposed, automated, and supervised. The US Department of Energy's Genesis Mission is the most ambitious current instantiation of this shift, but the fundamental questions it raises extend far beyond any single program. This essay examines seven such questions: the erosion of the intergenerational transmission of scientific competence; the growing opacity of AI-generated theories; the collapse of peer evaluation under a flood of machine-generated output; the unproven capacity of AI for paradigm-shifting discovery; the capture of the scientific agenda by political and industrial actors; the compounding of systematic errors in closed-loop pipelines; and the structural bifurcation of the global research community into incommensurable tiers. These concerns do not constitute an argument against AI-driven science - whose demonstrated potential is real and significant. They constitute the conditions under which that potential can be responsibly pursued.

---


### 197. [MedFailBench: A Clinician-Built Open-Source Benchmark for Medical AI Safety Boundary Inspection](https://arxiv.org/abs/2607.15166)

**<font color=#1a73e8>作者：</font>** Goktug Ozkan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most medical AI benchmarks measure whether a model knows the correct answer. MedFailBench asks a different question: which safety boundary failed? We present a clinician-built synthetic benchmark and failure atlas that labels medical AI errors by severity (1--5) and safety gate type (missed urgent escalation, unsafe remote dosing, unsafe discharge reassurance, evidence fabrication, unsafe protocol execution, source support gap). The current public release (v0.2.1) contains 44 clinician-reviewed synthetic cases with severity annotations, a live HuggingFace leaderboard preview, a safety gate taxonomy, a clinical severity rubric, and an automated pipeline for archiving model-response screening runs. No patient data, clinical validation claims, or model rankings are included. MedFailBench is released under Apache-2.0 and CC-BY-4.0 and carries the Zenodo DOI https://doi.org/10.5281/zenodo.21205535.

---


### 198. [T^2MLR: Transformer with Temporal Middle-Layer Recurrence](https://arxiv.org/abs/2607.15178)

**<font color=#1a73e8>作者：</font>** Ziyang Cai, Xingyu Zhu, Yihe Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer reasoning is limited by autoregressive decoding, which repeat edly compresses rich hidden computation through token space and makes it difficult for intermediate reasoning states to persist across time. We in troduce Transformers with Temporal Middle-Layer Recurrence (T2MLR), a transformers-based latent reasoning architecture that fuses a cached middle layer representation from the previous token directly into an earlier layer of the current token position, enabling abstract intermediate computation to persist across decoding steps with little inference overhead. Across natural-language pretraining and multi-hop reasoning finetuning, T2MLR consistently outperforms data- and parameter-matched Transformer base lines. Moreover, applying recurrence to only a localized middle-layer block (as little as 20% of the network) often outperforms full-layer recurrence. Im portantly, T2MLR does not require pretraining from scratch: retrofitting the recurrent pathway into an existing pretrained 1.7B Transformer and briefly finetuning substantially improves math reasoning, lowering the barrier to practical adoption. These results suggest that effective latent reasoning in Transformers does not require looping over all layers as in previous works, but can instead emerge more strongly from targeted middle-layer recurrence.

---


### 199. [RTS Smoother-Guided Learning of Physics-Based Neural Differential Models](https://arxiv.org/abs/2607.15180)

**<font color=#1a73e8>作者：</font>** Ahmet Demirkaya, Georgios Stratis, Tales Imbiriba 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ordinary differential equations (ODEs) are widely used to model dynamical systems in physics, biology, neuroscience, and physiology, but in many applications some equations of the dynamics are unknown and only a subset of the state variables are measured. We propose a hybrid neural--physics framework in which the known components of the ODE are kept explicit and the missing components are represented by a neural network. The proposed method consists of two stages where we alternate between state and parameter estimation and iterate until a predetermined criterion is met. Specifically, in the first step, we treat the model parameters as being known and we infer the latent states from the available measurements using a Rauch--Tung--Striebel (RTS) smoother. In the second stage, we treat the smoothed trajectories as being known and use them to estimate the neural networks' parameters through backpropagation. We evaluate the method on benchmark systems spanning linear, nonlinear, and stiff dynamics under partial state observation. Across these settings, the proposed method learns missing ODE components from incomplete measurements while exploiting and retaining interpretable mechanistic structure and improving latent-state reconstruction and long-horizon prediction.

---


### 200. [Stigmergic Graph Memory: An Environment-Aware Approach for Many-to-Many Multi-Agent Pickup and Delivery](https://arxiv.org/abs/2607.15182)

**<font color=#1a73e8>作者：</font>** Aditya Dutta, Joon-Seok Kim  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Automated fulfillment warehouses must continuously assign and execute pickup-and-delivery work while avoiding congestion. In many-to-many Multi-Agent Pickup and Delivery (MAPD), a request specifies a stock-keeping unit rather than fixed endpoints, requiring the controller to select an agent, source, and destination before path planning. Existing graph-guidance methods primarily influence routing after goals are fixed, leaving endpoint instantiation uninformed by recent traffic. We introduce Stigmergic Graph Memory (SGM), a bounded, decaying memory layer that records recent execution signals on warehouse nodes and directed edges to rank feasible endpoints and route preferences without altering collision constraints or planner validity. Across paired request streams on five layouts, three load levels, and 25 seeds per condition, SGM outperforms two reconstructed many-to-many allocation baselines in all 15 map-load conditions, with paired throughput gains of 20.5-36.7%. These results show that recent execution memory can improve warehouse throughput by shaping which feasible goals enter the planner, not only how agents travel to already fixed goals.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-221](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
