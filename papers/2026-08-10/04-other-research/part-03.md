# 📦 其他研究 | 2026年08月10日

> 本类共 **190** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-190](./part-04.md)

---

### 101. [AVCap: Reinforcing Audio-Video Joint Caption with Detail-Aware Reward](https://arxiv.org/abs/2608.06930)

**<font color=#1a73e8>作者：</font>** Mingyang Wu, Kaituo Feng, Bohao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detailed audio-video joint captioning is essential for multimodal video understanding and generation. However, prior works are constrained by three main limitations: (1) the scarcity of high-quality public datasets with fine-grained audio-visual joint captions; (2) reinforcement-learning methods that rely on coarse reward signals; and (3) the lack of a benchmark and metric for evaluating detailed audiovisual captions at the atomic level. To address these challenges, we propose: (1) AVCap-100K, a high-quality dataset of 100K temporally aligned, detail-rich audio-video captions; (2) AVCap, a model optimized via Detail-Aware GRPO (Da-GRPO) that achieves state-of-the-art performance among open-source models and matches or surpasses proprietary models on several evaluations; and (3) AVCap-Bench and AVCap-Score, a specialized benchmark and metric for evaluating atomic-level details in audiovisual captions. Our code, models, and datasets are available at this https URL.

---


### 102. [Walkable to Whom? Capturing Subjective Variability in Walkability Perception Using Multimodal Deep Learning](https://arxiv.org/abs/2608.06934)

**<font color=#1a73e8>作者：</font>** Moloud Damandeh, Meead Saberi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual perception of walkability varies substantially across individuals, reflecting differences in personal characteristics, experiences, and preferences. Existing studies, however, often reduce these diverse judgements to aggregated scores, implicitly assuming uniform perception, and commonly rely on vehicle-mounted street-view imagery that does not reflect the pedestrian's visual experience. This paper introduces a dataset of 29,870 walkability ratings from 1,196 respondents, linking sidewalk-view imagery across urban, suburban, and regional Australian environments with individual rater attributes, and proposes the first user-conditioned multimodal deep learning framework for walkability perception, fusing visual features with respondent-level representations. A viewpoint-comparison study shows that sidewalk-view images receive significantly higher walkability ratings than matched street-view images, indicating that imagery source is a substantive design decision in perception surveys. The user-conditioned model improves rank agreement with observed ratings by 65% over an image-only baseline (quadratic weighted kappa 0.47 vs. 0.29), demonstrating that who is evaluating an environment carries predictive indication beyond image content alone. These findings support moving from aggregated, observer-independent walkability scores toward models that represent diverse users, enabling more inclusive assessment of pedestrian environments.

---


### 103. [ELMZip: Onboard Satellite Image Compression via Extreme Learning Machines for Efficient Downlink](https://arxiv.org/abs/2608.06942)

**<font color=#1a73e8>作者：</font>** Woojin Cho, Junghwan Park, Sangcheol Sim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The acquisition of multispectral imagery via small satellites (e.g., CubeSats) presents significant data downlink challenges due to high data volumes and restricted communication windows. While onboard image compression is critical to address this bottleneck, traditional methods often struggle to adapt to the nonlinear statistics of multi-band, multi-resolution data. To overcome these limitations, we propose ELMZip, a novel framework based on Extreme Learning Machines (ELM) and domain decomposition strategies for efficient, resolution-free onboard neural representation. ELMZip formulates the fitting process as a convex least-squares problem using random-feature single-layer networks, thereby eliminating the need for computationally expensive backpropagation. By adopting an asymmetric transmission protocol that sends only the compact output weights, the proposed method significantly reduces the downlink payload. Unlike previous neural representation approaches that rely on iterative optimization and require transmitting full network parameters, ELMZip achieves significant compression efficiency while maintaining high reconstruction fidelity. This capability enables immediate image reconstruction for analysis, allowing resource-constrained platforms to maximize data return and advancing real-time AI-powered Earth observation.

---


### 104. [Dual-Space Modality Consistency Learning for Universal Cross-Modal Re-Identification](https://arxiv.org/abs/2608.06943)

**<font color=#1a73e8>作者：</font>** Yujian Zhao, Yukang Zhao, Hankun Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal Re-Identification (ReID) aims to retrieve the same identity across heterogeneous imaging modalities and has been widely studied in visible-infrared person ReID and cross-modal ship ReID. Existing methods have achieved promising performance by learning modality consistency in the spatial embedding space, yet often overlook frequency-domain modality discrepancy, particularly in high-frequency representations that are both highly discriminative and modality-sensitive. In addition, most approaches are tailored to specific modality settings, limiting their applicability across diverse cross-modal scenarios. To address these challenges, we propose a Dual-Space Modality Consistency Learning (DSMCL) framework for universal cross-modal ReID. Specifically, DSMCL jointly models spatial feature distribution consistency and frequency-domain discriminative consistency. A Spatial Modality Consistency Learning (SMCL) branch performs Gaussian-based feature alignment, while a Frequency-aware Discriminative Consistency Learning (FDCL) strategy regularizes high-frequency representations through identity-aware cross-modal contrastive learning. By jointly capturing modality-specific characteristics and modality-shared identity cues, DSMCL learns robust representations and establishes a unified framework capable of accommodating diverse heterogeneous modality settings. Moreover, DSMCL is a plug-and-play framework that can be readily integrated into existing cross-modal ReID architectures. Extensive experiments on SYSU-MM01, RegDB, LLCM, HOSS-ReID, and CMShipReID across seventeen evaluation protocols show that DSMCL consistently improves multiple representative baselines.

---


### 105. [LMM Modality Transfer: A Pre-requisite for Autonomous GIS Agents](https://arxiv.org/abs/2608.06948)

**<font color=#1a73e8>作者：</font>** Ivan Majic, Zexian Huang, Franziska Hübl 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI models are becoming increasingly adept at understanding and processing spatial information, thereby facilitating agentic problem-solving in spatial tasks and workflows. However, most of the research on their spatial capabilities (e.g., spatial reasoning) has focused on the textual modality as input and output. This contrasts with the human approach to GIS workflows, where text and visual modalities are often used together, interchangeably, and in a complementary manner. Thus, to truly achieve an automated GIS analysis pipeline or carry out human-designed GIS workflows, AI models --- Large Multimodal Models (LMMs) in particular --- need to be able to seamlessly transition between image- and text-based modalities that are traditionally used in such workflows. We present a modality transfer task that (1) asks an LMM to first describe an input image of colored squares in a regular grid, and (2) asks a new LMM instance to re-generate an image of the original spatial scene using the textual description output by the former model. This task quantifies the ability of LMMs to transfer spatial information between image and text modalities. Ultimately, by examining the modality transfer capability of LMMs through the lens of spatial information theory, this work highlights a critical bottleneck: achieving strong and robust geospatial understanding in LMMs requires rigorous, multi-modal alignment. Our results indicate that recent LMMs (here from OpenAI) still struggle with modality transfer, when tasked with re-generating an image of a simple spatial grid of color squares.

---


### 106. [A Rate Separation for Agnostic Direct Sums](https://arxiv.org/abs/2608.06951)

**<font color=#1a73e8>作者：</font>** Mihir More, Aritra Das, Debayan Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hanneke, Moran, and Waknine \cite{HannekeMoranWaknine2024} asked how the agnostic PAC learning curve of the direct sum $C^r$ depends on the single-instance learning curve $\epsagn(n\mid C)$ and on $r$. We show that the single-instance learning rate does not determine the direct-sum rate. Let $\F$ be the class of the two constant binary functions and let $\G$ consist of the zero function and the identity function. Both classes have agnostic learning curve of order $n^{-1/2}$.

---


### 107. [Casting the Net! Revisiting MasterFace Impersonation Attacks](https://arxiv.org/abs/2608.06952)

**<font color=#1a73e8>作者：</font>** Seunghun Paik, Sunpill Kim, Chanwoo Hwang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Impersonation is a fundamental security threat in face recognition systems (FRSs). While the security of FRSs has been challenged by various attack vectors, under realistic adversarial capabilities, e.g., a limited number of decision-only authentication trials and no internal system knowledge, most attack techniques become infeasible. As a result, impersonation by zero-effort impostors, characterized by false match rate (FMR), is commonly regarded as a standalone baseline. A few years ago, impersonation attacks based on MasterFaces emerged as a notable security threat that could break the barrier of the FMR-based baseline under such realistic constraints. However, they were believed not to yield impersonation above the standard FMR in modern FRSs, as discussed by multiple follow-up studies. In this paper, we demonstrate that even legitimate access to public commercial APIs allows an adversary to amplify impersonation rates through MasterFaces, resulting in a non-trivial impersonation attack beyond FMR on downstream applications built on top of these APIs. We observe that several real-world FRS deployments are implemented using commercial APIs, and that the backend service provider is publicly disclosed or trivially inferable. As a result, the adversary can purchase these pay-as-you-go API services without requiring any additional privilege over the target FRS. From this observation, we formalize the MasterFaces attack as a maximum coverage problem over the biometric representation space, which we call a NET, and show that the adversary can construct an API-tailored NET by leveraging the geometric structure of the representation space. We demonstrate that our attack amplifies the impersonation rates of several open-source and commercial API-based FRSs by up to 9.5$\times$ within at most 30 authentication trials, compared to those expected from the standard FMR.

---


### 108. [Explicit, Not Longer: What Makes Epistemic Stance Survive Memory Compression](https://arxiv.org/abs/2608.06953)

**<font color=#1a73e8>作者：</font>** Alex Kwon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent memory systems compress what they store, and compression is built to drop qualifiers, so a claim's epistemic standing tends not to survive being written to memory. We ask what governs whether it does. Matched notes carry the identical claim and identical stance and differ only in where that stance sits; one model compresses both under the same budget among the same filler notes, and a blind reader that never sees the condition scores the result. Across 60 claims in seven registers, writing the stance as a labelled field rather than a bracketed aside raises retention by about 15 points on two models (37 claims to 2 on one, 30 to 8 on the other; permutation p=0.00005), and a pre-registered replication on Haiku, its prediction and decision rule committed before the run, gives +15.6 points, 38 claims to 1. Ablating the format on both models gives the same net effect from different parts: labels help on both (+9.7 and +12.8) and length helps on neither, but wording the stance as a full sentence is the largest component on one model (+12.5) and worth nothing on the other (+0.6). Either model alone would have licensed a confident and different mechanism, so we claim only the intersection: make the stance explicit, not merely longer, and expect the best way of being explicit to depend on the model. A deterministic readout with no model reproduces the two-cell direction and five of seven ablation contrasts, but not length or labels, which we therefore do not claim on one instrument. Fifty hand labels (kappa=0.75) agree on direction; we print their seven disagreements in full. We also report nine withdrawn claims, three of them former title claims of this paper.

---


### 109. [How Molecular Generative Models Organize Molecular Identity](https://arxiv.org/abs/2608.06956)

**<font color=#1a73e8>作者：</font>** Raul Ortega-Ochoa, Tejs Vegge, Jens S. Bakander 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models for matter are often evaluated as samplers over output representations, and their latent spaces are commonly used as proxies for navigating chemical space. Much less is known about how these models internally arrange discrete chemical identities within those representations. We study this arrangement by making molecular identity explicit and pulling it back through the generative process. Through these pullbacks we probe the regions that generate the same object, exposing the trained model's internal repertoire: a fixed partition that determines which objects (novel or not) the model can produce.
Across three molecular generative architectures, we find that this repertoire is arranged into piecewise-constant regions separated by recurring coarse-to-fine boundaries. Its organization depends on the representation probed, the identity convention, decoder stochasticity, and the metric used to compare coordinates. During training, local chemical organization stabilizes while the number of distinct molecular identities represented within each neighborhood continues to change. Internal organization must therefore be characterized, rather than assumed, before a generative space can be treated as chemically navigable.

---


### 110. [CAi Copilot: Reducing Operational Workload in Molecular Design through Intent-Driven Agentic Workflows](https://arxiv.org/abs/2608.06961)

**<font color=#1a73e8>作者：</font>** Zhu Wang, Jiangyu Chen, Yingjun Shang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early-stage molecular design is an iterative process, not just a task of generating molecules. Researchers turn broad goals into design strategies, refine candidates, assess many properties, and gather evidence before synthesis and tests. AI methods can generate molecules, optimize several goals, predict properties, dock compounds, and account for synthesis. Yet these functions are spread across specialized tools. Experts must still coordinate each step, judge interim results, and integrate evidence. The central challenge is thus to turn research intent into adaptive, traceable runs grounded in scientific tools. We cast this challenge as intent-to-evidence molecular design workflow execution and present CAi Copilot, an expert-oriented agent with three linked layers. The Research Interface Layer turns intent into an executable plan. The Agent Reasoning Layer uses interim results to guide each run. The Execution Substrate supplies molecular tools, metrics, reusable utilities, and backend services. Across 45 tasks, CAi achieves the strongest overall performance, with an outcome score of 84.59, exceeding the next-best result by 18.07 points. Additional benchmarks test how CAi coordinates generation, screening, and multi-criteria evaluation, while exposing limits in long-horizon execution. These results show that CAi turns broad molecular-design intent into transparent, traceable workflows that connect interim decisions to candidate-level evidence.

---


### 111. [Learning in Deep Networks under Dale's Constraint](https://arxiv.org/abs/2608.06963)

**<font color=#1a73e8>作者：</font>** Roy Abel, Shimon Ullman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biologically plausible learning models aim to explain how neural circuits can implement effective learning under the constraints of real neurons. Although significant progress has been made, a major remaining challenge is that existing models often allow neurons or synapses to represent mixed-sign values, both positive and negative, in violation of a basic aspect of cortical circuitry -- Dale's constraint: biological neurons are either excitatory or inhibitory, but not both, and synapses cannot change sign. In this work, we address this discrepancy by introducing a biologically motivated neural architecture in which both neural activations and learning signals are represented by non-negative activity, and synapses have fixed sign, while still supporting backpropagation-like learning. Our approach uses two complementary interacting non-negative channels to represent positive and negative contributions, inspired by evidence of on-off representations in the brain. These channels are implemented through a simple neural circuit motif, which is repeated throughout the network in both bottom-up and top-down pathways. Combined with a local Hebbian learning rule, the resulting model propagates learning signals and updates weights using only local interactions between neurons. We show theoretically that our learning scheme can exactly recover the backpropagation update despite relying solely on non-negative error signals. Empirically, beyond satisfying stronger biological constraints, the on-off architecture learns efficient representations, yielding substantial gains over comparable vanilla networks on the Tiny ImageNet benchmark. These results demonstrate that effective learning can emerge from biologically plausible mechanisms without requiring mixed-sign signals, providing a step toward more realistic models of neural computation.

---


### 112. [Finding Usable Weight Mechanisms with Tiled SVD](https://arxiv.org/abs/2608.06969)

**<font color=#1a73e8>作者：</font>** Ash Manvi, Samreena Tajreen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The dominant approach to mechanistic interpretability trains proxy dictionaries such as sparse autoencoders and labels features from max-activating text. The best such atlases identify con- cepts, but that identity lives in the learned dictionary rather than in the network weights them- selves. We propose extracting mechanism mounts directly from linear sites by column-tiled SVD: each mount is a triple (v,u,{\sigma}) read as trigger, write, and strength. Identity is the weight rule. We evaluate mounts with a pre-registered suite judged on full-write energy lift rather than tile-local lift. On Gemma-2-2B with WikiText-2 (16,384-token subsample), all seven linear maps are scored: residual writes (this http URL, attn.o) receive full A/B/C with steer after post-sublayer RMSNorm and pass 52/52 site-layers; other maps receive A/B only (this http URL this http URL 26/26 each). Aggregate: 182/182 GO. We release library code, the corpus builder, the experiment entrypoint, and unit tests.

---


### 113. [When One Modality Is Not Enough: Multimodal Sex and Life-Stage Classification of Red Deer from Aerial RGB-Thermal Video](https://arxiv.org/abs/2608.06973)

**<font color=#1a73e8>作者：</font>** Hugo Markoff, Christoph Praschl, Ivan Ludoški 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial drone surveys increasingly support wildlife population estimation, yet a useful census is more than a count: population dynamics are defined by species composition, sex ratios and age structure, that is, by which species are present and how a herd splits into adult males, adult females and juveniles. We use red deer ($\textit{Cervus elaphus}$) as a test case, because managers act on these dynamics and because the visible cue defining adult males, the antlers, is seasonally variable. Surveys are flown nadir, high enough not to disturb the animals, so each deer occupies only a small, low-resolution patch. The two recording modalities fail in opposite conditions: in color a deer under canopy blends into the ground, while in thermal it becomes a bright blob that loses fine detail. Rather than trust either modality alone, we fuse them at every stage using self-supervised DINOv3 features. Our pipeline tracks animals in both modalities, treats an animal as confirmed only when the two cameras agree, keeps only the clear, non-occluded frames, and assigns species and sex by a vote across them; life stage is read separately from geo-referenced body size, since at survey resolution a juvenile often only differs from an adult female in size. Across four flights spanning the antler season the fused pipeline correctly classifies 25 of the 26 detected individuals (7 of 8 adult males, all 16 adult females and 2 juveniles), against 20 of 26 for either sensor alone. Multimodal species classification reaches 96.0%, while for sex classification fusing the two sensors matters most: the combined RGB+thermal model is the most robust across environments and seasons. Automating the demographic classification turns a drone flight from a count into a repeatable reading of herd structure, so the sex ratios and age structure that managers already act on can be gathered as often as a survey can be flown.

---


### 114. [Social Facilitation of Creative Reflection: AI-agents and Humans](https://arxiv.org/abs/2608.06980)

**<font color=#1a73e8>作者：</font>** Olga Sutskova, Corey Ford  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social collaboration can support people's reflection and is a crucial component of creativity. Creative technologies have been designed to support more collaborative ways of working, including using AI to simulate social partners. As human-AI creative collaborations increase, further investigation is needed into how different social interactions influence creative reflection and at which stage a social intervention is crucial to improve creative outcomes. Considering that non-verbal communication is the bedrock of human cognition and influence, non-verbal social dynamics should be examined in detail in the age of AI-companionship. For example, during social interaction, the social facilitation effect describes how the mere presence or observation of others influences how a person behaves and feels in the context. Whether changes in technology-mediated social environments influence how people reflect on their creative work needs further exploration, as does whether social AI-companionship elicits similar effects as humans. This paper discusses how theoretical mechanisms relating to social facilitation could influence creative practice and reflection, proposing ways of further testing these effects.

---


### 115. [Local Epistemic Uncertainty Guided Active Sampling for Plug-and-play Diffusive Image Restoration](https://arxiv.org/abs/2608.06981)

**<font color=#1a73e8>作者：</font>** Jiaqi Zhang, Zheng Pang, Rongrong Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have demonstrated remarkable effectiveness in image restoration tasks. However, when guiding image reconstruction, existing Diffusion Model-based Image Restoration (DMIR) methods typically rely on fixed data constraints and uniform step sizes, thereby overlooking the dynamic nature of the generative process. Such rigid designs render the models vulnerable to spatially non-uniform degradations, thus resulting in structural distortions and loss of fine details. Meanwhile, uniform step sizes introduce computational redundancy, whereas naïve step reduction strategies tend to accumulate approximation errors. To address these limitations, we propose a Local Epistemic Uncertainty Guided Active Sampling framework (LEADer). In the spatial domain, LEADer leverages pixel-wise uncertainty to dynamically modulate the prior strength within the null space, which effectively balances detail preservation and artifact suppression. In the temporal domain, it quantifies sampling stability via the uncertainty trace to enable adaptive trajectory pruning, thereby accelerating convergence. Theoretical proofs demonstrate that our framework achieves strict data consistency, while the trajectory pruning strategy admits a deterministic error bound, thereby guaranteeing stable convergence under skip sampling. Notably, our plug-and-play method can be seamlessly integrated into various DMIR baselines. Extensive experiments show that LEADer improves the performance of multiple state-of-the-art DMIR methods, while significantly reducing sampling time with negligible memory overhead. Code is available at this https URL.

---


### 116. [HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses](https://arxiv.org/abs/2608.06984)

**<font color=#1a73e8>作者：</font>** Xiao Zhang, Yusheng Wang, Yuhao Fei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern agent harnesses persist state across tasks and sessions through persistent carriers like memory, skills, tools, and shared artifacts. However, this capability creates delayed safety risks: attacker-influenced content can cross system boundaries and later affect the execution of a benign request. Existing benchmarks typically focus on a few carriers or harnesses, while end-to-end attack-success rates reveal little about how risks propagate. To this end, we present HarnessSafe, a benchmark comprising 328 executable cases across seven persistent-carrier families and evaluated on most mainstream agent harnesses. Each case is specified as a Persistent-Risk Lifecycle that traces attacker influence from its initial entry, through persistence across carriers and system boundaries, to a later benign trigger and an observable violation. We further introduce a multi-stage, trace-based evaluation that uses observable execution evidence to determine how far each attack chain progresses and where it is stopped. Experiments show that containment is carrier-specific and strongly depends on the harness-model configuration. Both the harness and model backend substantially shape containment outcomes, while attack success rates cannot reflect distinct lifecycle progression patterns.

---


### 117. [Switched Reading: Toward Seamless Visual-Auditory Switching When Reading Text in Augmented/Mixed Reality](https://arxiv.org/abs/2608.06985)

**<font color=#1a73e8>作者：</font>** Kazuyuki Fujita, Yuto Matsui, Ikuru Sato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Augmented/mixed reality (AR/MR) wearable glasses now permit information interaction anywhere, but visual displays can be inappropriate when real-world awareness is essential. We propose Switched Reading, a novel interaction framework for reading text in AR/MR that supports switching between visual and auditory modalities as needed. Specifically, we explore two key interaction techniques within this framework: (1) gaze-based voice playback and (2) a correspondence-aware transition effect. We implemented them on an MR headset through a parameter-tuning user test. Next, we conducted a user study (N=16) to investigate the impact of the two techniques on reading performance and overall user experience with simulated modality switching in virtual reality. The results show that the condition combining both techniques was the most preferred among four conditions. Moreover, we found that the gaze-based voice playback reduced gaze offsets when switching modalities and improved reading speed over the baseline condition using scroll position. Finally, we implemented a Switched Reading application for reading while walking and collected user feedback, yielding further design implications for practical use.

---


### 118. [Density-aware Hierarchical Clustering Based on Element-Categorized Connection Subgraphs](https://arxiv.org/abs/2608.06990)

**<font color=#1a73e8>作者：</font>** Yuning Yu, José Rodríguez-Piñeiro, Xuefeng Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustering is a fundamental data mining technique for pattern recognition through unsupervised learning. Among various clustering methods, hierarchical clustering, density-based clustering, and graph clustering stand out as representative approaches. For hierarchical clustering, it can be categorized into agglomerative and divisive modes to construct clusters in a recursive manner. The key aspect of both modes is the calculation of inter-cluster similarity, which determines whether to merge the sub-clusters into one cluster or divide a current cluster into sub-clusters. Traditionally, the similarity is derived from pairwise distances, often overlooking density variations and structural connectivity in graphs. To address this, we propose a density-aware hierarchical clustering method based on element-categorized connection subgraphs (DHC-ECS), which effectively integrates the hierarchical clustering, density-based clustering, and graph clustering. Particularly, a novel inter-cluster similarity metric is introduced that considers not only distances but also the element categorization in the KNN connection subgraphs, kernel density estimation, and local connectivity within sub-clusters. Extensive evaluations on heterogeneous benchmark datasets demonstrate that DHC-ECS exhibits superior overall performance in terms of clustering accuracy and parameter robustness compared with the baseline methods (including AChameleon, RNN-DBSCAN, McDPC, and G-RMS). The work indicates the great potential of the proposed clustering algorithm for low-dimensional datasets by leveraging local density and graph-structured connectivity (i.e., the duality of vertices and edges), as well as the possibility to determine an intrinsic threshold, reducing the reliance on manual parameter tuning.

---


### 119. [HRDiT: Training-Free High-Resolution Image Generation with Off-the-Shelf Diffusion Transformer Models](https://arxiv.org/abs/2608.07003)

**<font color=#1a73e8>作者：</font>** Yu Xue, Haoxuan Qu, Zhuoling Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free text-to-high-resolution image generation has recently attracted growing research attention. However, existing studies on this task primarily focus on adapting off-the-shelf U-Net-based diffusion models to high resolutions, with limited progress on adapting off-the-shelf Diffusion Transformer (DiT) models despite their strong text-to-image generation capabilities at limited resolutions. In this work, we find two key challenges particularly hindering the application of off-the-shelf DiT models for high-resolution image synthesis in a training-free manner, namely, spatial disorder and long generation time. To address these challenges, we propose a novel method tailored to adapt off-the-shelf DiT models for high-resolution image synthesis. Extensive experiments show the efficacy of our method. Our code is available at: this https URL.

---


### 120. [FedLBW: A Loss-Based Weighting Strategy for Federated Learning on Non-IID Data in Wireless Networks](https://arxiv.org/abs/2608.07007)

**<font color=#1a73e8>作者：</font>** Majid Kundroo, Tinku Singh, Taehong Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative machine learning (ML) across distributed clients while preserving privacy. However, efficient model convergence in FL remains challenging, especially in wireless networks where non-independent and identically distributed (non-IID) data and frequent client dropouts are common. Traditional FL algorithms, such as FedAvg, rely solely on dataset size to weight client updates. This introduces biases towards clients with larger datasets and makes the process sensitive to non-IID data, outliers, and client dropouts. To address these challenges, we propose Federated Learning with Loss-Based Weighting (FedLBW), a novel aggregation method that assigns each client's update a weight proportional to the inverse of its validation loss, computed using a small proxy dataset on the server, rather than its dataset size. This ensures that lower-loss models exert greater influence during aggregation, prioritizing the most reliable updates and boosting overall performance. Through extensive experiments across multiple datasets, including FashionMNIST (CNN), CIFAR-10 (ResNet-18), and CIFAR-100 (ResNet-34), we demonstrate that FedLBW achieves higher accuracy and faster convergence compared to baseline algorithms such as FedAvg, FedAvgM, FedProx, FedNova, FedLAW and FedDkw, with notable improvements of up to 7.6 % higher accuracy on CIFAR-10 in extreme non-IID cases. Moreover, FedLBW showcases exceptional resilience to increasing dropout probabilities, consistently maintaining significantly higher accuracy even in challenging conditions. These results establish FedLBW as an effective and resilient solution for FL in wireless network environments, offering marked improvements in model accuracy, convergence speed, and robustness to non-IID data and client dropouts.

---


### 121. [Scenix: Sparse-View 3D Scene Reconstruction via Executable Scene Programs](https://arxiv.org/abs/2608.07012)

**<font color=#1a73e8>作者：</font>** Kai Li, Lutao Jiang, Zhenyang Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing a structured and editable 3D indoor scene from a few uncalibrated RGB views requires more than generating high-quality individual assets: a system must infer the room structure, associate objects across incomplete observations, and recover a globally consistent spatial configuration. Previous methods mainly focus on 3D scene generation with text input or require continuous visual inputs with additional priors, \ e.g., human-annotated masks or accurate 3D layouts, which makes these methods labor demanding and hard to apply in general cases. We present \textsc{Scenix}, a sparse-view 3D scene reconstruction framework via executable scene programs, a structured representation that can be directly instantiated into editable 3D scenes. Given sparse views, \textsc{Scenix} predicts executable scene programs through perception-grounded asset instantiation and closed-loop spatial refinement. % We present \method, a framework that predicts an executable scene representation from sparse views and realizes it through perception-grounded asset instantiation and closed-loop spatial refinement. To support this task, we construct \dataset, a dataset of approximately 110,000 synthetic and real indoor scenes with multiview imagery, room structures, object-centric descriptions, and metric spatial annotations. We further introduce observation-consistent supervision that aligns each target scene with the visual evidence available in its input views. Experiments on held-out \textsc{XScene} scenes, real indoor images, and out-of-distribution SpatialGen cases evaluate structured scene prediction, object grounding, and spatial refinement.

---


### 122. [Understand Before Detect: Vision--Language Learning for Omni-Domain Infrared Small Target Detection](https://arxiv.org/abs/2608.07015)

**<font color=#1a73e8>作者：</font>** Haoyang Yuan, Boyang Li, Yingqian Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-domain infrared small target (IRST) detection is crucial for infrared surveillance, yet remains challenging due to heterogeneous imaging domains and inconsistent target characteristics. Previous deep learning-based methods have been developed for visual-only paradigms and achieved promising performance on domain-specific tasks. However, existing methods follow the task-specific supervised learning paradigm. This paradigm simplifies the full-scene infrared observations to sparse target supervision, discarding the semantics that remain invariant across heterogeneous domains. Consequently, detection performance suffers substantially under domain shifts. To handle this issue, we introduce \textbf{``understand before detect''}, a paradigm that formulates omni-domain IRST detection as an understanding-driven process, where holistic infrared target understanding precedes precise detection. Building on this paradigm, we propose \textbf{JinSight}, which first develops holistic IRST understanding through language supervision and then transfers the learned cross-domain representations to precise small-target detection. By grounding infrared representations in language semantics, JinSight enables a single model to generalize across heterogeneous infrared domains. We then introduce Latent Semantic Interaction (LSI), which exchanges language-aligned global semantics with fine-grained spatial features in a compact low-rank space. To address the lack of multimodal omni-domain IRST benchmarks, we build \textbf{OmniIRST-VL}, the first large-scale, highly diverse vision--language dataset for omni-domain IRST detection. It comprises over 39k annotations across six complementary instruction tasks covering both scene-level understanding and target-centric reasoning.

---


### 123. [Effects of parental controls in the context of Digital Forensics](https://arxiv.org/abs/2608.07016)

**<font color=#1a73e8>作者：</font>** Selina Märchya, Mauro Vignatia, Frank Breitinger  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Parental control systems are designed to protect minors online, but can inadvertently obstruct digital forensic investigations. When enabled, these systems restrict administrative privileges, disable debugging options, and alter data accessibility, complicating evidence acquisition and analysis. This study empirically examines the impact of Microsoft, Google, and Apple parental controls on forensic processes across fifteen Windows, Android, and iOS devices. Through controlled experiments, we evaluate their impact on evidence accessibility and identify forensically sound methods to overcome these limitations. The findings provide practical guidance for investigators and contribute to improving forensic readiness in environments governed by parental control systems.

---


### 124. [Hyperbolic Graph Embedders for Link Prediction and Topology Reconstruction](https://arxiv.org/abs/2608.07029)

**<font color=#1a73e8>作者：</font>** Robert Jankowski, Maksim Kitsak, Dorota Celińska-Kopczyńska  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperbolic embeddings provide compact geometric representations of complex networks in hyperbolic spaces, but systematic comparisons of methods developed in machine learning, network science, and algorithmics remain rare. We benchmark 13 unsupervised hyperbolic graph embedders under a unified protocol for link prediction and topology reconstruction on synthetic and empirical networks. The protocol captures both missing-link recovery and the preservation of local and global network structure. Maximum-likelihood and representation-learning-based approaches, including hybrid variants, achieve the strongest overall performance, although no method dominates across all tasks and structural regimes. Performance is more strongly associated with embedding paradigm than with disciplinary origin. We identify the network regimes in which different paradigms succeed or fail and provide practical guidance for method selection in downstream applications.

---


### 125. [Accounting Graph Transformer for Short-History Multi-KPI Forecasting in Small Businesses](https://arxiv.org/abs/2608.07037)

**<font color=#1a73e8>作者：</font>** Shrutendra Harsola, Vignesh Subrahmaniam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small businesses often have only 12-24 months of accounting history, yet planning and risk workflows require coordinated forecasts across financial statements. We study joint 12-month forecasting of 13 income-statement, balance-sheet, cash-flow, and working-capital key performance indicators (KPIs) from 71 monthly ledger series. We introduce the Accounting Graph Transformer (AGT), which represents each ledger series as a masked token, exchanges information through typed attention on a fixed accounting-relation graph, pools target-specific context, and fuses it with a gated three-month recency path. Across 11,993 forecast origins from 1,060 unseen companies, AGT achieves sample-weighted KPI-macro mean absolute error (MAE) $0.6990 \pm 0.0013$ over three independent seeds, compared with $0.7378 \pm 0.0014$ for the strongest baseline, LightGBM. At the pre-specified seed 42, a paired company-clustered bootstrap gives a LightGBM-minus-AGT difference of 0.0395 with 95% confidence interval (CI) $[0.0350,0.0439]$. AGT is best on all 13 KPIs against LightGBM, TimeMixer, and SOFTS in the matched seed-42 comparison, while final-architecture ablations show that relational attention, accounting topology, and the recency path each improve validation and test accuracy. On 7,094 additional unseen companies with origins sampled from January-May 2025, AGT obtains 0.7548 MAE versus 0.7694 for SOFTS. A single 5.3M-parameter model produces 156 aligned forecasts without company-specific fitting, providing one forecasting layer for integrated planning, liquidity, and working-capital analysis.

---


### 126. [BONSAI: Evolvability-Guided Tree Search over Skills](https://arxiv.org/abs/2608.07056)

**<font color=#1a73e8>作者：</font>** Yash Priya Shastri, Anand Eswaran, Adnan Qidwai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A skill is a naturallanguage document that steers a frozen agent whose weights cannot be updated so any capability the agent lacks must be supplied in prose Optimising a skill is therefore optimising text against a score and the standard recipe which keeps any edit that raises a heldout score is blind in a specific way a single score cannot tell a document perched on a narrow overfit spike from one resting on a broad plateau even though only the second can still be improved We introduce BONSAI a novel skilloptimisation framework that steers instead by evolvability the capacity of a region of documentspace to keep producing viable variation under further mutation a property biology treats as separate from present fitness BONSAI grows skills as a MonteCarlo search tree in which every child document is a mutation of its parent and descends it under an upperconfidence selection rule whose exploitation term blends a skills own fitness with the fitness of its mutational neighbourhood Because every child is a mutation the mean score recorded beneath a node estimates that neighbourhoods evolvability at no extra cost so the rule concentrates budget on regions that keep improving while its exploration term keeps a currently weak branch in contention BONSAI ships the single bestscoring document it finds at no cost beyond the acceptifbetter loop it replaces With a frozen 30B agent and averaged over three benchmarks BONSAI lifts heldout accuracy over the skillfree agent by 2313 points and improves on two budgetmatched baselines GEPA and SkillOpt by 387 and 397 points respectively

---


### 127. [KnifeHunter: Structured Local Representation Learning for Fine-Grained Knife Image Retrieval in Law Enforcement](https://arxiv.org/abs/2608.07057)

**<font color=#1a73e8>作者：</font>** Syed Sameed Husain, Eng-Jon Ong, Stephen Simpson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knife-enabled violence presents a major public safety challenge, and law enforcement agencies require scalable tools for catalogue-level knife identification, intelligence analysis, and source attribution. Manual visual comparison is specialist, time-consuming, and difficult to scale under operational imaging conditions. We introduce KnifeHunter, an end-to-end forensic knife image retrieval system developed with UK law enforcement. The work contributes the KnifeHunter dataset, comprising 25,843 images across 543 knife classes from police evidence, retail catalogues, and border-force seizures, with structured metadata, Medium/Hard evaluation protocols, and large-scale distractor evaluation. We further propose CoRe-Net, a compact single-descriptor retrieval architecture that combines global context with spatially localised discriminative evidence. CoRe-Net introduces Structured Complementary Representation Learning (SCRL) to organise local evidence into complementary prototype-based representations, and Bi-Directional Reciprocal Fusion (BDRF) to integrate global and local evidence through residual projection and gated local-to-global injection. Using an EVA02-Base backbone and cosine-similarity retrieval, CoRe-Net achieves 88.0% mAP and 86.7% mP@10 on the Medium protocol, and 85.1% mAP and 83.8% mP@10 under distractor conditions. KnifeHunter was deployed by UK police forces during Operation Sceptre deployments from 2023 to 2025, achieving 99.2% mP@1 on field queries. These results demonstrate a practical and effective multimedia retrieval framework for fine-grained forensic knife matching in operational law-enforcement settings.

---


### 128. [Soft Redaction of Image Provenance via Zero-Knowledge Proofs](https://arxiv.org/abs/2608.07063)

**<font color=#1a73e8>作者：</font>** Muhammad Awan, John Collomosse  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Content provenance standards, such as C2PA, are increasingly used to attach signed records of origin, editing history, and rights to digital images. However, provenance transparency can conflict with privacy -- assertions that strengthen trust in an image may also reveal sensitive information about the creator or capture context. We propose soft redaction for image provenance: a mechanism that replaces sensitive provenance assertions with zero-knowledge proofs (ZKPs) of selected properties over hidden data. Our work focuses on distance proofs. We first show how location assertions can support proofs of proximity to a public reference point, using Chebyshev polynomial approximations within the ZKP proof circuit. We then extend the approach to L2 distance proofs over biometric embeddings, enabling privacy-preserving claims related to likeness to help enforce personality rights with images. Finally, we apply the same distance-proof construction to perceptual hashes (visual fingerprints), supporting an anti-spoofing use case in watermark-based recovery of stripped provenance metadata. Our results demonstrate that ZKPs over image provenance can provide practical soft-redaction capabilities, compatible with C2PA, that may be constructed in seconds and verified in milliseconds.

---


### 129. [XGait: A Multi-Modality Wireless Sensing Dataset for Indoor Human Tracking and Identification](https://arxiv.org/abs/2608.07064)

**<font color=#1a73e8>作者：</font>** Wei Xu, Zhu Wang, Yifan Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wireless sensing has emerged as a promising approach for tracking and identification using commodity Internet of Things devices. However, the features derived from a single wireless modality are often fragile to variations in environmental layouts and walking trajectories. Furthermore, most existing studies are based on datasets collected in specific scenarios with limited trajectory diversity and sensing modalities, preventing a robust evaluation of system generalization. \textcolor{blue}{To address this gap, we introduce \textbf{XGait}, a multi-modality wireless sensing dataset that synchronously captures human walking using Wi-Fi and acoustic transceivers across three indoor scenarios, with vision-based measurements serving as ground truth. Specifically, XGait contains more than 22K walking samples from 27 participants, covering diverse directions and trajectories to support both indoor tracking and identity recognition. To bridge the heterogeneity of wireless sensing modalities, we propose a unified Doppler spectrogram representation that maps Wi-Fi and acoustic signals into a shared time--frequency space, along with a standardized benchmark pipeline for pre-processing, temporal alignment, and feature construction, enabling reproducible evaluation and systematic cross-modal analysis. Extensive evaluations demonstrate that Wi-Fi and acoustic sensing exhibit complementary strengths, particularly under complex trajectories and challenging propagation conditions, thereby paving the way for novel research in the field of multi-modality wireless sensing.} The dataset and code are available at this https URL.

---


### 130. [PTQ4SNN: Membrane-Aware Post-Training Quantization for Spiking Neural Networks](https://arxiv.org/abs/2608.07066)

**<font color=#1a73e8>作者：</font>** Hui Xie, Tong Shi, Haotong Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs) enable sparse and event-driven computation, but their low-bit deployment remains incomplete because recurrent membrane states are commonly retained in floating point even after weight quantization. Quantizing these states is challenging because their distributions differ across channels and from the preceding weights, while small perturbations near the firing threshold may alter spike decisions and accumulate over time. We propose PTQ4SNN, a membrane-aware post-training quantization framework that jointly quantizes weights and recurrent membrane states using only a small calibration set. First, a channel-wise Unified Scale Bridge constrains the membrane scale as s_mem,c = s_w,c * 2^k_c, adapting to membrane distributions while enabling shift-compatible scale conversion. Second, Mixed-Precision Bit Allocation assigns 2/4/8-bit precision to membrane channels according to firing activity and quantization sensitivity under an average-bit budget. The framework operates on reusable projection-LIF pairs and supports both convolutional SNNs and spike-driven Transformers without backbone retraining. Experiments on static and event-based classification and semantic segmentation show that PTQ4SNN effectively preserves model accuracy under W4 quantization and approximately 4-bit membrane precision.

---


### 131. [DocMemo: Dynamic Evidence Discovery via Probabilistic Memory-Guided Retrieval for Multi-Modal Document Understanding](https://arxiv.org/abs/2608.07067)

**<font color=#1a73e8>作者：</font>** Hanshu Yao, Janfeng Zhong, Niu Lian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-document understanding requires locating sparse and heterogeneous evidence across hundreds of pages, yet existing systems remain limited by static retrieval and fragile cross-round memory. Mainstream single-round methods commit to a fixed top-$k$ page set at the outset and struggle to recover from early retrieval errors; recent iterative approaches allow multi-round evidence acquisition, but they do not investigate the propagation mechanism of cross-round states, making it difficult to track the dynamic changes in page relevance. To address these limitations, we propose DocMemo, a memory-guided framework that formulates long-document reasoning as dynamic evidence exploration. DocMemo maintains a tri-level retrieval state consisting of Document Schema Memory, Page Belief Memory, and Question Episodic Memory, which respectively capture structural priors, dynamic relevance estimation, and query-specific reasoning trajectories. During reasoning, DocMemo continuously refines cross-round page selection through Bayesian page belief updating with Thompson sampling, spatial proximity propagation, and structure-aware adaptive-granularity evidence access, while supplementing page-level evidence with fine-grained visual regions. Experiments on 3 benchmarks show that DocMemo achieves state-of-the-art performance and validate the efficacy of structured memory and dynamic page belief updating. Code is available at this https URL.

---


### 132. [MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents](https://arxiv.org/abs/2608.07068)

**<font color=#1a73e8>作者：</font>** Zhiyuan Liu, Tinghong Ye, Chenghao Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents accumulate growing contexts during interaction, impairing performance and stability. Compact memory mitigates this problem by compressing and rewriting the history retained between model invocations. Learning what to retain typically relies on proximal policy optimization (PPO) with final task rewards, but sparse rewards provide little guidance for individual memory updates. This limitation motivates on-policy distillation (OPD), which supplies dense teacher supervision on student rollouts. For such supervision to be valid, the teacher must evaluate each sampled action under the same state in which it was generated. However, the context rewriting performed during memory compression can break this alignment. When sampled responses are retained and re-encoded for later invocations, flattening the interaction into a persistent history may cause the teacher to score the action under a state that the student never visited during rollout. The action therefore remains on-policy by provenance, but not necessarily by state. We therefore propose Memory-Aligned On-Policy Distillation (MemOPD). MemOPD records the inputs and sampled outputs of each model invocation, restores its original token positions and causal visibility, and packs the reconstructed invocations for efficient teacher scoring. The teacher provides full-vocabulary supervision at the sampled action positions, while PPO preserves the final task objective. Experiments verify state alignment across several context updates and show that it improves F1 by 7.0% over persistent-history teacher scoring in a matched control. Overall, MemOPD-3B improves F1 over PPO by up to 416.2%, while packing yields up to a 1.63x speedup in actor computation during training. The code for this work is publicly available at: this https URL.

---


### 133. [Beyond Isolation: Unlocking Reinforcement Learning Component Synergy for Sample-Efficient Continuous Control](https://arxiv.org/abs/2608.07086)

**<font color=#1a73e8>作者：</font>** Qi Zhao, Guozheng Ma, Yilun Kong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning systems are significantly more complex than other machine learning paradigms due to inherent properties, causing RL system design to jointly account for many tightly coupled factors. Despite advances in individual algorithmic components, their functional interdependencies remain underexplored: do they exhibit mutual synergy or counterproductive interference? To bridge this gap, we conduct a systematic investigation and find that the efficacy of different components exhibits significant task-dependency, and naively stacking state-of-the-art techniques does not necessarily yield performance gains; instead, it often triggers emergent challenges, such as compounded non-stationarity. Building upon these findings, we distill a suite of actionable insights into the principled coordination of these components. Guided by these insights, we propose ROSER, an RL framework that coordinates three critical dimensions: Model-based Representation, Optimization Stability, and Experience Replay. Across diverse continuous-control benchmarks, ROSER consistently outperforms vanilla baselines and achieves 17.60% gains over naive stack. Our findings underscore the necessity of a holistic perspective in RL system design and paves the way for developing sample-efficient agents.

---


### 134. [Synthetic LiDAR Data Generation and Deterministic Downsampling for Point Cloud Classification on the Edge](https://arxiv.org/abs/2608.07106)

**<font color=#1a73e8>作者：</font>** Niclas Meyer, Stefan Reitmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying three-dimensional deep learning frameworks to low-power embedded processors is bottlenecked by the unstructured nature of spatial data and the resource-intensive distance sorting algorithms often used before neural network inference. To address this gap, this paper presents a hardware-constrained workflow optimized for native execution on the Raspberry Pi 5. To account for the reality gap between noiseless, clean computer-aided design (CAD) datasets and real-world sensor data, we use physics-based simulation to construct a synthetic LiDAR dataset. Cross-dataset evaluations demonstrate a substantial drop in classification accuracy when networks trained on clean CAD data are evaluated on synthetic LiDAR sensor data, highlighting the critical need for sensor-aware training. To address the latency bottleneck of traditional geometric preprocessing on edge CPUs, we integrate an isolated, feature-driven Critical Points Layer (CPL) as a frontend filter. Our results show that the pretrained CPL deterministically compresses raw 1024-point clouds to a subset of 40 to 60 unique coordinates. When profiled on the ARM Cortex-A76 processor, the complete pipeline achieves an inference throughput of approximately 50 FPS while maintaining an instance classification accuracy of 88.36%, demonstrating the viability of deterministic real-time 3D perception at the edge.

---


### 135. [MemWM: Memory-Augmented Text-Based World Model](https://arxiv.org/abs/2608.07107)

**<font color=#1a73e8>作者：</font>** Yujun Wang, Tao Zhang, Jinhe Bi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are increasingly used to support planning in agents by predicting how environment states evolve in response to agent actions. Yet fluent next-state predictions can still omit task-critical facts, corrupt product attributes, or apply incorrect transition rules. To address such systematic prediction errors, we introduce MemWM, a memory-augmented text-based world model. MemWM uses world memory, a curated memory bank of transition rules, state caches, and hard-to-predict facts, to condition next-state imagination. We evaluate factual state preservation with Structured State Fidelity (SSF), which scores predicted states through benchmark-specific facts and fields. Compared with SFT, memory-augmented training improves SSF by up to 206.3%. In the full planning setting, we keep the policy model frozen and provide policy-side world skill: retrieved task-level skills and step-wise corrective guidance for action selection. Across ALFWorld, WebShop, and ScienceWorld, memory-augmented agents improve downstream success over an SFT-trained world-model agent, with up to a 65.4% relative gain. Sensitivity analyses further show that retrieved memory improves task success and efficiency under different memory and action-budget settings.

---


### 136. [Modular TTT: Rethinking Test-Time Training as Composable Modules](https://arxiv.org/abs/2608.07110)

**<font color=#1a73e8>作者：</font>** Bohao Tang, Zhen Qin, Yuqi Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time training (TTT) views sequence modeling as an online learning problem in which fast weights are updated by an internal learning rule. Despite the growing number of TTT variants, existing approaches typically hard-code each variant separately, which makes it difficult to design new TTT methods and to isolate the role of each component. To address this, we propose Modular TTT, a framework that represents the inner learner as a directed acyclic graph and exposes the fast-weight network, loss function, learning rate, weight decay, and normalization as explicit design dimensions. Modular TTT automatically composes primitive-level train-view forward, train-view backward, and causal query-view rules into the full graph-level TTT computation, including the fast-weight state transition. Using Modular TTT, we systematically ablate the components of TTT and find that small learning-rate initialization, weight decay, and a single-layer nonlinearity improve performance, while MSE and inner-product losses perform similarly. Deeper fast-weight networks and normalization tend to hurt performance because they induce excessively large activations, while residual connections and gating provide little measurable benefit. Guided by these findings, we train the best resulting variant as 410M- and 1.45B-parameter models on 100B tokens, and observe training loss and benchmark performance comparable to Gated DeltaNet.

---


### 137. [Geometry-Aware Camera Localization for Bronchoscopy](https://arxiv.org/abs/2608.07116)

**<font color=#1a73e8>作者：</font>** Lumin Chen, Qingyao Tian, Jinpeng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera localization in bronchoscopy remains a challenging problem due to stringent accuracy requirements, real-time constraints, and limited training data. Compared to natural scenes, the confined anatomical structures demand millimeter-level precision, while intraoperative guidance necessitates low-latency inference. However, existing methods often fail to effectively exploit preoperative geometric priors, limiting their robustness and accuracy. To address these limitations, we propose a unified geometry-aware bronchoscope localization framework (GABL) that effectively fuses preoperative structural priors with paired intraoperative video to estimate 6-DoF camera poses. Specifically, to address visual ambiguity in complex airways, we propose a graph-guided coarse-to-fine localization scheme that effectively leverages structural priors for precise pose estimation. Furthermore, to mitigate pose jitter and bridge the visual-structural gap, we integrate a Transformer-based tracking model with a novel RGB-depth matching objective, jointly enforcing spatio-temporal and geometric consistency. Extensive experiments demonstrate that our method yields remarkable reductions of 8.37% and 31.76% in translation and rotation errors over the prior state-of-the-art, alongside 4 times inference speedup (33.6 FPS) for robust real-time bronchoscope localization. Project website: this https URL.

---


### 138. [How Much, Then Where: Credit-Conserving Action-to-Token Allocation for Multi-Turn Agent Reinforcement Learning](https://arxiv.org/abs/2608.07118)

**<font color=#1a73e8>作者：</font>** Lichao Ma, Yang Sun, Shuaitao Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Credit assignment in multi-turn agent reinforcement learning operates at two levels: assigning trajectory-level credit to actions and distributing each action's credit across its tokens. In this paper, we introduce FACTOR, which separates these decisions. FACTOR uses checkpoint-calibrated TD residuals to assign per-action credits that telescope to the trajectory advantage, and feedback-conditioned teacher-student likelihood gaps to allocate each credit across the realized action tokens. Per-action normalization preserves the action-average coefficient and prevents token-level sign flips. We pair this construction with an action-mean reduction, removing the implicit dependence of an action's scalar surrogate weight on its token length. At the behavior policy and before clipping, each action's inner action-mean surrogate equals its TD credit. FACTOR consistently improves over competitive baselines across ALFWorld, WebShop, and ScienceWorld, with every environment-seed comparison favoring FACTOR and the largest gains emerging on the longest-horizon environment. The same hyperparameters transfer without retuning to a larger backbone and to a different model family. Ablations identify TD action credit as the dominant driver of the improvement, with hindsight token allocation contributing complementary gains.

---


### 139. [Multiple Hypothesis Flow Estimation for Video Frame Interpolation under Matching Ambiguity](https://arxiv.org/abs/2608.07120)

**<font color=#1a73e8>作者：</font>** Zibo Su, Jing Kong, Ruixing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many flow-based video frame interpolation (VFI) methods synthesize an intermediate frame by estimating optical flow fields, warping the two input frames, and blending the warped observations. These latent flow fields are typically learned through image-level reconstruction supervision without direct flow annotations. In ambiguous regions containing repetitive or stochastic textures, rotating symmetric structures, or fast motion with blur, the matching evidence for a single query may contain multiple comparable and spatially separated peaks. Although the ground-truth intermediate frame provides indirect supervision, it may not uniquely identify the latent correspondence in ambiguous this http URL several locations provide multiple plausible matches, a single-flow estimator can retain only one displacement and discard the remaining candidates. If the selected match is incorrect or inconsistent with those of neighboring pixels, warping samples content from mismatched locations, producing ghosting, structural distortion, or this http URL address this limitation, we propose a multiple hypothesis flow estimation framework that preserves top-K candidate correspondences and selects one per location through a reliability-guided router. Each hypothesis is initialized from a coarse matching anchor and refined separately through anchor-centered local attention. Frame synthesis is thus conditioned on one selected flow-appearance hypothesis rather than a soft combination of candidate this http URL on the proposed MA-HD benchmark and public VFI benchmarks show that our method achieves the best LPIPS and DISTS among the compared methods.

---


### 140. [Thermodynamic Human-Computer Interaction](https://arxiv.org/abs/2608.07123)

**<font color=#1a73e8>作者：</font>** Uzafir Ahmad Rafaq, Muaz Hassan, Ali Muzaffar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Traditional human-computer interaction models rely on domain-specific techniques to model target prediction; models designed for cursor interaction prediction fail to generalize to mobile interfaces and vice versa. We introduce a unifying framework grounded in thermodynamics, proposing that human interaction is composed of phases in thermodynamic equilibrium and non-equilibrium. To demonstrate this, we derive Fitts' law and the proposed target prediction model from equilibrium thermodynamics by assigning kinetic and potential energies to a moving agent and target. Subsequently, we analyze the shortcomings of the prediction model and Fitts' law in edge cases, such as predicting intent for large targets. This analysis demonstrates that large targets cannot be accurately modeled using equilibrium thermodynamics. The proposed model scales across interaction modalities without modification, requires zero training data, and evaluates in constant O(1) time. Furthermore, we show that design properties such as the color of a button act as independent parameters that influence the attractive force exerted on an agent. Applied to live web prefetching tasks, the framework achieved an efficient Fetch:Click ratio of 1.37 and predicted the user's target with an accuracy of 98.1%.

---


### 141. [Online Conformal Prediction Beyond Feedback](https://arxiv.org/abs/2608.07139)

**<font color=#1a73e8>作者：</font>** Joar Skalse, Edoardo Pona, Osvaldo Simeone 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification is essential when deploying machine learning models in safety-critical applications. Online conformal prediction (OCP) provides theoretically principled uncertainty quantification for arbitrary black-box classifiers and non-i.i.d. data streams by constructing prediction sets that are guaranteed to contain the true label at a user-specified frequency. OCP usually updates prediction sets using feedback from previously deployed predictions. We instead study an OCP setting beyond feedback: on each round, the learner can either output a prediction set or query the correct label, but not both. Thus, no deployed prediction is ever evaluated directly. We reduce this problem to a partial monitoring game in which prediction actions return no observation and a separate query action reveals the label. The reward function is constructed in a way that encourages the learner to output small prediction sets while ensuring that the correct label is covered with a sufficiently high probability. To solve this game, we develop OCP with queries (OCPQ) by adapting the label efficient forecaster of Cesa-Bianchi, Lugosi, and Stoltz (2004) to our setting. For any black box classifier and any (non-i.i.d.) oblivious data stream of length $T$, OCPQ has $O(T^{2/3})$ expected regret and expected coverage at least $\beta-O(T^{-1/3})$ for a user-defined $\beta$, while querying only an expected $T^{-1/3}$ fraction of rounds. This provides coverage comparable to bandit-based OCP methods while requiring no feedback from deployed prediction sets. Experiments on real-world datasets further demonstrate the effectiveness of our approach.

---


### 142. ["Operator, can you hear me?" A Faithful Line into the UNISOC Baseband](https://arxiv.org/abs/2608.07143)

**<font color=#1a73e8>作者：</font>** Eduard Vlad, Philipp Mao, Marcel Busch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Baseband processors are reachable over the radio at all times. Their most security-relevant logic runs deep inside protocol state machines: the control-plane handlers that gate registration, authentication, and session setup. Analyzing that logic systematically requires introspecting the firmware as it runs, which makes re-hosting the baseband necessary. Existing re-hosting work approximates the execution environment and under-approximates the SoC complexity of the baseband processor together with its surrounding components, bringing this state practically out of reach. We instead model each surrounding component, co-processors, SIM, application processor, from what a real device does, and step them in lockstep with the baseband on one shared clock. That makes faithfulness checkable at component interfaces, rather than assumed.
We call this method Unislop and demonstrate it on the UNISOC UDX710, a platform in an estimated 10-15% of cellular modems and in automotive systems, not systematically analyzed before. Starting from a Quectel RM500U-CNV module, we gain code execution, defeat its firmware-integrity check, instrument the baseband, and recover its peripheral environment from the running device. The resulting re-host reaches the same control-plane states as the real device, establishes a full PDU session, and carries real IP traffic on both ingress and egress. The recovered components are shared across UNISOC's baseband lineup, so with additional reverse-engineering effort the same design extends to further targets.

---


### 143. [InstanceSplat: Instance-Aware Feed-Forward 3D Gaussian Splatting for Scene Understanding](https://arxiv.org/abs/2608.07144)

**<font color=#1a73e8>作者：</font>** Minchao Jiang, Xiaoxuan Ma, Shunyu Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) enables efficient and generalizable 3D reconstruction, but current feed-forward 3DGS methods for scene understanding remain largely category-oriented. In contrast, instance-aware 3DGS methods typically rely on per-scene optimization and often decouple reconstruction from instance and semantic learning, limiting reciprocal interactions among them. We present InstanceSplat, a unified feed-forward 3DGS framework for generalizable 3D reconstruction and instance-aware scene understanding from pose-free multi-view images. In a single forward pass, InstanceSplat constructs an instance-aware Gaussian representation that jointly encodes appearance, geometry, instance identity, and language-aligned semantics. Shared 3D Gaussians ground instance identities across views, producing renderable and cross-view-consistent instance features. To allow reconstruction and scene understanding to benefit from each other, we further design an instance-centric learning strategy that connects reconstruction, instance learning, and semantic learning through shared instance structure. Specifically, instance cues guide reconstruction, language-aligned semantics strengthen the discrimination of confusing same-category instances, and instance regions aggregate semantic evidence into coherent object-level predictions. Experiments on novel-view synthesis, instance segmentation, and open-vocabulary semantic understanding under varying input-view settings and on an unseen dataset demonstrate state-of-the-art performance, practical efficiency, and strong generalization.

---


### 144. [Interpretable reinforcement learning with decision-tree pruning](https://arxiv.org/abs/2608.07151)

**<font color=#1a73e8>作者：</font>** Mark Leon Ringer, Michel Tokic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning policies are difficult to inspect, but interpreting them is a prerequisite for trustworthiness. Converting a trained policy into explicit decision-tree rules improves transparency and the resulting artifacts often remain too complex for human understanding. We present a pruning process that simplifies such rule-based policies while preserving task performance and making edits to the policy auditable. The process defines a small set of structural and usage-aware operators and evaluates candidate edits by re-executing the policy to measure return and interpretability proxies. This exposes an transformation process from complex to compact policy structures. We investigate this approach on classic control and MuJoCo benchmarks, where pruning traces reveal consistent interpretability improvements while maintaining high performance.

---


### 145. [Machine Learning-Based Inter-Crystal Scatter Recovery for Ultra-High Resolution PET Imaging](https://arxiv.org/abs/2608.07155)

**<font color=#1a73e8>作者：</font>** Alexandre Bernier, Roger Lecomte, Jean-Baptiste Michaud  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inter-crystal scatter (ICS) events pose a significant challenge in ultrahigh- resolution positron emission tomography (UHR-PET), especially as detector crystals become smaller and their readouts increasingly segmented. Current approaches either reject these events, reducing sensitivity, or accept them with suboptimal positioning algorithms, degrading image resolution. We present a feed forward neural network to optimize ICS event recovery by inferring the line-of-response belonging to the first Compton interaction. Our approach was validated using both Monte Carlo simulations and experimental data from the fully pixelated LabPET-IIbased preclinical and brain UHR-PET this http URL demonstrate a 70% to 106% increase in sensitivity while preserving sub-millimeter spatial resolvability (down to 1.6 mm) compared to conventional methods. This ICS recovery approach is an effective solution that compensates for the lower detection efficiency of small, pixelated detectors in UHR-PET, enabling reduced scan times and lower radiation doses while largely preserving image quality.

---


### 146. [Capacity Confounds and Coverage Guarantees in Adaptive Sub-model Federated Learning](https://arxiv.org/abs/2608.07157)

**<font color=#1a73e8>作者：</font>** Alireza Moayedikia, Alicia Troncoso Lora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sub-model federated learning lets resource-constrained clients train width-reduced versions of a global model, but existing methods allocate capacity by device resources alone. A natural next step, allocating capacity by each client's data heterogeneity as estimated from the updates the server already observes, has been repeatedly suggested. We ask whether that step is possible, using HAS-FL, an adaptive capacity-allocation framework, as a test case. Our findings are threefold. First, validated against ground-truth label-distribution divergence on reproducible partitions, update-divergence estimates of client heterogeneity are dominated by capacity rather than data: across two corrected estimators, multiple datasets, and all seeds, the estimates correlate strongly and negatively with device capacity, and no data signal remains once capacity is controlled for. This previously undocumented confound affects any method estimating client statistics from sub-model updates. Second, adaptive allocation has a hidden failure mode: when every client is capped below full width, the uncovered parameters stay at random initialization and progressively corrupt the global model. A simple coverage guarantee removes the failure and explains why uniform allocation collapses. Third, a matched-budget control settles what adaptivity contributes: random allocation to the same average budget performs no differently on both image benchmarks, and on the naturally partitioned text benchmark the adaptive policy is the weakest of the three strategies while consuming the most capacity. Sub-model training remains valuable because it admits constrained clients at quadratically reduced cost, but what protects accuracy is parameter coverage rather than allocation intelligence. Its apparent benefits come from capacity budgeting and coverage, and future designs need heterogeneity signals separable from capacity effects.

---


### 147. [Edge Sparsification via Temporal Forman-Ricci Curvature for Dynamic Graph Learning](https://arxiv.org/abs/2608.07158)

**<font color=#1a73e8>作者：</font>** Poupak Azad, Cuneyt Gurcan Akcora, Kiarash Shamsi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal graph learning has become essential for analyzing real-world systems whose interactions continuously evolve over time, including financial transaction networks, communication systems, and online social platforms. However, learning from large-scale temporal graphs remains computationally challenging when networks are dense and rapidly changing. To address this limitation, we propose a network-curvature-inspired edge sparsification framework for dynamic graph learning. Our proposed method, TRicci, extends classical Forman-Ricci curvature to directed weighted temporal graphs by capturing structural support, temporal recency, and local interaction competition.
Experiments on 9 transaction networks and 3 temporal graph benchmark datasets demonstrate that the proposed framework preserves predictive performance across multiple graph-level prediction tasks. The results show that TRicci sparsifies temporal graphs by approximately 80% while reducing end-to-end downstream training and inference time by an average of 55.94%, without substantial degradation in predictive performance. Our findings suggest that temporal curvature can serve as a principled basis for scalable temporal graph learning by preserving predictive temporal-structural information under substantial sparsification.

---


### 148. [Fluid-DiT: Graph-Free Diffusion Transformers for Fluid Flow Simulations Learning](https://arxiv.org/abs/2608.07161)

**<font color=#1a73e8>作者：</font>** Shentong Mo, Guolin Ke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulating complex fluid flows requires capturing full equilibrium distributions rather than just mean trajectories, yet high-fidelity solvers remain computationally prohibitive. Recent advances, such as Diffusion Graph Networks (DGNs), have combined diffusion models with graph neural networks to sample equilibrium states directly from unstructured meshes, enabling distributional accuracy even from short simulations. However, graph-based diffusion approaches suffer from hand-crafted architectural constraints, limited receptive fields in message passing, and costly multi-scale designs, which restrict scalability to larger and more complex domains. We propose Fluid-DiT, a Graph-Free Diffusion Transformer that replaces graph message passing with attention-based denoising, eliminating explicit graph design while preserving the ability to model distributions of chaotic flows. Our framework introduces a latent-space formulation that disentangles geometric fidelity from distributional learning, reducing high-frequency artifacts and accelerating sampling. By leveraging the transformer's global receptive field, Fluid-DiT naturally captures both local flow structures and long-range correlations without requiring hierarchical graph coarsening. On canonical benchmarks including laminar cylinder wakes, ellipse-flow systems, and turbulent 3D wing experiments, Fluid-DiT consistently outperforms graph-based diffusion baselines in both sample quality and distributional accuracy, achieving higher $R^2$ correlations and lower Wasserstein distances. Moreover, it generalizes robustly from short, incomplete trajectories to unseen Reynolds numbers and geometries, demonstrating strong scalability.

---


### 149. [Momba: Network Modernization Improves Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2608.07180)

**<font color=#1a73e8>作者：</font>** Adam Štafa, Santeri Heiskanen, Petr Novotný 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in deep reinforcement learning (RL) have shown that improving neural network architectures can yield substantial gains in sample efficiency and asymptotic performance without altering the underlying algorithms. In contrast, work on multi-objective reinforcement learning (MORL), which aims to discover a set of policies that balance trade-offs among conflicting objectives, has predominantly focused on algorithmic innovations, leaving the area of architectures underexplored. While the optimal policies and value functions can differ significantly depending on the trade-offs, MORL algorithms commonly represent them with simple feedforward networks conditioned on the trade-off. This raises the question of whether the performance of the algorithms could be improved with more expressive function approximators. In this paper, we integrate recent advances in neural network design: (i) observation and feature normalization, (ii) weight normalization, and (iii) modeling of distributional returns with an entropy-regularized MORL algorithm. The empirical results across standard continuous control benchmarks demonstrate that these changes substantially improve the quality of the produced solution sets without requiring major changes to the underlying algorithm.

---


### 150. [Conformal Fusion Under Missing Modalities](https://arxiv.org/abs/2608.07183)

**<font color=#1a73e8>作者：</font>** Alireza Moayedikia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal fusion architectures typically assume all modalities are available at inference, yet sensor failures, acquisition variability, and cost constraints routinely produce incomplete observations. Existing work treats modality absence as a prediction-accuracy problem, leaving a more basic question unanswered: whether a model's confidence estimates remain calibrated when an entire input stream is removed. We argue that missing-modality robustness and calibrated uncertainty are a single coupled property, and introduce Modality-Conditioned Conformal Fusion (MCCF), an architecture that addresses both at once. MCCF combines a multimodal bottleneck fusion backbone trained with modality dropout, per-modality evidential heads producing modality-decomposed Dirichlet distributions, and a Dempster-Shafer combination rule that fuses the per-modality evidence into a joint predictive distribution; an absent modality contributes vacuous evidence that is structurally ignored, so the fused uncertainty automatically reflects the reduced information without test-time imputation. A Mondrian conformal calibration module keyed on the modality-presence mask then provides finite-sample group-conditional coverage for every non-empty modality subset. MCCF is, to our knowledge, the first method with formal coverage guarantees under arbitrary modality availability through architectural integration rather than post-hoc recalibration, and the evidential decomposition yields per-modality vacuity scores that localise uncertainty to the absent modality responsible. Across a synthetic problem and three real multimodal benchmarks, MCCF holds its target coverage on every modality-presence subset, substantially narrows the coverage gap between full and partial modalities relative to a marginal split-conformal baseline, and imposes no measurable accuracy cost relative to temperature-scaled and evidential baselines.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-190](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
