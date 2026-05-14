# 📦 其他研究 | 2026年05月15日

> 本类共 **328** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

---

### 1. [Scale-Gest: Scalable Model-Space Synthesis and Runtime Selection for On-Device Gesture Detection](https://arxiv.org/abs/2605.12506)

**<font color=#1a73e8>作者：</font>** Abdul Basit, Saim Rehman, Muhammad Shafique  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Realizing on-device ML-based gesture detection under tight real-time performance, energy and memory constraints is challenging, especially when considering mobile devices with varying battery-power levels. Existing EdgeAI deployments typically rely on a single fixed detector, limiting optimization opportunities. We present Scale-Gest, a novel run-time adaptive gesture detection framework that expands the detector space into a dense family of tiny-YOLO architectures. We introduce multiple novel device-calibrated ACE (Accuracy-Complexity-Energy) profiles by analyzing different model-resolution-stride operating points. A lightweight run-time controller selects an appropriate ACE mode under user-defined and battery constraints, while a motion-aware hand-gesture-tracking ROI gate crops the input for reduced complexity detection. To evaluate performance of our system in real-world car driving scenarios, we introduce a temporally-annotated Driver Simulated Gesture (DSG-18) dataset. Scale-Gest maintains event-level F1 while significantly reducing energy and latency compared to single-detector approaches. On a battery-powered laptop running gesture streams, our ACE controller reduces per-frame energy by 4x (from 6.9 mJ to 1.6 mJ) while maintaining high gesture-detection performance (event-level F1 = 0.8-0.9) and low mean latency (6 ms).

---


### 2. [Exploring how EFL students talk to and through AI to develop texts](https://arxiv.org/abs/2605.12523)

**<font color=#1a73e8>作者：</font>** David James Woo, Yangyang Yu, Yilin Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative Artificial Intelligence (AI) introduces new considerations for English as a foreign language (EFL) writing pedagogy. This study explores how students talk to and through AI by prompt engineering and negotiating authorship, respectively, and whether any patterns in the latter relate to students' writing performance. Using an exploratory mixed methods design, we analyzed screen recordings of 44 Hong Kong secondary students completing a Curricular Writing Task with AI Chatbots. Content analysis identified ten types of prompting strategies students employed, including questions, searches, and detailed instructions. From clustering these strategies, three distinct profiles of human-AI rhetorical load responsibility emerged: AI-dominant (52% of students), Human-dominant (25%) and Collaborative human-AI (14%). A MANOVA analysis indicated no significant multivariate effect of rhetorical load responsibility on three dimensions of students' writing performance: content, language, and organization. Students' prompting strategies and rhetorical load responsibility patterns have implications for their engagement and autonomy in EFL writing pedagogy.

---


### 3. [MorphOPC: Advancing Mask Optimization with Multi-scale Hierarchical Morphological Learning](https://arxiv.org/abs/2605.12528)

**<font color=#1a73e8>作者：</font>** Yuting Hu, Lei Zhuang, Chen Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As feature sizes shrink to the nanometer scale, accurately transferring circuit patterns from photomasks to silicon wafers becomes increasingly challenging. Optical proximity correction (OPC) is widely used to ensure pattern fidelity and manufacturability. Recent generative mask optimization models based on encoder-decoder architecture can synthesize near-optimal masks, serving as fast machine learning (ML) surrogates for traditional OPC. However, these models often fail to capture the geometric transformations from target layouts to mask patterns, leading to suboptimal quality. In this work, we formulate mask generation as a sequence of morphological operations on local layout features and propose \textit{MorphOPC}, a multi-scale hierarchical model with neural morphological modules to learn these transformations. Experiments on edge-based OPC and ILT benchmarks across metal and via layers show that \textit{MorphOPC} consistently outperforms state-of-the-art methods, achieving higher printing fidelity and lower manufacturing cost, demonstrating strong potential for scalable mask optimization.

---


### 4. [Ghost in the Context: Measuring Policy-Carriage Failures in Decision-Time Assembly](https://arxiv.org/abs/2605.12535)

**<font color=#1a73e8>作者：</font>** Igor Santos-Grueiro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LM agents do not act on raw interaction history; they act on a bounded decision state assembled by truncation, summarization, reordering, and rewriting. If directive-bearing state is dropped, weakened, or rebound during that step, an agent can cross a policy boundary without prompt override, model changes, or persistent-memory compromise. We study this failure mode over local Llama 3.1 8B, Qwen 2.5 7B, and Mistral 7B using judged exact constraint respect and direct audits of assembled-state visibility. We evaluate SafeContext, a control layer that pins control state, reuses retained control prefixes, and optionally injects reminders under pressure while keeping model weights fixed. Unmitigated risk is systematic, but absolute exact respect remains low. Against truncation, SafeContext yields small gains; against a strong structured-compaction policy, most aggregate lift disappears, leaving residual benefit mainly in overflow eviction and selected aliasing slices. Replay-only does not explain the effect. A larger-model extension on Qwen 14B and Llama 70B shows the same failure object under larger models, although sign and magnitude remain policy-conditional. Decision-time context assembly is therefore a measurable part of the control path that can be partially hardened.

---


### 5. [CROP: Expert-Aligned Image Cropping via Compositional Reasoning and Optimizing Preference](https://arxiv.org/abs/2605.12545)

**<font color=#1a73e8>作者：</font>** Zhitong Dong, Chao Li, Jie Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aesthetic image cropping aims to enhance the aesthetic quality of an image by improving its composition through spatial cropping. Previous methods often rely on saliency prediction or retrieval augmentation, ignoring the task's core requirement: a deep understanding of composition and aesthetics. Consequently, saliency-based methods struggle to make compositional trade-offs in complex scenes, while retrieval-based methods blindly refer to similar cases, lacking adaptive reasoning for unique scenes. Both approaches fail to align their automated cropping results with those of human experts. To address the above issues, we propose a novel paradigm that reformulates aesthetic cropping as a multimodal reasoning task, aiming to activate the VLM's analytical and comprehension capabilities in aesthetics. We design a Compositional Reasoning and Optimizing Preference method (CROP) that directs the VLM to think like a professional photographer. It deconstructs a complex and subjective aesthetic problem into an "analysis-proposal-decision" process, reasoning step by step through the analysis of scene elements and compositional principles. Meanwhile, our expert preference alignment module makes the model's decision consistent with human expert aesthetics. Extensive experiments across multiple datasets validate our method's superiority and component effectiveness.

---


### 6. [What Happens Before Decoding? Prefill Determines GUI Grounding in VLMs](https://arxiv.org/abs/2605.12549)

**<font color=#1a73e8>作者：</font>** Jiaping Lin, Fei Shen, Junzhe Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing training-free approaches for GUI grounding often rely on multiple inference runs, such as iterative cropping or candidate aggregation, to identify target elements. Despite this additional computation, each forward pass still independently interprets the instruction and parses the visual layout, without enabling progressive interaction among visual tokens. In this paper, we study what happens during GUI grounding in Vision-Language Models (VLMs) and identify a previously overlooked bottleneck. We show that grounding follows a two-stage paradigm: the prefill stage determines candidate UI elements, while the decoding stage subsequently refines the final coordinates. This asymmetry establishes prefill as the critical step, as errors in candidate selection cannot be effectively corrected during decoding. Based on this observation, we propose Re-Prefill, a training-free method that revisits inference by introducing an attention-guided second prefill stage to refine target selection. Specifically, visual tokens that consistently receive high attention from the query position, i.e., the final token, across layers are extracted as a preliminary target hypothesis and appended to the input, together with the instruction hidden states, enabling the model to deeply re-think its decision before coordinate generation. Experiments across four VLMs and five benchmarks, including ScreenSpot-Pro, ScreenSpot-V2, OSWorld-G, UI-Vision, and MMBench-GUI, demonstrate consistent improvements without additional training, with gains of up to 4.3% on ScreenSpot-Pro. Code will be available at this https URL.

---


### 7. [SSDA: Bridging Spectral and Structural Gaps via Dual Adaptation for Vision-Based Time Series Forecasting](https://arxiv.org/abs/2605.12550)

**<font color=#1a73e8>作者：</font>** Mingrui Zhang, Hanchen Yang, Wengen Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision models (LVMs) have recently proven to be surprisingly effective time series forecasters, simply by rendering temporal data as images. This success, how ever, rests on a largely unexamined premise: the rendered time series images are sufficiently close to natural images for knowledge in pre-trained models to transfer effectively. We argue that two gaps still remain, i.e., spectral and structural gaps, fundamentally limiting the potential of LVMs for time series forecasting. Spectrally, we systematically reveal that rendered time series images exhibit a markedly shallower power spectrum than the natural images LVMs are pre-trained to recognize. Structurally, reshaping 1D temporal sequences into 2D grids fabricates spurious spatial adjacencies while severing genuine temporal continuities, misleading the spatial inductive biases of pre-trained LVMs. To bridge these gaps, we propose SSDA, a dual-branch network that spectrally and structurally adapts to unlock the full potential of LVMs for time series forecasting. At the data level, a Spectral Magnitude Aligner (SMA) applies 2D FFT to selectively enhance the magnitude spectrum toward natural-image statistics while preserving phase. At the model level, a Structural-Guided Low-Rank Adaptation (SG-LoRA) injects position-aware temporal encodings into patch embeddings and adapts at tention via low-rank updates. The two branches are further adaptively fused to produce the final forecast. Extensive experiments on seven real-world benchmarks demonstrate that SSDA consistently outperforms strong LVM- and LLM-based baselines under both full-shot and few-shot settings. Code is publicly available at this https URL.

---


### 8. [DelAC: A Multi-agent Reinforcement Learning of Team-Symmetric Stochastic Games](https://arxiv.org/abs/2605.12555)

**<font color=#1a73e8>作者：</font>** Duan-Shin Lee, Yu-Hsiu Hung  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In this paper we study team-symmetric games with $m\ge 2$ teams. Players within a team have symmetric identity and have a common payoff function. We show that team-symmetric games always have a team-symmetric Nash equilibrium. We develop and solve a linear complementarity problem of team-symmetric Nash equilibria. We propose an actor-critic based multi-agent reinforcement learning algorithm for team-symmetric games. Through simulations, we show that this multi-agent reinforcement learning algorithm performs much better than many existing algorithms.

---


### 9. [M2Retinexformer: Multi-Modal Retinexformer for Low-Light Image Enhancement](https://arxiv.org/abs/2605.12556)

**<font color=#1a73e8>作者：</font>** Youssef Aboelwafa, Hicham G. Elmongui, Marwan Torki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light image enhancement is challenging due to complex degradations, including amplified noise, artifacts, and color distortion. While Retinex-based deep learning methods have achieved promising results, they primarily rely on single-modality RGB information. We propose M2Retinexformer (Multi-Modal Retinexformer), a novel framework that extends Retinexformer by incorporating depth cues, luminance priors, and semantic features within a progressive refinement pipeline. Depth provides geometric context that is invariant to lighting variations, while luminance and semantic features offer explicit guidance on brightness distribution and scene understanding. Modalities are extracted at multiple scales and fused through cross-attention, with adaptive gating dynamically balancing illumination-guided self-attention and cross-attention based on the reliability of auxiliary cues. Evaluations on the LOL, SID, SMID, and SDSD benchmarks demonstrate overall improvements over Retinexformer and recent state-of-the-art methods. Code and pretrained weights are available at this https URL

---


### 10. [Learning When to Act: Communication-Efficient Reinforcement Learning via Run-Time Assurance](https://arxiv.org/abs/2605.12561)

**<font color=#1a73e8>作者：</font>** Adam Haroon, Erick J. Rodríguez-Seda, Cody Fleming 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe reinforcement learning (RL) typically asks $\textit{what}$ an agent should do. We ask $\textit{when}$ it needs to act, and show that a single policy can jointly learn control inputs and communication-efficient timing decisions under a pointwise Lyapunov safety shield. We focus on stabilization around a known equilibrium, where CARE-based LQR backups, Lyapunov certificates, and classical Lyapunov-STC are well defined, enabling clean comparison against analytical baselines. A run-time assurance (RTA) layer overrides the policy via a one-step-ahead Lyapunov prediction and a precomputed LQR backup, providing a strictly stronger guarantee than constrained MDP methods that enforce safety only in expectation. On an inverted pendulum, cart--pole, and planar quadrotor, the learned policy achieves $1.91\times$, $1.45\times$, and $3.51\times$ higher mean inter-sample interval (MSI) than a Lyapunov-triggered baseline; a fixed LQR controller at the same average rate is unstable on all three plants, showing that adaptive timing, not a lower average rate, makes sparsity safe. A CARE-derived Lyapunov reward transfers across environments without redesign, with a single weight $w_c$ controlling the stability--communication tradeoff; ablations confirm the RTA shield is essential, with its removal reducing MSI by $1.27$--$1.84\times$ and degrading state norms. A preference-conditioned extension recovers the full tradeoff frontier from one model at $\tfrac{2}{11}$ of training compute, and SAC experiments show the results are algorithm-agnostic across discrete and continuous domains. A 12-state 3D quadrotor case study extends the framework to higher-dimensional systems where classical STC is intractable, and robustness to $\pm30\%$ mass variation and disturbances shows graceful degradation, with the RTA absorbing what the learned policy cannot.

---


### 11. [OverrideFuzz: Semantic-Aware Grammar Fuzzing for Script-Runtime Vulnerabilities](https://arxiv.org/abs/2605.12563)

**<font color=#1a73e8>作者：</font>** Yiran Qiu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Script-language runtimes such as Python, Lua, and JavaScript are widely deployed in security sensitive contexts, yet they remain difficult to test because valid inputs must satisfy syntax, dynamic type constraints, and object-level semantics. Existing grammar and reflection-based fuzzers improve syntactic validity and interface reachability, but they rarely model override hooks, dynamic rebinding, and attribute-resolution behavior that can redirect built-in operations across the script-native boundary and trigger use-after-free or type-confusion bugs. We present OverrideFuzz, a two-phase, semantic-aware grammar fuzzer for script-language runtimes. Its declaration phase constructs objects with overriding methods, while its execution phase generates operations that route through those hooks. Active reflection tracks runtime types, and passive reflection learns from error messages to remove invalid operation shapes, allowing generation to approach semantic correctness without manual API specification. We evaluate OverrideFuzz on CPython, Lua, and QuickJS. All three targets show consistent coverage growth, with rapid early expansion followed by slower incremental gains, and Lua benefits most from its pervasive metamethod dispatch mechanism. Although OverrideFuzz did not discover novel vulnerabilities during the bounded evaluation period, corpus analysis shows that it reconstructs inputs matching known vulnerability patterns, which suggests that semantic-aware generation reaches the intended script-native boundary behaviors.

---


### 12. [Persona-Conditioned Adversarial Prompting (PCAP): Multi-Identity Red-Teaming for Enhanced Adversarial Prompt Discovery](https://arxiv.org/abs/2605.12565)

**<font color=#1a73e8>作者：</font>** Cristian Morasso, Anisa Halimi, Muhammad Zaid Hameed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing automated red-teaming pipelines often miss attacks that depend on attacker identity, framing, or multi-turn tactics. This under-coverage underestimates real-world risk. We introduce Persona-Conditioned Adversarial Prompting (PCAP), which conditions adversarial search on attacker personas and strategy cards and runs parallel persona-conditioned beam searches to discover diverse, transferable jailbreaks. PCAP is orthogonal to the underlying search algorithm and substantially increases attack success rate (ASR) and prompt diversity (e.g., ASR on GPT-OSS~120B from $\approx58\% \rightarrow \approx97\%$), improving attack strategy coverage and diversity.

---


### 13. [Pyramid Self-contrastive Learning Framework for Test-time Ultrasound Image Denoising](https://arxiv.org/abs/2605.12567)

**<font color=#1a73e8>作者：</font>** Jiajing Zhang, Bingze Dai, Xi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The inherent electronic and speckle noise complicates clinical interpretation of ultrasound images. Conventional denoising methods rely on explicit noise assumptions whose validity diminishes under composite noise conditions. Learning-based methods require massive labeled data and model parameters. These pre-defined and pre-trained manners entail an inevitable domain shift in complex in vivo environments, so they are limited to a specific noise type and often blur structural details. In this study, we propose a pure test-time training framework for one-shot ultrasound image denoising and apply it to synthetic aperture ultrasound (SAU), which synthesizes transmit focus from sub-aperture transmissions. Our Aperture-to-Aperture (A2A) framework disentangles anatomical similarity and noise randomness from shuffled sub-apertures through self-contrastive learning in pyramid latent spaces. The clean image is then decoded from the anatomy space, while discarding the noise space. A2A is trained at test time on one noisy sample of SAU signals, so it fundamentally eliminates the domain shift and pretraining costs. Simulation experiments, including electronic noise levels of 0 to 30 dB and different inclusion geometries, demonstrated an improvement of 69.3% SNR and 34.4% CNR by A2A. The in vivo results showed 84.8% SNR and 25.7% CNR gains using only two aperture data of the heart in six echocardiographic views, liver, and kidney. A2A delivers clear images/signals across diverse imaging targets and configurations, paving the way for more reliable anatomical visualization and functional assessment by ultrasound.

---


### 14. [M3Net: A Macro-to-Meso-to-Micro Clinical-inspired Hierarchical 3D Network for Pulmonary Nodule Classification](https://arxiv.org/abs/2605.12570)

**<font color=#1a73e8>作者：</font>** Jinyue Li, Yuzhou Yu, Jingjing Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The accurate classification of benign and malignant pulmonary nodules in CT scans is critical for early lung cancer screening, yet remains challenging due to the multi-scale and heterogeneous nature of pulmonary nodules. While deep learning offers potential for auxiliary diagnosis, most existing models act as "black boxes", lacking the transparency and explainability required for trustworthy clinical integration. To address this issue, we propose M3Net, a novel 3D network for pulmonary nodule classification inspired by the hierarchical diagnostic workflow of radiologists, which integrates multi-scale contextual information from fine-grained structures to global anatomical relationships. Our framework constructs a progressive multi-scale input, from fine-grained nodule structures to local semantics and global spatial relationships. M3Net employs scale-specific encoders and ensures cross-scale semantic consistency through latent space projection and mutual information maximization. Extensive experiments on the public LIDC-IDRI dataset and a self-collected clinical dataset (USTC-FHLN) demonstrate that our method achieves state-of-the-art performance, with accuracies of 86.96% and 84.24% respectively, outperforming the best baseline by 3.26% and 2.17%. The results validate that M3Net provides a more robust and clinically relevant solution for pulmonary nodule classification. The code is available at this https URL.

---


### 15. [Improving Diffusion Posterior Samplers with Lagged Temporal Corrections for Image Restoration](https://arxiv.org/abs/2605.12573)

**<font color=#1a73e8>作者：</font>** Davide Evangelista, Elena Morotti, Francesco Pivi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based posterior sampling (PS) is a leading framework for imaging inverse problems, combining learned priors with measurement constraints. Yet, its standard formulations rely on instantaneous data-consistent estimates, which induce temporal variability in the reverse dynamics. We reinterpret PS from a dynamical perspective, showing that the standard PS update corresponds to a first-order discretization of the diffusion dynamics plus a residual correction capturing the mismatch between the denoised prediction and the data-consistent estimate. A second-order discretization, however, naturally introduces a temporal correction based on the variation of consecutive estimates. Building on this, we propose LAMP, combining the second-order update with the residual correction characterizing a PS technique. LAMP thus inherits a lagged temporal correction, and it can be implemented as a modular plug-in over the PS backbone. We show that LAMP preserves the structure of a posterior sampler, and we perform a one-step risk analysis to characterize when LAMP improves the reverse transition via a bias-variance trade-off. Experiments across multiple imaging tasks demonstrate consistent improvements over strong baselines such as DiffPIR and DDRM, without increasing the number of denoising evaluations.

---


### 16. [CAWI: Copula-Aligned Weight Initialization for Randomized Neural Networks](https://arxiv.org/abs/2605.12580)

**<font color=#1a73e8>作者：</font>** Mushir Akhtar, M. Tanveer, Mohd. Arshad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Randomized neural networks (RdNNs) enable efficient, backpropagation-free training by freezing randomly initialized input-to-hidden weights, which permits a closed-form solution for the output layer. However, conventional random initialization is blind to inter-feature dependence, ignoring correlations, asymmetries, and tail dependence in the data, which degrades conditioning and predictive performance. To the best of our knowledge, this limitation remains unaddressed in the RdNN literature. To close this gap, we propose CAWI (Copula-Aligned Weight Initialization), a framework that draws input-to-hidden weights from a data-fitted copula that matches empirical dependence, ensuring the frozen projections respect inter-feature dependence without sacrificing the closed-form solution. CAWI (i) maps each feature to the unit interval using empirical CDFs, (ii) fits a multivariate copula that captures rank-based dependence among features, and (iii) samples each weight column w_j from the fitted copula and applies a fixed inverse marginal transform to set scale. The objective, solver, and "freeze-once" paradigm remain unchanged; only the sampling law for W becomes dependence-aware. For dependence modeling, we consider two copula families: elliptical (Gaussian, t) and Archimedean (Clayton, Frank, Gumbel). This enables CAWI to handle diverse dependence, including tail dependence. We evaluate CAWI across 83 diverse classification benchmarks (binary and multiclass) and two biomedical datasets, BreaKHis and the Schizophrenia dataset, using standard shallow and deep RdNN architectures. CAWI consistently delivers significant improvements in predictive performance over conventional random initialization. Code is available at: this https URL

---


### 17. [TrackCraft3R: Repurposing Video Diffusion Transformers for Dense 3D Tracking](https://arxiv.org/abs/2605.12587)

**<font color=#1a73e8>作者：</font>** Jisu Nam, Jahyeok Koo, Soowon Son 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense 3D tracking from monocular video is fundamental to dynamic scene understanding. While recent 3D foundation models provide reliable per-frame geometry, recovering object motion in this geometry remains challenging and benefits from strong motion priors learned from real-world videos. Existing 3D trackers either follow iterative paradigms trained from scratch on synthetic data or fine-tune 3D reconstruction models learned from static multi-view images, both lacking real-world motion priors. Pre-trained video diffusion transformers (video DiTs) offer rich spatio-temporal priors from internet-scale videos, making them a promising foundation for 3D tracking. However, their frame-anchored formulation, which generates each frame's content, is fundamentally mismatched with reference-anchored dense 3D tracking, which must follow the same physical points from a reference frame across time. We present TrackCraft3R, the first method to repurpose a video DiT as a feed-forward dense 3D tracker. Given a monocular video and its frame-anchored reconstruction pointmap, TrackCraft3R predicts a reference-anchored tracking pointmap that follows every pixel of the first frame across time in a single forward pass, along with its visibility. We achieve this through two designs: (i) a dual-latent representation that uses per-frame geometry latents and reference-anchored track latents as dense queries, and (ii) temporal RoPE alignment, which specifies the target timestamp of each track latent. Together, these designs convert the per-frame generative paradigm of video DiTs into a reference-anchored tracking formulation with LoRA fine-tuning. TrackCraft3R achieves state-of-the-art performance on standard sparse and dense 3D tracking benchmarks, while running 1.3x faster and using 4.6x less peak memory than the strongest prior method. We further demonstrate robustness to large motions and long videos.

---


### 18. [A Data Efficiency Study of Synthetic Fog for Object Detection Using the Clear2Fog Pipeline](https://arxiv.org/abs/2605.12608)

**<font color=#1a73e8>作者：</font>** Mohamed Ahmed Mohamed, Xiaowei Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection in adverse weather is critical for the safety of autonomous vehicles; however, the scarcity of labelled, real-world foggy data remains a significant bottleneck. In this paper, we propose Clear2Fog (C2F), an end-to-end, physics-based pipeline that simulates fog on clear-weather datasets while ensuring sensor-level consistency across camera and LiDAR. By using monocular depth estimation and a novel atmospheric light estimation method, C2F overcomes structural artifacts and chromatic biases common in existing techniques. A human perceptual study confirms C2F's physical realism, with the generated images being preferred 92.95% of the time over an established method. Utilising a training set of 270,000 images from the Waymo Open Dataset, we conduct an extensive data efficiency study to investigate how environmental diversity influences model robustness. Our findings reveal that models trained on mixed-density fog datasets at 75% scale outperform those trained on fixed-density datasets at 100% scale. Furthermore, we investigate the sim-to-real transfer by fine-tuning pre-trained models on real-world foggy data. We demonstrate that a tenfold increase over the default fine-tuning learning rate successfully overcomes negative transfer from synthetic biases, resulting in a 1.67 mAP improvement over real-only baselines. The C2F pipeline provides a scalable framework for enhancing the reliability of autonomous systems in adverse weather and demonstrates the potential of diverse synthetic datasets for efficient model training.

---


### 19. [Creating Group Rules with AI: Human-AI Collaboration in WhatsApp Moderation](https://arxiv.org/abs/2605.12613)

**<font color=#1a73e8>作者：</font>** Gauri Nayak, Farhana Shahid, Aditya Vashistha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> WhatsApp is one of the most widely used messaging platforms globally, with billions of users sharing information in private groups. Yet, it offers little infrastructure to support moderation and group governance. In the absence of platform-level oversight, group admins bear the responsibility of governing group behavior. In this paper, we explore how WhatsApp group admins collaborate with AI tools to create, enforce, and maintain group rules. Drawing on a two-phase speculative design study with 20 admins in India, we examine how participants interacted with an AI assistant (Meta AI) to co-create rules and responded to a series of probes illustrating AI-assisted moderation features. Our findings show that while admins appreciated the AI's ability to surface overlooked rules and reduce their moderation burden, they were highly sensitive to issues of relational trust, data privacy, tone, and social context. We identify how group type and admin style shaped their willingness to delegate authority, and surface the limitations of current chatbot interfaces in supporting collaborative rule-making. We conclude with design implications for building moderation tools that center human judgment, relational nuance, contextual adaptability, and collective governance.

---


### 20. [DocAtlas: Multilingual Document Understanding Across 80+ Languages](https://arxiv.org/abs/2605.12623)

**<font color=#1a73e8>作者：</font>** Ahmed Heakl, Youssef Mohamed, Abdullah Sohail 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual document understanding remains limited for low-resource languages due to scarce training data and model-based annotation pipelines that perpetuate existing biases. We introduce DocAtlas, a framework that constructs high-fidelity OCR datasets and benchmarks covering 82 languages and 9 evaluation tasks. Our dual pipelines, differential rendering of native DOCX documents and synthetic LaTeX-based generation for right-to-left scripts produce precise structural annotations in a unified DocTag format encoding layout, text, and component types, without learned models for core annotation. Evaluating 16 state-of-the-art models reveals persistent gaps in low-resource scripts. We show that Direct Preference Optimization (DPO) using rendering-derived ground truth as positive signal achieves stable multilingual adaptation, improving both in-domain (+1.9%) and out-of-domain (+1.8%) accuracy without measurable base-language degradation, where supervised fine-tuning degrades out-of-domain performance by up to 21%. Our best variant, DocAtlas-DeepSeek, improves +1.7% over the strongest baseline.

---


### 21. [OceanCBM: A Concept Bottleneck Model for Mechanistic Interpretability in Ocean Forecasting](https://arxiv.org/abs/2605.12639)

**<font color=#1a73e8>作者：</font>** Sanah Suri, Kieran Ringel, Maike Sonnewald  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extreme ocean phenomena are challenging not only to predict but to diagnose, as accurate forecasts alone do not reveal the underlying physical drivers. While recent machine learning approaches achieve strong predictive skill, they remain largely opaque and provide limited guarantees of fidelity to ground-truth physics. We introduce OceanCBM, the first concept bottleneck model (CBM) for spatiotemporal prediction and mechanistic interrogation of ocean dynamics. OceanCBM uses mixed supervision to predict mixed layer heat content, a key precursor of marine heatwaves, while routing information through an intermediate layer of prescribed concepts derived from geophysical fluid dynamics and a 'free' concept. This design imposes soft physical structure without over-constraining the model, and the free concept both regularizes concept predictions and captures residual physical processes. Across ensemble initializations, we show that mixed supervision yields consistent mechanistic representations, whereas prediction-only and prescription-only baselines learn highly variable latent structures despite similar predictive performance. OceanCBM achieves interpretable, physically grounded representations without sacrificing skill, explicitly characterizing the interpretability-performance trade-off.

---


### 22. [MambaPanoptic: A Vision Mamba-based Structured State Space Framework for Panoptic Segmentation](https://arxiv.org/abs/2605.12640)

**<font color=#1a73e8>作者：</font>** Qing Cheng, Damiano Bertolini, Wei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoptic segmentation requires the simultaneous recognition of countable thing instances and amorphous stuff regions, placing joint demands on long-range context modelling, multi-scale feature representation, and efficient dense prediction. Existing convolutional and transformer-based methods struggle to satisfy all three requirements concurrently: convolutional architectures are limited in their capacity to model long-range dependencies, while transformer-based methods incur quadratic computational cost that is prohibitive at high resolutions. In this paper, we propose MambaPanoptic, a fully Mamba-based panoptic segmentation framework that addresses these limitations through two principal contributions. First, we introduce MambaFPN, a top-down feature pyramid that leverages Mamba blocks to generate globally coherent, multi-scale feature representations with linear computational complexity. Second, we adopt a PanopticFCN-style kernel generator that produces unified thing and stuff kernels for proposal-free panoptic prediction, enhanced by a QuadMamba-based feature refinement module applied at multiple network stages. Experiments on the Cityscapes and COCO panoptic segmentation benchmarks demonstrate that MambaPanoptic consistently outperforms PanopticDeepLab and PanopticFCN under comparable model sizes, and matches or surpasses Mask2Former on Cityscapes in PQ and AP while requiring fewer parameters.

---


### 23. [Co-Designing Organizational Justice Indicators for Algorithmic Systems](https://arxiv.org/abs/2605.12643)

**<font color=#1a73e8>作者：</font>** Fujiko Robledo Yamamoto, Nicholas Mattei, Pradeep Ragothaman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Fairness in machine learning is often conceptualized narrowly in comparative, distributional terms. In studying stakeholders' concepts of fairness, we find that this framing is insufficient to capture the full range of issues raised. As an alternative, we propose organizational justice as a framework that subsumes distributional fairness as well as other normative concerns. We conduct a case study of organizational justice relative to personalized recommendation in the context of Kiva Microfunds, a nonprofit micro-lending organization whose mission is to increase financial access for underserved communities across the world. We report on the results of co-design workshops conducted with Kiva employees who are involved in different departments and whose roles often lead them to prioritize normative concerns that are most supportive of the stakeholders with whom they work most closely. We apply organizational justice to understand design trade-offs among different normative goals stakeholders invoke. Based on these goals, we identify a suite of metrics that Kiva employees can use to monitor and assess the recommender system's impact on their organizational justice concerns and to seed discussions within the organization about appropriate configuration and deployment of this system in context.

---


### 24. [Population Risk Bounds for Kolmogorov-Arnold Networks Trained by DP-SGD with Correlated Noise](https://arxiv.org/abs/2605.12648)

**<font color=#1a73e8>作者：</font>** Puyu Wang, Jan Schuchardt, Nikita Kalinin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish the first population risk bounds for Kolmogorov-Arnold Networks (KANs) trained by mini-batch SGD with gradient clipping, covering non-private SGD as well as differentially private SGD (DP-SGD) with Gaussian perturbations that interpolate between independent and temporally correlated noise. This setting is substantially closer to practice than prior KAN theory along two axes: training is by mini-batch SGD, the standard recipe for modern networks, rather than full-batch gradient descent (GD); and correlated-noise mechanisms have empirically shown a more favorable privacy-utility tradeoff than independent-noise mechanisms. Our results cover the corresponding full-batch GD and independent-noise DP-GD results for KANs by Wang et al. (2026), while yielding sharper fixed-second-layer specializations. The technical core is a new analysis route for correlated-noise DP training in the non-convex regime. Temporal dependence breaks the conditional-centering structure underlying standard one-step SGD arguments, and the projection step obstructs the exact cancellation structure of correlated perturbations. We address these difficulties through an auxiliary unprojected dynamics, a shifted iterate that absorbs the current noise perturbation, and a high-probability bootstrap certifying projection inactivity. Combining this optimization analysis with a stability-based generalization argument yields the stated population risk bounds. To the best of our knowledge, this is the first optimization and population risk analysis of a correlated-noise mechanism for DP training beyond convex learning, in particular for neural networks.

---


### 25. [DIVER:Diving Deeper into Distilled Data via Expressive Semantic Recovery](https://arxiv.org/abs/2605.12649)

**<font color=#1a73e8>作者：</font>** Qianxin Xia, Zhiyong Shu, Wenbo Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset distillation aims to synthesize a compact proxy dataset that is unreadable or non-raw from the original dataset for privacy protection and highly efficient learning. However, previous approaches typically adopt a single-stage distillation paradigm, which suffers from learning specific patterns that overfit on a prior architecture, consequently suppressing the expression of semantics and leading to performance degradation across heterogeneous architectures. To address this issue, we propose a novel dual-stage distillation framework called ${\textbf{DIVER}}$, which leverages the pre-trained diffusion model to dive deeper into $\textbf{DI}$stilled data $\textbf{V}$ia $\textbf{E}$xpressive semantic $\textbf{R}$ecovery, an entire process of semantic inheritance, guidance, and fusion. Semantic inheritance distills high-level semantics of abstract distilled images into the latent space to filter out architecture-specific ``noise" and retain the intrinsic semantics. Furthermore, semantic guidance improves the preservation of the original semantics by directing the reverse procedure. Finally, semantic fusion is designed to provide semantic guidance only during the concrete phase of the reverse process, preventing semantic ambiguity and artifacts while maintaining the guidance information. Extensive experiments validate the effectiveness and efficiency of DIVER in improving classical distillation techniques and significantly improving cross-architecture generalization, requiring processing time comparable to raw DiT on ImageNet (256$\times$256) with only 4 GB of GPU memory usage. Code is available: this https URL.

---


### 26. [Runtime Monitoring of Perception-Based Autonomous Systems via Embedding Temporal Logic](https://arxiv.org/abs/2605.12651)

**<font color=#1a73e8>作者：</font>** Parv Kapoor, Abigail Hammer, Ashish Kapoor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Runtime monitoring of autonomous systems traditionally relies on mapping continuous sensor observations to discrete logical propositions defined over low-dimensional state variables. This abstraction breaks down in perception-driven settings, where such mappings require additional learned modules that are often computationally expensive, brittle, and semantically misaligned. In this work, we propose Embedding Temporal Logic (ETL), a temporal logic that performs monitoring directly in learned embedding spaces. ETL defines predicates through distances between observed embeddings and target embeddings derived from reference observations. This formulation allows specifications to capture high-level perceptual concepts, such as similarity to visual goals or avoidance of semantic regions, that are difficult or impossible to express using traditional predicates. By composing these predicates with temporal operators, ETL naturally expresses temporally extended and sequential perceptual behaviors. We introduce ETL monitors for evaluating specifications over bounded embedding traces, along with a conformal calibration procedure that provides reliable and safety-oriented predicate evaluation. We evaluate our approach across multiple manipulation environments to show that ETL achieves strong empirical agreement with ground-truth semantics, including accurate monitoring of temporally composed behaviors.

---


### 27. [Multi-Rollout On-Policy Distillation via Peer Successes and Failures](https://arxiv.org/abs/2605.12652)

**<font color=#1a73e8>作者：</font>** Weichen Yu, Xiaomin Li, Yizhou Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are often post-trained with sparse verifier rewards, which indicate whether a sampled trajectory succeeds but provide limited guidance about where reasoning succeeds or fails. On-policy distillation (OPD) offers denser token-level supervision by training on student-generated trajectories, yet existing methods typically distill each rollout independently and ignore the other attempts sampled for the same prompt. We introduce Multi-Rollout On-Policy Distillation (MOPD), a peer-conditioned distillation framework that uses the student's local rollout group to construct more informative teacher signals. MOPD conditions the teacher on both successful and failed peer rollouts: successes provide positive evidence for valid reasoning patterns, while failures provide structured negative evidence about plausible mistakes to avoid. We study two peer-context constructions: positive peer imitation and contrastive success-failure conditioning. Experiments on competitive programming, mathematical reasoning, scientific question answering, and tool-use benchmarks show that MOPD consistently improves over standard on-policy baselines. Further teacher-signal analysis shows that mixed success-failure contexts better align teacher scores with verifier rewards, indicating that the gains arise from more faithful, instance-adaptive supervision. These results indicate that effective on-policy distillation should exploit the student's multi-rollout trial-and-error behavior rather than treating rollouts as isolated samples.

---


### 28. [Plan Before You Trade: Inference-Time Optimization for RL Trading Agents](https://arxiv.org/abs/2605.12653)

**<font color=#1a73e8>作者：</font>** Eun Go, Rohan Deb, Arindam Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning agents for portfolio management are typically trained and deployed as static policies, with no mechanism for using price forecasts at inference time. We propose $\text{FPILOT}$ (**Fin**ancial **P**lugin **I**nference-time **L**earning for **O**ptimal **T**rading), a plugin inference-time optimization framework inspired by Model Predictive Control (MPC). Our key structural insight is that future prices mostly do not depend on one agent's portfolio allocation, so a suitable predictive model can produce a multi-step price trajectory without iterative action-conditioned rollouts as in typical reinforcement learning. At each decision step, we use the forecaster's predicted price trajectory to construct an allocation-based imagined return objective, and optimize the policy at inference-time before executing one step of the trade. Our framework is compatible with any pre-trained agent and adapts the policy to the forecaster's predictions without any retraining. Evaluated across five policy learning algorithms on the TradeMaster DJ30 benchmark, $\text{FPILOT}$ produces consistent improvements in total return and return-based risk-adjusted metrics (Sharpe, Sortino, Calmar), with stochastic policies benefiting more than deterministic ones. Further, using synthetic forecasts at calibrated quality levels, we show that gains consistently improve with forecaster quality, suggesting that our performance will improve based on advances in financial forecasting.

---


### 29. [Macro-Action Based Multi-Agent Instruction Following through Value Cancellation](https://arxiv.org/abs/2605.12655)

**<font color=#1a73e8>作者：</font>** Wo Wei Lin, Ethan Rathbun, Enrico Marchesini Xiang Zhi Tan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent reinforcement learning (MARL) in real-world use cases may need to adapt to external natural language instructions that interrupt ongoing behavior and conflict with long-horizon objectives. However, conditioning rewards on instructions introduces a fundamental failure mode as Bellman updates couple value estimates across instruction contexts, leading to inconsistent values when instructions interrupt macro-actions. We propose Macro-Action Value Correction for Instruction Compliance (MAVIC), which corrects Bellman backups at instruction boundaries by correcting the incoming instruction objective and restoring the continuation value under the current objective. Unlike reward shaping, MAVIC modifies the bootstrapping target itself, enabling consistent value estimation under stochastic instruction switching within a unified policy. We provide theoretical analysis and an actor-critic implementation, and show that MAVIC achieves high instruction compliance while preserving base task performance in increasingly complex cooperative multi-agent environments.

---


### 30. [scShapeBench: Discovering geometry from high dimensional scRNAseq data](https://arxiv.org/abs/2605.12662)

**<font color=#1a73e8>作者：</font>** Andrew J Steindl, João Felipe Rocha, Brian Tshilengi Di Bassinga 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional point cloud data arise across many scientific domains, especially single-cell biology. The shapes or topologies of these datasets determine the types of information that can be extracted. For example, clustered data supports cell-type identification, trajectory structures support transition analysis, and archetypal structures capture continua of cellular behaviors. Existing analysis pipelines often assume a specific shape. The standard Seurat pipeline combines UMAP visualization with Louvain clustering and therefore assumes clustered data, while tools such as Monocle and SPADE assume tree-like structures, and flow-based models such as MIOFlow and Conditional Flow Matching target trajectories. Choosing which pipeline to apply is therefore often left to bioinformaticians who visually inspect datasets before selecting an analysis strategy. With the rise of agentic AI scientists, automating shape detection is increasingly important for selecting downstream analysis pipelines. To address this problem, we introduce scShapeBench, a benchmark dataset for shape detection containing both synthetic and expert-annotated single-cell datasets. Synthetic datasets are sampled from ground-truth skeleton graphs with controlled variance. Real single-cell datasets are curated from diverse sources and annotated by experts into four categories: clusters, single trajectory, multi-branching, and archetypal. We additionally introduce scReebTower, a baseline method that uses diffusion geometry to extract Reeb graphs and connect visualization with pipeline selection. We provide topology-aware evaluation metrics and compare scReebTower against PAGA and Mapper on synthetic and real data. Our results indicate that scReebTower outperforms existing baselines. Overall, our contributions span benchmarks, evaluation metrics, and a baseline for automated shape detection in single-cell data.

---


### 31. [Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack](https://arxiv.org/abs/2605.12673)

**<font color=#1a73e8>作者：</font>** Hao Wang, Hanchen Li, Qiuyang Mang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent benchmarks have become the de facto measure of frontier AI competence, guiding model selection, investment, and deployment. However, reward hacking, where agents maximize a score without performing the intended task, emerges spontaneously in frontier models without overfitting. We argue that benchmarks must be secure by design. From past incidents of reward hacks, we derive a taxonomy of eight recurring flaw patterns and compile them into the Agent-Eval Checklist for benchmark designers. We condense the insights into BenchJack, an automated red-teaming system that drives coding agents to audit benchmarks and identify possible reward-hacking exploits in a clairvoyant manner. Moreover, we extend BenchJack to an iterative generative-adversarial pipeline that discovers new flaws and patches them iteratively to improve benchmark robustness. We apply BenchJack to 10 popular agent benchmarks spanning software engineering, web navigation, desktop computing, and terminal operations. BenchJack synthesizes reward-hacking exploits that achieve near-perfect scores on most of the benchmarks without solving a single task, surfacing 219 distinct flaws across the eight classes. Moreover, BenchJack's extended pipeline reduces the hackable-task ratio from near 100% to under 10% on four benchmarks without fatal design flaws, fully patching WebArena and OSWorld within three iterations. Our results show that evaluation pipelines have not internalized an adversarial mindset, and that proactive auditing could help close the security gap for the fast-paced benchmarking space.

---


### 32. [Revealing Interpretable Failure Modes of VLMs](https://arxiv.org/abs/2605.12674)

**<font color=#1a73e8>作者：</font>** Isha Chaudhary, Vedaant V Jain, Kavya Sachdeva 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are increasingly used in safety-critical applications because of their broad reasoning capabilities and ability to generalize with minimal task-specific engineering. Despite these advantages, they can exhibit catastrophic failures in specific real-world situations, constituting failure modes.
We introduce REVELIO, a framework for systematically uncovering interpretable failure modes in VLMs. We define a failure mode as a composition of interpretable, domain-relevant concepts-such as pedestrian proximity or adverse weather conditions-under which a target VLM consistently behaves incorrectly. Identifying such failures requires searching over an exponentially large discrete combinatorial space. To address this challenge, REVELIO combines two search procedures: a diversity-aware beam search that efficiently maps the failure landscape, and a Gaussian-process Thompson Sampling strategy that enables broader exploration of complex failure modes.
We apply REVELIO to autonomous driving and indoor robotics domains, uncovering previously unreported vulnerabilities in state-of-the-art VLMs. In driving environments, the models often demonstrate weak spatial grounding and fail to account for major obstructions, leading to recommendations that would result in simulated crashes. In indoor robotics tasks, VLMs either miss safety hazards or behave excessively conservatively, producing false alarms and reducing operational efficiency. By identifying structured and interpretable failure modes, REVELIO offers actionable insights that can support targeted VLM safety improvements.

---


### 33. [Parallel-in-Time Training of Recurrent Neural Networks for Dynamical Systems Reconstruction](https://arxiv.org/abs/2605.12683)

**<font color=#1a73e8>作者：</font>** Florian Hess, Florian Götz, Daniel Durstewitz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing nonlinear dynamical systems (DS) from data (DSR) is a fundamental challenge in science and engineering, but it inherently relies on sequential models. Recent breakthroughs for sequential models have produced algorithms that parallelize computation along sequence length $T$, achieving logarithmic time complexity, $\mathcal{O}(\log T)$. Since sequence lengths have been practically limited due to the linear runtime complexity $\mathcal{O}(T)$ of classical backpropagation through time, this opens new avenues for DSR. This paper studies two prominent classes of parallel-in-time algorithms for this task, both of which leverage parallel associative scans as their core computational primitive. The first class comprises models with linear yet non-autonomous dynamics and a nonlinear readout, such as modern State Space Models (SSMs), while the second consists of general nonlinear models which can be parallelized using the DEER framework. We find that the linear training-time recurrence of the first class of models imposes limitations that often hinder learning of accurate nonlinear dynamics. To address this, we augment DEER with Generalized Teacher Forcing (GTF), a novel variant within the more general nonlinear framework that ensures stable and effective learning of nonlinear dynamics across arbitrary sequence lengths. Using GTF-DEER, we investigate the benefits of training on extremely long sequences ($T>10^4$) for DSR. Our results show that access to such long trajectories significantly improves DSR if the data features long time scales. This work establishes GTF-DEER as a robust tool for data-driven discovery and underscores the largely untapped potential of long-sequence learning in modeling complex DS.

---


### 34. [A Unified Perspective for Learning Graph Representations Across Multi-Level Abstractions](https://arxiv.org/abs/2605.12685)

**<font color=#1a73e8>作者：</font>** Mohamed Mahmoud Amar, Nairouz Mrabah, Mohamed Bouguessa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Self-Supervised Learning (GSSL) has emerged as a powerful paradigm for generating high-quality representations for graph-structured data. While multi-scale graph contrastive learning has received increasing attention, many existing methods still predominantly focus on a single graph abstraction level. To address this limitation, we propose a unified contrastive framework that can target node-level, proximity-level, cluster-level, and graph-level information and integrate them through a linear combination of similarity scores on positive pairs and dissimilarity scores (i.e., similarity scores on negative pairs). Furthermore, current approaches typically assign uniform penalty strengths to all examples, which reduces optimization flexibility and leads to ambiguous convergence status. To overcome this, we introduce a novel parameter-free fine-grained self-weighting mechanism that adaptively assigns weights to individual similarity and dissimilarity scores. The proposed mechanism emphasizes the scores that deviate significantly from their target values. Our approach not only enhances optimization flexibility but also eliminates the computational overhead of hyperparameter tuning in conventional multi-task GSSL methods. Comprehensive experiments on real-world datasets show that our methods consistently outperform state-of-the-art approaches across downstream tasks, including classification, clustering, and link prediction, in both single-level and multi-level scenarios.

---


### 35. [On the Size Complexity and Decidability of First-Order Progression](https://arxiv.org/abs/2605.12691)

**<font color=#1a73e8>作者：</font>** Jens Classen, Daxin Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Progression, the task of updating a knowledge base to reflect action effects, generally requires second-order logic. Identifying first-order special cases, by restricting either the knowledge base or action effects, has long been a central topic in reasoning about actions. It is known that local-effect, normal, and acyclic actions, three increasingly expressive classes, admit first-order progression. However, a systematic analysis of the size of such progressions, crucial for practical applications, has been missing. In this paper, using the framework of Situation Calculus, we show that under reasonable assumptions, first-order progression for these action classes grows only polynomially. Moreover, we show that when the KB belongs to decidable fragments such as two-variable first-order logic or universal theories with constants, the progression remains within the same fragment, ensuring decidability and practical applicability.

---


### 36. [IGT-OMD: Implicit Gradient Transport for Decision-Focused Learning under Delayed Feedback](https://arxiv.org/abs/2605.12693)

**<font color=#1a73e8>作者：</font>** Benjamin Amoh, Geoffrey G. Parker, Wesley Marrero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-focused learning trains predictive models end-to-end against downstream decision loss, but online settings suffer delayed feedback: outcomes may not arrive for many environment interactions. We identify \emph{staleness amplification}, a failure mode unique to bilevel optimization under delay, in which gradient staleness couples with inner-solver sensitivity to inflate regret beyond single-level delay theory. We prove that any black-box delayed optimizer incurs an irreducible regret cost from inner-solver approximation error, and that gradient staleness contributes a quadratically growing transport error without bilevel-aware correction. Our algorithm, \textbf{IGT-OMD}, applies Implicit Gradient Transport to hypergradients within Online Mirror Descent, re-evaluating stale gradients at the current parameters using stored inner solutions. This method reduces transport error from a quadratic to a linear dependence on delay and achieves the first sublinear regret bound for delayed bilevel optimization with queue-length-adaptive step sizes. Controlled experiments provide a \emph{mechanistic fingerprint}: transport benefit is exactly $0.0\%$ ($p=1.00$) at unit delay and grows monotonically to $9.5\%$ at fifty rounds ($p<0.001$), isolating the correction's effect. On Linear Quadratic Regulator, Warcraft shortest-path, and Sinkhorn optimal transport, IGT-OMD reduces decision loss by $17$--$55\%$ relative to single-level baselines, with phase transitions matching the theory.

---


### 37. [Modeling Heterophily in Multiplex Graphs: An Adaptive Approach for Node Classification](https://arxiv.org/abs/2605.12699)

**<font color=#1a73e8>作者：</font>** Kamel Abdous, Nairouz Mrabah, Mohamed Bouguessa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing multiplex graph models often assume homophily, where connected nodes tend to belong to the same class or share similar attributes. Consequently, these models may struggle with graphs exhibiting heterophily, where connected nodes typically belong to different classes and have dissimilar attributes. While recent methods have been developed to learn reliable node representations from unidimensional graphs with heterophily, they do not fully address the complexities of multiplex graphs. In a multiplex graph, nodes are linked through multiple types of edges (referred to as dimensions), which can simultaneously exhibit homophilic and heterophilic interactions. To address this gap, we propose \methodname, a novel method for node classification in multiplex graphs that adapts to both homophilic and heterophilic dimensions. \methodname introduces dimension-specific compatibility matrices to model varying degrees of homophily and heterophily across dimensions. A key innovation is its use of a product of trainable low-pass and high-pass filters, approximated via Chebyshev polynomials, to capture both smooth and abrupt changes in the graph signal. By composing these filters and optimizing label predictions using a proximal-gradient method, \methodname dynamically adjusts to the heterophilic characteristics of each dimension. Extensive experiments on synthetic and real-world datasets provide evidence that \methodname captures the complex interplay of homophilic and heterophilic interactions in multiplex graphs, and tends to yield improved node classification performance compared to state-of-the-art methods.

---


### 38. [UFO: A Domain-Unification-Free Operator Framework for Generalized Operator Learning](https://arxiv.org/abs/2605.12700)

**<font color=#1a73e8>作者：</font>** Hanli Qiao, George Em Karniadakis, Muhammad Muniruzzaman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators have become an effective framework for learning mappings between function spaces, yet most existing architectures realize operators within a single representational domain, such as physical, spectral, or latent space. In this work, we introduce UFO (Domain-Unification-Free Operator), a cross-domain neural operator framework that realizes operators through adaptive, jointly conditioned interactions among representations defined on distinct domains. UFO enables discretization decoupling: the input function can be observed at resolutions or locations different from those used during training, while the solution can be queried at arbitrary output resolutions. Across four complementary benchmarks covering discontinuous inputs, irregular sampling with spectral mismatch, nonlinear dynamics, and stochastic high-frequency fields, UFO delivers accurate, robust, and physically coherent predictions under distribution shifts. These results establish cross-domain, phase-modulated realization as a powerful framework for discretization-decoupled neural operator learning.

---


### 39. [Do Fair Models Reason Fairly? Counterfactual Explanation Consistency for Procedural Fairness in Credit Decisions](https://arxiv.org/abs/2605.12701)

**<font color=#1a73e8>作者：</font>** Gideon Popoola, John Sheppard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning algorithms in socially sensitive domains (e.g., credit decisions) often focus on equalizing predictive outcomes. However, satisfying these metrics does not guarantee that models use the same reasoning for different groups. We show that existing outcome-fair models can still apply fundamentally different reasoning to individuals, a ``hidden procedural bias'' missed by standard fairness metrics and algorithms. We propose Counterfactual Explanation Consistency (CEC), a framework that detects and mitigates this bias by aligning feature attributions between individuals and their counterfactual counterparts. Key contributions include a nearest-neighbor counterfactual generation method, a modified baseline for integrated gradient comparisons, an individual-level procedural fairness metric, and a corresponding training loss. We introduce a taxonomy identifying ``Regime B'' (same outcome, different reasoning) as a critical blind spot. Experiments on synthetic data, German Credit, Adult Income, and HMDA mortgage data demonstrate that outcome-fair baselines exhibit substantial hidden bias, while CEC substantially reduces it with modest utility cost.

---


### 40. [A Resampling-Based Framework for Network Structure Learning in High-Dimensional Data](https://arxiv.org/abs/2605.12706)

**<font color=#1a73e8>作者：</font>** Ziwei Huang, Zeyuan Song, Paola Sebastiani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RSNet is an open-source R package that provides a resampling-based framework for robust and interpretable network inference, designed to address the limited-sample-size challenges common in high-dimensional data. It supports both the estimation of partial correlation networks modeled as Gaussian networks and conditional Gaussian Bayesian networks for mixed data types that combine continuous and discrete variables. The framework incorporates multiple resampling strategies, including bootstrap, subsampling, and cluster-based approaches, to accommodate both independent and correlated observations. To enhance interpretability, RSNet integrates graphlet-based topology analysis that captures higher-order connectivity and edge sign information, enabling single-node and subnetwork-level insights. Notably, RSNet is the first R package to efficiently construct signed graphlet degree vector matrices (GDVMs) in near-constant time for sparse networks, providing scalable analysis of higher-order network structure. Collectively, RSNet offers a versatile tool for statistically reliable and interpretable network inference in high-dimensional data.

---


### 41. [Spectral Energy Centroid: a Metric for Improving Performance and Analyzing Spectral Bias in Implicit Neural Representations](https://arxiv.org/abs/2605.12709)

**<font color=#1a73e8>作者：</font>** Tomasz Dądela, Adam Kania, Maciej Rut 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Implicit Neural Representations (INRs) model continuous signals using multilayer perceptrons (MLPs), enabling compact, differentiable, and high-fidelity representations of data across diverse domains. However, due to the low-frequency bias of MLPs that prevents effective learning of small details, the model's frequency must be carefully tuned through the embedding layer. Prior work established that this tuning can be performed before training based on the target signal, but it did not account for the significant effect of model depth, indicating that our understanding of the relationship between frequency and INR performance remains limited. To gain insights into this relationship, we utilize the Spectral Energy Centroid (SEC) metric that quantifies the frequency of target images and the spectral bias of INR models. We show that SEC is a versatile tool for INR analysis, demonstrating its utility across three tasks: (1) a data-driven strategy (SEC-Conf) for hyperparameter selection that outperforms existing heuristics and is robust to model depth, (2) a reliable proxy for signal complexity, and (3) effective alignment of spectral biases across diverse INR architectures.

---


### 42. [Scaling Laws for Mixture Pretraining Under Data Constraints](https://arxiv.org/abs/2605.12715)

**<font color=#1a73e8>作者：</font>** Anastasiia Sedova, Skyler Seto, Natalie Schluter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As language models scale, the amount of data they require grows -- yet many target data sources, such as low-resource languages or specialized domains, are inherently limited in size. A common strategy is to mix this scarce but valuable target data with abundant generic data, which presents a fundamental trade-off: too little target data in the mixture underexposes the model to the target domain, while too much target data repeats the same examples excessively, yielding diminishing returns and eventual overfitting. We study this trade-off across more than 2,000 language-model training runs spanning multiple model and target dataset sizes, as well as several data types, including multilingual, domain-specific, and quality-filtered mixtures. Across all settings, we find that repetition is a central driver of target-domain performance, and that mixture training tolerates much higher repetition than single-source training: scarce target corpora can be reused 15-20 times, with the optimal number of repetitions depending on the target data size, compute budget, and model scale. Next, we introduce a repetition-aware mixture scaling law that accounts for the decreasing value of repeated target tokens and the regularizing role of generic data. Optimizing the scaling law provides a principled way to compute effective mixture configurations, yielding practical mixture recommendations for pretraining under data constraints.

---


### 43. [Inline Critic Steers Image Editing](https://arxiv.org/abs/2605.12724)

**<font color=#1a73e8>作者：</font>** Weitai Kang, Xiaohang Zhan, Yizhou Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based image editing exhibits heterogeneous difficulty not only across cases but also across regions of an image, motivating refinement approaches that allocate correction to where the model struggles. Existing refinement signals arrive late, after a fully generated image or a completed denoising step. We ask whether such a signal can act within an ongoing forward pass. To investigate this, we probe a frozen image-editing model and find that although generation capability emerges only in the last few layers, the error pattern is already set in early layers (rank correlation \r{ho} = 0.83 with the final-layer error map). Based on this, we introduce Inline Critic, a learnable token that critiques a frozen model's predictions at its intermediate layers and steers its hidden states to refine generation during the forward pass. A three-stage recipe is proposed to stabilize the training from learning how to critique to steering generation. As a result, we achieve state of the art on GEdit-Bench (7.89), a +9.4 gain on RISEBench over the same backbone, and the strongest open-source result on KRIS-Bench (81.92, surpassing GPT-4o). We further provide analyses showing that the critic genuinely shapes the model's attention and prediction updates at subsequent layers.

---


### 44. [Before the Last Token: Diagnosing Final-Token Safety Probe Failures](https://arxiv.org/abs/2605.12726)

**<font color=#1a73e8>作者：</font>** Shravan Doda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Final-token safety probes monitor a single hidden state after prompt prefill, but jailbreak prompts can contain probe-visible unsafe evidence distributed across earlier user-token representations that is missed by this readout. We study this prefill-time failure mode using SafeSwitch-style probes trained only on clean harmful and benign prompts across three instruction-tuned LLMs. The probes achieve high recall on clean harmful prompts, but miss many jailbreaks and can produce false positives on safety-adjacent benign prompts. Subspace analyses suggest that missed jailbreaks differ from clean benign prompts along directions that are poorly captured by the probe's representational subspace, and increasing probe bottleneck width does not reliably resolve this mismatch. Token-level prefill analyses reveal that probe-visible unsafe evidence often appears earlier in the sequence but is not exposed at the final-token readout, while naive max-pooling over token positions overfires on safe prompts. A simple PCA-HMM trajectory model, trained only on the same clean split, recovers many final-token misses from user-content prefill trajectories without the catastrophic false-positive behavior of naive token pooling, motivating trajectory-aware hidden-state analyses as diagnostic complements to final-token probes

---


### 45. [BEHAVE: A Hybrid AI Framework for Real-Time Modeling of Collective Human Dynamics](https://arxiv.org/abs/2605.12730)

**<font color=#1a73e8>作者：</font>** Helene Malyutina  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing AI systems for modeling human behavior operate at the level of individuals or detect events after they occur. As a result, they systematically fail to capture the collective dynamics that determine whether a group remains stable or transitions into escalation or breakdown. We propose a different foundation: a group of interacting humans constitutes a complex dynamical system in the precise mathematical sense, exhibiting emergence, nonlinearity, feedback loops, sensitivity near critical points, and phase transitions between qualitatively distinct regimes. The state of such a system is not located within any single participant; it is distributed across mutual influence loops and observable through the micro-dynamics of the body.
We introduce BEHAVE (Behavioral Engine for Human Activity Vector Estimation), a formal framework that models collective dynamics as continuous behavioral fields defined over an interaction space derived from observable physical signals. Kinematic micro-signals (position, velocity, body orientation, gestural activity) are structured into a directed interaction graph and aggregated into a basis of behavioral fields capturing distinct, non-redundant axes of collective state. The framework rests on one theorem and two structural propositions characterizing the tension field, the field basis, and the criticality index. Perception and forecasting layers are implemented using neural models, enabling data-driven learning and approximation of system dynamics. BEHAVE is formulated as a computational system for learning, representing, and forecasting collective dynamics from data. A working pipeline is demonstrated on a 7-agent negotiation snapshot. The same fields, recalibrated, apply to crowd safety, crisis-team dynamics, education, and clinical contexts.

---


### 46. [From Generalist to Specialist Representation](https://arxiv.org/abs/2605.12733)

**<font color=#1a73e8>作者：</font>** Yujia Zheng, Fan Feng, Yuke Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given a generalist model, learning a task-relevant specialist representation is fundamental for downstream applications. Identifiability, the asymptotic guarantee of recovering the ground-truth representation, is critical because it sets the ultimate limit of any model, even with infinite data and computation. We study this problem in a completely nonparametric setting, without relying on interventions, parametric forms, or structural constraints. We first prove that the structure between time steps and tasks is identifiable in a fully unsupervised manner, even when sequences lack strict temporal dependence and may exhibit disconnections, and task assignments can follow arbitrarily complex and interleaving structures. We then prove that, within each time step, the task-relevant latent representation can be disentangled from the irrelevant part under a simple sparsity regularization, without any additional information or parametric constraints. Together, these results establish a hierarchical foundation: task structure is identifiable across time steps, and task-relevant latent representations are identifiable within each step. To our knowledge, each result provides a first general nonparametric identifiability guarantee, and together they mark a step toward provably moving from generalist to specialist models.

---


### 47. [ConRetroBert: EMA Stabilized Dual Encoders for Template-Based Single-Step Retrosynthesis](https://arxiv.org/abs/2605.12736)

**<font color=#1a73e8>作者：</font>** Mohammad Jahid Ibna Basher, Ali Khodabandeh Yalabadi, Ivan Garibay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Template based single step retrosynthesis predicts reactants by selecting and applying an explicit reaction template, making each prediction traceable to a chemical transformation rule. This is useful for synthesis planning, but template based methods are often viewed as less competitive than template free models because template prediction is commonly formulated as global classification over a long tailed rule library. We argue that this weakness is not inherent to templates, but to the learning formulation. We present ConRetroBert, a dual encoder framework that reframes template based retrosynthesis as dense product template retrieval followed by candidate set listwise ranking. Stage 1 uses contrastive pretraining to learn a shared embedding space between products and reaction templates. Stage 2 refines template ranking over mined hard negative candidate sets with a multi positive listwise objective. To enable template side adaptation without destabilizing hard negative mining, ConRetroBert uses a slow moving exponential moving average template encoder for retrieval bank construction while updating the live template encoder through the ranking loss. On the local USPTO-50k benchmark, Stage 2 candidate set ranking improves top-1 reaction accuracy from 50.5% to 61.3%, while EMA stabilized template adaptation further improves it to 62.4%. Fine tuning from a leakage controlled USPTO-Full checkpoint reaches 75.4% top-1 accuracy on USPTO-50k. We also show that retrieval based template prediction is strong in the long tail of rare templates, and that many correct reactant predictions arise from alternative explicit templates rather than only the recorded positive label. Code and data are available at this https URL.

---


### 48. [Quieting the Cobwebs: Browser Interaction for Visual Floaters](https://arxiv.org/abs/2605.12739)

**<font color=#1a73e8>作者：</font>** Kenneth Ge, Jinglin Li, Shikhar Ahuja  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Floaters, cobweb-like shadows that move around a person's visual field, impair vision for nearly 33% of the population, yet have limited treatment options. Floaters especially harm screen use, since they reduce contrast, introduce clutter, and add moving distractions. While existing high-contrast tools offer some help, few address the motion that makes screen use with floaters uniquely difficult. In this paper, we build a floater simulation inspired by the physics of the eye, use it to quantitatively assess text readability at varying levels of motion, and build a novel web extension that minimizes eye movement, maximizing the signal-to-noise ratio of performing browser tasks. Importantly, our tool works not only for text, but for all UI elements, requiring no modifications to existing websites.

---


### 49. [Still Camouflage, Moving Illusion: View-Induced Trajectory Manipulation in Autonomous Driving](https://arxiv.org/abs/2605.12743)

**<font color=#1a73e8>作者：</font>** Shuo Ju, Qingzhao Zhang, Huashan Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing physical adversarial attacks on vision-based autonomous driving induce time-evolving perception errors, including biased object tracking or trajectory prediction, through (i) sophisticated physical patch inducing detection box drift when entering the view distance, or (ii) dynamically changing patches that cause different perception errors at different time. In both cases, viewing-angle variation is treated as a challenge, requiring adversarial patches to remain effective across frames under varying views, leading to complex multi-view optimization. In contrast, we show that viewing-angle variation itself can be turned into an attack tool. We design a new attack paradigm where a static, passive adversarial camouflage is mounted on a vehicle whose view-dependent appearance naturally evolves with relative motion, inducing consistent feature drift across frames. This causes the system to infer a physically plausible but incorrect trajectory, such as a false cut-in, which propagates to downstream decision-making and triggers unnecessary braking. Unlike prior approaches that require multi-view robustness or active intervention, our attack emerges from normal driving dynamics and is easy to deploy: a parked vehicle with a natural camouflage can induce hard braking in passing autonomous vehicles. We demonstrate the novel attack on nuScenes dataset, showing the effectiveness with an end-to-end success rate of up to 87.5%, measured by hard-braking events, and robustness across different scene backgrounds, victim vehicle speeds, and perception models.

---


### 50. [What Do You Think I Think? Accounting for Human Beliefs Using Second-Order Theory of Mind](https://arxiv.org/abs/2605.12745)

**<font color=#1a73e8>作者：</font>** Patrick Callaghan, Reid Simmons, Henny Admoni  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Discrepancies between an agent's actual knowledge and what a person thinks the agent knows can hinder interactions. If an agent could detect such discrepancies, it could provide feedback to account for them and improve current and future interactions. Using the I-POMDP as a framework for a second-order Theory of Mind (ToM-2), this work endows an agent with the ability to model the evolution of a person's erroneous beliefs about an agent and the cognitive biases and heuristics (CBH) from which they arise. In doing so, the agent can detect when CBH might be at play during an interaction and adaptively generate feedback that accounts for them. An in-person user study shows how a ToM-2 learner can account for the effects of a teacher's CBH to significantly improve the informativeness of teacher actions, and subjective results suggest people find the ToM-2 learner's feedback more useful.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-328](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
