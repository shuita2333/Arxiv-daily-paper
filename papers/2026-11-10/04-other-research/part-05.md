# 📦 其他研究 | 2026年11月10日

> 本类共 **222** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-222**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-222**

---

### 201. [Safety Is $Π_1$, Provability Is $Σ_1$: One Framework for the Hugging Face Breach and OpenAI's Mathematical Proofs](https://arxiv.org/abs/2611.09736)

**<font color=#1a73e8>作者：</font>** Jinho Kang, Jinsook Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> OpenAI's agents breached Hugging Face in July 2026, and the same company released more than seven hundred AI-generated manuscripts of mathematical proofs in October 2026. The first event is read as a failure in security, while the second is read as a success in mathematics. We read both through the hybrid framework of our paper (Kim and Kang, 2026, arXiv:2611.01914), in which coding, proving, and learning from data are derivations by one and the same deductive mechanism, distinguished by the kinds of premises from which they are derived. Under this framework, the AI systems behind the two events ran the same loop, in which a statistical proposer produces candidate exploits or proofs and a deductive verifier settles each one by a derivation. What separates the events is the logical form of the statement wanted by each of the two domains, security and mathematics. The safety of a program is a $\Pi_1$ statement, for it says that no exploit exists, which is not assured by any finite list of tests that have been passed by the program. By contrast, the provability of a sentence is a $\Sigma_1$ statement, for it says that a proof exists, which is assured by a single instance, namely a proof that has been checked by the deductive verifier. The theorem behind both is Turing's Undecidability Theorem: the halting set is $\Sigma_1$ but not decidable, so its complement is $\Pi_1$ and not $\Sigma_1$, which is to say that membership has a finite witness but non-membership has none. We prove that attaching a statistical proposer to a deductive verifier does not change this undecidability result, however good the proposer is. We then discuss what does assure safety and where the residual risk goes.

---


### 202. [Continuous wavelet-based feature extraction for laser-induced breakdown spectroscopy classification of human plasma samples](https://arxiv.org/abs/2611.09746)

**<font color=#1a73e8>作者：</font>** Md Mahmudur Rahman, Atqiya Munawara Mahi, Nazim Ahmed Belabbaci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extracting discriminative features from laser-induced breakdown spectroscopy (LIBS) spectra is important for the classification of complex biological samples. This study evaluates continuous wavelet transform (CWT)-based spectral peak extraction for distinguishing human plasma samples labeled as SARS-CoV-2-positive or negative. Plasma specimens from 181 individuals, comprising 53 positive samples and 128 negative controls, were deposited as 5 {\mu}L droplets on silicon substrates and dried before analysis. Spectra were acquired using a nanosecond Nd:YAG laser operating at 1064 nm, with 100 single-shot measurements collected per specimen and averaged after intensity-based outlier rejection. CWT-based peak detection was coupled with a support vector machine (SVM) classifier. The reported leave-one-out evaluation yielded an accuracy of 93.00%, sensitivity of 94.67%, and specificity of 91.61%; these estimates remain provisional pending reconciliation with specimen-level predictions. Features identified by the CWT pipeline included emission lines assigned to Ca II, K I, and N I. The workflow provides a basis for examining spectral features associated with the studied plasma groups. Independent validation and assessment of specimen, substrate, and acquisition-related variability are required to establish generalizability and diagnostic relevance.

---


### 203. [A lightweight convolutional neural network for target detection in an edge environment](https://arxiv.org/abs/2611.09756)

**<font color=#1a73e8>作者：</font>** Hughes Perreault, Ola Ahmad, Daniel Czuboka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a novel, lightweight convolutional neural network (CNN) designed for edge device deployment. The CNN is developed to recognize and classify threats or targets of interest. The model is equipped with a real-time hotspot detection algorithm, which enables it to process information quickly and accurately, resulting in improved inference time of up to 20 fps and a detection range of more than 400 meters with typical thermal situational awareness sensors. The proposed CNN has been rigorously tested and validated to demonstrate its high accuracy, sensitivity, and low false positive rate, providing a reliable solution for edge devices to detect potential targets. Additionally, the lightweight design of the CNN allows for easy deployment, making it an ideal solution for extending the security bubble for edge devices. The proposed model can be used for a variety of applications, including surveillance, security, and object recognition.

---


### 204. [Diffusion-free Score Matching for Exact Conditional Sampling](https://arxiv.org/abs/2611.09758)

**<font color=#1a73e8>作者：</font>** Thomas Wedenig, Robert Peharz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of modern score-based generative models is largely driven by diffusion-based training, which learns a collection of time-indexed score fields corresponding to progressively noisier versions of the data distribution. While such models achieve impressive sample quality, leveraging them for sound probabilistic inference---particularly sampling from arbitrary conditionals of the model---remains challenging. This difficulty arises because conditioning information is only available for clean data and not for the higher noise levels required to generate exact conditional samples. In this paper, we introduce DIffusion-free SCOre matching (DISCO), a principled approach that sidesteps the need for time-dependent score fields altogether. Our method is based on an objective that, while reminiscent of diffusion-based training, estimates only a single score of the (slightly perturbed) data distribution, for which the exact conditional score is readily obtained. In experiments, DISCO is competitive with state-of-the-art diffusion models in terms of sample quality. More importantly, DISCO yields a more faithful representation of the underlying data distribution and---crucially---enables accurate sampling from arbitrary conditionals, outperforming standard heuristic samplers. This capability opens the door to principled and flexible probabilistic reasoning with score-based models.

---


### 205. [From PAC bounds on the generalization error to PAC bounds on the parameter estimation error](https://arxiv.org/abs/2611.09767)

**<font color=#1a73e8>作者：</font>** Mihaly Petreczky, John Leth, Emma Lukacs 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probably Approximately Correct (PAC) bounds on the generalization error (the difference between the empirical prediction error computed on the training data and its expectation) are an established tool in statistical machine learning, and there have been several extensions of these bounds to dynamical systems. In parallel, in recent years, there has been growing interest in finite-sample bounds for parameter estimation error in system identification. The latter bounds tend to be algorithm-specific, relying on reformulating the identification algorithm as a least-squares regression problem. This is in contrast to classical PAC bounds, which are algorithm-agnostic and can be applied to any identification algorithm based on minimizing a cost function involving the empirical loss.
In this paper, we show how oracle bounds derived from PAC bounds can be used to derive finite-sample bounds for dynamical systems. As an illustration of this approach, we present finite-sample parameter-estimation bounds for linear and bilinear systems with bounded inputs and noise. These bounds apply to identification algorithms based on minimizing a regularized empirical loss function.
The key ingredient is to establish an oracle inequality, i.e., an inequality between the true prediction error of the learned model and the minimum achievable true prediction error, and then use either the convexity of the true loss or system-theoretic properties of the loss function to derive bounds on the parameter estimation error. We also analyze the rates of the obtained bounds and compare them with those of classical asymptotic results.

---


### 206. [A Cross-Domain TARA-to-NAC Rule Mapping Methodology: From Automotive OEM Networks to Energy Storage Systems](https://arxiv.org/abs/2611.09771)

**<font color=#1a73e8>作者：</font>** Krishna Teja Medam, Thiago Quinelato  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Threat analysis and risk assessment under ISO/SAE 21434 ends with cybersecurity goals, but existing methods give little structured guidance for turning those goals into enforceable network access control rules. Compliance standards such as IEC 62443, ISO/SAE 21434, and ISO/IEC 27001 are usually applied as parallel efforts rather than as one enforcement architecture. This paper presents a six-step methodology that maps cybersecurity goals from a threat analysis and risk assessment to network access control rules, each placed at a named enforcement point and traceable to the threat records behind it. It also presents a unified compliance framework that treats IEC 62443 and ISO/IEC 27001 as a fixed substrate and domain-specific regulation as an interchangeable overlay. The methodology is applied to an automotive original equipment manufacturer plant network, addressing multi-tier supplier authorization and legacy operational technology devices, and then to utility-scale battery energy storage, where North American Electric Reliability Corporation Critical Infrastructure Protection standards and ISO/IEC 27019 replace the automotive-specific standard while the substrate stays constant. In the automotive example, 37 threat entries and 24 cybersecurity goals yield 23 rules covering 11 of the 13 in-scope goals; the energy example yields six rules. Three derived rules have no equivalent in the cited standards. Both examples are desk-based: the methodology is applied to them, not tested on them. The result is a reusable pattern for translating risk assessment into enforcement across critical infrastructure sectors, with empirical validation left as future work.

---


### 207. [Quasipolynomial-Time Planning for Decodable POMDPs](https://arxiv.org/abs/2611.09778)

**<font color=#1a73e8>作者：</font>** Oliver Dobson, Varun Jog, Chun Hei Michael Shiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study planning for finite-horizon partially observable Markov decision processes (POMDPs) with finite state, action, and observation spaces. Both exact and approximate planning are known to be computationally hard in this setting, so prior work has explored natural assumptions that make planning easier. Recent work [Golowich et al., 2022] gave quasipolynomial-time approximate planning algorithms for observable POMDPs. These are POMDPs whose observation channels satisfy an $\ell_1$-observability condition, but notably, no assumptions are required on the transition dynamics. In a similar vein, for every fixed $\rho>0$, we give quasipolynomial-time approximate planning algorithms for $\rho$-decodable POMDPs. We show that decodability is implied by both $\ell_1$- and $\ell_2$-observability and is strictly weaker than observability. Moreover, we show that the optimal decodability constant can be computed in polynomial time, whereas computing the optimal $\ell_1$-observability constant is NP-hard in the worst case. We also show that the fast filter-forgetting guarantee underlying the approach of [Golowich et al., 2022] does not extend directly from $\ell_1$-observability to constant $\ell_2$-observability. Thus, decodability is an easy-to-check, unifying assumption under which quasipolynomial-time approximate planning for POMDPs is possible.

---


### 208. [Knowing When to Intervene: Causal Evaluation of AI Agents](https://arxiv.org/abs/2611.09792)

**<font color=#1a73e8>作者：</font>** Ayush Sawarni, Wenqian Xing, Tijana Zrnic 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current evaluations of agentic AI systems primarily rely on benchmarks. However, the static nature of benchmarks makes them uninformative about the value of auditing interventions at deployment time. For reliable deployment, we often need to determine within an agent's trajectory whether or not to intervene, e.g., by verifying the agent's current output or steering it toward different behavior, using either human review or more costly models or time-consuming agentic supervision. The value of such interventions is fundamentally a causal inference question, asking whether the causal effect of such an intervention is beneficial for the final outcome. Estimating this causal effect is particularly challenging due to the dynamic nature of the problem: the impact of an intervention depends on the current context and environment, as well as the agent's future behavior. We develop the first methodologically grounded framework for evaluating the causal effects of randomized interventions within agent trajectories. By leveraging a relatively small dataset of agent trajectories collected under randomized interventions such as verification or screening, we can estimate the dynamic causal effect of a rich class of (contextual) intervention policies. The structural parameters that we estimate can also be used to construct safety leaderboards that capture the risk of various agentic actions, which can be used by practitioners for audit prioritization. Applying our methods to tau-bench Retail, ToolSandbox, and ImpossibleBench, we find that intervention effects vary substantially across agent actions and states. More broadly, our work suggests a rich research agenda at the intersection of causal inference and agentic evaluation, which we believe is essential for the reliable and safe deployment of AI agents in the real world.

---


### 209. [AR-Edit: Training-Free Autoregressive Video Editing without Inversion](https://arxiv.org/abs/2611.09795)

**<font color=#1a73e8>作者：</font>** Hovhannes Margaryan, Quentin Bammey, Christian Sandor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Editing a video stream in real time, without access to future frames, is essential for interactive applications. Existing training-free video editing methods, however, assume full offline access to the entire sequence, while streaming approaches either rely on additional training or are limited to specific editing techniques. We show that this limitation can be removed by analyzing the self-attention dynamics of DMD-distilled autoregressive (AR) video diffusion models. We uncover a key asymmetry: queries and keys remain stable and aligned with their source counterparts across denoising timesteps, while values diverge and encode the evolving content. Inherited from the non-distilled bidirectional teacher, this asymmetry is strongest at high noise, where few-step streaming models operate. The resulting mechanism is simple: a single forward pass suffices to capture source identity in the value features, which can be reused throughout generation. Starting from pure Gaussian noise and injecting only these source values reconstructs the input with fidelity matching or surpassing inversion-based methods, effectively eliminating inversion. Based on this insight, we introduce AR-Edit, a training-free, inversion-free method that caches source values once and selectively injects them during denoising. Across multiple AR backbones, AR-Edit enables real-time streaming editing with superior source preservation and tonal fidelity at minimal overhead.

---


### 210. [Scaling Graph Similarity Learning with Graph Neural Networks](https://arxiv.org/abs/2611.09805)

**<font color=#1a73e8>作者：</font>** Ahmet Tüzen, Helge Langseth, Kjetil Nørvåg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph similarity computation is an important task in graph mining with many real-world applications, such as chemical compound analysis, program dependence comparison, and social network analysis. The problem is computationally challenging: Graph Edit Distance (GED) and Maximum Common Subgraph (MCS), which quantify the distance between graphs and identify their largest shared subgraph, respectively, are NP-hard to compute exactly. To address these computational challenges, Graph Neural Networks (GNNs) have been applied to this problem. However, existing GNN-based approaches have primarily focused on small-scale graph datasets, while scalability to larger scales remains underexplored. In this work, we propose FiLSim, a scalable GNN-based framework, and investigate whether a simplified GNN pipeline can maintain competitive performance on standard benchmarks while scaling to large graphs. We additionally propose a sequential graph-editing strategy to construct large-scale graph datasets with reliable GED labels to evaluate scalability. The proposed framework is evaluated on four benchmark datasets and four newly created large-scale datasets, demonstrating its effectiveness and scalability. FiLSim remains accurate on graphs with more than 150{,}000 nodes, where the baseline methods run out of memory or fail to learn, and scores all test pairs within seconds on a single GPU.

---


### 211. [The Cost of Coverage: Conformalising Native Forecast Uncertainty for GB Wind Power](https://arxiv.org/abs/2611.09815)

**<font color=#1a73e8>作者：</font>** Carl Somers  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty bands on wind forecasts help inform reserve sizing and commitments, but often fail to deliver their stated coverage. We apply conformal prediction to native bands to see what it adds and what it costs, comparing six forecasters, from ARIMA to a tabular foundation model, at two wind farms in Great Britain (GB) under operational conditions. We show that calibration repairs empirical marginal coverage with little or no Winkler Score penalty, but this apparent success conceals under-coverage in high winds. Calibrating by forecast wind regime turns marginal coverage into regime-level coverage, cutting day-ahead out-of-band volume in high winds by over 40% relative to pooled calibration while narrowing bands overall.

---


### 212. [Can Agentic Systems Close the Gap in Radiology with Production AI Tools?](https://arxiv.org/abs/2611.09836)

**<font color=#1a73e8>作者：</font>** Aubin Charley, Julien Khlaut, Charles Corbière 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Radiology AI has developed along two paths: specialized models that perform well on narrow tasks but cover few clinical findings, and generalist models that address a broader range of tasks but remain prone to hallucination and inaccurate measurements. Combining the two through agentic systems offers a route towards comprehensive radiology reporting, but published systems are tied to one modality or body part. We describe a radiology agentic framework that standardizes how an orchestrator calls modular tools to produce a structured report, and use it to measure what such a system can do with the tools from FDA-cleared radiology AI devices. Report generation is simulated on a large multi-modality report corpus, with the orchestrator given either a catalog of finding classes consolidated from the cleared devices, each available on the modalities it is cleared for, or an unlimited catalog in which any class can be requested, and planning either from the clinical indication or from the target report. Tool outputs are simulated from the reference report, so the comparison isolates tool availability and orchestration from tool error. With the cleared catalog and the indication alone, the orchestrator recovers under a third of the clinically actionable findings; recovery improves substantially with the unlimited catalog, and further when the plan is written from the target report. Attributing every missed finding to a cause shows that most are classes no cleared device offers for the study's modality, and that a third are classes or tools that were offered and not called. Adding the most frequently missing tools closes most of the gap to the unlimited catalog on held-out reports, whereas a smaller orchestrator with the unlimited catalog gives up the whole gain. Tool availability and effective orchestration are thus complementary constraints on comprehensive AI-assisted radiology reporting.

---


### 213. [Fifty-Two Shades of Pig: What the UCR Archive Really Asks Classifiers to Do](https://arxiv.org/abs/2611.09843)

**<font color=#1a73e8>作者：</font>** Omar Swelam, Jaris Küken, Shi Bin Hoo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The pigs were bleeding. That was the point of the experiment: could airway pressure reveal hemorrhage before it became critical? In the UCR Time Series Classification Archive, the de facto benchmark for Time Series Classification (TSC), the same recordings ask a different question: "which of 52 pigs produced this trace?". The dataset PigAirwayPressure is not an outlier. Although the archive is the standard benchmark, whether its tasks resemble the problems TSC is meant to solve has rarely been examined. We find that several datasets are repurposed from their original task, built from toy setups, or have flawed test splits. We further question how representative the archive's ordered non-temporal sequences (e.g. spectra, shape outlines) are of real TSC, and the potential downsides from the decomposition of multivariate problems. Our findings call for more careful interpretation of archive-wide scores and greater attention to deployment-relevant evaluation. The audit is at this https URL.

---


### 214. [Health-System-Wide Mapping of Demographic Information in Routine Clinical Histopathology](https://arxiv.org/abs/2611.09851)

**<font color=#1a73e8>作者：</font>** Shengjia Chen, Ruchika Verma, Kevin Clare 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The extent to which demographic-associated information is detectable across organs and disease states in routine clinical histopathology remains unclear. Here, we analyzed 1.3 million hematoxylin and eosin whole-slide images from 257,322 patients across 25 organs, using pathology foundation-model representations and multiple-instance learning to systematically map information associated with sex, age group, and self-reported race. Across 69 organ-demographic combinations, demographic attributes were broadly recoverable, with pan-organ mean AUROCs of 0.828 for sex, 0.733 for age group, and 0.662 for self-reported race, and substantial variation across organs. Demographic-class balancing produced relatively small changes in performance, while evaluation within diagnosis-text clusters showed modest attenuation. Under training with diagnosis-based grouping, demographic-associated signals remained detectable across multiple organs, including sex in gastric tissue (AUROC 0.865), age group in breast (0.816), and self-reported race in skin (0.728). Literature-guided analysis of these settings generated candidate histomorphological and contextual explanations for further investigation. Together, these findings provide a systematic map of demographic-associated information in routine histopathology, informing investigations of its sources, assessments of potential shortcut learning, and the development of more interpretable computational pathology models.

---


### 215. [Flow-Guided Target-Space Alignment via Path Consistency](https://arxiv.org/abs/2611.09863)

**<font color=#1a73e8>作者：</font>** Ruizhi Yuan, Zeqiu Yu, Wei Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many multimodal alignment problems require mapping a source modality into a fixed space defined by a target modality, where the target space is not merely an intermediate embedding but is used directly for downstream analysis. In this setting, successful alignment should preserve both the global structure of the target distribution and the instance-level correspondence observed in paired source--target training data. Existing objectives typically address only part of this goal: contrastive losses encourage relative similarity, distribution-matching losses improve marginal agreement, and pointwise regression fits each source sample to its paired target without explicitly modeling target-space path geometry. We propose FlowAlign, a flow-guided target-space alignment method that repurposes conditional flow matching as a training-time alignment signal rather than an inference-time transport model. FlowAlign uses the learned flow field to guide the alignment of source-side representations with the fixed target space, encouraging them to preserve paired correspondence while remaining compatible with the global target-space structure. We further provide theoretical analysis showing how FlowAlign helps improve paired correspondence by controlling endpoint accuracy and capturing local target-space geometry. Experiments on synthetic data, paired single-cell multiome benchmarks, and image--text alignment demonstrate that FlowAlign improves instance level correspondence while preserving target-space structure across different modality settings.

---


### 216. [GRAC: Graph-Based Retrieval-Augmented Captioning for Surgical Scene Description](https://arxiv.org/abs/2611.09866)

**<font color=#1a73e8>作者：</font>** Rochak Dhakal, Chen Zhao, Soup Cobb 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Surgical operative reports support procedural documentation, surgical training, performance assessment, and workflow review. However, extracting meaningful information often requires extensive manual review and clinical expertise. Automated surgical scene descriptions could reduce this burden by leveraging recurring surgical activities and prior knowledge.
Methods: We propose GRAC (Graph-Based Retrieval-Augmented Captioning), a framework that represents surgical scenes as graphs capturing relationships among instruments, actions, and anatomical structures. Given an input scene graph, GRAC learns to retrieve relevant graph-caption pairs from training data. It compares instrument-tissue interactions between retrieved examples and the input scene, using comparison features to condition retrieved-caption representations during generation.
Results: On the EndoVis-18 benchmark, GRAC achieved a CIDEr-D of 5.88, compared with 4.23 for SGT and 3.36 for the strongest conventional Transformer baseline. Exact instrument-action-target triplet-set accuracy reached 52.6%, compared with 32.7% for SGT and 26.2% for the strongest conventional baseline. These results demonstrate improvements in language quality and factual agreement. On TORS, GRAC achieved a CIDEr-D of 5.06, compared with 3.80 for the strongest baseline.
Conclusion: GRAC demonstrates that combining structured surgical scene representations with retrieved examples improves surgical scene captioning and produces more contextually meaningful descriptions.

---


### 217. [Graded convolutional networks: scale invariance without the scale and robustness to unknown blur](https://arxiv.org/abs/2611.09878)

**<font color=#1a73e8>作者：</font>** Tanush Shaska  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Gaussian jet of an image is a graded vector space: a dilation by $\lambda$ multiplies derivatives of order $k$ by $\lambda^{-k}$. Local graded convolutions are exactly homogeneous differential operators, and a local feature is dilation-invariant if and only if it factors through the scale-normalized jet or, without the scale, through the retraction onto the weighted sphere of the grading. Under unknown Gaussian blur the retraction changes only by a change of scale, whereas the scale-normalized jet acquires a grading factor that no radial normalization removes. At the zero jet the retraction separates image families that radial normalizations and continuous classifiers cannot. Networks built on the retraction are universal for invariant features. On MNIST such a network keeps 88.4% accuracy under a two-pixel blur, against 66.2% for the same network on scale-normalized derivatives; in Lindeberg's Gaussian derivative network the retraction raises accuracy at that blur from 91.5% to 95.1%.

---


### 218. [PhotoFinish: Portable Timerless Probing of Microarchitectural Latencies](https://arxiv.org/abs/2611.09879)

**<font color=#1a73e8>作者：</font>** Tristan Hornetz, Eduard Ebert, Lorenz Hetterich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Timing measurements are a fundamental building block of microarchitectural attacks, enabling software to convert otherwise invisible latency differences into architectural observations. Thus, restricting high-resolution timers is a common defense, especially in constrained environments such as web browsers. Timerless probing primitives provide an alternative approach. Instead of reading or constructing a timer, they observe architectural events that correlate with the microarchitectural state. However, such primitives typically rely on platform-specific behavior, and none generalizes across the wider computing landscape. In this paper, we present PhotoFinish, a portable timerless probing primitive that converts latency differences directly into an architectural value. PhotoFinish races an operation under test against a fixed reference in two parallel threads that then write unique values to the same shared location, resulting in a latency-dependent architectural value. PhotoFinish only requires parallel execution and shared memory, without constructing or reading a clock. We evaluate PhotoFinish on 38 CPUs spanning four ISAs and demonstrate reliable cache state classification across widely different microarchitectures, with comparable fidelity when compiled to WebAssembly and executed inside a browser. We further use PhotoFinish in AES T-table and Evict+Reload attacks, show that it applies beyond caches to TLB and execution-engine latencies, and demonstrate sufficient precision to identify the LLC slice of an address. Our results demonstrate shared-memory races as a generic and precise replacement for explicit timing, showing that restricting timers alone does not prevent software from observing fine-grained microarchitectural latency differences.

---


### 219. [ZeoBench: A Benchmark for Self-Supervised Learning on 3D Zeolite Representations](https://arxiv.org/abs/2611.09880)

**<font color=#1a73e8>作者：</font>** Aaron Sun, Yachan Liu, Ping Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zeolites are an important class of porous crystalline materials with broad applications in gas storage, separations, and catalysis. Although hundreds of thousands of experimentally realized and hypothetical zeolite structures are known, identifying materials optimized for a target application remains challenging because property labels are expensive to obtain and available only for limited structure-molecule pairs. While prior work has demonstrated that 3D neural representations can predict zeolite properties effectively, it remains unclear which representation-learning strategies are most effective in the low-data regime relevant to materials discovery. We present ZeoBench, a benchmark for self-supervised learning on dense 3D representations of all-silica zeolites, and evaluate the resulting features on six existing downstream adsorption-property prediction tasks, across a range of training set sizes. Our study compares self-supervised 3D pretraining on volumetric zeolite data, adaptations of image-pretrained 2D ConvNets and vision transformers to 3D via multiview and channel-inflation strategies, and 3D ConvNets pretrained on out-of-domain volumetric datasets, alongside hand-crafted descriptors and supervised baselines. Using our pretraining and evaluation framework, we find self-supervised 3D representations outperform existing methods and achieve state-of-the-art performance across both in-domain label regimes and for the unseen domain of metal organic frameworks. Learned representations consistently outperform hand-crafted descriptors, and convolutional architectures are generally more effective than vision transformers in this setting. These results establish ZeoBench as a practical benchmark for 3D representation learning in zeolites and provide guidance for data-limited adsorption property prediction.

---


### 220. [FlowMoP: Stochastic Multi-Person Motion Prediction](https://arxiv.org/abs/2611.09882)

**<font color=#1a73e8>作者：</font>** Aadya Agrawal, Ho Kei Cheng, Alexander Schwing  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting the future motion of multiple people is inherently stochastic: the same observed history admits many plausible continuations depending on intent, coordination, and social context. Yet the dominant paradigm in multi-person 3D motion prediction remains deterministic, with existing methods producing a fixed number of outputs per agent. In contrast, we present a conditional flow matching framework that jointly generates diverse future motions for multiple agents, modeling both global trajectories and root-relative poses. A B-spline reparameterization compresses the generative state space while enforcing temporal smoothness, and a dual-stream transformer conditions each agent's predictions on observed neighbor motion for interaction-aware forecasting. Our method achieves state-of-the-art performance on CMU-Mocap (UMPM) and 3DPW, outperforming deterministic baselines on joint position error, pose error, and final displacement error despite producing a full predictive distribution. We additionally establish the first motion prediction baseline on WorldPose, a large-scale professional soccer dataset, where social conditioning demonstrably concentrates predictive uncertainty along interaction-constrained directions.

---


### 221. [On the (non-)closedness of the set of ReLU networks](https://arxiv.org/abs/2611.09887)

**<font color=#1a73e8>作者：</font>** Eloi Martinet, Leon Bungert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove that the set $\mathcal{N}_N$ of ReLU networks with one hidden layer and at most $N\in\mathbb N$ neurons is weakly closed in $W^{1,p}(\Omega)$, for a bounded connected open set $\Omega\subset\mathbb R^d$. Consequently, every coercive, weakly lower semicontinuous energy on this space attains its minimum over $\mathcal{N}_N$. This covers the Deep Ritz method with convex integrands, Sobolev training and Lipschitz learning. Moreover, as the weight decay parameter tends to zero, minimizers of the regularized problem converge, up to subsequences, to minimizers with minimal parameter norm. We also prove that the set of ReLU networks with two hidden layers of bounded widths is not closed in $W^{1,p}(\Omega)$ or in $C(\overline\Omega)$. This disproves a conjecture of Petersen, Raslan and Voigtlaender.

---


### 222. [SciCheck: A Framework for Verifying the Integrity of Deep Learning Training](https://arxiv.org/abs/2611.09889)

**<font color=#1a73e8>作者：</font>** Alexander Nguyen, Dylan Gresham, Gaby G. Dagher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep learning training is difficult to verify within a scientific workflow: its architecture, hyperparameters, and procedure are rarely fixed until training has been attempted, and two honest runs never produce the same weights, so recomputation cannot serve as a check. We present SciCheck, a framework in which the scientist explores training configurations freely and posts a blueprint to a provenance ledger for each candidate they want verified, and a verifying scientist judges the resulting run in two layers: a statistical judge model that compares per-step gradient statistics against the verifier's own reference run, and a spot-check that re-executes randomly chosen training segments whose checkpoints are committed to the ledger one epoch at a time. On an MLP, a CNN, and an autoencoder at 100k-500k parameters, under gradient sign flipping, label poisoning, and fabricated runs, SciCheck reaches F1 of 0.966, 0.906, and 0.976 while rejecting 0-4.4% of honest runs. For the attacks we test, the spot-check accounts for most of this accuracy, and we characterize what each layer can detect. The effective-signal statistic falls as $(1-2s)^2$ under a sign flip of severity $s$, so gradient statistics alone catch strong enough sign flips, while fabricated runs that replay genuine statistics look no more anomalous than honest runs to any statistical detector we test. The spot-check catches fully fabricated segments with probability at least $1-(1-s)^k$ for $k$ sampled segments when the draws stay hidden until the run is committed, which roughly matches our measurements and lets a verifier choose $k$ for a target soundness. Verification costs 1.5-2.3x one retraining, mostly for the verifier's reference run; each submission's spot-check takes under 1.5 s, and per-epoch commitments reduce checkpoint storage 5-17x compared with keeping every checkpoint.

---


> [!TIP]
> 当前位于：**201-222**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-222**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
