# 📦 其他研究 | 2026年06月30日

> 本类共 **160** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-160](./part-04.md)

---

### 51. [Joint Transcription and Decryption of Images of Encrypted Handwritten Documents: A Comparison with the Traditional Pipeline](https://arxiv.org/abs/2606.27700)

**<font color=#1a73e8>作者：</font>** Marino Oliveros-Blanco, Lei Kang, Alicia Fornés 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Historical encrypted manuscripts present a challenging problem at the intersection of cryptology, linguistics, paleography, and computer vision. Current automatic decipherment approaches usually rely on a two-stage pipeline: transcription of cipher symbols from manuscript images, followed by decryption into plaintext. However, this design is sensitive to transcription errors, which propagate to the final output. We present Direct Image Decryption, an end-to-end approach that directly maps encrypted manuscript images to plaintext, bypassing the intermediate transcription stage. Using the Copiale cipher as a case study, we build a synthetic data generation pipeline to create large-scale cipher-like training data and compare the traditional pipeline with the proposed joint architecture. Results show that joint image-to-plaintext modeling is a promising alternative to traditional transcription-based pipelines.

---


### 52. [AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis](https://arxiv.org/abs/2606.27704)

**<font color=#1a73e8>作者：</font>** Robi Paul, Michael Zuzak  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> TinyML models deployed on edge devices are increasingly adopted in safety/security-critical applications, making them a prime target for adversarial example (AE) attacks where inputs are modified to cause misclassifications. However, existing AE detection methods either require white-box model access, which is often unavailable in licensed black-box deployments, or rely on input pre-processing stages that add non-trivial latency and resource overhead, often exceeding what mission-critical applications can afford on their inference path. To address these challenges, we propose AdvScan, a runtime power analysis-based methodology for AE detection that operates in a black-box scenario while inducing minimal latency. AdvScan is based on the observation that AEs produce anomalous neuron activations, which in turn generate distinctive power-consumption signatures. The algorithm initially constructs a baseline distribution of power signatures from known benign inputs; then, at runtime, it applies a one-sample t-test to determine whether a test input's power signature significantly deviates from this baseline, thereby detecting AEs. We evaluated AdvScan using three adversarial example generation algorithms: Fast Gradient Sign Method (FGSM), Projected Gradient Descent (PGD), and Carlini-Wagner (C&W), on three MLPerf Tiny benchmark models implemented on two target devices: the STM32F303RC (ARM Cortex-M4) and STM32L562RE (ARM Cortex-M33) microcontrollers. Across 318,400 total test inputs, AdvScan detects 99.984% of AEs with only 40 false negatives and zero false positives. These results demonstrate the viability of power-based AE detection for secure, accuracy-critical TinyML deployments in black-box environments.

---


### 53. [The Simulacrum: Decision-Theoretic Pretraining for Near-Optimal Time-Series Forecasting and Inference](https://arxiv.org/abs/2606.27711)

**<font color=#1a73e8>作者：</font>** Pablo Montero-Manso, Marcel Scharth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a neural network-based framework for learning time series estimators through a process we term decision-theoretic pretraining. Analysts specify a generative world, a distribution over data-generating processes, and a target decision objective. A neural network trained on stratified simulations from this world approximates the corresponding optimal decision rule, yielding a neural estimator that provides forecasts, parameter estimates, predictive intervals, or model-selection for zero-shot inference on previously unseen time series.
The joint specification of the generative world and objective enables the estimators to directly approximate process-level, finite-sample properties: near-optimal risk, bias control, minimax performance, and uniform calibration. Our experiments demonstrate that these neural estimators can outperform traditional baselines such as maximum likelihood estimation and model selection via AICc, for the same model structural model classes. Furthermore, even when trained purely on simulations of structural models, they achieve competitive or state-of-the-art forecasting accuracy on major real-world benchmarks, compared with statistical, neural or large pre-trained models.
We illustrate the framework by addressing two longstanding challenges: finite-sample bias and miscalibration in AR(p) models, and the forecast combination puzzle. These applications highlight the approach's main advantage: its ability to approximate solutions to analytically intractable or computationally prohibitive time series problems, including complex structural equations or optimality criteria. Ultimately, by enabling explicit control over decision-theoretic trade-offs, the framework equips analysts with highly efficient estimation tools tailored to their specific analytical needs.

---


### 54. [Do Speech Emphasis Models Generalize across Languages and Emotions?](https://arxiv.org/abs/2606.27717)

**<font color=#1a73e8>作者：</font>** Megan Wei, Deepali Aneja, Jiaqi Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prosodic emphasis varies across languages, emotions, and speaking styles, yet existing emphasis detection models are largely trained and evaluated on monolingual neutral read speech. We introduce MMEE (Multilingual Multi-Emotion Emphasis), a corpus of 10,000 professionally recorded expressive utterances (14.13 hours) across 7 languages and 34 emotion/style categories, with three-level perceptual labels (10 annotations per sample). We benchmark two state-of-the-art architectures under monolingual, cross-lingual, multilingual, cross-emotion, cross-dataset, and data-scale settings. Monolingual models show limited zero-shot transfer, degrading across typologically distant languages, while multilingual training substantially improves robustness. Models transfer robustly between high- and low-arousal emotions; bidirectional transfer between synthetic and perceptual benchmarks suggests shared prosodic structure; and performance stays robust even at smaller training scales.

---


### 55. [MASS: Motion-Aligned Selective Scan for Refinement in Flow-Based Video Frame Interpolation](https://arxiv.org/abs/2606.27718)

**<font color=#1a73e8>作者：</font>** Jun-Sang Yoo, Seung-Won Jung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video frame interpolation (VFI) remains a challenging task, particularly when dealing with large, non-linear motions and complex occlusions. While flow-based methods are prevalent, they often struggle with ambiguous correspondences. Recent VFI methods based on selective State Space Models (SSMs) are still limited by static grid-based scanning that misaligns with physical motion. In this paper, we propose Motion-Aligned Selective Scan (MASS), a novel framework that reformulates feature scanning from static spatial grids to dynamic motion trajectories. MASS builds a feature sequence along each pixel's flow-guided trajectory and aggregates it with an SSM. Specifically, we introduce a learnable non-linear path integration to approximate complex curved trajectories via residual velocity updates, and a velocity-aware SSM that dynamically adjusts the sampling budget and step size based on motion magnitude. This adaptive strategy allocates denser sampling to fast-motion regions while keeping static regions efficient. Furthermore, the aggregated states guide a refinement module to rectify intermediate flows and masks in an end-to-end manner. Extensive experiments indicate that MASS achieves highly competitive overall performance on standard benchmarks, establishing state-of-the-art results particularly in challenging scenarios with large displacements and complex dynamics.

---


### 56. [Scene and Human in One World: Reconstruction in a Feedforward Pass](https://arxiv.org/abs/2606.27720)

**<font color=#1a73e8>作者：</font>** Boao Shi, Qiao Feng, Yiming Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing humans in dynamic scenes from moving monocular cameras remains challenging due to scale ambiguity, human-scene misalignment, and occlusion interference. Rather than treating human mesh recovery and scene reconstruction as separate tasks, we believe that accurate human-scene reconstruction requires the two tasks to mutually inform each other: parametric human models offer semantic structure and metric-scale priors, while scene geometry provides spatial context for human localization and alignment. Built on this insight, we introduce SHOW, a mask-promptable human mesh recovery framework that couples feed-forward 3D scene reconstruction with Human Mesh Recovery in a unified metric space. SHOW injects human semantics and scale priors from parametric human models into normalized point-map prediction, enabling metric-scale scene reconstruction from inherently scale-ambiguous monocular input. In turn, the recovered scene geometry constrains human mesh estimation, encouraging spatially consistent human placement and improved human-scene alignment. To handle complex multi-person and cluttered scenes, SHOW further incorporates a promptable masking mechanism that enables flexible target-human selection while suppressing background distractions and occlusion interference. Through joint training, the model learns both human-aware geometric features and geometry-constrained human features, producing aligned metric-scale reconstructions from monocular human-centric videos. Extensive experiments demonstrate that SHOW improves metric-scale consistency, human-scene alignment, and reconstruction accuracy under challenging camera motion, occlusion, and cluttered backgrounds.

---


### 57. [Learning to Reason with Curriculum II: Compositional Generalization](https://arxiv.org/abs/2606.27721)

**<font color=#1a73e8>作者：</font>** Nived Rajaraman, Audrey Huang, Miroslav Dudik 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compositional generalization, the ability to solve complex problems by combining solutions to simpler sub-problems, is a fundamental capability of both natural and artificial intelligence, and a key mechanism underlying chain-of-thought reasoning. However, the theoretical underpinnings of compositional generalization remain poorly understood: when and why does decomposing a problem into parts yield more efficient learning than solving it directly? We study this question through the canonical problem of learning to simulate semiautomata (predicting the outcome of $T$ steps of sequential computation), a model that captures state tracking, regular language recognition, and modular arithmetic. We show that an autocurriculum-based approach building on Part I of this series, recursively decomposing longer sequences into shorter sub-problems, learning to solve them, and composing the solutions, achieves dramatically better statistical complexity than direct methods. (i) For a setting inspired by supervised fine-tuning (SFT) where the learner receives interactive feedback on intermediate states of the computation, curriculum facilitates learning from only $2^{\mathcal{O}(\sqrt{\log T})}$ tokens of supervision; i.e., subpolynomial in the sequence length $T$, overcoming the $\Omega(T)$ token barrier required by direct simulation. (ii) For a setting inspired by reinforcement learning with verifiable rewards (RLVR), where the learner improves a pre-trained reference model using an outcome verifier, we show that curriculum reduces the requirement on the reference model from coverage at the full sequence length $T$ to coverage at a shorter block length $B \ll T$, an exponentially weaker condition.

---


### 58. [Learning 1-Bit LiDAR-based Localization with Auxiliary Objective](https://arxiv.org/abs/2606.27729)

**<font color=#1a73e8>作者：</font>** Kaijie Yin, Zhiyuan Zhang, Tian Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 6-DoF LiDAR-based localization is a fundamental capability for autonomous systems operating in large-scale outdoor environments. Many deep-learning-based localization methods have achieved promising performance so far. However, as one of the always-on modules competing for limited on-board computational resources, the localization module is expected to consume only a small portion of the overall compute budget. Most existing learning-based methods are still too heavy for this purpose. In contrast, binary neural networks (BNNs) offer an appealing solution, but the 1-bit compression causes severe information loss and performance drop. In this paper, we address this challenge by proposing Binarized LiDAR-based Localization (BiLoc), the first binary neural network framework for 6-DoF LiDAR localization. Specifically, we reinterpret the training of BNNs from the perspective of the information-bottleneck principle, aiming at retaining minimal yet sufficient representations for pose estimation while suppressing redundant variations. And we introduce an auxiliary objective that adaptively regulates information retention in the binary encoder, effectively mitigating the information loss caused by binarization. This auxiliary objective provides additional optimization signals that compensate for the limited representational capacity and the gradient mismatch inherent in BNNs. Extensive experiments on large-scale outdoor LiDAR datasets demonstrate that BiLoc establishes a new state of the art for LiDAR localization with BNNs.

---


### 59. [ToE: A Hierarchical and Explainable Claim Verification Framework with Dynamic Multi-source Evidence Retrieval and Aggregation](https://arxiv.org/abs/2606.27736)

**<font color=#1a73e8>作者：</font>** Zhaoqi Wang, Zijian Zhang, Kun Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid spread of fake news poses increasing threats to information ecosystems, especially as AI-generated misinformation under Generative Engine Optimization (GEO) poisoning allows adversarially crafted content to be systematically surfaced by retrieval systems, contaminating LLM reasoning. In this paper, we propose Tree of Evidence (ToE), a hierarchical evidence reasoning framework for automated fact-checking that models each claim as a dynamically expanding argument tree. ToE integrates a reinforcement learning-driven multi-source retrieval agent, an evidence evaluation agent, and an argument tree aggregation algorithm to iteratively decompose, retrieve, and verify claims through an explainable evidence chain. We further provide a theoretical analysis of the retrieval process, deriving a formal error bound that guarantees the learned policy converges to a neighborhood of the information-theoretically optimal policy. Experiments across multiple datasets and backbone LLMs demonstrate that ToE achieves improvements ranging from 4 to 24 percentage points over competitive baselines, with particularly pronounced gains on adversarially poisoned inputs.

---


### 60. [Reduction of Probabilistic Chemical Reaction Networks](https://arxiv.org/abs/2606.27737)

**<font color=#1a73e8>作者：</font>** Mauricio Montes, Gregoire Sergeant-Perthuis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Programming adaptive behaviors at the cellular level is a long-standing goal that raises the question of how probabilistic computation can be implemented in biochemical systems. Chemical reaction networks (CRNs) provide such a substrate and have been shown to realize probabilistic models, including hidden Markov models and factor graphs, with dynamics reproducing Bayesian inference and belief propagation. However, encoding these algorithms typically requires prohibitively large reaction networks, and classical CRN reduction techniques do not directly apply. By recovering the factor graph structure encoded in Napp--Adams-compiled CRNs, we transport recent factor-graph reduction results to their chemical implementations, obtaining significantly smaller CRNs while preserving the belief-propagation fixed points on surviving variables.

---


### 61. [HandMade: Spatial Prompting for Generative 3D Creation with Part-Labeled VR Sketches](https://arxiv.org/abs/2606.27738)

**<font color=#1a73e8>作者：</font>** Jialin Huang, Rana Hanocka, Ariel Shamir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Text-to-3D generation lowers the barrier to 3D content creation, but text alone is a weak interface for specifying spatial intent: where parts should be placed, how they relate, and how an object should be organized in 3D. We present HandMade, a workflow that combines VR 3D sketching and language for open-domain 3D asset generation. HandMade treats coarse, part-labeled 3D sketches not as incomplete geometry to reconstruct directly, but as spatial prompts for existing generative models. It converts segmented VR strokes into multi-view part guidance and structured prompts, allowing users to specify object layout and part relationships through 3D sketching while using language for identity, material, style, and local details. A technical evaluation shows that HandMade better preserves user-authored spatial scaffolds than text-only and sketch-based baselines on 20 varied examples. A user study with eight participants characterizes how users make use of 3D sketching for spatial layout and language for identity, materials, and details across initial authoring and subsequent revision. HandMade contributes an interaction paradigm and interface-to-generation pipeline for spatially guided 3D creation.

---


### 62. [The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment](https://arxiv.org/abs/2606.27739)

**<font color=#1a73e8>作者：</font>** Tianyu Jia, Yue Fang, Hongxin Ding 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Process reward models (PRMs) enhance the reasoning capabilities of large language models (LLMs) by providing fine-grained feedback, yet training PRMs typically requires expensive stepwise annotations. Outcome-supervised PRMs offer a scalable alternative by learning from final-answer correctness alone, but this introduces a fundamental *credit assignment* challenge, i.e., attributing outcomes to responsible reasoning steps. Existing approaches rely on either uniform or causal assignment, both of which fail to anchor credit in step correctness and thus hinder process error identification.
In this work, we propose Outcome-Supervised Process Reward Modeling via **L**earnable **C**redit **A**ssignment (**LCA**), an outcome-supervised PRM framework that jointly learns credit assignment and reward modeling under the principle of *Weakest Link Assignment: a reasoning chain is as strong as its weakest link*. To address mutual dependence between credit assignment and reward modeling, we formalize outcome-supervised PRM as a Multiple Instance Learning (MIL) problem and introduce Softmax-Weighted-Sum (SWS) pooling, an MIL pooling technique tailored for strong dependence and redundancy among reasoning states. We prove Bayes consistency of our algorithm under mild assumptions. Extensive experiments demonstrate that **LCA** consistently outperforms state-of-the-art outcome-supervised PRMs across multiple tasks and backbones. Code is available at this https URL.

---


### 63. [KG2Cypher: Data-Centric Pipeline for Building Enterprise Text-to-Cypher Systems](https://arxiv.org/abs/2606.27742)

**<font color=#1a73e8>作者：</font>** Minjun Choi, Yerin Kim, Junghyuk Seo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise Knowledge Graphs (KGs) are increasingly used for internal search, analytics, and question answering, but building natural-language interfaces for private enterprise graphs remains costly. We present KG2Cypher, a data-centric pipeline for building enterprise text-to-Cypher systems from existing KGs. KG2Cypher first constructs an executable Cypher query from observed graph facts and then uses LLMs to generate its associated natural-language question. The resulting Text-Cypher pairs are validated with an LLM judge and human validation, and are converted into candidate-aware SFT data. The trained generator is served with class-conditioned schema prompting, entity retrieval, and LoRA-based inference. We evaluate KG2Cypher in Korean enterprise settings, where short search-style queries and schema paraphrases make language grounding difficult. LoRA SFT improves execution-result F1 from 0.806 to 0.950 on broadcast-program queries and from 0.70 to 0.92 on company queries. In an 11-class setting, KG2Cypher achieves 95.2% exact match, 99.9% execution rate, and 0.964 execution-result F1.

---


### 64. [Flexformer: Flexible Linear Transformer with Learnable Attention Kernel](https://arxiv.org/abs/2606.27748)

**<font color=#1a73e8>作者：</font>** Haoran Zhang, Feng Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer models rely on attention mechanism to capture long-range dependencies but suffer from quadratic complexity, limiting their scalability to long sequences. Kernel-based linear attention reduces this complexity but typically relies on fixed or weakly learnable kernels, restricting expressiveness and performance. In this work, we propose Flexformer, a flexible linear Transformer that learns attention kernels in a fully data-driven manner. Flexformer builds on random Fourier feature-based linear attention and treats spectral frequencies as trainable parameters, enabling the model to learn a broad family of attention kernels.
We develop both stationary and nonstationary variants, with the latter offering strictly greater expressiveness.
Extensive experiments on language modeling and sequence classification demonstrate that Flexformer consistently outperforms baselines. Moreover, Flexformer can be effectively distilled from pretrained Transformers to recover softmax attention and exhibits strong kernel transferability across domains, achieving both high efficiency and competitive performance on long-sequence tasks.

---


### 65. [PerturbCellRL: Verifier-Guided Reinforcement Learning for Single-Cell Perturbation Prediction](https://arxiv.org/abs/2606.27752)

**<font color=#1a73e8>作者：</font>** Dongxia Wu, Mingyu Li, Yuhui Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-cell perturbation models can reduce costly wet-lab screening by predicting how cells respond transcriptionally to interventions. While recent generative models improve population-level prediction, individual generated cells are not explicitly checked for biological consistency. We introduce PerturbCellRL, a reinforcement learning (RL) framework that post-trains a pretrained single-cell transcriptomic generator using a suite of cell-level verifiers as rewards. These verifiers define four rewards: Pearson top-k similarity, RMSE top-k proximity, DE Spearman, and Pathway activity. The Pathway activity verifier rewards cells whose pathway responses match known perturbation biology. We evaluate PerturbCellRL on multiple genetic and chemical perturbation benchmarks. Across these benchmarks, PerturbCellRL improves over the pretrained flow-matching generator on reward-aligned evaluation metrics and a held-out evaluation metric. Moreover, PerturbCellRL remains competitive with state-of-the-art methods on population-level metrics. Together, these results frame trustworthy single-cell prediction as verifier-guided generative alignment, moving beyond matching expression distributions toward predictions whose single-cell perturbation effects are explicitly checked for biological consistency.

---


### 66. [Layerwise Progressive Freezing: A Training Scaffold for Depth-Scalable Binary Networks](https://arxiv.org/abs/2606.27759)

**<font color=#1a73e8>作者：</font>** Evan Gibson Smith, Bashima Islam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training binary neural networks (BNNs) from scratch is dominated by the straight-through estimator (STE), whose forward/backward mismatch produces severe accuracy degradation as networks deepen. We study an orthogonal axis: when and where binarization is enforced during training. We introduce StoMPP (Stochastic Masked Partial Progressive Binarization), which gradually replaces clipped weights and activations with their hard binary counterparts layer by layer from input to output, using stochastic partial masks with soft refresh. StoMPP delivers two complementary benefits. As a standalone training rule, it provides a fully STE-free procedure that improves over vanilla STE with gains that grow with depth (ResNet-50 BNN: +18.0/+13.5/+3.8 on CIFAR-10/100/ImageNet), and the pattern holds across ResNet-18/34/50, MobileNetV2, and BERT fine-tuning. Composed with surrogate gradients by applying STE only to frozen entries, it reaches +27.1/+19.8/+17.7 over vanilla STE on the same setting. Underlying both regimes is a single mechanistic finding: progression order is decisive. Forward layerwise progression prevents depth collapse, reverse progression collapses to near-chance, and binary-weight networks (without binary activations) are insensitive to order. We trace this asymmetry to activation-induced gradient blockades: a committed binary activation severs gradient flow upstream, and ordering controls when these blockades form. To isolate the progression's contribution from any benefit conferred by STE, we conduct all ablations in the STE-free regime; the resulting characterization (schedule, refresh, ordering, dynamics) thus reflects the progression itself rather than its interaction with surrogate gradients.

---


### 67. [PixelU: A U-Shaped Transformer for Efficient End-to-End Pixel Diffusion](https://arxiv.org/abs/2606.27760)

**<font color=#1a73e8>作者：</font>** Zipeng Guo, Lichen Ma, Yu He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end pixel-space diffusion models bypass the lossy compression of Latent Diffusion Models (LDMs) but struggle to jointly model low-frequency semantics and high-frequency signals in high-dimensional space. Existing works heavily rely on complex pixel decoders to alleviate this issue. In this paper, we challenge this trend by revealing that these decoders primarily compensate for the optimization difficulties inherent to velocity prediction ($v$-prediction). Under the clean data paradigm ($x$-prediction), they are redundant. Motivated by this insight, we advocate for simplicity over complexity and introduce PixelU, a minimalist, single-stage U-shaped Diffusion Transformer tailored for pixel space. PixelU abandons auxiliary decoders in favor of zero-cost skip connections, which provide an "information highway" that directly routes uncorrupted high-frequency spatial details from shallow to deep layers. To further enable the backbone to focus exclusively on modeling low-frequency semantics, we introduce a constant-channel spatial down-sampling mechanism as a natural low-pass filter, which compresses deep features into a compact, low-frequency semantic manifold. Extensive experiments demonstrate that this decoupling of frequencies could outperform the strong baseline (JiT-G) with only about 1/3 of its computation cost. On ImageNet 256$\times$256 and 512$\times$512, PixelU achieves FID of 1.63 and 1.92 respectively, surpassing recent pixel-space methods and establishing a simple yet powerful new paradigm for end-to-end diffusion models.

---


### 68. [RS-Diffuser: Risk-Sensitive Diffusion Planning with Distributional Value Guidance](https://arxiv.org/abs/2606.27766)

**<font color=#1a73e8>作者：</font>** Shiqiang Gong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning enables policy learning from fixed datasets without additional environment interaction, making it appealing for safety-critical applications where online exploration is costly or unsafe. Diffusion-based decision-making methods have recently achieved strong performance in offline RL by modeling rich, multimodal trajectory distributions. However, existing diffusion planners are typically risk-neutral and therefore may overlook rare but catastrophic outcomes that are crucial in real-world deployment. In this work, we propose RS-Diffuser, a risk-sensitive offline diffusion planning framework that combines diffusion-based trajectory generation with distributional value critics. RS-Diffuser learns a diffusion planner over future state trajectories, a separate inverse dynamics model for action decoding, and a Monte Carlo distributional critic that estimates the full return distribution of candidate plans through quantile regression. At sampling time, we incorporate a risk-sensitive guidance signal into the denoising process, using gradients computed from tail-aware objectives such as Conditional Value at Risk to steer generation toward desired risk profiles. As a result, a single trained model can flexibly produce risk-averse, risk-neutral, or risk-seeking behaviors by changing only the inference-time risk parameter. Extensive experiments on risk-sensitive D4RL and risky robot navigation benchmarks demonstrate that RS-Diffuser achieves state-of-the-art performance, improving both overall return and worst-case robustness while reducing safety violations.

---


### 69. [Difference of Convex Programming in the Wasserstein Space with Applications to MMD Optimization](https://arxiv.org/abs/2606.27767)

**<font color=#1a73e8>作者：</font>** Clément Bonet, Pierre-Cyril Aubin-Frankowski, Youssef Mroueh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing functionals over the space of probability measures is now ubiquitous in machine learning. A widely used approach is to perform the optimization directly over the Wasserstein space, but many objective functionals of practical interest are non-convex along Wasserstein geodesics, making the analysis of standard first-order methods challenging. In this work, we study a class of objectives over the Wasserstein space that admit a difference-of-convex (DC) decomposition and we lift the classical convex-concave procedure (CCCP) to this setting. Under smoothness and strong convexity assumptions on the convex components of the decomposition, we prove almost stationarity along the iterates of the resulting algorithm. Our main focus is on the Maximum Mean Discrepancy (MMD) and the Energy Distance (ED) functionals, for which we develop explicit Wasserstein DC decompositions, and establish local convergence of the scheme under mild assumptions. Empirically, we show that well-chosen DC decompositions yield faster and more stable convergence than Wasserstein gradient descent on these MMD objectives.

---


### 70. [An Embedded Real-Time License Plate Recognition System for Complex Traffic Scenes](https://arxiv.org/abs/2606.27772)

**<font color=#1a73e8>作者：</font>** Anuki Pasqual, Dulan Lokugeegana, Manimohan Thiriloganathan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vehicle license plate recognition is an integral component of intelligent transportation systems. In this work, we present an embedded real-time license plate recognition system customized for developing countries. We address the challenge of handling complex, unstructured traffic scenes with diverse vehicle types while implementing the system on an embedded platform for low-cost deployment. Our method consists of license plate detection on a multi-vehicle image, followed by character recognition on the detected license plates. Both steps use lightweight convolutional neural networks to balance accuracy and efficiency. We also introduce the SL-LPR dataset of Sri Lankan road images, which contains a variety of vehicle types and traffic conditions typically seen in developing countries. On this dataset, the license plate detection and character recognition models achieved 93.6% mAP and 87.88% accuracy, respectively, and were competitive against larger models on several public datasets. To achieve real-time performance in a resource-constrained embedded environment, we applied low-bitwidth quantization using the Brevitas library and implemented FPGA acceleration for the models using the FINN framework. The end-to-end system can operate at 11.5~FPS when implemented on the Xilinx Kria KV260 platform. These results demonstrate that our system is effective for real-time license plate recognition on an embedded device, even in complex traffic scenarios. The SL-LPR dataset is available for research use at: this https URL.

---


### 71. [ModaFlow: Modality-Aware Flow Matching for High-Fidelity Virtual Try-On](https://arxiv.org/abs/2606.27773)

**<font color=#1a73e8>作者：</font>** Xiangyu Sai, Meysam Madadi, Sergio Escalera 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-based virtual try-on has emerged as a compelling task in e-commerce and augmented reality, yet existing methods struggle to simultaneously preserve fine garment semantics and adapt to diverse person body geometries under large clothing-body deformations. We present ModaFlow, a modality-aware flow-matching based framework for high-fidelity virtual try-on that achieves precise alignment between textual descriptions and garment appearance. Unlike prior methods that treat multimodal conditions uniformly, ModaFlow introduces a modality-aware guidance scheme: visual garment embeddings extracted by a pretrained image prompt adapter provide deterministic, persistent structural guidance, while textual embeddings generated from garment descriptions are controlled via classifier-free guidance (CFG) with adaptive scaling and zero-initialized velocity. To further enhance flow field accuracy, we propose two regularization losses, cosine similarity and perceptual flow discrimination, that jointly improve directional consistency and perceptual realism of the velocity field. Additionally, a mask manipulation strategy stochastically samples among box, transparent, and relaxed masks during training, simulating diverse occlusion scenarios and enabling robust inference under unpaired settings where only a box mask is available. Experiments show that ModaFlow achieves state-of-the-art results in both qualitative and quantitative evaluations, reducing FID by approximately 30% on paired and 20% on unpaired benchmarks.

---


### 72. [TRUST: Efficient Abdominal Trauma Recognition via Image-to-Ultrasound-Video Transfer Learning](https://arxiv.org/abs/2606.27777)

**<font color=#1a73e8>作者：</font>** Enguang Wang, Hao Zhou, Shuo Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Abdominal ultrasound is indispensable for rapid, noninvasive trauma triage. However, interpreting the subtle dynamic cues embedded in continuous scanning is time-intensive and operator-dependent. Parameter-Efficient Image-to-Video Transfer Learning (PEIVTL), which efficiently adapts pre-trained image models to the video domain, notably through visual-textual alignment, offers a promising paradigm for ultrasound video analysis. Nevertheless, substantial spatiotemporal and semantic variations arising from physician-dependent scanning practices continue to limit the effectiveness and generalizability of this framework. We propose TRUST, a scan-aware PEIVTL framework that explicitly models fine-grained spatiotemporal variations to enable reliable ultrasound video understanding. First, we introduce a Cross-Frequency Collaborative Adapter (CFCA) that establishes mutual constraints between low- and high-frequency components, enhancing discriminative spatial feature extraction under heavy speckle corruption. Second, we design a Multi-Granularity Motion-Aware (MGMA) module that integrates local temporal convolutions with motion-prior-guided global self-attention, jointly capturing stable intra-view patterns and abrupt inter-view transitions to characterize complex scanning dynamics. Third, a Visual Query Semantic Aggregation (VQSA) module dynamically generates text prototypes conditioned on visual features, enabling adaptive visual-textual alignment robust to intra-class variability under diverse scanning conditions. Experiments on in-house ultrasound trauma datasets demonstrate that TRUST outperforms state-of-the-art methods by 9.63% with superior computational efficiency.

---


### 73. [MindFlow: Harmonizing Cognitive Semantics and Acoustic Dynamics for Facial Animation Generation in Dyadic Conversations](https://arxiv.org/abs/2606.27779)

**<font color=#1a73e8>作者：</font>** Hejia Chen, Haoxian Zhang, Xu He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating lifelike facial animation for dyadic conversations requires reconciling high-level cognitive intent with precise low-level motor reflexes, yet existing methods fall short in the semantic understanding of dialogue context and in precise dynamic control. In this paper, we propose MindFlow, a dual-pathway generative framework inspired by the Ventral-Dorsal pathway model in neuroscience, which decouples generation into two collaborative streams, thereby harmonizing deep semantic reasoning with fine-grained control. In the Ventral module, we transform the conventional Sentence-Action approach into a novel Chunk-State approach that models raw acoustic streams as a context-aware, evolving emotional state chain, capturing subtle paralinguistic nuances and mid-utterance emotional shifts missed by sentence-level modeling. The Dorsal module features a conditional autoregressive flow matching network for high-fidelity facial motion, driven by high-frequency acoustic cues and modulated by emotion states, plus a Selective Acoustic Injector for adaptive audio gating to ensure robustness in talking-and-listening dynamics without interference. Extensive experiments demonstrate that MindFlow achieves superior semantic appropriateness and motion naturalness compared to state-of-the-art baselines.

---


### 74. [Improving Adversarial Robustness via Activation Amplification and Attenuation](https://arxiv.org/abs/2606.27784)

**<font color=#1a73e8>作者：</font>** Taïga Gonçalves, Yongsong Huang, Tomo Miyazaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The existence of adversarial attacks is often attributed to the presence of non-robust features in neural networks. While prior defenses reduce their impact via pruning, masking, or feature recalibration, we instead propose to jointly learn to amplify and attenuate these signals through a simple activation scaling mechanism. To this end, we introduce Activation Amplification and Attenuation (A3), a lightweight plug-in module that enhances adversarial robustness with minimal modifications of the activations. A3 dynamically rescales the activations using a learnable mask and a scaling factor derived from the original activation magnitudes. The influence of adversarial perturbations can be amplified or attenuated using the same learnable parameters by simply flipping the sign of the scaling operation. The amplified signals serve as negative references to construct novel contrastive and ranking loss functions. Experimental analysis shows that learning to degrade the predictions in amplification mode simultaneously improves adversarial robustness in attenuation mode. Moreover, A3 relies on only a small number of learnable parameters, with most of its behavior being determined by the scaling mechanism rather than additional network capacity. Extensive experiments demonstrate that integrating A3 into different backbones, datasets, and training methods consistently improves adversarial robustness while introducing negligible computational and memory overhead compared to existing plug-in modules. Code is available at: this https URL.

---


### 75. [NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation](https://arxiv.org/abs/2606.27791)

**<font color=#1a73e8>作者：</font>** Qiong Tang, Xiangkun Hu, Xiangyang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hybrid attention models that mix full and sliding-window attention across layers offer a promising approach to efficient long-context inference, but the critical question of \emph{which layers} should retain full attention remains unsolved. Existing methods use either fixed periodic patterns or attention-based heuristics that may not capture what matters for downstream accuracy. We propose NLL-guided layer selection, a training-free method that directly measures each layer's importance by computing the negative log-likelihood degradation on answer tokens when that layer uses sliding-window instead of full attention. On LongMemEval with Qwen3-4B, our method achieves 64.6\% accuracy using only 1/4 full-attention layers, matching the 1/2-FA periodic baseline (65.0\%) while halving the computational budget. NLL-guided selection outperforms the SWAA-reported periodic 1/4-FA baseline by 10.4 percentage points and a matched LightTransfer-style baseline by 26.4 percentage points. De-confounding analysis shows the signal is consistent with long-range attention needs rather than generic layer sensitivity. The method requires only $\sim$15 minutes of one-time calibration, advancing the efficiency-accuracy Pareto frontier for long-context LLM deployment.

---


### 76. [Position Bias Correction is Insufficient for One-Pass Attention Sorting](https://arxiv.org/abs/2606.27793)

**<font color=#1a73e8>作者：</font>** Qiong Tang, Xiangkun Hu, Xiangyang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context language models suffer from position bias, where information in middle positions is underutilized. Attention Sorting addresses this by iteratively reordering documents based on attention patterns, but its multiple sort-and-generate cycles increase deployment cost. We hypothesize that position bias is the primary bottleneck and propose Debiased One-Pass Attention Sorting, which estimates a per-prompt position-bias curve from the low-attention majority of documents and uses it to correct raw attention scores (via subtraction or division) to enable single-pass sorting. Our experiments on two models refute this hypothesis in the tested setting: on LLaMA-2-7B-32K-Instruct, debiasing produces identical results to uncalibrated single-pass sorting (94.83\% containment accuracy), while on YaRN-Llama-2-7b-64k, debiasing improves accuracy by 8.67 percentage points but remains 14.84pp behind iterative sorting, closing only 37\% of the gap. These results suggest that position-bias correction is insufficient to match iterative sorting, and that repeated reordering provides additional benefits beyond bias correction.

---


### 77. [Text as Illumination: Spatial Contrastive Retinex Learning for Language-guided Medical Image Segmentation](https://arxiv.org/abs/2606.27794)

**<font color=#1a73e8>作者：</font>** Jian Shi, Cheng Zhen, Pingping Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-guided Medical Image Segmentation (LMIS) has shown great potential to improve the delineation of anatomical structures and lesions by integrating clinical textual information. Existing methods generally rely on either implicit interaction between textual and visual features or auxiliary coarse-grained supervision for cross-modal alignment. However, these methods lack explicit and fine-grained constraints to ensure semantic consistency, causing a mismatch between language and the segmentation outputs. To address this issue, we propose Text-as-Illumination Retinex Network (TIRNet), a novel Retinex-inspired framework that treats text embeddings as semantic illumination for feature modulation, thereby improving semantic consistency in LMIS. TIRNet introduces two key blocks integrated at each decoder stage: (1) the Retinex-inspired Text Modulation Block (RTMB), which employs positive and negative illumination maps to enhance text-relevant foreground features and suppress background interference; and (2) the Consistent Detail Compensation Block (CDCB), which selectively recovers high-frequency details via a consistency-gated mechanism conditioned on illumination reliability. Furthermore, we propose a Multi-Scale Illumination Supervision Loss (MSIS-Loss), comprising a Region-Grounded Contrastive Loss (RGC-Loss) that enforces cross-modal similarity to be concentrated in text-relevant foreground regions and suppressed in background regions, and a Background Suppression Loss (BS-Loss) that provides pixel-level supervision for negative illumination maps, jointly ensuring a precise cross-modal alignment at each decoder stage. Extensive experiments on the MosMedData+ and QaTa-COV19 datasets demonstrate that TIRNet achieves state-of-the-art performance in LMIS. The code is available at: this https URL.

---


### 78. [Accelerating Hierarchical Sparse Predictive Coding with Hybrid Amortized Inference](https://arxiv.org/abs/2606.27802)

**<font color=#1a73e8>作者：</font>** Kazuhisa Fujita  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical predictive coding provides an interpretable framework for perception as error-driven inference in multi-layer generative models, while sparse coding imposes parsimonious latent representations through explicit sparsity constraints. Their combination yields hierarchical sparse predictive coding models with appealing computational and neuroscientific properties, but practical use is often limited by the cost of iterative latent inference. In such models, each input may require many recurrent refinement steps before a useful sparse representation is obtained, and this burden becomes more severe as the hierarchy deepens. We study this bottleneck by holding the hierarchical sparse energy fixed and varying the inference procedure. The comparison includes four schemes: classical iterative inference based on ISTA, an accelerated MFISTA reference, structurally informed amortized inference using a LISTA-style bottom-up encoder adapted to the hierarchical model, and a hybrid method in which this fast amortized initialization is followed by a small number of corrective energy-based refinement steps. Under this shared objective, we measure reconstruction quality, sparsity, latency, and stability on static image benchmarks. The results show that a shallow LISTA-style initializer plus short corrective recurrence improves over pure amortization while remaining much faster than long iterative inference.

---


### 79. [Reliable Homomorphic Matching for Fuzzy Labeled PSI at Scale](https://arxiv.org/abs/2606.27803)

**<font color=#1a73e8>作者：</font>** Erkam Uzun  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fuzzy Labeled Private Set Intersection (FLPSI) lets a receiver learn the labels of enrolled records similar to its query, and nothing else. Constructions based on a set-threshold reduction reach practical performance: a query matches a record when the two agree on a threshold number of components, and the private matching is delegated to an inner set-threshold kernel. We study its homomorphic form, which combines leveled-BFV homomorphic encryption (HE), a garbled circuit, and secret sharing to decide the match under encryption and release the record's label. We identify a composition gap in this kernel: efficiency is bought with a per-trial false-accept probability, but one query runs a trial for every record, so the error compounds with the database size into the kernel's realization soundness error (RSE), the rate at which it accepts a query the plaintext matcher would reject. The RSE is a reliability property of the cryptographic matching layer, not the matcher's accuracy, and a sound kernel must contribute zero or negligible RSE of its own. We formalize this as a composable security property, give a closed-form bound on the receiver's advantage, and close the gap with CSTPSI, a kernel that runs independent token rounds and raises the per-trial bound to a matching power. We prove CSTPSI secure in the semi-honest model. The bound sets the round count: two token rounds suffice for million-scale databases and three for billion-scale at the $10^{-6}$ engineering threshold. Our evaluation confirms this: at a million records the baseline kernel's RSE reaches 100% while CSTPSI holds it at 0 in every measured configuration. For large labels at small to moderate scale CSTPSI is more than 20x faster than the baseline, with up to 93% less communication, converging to the baseline only at million-scale. Our implementation, with a one-command reproducibility harness, is publicly available.

---


### 80. [Learning Complementary Action Modeling from Automotive Maintenance Instructions](https://arxiv.org/abs/2606.27808)

**<font color=#1a73e8>作者：</font>** Jiaqi Wu, Bai Li, Jochen Hartmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A minute lexical variation can reverse the procedural meaning of an instruction even when the rest of the sentence remains unchanged. In automotive maintenance instructions, this pattern often appears when an action phrase turns an instruction into its procedural counterpart. The entities, modifiers, and surrounding context remain largely invariant, while the action phrase determines the procedural relation. We define this task as Complementary Action Modeling (CAM). Given a maintenance instruction, the goal is to identify or generate its procedural counterpart by modifying the action phrase while preserving the remaining sentence context. This task focuses on three aspects: distinguishing complementarity from surface similarity, controlling generation at the action-phrase level, and evaluating relational correctness using retrieval, overlap-based, and human evaluation. Using a German automotive maintenance dataset, we examine these questions through candidate matching and controlled Seq2Seq generation. The results show that complementary maintenance instructions are best modeled as procedural associations grounded in subtle lexical cues. They should therefore not be treated as ordinary cases of sentence similarity or synonym-based paraphrasing.

---


### 81. [ATOD: Annealed Turn-aware On-policy Distillation for Multi-turn Autonomous Agents](https://arxiv.org/abs/2606.27814)

**<font color=#1a73e8>作者：</font>** Qitai Tan, Zefang Zong, Yang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training small language-model agents for long-horizon interactive tasks requires both fast imitation and reward-driven improvement. On-policy distillation (OPD) provides dense teacher guidance and typically improves rapidly in the early stage, but its gains saturate once the student approaches the teacher, limiting the final performance ceiling. Reinforcement learning (RL) directly optimizes environment rewards and encourages exploratory improvement toward a higher reward-defined ceiling, but sparse and delayed feedback makes early-stage learning much less efficient than OPD. In this paper, we propose ATOD (Annealed Turn-aware On-policy Distillation), a hybrid online distillation algorithm that explicitly exploits this complementarity. (1) ATOD uses an annealed OPD-RL schedule: OPD dominates early training to approach teacher-level behavior, while RL is gradually strengthened to drive reward-based exploration. (2) ATOD introduces Turn-level Disagreement-Uncertainty Reweighting (T-DUR), which softly amplifies high-utility turns and improves dense supervision in long trajectories. Experiments on ALFWorld, WebShop, and Search-QA show that ATOD consistently outperforms competing post-training baselines: across the three student sizes, ATOD improves average success rate by 3.03 points over OPD and 23.62 points over GRPO, while surpassing the corresponding teacher models by 2.16 points.

---


### 82. [Scalable and Differentiable Point-Cloud Registration Using Maximum Mean Discrepancy](https://arxiv.org/abs/2606.27818)

**<font color=#1a73e8>作者：</font>** Rixon Crane, Fahira Afzal Maken, Nicholas Lawrance 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MMD-Reg, a novel correspondence-free approach to point-cloud registration that is differentiable and has linear computational complexity in the number of points. We model registration as a nonlinear least-squares problem based on the Maximum Mean Discrepancy, approximated using random Fourier features. The resulting objective can be solved efficiently with standard methods such as Levenberg-Marquardt, and the solution is differentiable via the implicit function theorem. This allows MMD-Reg to be used as a differentiable optimization layer within end-to-end trainable models, supporting registration under challenging conditions such as poor initial alignment and partial overlap. We demonstrate this Neural MMD-Reg formulation by integrating the layer with a set transformer, training the resulting model in supervised and unsupervised settings, and comparing its performance against recent learning-based methods. We also evaluate standalone MMD-Reg, comparing its accuracy and scalability against widely used non-learning-based registration methods.

---


### 83. [Exploring and Exploiting Synchrony Limitations of Time-Triggered Network-Agnostic Guardians](https://arxiv.org/abs/2606.27819)

**<font color=#1a73e8>作者：</font>** Shreya Vithal Kulhalli, Mohammad Ibrahim Alkoudsi, Gerhard Fohler  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Time-triggered communication protocols rely on trusted components known as guardians to enforce adherence to predetermined network schedules. Network-agnostic guardians offer an efficient and scalable distributed solution with reduced implementation cost and complexity compared to network-aware alternatives. However, this efficiency is based on the guardian's dependence on the controlled node for clock synchronization, which introduces a vulnerability: a malicious node can exploit this dependency to launch timing attacks against its guardian and eventually interfere with messages from other nodes on the network. In this paper, we establish a theoretical lower bound on the attainable clock synchronization precision between a node and its network-agnostic guardian. Building on this result, we introduce a timing attack that leverages the unavoidably imperfect clock synchrony to cause controlled and undetected de-synchronization of the guardian. The attack enables a malicious node to cause collisions with targeted critical network messages. We evaluate the effectiveness of the attack using a FlexRay field bus network model implemented in the OMNeT++ simulation framework. Our results show that the attack is able to remain undetected with 100% success and disrupts the transmission of the critical messages of the target node by causing collisions with them with 100% success.

---


### 84. [Pepti-drift: Toxicity-Repulsive Drifting for Antigen-Conditioned Discrete Peptide Generation](https://arxiv.org/abs/2606.27824)

**<font color=#1a73e8>作者：</font>** Takashi Fujiwara, Hikaru Shindo, Kaushalya Madhawa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Peptides are a promising therapeutic modality that combine the chemical tunability of small molecules with the target specificity of macromolecular therapeutics. However, designing antigen-specific binding peptides while avoiding toxicity remains a major challenge for therapeutic peptide discovery. Here, we present Pepti-drift, a toxicity-aware latent refinement framework that generates peptide candidates through a single antigen-conditioned drift step. In a peptide embedding space, Pepti-drift learns to attract generated peptide latents toward antigen-matched binding peptides while repelling them from toxicity-associated regions. This is challenging because binding-promoting physicochemical features often overlap with toxicity-associated features in peptide representation space. To address this, we introduce a warm-up strategy to stabilize this competing objective by first learning binding-oriented attraction and then increasing toxicity repulsion.

---


### 85. [CSD: Content-aware Speculative Decoding for Efficient Image Generation](https://arxiv.org/abs/2606.27829)

**<font color=#1a73e8>作者：</font>** Mingcheng Wang, Junbo Qiao, Yunchen Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Speculative decoding (SD) has emerged as a key solution to accelerate the inference of autoregressive models. However, in the field of image generation, it faces the challenge of low acceptance rates, and directly relaxing its criteria leads to degradation in image quality. In this paper, we propose a novel content-aware speculative decoding algorithm, termed CSD, which integrates an entropy-based probability relaxation mechanism with an optimal resampling strategy to enhance the inference efficiency for autoregressive image generation. By leveraging the informational uncertainty inherent in different regions of an image, CSD dynamically adjusts the acceptance probability of candidate tokens, increasing the acceptance rate in low-detail areas to accelerate generation. Moreover, a distribution alignment filter is introduced to ensure the output distribution to be aligned with the target model, which significantly improves the generative quality. Experiments conducted on Lumina-mGPT and Janus-Pro demonstrate that the superiority of the proposed CSD. Our source code is available at this https URL.

---


### 86. [Hippocampus-DETR: An Explicit Memory Object Detection Framework Based on Hippocampus Modeling](https://arxiv.org/abs/2606.27831)

**<font color=#1a73e8>作者：</font>** Zhaoning Shi, Bo Ma, Hao Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the lack of explicit memory mechanisms in current object detection models and proposes Hippocampus-DETR, a novel detection framework based on biological hippocampal memory modeling. This framework integrates a hippocampal memory network module, HipNet, into the DETR architecture and systematically simulates the anatomical structure and functional organization of hippocampal subregions, including the entorhinal cortex, dentate gyrus, CA3, CA1, and subiculum. Through this design, Hippocampus-DETR realizes pattern separation, pattern completion, importance filtering, and information integration of visual encoding features. During training, different memory submodules are optimized using a layer-wise training strategy, ultimately forming a memory system with memory retrieval and completion capabilities. Experimental results demonstrate that Hippocampus-DETR achieves higher detection accuracy than current mainstream models. More importantly, models equipped with this framework also exhibit excellent generalization ability and data efficiency in tasks such as few-shot image classification, multimodal feature construction, and image restoration. Subsequent experiments further validate the functional necessity and internal interpretability of each memory submodule. This study not only provides a novel object detection framework, but also offers a feasible technical pathway for integrating neurocognitive mechanisms with deep learning models, highlighting its significant value in improving model learning efficiency and task robustness. The project is available at this https URL.

---


### 87. [USAD: Uncertainty-aware Statistical Adversarial Detection](https://arxiv.org/abs/2606.27832)

**<font color=#1a73e8>作者：</font>** Zhijian Zhou, Xunye Tian, Jiacheng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Statistical adversarial detection (SAD) treats detection as a two-sample test. Given a reference set of clean examples (CEs) and a batch of queries, potentially containing an unknown mixture of CEs and adversarial examples (AEs), SAD decides whether the query distribution drifts away from the CE distribution while controlling the false-alarm rate. Existing SAD-based methods mainly use maximum mean discrepancy (MMD) to measure the distributional discrepancy. However, MMD's distributional properties limit its ability to capture characteristic uncertainty patterns of AEs that are crucial for detection: AEs typically exhibit abnormal feature spread (i.e., global uncertainty) and instability under perturbations (i.e., local uncertainty). To close the gap, we propose Uncertainty-aware Statistical Adversarial Detection (USAD), which explicitly captures these uncertainty patterns with two new statistics: (1) Variance Discrepancy (VD), which measures the difference in feature spread between AEs and CEs to capture global uncertainty differences. (2) Perturbation-based Covariance Discrepancy (PCD), which compares feature covariance under Gaussian perturbations to capture local uncertainty differences. By aggregating VD and PCD, USAD achieves superior detection performances over baseline methods against various adversarial attacks, highlighting the importance of considering characteristic behaviors of AEs for effective SAD. Our code is available at: this https URL.

---


### 88. [WattLayer: Get Layers Right to Estimate Inference Energy of Neural Networks](https://arxiv.org/abs/2606.27841)

**<font color=#1a73e8>作者：</font>** Adrien Sardi, Marie-Line Alberi Morel, Sara Alouf 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of Artificial Intelligence (AI) has led to increasing concerns about energy consumption, yet there is a lack of standardized methodologies to accurately estimate AI inference energy consumption, particularly across various tasks and architectures. In this study, we propose a task independent, layer-wise energy estimation model for AI architectures. Our model is evaluated on a large dataset of more than 100,000 layers for 295 neural network architectures across 3 widely-used tasks and 3 distinct hardware platforms. Our approach achieves a median error of 19.6%, outperforming state-of-the-art methods. We further show that layer-wise decomposition generalize to new tasks without complete retraining, by leveraging shared layers across architectures. It offer tools, insights and a precise methodology to empower stakeholders in designing energy-efficient AI systems.

---


### 89. [Applicability of memorization indicators for early spotting of overfitting while recalibrating sEMG-decoders on low sample sizes](https://arxiv.org/abs/2606.27855)

**<font color=#1a73e8>作者：</font>** Stephan J. Lehmler, Tobias Glasmachers, Ioannis Iossifidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models for surface electromyography (sEMG) can benefit substantially from subject-specific (re-)calibration, since no sufficiently large and diverse datasets are available to train fully generic decoders. However, for user acceptance, the number of repetitions that can realistically be collected during calibration is severely limited, which increases the risk of overfitting and, in extreme cases, can even degrade performance compared to the uncalibrated model. Classical overfitting indicators such as validation performance and regularization with early stopping are difficult to apply in this low-sample regime, as they require additional held-out data that is rarely available in practical calibration scenarios. In this work, we investigate a recently proposed class of memorization indicators based solely on the activation statistics of rectified linear units (ReLU) in deep neural networks, which can be computed directly from training data without any extra validation set. We conduct a transferlearning experiment on a benchmark sEMG dataset, where a convolutional neural network is first pre-trained on multiple subjects and subsequently fine-tuned on individual users using only a small number of repetitions. During calibration, we monitor both decoding performance and the activation behaviour of the last hidden layer. Our results provide first evidence that decreases in test accuracy during fine-tuning are ac companied by characteristic changes in activation rates, indicating that activation-based memorization indicators are a promising tool for early spotting of unsuccessful learning in low-sample sEMG calibration settings.

---


### 90. [ScaLe-INR: Scale and Learn Implicit Neural Representations](https://arxiv.org/abs/2606.27862)

**<font color=#1a73e8>作者：</font>** Buwaneka Epakanda, Athulya Ratnayake, Pandula Thennakoon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit Neural Representations (INRs) parameterized by multilayer perceptrons excel at modeling continuous signals. However, a key challenge persists as INRs fundamentally suffer from spectral bias and information cross-talk. When a single network attempts to capture multi-scale phenomena, high-frequency weight updates destructively interfere with the underlying low-frequency structural approximation. We introduce Scale and Learn INR (ScaLe-INR), a novel multi-branch architecture that resolves these limitations by explicitly matching the signal's frequency spectrum with the optimal operating region of the INR. Drawing upon the Fourier inverse scaling theorem we demonstrate that applying directional coordinate scaling expands a network's representational bandwidth along specific spatial axes. To mathematically enforce functional disentanglement and minimize task-specific information leakage between branches, we propose a Directional Edge Guidance Loss, a spatially-conditioned sparsity prior derived from ground-truth gradients. By constraining the high-frequency branches to act as strict, localized edge-filters, ScaLe-INR eliminates spectral cross-talk, accelerates convergence, and achieves high-fidelity signal reconstruction on complex multi-scale topologies. We evaluate ScaLe-INR across diverse reconstruction and inverse tasks, demonstrating substantial performance gains over existing state-of-the-art (SOTA) methods. The proposed architecture improves upon the nearest baselines by +5.16 dB in image reconstruction and +0.65 dB in image denoising. Furthermore, it achieve an impressive figure of 50.02 dB on audio reconstruction and 0.999 IOU(Intersection Over Union) on 3D reconstruction which beats the all SOTA models.

---


### 91. [GNBAN: Graph Neural Basis Attention Networks for Long-Horizon Forecasting over Large Entity Sets](https://arxiv.org/abs/2606.27863)

**<font color=#1a73e8>作者：</font>** Janak M. Patel, Anirudh Deodhar, Dagnachew Birru  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Demand forecasting at the bottom of a retail hierarchy requires predicting tens of thousands of correlated long-horizon series across products, stores, and regions. Modern systems must scale across massive catalogs, capture shared demand dynamics, and remain interpretable enough to be trusted. Classical statistical methods need a separate model per series and are hard to manage at scale; deep autoregressive models struggle as the joint state grows to tens of thousands of dimensions; and recent graph-based forecasters, while capturing cross-entity dependencies, often produce opaque long-horizon forecasts. We propose GNBAN (Graph Neural Basis Attention Network), an end-to-end architecture combining heterogeneous graph representation learning with an interpretable basis-decomposition head. Retail data are represented directly as a heterogeneous graph derived from the relational schema, so a single model serves the entire catalog. Rather than predicting the horizon directly, GNBAN decomposes each forecast into trend, seasonal, and generic components. Its key innovation is a per-basis attention mechanism: each basis function keeps its own learnable query and retrieves information independently from the entity's historical neighborhood, letting different bases specialize to distinct temporal patterns while preserving interpretability. On two large-scale benchmarks, M5 Walmart and Favorita Grocery Sales, evaluated under matched protocols, GNBAN improves volume-weighted WRMSSE by roughly 4-5% over a matched graph baseline. Qualitative analysis shows the learned decomposition exposes trend, seasonal, and residual demand drivers without post-hoc explanation methods. These results demonstrate that scalable relational forecasting and interpretable forecast decomposition can be achieved together in a unified graph-based framework.

---


### 92. [A Unified Framework for Vision Transformers Equivariant to Discrete Subgroups of $\mathrm{O}(2)$](https://arxiv.org/abs/2606.27864)

**<font color=#1a73e8>作者：</font>** T\=ıkun Ông, Georg Bökman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision transformers have become a dominant architecture for visual recognition. However, standard models do not explicitly encode the planar symmetries that arise in many vision domains. We introduce a family of vision transformers equivariant to arbitrary discrete subgroups of $\mathrm{O}(2)$, providing a unified framework that generalizes prior flipping- and $D_4$-equivariant transformer architectures. Our construction yields equivariant analogues of the core transformer components, together with expressivity guarantees for the resulting layers. In particular, we show that whenever $H \le G$, the class of $G$-equivariant ViTs embeds naturally into the class of $H$-equivariant ViTs. We also prove that, in the single-head setting, the corresponding equivariant self-attention layer realizes every $G$-equivariant self-attention map representable by ordinary self-attention. We further construct a $D_6$-equivariant model based on hexagonal patches, making the architecture compatible with six-fold rotational symmetries. We evaluate the resulting models on the PatternNet aerial image dataset in artificially data-scarce regimes across subgroups of $D_4$ and $D_6$. Our experiments compare two equivariant attention mechanisms and analyze how the choice of homogeneous-space configurations used in the nonlinearities affects performance. Preliminary results under matched parameter budgets indicate that equivariance can improve recognition accuracy, motivating further study of how discrete symmetry groups shape transformer-based visual recognition models.

---


### 93. [SpatialUAV: Benchmarking Spatial Intelligence for Low-Altitude UAV Perception, Collaboration, and Motion](https://arxiv.org/abs/2606.27876)

**<font color=#1a73e8>作者：</font>** Haoyu Zhang, Meng Liu, Qianlong Xiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence is essential for low-altitude unmanned aerial vehicle (UAV) perception, collaboration, and navigation. However, existing UAV benchmarks often emphasize image-level recognition, single-view understanding, or narrow answer formats, leaving 3D spatial inference, multi-view collaboration, scene dynamics, and diverse task formulations insufficiently evaluated. To address these gaps, we introduce SpatialUAV, a real low-altitude UAV benchmark comprising 4,331 curated instances across 14 fine-grained task types, covering semantic discrimination, spatial relation, aerial--aerial collaboration, aerial--ground collaboration, and motion understanding. SpatialUAV organizes all samples into a unified visual-input--question--answer schema, while supporting seven input configurations and nine answer formats, including option labels, region identifiers, geometric values, cross-view correspondences, and free-form motion descriptions. To ensure reliable and grounded evaluation, our data construction pipeline integrates detector-assisted regions, depth supervision, metadata-derived rules, extensive manual annotation, blind filtering, and multi-turn human validation, together with task-specific metrics for heterogeneous outputs. Evaluating representative vision-language models across three categories, we show that current models remain far from human-level performance, with pronounced bottlenecks in cross-view association, structured grounding, geometric reasoning, and temporal viewpoint understanding. These results offer empirical guidance for advancing low-altitude UAV spatial intelligence. Code and data are available at this https URL.

---


### 94. [OrthoTryOn: Geometric Orthogonalization for Conflict-Free Unified Fashion Generation](https://arxiv.org/abs/2606.27880)

**<font color=#1a73e8>作者：</font>** Zhaotong Yang, Ying Tai, Jiahui Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified fashion generation integrates tasks like virtual try-on and garment reconstruction into a single model to reduce task-specific adaptation costs. However, naive parameter sharing across semantically distinct tasks induces negative transfer through severe inter-task gradient conflict. We propose OrthoTryOn, a unified framework mitigating this interference within a shared Low-Rank Adaptation (LoRA) module. Its Orthogonal Subspace Projection (OSP) applies task-specific orthogonal rotations to bottleneck features, mapping them into decorrelated coordinate frames. To address residual semantic coupling at inference time, we further propose Fisher-guided Negative Guidance (FNG), a parameter-free strategy that utilizes diagonal Fisher information to quantify inter-task sensitivity overlap and explicitly repels generation trajectories from the most confusable task via Classifier-Free Guidance. Extensive experiments demonstrate that OrthoTryOn avoids the severe performance degradation typical of naive unified training and even surpasses independently trained task-specific models, achieving state-of-the-art results across multiple benchmarks while generalizing robustly across diverse diffusion backbones. Code is available at this https URL.

---


### 95. [A Study of Temporal Fusion Strategies for Named Entity Recognition in Historical Texts](https://arxiv.org/abs/2606.27881)

**<font color=#1a73e8>作者：</font>** Emanuela Boros  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Temporal variation poses a unique challenge for named entity recognition (NER) in historical texts, where entities drift in surface form and salience across time. While language models (LMs) have made progress in various NLP tasks, their ability to reason about temporality, especially in diachronic contexts, remains limited or at least, questionable. In this paper, we systematically study how temporal metadata can be structurally embedded into NER models using a range of lightweight fusion strategies. We experiment with both absolute and relative temporal representations, injected into Transformer-based architectures via early or late fusion mechanisms such as cross-attention, adapters, and concatenation. Our evaluations on French and German historical datasets reveal that late fusion strategies yield more robust and temporally generalisable performance, particularly in early and noisy periods.

---


### 96. [A Comparison of Fusion Techniques for Multi-Modal Human Activity Recognition on the HARMES Dataset](https://arxiv.org/abs/2606.27886)

**<font color=#1a73e8>作者：</font>** Ahmed Mohamady, Robin Burchard, Kristof Van Laerhoven  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in Human Activity Recognition (HAR) from wearable sensors have shown that multi-modal deep learning models consistently outperform their uni-modal counterparts. Modalities can include IMUs, RGB cameras, audio signals, and others. One important aspect of multi-modal deep learning is the sensor fusion approach we apply. Over recent years, multiple fusion paradigms have been proposed for multi-modal HAR. However, to the best of our knowledge, no head-to-head comparison of these paradigms exists on a common multi-modal HAR benchmark dataset. To address this research gap, we systematically compare seven state-of-the-art sensor fusion methods on the recently released HARMES dataset, which comprises 61 hours of fully labeled IMU, audio, and ambient humidity data. The chosen dataset focuses on 15 household and personal hygiene activities of daily living (ADLs). By applying the seven different fusion techniques to a state-of-the-art multi-modal model architecture, we show that Gated Multi-modal Fusion achieves the highest macro F1-score (0.82), surpassing the concatenation-based late fusion HARMES paper baseline of 0.76 by +6pp under leave-one-participant-out evaluation. All code used in our experiments is made publicly available on GitHub.

---


### 97. [A Multi-Attribute Latent Space for Visual Analysis of Watches](https://arxiv.org/abs/2606.27897)

**<font color=#1a73e8>作者：</font>** Kai Lawonn, Tobias Günther, Monique Meuschke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a design rationale, embedding model, and interactive visual-analysis system for exploring large wristwatch collections through heterogeneous visual and semantic attributes. The system addresses a common limitation of catalog and e-commerce interfaces: users can filter by metadata, but they receive little support for open-ended exploration of visual similarity, stylistic alternatives, and mixed aesthetic-functional criteria. We therefore represent watches with separate attribute graphs for dial color and dial design, while using watch type as an explicit semantic organizer. Dials are segmented with a U-Net, watch types are predicted with a Vision Transformer, colors are represented through a shared CIELAB reference palette, and dial structure is described with a gradient-based image descriptor. We extend UMAP by combining attribute-specific neighborhood graphs in a unified probabilistic objective and by adding a class-aware layout term that separates global type structure from local visual neighborhoods. The resulting map is exposed in an interactive interface with spatial navigation, metadata filtering, detail inspection, and search-by-example insertion. We evaluate the approach through parameter analysis, runtime measurements, and a qualitative pilot study with watch experts and novices. The results suggest that the system supports discovery and comparison, while also revealing limitations in scalability assessment, search-by-example validation, and the need for broader domain studies. We explicitly discuss these limitations and derive design implications for multi-attribute latent-space visualization across heterogeneous visual collections.

---


### 98. [Long-Term Prediction of Local and Global Human Motion with Occlusion Recovery](https://arxiv.org/abs/2606.27900)

**<font color=#1a73e8>作者：</font>** Qiaoyue Yang, Sven Heutger, Christopher Niemann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion describes the three-dimensional full-body movement of a person. Anticipating such motion holds significant relevance across a wide range of application domains such as human-robot interaction, autonomous driving, animation, and healthcare. In recent research, spatial and temporal dependencies are modeled by bidirectional attention mechanisms. These typically anticipate human motion in an autoregressive manner which could cause an accumulation of errors over time. As a consequence, they solely focus on local pose forecasting. To address these limitations, we propose a non-autoregressive transformer based on spatio-temporal attention, and train it not only for local pose anticipation, but also for global motion prediction in space. Furthermore, to enhance its applicability in real-world scenarios, our model is also trained to recover missing joints due to occlusions, and is capable of processing varying lengths of history observations. Our code is publicly available at this https URL.

---


### 99. [There and Back Again: A Flexible-Frame Transformer for Multi-Exposure Fusion](https://arxiv.org/abs/2606.27905)

**<font color=#1a73e8>作者：</font>** Lishen Qu, Yao Liu, Shihao Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-exposure fusion (MEF) brings the dynamic range of conventional cameras closer to that of human vision, producing images with rich scene content. Given the large variability in scene luminance, exposure strategies often require different numbers of frames to capture the full radiance range faithfully. However, conventional MEF techniques are typically designed for a fixed number of inputs, forcing deployment systems to maintain separate models for different frame-count requirements, which undermines deployment efficiency. To address this limitation, we propose FreeMEF, the first flexible-frame transformer for MEF that seamlessly accommodates varying numbers of input exposures without retraining or architectural changes. The proposed approach consists of two key modules. First, we introduce a recurrent state space module (RSSM) that sequentially fuses features from arbitrary sequences via adaptive alignment and state-space recurrent modeling, thereby providing global information guidance for the subsequent restoration. Second, we devise a global feature guided block (GFGB) incorporating an extremity-aware hybrid attention (EAHA) and an affine-injection feed-forward network (AFFN), which effectively resolves the similarity paradox while simultaneously optimizing contrast and brightness regulation. Extensive experiments on three benchmark datasets demonstrate the effectiveness of our method, which performs favorably against state-of-the-art methods both quantitatively and qualitatively.

---


### 100. [TA-SparseMG: Trend-Aware Sparse Forecasting via Multi-Scale Gating for Long-Term Time Series](https://arxiv.org/abs/2606.27908)

**<font color=#1a73e8>作者：</font>** Wenchao Liu, Hongbing Wang, Youji Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term time series forecasting finds extensive applications in domains such as power demand, traffic flow, meteorological observation, and renewable energy dispatch. Forecasting dynamically varying long-term time series poses inherent challenges, including statistical nonstationarity, local high-frequency disturbances, and coupled cross-period dependencies, which make it difficult for lightweight models to balance parameter efficiency and forecasting performance. To address this issue, this study presents TA-SparseMG, a lightweight cross-period forecasting model built on SparseTSF's sparse cross-period modeling framework. It incorporates three key modules: a trend-aware reversible instance normalization module, a scale-adaptive gated denoising module, and a multiscale gated-attention MLP forecasting module. The trend-aware normalization module captures input-window statistics and calibrates forecast-window distributions, effectively mitigating distribution shift. The scale-adaptive gated denoising module performs feature smoothing and residual suppression before period rearrangement, thereby reducing interference from high-frequency perturbations. The multiscale gated attention prediction module strengthens the prediction head's adaptive representational capacity via conditional gating and feature modulation. Extensive experiments across multiple LTSF benchmarks demonstrate that the proposed TA-SparseMG consistently achieves superior, stable performance. Ablation studies confirm that each module independently improves distribution adaptation, input robustness, and cross-period feature mapping capability.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-160](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
