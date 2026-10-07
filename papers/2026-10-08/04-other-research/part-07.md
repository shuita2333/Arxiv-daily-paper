# 📦 其他研究 | 2026年10月08日

> 本类共 **335** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-335**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-335**

---

### 301. [Random Feature Gaussian Process Attention: Linear-Time Probabilistic Attention with Calibrated Uncertainty](https://arxiv.org/abs/2610.08578)

**<font color=#1a73e8>作者：</font>** Amir Mohammad Mahfoozi, Zi Yang, Ying Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers provide a state-of-the-art modeling framework, yet poor calibration limits their reliability in safety-critical applications. A promising direction addresses this issue by interpreting attention as a Gaussian process (GP) posterior, which enables principled uncertainty calibration but incurs cubic complexity in sequence length due to the inversion of the kernel; although decoupled GP variants reduced the cost to quadratic, the computation remains prohibitive in practice. In this paper, we propose the plug-and-play random Fourier feature Gaussian process attention (RFF-GPA) module, which represents the attention as a GP with a stationary kernel approximated by random Fourier features. This low-rank approximation results in linear-time complexity for approximating the posterior mean and variance, making it far more scalable compared to previous work. Empirical results on multiple real-world datasets show that our attention module improves calibration while maintaining predictive accuracy, and simultaneously reduces computational complexity to linear in the sequence length.

---


### 302. [TwinViT-DeepJSCC: Adversarially Robust Semantic Image Communication](https://arxiv.org/abs/2610.08590)

**<font color=#1a73e8>作者：</font>** Maedeh Fallahreyhani, Paeiz Azmi, Nader Mokari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Learning-based semantic communication is vulnerable to adversarial perturbations introduced before semantic encoding or over wireless channels. This paper proposes TwinViT-DeepJSCC, a preventive-corrective semantic image transceiver operating under a fixed channel-use budget. Two Vision Transformer (ViT)-based deep joint source-channel coding (DeepJSCC) branches learn complementary latent representations protected by sensitivity-aware masking. At the receiver, confidence-aware fusion, blind corruption-severity estimation, and signal-to-noise ratio (SNR)-severity-conditioned denoising diffusion implicit model (DDIM) purification mitigate residual corruption without requiring attack metadata. Experiments on the Canadian Institute for Advanced Research 100-class (CIFAR-100) dataset consider fast gradient sign method (FGSM), projected gradient descent (PGD), natural evolution strategies (NES), and Carlini-Wagner (CW) source-domain attacks, as well as random jamming and channel-aware adversarial waveforms over additive white Gaussian noise (AWGN) and block-flat Rayleigh fading. Under matched channel-use and attack budgets, TwinViT-DeepJSCC achieves maximum peak signal-to-noise ratio (PSNR) gains of approximately 9.5 dB under 20-step PGD and 10.8 dB under channel-aware waveform attacks over block-flat Rayleigh fading. Under PGD, it also improves Top-1 accuracy by up to approximately 38 percentage points over the undefended baseline and 13 percentage points over the strongest competing defense. Ablation results confirm the complementary contributions of the proposed transmitter- and receiver-side mechanisms.

---


### 303. [CNet: A Complex-Valued Deep Learning Framework with Wirtinger Autodifferentiation and FFT--Hadamard Convolution](https://arxiv.org/abs/2610.08592)

**<font color=#1a73e8>作者：</font>** Marcel Crasmaru  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> CNet is a C++/CUDA framework for building and training deep complex-valued neural networks (CVNNs) and, more generally, for optimizing complex-valued functions by gradient descent with Wirtinger (CR-calculus) derivatives. It takes a physics-native stance: a network is a cascade of complex -- and often unitary (the DFT) -- operations acting on an amplitude vector, and classification is a Born-rule measurement $p_k = |z_k|^2 / \|z\|^2$ rather than a softmax over real logits. Every layer ships a CPU reference and a CUDA kernel checked against finite differences, and the computation graph is cloned across the batch for GPU execution. On top of the base layers we add signal-processing primitives that turn the identity conv(x,k) = IFFT(FFT(x) . FFT(k)) into a learnable complex convolutional network, together with a true-Adam optimizer and a reduced-memory inference mode.
We report three studies. First, a fully complex-valued, FNet-style causal sequence model built on a new $O(N \log N)$ causal Fourier mixer -- a triangular-masked DFT evaluated by a Bluestein / chirp-z factorization: once properly tuned it matches or exceeds a parameter-matched real-valued causal FNet on character-level language modeling, reaching the real model's converged quality in under half the training steps. Second and third, bottleneck analyses on radio-modulation classification (RML2016.10a) and the Fourier phase problem of coherent-diffraction imaging, which isolate exactly where complex-valued networks still need new operators. Across all three the complex formulation provably learns the physically correct structure.
Code: this https URL

---


### 304. [Multi-Label Perceptual Bug Detection in Video Games using Deep Learning on Gameplay Footage](https://arxiv.org/abs/2610.08593)

**<font color=#1a73e8>作者：</font>** Nahian Rifaat, Felix Morosov, Loutfouz Zaman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional approaches for automated bug detection in video games, such as manual testing, can be beneficial for the improvement of quality assurance, but they can be expensive and time-consuming. The scarce number of tools available to detect multiple perceptual bugs in the same video frame introduces detection challenges for automated bug detection tools in real-world scenarios. We propose a deep learning model for multi-label perceptual bug detection and compare it against video classification models such as Inflated 3D ConvNet and 3D ResNet. Our proposed model, ResNet-BiLSTM, achieved an F1 score of 85.78% on the benchmark dataset. Our results demonstrated that temporal dependency modelling is beneficial for accurate video-based bug detection. We believe this work with multi-label perceptual bug detection on gameplay videos will help save resources spent on manual testing workloads in video games. Furthermore, we introduce a new dataset with multi-label perceptual bugs in this work. The dataset contains 77,969 video clips across different genres of games with approximately 1.2 million frames, containing combinations from 5 classes of bugs in the same video frame.

---


### 305. [A Space-Agnostic Visual Game Analytics Tool with Adaptive Spatial Reconstruction for Mixed Reality Game Development](https://arxiv.org/abs/2610.08619)

**<font color=#1a73e8>作者：</font>** Nahian Rifaat, Fedir Skliar, Parisa Sargolzaei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent years have seen an increasing need for MR tools for game development and visual game analytics. However, the number of visual game analytics tools for MR games remains scarce due to the unique complexities in integrating real components from both the physical and the digital worlds in MR games. Existing visual analytics tools for such games are not suitable for space-agnostic generalization. To tackle this problem, we introduce a space-agnostic visual game analytics tool that incorporates adaptive spatial reconstruction and real-time object detection built for the Microsoft HoloLens 2 MR headset. We believe that the outcomes of our work will increase insights into player environment and pave a new direction for visual game analytics for MR game development.

---


### 306. [Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game Harness](https://arxiv.org/abs/2610.08621)

**<font color=#1a73e8>作者：</font>** Jiajun Chen, Haoyu Wu, Mingda Jia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent game design agents have made substantial progress in generating playable games. However, program correctness does not ensure an enjoyable experience for players. We present Recursive Game Creator, an experience-oriented harness to advance agentic game development from rough game prototypes into entertaining games. Recursive Game Creator organizes recursive development around four components: Designer, Builder, Player, and Reviewer. The Designer translates user instructions and Reviewer's feedback into detailed plans. The Builder turns these plans into candidate games. The coding-native Player creates and executes reusable policies through programmatic interfaces to efficiently collect diverse gameplay trajectories, mitigating evaluation bias caused by slow GUI-based collection. The Reviewer uses carefully designed trajectory-based metrics to induce player preferences, integrating with visual evidence and explicit textual preferences to evaluate games against game-specific criteria. Finally, the Reviewer accepts the better version and provides improvement reviews for the next round, closing the recursive loop. Our method achieves state-of-the-art overall performance of 77.89 on GameCraft-Bench. On GameASG-Bench, it achieves a strict task success rate of 53.2%, a 34.1% improvement over the same-model baseline, and the highest mean runtime-check pass rate at 93.4% among compared methods. A user study shows longer playtime and higher ratings. Code is coming soon.

---


### 307. [Early Memory Selection for Balanced Adam](https://arxiv.org/abs/2610.08624)

**<font color=#1a73e8>作者：</font>** Alberto Fernández-Hernández, Cristian Pérez-Corral, Jose I. Mestre 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a method for choosing the shared memory parameter $\beta_1=\beta_2=\beta$ in Adam from a short pilot training. The selected $\beta$ remains fixed during the subsequent full training. A local model of Adam's normalized direction balances sampling variability against the delay introduced by averaging past gradients. This balance gives a cubic memory rule, whose two coefficients are estimated from gradient probes at a few pilot checkpoints. The estimator uses the numerator and denominator jointly, preserving their covariance. With a 200-update pilot and sixteen probe gradients at each of four checkpoints, a seed-matched retrospective evaluation on eleven vision and language workloads reduces mean relative validation gap by 40.7% and worst-quarter mean gap by 44.3% against the grid representative of shared $\beta=0.95$. The mean gap is also 32.3% lower than that of the best constant $\beta$ chosen across all eleven workloads.

---


### 308. [Parallel Predictive World Models for Accurate and Efficient Long-Horizon Planning](https://arxiv.org/abs/2610.08627)

**<font color=#1a73e8>作者：</font>** Wanjin Feng, Baobin Zhang, Ao Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon world-model planning typically relies on autoregressive rollouts, where predicted states are repeatedly fed back into the model. This preserves temporal structure but creates a horizon-length sequential path and exposes later predictions to recursive decoded-state feedback. We introduce Parallel Predictive World Models (PPWM), which predict a finite-horizon trajectory in parallel while retaining causal interaction among future representations. Each horizon is conditioned on its causal action prefix, and future representations interact before decoding, separating temporal causality from state-by-state output recursion. We formalize this distinction by viewing autoregressive rollout as a causal trajectory map and identifying the decoded-state feedback pathway removed by PPWM. Across four visual-control tasks, PPWM achieves the lowest long-horizon prediction error and the highest Cross-Entropy Method (CEM) simulator success among the evaluated predictive interfaces. Meanwhile, PPWM achieves more than a 3$\times$ average CEM planning speedup over the autoregressive LeWM baseline. These results suggest that accurate and efficient long-horizon world-model planning does not require state-by-state autoregression, but can instead be achieved through parallel causal trajectory prediction.

---


### 309. [Forensic Reserve: Eliciting Latent Knowledge for Image Forgery Detection](https://arxiv.org/abs/2610.08639)

**<font color=#1a73e8>作者：</font>** Jiahua Li, Zixu John, Tom Zhong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As generated images become increasingly realistic, reliable forgery detection is essential for maintaining trust in visual information. However, existing methods primarily rely on task-specific supervision to adapt vision foundation model representations, without fully exploiting internal forensic knowledge to guide detection. To address this limitation, we propose Reserve-Guided Elicitation (RGE), a framework that treats sparse, origin-sensitive internal components in pretrained models as a forensic reserve and translates their localization into structural constraints for lightweight adaptation. Specifically, we first use the Forensic Lens (F-lens) to decompose activations across layers and token groups into independent components and globally screen them by their response differences between real and generated images, identifying reserve sites and directions. Next, we map the selected directions back to hidden-state space to construct fixed reserve subspaces and insert Forensic Reserve Adapters (FRA) only at the identified sites. Finally, with the backbone parameters, previously fitted reference classifier, and subspace bases fixed, we train only the FRA coefficient maps to generate input-dependent residual updates constrained to the corresponding subspaces, strengthening existing forensic responses. Using only 500 labeled training images and a trainable parameter budget below 0.2% of the backbone, RGE achieves competitive performance across three detection benchmarks without target-benchmark adaptation. Furthermore, RGE consistently improves over the corresponding frozen detectors across eight encoders spanning self-supervised and vision-language pretraining, eliciting a latent forensic capacity broadly shared across pretrained vision models.

---


### 310. [Knowing When to Trust a Prior: Reliability-Gated Cue Fusion for Video Gaze Prediction](https://arxiv.org/abs/2610.08663)

**<font color=#1a73e8>作者：</font>** Lichen Zhu, Yueqian Lin, Yiheng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video gaze prediction is led by gaze-trained models, yet gaze-free priors carry signal those models have not absorbed, if one knows when to trust them. We propose FocusGate, a gated ensemble of gaze-free priors whose members may abstain. A per-frame gate reads three shape statistics of a defocus map and selects the frames on which the estimator is above chance on average, so rejected frames reduce to the base exactly, while midrank normalisation lets an all-zero prior abstain at zero parameters. Gated fusion is significantly positive on film, sports and web video, whereas unconditional fusion is harmful on sports and null on web. Added to four supervised predictors, the NTIRE 2026 champion among them, FocusGate improves all sixteen model-domain cells in shuffled AUC, fifteen significantly, one domain pre-registered and scored once, while adding only 1% to the champion's latency. Alone, it surpasses TASED-Net and UNISAL in shuffled AUC on film with a 16-frame causal mean.

---


### 311. [MemFLoRA: Memory-Floor LoRA for CNN Adaptation at the Edge](https://arxiv.org/abs/2610.08669)

**<font color=#1a73e8>作者：</font>** Mehmet Emre Akbulut, Johannes Geier, Ulf Schlichtmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device learning is necessary when the model encounters user-,sensor-, or environment-specific shifts after deployment. Although parameter-efficient fine-tuning (PEFT) methods, particularly Low-Rank Adaptation (LoRA) variants, enable efficient adaptation at the edge, the limiting resource for Convolutional Neural Network (CNN) adaptation is often not the number of trainable parameters but the activation state that must be retained until the backward pass. This paper introduces Memory-Floor LoRA (MemFLoRA), a low-rank CNN adapter built around a memory-first design principle rather than a direct application of transformer-oriented LoRA. Instead of merely reducing trainable weights, we define an activation-memory-floor criterion: trainable backward computations must not depend on full-width layer inputs. The resulting adapter freezes the down-projection, trains a scale-matched up-projection, and combines eval-mode backbone normalization with activation-minimal backward rules, reducing saved state to the low-rank branch. Evaluated on three Human Activity Recognition (HAR) datasets and two CNN backbones under subject, body-location, and sensor-placement shifts, MemFLoRA reduces saved-activation memory by 98.5-98.7% and peak training-state memory by 94.9-97.3% relative to full fine-tuning, while matching or exceeding CNN PEFT baselines.

---


### 312. [PDB: Point-Based Deformation Blending for Facial Animation Retargeting](https://arxiv.org/abs/2610.08672)

**<font color=#1a73e8>作者：</font>** Sihun Cha, Hyeonseung Shin, Suah Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mesh-agnostic facial animation retargeting transfers expressions across meshes with different structures, but preserving facial motion without surface artifacts remains challenging. To address this, we present PDB, Point-Based Deformation Blending for facial animation retargeting. PDB predicts a compact set of deformed control points from a source neutral-expression pair and blending weights from the target neutral mesh. The weights are computed once per target and reused across frames, while the control points vary with each source expression. ReLU enforces non-negative weights and permits exact zeros, followed by row-wise normalization. The target mesh is reconstructed directly by multiplying the weights and control points, without a predefined cage, precomputed coordinates, a learned per-element deformation decoder, or a global reconstruction solve. Trained only with self-retargeting reconstruction supervision, PDB supports cross-identity transfer without paired cross-identity training expressions. Experiments demonstrate accurate retargeting, fast inference, and localized support in the learned weights. Joint evaluation of expression accuracy and local surface preservation shows reduced surface artifacts relative to the evaluated dense displacement method while retaining the intended motion. Perceptual evaluations further support expression fidelity and visual quality in both self- and cross-retargeting.

---


### 313. [Variance-Optimal Off-Policy Evaluation with Conjunct Effect Modeling](https://arxiv.org/abs/2610.08677)

**<font color=#1a73e8>作者：</font>** Nicolò Felicioni, Michael Benigni, Maurizio Ferrari Dacrema 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-policy evaluation (OPE) for contextual bandit policies becomes challenging when action-level importance weighting incurs excessive variance. Doubly robust (DR) estimation remains unbiased under common support but retains these high-variance action-level weights. A prior estimator, Off-policy evaluation with Conjunct Effect Model (OffCEM), replaces them with more stable cluster-level weights, at the cost of relying on local correctness of the reward model. In this paper, we show that, under the assumptions required by DR and OffCEM, there exists an unbiased family of estimators that interpolates between OffCEM and DR. Building on this result, we propose the Variance Optimal-CEM (VOCEM) estimator, which selects the interpolation coefficient to minimize variance. We derive the population-optimal coefficient in closed form and show that the resulting estimator has variance no larger than either endpoint, OffCEM or DR. Experiments in controlled synthetic settings and on two large-action benchmarks show that VOCEM improves upon both endpoints in all 23 evaluated conditions, exhibiting greater stability and empirical robustness.

---


### 314. [Juicy Interactive Visualization: Evaluating How Excessive Feedback Design Shapes Visualization Engagement](https://arxiv.org/abs/2610.08681)

**<font color=#1a73e8>作者：</font>** Shano Liang, Max Chen, Lane Harrison  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visualization research has long examined embellishment and animation, while the design of rich interaction-contingent feedback remains under-articulated as a systematic design space. We introduce JuicyVIS, a theory-informed operationalization of juicy feedback for interactive visualization that translates ideas from game studies into a visualization-centered framework. JuicyVIS introduces three dimensions, interaction type, feedback timing, and feedback intensity, which we explore through 26 controlled prototypes, grounded in established visualization interaction categories and prior work on juicy feedback in games. We evaluate the juicy design space through three exploratory mixed-methods online studies. Results show that juicy feedback was consistently associated with higher engagement and aesthetic experience, while the clearest gains came from post-interaction feedback, not, for example, by simply increasing intensity. We discuss how juicy feedback can be thought of as a design material in visualizations, shaping how visualization interactions feel, how action consequences are perceived, and how users remain engaged with data representations.

---


### 315. [Coupled but Late: Turn-Taking Between Full-Duplex Speech Models in Unscripted Dialogue](https://arxiv.org/abs/2610.08683)

**<font color=#1a73e8>作者：</font>** Lichen Zhu, Yueqian Lin, Yiheng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-duplex speech models are trained to converse with a person, but they are increasingly made to converse with each other, in self-play data generation, agent societies, and model-based evaluation. In that loop no human absorbs a timing error: each model's turn-taking is the other's input. We ask what timing the loop settles into. Two PersonaPlex-7B instances exchange audio tokens on a shared clock in unscripted conversation, and one floor-transfer rule is applied to them and to Switchboard. Their timing is coupled: re-pairing speakers across conversations destroys it. But the floor changes hands late, at a median of 400-560 ms against 137 ms for humans, and the last 120 ms of the partner's turn, where human projection places a tenth of its transfers, holds 1% of theirs. Delaying one direction of the channel shifts the response one-for-one and leaves the run-up to it empty, consistent with a reactive wait after the perceived end rather than the turn-end projection human timing requires.

---


### 316. [RenderBench: Benchmarking Render-to-Real Video Transfer with Reconstructed Digital Twins](https://arxiv.org/abs/2610.08684)

**<font color=#1a73e8>作者：</font>** Dicong Qiu, Zhiyuan Xu, Yaosheng Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video models can generate realistic videos from real appearance references and proxy renders that specify scene structure, viewpoint changes, and motion. Evaluating this render-to-real capability requires a real target video depicting the same scene evolution, paired with an editable, geometrically registered 3D replica. Such data has traditionally required substantial manual modeling, calibration, and animation effort. We introduce RenderBench, a benchmark of 12 reconstructed real-world scenes spanning large-scale indoor environments and egocentric viewpoints, with both static and dynamic settings. Our construction pipeline combines visual geometry, neural reconstruction, and assisted 3D authoring. Each scene is decomposed into static objects and dynamic actors, registered to the capture cameras, and accepted only after multi-view geometric and temporal validation. Each evaluation unit contains appearance reference images, a held-out real target video, an editable digital twin, a matched proxy render, and renderer-native scene annotations. We evaluate transfer models against paired real target videos, retain PAI-Bench-C-compatible structural projections, and use scene annotations to localize failures by object, visibility, articulation, and motion. The first release retains 12 of 14 registered samples (85.7%), comprising 1,496 paired real-proxy frames. All released scenes pass file-integrity and environment-edit audits, while proxy diagnostics yield a depth si-RMSE of 0.2170 and instance mIoU of 0.3673. RenderBench provides paired real observations and editable scene state for assessing both appearance fidelity and preservation of geometry and dynamics.

---


### 317. [Probabilistic Counterfactual Inference for Discrete Outcomes in Gaussian-Process Causal Models](https://arxiv.org/abs/2610.08689)

**<font color=#1a73e8>作者：</font>** Juliette Sinnott, Amir-Hossein Karimi, Mohammad Kohandel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual inference in Gaussian-process structural causal models (GP-SCMs) has been developed primarily for continuous endogenous variables, limiting applicability to causal graphs that contain discrete child nodes with continuous parents. We introduce a unified probabilistic framework for counterfactual inference with heterogeneous variable types by pairing GP predictors with explicit exogenous noise mechanisms. For discrete outcomes, we derive exact conditional noise-abduction procedures using a uniform threshold for binary variables, a Gumbel-max race for nominal categories, and a latent Gaussian cut-point model for ordinal ones. In each case, we propagate abducted noise through interventions while accounting for posterior uncertainty in the GP latent functions, and prove that the resulting mechanisms reproduce the fitted model's observational and interventional distributions. On synthetic SCMs with known ground-truth counterfactuals, we evaluate estimation accuracy, consistency, and robustness to coupling misspecification. A key finding is that applying a categorical coupling to ordinal data inflates counterfactual error roughly threefold even when observational fit remains comparable, and that this error does not diminish with more data. As the training set grows, the fitted structural equation converges to the truth while the counterfactual error flattens onto a floor. In the reverse direction, forcing a false order onto nominal data instead degrades the fitted equation itself. The choice of coupling must therefore be justified on structural grounds rather than read off the fit.

---


### 318. [nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://arxiv.org/abs/2610.08699)

**<font color=#1a73e8>作者：</font>** Guangyi Liu, Yong Liu, Jiangning Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person's accounts and devices, remember them across weeks, speak first when it is worth it, and answer for what it did. It is a kind of software, not a model, and until now had no open counterpart. This report defines the personal agent in five questions and three horizons. It reads how Muse is built from Meta's public record and a copy of its production prompt, each statement marked by its source. It then presents nanoMuse, the open-source counterpart under the GPL-3.0, one agent on every device a person owns, with hands on the phone's screen and the computer's. They share one conversation over a relay anyone can run; every action goes through a Sentinel, memory is files the person can read, and the model is their choice. Its size and cost are given as estimates. What is open, memory with provenance, an evaluation suite for the hands and an open model for them, is set out as a roadmap.

---


### 319. [reVISit-XR: Bringing Extended Reality into Embeddable, Trackable, and Replayable Visualization Studies](https://arxiv.org/abs/2610.08700)

**<font color=#1a73e8>作者：</font>** Shano Liang, Max Chen, Lane Harrison  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Extended reality (XR) is increasingly a setting for empirical visualization research, where study-relevant state is distributed across headset and controller pose, scene configuration, selections, spatial layouts, and AR anchors. Existing XR tools support parts of the workflow, such as scene authoring, interaction, or session analysis, yet seldom treat an XR stimulus as a reusable component of a complete study lifecycle. We present reVISit-XR, an extension of reVISit that makes customizable WebXR stimuli embeddable, trackable, and replayable within empirical visualization studies. reVISit-XR sequences XR scenes alongside standard study components, collects reactive task responses, captures scene-authored semantic state together with generic XR traces, and rehydrates participant sessions for later desktop and headset analysis. Organized as a reusable stimulus build package and a study integration package, it lets XR stimuli act as first-class study components. We demonstrate its scope and feasibility through seven integrated, reusable examples and a deployed study, and discuss its current capabilities and future extensions.

---


### 320. [Co-Evolving Paths and Flows via Path-Flow Alignment](https://arxiv.org/abs/2610.08717)

**<font color=#1a73e8>作者：</font>** Zeyu Michael Li, William Xingxu Chen, Xiang Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study path-flow alignment as a unified training objective for flow matching. Instead of fixing the interpolation path and learning only the velocity field, we jointly train an endpoint-preserving path network and a flow network using the same alignment loss: the flow learns to match the path velocity, and the path learns to align its velocity to the current flow. Although every fixed learned path defines a valid flow-matching objective, the alignment loss alone is not a reliable criterion for path learning. We identify path overfitting, a failure mode in which the alignment loss decreases while sample quality worsens. We find that this failure is associated with low-entropy bottlenecks in the induced probability path, where the learned path routes samples through overly concentrated intermediate marginals. Motivated by this diagnosis, we introduce a stochastic path regularizer that hides part of the source information from the path network while preserving exact endpoints. The resulting regularization gives an explicit entropy floor for the stochastic training-path marginals and empirically suppresses the bottleneck in the learned sampler, making joint path-flow training effective. On ImageNet-256x256 with SiT backbones, our method consistently improves FID across model scales, extends to model-guidance training, and leaves the inference-time architecture and sampler unchanged. Code is available at this https URL

---


### 321. [Holdout Best-of-N: Unbiased Evaluation and Its Cost](https://arxiv.org/abs/2610.08719)

**<font color=#1a73e8>作者：</font>** Shrey Shah, Yinheng Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reusing the scores that select a Best-of-$N$ winner can overstate its expected reward. We study evaluation from a fixed matrix of $K$ independent scores per candidate for a policy that selects using $J$ fresh scores. A single estimator based only on this matrix is exactly unbiased for expected judge reward under every independent, stable collection of candidate-specific score laws if and only if $J<K$, for every pool size $M\ge N\ge2$. At $J=K-1$, the selector deepens as $K$ grows. For independent Gaussian scores with common variance and fixed $M\ge N\ge2$, the unbiased minimax risk in this regime is of order $\sigma^2/\sqrt K$, attained by Holdout; allowing bias improves the rate to $\sigma^2/K$. For two candidates, we derive the minimum-variance unbiased estimator at known variance and the sharp asymptotic unbiased minimax constant $1/(\pi\sqrt2)$, which Holdout attains without knowing the variance. The cyclic average over subsets and ties can be computed in $O(MK\log M)$ operations. At fixed selector depth, cyclic evaluation of bounded scores has $O(K^{-1})$ risk uniformly in pool size. The impossibility result concerns the fixed matrix: one additional fresh winner score permits unbiased evaluation of the all-$K$ policy.

---


### 322. [Does an Agent's History Tell You When Compaction Will Hurt? A Modest, Bounded Effect on the TRACE Paired-Replay Corpus](https://arxiv.org/abs/2610.08722)

**<font color=#1a73e8>作者：</font>** Egor Pakhomov, Erik Nijkamp  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many long-horizon agents compact their context on a global rule, usually a token budget, blind to what the agent was doing. We ask whether the agent's recent behaviour predicts when a compaction will hurt. TRACE's public corpus of 590 harness-triggered AppWorld compaction boundaries replays each boundary from a re-executed prefix state under the pre-compaction context and under the summary, and records the burden of the next actions: calls that error or repeat a call already made. We find that pre-boundary history predicts post-compaction harm only weakly. An internally prespecified contrast by prefix placement is a wide null, and the naive "has-written" label behind it turns out to measure trajectory phase. The best extension-protocol trigger reaches held-out AUROC 0.66 (0.64 on the replicate's own label) against a same-boundary replicate of 0.72; the best frozen, interpretable trigger avoids 21% of harmful (positive-burden) boundaries while keeping 84% of compaction opportunities, and exceeds the random-rule expectation on count but not on burden mass (a post hoc comparison). Whether the best trigger beats a token-budget rule at matched retention cannot be evaluated on the release. We state what corpora should ship to answer it.

---


### 323. [Optimal and Efficient Online Inverse Optimization](https://arxiv.org/abs/2610.08735)

**<font color=#1a73e8>作者：</font>** Anupam Gupta, Guru Guruganesh, Honghao Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In online inverse linear optimization, a learner recommends an action and then observes the choice of an expert who maximizes a fixed, unknown linear objective on $\mathbb{R}^{d}$; the goal is to learn to optimize this objective without observing it. Sakaue recently obtained the optimal regret $O(\sqrt d)$ with a randomized algorithm making $(dT)^{O(d)}$ linear optimizations per round, and asked whether it can be attained in polynomial time. We answer positively: our deterministic algorithm has regret $O(\sqrt d)$ for every horizon $T$ and runs in time polynomial in $d$ and $T$. It is a variant of the variable-metric algorithms of Sakaue et al.\ and Cai et al., in which a metric update is revoked once the query point moves far enough from where the update was made.

---


### 324. [On the Computational Tractability of Robust Bandits](https://arxiv.org/abs/2610.08740)

**<font color=#1a73e8>作者：</font>** Vanessa Kosoy, Vinayak Pathak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning when the environment does not belong to the learner's hypothesis class is typically handled using agnostic learning guarantees. However, for anything beyond supervised learning, agnostic guarantees are difficult to come by. Recently, imprecise bandits (Kosoy, 2025) (later renamed to robust bandits in Appel and Kosoy, 2025) were introduced as another approach to unrealizable learning in the bandits setting and a $\Theta(\sqrt{T})$ regret learner was shown for a large class. However, no computational guarantees were provided. In this paper we identify a special case that admits a polynomial-time learner with $\tilde{O}(\sqrt{T})$ regret. We also show that several small generalizations of this special case are NP-hard thus indicating that the special case is at the boundary of what is tractable. It has been recently suggested (Kosoy, 2018) that computationally efficient learners for unrealizable learning problems are crucial for solving the AI alignment problem. This work is a small step in that direction.

---


### 325. [Reinforcement Learning with Conformal Action Sets: An Application to Sequential Recommendation](https://arxiv.org/abs/2610.08743)

**<font color=#1a73e8>作者：</font>** Wenwen Si, Honghao Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential recommenders typically use a fixed slate size even though the number of useful alternatives changes within a session. We propose Reinforcement Learning with Calibrated Pruning (RLCP), which adapts the retained action set using critic scores and an online threshold. The threshold is updated from binary feedback indicating whether the set contains an action in a proxy target. We prove a deterministic bound on the observed proxy miss rate along adaptive trajectories. To quantify the effect of pruning on reward, we derive an exact decomposition of value loss into filtering and selection losses. Under explicit proxy and critic approximation conditions, this decomposition yields a finite session reward bound that also accounts for imperfect selection and set truncation, without requiring the learning parameters to converge. Experiments on KuaiRand-Pure and MovieLens 1M compare two RLCP implementations with four RL baselines. In each of the 19 configurations, at least one RLCP variant achieves the highest catalog diversity, reaching $1.11\times$ to $5.21\times$ that of the strongest baseline, with competitive session depth and no larger retained sets.

---


### 326. [Linear Bandits under Exact Sliding-Window Constraints](https://arxiv.org/abs/2610.08745)

**<font color=#1a73e8>作者：</font>** Seyed Mohammad Hadi Hosseini, Yasin Abbasi-Yadkori, Sattar Vakili  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study linear bandits under exact sliding-window constraints, where every consecutive block of actions must belong to a prescribed feasible set. In the offline setting, where the reward function is known, we show that convexity and cyclic-shift invariance make a stationary solution optimal when $w\mid T$ and within an additive $O(w)$ gap otherwise. In the online setting, we show that geometric structure alone is insufficient for learning, and sublinear regret can be impossible. We introduce a transition diameter $\tau$ that quantifies feasible reachability and develop a rare-switching OFUL algorithm with regret $\widetilde{O}(d\sqrt{T}+\tau d+w)$ against the offline-optimal feasible trajectory. Finally, we remove cyclic invariance and consider general sliding-window constraints, where optimal behavior may be non-stationary. We represent recent action history as the state of a finite-memory control problem and introduce a history-state diameter $D$ that measures feasible communication between viable histories. Combining optimistic remaining-horizon planning with rare policy updates, we obtain a regret bound of $\widetilde{O}(d\sqrt{T}+dD+w)$. We evaluate our approach on real-world and synthetic benchmarks, showing that it maintains exact feasibility while achieving reward and regret comparable to baselines with substantially fewer policy updates.

---


### 327. [Neural Petri flows for chemical reactions](https://arxiv.org/abs/2610.08750)

**<font color=#1a73e8>作者：</font>** Jose Eduardo Escrig Molina, Daniel Probst  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Petri nets have been used to describe chemical processes such as this http URL map well to chemistry: Places are the bonds between atoms and the free valence of each atom, a token is a unit of bond order, a transition forms or breaks a bond, the conserved quantities are the valence budgets of the atoms, and the enabling rule is the valence rule. These semantics are not guaranteed by learned models of reactions or neural networks that are built on Petri nets that use the net as a scaffold for message passing. Here, we ask what architecture remains a Petri net for every value of its weights. We find the answer in the theory, where all semantics of a net share the firing form $m^\prime=m+C\sigma$, locality, as enabling reads only the inputs of a transition, and the enabling rule, and we prove that conservation forces the firing form and that non-negativity forces the enabling rule on local rate laws. This leaves free the rate law, which is the propensity of each transition to fire. We introduce Neural Petri Flow, which learns this rate law, or a readout for classification, and hard-wires the rest as parameter-free layers. On what we denote a valence net, atom mapping, reaction classification, and forward prediction become three tasks on one firing vector. Without training, the minimum firing vector maps 88.8% of the curated Golden set against 85.6% for RXNMapper, and 88.7 against 77.9% of the enzymatic reactions of EnzymeMap. On USPTO-480K, NPF trained on these firing vectors predicts 87.7% of the products and 67.4% when trained on a 1% subset of the training reactions. EC numbers of ECREACT are predicted at the third level for 90.2% of reactions, 5.6 points ahead of the best published method. With electrons as tokens, the same token game predicts 90.5% of the elementary steps of FlowER first, ahead of the published baseline, and every top-1 prediction is a valid molecule without a filter.

---


### 328. [Post-Training Semantic Lifting for 3D Gaussian Splatting: Separating Detector, Lifting and Representation Error](https://arxiv.org/abs/2610.08756)

**<font color=#1a73e8>作者：</font>** Iván Verdugo Guerra, Ezequiel López Rubio, Jorge García González  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The same Gaussian of a 3D Gaussian Splatting model is seen from many views, and these views do not always agree on the class it belongs to. The Gaussian may be occluded in some of them, and the confidence of the detector is not the same from one view to another. The ground truth, on the other hand, is given as an annotated mesh, because two training runs do not produce the same Gaussians. In this work, we propose a post-training lifting method that works with one target class at a time and combines the information coming from all the views. Target and non-target evidence are accumulated simultaneously, weighted by the visibility of each Gaussian in each view. After that, the Gaussians are filtered with two thresholds: a main threshold $\beta$ selects the high-confidence seeds, and a lower one $\gamma\beta$ adds the connected components around them. For the evaluation, the labels are transferred from the Gaussians to the mesh vertices that are both visible and annotated. With this design, we can separate three sources of error: the 2D detector, the lifting and the transfer between representations. The thresholds and the transfer operator are chosen on seven Replica validation scenes, and the method is evaluated on ten held-out ScanNet++ scenes with the same values for every scene and class. The mean mIoU on the validation scenes was 0.93 with masks from the dataset annotations and 0.65 with YOLO masks, and on the ScanNet++ test scenes it was 0.80 and 0.54. Compared with thresholding the evidence per view, as a previous version of the method did, the fraction improves the test mIoU by 0.24 and makes it possible to use a single threshold for all the classes and scenes of both datasets. Finally, the error analysis shows that most of the remaining error comes from the detector.

---


### 329. [Data Leakage in Patch-Based Hyperspectral Image Classification: Quantifying the Impact of Spatial Overlap](https://arxiv.org/abs/2610.08770)

**<font color=#1a73e8>作者：</font>** Mohammed Q. Alkhatib  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Patch-based learning improves hyperspectral image (HSI) classification by exploiting local spectral-spatial information, but random train-test sampling from the same image can cause spatial patch overlap, leading to data leakage and optimistic performance estimates. This paper investigates same-class train-test spatial overlap in patch-based HSI classification using two measures: overlap percentage (OP), which quantifies the global amount of overlapped testing patch pixels, and average overlap ratio (AOR), which measures the local severity among affected testing patches. Experiments on the Pavia University dataset compare random and non-random spatial sampling using SVM, MLP, 2D-CNN, 3D-CNN, ViT, and MorpMamba. The results show that deep patch-based models achieve high accuracy under random sampling, with 3D-CNN reaching 96.17% Overall Accuracy (OA), but drop substantially under non-random spatial sampling, where 3D-CNN decreases to 55.20% and ViT and 2D-CNN drop by 40.71 and 38.81 percentage points (PP), respectively. Patch-size analysis further shows that increasing the patch size from 5x5 to 19x19 raises the random-sampling overlap percentage from 23.28% to 77.02%. These findings demonstrate that random patch-based evaluation can substantially inflate classification performance, especially for models that strongly exploit spatial context. The code associated with this paper is available at: this https URL.

---


### 330. [Mission-Aware Attestation Envelopes for Time-Critical Autonomous Action: A Hardware-in-the-Loop V2I Study](https://arxiv.org/abs/2610.08771)

**<font color=#1a73e8>作者：</font>** Dimitrios Nikou, Nikolaos Kekatos, Sophia Petridou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An autonomous system that asks for a privileged physical action is usually gated on integrity evidence: a platform proves what it is running, and the request is granted or refused on that basis. Such a gate is normally treated as a predicate, yet the evidence behind it has an age, the decision that consumes it has a latency, and the physical system that waits for it has a deadline. We formulate mission-aware attestation as a runtime assurance contract that holds only when integrity is valid, the evidence is fresh enough, and the decision completes inside a budget derived from the current physical state. The contract yields four operational outcomes where a binary gate yields two, separating a refusal caused by tampering from one caused by stale evidence and from one caused by a late decision. We evaluate it on a hardware-in-the-loop vehicle-to-infrastructure platform: a driving simulator supplies the physical state and the authorisation deadline, while a microcontroller on-board unit and a TPM-backed roadside unit running Linux integrity measurement supply the assurance evidence. A security-blind model admits the whole operating space and a hardware-informed one three quarters of it, and every point it refuses fails the freshness margin rather than the response margin. Moving the attestation interval across the range the verifier permits costs about as much as a fivefold scaling of the latency distribution, and the interval is directly configurable, which makes it the immediately actionable deployment parameter. If the freshness bound does not exceed the authorisation budget, every late decision is also stale and lateness becomes unobservable, so the attestation interval and the freshness bound cannot be chosen from security requirements alone.

---


### 331. [Backend-Agnostic Sparse Attention for Fast High-Resolution Visual Generation](https://arxiv.org/abs/2610.08772)

**<font color=#1a73e8>作者：</font>** Liao Ma, Jiayi Song, Yunfeng Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have achieved strong performance in image and video generation, but the quadratic complexity of full attention makes high-resolution generation computationally expensive. Window attention offers an efficient alternative, yet existing methods face a practical trade-off: partitioned window attention typically achieves computational efficiency consistent with its theoretical complexity. However, isolated windows block cross-window interaction, often introducing visible grid-like artifacts in the generated results. Fine-grained sliding-window attention effectively restores interactions across neighboring windows and improves visual quality. However, its irregular computation patterns create a substantial gap between theoretical and practical speedups and require specialized kernels tailored to each hardware backend. To tackle these challenges, we propose BASA, a backend-agnostic sparse attention, which brings the best of both worlds: visual quality and practical acceleration. Specifically, BASA replaces visual self-attention with shifted local-window attention. By introducing a structured window-shifting scheme across DiT blocks, we allow tokens divided by window boundaries in one layer to communicate in the following layers, thereby achieving global information exchange and eliminating window-induced visual artifacts. Notably, our design introduces no additional irregular operators or customized kernels, making it readily deployable on existing attention backends and closing the gap between theoretical sparsity and practical acceleration. Experiments demonstrate that BASA achieves measured speedups exceeding 90\% of the theoretical estimates on FLUX and delivers a 4.52$\times$ attention speedup on Wan while maintaining competitive generation quality.

---


### 332. [CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching](https://arxiv.org/abs/2610.08777)

**<font color=#1a73e8>作者：</font>** Shangye Song, Dong Gong, Hong Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video world models need to generate each video chunk efficiently while responding faithfully to user controls. Many systems use chunk-wise autoregressive generation with few-step denoising, but each chunk still requires several costly denoising iterations. Training-free caching can reduce this cost, yet existing policies make reuse decisions primarily from model-internal denoising dynamics and do not explicitly account for control transitions. Actually, interactive generation explicitly exposes a signal they do not use: the controls for a chunk arrive before it is denoised, so a schedule derived from them costs no forward pass. To this end, we analyze adjacent chunks under different control regimes and find that structural similarity drops around action changes, while low-frequency structure remains more persistent than high-frequency detail. Motivated by these observations, we propose CtrlCache, a training-free control-aware caching framework that adapts computation to the current control sequence. Specifically, the action-aware scheduling and refresh policy detects action changes across and within chunks, and labels each chunk as initial, transition, turning, or steady state. At one selected interior denoising step, initial and transition chunks retain full computation, while turning and steady chunks reuse the transformer residual from the most recent fully computed step in the same chunk. To exploit the persistence of low-frequency structure during steady interaction, we further introduce a frequency-mixed history prior guidance that incorporates complementary information from the preceding clean latent without an additional DiT forward pass. Evaluated on Matrix-Game 2.0 and LingBot-World v1/v2, CtrlCache achieves 1.21x to 1.41x DiT-backbone speedups without model retraining while improving WBench Overall scores over original inference across all three models.

---


### 333. [4D-HOF: Hand-Object Flow Matching for Feed-Forward 4D Interaction Reconstruction](https://arxiv.org/abs/2610.08782)

**<font color=#1a73e8>作者：</font>** Shiqi Li, Sean Cho, Yijie Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing methods for 4D hand-object reconstruction often rely on costly per-sequence optimization, while generative approaches typically synthesize interactions from random noise, which can lead to unstable interaction prediction. We introduce 4D-HOF, a feed-forward framework that reconstructs 4D hand-object interactions from coarse but informative estimates produced by vision foundation models. Concretely, we learn a conditional flow matching model that transports foundation-model-derived hand-object states toward an interaction manifold, allowing the model to correct errors in translation, rotation, and alignment in a feed-forward manner. A key advantage of our generative formulation is that it naturally enables test-time guidance within the transport process. Rather than applying a separate post-hoc optimization after reconstruction, we directly steer the evolving generative states using physical interaction constraints and observed 2D evidence, allowing the reconstruction to be refined as part of the generative process itself. By training the generative model on diverse datasets, 4D-HOF generalizes robustly to challenging in-the-wild scenarios. Experiments on out-of-domain benchmarks show that 4D-HOF achieves state-of-the-art performance, producing more stable and accurate 4D hand-object reconstructions.

---


### 334. [Conformal Prediction Sets Quantify Information Gain: A Theoretical Perspective](https://arxiv.org/abs/2610.08785)

**<font color=#1a73e8>作者：</font>** Kevin Zhang, Stephen Bates  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction is a popular tool for uncertainty quantification that outputs prediction sets with finite-sample coverage guarantees. While prediction set size is commonly used as a heuristic measure of uncertainty, the information-theoretic basis for this interpretation remains poorly understood. In this work, we provide such a foundation using a decision-theoretic generalization of entropy tailored to set-valued prediction. In particular, we introduce a family of generalized information measures based on the size and coverage of conformal prediction sets. Notably, Shannon mutual information admits an exact integral representation in terms of these measures. We then show that, in standard classification settings, the reduction in conformal set size from additional information (i) is sandwiched between calibration-dependent members of this family and (ii) obeys a data processing inequality, both up to finite-sample calibration and model error terms. Together, our results formally relate conformal prediction to classical information-theoretic quantities and justify using set-size reduction as an information gain metric. Empirically, we validate our theory across 11 classification settings and show that set-size reduction and Shannon mutual information can rank features differently in a greedy feature selection experiment.

---


### 335. [Building Rome from a Single Image](https://arxiv.org/abs/2610.08790)

**<font color=#1a73e8>作者：</font>** Jiraphon Yenphraphai, Fang Li, Tianshuo Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image scene generation aims to produce a complete 3D scene mesh from a single image, including surfaces the camera did not observe. While pretrained 3D object generators encode a strong shape prior, they are mainly designed for isolated objects in a fixed canonical volume and focus mostly on indoor scenes, since diverse 3D data for outdoor scenes are quite limited. In this work, we present a method that redesigns such an object-centric generator, e.g., Trellis 2, to work on both indoor and outdoor scenes while retaining its prior. We accomplish this by (a) partitioning the scene into adaptive chunks that scale relative to the distance to the camera; nearby chunks have a smaller size to keep the finer detail, while distant structures, e.g., buildings, are covered by large chunks; (b) making the generator capture explicit 2D-3D correspondence by lifting image features and making the model aware of the free space, observed surface, and unobserved region; (c) synthesizing around 4,000 outdoor scenes to broaden the training data, as existing scene datasets are largely indoor. Experiments on Tanks and Temples, ScanNet++, and in-the-wild images show that our method outperforms all baselines in geometric accuracy and perceptual quality across both indoor and outdoor scenes.

---


> [!TIP]
> 当前位于：**301-335**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-335**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
