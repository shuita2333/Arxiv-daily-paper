# 📦 其他研究 | 2026年11月03日

> 本类共 **193** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-193](./part-04.md)

---

### 1. [FGSM Attack Transferability from Simulation to Quantum Hardware in Network Intrusion Detection](https://arxiv.org/abs/2610.40701)

**<font color=#1a73e8>作者：</font>** Zeeshan Ajmal, Kimmo Halunen, Marc Maußner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Quantum computers are now available through cloud platforms, and recent work has proposed using them to detect network intrusions. It is not yet clear how easily such systems can be attacked. We train a hybrid variational quantum classifier (VQC) on the Friday DDoS subset of CICIDS2017 and test it against two attacks: label flipping during training and FGSM evasion at prediction time. We run the tests in simulation and on IBM hardware, the Fez superconducting processor (Heron r2). We find that two models with similar accuracy can differ greatly in how easily they are attacked. A model that decides with little confidence loses half its detections to a very small change in the input, while a model trained to decide with more confidence needs a much larger change before it fails. Attacks built in simulation against the more confident model also work on real hardware, and the device classifies every unaltered attack sample correctly. Simulated device noise does not reduce accuracy, but it does reduce the model's confidence and makes attacks easier, so accuracy alone does not show how exposed a model is. Label flipping has no measurable effect until 15% of attack labels are changed. These results show that device noise should not be treated as a defense and that reported weaknesses in these classifiers depend partly on how they were trained.

---


### 2. [Bayesian Distribution System State Estimation with Flow Matching](https://arxiv.org/abs/2610.40728)

**<font color=#1a73e8>作者：</font>** Nan Lin, Peter Palensky, Pedro Vergara Barrios  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medium-voltage feeders have few real-time measurements, so distribution system state estimation (DSSE) rests on pseudo-measurements of the secondary substations, a prior in Bayesian terms. Weighted least squares keeps the power flow exact but reduces this prior to a mean and variance, while supervised deep learning estimators also learn the power flow and are tied to one measurement set. We propose PoSE (posterior sampling for state estimation), which keeps the Bayesian structure of DSSE and learns only what the distribution system operator does not know, namely the distribution of substation injections, modelled by a neural network trained with flow matching on historical data. The power flow equations, grid topology and measurements enter only at sampling, through a noise-aware Kalman-type correction. The neural network therefore never approximates the power flow, but every posterior sample is a physically consistent operating point, and one trained prior serves any measurement set, noise level and topology. On the IEEE 33-bus feeder, PoSE lowers the probabilistic injection error (CRPS) by 6.7-7.5% against a full-covariance Gaussian prior in all 12 tested settings. It provides reliable uncertainty: the 90% intervals contain the true injection almost exactly as often as exact posterior samples would, whereas those of supervised estimators contain it in only 37-78% of cases. On the 240-bus unbalanced three-phase Iowa feeder, it gives the lowest injection, voltage and branch-current errors of all estimators. A fast variant matches this accuracy at 0.2-0.6s per snapshot and, without retraining, beats Gaussian priors and retrained supervised estimators on seven reconfigured topologies.

---


### 3. [Don't Just Impute, Detect: Task-Aware Diffusion Pipelines for Edge Anomaly Detection](https://arxiv.org/abs/2610.40732)

**<font color=#1a73e8>作者：</font>** Jeongsu Park, Taehyeon Yun, Geonwoo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial Internet of Things (IIoT) edge pipelines routinely lose contiguous blocks of multi-sensor data to network dropouts and hardware faults. The standard remedy is a disjointed "impute-then-detect" pipeline whose imputer is trained only for Mean Squared Error (MSE). Such an imputer fills a missing block with the most probable normal pattern: a partially observed anomaly is smoothed back toward normality, and boundary artifacts on normal data raise false alarms. We call this imputation bias and propose the Task-Aware Diffusion Refiner (TADR), a conditional diffusion refiner trained against the loss landscape of a frozen downstream detector. Because back-propagating through the sampling trajectory is intractable, the task-aware terms act on the one-step clean-window estimate that the noise prediction already yields, so training costs no more than plain diffusion training. Under strict Point-to-Point evaluation over five seeds with paired significance tests, TADR raises F1 by $0.338$ over the unrefined detector on SMD ($p = 0.0015$), and the anomaly enhancement objective alone contributes $0.463$ in ablation. We also characterise when the method helps: the gain tracks the continuous, mutually redundant channels available and the anomaly evidence the outage removes, and it is absent on telemetry datasets dominated by one-hot command channels and on PSM. At ten sampling steps TADR runs in $41.4$ ms per window on a single CPU core, sustaining about $24$ concurrent 1 Hz streams from a $4.03$ MB model. Code and per-seed results are available at this https URL.

---


### 4. [Unsupervised Feature Selection Using Local Intrinsic Dimensionality -- Extended Version](https://arxiv.org/abs/2610.40736)

**<font color=#1a73e8>作者：</font>** Oussama Chelly, Michael E. Houle, Ken-ichi Kawarabayashi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High dimensionality degrades both the efficiency and the effectiveness of learning algorithms, and in many applications no class labels are available to guide dimensionality reduction. This paper proposes LIDFS, an unsupervised feature selection method based on Local Intrinsic Dimensionality (LID). The method builds on the formal equivalence between LID and the indiscriminability of distance measures. The data matrix is transposed so that each feature is treated as a point, and the LID of each feature is estimated by maximum likelihood from the distances to its $k$ nearest neighboring features. Features with lower LID exhibit greater local discriminability and receive higher importance scores. A refinement step then retains one representative per feature neighborhood and demotes locally redundant features. The result is a complete ranking from which any number of features can be selected without rerunning the procedure. LIDFS does not use any information about labels or the number of classes, and runs in $\mathcal{O}(d^2 n)$ time for $n$ instances and $d$ features. LIDFS is compared with classic and state-of-the-art methods and a random baseline on 23 high-dimensional datasets, the classic benchmark collection. The evaluation uses classification accuracy and AUC with five downstream classifiers, as well as clustering accuracy and normalized mutual information, over both full and aggressive selection ranges. LIDFS ranks first in the supervised evaluations and first or tied second in the clustering-based evaluations. It belongs to the top statistical group together with methods that require the number of classes, and it runs faster than its closest competitor. Several recent methods, by contrast, fail to outperform the random baseline. A sensitivity analysis shows that small neighborhood sizes yield the best results.

---


### 5. [Certified Behavioral Retention for Continual Adaptation with Held-Out Anchors](https://arxiv.org/abs/2610.40740)

**<font color=#1a73e8>作者：</font>** Ahanaf Hasan Ariq, Abrar Shahid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual adaptation requires deciding not only how to update a model, but whether to commit an update without exceeding a declared budget for changes to protected behavior. We introduce Certified Anchor-Based Adaptation (CABA), a candidate-agnostic post-update gate that reserves historical observations from candidate optimization, compares old and candidate policies on frozen representations, and selects the largest tested interpolation coefficient whose worst-anchor forward KL divergence remains within budget. The finite check requires neither action labels nor complete trajectories. We develop a theory-led certification framework that separates measured anchor retention from conditional off-anchor guarantees. Under explicit representation-coverage and Lipschitz assumptions, an accepted update satisfies a uniform behavioral-divergence bound on protected support. The analysis gives regularity bounds for affine softmax heads, probabilistic coverage and compression guarantees, interpolation monotonicity conditions, grid-resolution bounds, and trajectory-level and sequential-composition guarantees. In a controlled UCI Human Activity Recognition study used as a non-stationary sensor-policy proxy, CABA reduces mean forgetting from 1.01 percent for unconstrained adaptation to 0.00 percent at budget epsilon = 0.05, while reducing final average accuracy from 93.04 percent to 88.48 percent. The experiment illustrates a retention-plasticity trade-off and does not establish foundation-model or robotic performance. CABA provides an auditable retention check for candidate generators exposing comparable policy distributions and a declared update path, while deployment also requires separate evidence of current-task utility.

---


### 6. [PathoJev: Efficient Pathology Decisions from Shared Visual Context](https://arxiv.org/abs/2610.40752)

**<font color=#1a73e8>作者：</font>** Chengyang Zhang, Wenchuan Zhang, Bo Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology workflows require multiple visual judgments about the same slide, from identifying tumor type to assessing grade and invasion. Generating and parsing a separate textual response for each structured question adds latency between visual evidence and usable decisions. Building on the System One paradigm, we introduce PathoJev, a pathology model that directly predicts answer probabilities for whole-slide and region-level assessment. PathoJev encodes each slide once and evaluates independent question suffixes in batches over the shared visual context. Reusing the hybrid backbone's recurrent states further limits the computation that grows with slide-context length for each additional question. Across three whole-slide benchmarks, the 9B and 27B models achieve mean accuracies of 77.2% and 78.1%, exceeding SlideChat by 5.4 and 6.3 percentage points. Both scales also maintain competitive accuracy on five ROI benchmarks. On WSI-Bench, the 9B model runs 9.1x faster than SlideChat. Shared context accelerates eight-question workloads by 6.9x and 5.9x over separate prefix encoding, rising to 11.2x and 8.9x for 64 questions. These results provide a reusable probabilistic interface for combining multiple visual judgments in whole-slide and local tissue assessment. Code: this https URL.

---


### 7. [AutoHebb: Self-Modifying Neural Networks that Zero-Shot Infer and Continually Learn](https://arxiv.org/abs/2610.40757)

**<font color=#1a73e8>作者：</font>** Daniel Levine, David van Dijk, Kenneth Kay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans and animals have a unique capacity to generalize and learn in novel circumstances, including "0-shot" inference (ZI) and continual learning (CL) -- two powerful cognitive abilities. Despite this importance, efforts to model ZI and CL are seriously limited in several ways. First, existing models typically lack components critical to ZI and CL in the brain, namely, strong inductive biases (for ZI) and autonomous control of learning (for CL). Second, models can be less tractable to analysis if model components are overly complex (lacking simplicity), or too task-restricted if model components are overly bespoke (lacking expressivity). Here we introduce autonomous Hebbian networks ("AutoHebb"), a class of online learning feedforward neural networks that realize strong inductive biases and autonomously controlled learning, and are both simple and expressive. Unlike standard models that learn via externally controlled optimization (e.g. gradient descent), AutoHebb networks combine external feedback with internally generated activity to produce a global learning signal ('neuromodulator') fed back to the network. The neuromodulator in turn gates a biologically grounded local learning rule (3-factor Hebbian rule) that updates networks' plastic weights. Using meta-learning to search for fixed (non-plastic) weights, we find that AutoHebb networks (1) succeed on ZI tasks, (2) show emergent (untrained) ZI/CL abilities, (3) admit reverse-engineering into explicit algorithms, and (4) outperform modern learning models on ZI/CL tasks. Lastly, performance comparisons to related models implied an essential role for three model components: meta-learning, Hebbian plasticity, and autonomous control of learning. These findings indicate that AutoHebb may be useful in hypothesis generation, analysis, and discovery of biologically grounded forms of learning and generalization.

---


### 8. [Personalised 3D Mnemonics for Vocabulary Learning in Context](https://arxiv.org/abs/2610.40760)

**<font color=#1a73e8>作者：</font>** Karolina Trajkovska, Matjaž Kljun, Maheshya Weerasinghe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Augmented reality (AR) can support vocabulary learning by placing mnemonic cues in the physical contexts where new words are encountered. Prior work has augmented real objects with bilingual labels, audio, keywords, and 3D visualisations of those keywords interacting with the objects, but these cues are typically predefined by system designers. This limits scalability and reduces learners' ability to construct personal mnemonic links. By grounding mnemonics in objects that learners already recognise, use, and associate with prior experiences, a system could connect new vocabulary to existing mental models rather than requiring learners to adopt designer-defined associations. We outline a proof of concept and a storyboard of a generative AR approach in which learners create personalised 3D mnemonics by transforming familiar objects in their surroundings into situated mnemonic anchors. We position this concept within a timeline of related work and argue that recent advances in generative 3D asset creation enable a new design point: personalised 3D mnemonics that do not merely place content in the physical learning environment, but modify familiar real-world objects so that they become part of the mnemonic itself.

---


### 9. [Beyond Plausible Prediction: Safety Sufficiency in Web World Models](https://arxiv.org/abs/2610.40798)

**<font color=#1a73e8>作者：</font>** Zhifei Hu, Alexandra I. Cristea, Adel Bibi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web world models increasingly predict the consequences of candidate actions before agents act, yet a plausible predicted future does not necessarily support the correct safety decision. In a matched human evaluation of 3,000 predictions from ten frozen open models, 86.1% are judged semantically plausible. However, several models exhibit highly asymmetric authorisation behaviour, combining low false-safe execution with poor recall of clarifiable ASK cases and a strong preference for BLOCK. This motivates safety sufficiency: whether a predictive interface preserves and exposes the policy-decisive information required to distinguish actions that may be EXECUTED, require clarification through ASK, or should be BLOCKED. We introduce SafeWebWorld, a benchmark for evaluating safety sufficiency across five web-safety domains through action-conditioned futures, policy-decisive evidence, and policy-conditioned decisions. Under a controlled Security-Aligned Supervised Fine-Tuning protocol, evidence preservation can improve substantially while authorisation-sensitive decisions deteriorate. To determine whether this deterioration reflects loss of authorisation-sensitive score structure or a failure of the decision readout, we introduce Latent Authorisation Recovery (LAR). Frozen-score recalibration reveals substantial but backbone-dependent recovery, while paired recovery provides only a modest additional gain. Yet within-family and matched-authorisation evaluations remain poor, showing that aggregate recoverability does not imply robust fine-grained authorisation behaviour. Overall, plausible prediction, evidence preservation, and aggregate recovery are each insufficient on their own to establish robust authorisation.

---


### 10. [Circumventing the Computational Hardness of Computational Arbitrage](https://arxiv.org/abs/2610.40831)

**<font color=#1a73e8>作者：</font>** Nastaran Okati, Ricardo Olmedo, Moritz Hardt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI model marketplaces host providers with heterogeneous costs and capabilities. These differences create an opportunity for computational arbitrage (Olmedo et al., 2026), in which an intermediary purchases inference from a portfolio of models and resells it to users at a profit. Beyond creating profit opportunities for the arbitrageur, computational arbitrage offers financial value to both consumers and providers and could therefore significantly influence AI model markets. While prior work empirically demonstrates the feasibility of computational arbitrage for small model pools, scaling it to large marketplaces requires arbitrage strategies that are both computationally tractable and inexpensive to identify and deploy. In this work, we formalize computational arbitrage as an allocation problem and prove that it is generally NP-hard. However, we show that the optimal allocation can be computed efficiently under a natural diminishing-returns condition on how model performance scales with inference spending. We further develop a sample-efficient method for estimating model performance from limited data, reducing the upfront cost of identifying arbitrage strategies. Our analysis also yields several economic insights: at the optimum, every funded model delivers the same marginal utility per dollar; arbitrage directs revenue away from providers offering little utility relative to their prices; and it rewards complementary specialization.

---


### 11. [EgoHSI3R: Online 4D Hand-Scene Interaction Reconstruction from Egocentric Video](https://arxiv.org/abs/2610.40832)

**<font color=#1a73e8>作者：</font>** Mingzhi Pei, Zhangchen Ye, Ruoqu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric videos offer an abundant source of hand-scene interactions for embodied learning, which requires recovering hands, camera, and scene consistently in a shared 3D world. Existing methods focus on either camera-frame hands or world-space hand trajectories, without jointly recovering the scene pointmaps or interaction information. Building a complete reconstruction from such specialized predictions therefore typically requires per-sequence optimization. We propose EgoHSI3R, a unified feed-forward framework for online 4D hand-scene interaction reconstruction from egocentric monocular video. To jointly recover these components, it maintains a recurrent scene representation that accumulates geometric evidence over time and provides a shared world space and scale. We introduce hand-centric prompts that fuse pretrained hand priors and local scene context, while MANO vertex queries attend to scene features to predict dense per-vertex contact. These designs enable a single network to jointly estimate camera motion, dense scene geometry, world-space bilateral MANO hands, and per-vertex hand contact. Despite operating causally, EgoHSI3R achieves the lowest world-space hand joint error on ARCTIC among the evaluated methods, while offering faster inference than existing world-space hand reconstruction pipelines and competitive camera and scene reconstruction accuracy.

---


### 12. [Spatial Atlas-Informed Loss Ensembles for Whole-Body PSMA PET/CT Metastasis Segmentation](https://arxiv.org/abs/2610.40834)

**<font color=#1a73e8>作者：</font>** Grant N. Chau, Bashirul A. Biswas, Biratal Wagle 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing whole-body PSMA PET/CT prostate metastasis segmentation methods generally rely on images alone, without explicitly incorporating where metastases tend to occur. We investigate whether a population metastasis atlas can improve lesion detection when integrated into model training. We constructed voxel-wise mean and standard deviation maps from 375 expert-annotated training scans and used them to weight the cross-entropy loss of an nnU-Net. The additional penalties for missed lesions and false positives depend on spatial atlas statistics and diminish as predictions become confidently correct. Seven configurations were compared on validation data; three were combined by majority voting into SAILS (Spatial Atlas-Informed Loss enSemble). We compared SAILS with a baseline nnU-Net and inference-time atlas fusion on AutoPET~III (110 disease-positive cases) and Deep-PSMA (100 external cases). No atlas or registration is needed at inference. Results: On AutoPET~III, SAILS improved whole-body Dice (0.531 vs. 0.520; p=0.006), reduced missed-lesion volume (9.5 vs. 12.1 cc/case; p<0.01), and increased pooled lesion sensitivity (0.857 vs. 0.843; p=0.004). On Deep-PSMA, SAILS detected 126 additional reference lesions (sensitivity 0.769 vs. 0.751; p<0.001), without a significant whole-body Dice change (-0.009; p=0.36). High-risk bone Dice improved in both cohorts (0.576 vs. 0.552 and 0.667 vs. 0.653; both p<0.01). False-positive volume increased by 2.3 and 18.2 cc/case, respectively (p<0.001). Atlas-weighted training improves lesion detection, especially in high-risk bone, without test-time atlas registration, but increases false positives.

---


### 13. [Near-Optimal First-Order Regret for Bandits with Feedback Graphs](https://arxiv.org/abs/2610.40861)

**<font color=#1a73e8>作者：</font>** Mengxiao Zhang, Yuheng Zhang, Haipeng Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study first-order regret guarantees for adversarial bandits with a fixed, known directed feedback graph. For strongly observable graphs, [ACBDK15] establishes a minimax regret of $\widetilde{\Theta}(\sqrt{\alpha T})$, where $\alpha$ denotes the independence number of the graph and $T$ denotes the horizon. On the other hand, the best existing first-order bound scales as $\widetilde{O}(\sqrt{(\kappa+1) L^\star})$ [LLZ20], where $\kappa$ denotes the clique partition number, satisfying $\kappa+1\geq\alpha$, and $L^\star$ denotes the cumulative loss of the best arm, leaving a gap between the graph dependence in worst-case and first-order guarantees. In this paper, we bridge this gap by obtaining an expected regret bound of $\widetilde{O}(\sqrt{\alpha L^\star}+\alpha)$. Our first result is an algorithm for the special case of self-aware graphs, in which every vertex has a self-loop. The algorithm combines the update of EXP3 [ACBFS02] with a sampling rule inspired by exploration by optimization [LS20]. More specifically, we construct a map whose fixed points yield sampling distributions that control the one-round regret remainder in terms of the learner's loss and the graph's independence number, which is crucial in deriving optimal first-order guarantees. We further show that a sufficiently accurate fixed point can be computed in polynomial time by a geometrically convergent iteration. Finally, we extend the algorithm to general strongly observable graphs and achieve the same $\widetilde{O}(\sqrt{\alpha L^\star}+\alpha)$ guarantee by adapting the two-level aggregation approach of [LLZ20].

---


### 14. [TensorSSM: Memorizing Spatial Position in Dynamic State Space for Tensor Core Generation](https://arxiv.org/abs/2610.40871)

**<font color=#1a73e8>作者：</font>** Sheng Zhang, Xinyi Wang, Maolin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional tensors are ubiquitous in real-world applications but lead to massive storage overhead. Functional tensor decomposition addresses this by employing neural networks to map element coordinates to tensor cores, significantly reducing the parameters for data compression. However, existing functional methods typically flatten high-order tensors into 1D sequences. This folding operation causes highly overlapping local coordinate sequences and struggles to capture complex cross-mode spatial dependencies, severely limiting their expressiveness on diverse datasets. To tackle these challenges, we propose TensorSSM, a novel Implicit Neural Representation (INR) for functional decomposition method that memorizes spatial positions within a dynamic State Space Model (SSM). Specifically, TensorSSM first decomposes mode-wise coordinates into sequences spit by K-ary rule, encoding spatial tokens from coarse to fine, which effectively captures spatial variations. Furthermore, we extend the SSM's state space to explicitly map cross-mode spatial dependencies, allowing inter-mode interactions to enhance the updates of each mode. By integrating cross-mode information from previous hidden states into the current state transitions, TensorSSM effectively expands tensor representation along two dimensions: the sequence dimension for coarse-to-fine spatial tokens, and the state dimension for cross-mode memorization. This design effectively integrates spatial information into the state space and the tensor core, substantially advancing the state adaptability and enhancing the expressiveness of the data compression. Extensive experiments demonstrate that TensorSSM achieves significantly high reconstruction accuracy and storage efficiency, exhibiting robust expressiveness across diverse tensor datasets without relying on strict spatial assumptions.

---


### 15. [AquaProbe: Efficient Adaptation of Frozen Vision Models for Underwater Images](https://arxiv.org/abs/2610.40900)

**<font color=#1a73e8>作者：</font>** Md Shihabul Islam Shovo, Nishi Kanta Paul, Trung Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable visual perception is essential for safe autonomous underwater exploration. Yet vision models pretrained on terrestrial images become less reliable underwater, where turbidity, backscatter, and wavelength-dependent attenuation alter scene appearance. Existing adaptation methods either spread adapters equally across the encoder depth or select layers using the divergence between two fixed domains. In this paper, we introduce AquaProbe for measuring how the location of the domain gap changes with water type and imaging range. AquaProbe separates newly introduced divergence from that accumulated through a frozen vision encoder using paired clean and physically rendered images and allocates a fixed LoRA budget according to the measured profile. The segmentation mean Intersection-over-Union (mIoU) for the proportional LoRA rank allocation, based on the measured profile, is 70.1; this is a better result than uniform LoRA rank allocation by 1.9 mIoU points while having the same parameter budget of 0.59 million adapter parameters. The three-way router, conditioned on estimated condition clusters, achieves 70.6 mIoU on the standard SUIM split and 63.4 AUDRC under held-out degradation.

---


### 16. [No Channels Left Behind: Understanding Diffusion Acceleration through Residual Gates](https://arxiv.org/abs/2610.40914)

**<font color=#1a73e8>作者：</font>** Junha Park, Jaemyung Yu, Jaehui Hwang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training acceleration methods for diffusion transformers, such as REPA and dispersive regularization, are commonly explained by additional supervision, spatial-structure priors, or improved feature geometry. We revisit this view and uncover a striking internal change: the AdaLN-Zero residual gate $\alpha$, which directly controls how conditioned updates enter the residual stream, is substantially reorganized by these methods. This observation motivates our hypothesis that acceleration arises, at least in part, from reshaping the residual gating pathway rather than solely from the feature structures explicitly imposed by auxiliary objectives. Supporting this view, accelerated models are markedly more sensitive to perturbations of $\alpha$, and their gate geometry reflects semantic relationships among classes. We further introduce the normalized participation ratio (nPR) to characterize the channel-wise organization of the gates and find that, across REPA teachers, projector architectures, and radial-objective targets, broader gate participation accompanies better generation quality. Guided by this insight, we propose a simple teacher-free radial objective that promotes broader gate participation through feature-norm regularization, without pairwise feature comparisons. On ImageNet $256\times256$ with SiT-B/2, our method improves FID over dispersive loss while increasing mean gate participation over timesteps and classes, further supporting the link between gate organization and training acceleration. Our results identify residual-gate reorganization as a measurable axis of diffusion training acceleration and suggest a simple direction for further acceleration.

---


### 17. [Robot Navigation and Canine Welfare: A Pilot Study Surfacing Challenges for Cross-Species Legibility and Proxy Validity in Animal-Machine Interaction](https://arxiv.org/abs/2610.40921)

**<font color=#1a73e8>作者：</font>** Haoxiang Zhang, Nancy Smith  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Autonomous delivery robots increasingly share residential spaces with companion animals, yet navigation behavior is rarely designed with animal welfare in mind. This paper presents a pilot study evaluating a curve-out maneuver, a laterally arcing pass-by trajectory triggered at the dog's alert distance, proposed as a candidate welfare-informed navigation intervention grounded in canine social communication research and legible motion theory. Following a research through design approach, we developed and evaluated a first design iteration of the artifact in a naturalistic home environment with a companion dog. Contrary to our hypothesis, the curve-out produced a more acute stress response than the straight-line baseline. We argue that discontinuous execution limitation, the robot stopping and reorienting multiple times to approximate the arc, undermined legibility, which in itself became a stressor. The pilot surfaces the legibility of robot behavior to non-humans' eyes and proxy stimulus validity as structural challenges for AMI and repositions the design problem for future work.

---


### 18. [LiHA: Worse is Better for Lightweight Hash-based Source Authentication](https://arxiv.org/abs/2610.40928)

**<font color=#1a73e8>作者：</font>** Negin Dehghanchaleshtori, Homit Dalia, Himanshu Chandra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The omission of source IP authentication remains a fundamental vulnerability in the Internet. Existing approaches rely on routing plausibility, topology assumptions, per-flow state, or wide deployment. These requirements have kept strong source authentication out of the data plane.
As simplicity is the key to deployability, we present LiHA, a lightweight source authentication mechanism built around operations that routers already perform efficiently. LiHA binds secret keys to source prefixes using longest prefix match and authenticates each packet with a single message authentication code (MAC). The data plane requires no handshakes, per-flow state, or per-packet control plane access. A sender performs one prefix lookup and one fixed-size hash. The verifier repeats the same operations and forwards the packet only if the MAC matches.
LiHA is designed for incremental deployment. It primarily protects against off-path attackers that spoof source prefixes they do not control. An on-path attacker can replay valid authenticated packets until the key rotates. LiHA does not eliminate every denial-of-service threat. Instead, it confines accepted traffic to authenticated source prefix space within participating networks. We argue that simpler source authentication with clear limits is more likely to be deployed.
We implemented LiHA in three environments: as a set of user-space libraries, as eBPF programs, and in an FPGA. We found that the user-space implementation had very high overheads. The eBPF implementation got reasonable single thread performance even with a software based cryptographic hash. We found that only the FPGA could obtain 100 Gbps single thread performance, but that was only when bypassing the kernel using a DPDK user-level networking stack.

---


### 19. [Let LiDAR Decide Where to Look: Geometry-Measured Token Selection for Efficient Sparse Latent World Models](https://arxiv.org/abs/2610.40935)

**<font color=#1a73e8>作者：</font>** Zeping Zhang, Zhuoya Zhao, Robert Laganière  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-centric autonomous driving models encode thousands of image tokens per frame, yet most depict sky, buildings, or empty road---content irrelevant to planning. Worse, these tokens dilute the planner's attention: we show that randomly discarding 75% of tokens already outperforms the dense model, because the planner can concentrate on the remaining driving-critical content. Building on this finding, we present Geometry-Aware Token Selection (GATS), which uses LiDAR and radar point projections to select a small fraction of image tokens before the vision backbone runs. Because the selector operates on measured 3D geometry rather than visual features, the backbone encodes only the selected patches, cutting end-to-end FLOPs by up to $18\times$. Each kept token receives a 3D anchor from its LiDAR point and is fed to a self-supervised latent world model that predicts future features and 3D displacements without box annotations. At 25% budget, GATS achieves a 3-sec L2 displacement error of 0.520 m on nuScenes and an EPDMS of 88.9 on NAVSIM---surpassing the dense baseline (0.573 m / 85.9) at $6.6\times$ fewer total FLOPs. At an extreme 10% budget (24 GFLOPs, $18\times$ reduction), it still beats the dense baseline on both nuScenes (0.537 m vs. 0.573 m L2) and NAVSIM (87.9 vs. 85.9 EPDMS). On 739 intent-critical scenarios, GATS covers 95.8% of hazardous vehicles and achieves a 0.09% collision rate---73.5% lower than the dense model (0.34%).

---


### 20. [Fair Recommender Systems for Intersecting Groups](https://arxiv.org/abs/2610.40936)

**<font color=#1a73e8>作者：</font>** Christine Ling, Juba Ziani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recommendation systems that optimize for the average user can fail to capture the preferences of diverse demographic groups. We consider a dynamic recommendation system, where arriving users can belong to different demographic groups. Importantly, these groups can intersect, and a user may belong to several groups. We first show that over time, any group-blind policy (which excludes all current-user group information) recommending $K \geq 1$ items incurs linear total regret under mild conditions. In turn, we introduce three group-aware algorithms based on the classical Upper Confidence Bound algorithm (UCB): i) Intersection-Fitting, which runs UCB on each intersection, but has a sublinear group- and intersection-level regret guarantee with an exponential dependence in the number of groups; and ii) two group-level heuristics, Inner-Outer UCB and Group-Item UCB which allocate different arms to different groups, and use a sleeping expert meta-learner to choose which active group's recommendation an intersection should inherit at any given time step. We provide experimental results on two datasets, Goodreads and BoardGameGeek, and highlight that our heuristics can be preferable to the intersection-fitting algorithm when intersection-level preferences are closely related to group-level preferences, but that intersection-fitting performs better when different intersections within a same group prefer different items.

---


### 21. [Benchmarking Forecasting Agents on Yesterday's Tomorrows](https://arxiv.org/abs/2610.40940)

**<font color=#1a73e8>作者：</font>** Yuxuan Wang, Yishu Wang, Jiaqi Deng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital agents can now gather and organize information, reason over it, and use tools to complete complex tasks. Forecasting puts all of these abilities to the test: it requires integrating incomplete evidence, inferring causal drivers, and committing to calibrated probabilistic judgments. Existing benchmarks are poorly suited to measuring and improving this ability. Live benchmarks provide feedback only after events resolve, so every evaluation cycle waits on the calendar; fixed-corpus evaluations return results immediately but confine research to pre-collected documents. We introduce FABench, a scalable backtesting environment for Forecasting Agents. An automated pipeline discovers events, generates questions, and resolves outcomes for any past forecast date, so the benchmark can be renewed to stay ahead of model training cutoffs; its first release poses 287 questions across nine domains. Agents research each question freely in an archive environment that combines an offline archive with live web search screened to prevent temporal leakage. Evaluating agents built on eight recent models, we find that retrieval improves the Brier score of all eight in every retrieval setting and lifts the leading agents to the market consensus on the 54 questions linked to Polymarket, with the best three scoring slightly above it. Research traces reveal recurring failures in how agents weigh and apply evidence, leaving ample room for improvement. We release our code, data, and archive environment as a foundation for community research on forecasting agents.

---


### 22. [UFMF: Radar-Guided Kinematic Priors for Real-Time 4D Occupancy Forecasting](https://arxiv.org/abs/2610.40947)

**<font color=#1a73e8>作者：</font>** Zeping Zhang, Zhuoya Zhao, Robert Laganière  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time 4D occupancy forecasting requires reliably extrapolating both ego motion and surrounding actor motion under strict latency budgets. Recent occupancy world models improve long-horizon fidelity through generative decoders and 3D volumetric modeling, yet their computational cost makes real-time deployment challenging. Light-weight BEV forecasters meet latency requirements but often blur or suppress fast-moving actors at longer horizons. We present UFMF (Ultra-Fast Multi-modal Forecaster), a real-time forecaster that keeps an attention-free diagonal state-space temporal core while injecting targeted kinematic and geometric structure where lightweight models typically fail. A radar-guided velocity-aware dynamic prior (VADP) decomposes future displacement into a linear extrapolation plus a learned horizon-dependent residual. The resulting per-cell flow fields transport a compact dynamic latent subspace during rollout. Two auxiliary training constraints complement this branch: world-frame dynamic supervision enforces inter-horizon trajectory coherence, and class-conditioned vertical-profile supervision regularizes BEV-to-3D lifting. UFMF operates at 122 FPS on a single RTX 4090 and reaches 0.45 fast-displacement mIoU on nuScenes, outperforming recent occupancy world models at a fraction of their computational cost.

---


### 23. [AVID: A Weakly Aligned RGB-Infrared Dataset and Perturbation Benchmark for Tiny Aerial Targets](https://arxiv.org/abs/2610.40949)

**<font color=#1a73e8>作者：</font>** Dharini Raghavan, Vishnu Rao, Sethu Selvi S  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-range detection of small drones is complicated by their visual similarity to birds and by the limited detail available from ground-based cameras. Combining visible and infrared observations offers complementary information, but their usefulness depends on target size, cross-modal alignment, and image quality. We present AVID, a benchmark for studying these factors using real RGB-infrared bird-drone surveillance footage originating from the Drone Detection Dataset and curated for the IEEE ICIP 2025 Video and Image Processing Cup. AVID comprises 32,040 corresponding frame pairs from 115 videos, with 35,952 existing bird and drone annotations at $320\times256$ resolution. Targets occupy an unusually narrow size range: 68.1\% have a geometric-mean bounding-box side of 8--16 pixels, and 99.0\% meet the COCO small-object criterion. To characterize the geometric difficulty of combining the modalities, we introduce an object-relative alignment ratio and an alignment burden curve. In a sample of 300 frame pairs, 32.3\% have estimated global translations greater than 5 pixels; among the 264 pairs with matching annotations, 16.3\% exceed one median target side. We further introduce AVID-C, which simulates seven families of image degradation at five severity levels independently in RGB, infrared, or both. A fixed-feature analysis examines how scale, degradation, and added cross-modal shifts affect fitted bird-drone class overlap. At 12--16 pixels, the Bhattacharyya error bounds are 0.148 for RGB, 0.198 for infrared, and 0.046 for their combined features. These values describe separation in the specified feature and density models, not detector accuracy. Together, AVID and AVID-C support scale-aware, alignment-aware, and sensor-specific studies of tiny aerial targets.

---


### 24. [Monte Carlo Random Walk Kernel](https://arxiv.org/abs/2610.40956)

**<font color=#1a73e8>作者：</font>** Arslan Iamaletdinov, Elfat Sabitov, Konstantin Sorokin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Monte Carlo Random Walk Kernel (MCRWK), an estimator whose per-pair cost is independent of graph size and derived directly from the random walk kernel (RWK) expansion. By normalizing the kernel coefficients, MCRWK samples a shared walk length and estimates its contribution using random walks on the input graphs. This gives a simple way to approximate RWK without constructing the product graph. For a fixed expected walk length and efficient neighbor sampling, each pairwise estimate takes $O(m)$ time for $m$ Monte Carlo samples, allowing the sample budget to control the trade-off between runtime and accuracy. We evaluate MCRWK against Graph Voyagers and classical RWK methods on synthetic and real graph datasets. In the reported experiments on large synthetic graphs, MCRWK is faster than Graph Voyagers and, at matched runtime, more accurate. It also has the lowest Gram-matrix runtime on the five real datasets studied. Code and experiments are available at this https URL

---


### 25. [RADI3N: GeometRic ImAge EDiting via ParametrIc 3D CoNtrol](https://arxiv.org/abs/2610.40973)

**<font color=#1a73e8>作者：</font>** Abdul Wasi, Akhil Gorugantu, Mahesh Bhosale 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion-based methods have substantially advanced image editing, yet parametric 3D control at the part level remains challenging. Existing approaches either operate on whole objects with manual rigging, or revert to 2D handles at the part level. They also struggle to model appearance and texture under large transformations, leading to unrealistic outputs in geometry-intensive edits. To address these limitations, we introduce RADI3N, a framework for semantically-grounded part-aware object manipulation with parametric 3D control. Our CS-ARAP deformation module suppresses rotation-field discontinuities at part boundaries via neighborhood covariance smoothing, producing structurally consistent deformations under complex part-level edits. We further introduce an inversion-free selective texture transfer mechanism that suppresses high-frequency positional biases and scales up low-frequency semantic cues within cross-image attention. This eliminates strict spatial bias and supports semantic matching, allowing source appearance to follow the edited part onto its new geometry. Experiments demonstrate that RADI3N achieves state-of-the-art performance in geometric fidelity, viewpoint consistency, and controllability.

---


### 26. [Towards Elastic Least Privilege for Agent Planning](https://arxiv.org/abs/2610.40981)

**<font color=#1a73e8>作者：</font>** Simon Parkinson, Zhipeng Wang, Mustafa Mustafa  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> General-purpose AI agents require authority that changes between tasks and during execution. Common deployments trade broad permissions that expose unnecessary authority and narrow permissions that raise approval requests. Existing mechanisms can enforce dynamic authority, but agent tool interfaces rarely provide the agent's planner, the component that chooses its actions, a means of comparing the authority required by alternative actions or of seeing the cost of the authority it already holds. Drawing on the rich history of access control research, we propose the concept of \emph{elastic least privilege}, in which an agent begins with a small baseline of authority and may acquire more within an owner-defined envelope. Elevations are leased and measured against a replenishing budget. Their cost increases with power, proximity to mandatory safety invariants, and repeated requests. Costs are visible to the planner, which can prefer lower-privilege choices and release authority it no longer needs. Authority returns automatically to the baseline when a lease expires, when it is released, or when the budget is exhausted, while persistent legitimate demand may prompt an owner-approved change to the baseline. Building on prior risk-priced and budget-aware access control, we redesign these mechanisms for agents. How best to implement the approach and how well it works in practice are open research questions. In this paper, we present how the approach could work, illustrate the model, and set an open research agenda.

---


### 27. [RC Prediction: A Python Package for Parameter-Aware Reservoir Computing](https://arxiv.org/abs/2610.40984)

**<font color=#1a73e8>作者：</font>** Jin-Cheng Rao, Zheng-Meng Zhai, Ying-Cheng Lai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A nonlinear dynamical system can be characterized by the autonomous evolution of its state in time and its dependence on system parameters. As a parameter varies, the dynamics can change quantitatively and, at bifurcation points, qualitatively. When the governing equations are unknown, a data-driven model should therefore capture both elements from observational data, rather than reproduce the dynamics at a single operating condition only. Parameter-aware reservoir computing (PARC) is a model-free framework for this purpose, where the parameter is supplied to a reservoir computer through an additional input channel. PARC is trained on time series recorded at several parameter values, and the trained reservoir, run in closed loop as an autonomous dynamical system, generates trajectories at parameter values that were never observed. rc_prediction is an open-source Python package that implements this workflow. It provides multi-parameter training of a reservoir, autonomous closed-loop prediction at user-specified parameter values, parameter scans, and a standard echo state network for forecasting at a fixed parameter. Hyperparameter optimization and optional GPU acceleration through PyTorch are also provided. We use three benchmark dynamical systems as examples to demonstrate its usage. As one of the featured applications, here we illustrate the prediction of critical transitions and system collapse: trained only on pre-critical data, the model is queried beyond the training range to predict whether the system collapses, to estimate the critical parameter $p_c^{*}$, and to characterize transient lifetimes.

---


### 28. [A Robust Approach to Belief Mismatch in Non-cooperative Dynamic Games](https://arxiv.org/abs/2610.40999)

**<font color=#1a73e8>作者：</font>** Ryan Park, Li-huan Shen, Jesse Milzman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Game-theoretic models are increasingly used to describe multi-agent interactions in control and robotics applications. However, theoretical and computational complexity makes these models intractable in many dynamic, incomplete information scenarios. Recent work makes strong assumptions to reduce computational complexity: agents share sensor measurements with one another and maintain a common estimate of state uncertainty. Unfortunately, these assumptions enforce a degree of cooperation in generically noncooperative interactions. This paper takes the perspective of an ego agent seeking both computational tractability and robustness to unanticipated behavior of other agents due to mismatched state estimates from private---rather than shared---sensor measurements. To that end, we formulate the game theoretic planning problem in an augmented belief space with perturbed Bayesian dynamics that allows the ego to predict all agents' potentially divergent state estimates. These perturbations are chosen by a hypothetical adversary, ``nature,'' to reflect how non-ego agents' state estimates---based on measurements the ego agent will not see at runtime---may deviate from the ego's own belief. Ultimately, our approach can be understood in the spirit of classical H-infinity robust control, extended to noncooperative, stochastic dynamic games. We present a solver with polynomial-time iterations and conduct two experiments which show how robust belief space reasoning leads ego agents to proactively limit their future vulnerability to model misspecification of other agents' beliefs and actions, reducing performance degradation by over 48%.

---


### 29. [When Can Unlabeled Data Pools Replace Membership Queries?](https://arxiv.org/abs/2610.41001)

**<font color=#1a73e8>作者：</font>** Dravyansh Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Membership queries let a learner label arbitrary points and give near-optimal $\tilde O(n\log(1/\eps))$ label complexity for halfspaces under every marginal. A pool learner may label only sampled points. We ask when unlabeled data can replace membership queries. For homogeneous halfspaces the answer depends only on the angular law of $X/\|X\|$. If this law assigns zero mass to every hyperplane through the origin and positive mass to every nonempty open set of directions together with its reflection, a pool learner uses $O(n\log^3n\log(n/(\eps\delta)))$ labels, uniformly over all such marginals and targets, without density, moment, concavity or isotropy assumptions. The same label bound holds for non-homogeneous halfspaces under every marginal with full support and no mass on affine hyperplanes, including Gaussians. Dropping either angular assumption admits $\Omega(1/\eps)$ pool versus $O(\log(1/\eps))$ membership-query separations, even with unlimited unlabeled data. The price is paid in unlabeled data: in dimension $n\ge3$, for every unlabeled budget fixed in advance, some marginal satisfying both assumptions forces $\Omega(1/\eps)$ labels. For isotropic $s$-concave marginals in dimension $n\ge3$, unlimited pools keep logarithmic label rates for every finite $s$. With an unlabeled budget fixed in advance, class-uniform polylogarithmic rates hold exactly for $s>-1/(n+1)$, or $s>-1/n$ under central symmetry, and in the general class the optimal rate between these thresholds is $\tilde\Theta(\eps^{-(n-2)/n})$. This extends the range $s\ge-1/(2n+3)$ of previous sample-based guarantees, in the realizable setting.

---


### 30. [MOSAIC: Addressing Disproportionate Task-Modality Dependencies via Modality-Partitioned Gradient Routing](https://arxiv.org/abs/2610.41004)

**<font color=#1a73e8>作者：</font>** Aryan Chowdhury, Yizheng Sun, Thomas Carroll 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In multi-task settings, combining multiple modalities allows task representations to draw on signals that a single modality alone would not capture. However, individual tasks may depend disproportionately on particular modalities, a structure that conventional fusion-based architectures do not model explicitly, instead enforcing a unified representation space. Consequently, a task's gradients can affect parameters tied to modalities it barely relies on, leaving features that compromise between competing demands. Although prior work has explored task-weighting and loss-balancing strategies, their effectiveness is limited by the absence of explicit modality separation, preventing models from optimising each modality according to its task-specific importance. To address these limitations, we propose MOSAIC (MOdality-Separated Architecture with Inter-modal Cross-attention), which preserves unimodal representations while enabling controlled interaction between them, and uses modality-specific losses to route gradients to their corresponding partitions. On the Corpus of Everyday Japanese Conversation (CEJC), MOSAIC improves average macro-F1 by 7.4 points across four tasks with a 72% reduction in backbone parameters relative to a fusion-based baseline. Our results demonstrate that modality partitioning yields consistent gains across tasks while requiring far fewer backbone parameters than a fusion-based design.

---


### 31. [Adaptive Dynamic Security for Operational Technology Against AI-Powered Attacks](https://arxiv.org/abs/2610.41007)

**<font color=#1a73e8>作者：</font>** Mohamed Chahine Ghanem  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Operational technology now faces attackers whose tempo is set by AI. We present ADS-OT, an adaptive dynamic security framework modelling defensive posture as a partially observable decision problem. A reinforcement-learning policy adapts monitoring, access, deception, and segmentation under a safety-governance layer, reducing attack-path completion, detection, and containment versus static baselines.

---


### 32. [Prior-Guided Single-Exposure HDR Novel View Synthesis via Base-Gain Representation](https://arxiv.org/abs/2610.41011)

**<font color=#1a73e8>作者：</font>** Armin Shafiee Sarvestani, Sheyang Tang, Jialu Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-exposure high dynamic range (HDR) novel view synthesis (NVS) recovers HDR scenes from low dynamic range (LDR) views captured at a single exposure and estimates camera response function (CRF) for LDR re-exposure. Without HDR ground-truth, using single-exposure LDR views as the sole source of direct supervision underconstrains HDR reconstruction and cannot ensure its faithful recovery, motivating the need for learned LDR-to-HDR reconstruction priors. Moreover, single-exposure LDR views supervise CRF only over a limited range, necessitating a learnable prior for reliable re-exposure beyond it. We propose PriorGS, a 3D Gaussian Splatting framework that addresses both challenges by (1) guiding HDR recovery with pseudo-HDR supervision from 2D single-exposure HDR reconstruction methods while anchoring it to input LDR views through a closed reconstruction loop; and (2) regularizing CRF modeling with a learnable prior that guarantees monotonicity and promotes plausible responses. Yet cross-view inconsistencies in independently generated pseudo-HDR targets impair scene reconstruction when HDR is encoded directly as Gaussian's color attribute. We therefore introduce a 3D base-gain HDR representation that factors HDR radiance into an LDR base and an overlaid 3D gain field, promoting robustness to such inconsistencies and enabling 3D HDR appearance editing. Extensive experiments demonstrate PriorGS's substantial superiority over baselines.

---


### 33. [Violet Teaming in Practice: Lessons from a Pilot Expert Workshop on Governing Complex AI Systems](https://arxiv.org/abs/2610.41018)

**<font color=#1a73e8>作者：</font>** Steph Batalis, Kait Connors, Ben C. Snyder 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Violet teaming has been proposed as a method to integrate technical, policy, and societal considerations into the evaluation of emerging technologies. Here, we document a pilot expert workshop used to explore violet teaming as a governance methodology for biodefense-relevant AI capabilities and describe observations from the exercise. The workshop used a hypothetical technology scenario across three sequential stages - capability development, misuse potential, and implementation - while incorporating technical, security, operational, and policy perspectives. The sequential format provided an integrated way to examine potential benefits, misuse risks, and real-world implementation challenges, rather than considering these issues in isolation. The exercise surfaced non-obvious misuse pathways, expanded potential interventions beyond purely technical safeguards, and highlighted operational and policy constraints that could affect implementation. This report summarizes the workshop design, outputs, and lessons learned for applying violet teaming to the evaluation of complex, dual-use technologies.

---


### 34. [Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning](https://arxiv.org/abs/2610.41022)

**<font color=#1a73e8>作者：</font>** Shashank Gupta, Pilhwa Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models allow reinforcement learning agents to learn policies from imagined trajectories, yet determining the optimal depth of model reliance remains a fundamental challenge. Fixed imagination horizons apply uniform prediction depths regardless of trajectory reliability, exposing target values to compounding model error or over-relying on critic approximations. We introduce density-guided bootstrap boundaries, a trajectory-dependent mechanism that adapts the depth of imagined returns using a score-informed relative density proxy. The proxy accumulates the estimated divergence of a score-corrected auxiliary field formed by a feature displacement network and a noise-conditioned score estimator along imagined paths. We propose two gating mechanisms: a hard boundary that halts return expansion at a discrete state, and a soft boundary that continuously shifts the return recursion toward critic bootstrapping. Both variants preserve boundary value estimates and apply corresponding survival weights to actor and critic losses. Formulated independently of specific dynamics models and instantiated within Dreamer V3, we prove that the resulting gated Bellman operator is a strict contraction mapping and that early bootstrapping monotonically reduces conditional target variance. We clarify the theoretical assumptions distinguishing our expansion proxy from exact path likelihoods. Across continuous-control tasks and Atari Pong, empirical evaluations show that dynamic boundary selection enhances sample efficiency and late-training performance over fixed-horizon and auxiliary-enabled baselines.

---


### 35. [Omniprediction for All Mixable Proper Losses and Beyond](https://arxiv.org/abs/2610.41023)

**<font color=#1a73e8>作者：</font>** Junyan Liu, Haipeng Luo, Lillian J. Ratliff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Omniprediction concerns the task of making predictions that are simultaneously accurate with respect to different losses. Earlier results by [CV09] show that in an online learning setting, $O(\log(|\mathcal{F}||\mathcal{L}|))$ regret is achievable simultaneously against every predictor in a finite predictor class $\mathcal{F}$ and for every loss in a finite class $\mathcal{L}$ of mixable proper losses, while recent advances [OKK25, FP26] show that $\widetilde{O}(\sqrt{T\log(|\mathcal{F}||\mathcal{L}|)})$ regret is achievable simultaneously for every loss in a finite class $\mathcal{L}$ of bounded losses.
In this work, we ask whether sublinear regret remains possible when $\mathcal{L}$ is an infinite class of proper losses. Our first result gives a negative answer in general: even when $\mathcal{F}$ contains only two linear predictors, it is impossible to achieve sublinear regret simultaneously for all bounded proper losses. We then show that $\widetilde{O}(T^{1/3}(\log|\mathcal{F}|)^{2/3})$ regret is achievable simultaneously for \textit{all} mixable proper losses and that this bound is optimal up to logarithmic factors. This optimal rate stands in stark contrast to the constant (in $T$) regret achievable for a finite class of mixable proper losses. Finally, we extend our algorithm to obtain a best-of-all-worlds result: in addition to the new regret guarantee for all mixable proper losses, the resulting algorithm simultaneously achieves the existing guarantees for finite loss classes. With appropriate choices of these finite classes, our algorithm simultaneously achieves constant regret for squared loss and log loss, $\widetilde{O}(T^{1/3}(\log|\mathcal{F}|)^{2/3})$ regret for all mixable proper losses, and $\widetilde{O}(\sqrt{T\log|\mathcal{F}|})$ regret for $0$-$1$ loss, all Lipschitz losses, all GLM losses, and other structured families.

---


### 36. [Dreams Are Cheaper Than Flights: Curated World-Model Data Improves Aerial Detection](https://arxiv.org/abs/2610.41030)

**<font color=#1a73e8>作者：</font>** Rugved Katole, Vedant Patil, Jenna Kline 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robot perception is increasingly data driven, yet field data is slow, costly, and sometimes disruptive to collect. Video world models offer a cheaper source: seeded with real frames, they extend a recorded scene into new footage with the deployment's sensor, altitude, and environment. We ask whether such synthetic data matches the utility of real field data and whether detectors trained with it perform in the field. Seeding a 7B-parameter world model with wildlife drone video, we more than double the training set with curated frames. On held-out videos from the same drones, mAP@50--95 rises 4.3\% when these frames are added to real data and 10.3\% when they replace it, and up to 33.5\% on an urban benchmark. Although an expert rejects an estimated 87.5\% of generated clips, the data costs about \$1,100 of GPU time, against more than \$3,200 of field labor alone for a less useful real training set. Synthetic data thus shifts data costs from fieldwork to compute.

---


### 37. [An Incentive-Aligned Trust-Centric Coordination Layer for Heterogeneous Blockchain Interoperability](https://arxiv.org/abs/2610.41032)

**<font color=#1a73e8>作者：</font>** Saeed Moradi, Sara Rouhani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The interoperability between permissioned and public blockchains is hampered by asymmetric privacy, trust, and governance assumptions. We propose a coordination architecture that decouples cross-domain trust management and privacy enforcement from underlying blockchain protocols, requiring no protocol-level modifications. The framework integrates cryptographic unlinkability mechanisms with incentive-compatible relay selection, combining stake-weighted participation and temporally accumulated reputation to align economic commitment with sustained correctness. We formalize the adversarial model and derive security and privacy properties for cross-domain coordination, demonstrating robustness against Sybil infiltration, collusion, and strategic stake concentration. Simulation-based analysis characterizes key design trade-offs between quorum thresholds, reputation memory, and anonymity parameters, indicating that privacy-preserving coordination can be achieved without degrading responsiveness or incentive stability when parameters are properly tuned.

---


### 38. [Before We Adapt: The Zero-Shot Generalization Bottleneck in Continual World Models](https://arxiv.org/abs/2610.41041)

**<font color=#1a73e8>作者：</font>** Amir Mesbah, Di Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual reinforcement learning (CRL) requires agents to operate under environmental changes while reusing prior knowledge whenever possible. We argue that model-based reinforcement learning provides a promising framework for this setting because learned world models (WMs) can, in principle, support change detection, knowledge reuse, adaptation, and acquisition of new knowledge. However, such benefits depend heavily on whether the learned model can generalize beyond the contexts in which it was trained. In this work, we propose to formulate this problem with a contextual Markov decision process in which context is decomposed into behavioral and physical components. This view organizes continual WM learning into reuse, adaptation, and acquisition of new knowledge. As a first step, we study direct reuse when behavioral rules remain unchanged. Using Dyna-Q and TD-MPC in controlled FourRooms tasks, we find that zero-shot reuse can degrade substantially under physical-context changes and that this behavior depends strongly on the observation representation used by the WM. Additional ablation studies and latent-space diagnostics suggest that learned representations do not automatically provide the invariances needed for reuse. These results identify representation generalization as an important bottleneck for reliable world-model reuse in CRL.

---


### 39. [Localizing predictive concepts encoded in neural representations via hierarchical testing](https://arxiv.org/abs/2610.41046)

**<font color=#1a73e8>作者：</font>** Viktoriia Huryn, Marco Simnacher, Jim Berend 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding which regulatory sequence motifs a genomic deep learning model has learned, with statistical error guarantees, is essential for trusting its use in downstream tasks such as variant effect prediction. Existing approaches to identifying which units in a trained network encode human- understandable concepts fall into two groups. Exploratory methods rank and visualize units but offer no statistical guarantee that the selected units are associated with the prediction target across the population of inputs. Testing-based methods test only single units or one pre-defined set of them, and do not control the error across the many sets of units. We introduce CUTTIE (Cluster-tree Unit Top-down Testing of Independence with Error control), which clusters the units of each layer into a tree and tests the clusters top-down with conditional independence tests, localizing information about the target while controlling the family-wise error rate. Thereby, we identify clusters that carry information about the target beyond the rest of the layer. For the units in the identified clusters, conditional attribution maps then reveal what motifs they encode. In a controlled simulation, the procedure identifies the clusters whose concepts affect the target. We apply the procedure to a convolutional model predicting cell-type-specific chromatin accessibility from DNA sequence, where the concepts encoded in the identified clusters map onto known regulatory motifs.

---


### 40. [Closing the Applied Cybersecurity Gap in Critical Infrastructure: A Cyber-to-Physical Security Assessment Framework for Water Systems](https://arxiv.org/abs/2610.41050)

**<font color=#1a73e8>作者：</font>** Halil Dursunoglu, Kaan Sulkalar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The integration of information technology and operational technology in water infrastructure creates pathways through which cyber compromise may affect physical service delivery. This study revisits the Applied Cybersecurity Gap (ACG) framework by evaluating an experimental Applied Cybersecurity Gap Index (ACGI) alongside the Cyber-to-Physical Propagation Rate (CPPR), defined as the proportion of initially compromised trials that produce a specified physical-impact outcome. The expanded evaluation comprises 2,160 synthetic trials across three water-network benchmarks, including EPANET Example Network 3 (Net3), and couples declared cyber-attack progression rules with hydraulic simulations. A source-trained machine-learning model evaluated on 247 compromised Net3 trials achieved ROC-AUC 0.772, PR-AUC 0.775, and F1 0.733, compared with 0.661, 0.642, and 0.704 for a scenario-only baseline. The configuration-cluster bootstrap interval for the ROC-AUC difference was 0.038--0.183. A separate 720-run Net3 hydraulic operating-point sensitivity analysis achieved the study's exploratory baseline pressure criterion in all reruns, preserved 717 of 720 physical-impact labels, and produced ROC-AUC 0.791 with the frozen source-trained model. Additional analyses examine the sensitivity of CPPR to the physical-impact threshold and assumed control-blocking probabilities, and demonstrate that the ACGI--CPPR association is partly induced by the simulation design rather than independently validated. The findings establish a reproducible simulation-based assessment workflow, but do not constitute field calibration of cybersecurity-control effectiveness or prediction of real-world utility incidents.

---


### 41. [Communication-Efficient Private Federated Reinforcement Learning with Post-Quantum Authentication for Vehicular Networks](https://arxiv.org/abs/2610.41055)

**<font color=#1a73e8>作者：</font>** Hojat Allah Salehi, Devrim Aras, Md Jueal Mia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated reinforcement learning supports cooperative vehicular routing without centralizing trajectory data, but model updates may reveal private information and incur communication overhead over intermittent vehicle-to-infrastructure links, particularly when post-quantum authentication is required. We study correlated private quantization, using complementary shared randomness between paired vehicles to reduce aggregation mean squared error while preserving the marginal parameter-level local differential privacy and one-bit communication cost of independent quantization. A tunable extension mixes shared and independent randomness to bound privacy leakage given paired outputs and shared-randomness side information. For this extension, Rényi differential privacy accounting establishes vector-level local differential privacy for one model upload even when pairings are revealed. Under matched vector-level privacy and identical local and global parameters, the extension yields 16.5% lower analytical aggregation mean squared error than independent quantization. We evaluate cooperative routing by coupling traffic simulation with packet-level simulation of post-quantum-authenticated vehicle-to-infrastructure communication. Compared to full-precision updates, one-bit uploads reduce authenticated uplink size by 92.4% and increase mean verified updates aggregated per round from 19.6 to 26.5. Under mobility-constrained communication at a parameter-level privacy budget of 1, correlated private quantization reduces mean travel time by 14.3% relative to independent quantization at the same budget and communication cost. At a parameter-level privacy budget of 0.3, a vehicle-origin inference attack trained on independent simulations reaches 30% accuracy with correlated private quantization and 22% with independent quantization after 100 rounds, versus 91% without privacy and 10% for random guessing.

---


### 42. [Nonlinear Maps Between Irreducible Representations in Graph Neural Networks](https://arxiv.org/abs/2610.41059)

**<font color=#1a73e8>作者：</font>** Mani Shayestehfar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant linear maps cannot mix non-isomorphic irreducible representations, whereas nonlinear activations can. We develop a degree-resolved version of this nonlinear interaction picture and use the resulting block inventory to construct Specht Triple, a residual on unordered graph triples. On a synthetic structural benchmark with a frozen GIN backbone, Specht Triple reduces aggregate standardised test MSE by 11.05% relative to a parameter-matched Projector Control using the same irreducible projectors and complete linear equivariant space. The results support irreducible decomposition as an inductive bias for nonlinear higher-order equivariant processing.

---


### 43. [Segment Anything Pancreas: A Unified MRI Segmentation Model for Pancreatic Cancer Radiotherapy](https://arxiv.org/abs/2610.41063)

**<font color=#1a73e8>作者：</font>** Zach Eidex, Mojtaba Safari, Kundan Thind 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Limited tumor annotations and incomplete labels across MRI datasets hinder unified segmentation of pancreatic tumors and organs at risk (OARs) for MRI-guided radiotherapy. Purpose: We propose Pancreas-MedNeXt, a unified model that segments the whole pancreas, its subregions, tumors, and surrounding OARs from one MRI volume. Methods: The model uses a shared MedNeXt encoder-decoder with supervised whole-pancreas and subregion pretraining, followed by multitask fine-tuning. Three output heads predict the pancreatic subregions, tumor, and OARs (stomach, duodenum, kidneys). An annotation-aware loss allows training on partially labeled data without treating unannotated structures as background. Pancreas and tumor were evaluated by three-fold cross-validation on 142 PANTHER patients (92 diagnostic, 50 MR-Linac), subregions and OARs on Cyst-X and AMOS test sets, and pancreas and OARs on 33 external T1-weighted TotalSegmentator scans. Comparisons with nnU-Net, MedNeXt, VISTA3D, and Swin UNETR used the Dice similarity coefficient (DSC) with paired bootstrap 95% CIs. Results: Pancreas-MedNeXt achieved the highest mean pancreas and tumor DSC on diagnostic and MR-Linac MRI. Tumor DSC was 58.41% and 42.55%, exceeding task-specific MedNeXt by 4.94 (95% CI: 0.28-9.45) and 5.89 (95% CI: 2.37-9.72) percentage points, respectively. Whole-pancreas DSC was 85.73% and 70.66%. Pretraining improved head, body, and tail DSC by 2.01, 3.00, and 3.78 percentage points over training from scratch. It also achieved the highest DSC for the pancreas, duodenum, and right kidney on AMOS, and for all five organs on external MRI, exceeding the next-best method by 4.92-8.85 percentage this http URL: A single Pancreas-MedNeXt model segments tumors, pancreatic subregions, and OARs on diagnostic and MR-Linac MRI, which could streamline contouring for pancreatic cancer radiotherapy.

---


### 44. [Single-Annotation, Multi-Hypothesis Segmentation with Semantic-Spatial Residual Banks](https://arxiv.org/abs/2610.41069)

**<font color=#1a73e8>作者：</font>** Armin Dadras, Robert Sablatnig, Franziska Proksa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-rater segmentation datasets show that a single image can admit several valid masks, yet most training sets expose only one annotation per image. We study single-annotation multi-hypothesis segmentation: each training image exposes one fixed mask, while the model must return a finite bank that covers held-out human annotations at test time. Our experiments reveal a representation tradeoff. Banks learned directly from images recover variations in local boundaries and extent but lose structural hypotheses, whereas frozen semantic features preserve structural grouping but underrepresent spatial variation. We introduce the Semantic-Spatial Residual Bank (SSRB), which freezes a semantic bank trained with balanced assignments and learns a residual from the image for each hypothesis. Across five medical endpoints, SSRB improves coverage of held-out masks at $K=8$ over a Probabilistic U-Net under the same one-mask constraint. On LIDC and LIDC-hard, it also produces substantially more distinct useful masks. On BSDS, it preserves the semantic bank's performance in grouping regions. Its advantage grows as more masks are returned, showing that residuals learned for corresponding heads improve coverage of local annotation variation while preserving how regions are grouped.

---


### 45. [Where, When, and How Many Bits? Scaling Laws for SGD with Stochastic Rounding](https://arxiv.org/abs/2610.41074)

**<font color=#1a73e8>作者：</font>** Zhichao Wang, Michael W. Mahoney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-precision training reduces computation but introduces additional rounding error. We theoretically study how stochastic rounding (SR) affects prediction risk as model size, training time, and precision change. We consider a two-layer linear network with a fixed random first layer, trained by mini-batch SGD on fresh Gaussian data with power-law spectra. At each SGD step, the features used in forward and backward computations are rounded independently. We prove matched upper and lower bounds on prediction error for the final model and for uniform parameter averaging, with general learning-rate and precision schedules chosen before training. For fixed precisions and constant learning rates with parameter averaging, we derive how the smallest prediction error decreases with compute, and we identify model sizes and training times that achieve this optimal-compute scaling. Rounding only the forward features preserves the compute scaling of exact arithmetic, while rounding backward features changes it. Averaging parameters can change which computation needs higher precision and when higher precision is useful. Our results also give bit requirements for a given accuracy tolerance and show how backward rounding can change learning-rate schedule design. At a fixed compute budget, lower precision can improve prediction when the benefit of a larger model or longer training outweighs the additional SR-induced error. Model simulations illustrate these tradeoffs, and experiments with an MLP and a small transformer examine rounding choices beyond the theoretical model.

---


### 46. [Optimization Techniques for Solving the Minimum Red--Blue Separating Set Problem with an Application to Human--AI Text Separation](https://arxiv.org/abs/2610.41081)

**<font color=#1a73e8>作者：</font>** Marko Djukanović, Staša Vujičić Stanković, Žiga Zebec 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the so-called Minimum Red''Blue Separating Set Problem (MRBSSP) which arises from computational geometry. In particular, we propose a compact Set-Cover ILP formulation, safe preprocessing rules, a Greedy Randomized Adaptive Search Procedure (GRASP), and two exact approaches: one is based on Logic-Based Benders Decomposition (LBBD) approach, and the second represents a novel Branch-and-Benders-Cut (BBC) approach. These two exact approaches are compared to ILP--alongside GRASP and the Variable Neighborhood Search (VNS) from literature. Experiments on 250 random graphs with up to 500 vertices reveal complementary strengths: ILP yields the best feasible solutions, LBBD provides the strongest lower bounds and smallest mean optimality gap, and BBC certifies optimality most frequently. We further introduce an NLP application distinguishing human- and AI-generated texts through vocabulary-based graph features. On 42 instances, BBC achieves the smallest mean optimality gap, certifying 16 optima, while GRASP outperforms VNS. Structural analysis of optimal vocabulary separators identifies 113 mandatory and 151 replaceable features across 272 tests, highlighting substantial variability among optimal solutions. Overall, our results demonstrate the effectiveness of complementary optimization strategies and the interpretability of optimal vocabulary-based discrimination.

---


### 47. [Evaluating Structural and SAT Attack Resilience in Cryptographic Dynamic Logic Locking via Keystream Capping](https://arxiv.org/abs/2610.41083)

**<font color=#1a73e8>作者：</font>** Nahush Tambe, Naseeruddin Lodge, Vineet Chadalavada 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Untrusted third-party entities throughout the semiconductor supply chain expose proprietary hardware intellectual property to reverse engineering, piracy, and overproduction. While logic locking counters this threat by embedding key-dependent logic, conventional static key-gates remain vulnerable to both oracle-guided SAT attacks and structural removal attacks due to their time-invariant netlist signatures. Dynamic schemes such as STREAMLOCK mitigate oracle attacks by continuously masking signals with cryptographic keystream, achieving near 50\% Hamming distance output corruption under incorrect keys with low hardware overhead. However, confining key-gates to primary outputs leaves internal combinational cones vulnerable to single-tap structural bypasses. This work extends dynamic logic locking by distributing key-gates within internal paths prioritized via fault-propagation analysis. The original and internally-hardened architectures are evaluated against structural removal attacks and a bounded, unrolling-based SAT-style attack across three ISCAS'85 benchmarks. Distributing masking internally raises the uninformed attacker's brute-force search space from 6 candidate node subsets to over $10^{45}$ for the largest benchmark. Crucially, empirical analysis reveals that topological relocation alone does not prevent algebraic key extraction when wide circuits expose numerous keystream bits per clock cycle. To eliminate this leak, a keystream-bit reuse cap is introduced to restrict per-cycle exposure independent of circuit width. Under this constraint, SAT-solver tractability encounters an immediate computational cliff, transitioning sharply from rapid under-constrained solving to timeout thresholds without disclosing the secret key. Integrating fault-aware internal placement with keystream reuse capping delivers joint resilience against structural bypasses and bounded SAT attacks.

---


### 48. [Payroll Fraud Detection in Synthetic HR/ERP Graphs: An Inductive Comparison of Rules, Path Features, and Graph Neural Networks](https://arxiv.org/abs/2610.41085)

**<font color=#1a73e8>作者：</font>** Xiaobo Chen, Genliang Zhu, Ziyuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Payroll-fraud screening requires finding hidden employee--payee links while distinguishing suspicious relationships from legitimate ones. We formulate this problem as inductive link prediction and entity ranking on synthetic human-resources and enterprise resource planning (HR/ERP) graphs, with unseen organizations and a matched benign twin for every planted case. An original study on 24 held-out organizations and a prospectively frozen extension compare analyst rules, explicit path features and graph neural networks (GNNs). A tuned gradient-boosted model on chained-join features achieved the highest overall link average precision (AP; 0.823), above the GraIL-style GNN (0.663); its 4-hop AP was 0.646 versus 0.272. Thus, the observed multi-hop gain is not specific to GNNs. On a new synthetic cohort with 2.0% positive entities, chained-join boosting again led (AP 0.798); the relational entity GNN also exceeded record-aware rules (0.707 versus 0.504). At a 2% review budget, their precision was 0.695 versus 0.602. Under 40% failed identifier joins, the entity GNN ranked above chained-join boosting (AP 0.712 versus 0.683, descriptively). Structure-only auditing exposed a shortcut in the initial generator; matched twins reduced the audited twin-pool AUROC to 0.493--0.514. These results separate multi-hop candidate discovery, record-based discrimination and review prioritization within an explicit synthetic evaluation design. Code and data are available from the authors on request.

---


### 49. [Verifying Text-to-SQL Queries under Changing Business Semantics](https://arxiv.org/abs/2610.41090)

**<font color=#1a73e8>作者：</font>** Genliang Zhu, Xiaobo Chen, Ziyuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In text-to-SQL and AI-agent analytics, successful SQL execution does not establish semantic correctness under changing business definitions. We study revalidation of fixed queries after changes to refund attribution, tax treatment, eligible populations and exchange-rate dates. An executable verification profile binds the requested revision and knowledge cutoff to legal counterexample data and exact monetary comparison. A preregistered confirmation on 32 newly authored revision families and two local producer bundles retains 192 query-definition cells: 144 nonconforming, 36 finite-suite agreeing and 12 unresolved. Of the nonconforming cells, 63 agree on the current snapshot. At an eight-ledger budget, obligation-guided checking detects 137 discrepancies versus 127 for generic ordering, a paired difference of 6.9 percentage points (family bootstrap 95% interval [2.1, 13.6]; exact family sign-flip p=0.0156). Every ledger arm rejects zero of the 36 agreeing cells. Current-obligation and equal-weight scoring match the guided result, identifying coverage rather than revision-specific priority as the observed source of benefit. Controlled assays, a natural-query pilot and repeated samples provide separate mechanism and robustness evidence. A legal discrepancy refutes conformance; agreement remains restricted to the recorded suite. The study establishes an auditable business-semantic revalidation profile within its authored schema and local-model scope.

---


### 50. [Flash Word : ESL Listening Support with Subtitle Skimming](https://arxiv.org/abs/2610.41098)

**<font color=#1a73e8>作者：</font>** Yuzu Saijo, Jun Rekimoto  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Listening to English audio with English subtitles is thought to be effective for ESL students to improve listening comprehension skills. However, for those who learn English as a second language it can be hard to finish English subtitles. Also they are unlikely to focus on listening while being busy reading subtitles. We propose Flash Word, a subtitling system which generates and presents shortened intralingual subtitles for English audio by detecting keywords from the script. Flash Word extracts keywords from scripts using an existing algorithm, and shows them one at a time like a flashcard. The system calculates when the keywords are being pronounced and aligns them correctly. Flash Word aims to enable ESL students to focus better on listening by minimising the cost of reading subtitles.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-193](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
