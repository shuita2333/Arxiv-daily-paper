# 🧠 大模型相关研究 | 2026年10月12日

> 本类共 **288** 篇论文：已确认 **273** 篇，待复核 **15** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-288](./part-06.md)

---

### 151. [Sera: Semantic Representation Aggregation for Reliable and Interpretable Battery Health Forecasting](https://arxiv.org/abs/2610.11567)

**<font color=#1a73e8>作者：</font>** Jiawei Li, Fang Liu, Wei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Battery state of health (SoH) forecasting is important for battery management, but remains challenging due to nonlinear degradation and heterogeneity across batteries. Existing data-driven approaches primarily use temporal models to learn from numerical battery time series, and higher-level degradation characteristics are often not explicitly represented. These characteristics, however, can provide degradation guidance to support reliable forecasting and make the influence of degradation more interpretable. In this paper, we propose \textsc{Sera}, a \underline{se}mantic \underline{r}epresentation \underline{a}ggregation framework that complements temporal modelling with degradation semantics. Guided by battery domain expertise, \textsc{Sera} extracts degradation semantics from time series and constructs two complementary representations using rule-based knowledge and LLM-based interpretation. The representations are independently encoded and integrated with the representation learned by temporal models through gated aggregations. Experiments on the mainstream benchmark across multiple prediction horizons and different temporal models show that \textsc{Sera} consistently improves forecasting performance, achieving up to a 37.3\% reduction in prediction error over the temporal baseline and enhanced generalizability. Counterfactual analysis examines how forecasts respond to changes in degradation semantics to assess interpretability. The results show that prediction responses are consistent with the meanings of key degradation descriptors across tested horizons. Together, these findings demonstrate that structured degradation semantics and effective aggregation can improve forecasting accuracy and support reliable and interpretable battery health forecasting for advanced battery management.

---


### 152. [Memory Type Varies: Empowering LLM Agents for Long-Term Memory with Diverse Strategies](https://arxiv.org/abs/2610.11573)

**<font color=#1a73e8>作者：</font>** Yi Wen, Derong Xu, Pengyue Jia 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The memory capabilities of Large Language Models (LLMs) have garnered increasing attention recently. Despite great success achieved, existing retrieval-based memory approaches typically overlook the differences between memories and employ a unified strategy to process all memories, leading to suboptimal performance. Thus, an intuitive question arises: can we categorize memory into different types and select appropriate strategies? However, given the topic-rich, scenario-complex, and boundary-blurred nature of memory scenarios, achieving precise classification of memories is not easy. To address this challenge, we propose a memory multi-class dataset in this paper, termed TriMEM, which provides precise annotations for memory types across diverse scenarios. Building upon this foundation, we propose a novel memory framework, named MemoType, which can adaptively recognize each memory and query type with the learned router model. With the memory and query routing, MemoType can retrieve the memory with corresponding query types and design tailored retrieval strategies, thereby enhancing the retrieval performance. Moreover, we theoretically prove that any single retrieval strategy is subject to a fundamental upper bound on its expected retrieval precision in multi-class corpora, leading to systematic precision degradation. Extensive experiments on three datasets demonstrate that MemoType consistently outperforms existing methods, achieving up to 16.18% improvement in Recall@1.

---


### 153. [Smoothing the Top-k Exposure Boundary for Sparse Mixture-of-Experts](https://arxiv.org/abs/2610.11575)

**<font color=#1a73e8>作者：</font>** Yunkai Chai, Tong Zhu, Xiaoye Qu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts models scale parameter capacity efficiently while maintaining a fixed compute budget per token. However, traditional training paradigms enforce a static choice of top-$k$ experts, which converts a continuous routing distribution into a rigid step function. This constraint introduces a brittle boundary where highly competitive experts are arbitrarily separated into full-supervision and zero-feedback zones based on minor score fluctuations. To address this issue, we propose Elastic Expert Routing, which stochastically samples the active expert budget from a localized discrete distribution centered at $k$. Over multiple training iterations, this mechanism softens the sharp threshold into a gradual probability distribution. Because the sampling neighborhood remains symmetric, this approach matches the expected computational cost of deterministic training, while preserving the inference budget. Extensive experiments demonstrate the efficacy of our method on both supervised fine-tuning and from-scratch pretraining settings. During supervised fine-tuning, elastic routing improves downstream macro-averages on OLMoE-1B-7B and Qwen3-30B-A3B by $+0.84$ and $+2.02$ points, respectively. In addition, in from-scratch pretraining, it outperforms the static top-$k$ baseline by $1.6$ points on average across downstream tasks.

---


### 154. [Adapting English Quality Classifiers for Multilingual LLM Pretraining Data Selection](https://arxiv.org/abs/2610.11585)

**<font color=#1a73e8>作者：</font>** Vinko Sabolčec, Bettina Messmer, Yassine Turki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language model (LLM) pretraining highlight the role of high-quality training data in improving performance. While model-based filtering has proven effective in selecting high-quality subsets from web-scale corpora, especially for high-resource languages, low-resource languages face challenges due to limited availability of annotated data. This work explores extending quality filtering to over 100 languages by proposing a multilingual adaptation approach that converts an existing English quality classifier into a multilingual variant. Our approach proposes training a small multi-layer perceptron on top of Transformer encoder-only model embeddings, using multilingual text as input and scores obtained from English classifiers applied to machine-translated text as labels. Our 1B, 3B and 8B scale experiments show that our approach maintains the downstream LLM benchmark performance of existing multilingual model-based filtering baselines, without harming regional and cultural knowledge benchmarks. To further evaluate cross-lingual generalization, we compare classifier scores of high-quality synthetic data and web samples, and the correlation of classifier scores with LLM-based ones, revealing that the classifier can learn the scoring criteria of its original English variant, even for languages not included in its training data.

---


### 155. [Measuring Cultural Alignment Beyond the Average: A Framework for Evaluating Maternal-Health LLM Interactions in Indian Contexts](https://arxiv.org/abs/2610.11586)

**<font color=#1a73e8>作者：</font>** Umaira Izhar, Gunjan Arora, Pushpendra Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing evaluation methods for healthcare LLMs primarily assess factual correctness,safety, and fluency, while providing limited insight into whether generated interactions reflect culturally situated healthcare reasoning. This limitation is particularly important in maternal health, where care decisions are shaped by social and relational norms. We introduce MH-INDIC, a culturally grounded evaluation framework for maternal-health interactions in urban and semi-urban North Indian contexts that operationalises cultural behaviour through ten dimensions of maternal-health reasoning. Using a 26-item survey administered to 102 pregnant and postpartum women from urban and semi-urban North India, we evaluate ten LLMs. We distinguish population level cultural alignment from profile-level behavioural variation. Although several models approximate the human population-level distribution, all evaluated systems exhibit substantially lower variation across demographic and household profiles than the human cohort, revealing a gap between aggregate alignment and profile-conditioned sensitivity. As a downstream application of MH-INDIC, we use the strongest-aligned proprietary and open-source models to generate culturally conditioned maternal-health dialogues under zero-shot, self-conditioned, and human-grounded prompting. Human-grounded conditioning produces stronger profile alignment and dialogue quality ratings, suggesting that measured cultural profiles can improve the cultural grounding of generated interactions

---


### 156. [NeuroDivSim: An Interactive Tool for Model-Based Reflection on Cognitive Diversity in Interface Design](https://arxiv.org/abs/2610.11590)

**<font color=#1a73e8>作者：</font>** Eske Beckefeld, Henrik H.J. Detjen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent approaches to simulated and synthetic users offer new ways to support design, but raise questions about how computational representations of users should contribute to design practice. We present NeuroDivSim, an interactive tool that explores simulation as an inspectable mechanism for reflecting on cognitive diversity during design and prototyping. Rather than using an LLM to act as a simulated user, NeuroDivSim uses generative AI to construct inspectable task, interface, and environment models from a usage scenario. After human review, these models are combined with explicit cognitive reference configurations and processed through deterministic simulation. This enables designers to hold a modeled usage situation constant while varying cognitive assumptions and tracing their consequences to interaction steps and rule-based design recommendations. We further report an exploratory pilot evaluation (N=10) that provided formative insights into how participants engaged with the workflow and informed subsequent refinements to the presentation of models, simulation results, and recommendations.

---


### 157. [Probing for Long-Horizon Deductive Reasoning Capabilities in Language Models with Prolog](https://arxiv.org/abs/2610.11592)

**<font color=#1a73e8>作者：</font>** Hadeel Al-Negheimish, Jasna Ilieva, Yoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current frontier LLMs can theoretically process long contexts with 1M tokens or more. But to what extent can they go beyond simple retrieval and perform deeper reasoning over such long contexts? We empirically investigate long-horizon reasoning capabilities of LLMs, focusing on deductive logic expressed in Prolog. We construct ProloNg, a synthetic testbed to probe Prolog Long Reasoning, which systematically varies the complexity (reasoning depth) of problems, where the hardest case has a reasoning depth of 22 and 62k context length. We study 8 reasoning models across 5 families of frontier LLMs, and find that performance degrades substantially as reasoning depth grows, with the majority of models approaching chance beyond depth 10.

---


### 158. [Large Language Model Turnover Undermines Screening for Artificial Intelligence-Assisted Scientific Writing](https://arxiv.org/abs/2610.11599)

**<font color=#1a73e8>作者：</font>** Kazuki Nakajima, Takayuki Mizuno  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Journals and conferences have begun to screen submitted manuscripts for text written using large language models (LLMs). The reliability of this screening rests on benchmark evaluations against a fixed set of LLM versions, while the versions in actual use keep changing. Here we quantify how this LLM turnover affects the screening of scientific manuscripts. We paired 4,000 pre-ChatGPT abstracts from the Proceedings of the National Academy of Sciences with their rewrites by 23 LLM versions from three vendors, released between June 2023 and August 2026. We then trained detectors under maintenance scenarios ranging from a detector retrained on every new version to one trained once and never updated. Detectors trained only on a vendor's past versions can collapse at the boundaries between model generations: calibrated to falsely flag 1% of human-written abstracts, they catch above 99% of rewrites just before the sharpest boundary and 3.8% just after it. Detectors trained on later versions can also miss rewrites of earlier ones. Vocabulary differences between versions largely track where detection transfers and where it fails. In the two screening scenarios we simulated, screens covering all 23 versions either flagged one in eight human-written abstracts or missed one in three rewrites of the newest version. Indeed, a commercial detector missed most rewrites of the version just after the sharpest boundary while flagging almost no human-written abstracts. Research-integrity policy should therefore treat the benchmark accuracy of a detector as provisional, to be re-verified with every LLM release, including earlier versions.

---


### 159. [Error-Propagation Modeling for Failure Attribution in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2610.11600)

**<font color=#1a73e8>作者：</font>** Jiaqi Liao, Yuanzhao Zhai, Huanxi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (MASs) are increasingly used to solve complex tasks through coordinated reasoning, tool use, and interaction with external resources. However, attributing failures in such systems remains challenging because the observed outcome often does not directly reveal the error responsible for the failed execution. In this work, the attribution target is the decisive error, defined as the agent--step pair whose correction would recover the failed execution. Existing approaches largely identify suspicious steps without explicitly modeling how errors propagate across interactions or persist in unresolved loops, making decisive errors difficult to distinguish from downstream failure symptoms. We propose \textbf{E}rror-Propagation \textbf{M}odeling for \textbf{F}ailure \textbf{A}ttribution (\textbf{EMFA}). EMFA constructs a structured representation of the failed trajectory, models both cascading propagation and persistent interaction loops, and uses propagation-aware candidate screening followed by counterfactual verification to identify the decisive agent--step pair. On the Who\&When benchmark, EMFA achieves state-of-the-art step-level attribution accuracy and remains competitive at the agent level. It improves the previous best step-level results by 3.45 and 4.40 percentage points on the Hand-Crafted and Algorithm-Generated subsets, respectively.

---


### 160. [Where Do the Tokens Go? Understanding and Reducing Costs in LLM Agents for Vulnerability Discovery](https://arxiv.org/abs/2610.11602)

**<font color=#1a73e8>作者：</font>** Li Lu, Yanjie Zhao, Hongjie Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents can spend millions of tokens during vulnerability discovery without producing a working proof of concept (PoC). What consumes that budget, and why does it fail to produce results? We diagnose these costs and failures through a multi-axis open-coding study of 200 CyberGym traces, spanning four agents (i.e., Codex, OpenCode, Cybench, and EnIGMA) under an unaided baseline and four existing efficiency methods. The study reveals three key findings. First, different agents vary substantially in success and cost, and higher spending does not consistently yield better outcomes. Second, code localization and understanding, together with vulnerability reasoning and trigger design, account for 60.4% of tokens and represent the two leading bottlenecks in failed runs. Third, only 24.4% of matched comparisons preserve success at lower total cost; unsuitable signals and auxiliary overhead limit the benefits of existing methods. Motivated by these findings, we present AVRI, an Agent-centric Vulnerability Reasoning Interface built around a persistent Bidirectional Evidence Trace (BET). BET connects how the harness consumes input with the conditions required to make a selected operation unsafe, retaining source-supported correspondences alongside the agent's hypotheses and open questions. Reading, analysis, and persistence commands help agents build and reuse this evidence rather than repeatedly retrieve and reconstruct it. On 20 evaluation tasks, AVRI reduces total cost by 18.0% for Codex and 23.7% for OpenCode while preserving success rates and improving or maintaining recall.

---


### 161. [NanoProof: Open and Efficient Automated Theorem Proving in Lean 4](https://arxiv.org/abs/2610.11605)

**<font color=#1a73e8>作者：</font>** Matěj Kripner, Milan Straka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce NanoProof, to our knowledge the first factorized execution-guided theorem prover in Lean 4 whose training data, extraction tooling, training pipeline, and weights are all released, making it end-to-end reproducible using open-source resources. To this end, we build and release a dataset of structured proof trees, as well as a tool for programmatic interaction and data extraction within the Lean 4 formal verifier. To support sustainable research, we focus on compute efficiency to facilitate accessible training and evaluation. NanoProof achieves 50.8% pass@16 on MiniF2F-Test, exceeding the two closest systems of its class, HyperTree Proof Search and ABEL, at roughly 90x and 7x less compute, and using more than four orders of magnitude less compute than AlphaProof. Stronger open-weight provers exist, but they are fine-tuned from large pretrained language models and release neither training data nor pipeline; NanoProof shows that the factorized execution-guided class of provers can be rebuilt from scratch with modest resources.

---


### 162. [Where to Adapt Matters: Layer-Selective Fine-Tuning for Capability Retention](https://arxiv.org/abs/2610.11620)

**<font color=#1a73e8>作者：</font>** Zhiqiang Pang, Zihong Sun, Qi Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) enables large language models (LLMs) to adapt to specialized tasks, but often at the cost of degrading general capabilities acquired during pretraining. Existing approaches primarily mitigate this trade-off through data replay or regularization, relying on additional data or explicit optimization constraints. We instead focus on a different question: where should adaptation be applied? We find that fine-tuning different Transformer layers produces different target-task gains and degrees of capability degradation, suggesting that not all layers are equally suitable for adaptation. To characterize this difference, we use layer-wise empirical Fisher information to measure target-task sensitivity. However, computing Fisher scores requires backward computation and becomes increasingly expensive for large models. We therefore introduce input--output cosine similarity as a lightweight, forward-only proxy for ranking layer sensitivity. Across models and tasks, layers with lower input--output similarity consistently exhibit higher empirical Fisher scores. Building on this observation, we propose Layer-Selective LoRA (LS-LoRA), which places trainable LoRA adapters only in layers with low input--output similarity. Experiments on mathematical reasoning and code generation show that LS-LoRA improves average target-task performance while retaining substantially more commonsense reasoning capability than standard all-layer LoRA, demonstrating that carefully choosing where to adapt can provide a simple and effective way to balance target-task adaptation and general capability retention.

---


### 163. [Evidence-Traceable Dynamic Interviewer Architecture for Expertise-Adaptive Qualitative Interviews Using Local LLMs](https://arxiv.org/abs/2610.11651)

**<font color=#1a73e8>作者：</font>** Aisvarya Adeseye, Jouni Isoaho, Adeyemi Adeseye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated interviewers and conversational agents are increasingly used in research, recruitment, customer service, and education. However, many existing systems rely on fixed question sequences and provide limited context-based personalization without considering participants' knowledge, which can lead to repetitive or irrelevant follow-up questions. Therefore, there is a need for an adaptive interviewing system that can adjust question depth while maintaining conversational continuity and semantic progression. To address this, an Evidence-Traceable Dynamic Interviewer Architecture is presented using a locally hosted Large Language Model (LLM), with the interview continuously adapted throughout the entire conversation based on the participant's responses and evolving context. The interviewer profiles participants' expertise in real time to generate knowledge-appropriate questions, well-articulated responses, and smooth transition messages that support conversational continuity. A five-module prompt-driven architecture and persistent interview-state record support these functions. The interviewer was evaluated with 246 participants. Expertise Profiling module (M3) showed 78.9% exact agreement with independently reported participant expertise, with a weighted Cohen's K of 0.80. Generate Iterative Questions module (M4) showed a strong expertise-complexity association (p=.79, p<.001), and participants reported high relevance (mean 4.41), engagement (mean 4.32), and satisfaction (mean 4.38), providing evidence that the architecture's adaptive components operated consistently with their intended functions while participants reported a positive interview experience.

---


### 164. [Harness Evolution Hits a Ceiling: When Weight Training Should Begin](https://arxiv.org/abs/2610.11655)

**<font color=#1a73e8>作者：</font>** Yuan Tian, Bing Hu, Hao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving a long-horizon LLM agent means evolving the harness around a frozen model or training its weights. We let a self-evolving harness make the system stronger first, then cross seed and evolved harnesses with base and trained weights to learn which gains the trained model keeps and which still need the runtime. We show that the right lever can be read off the agent's failure composition: labelling failed trajectories by the first signal that fires separates process failures (blocked calls, loops, exhausted step budgets) from content failures (a delivered plan that is poor). Harness evolution repairs the former, the behaviour it instils can be trained into the weights, and content failures are what weight training is for. On DeepPlanning, a self-evolving harness loop lifts the held-out score of Qwen3.5-4B from 0.16 to 0.30 and of Qwen3.5-9B from 0.32 to 0.44; for 4B, held-out delivery rises from 55% to 90% while content failures are left for the weights. LoRA adapters trained on evolved-harness trajectories internalise the gain: under the original harness they add +0.13 on held-out tasks for both sizes; on 4B they stack with the harness to more than double the held-out score, and on 9B the adapter alone matches the full evolution line, cutting content failures from a quarter of trajectories to one in twenty. A placebo adapter trained on answer-shuffled trajectories falls below the base model. The loop transfers to WebArena-Lite (+0.09 on 117 unseen tasks), where the gain lives in what the model sees and adapters do not add to it. The result is a diagnose-then-intervene rule applied twice: read the failure composition to choose between harness and weights, then read what the accepted edits changed to decide which gains to train in. Scores are four-rollout means against fresh anchors, same-night except where marked, across eight models from six families and two benchmarks.

---


### 165. [DIAL-OPD: Learning More from Fewer Tokens in On-Policy Distillation](https://arxiv.org/abs/2610.11659)

**<font color=#1a73e8>作者：</font>** Anhao Zhao, Haoran Xin, Junlong Tong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) supervises student-generated trajectories with token-level teacher signals. Its sampled-token variant avoids the cost of full-vocabulary probabilities. Yet we find that training on fewer tokens can outperform full-token OPD, challenging the intuition that more supervision improves learning. This motivates selecting tokens by learning value. Existing disagreement-based criteria ignore probability scale: tokens assigned negligible probability by both models, termed low-low tokens, can receive large log-ratio rewards and hinder learning. We propose DIAL-OPD, a token-selection method that bridges log-probability and probability spaces by weighting reward magnitude with the logarithmic mean of teacher and student probabilities. A parameter beta controls this weighting, and the highest-scoring tokens are retained. Across 4 teacher-student pairs and 7 mathematical reasoning benchmarks, we compare DIAL-OPD with 9 baselines. Retaining only 40% of tokens, it outperforms Vanilla OPD and its full-token variants, with mean accuracy gains reaching 5.25 percentage points over Vanilla OPD, and doubles AIME25 Pass@16 from 13.33% to 26.67%. It also achieves up to an 18% relative improvement in mean accuracy over the strongest token-selection baseline at matched retention ratios. With a 4B teacher, DIAL-OPD surpasses the strongest full-token baseline using an 8B teacher at both student scales, showing that effective supervision allocation can outweigh teacher scaling. Further analysis shows that moderate beta balances suppressing low-low tokens against preserving useful disagreements. Token-level evidence reveals that DIAL-OPD filters high-reward tokens with limited reasoning value while preserving supervision critical to reasoning correctness.

---


### 166. [Perceptually Grounded and Semantics-Aware Evaluation for Holistic Co-Speech Gesture Generation](https://arxiv.org/abs/2610.11669)

**<font color=#1a73e8>作者：</font>** Nick Milkin, Lanmiao Liu, Esam Ghaleb 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Holistic and semantics-aware co-speech gesture generation has advanced rapidly, yet evaluation remains behind: objective metrics do not consistently reflect human perception, and semantic appropriateness remains difficult to quantify. We present a perceptually grounded and semantics-aware benchmark that combines standardized model comparison, human-centered metric validation, and fine-grained semantic evaluation. We first curate a list of 13 objective metrics covering different aspects, including distributional similarity, geometric fidelity, kinematic quality, cross-modal synchrony, and semantic appropriateness. For the semantic-appropriateness category, we propose a new metric, Semantic Gesture Preservation (SGP), which measures how far semantic gestures in the ground truth are preserved in the generated gestures. For this, we augment the BEAT2 dataset's annotations using a multi-modal LLM. We then conduct a perceptual study where 101 participants score generated gestures among five dimensions, including human-likeness, motion diversity, absence of animation errors, speech timing and content match. We systematically analyze objective metric--subjective score correlations. Unlike Semantic Score (SC), which shows no significant association with the evaluated perceptual dimensions, SGP is selectively aligned with speech-aware human judgments. We construct five target-specific composite metrics aligned with the subjective dimensions. These composites improve perceptual alignment across all five dimensions, with the largest gains for absence of animation errors and content match, indicating that complementary objective signals can better approximate human judgments than individual metrics alone. Overall, our results show that objective metrics require validation against subjective evaluations.

---


### 167. [VESSI - VLM-Enhanced Support for Surveillance and Investigations](https://arxiv.org/abs/2610.11674)

**<font color=#1a73e8>作者：</font>** Saverio Cavasin, Pietro Tedeschi, Mattia Tamiazzo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated video surveillance analysis has become a critical component of intelligence infrastructures and Law Enforcement agencies. Traditional systems lack the semantic module for comprehensive situational awareness and forensic tasks, limiting their ability to interpret events meaningfully or support post-incident investigations. This slows operational insight and increases the burden on human analysts. Recent advances in Vision-Language Models (VLMs) offer promising pathways to bridge this gap. To address this, we propose VLM-Enhanced Support for Surveillance and Investigations (VESSI), a VLM-based framework designed to enhance automated video surveillance analysis through prompt-driven interrogation of video sequences where salient visual features are converted into textual descriptions. We test our framework with four state-of-the-art models. Since most datasets for this task are unlabeled, we also propose the Composite Model Utility Score (CMUS) to assess VLM performance. Experimental results show that our solution substantially improves the analysis capabilities of human operators and enhances the flexibility of automated surveillance systems. In our evaluation, the most reliable model flagged potentially relevant activity in more than 66% of the videos while reducing review time by more than 85%, offering a practical balance between selectivity and efficiency. The model ordering produced by the reference-free CMUS evaluation was reproduced by the normal-video CMUS evaluation and matched the false-positive-rate ordering obtained from 5,909 manually referenced frames. This agreement supports the operational use of the score within the evaluated setting.

---


### 168. [TRACE: Diagnosing Verifier Brittleness in Agentic Evaluation](https://arxiv.org/abs/2610.11678)

**<font color=#1a73e8>作者：</font>** Radhika Gaonkar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Verifier scores now serve as both benchmark metrics and training rewards for large language model (LLM) agents, and a change in score is routinely read as a change in capability. It may instead reflect a change in the evaluation. We introduce TRACE, a protocol that turns a score change from a verdict into a testable diagnosis: it applies a targeted change to one part of an evaluation, compares paired runs, checks whether the agent's behavior changed, and rescores unchanged trajectories to test whether the scoring rule is responsible. In a controlled suite of 25 synthetic tasks, renaming tools lowers a scripted agent's score by 0.250 even though it performs exactly the same operations; restoring the original names at scoring time closes the entire gap, while the same mutation exposes a genuine behavioral failure in a second agent. On public $\tau^2$-bench tasks with four LLM agents, an initial 30-task study finds mixed reward changes whose one clear effect does not replicate. In a larger follow-up on 88 new tasks with repeated runs per condition, renaming tools or reformatting tool outputs leaves reward unchanged to within $\pm$0.10 for seven of eight agent-change pairs, whereas tool names that deliberately mislead lower every agent's reward by 0.20-0.44, showing that the setup can detect real effects. Identical reruns flip 15-36% of task outcomes, so single-run comparisons cannot separate presentation effects from run-to-run variation. Two frontier LLM judges give consistent verdicts when a fixed trajectory is presented differently, yet disagree with each other on 57% of the same records, largely because one grades procedure rather than outcome. TRACE thus separates what a score change says about the agent from what it says about the measurement.

---


### 169. [A 3D Characterization Framework for Intelligent Sequential Decision Making](https://arxiv.org/abs/2610.11696)

**<font color=#1a73e8>作者：</font>** Sadig Gojayev, Carolina Fortuna  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Puzzles are widely used to evaluate the reasoning capabilities of artificial intelligence (AI) systems for sequential decision making, yet approaches originating from different paradigms are rarely compared under unified conditions. To address this gap, we introduce a three-dimensional characterization framework that enables the analysts of AI methods by 1) projecting them to the Markov decision process (MDP) sequential decision making formalism, 2) degree of autonomy through human prior ranking of their designs and, 3) skill and computational cost. Using this framework, we analyze how representative graph-based, reinforcement learning, and large language model (LLM)-based approaches differ in their design choices and performance characteristics, instantiated respectively by Neurosolver, forward-backward reinforcement learning (FBRL), and automated thought-of-search (AutoToS), including a double-agent extension of thought-of-search (DA-ToS). The analysis relies on the Tower of Hanoi puzzle that provides a controlled benchmark with well-defined rules and scalable complexity, enabling consistent comparison across increasing problem sizes. The 3D characterization reveals that LLM-based methods, due to their weakly constrained action-space design, shift complexity from architecture to inference-time verification, leading to substantially higher memory and runtime costs than Neurosolver and FBRL.

---


### 170. [Internalizer: Portable Context-to-Parameter Mapping for Very Large Language Models](https://arxiv.org/abs/2610.11715)

**<font color=#1a73e8>作者：</font>** Peter Devine, Nick Ryan, Benjamin Sirb 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hypernetworks that map a context directly to a LoRA adapter let a large language model carry that context in its weights, but prior work has demonstrated them only on base models of up to 14 billion parameters.
We present the Internalizer, a state-of-the-art, portable Context-to-Parameter Mapping hypernetwork that generates document-specific LoRA adapters for the frozen 284B-parameter DeepSeek v4 Flash, a target two orders of magnitude larger than in any previous work. Most of its parameters live in a model-agnostic trunk with only thin entry and exit layers per base model, so it trains cheaply against small models before being ported to the large one.
On unseen documents of up to 4096 tokens, the generated adapters reach 84.9% top-1 and 97.8% top-5 teacher-forced accuracy against 63.4% and 83.5% for the base model, with nothing in the context window but a three-word instruction.
Once the hypernetwork is trained, a single forward pass turns any document into an adapter for such a model, which could be served alone for speed or alongside the document in the window to raise accuracy further.

---


### 171. [Spectral Weight Decay: Inducing Low-Rank Structure in Neural Network Weights](https://arxiv.org/abs/2610.11730)

**<font color=#1a73e8>作者：</font>** Dmitrii Andriianov, Andrey Veprikov, Aleksandr Beznosikov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard weight decay treats each weight matrix as a vector and ignores its spectral structure. We introduce spectral weight decay, a post-step decoupled nuclear-norm update that applies additive rather than multiplicative spectral shrinkage. We connect the update to approximate proximal descent and show that its sensitivity to update order can exceed that of conventional $\ell_2$ weight decay near rank deficiency. Across LLaMA models with $124$M to $500$M parameters, spectral weight decay lowers effective rank and improves SVD-LLM compression at matched validation loss. At $500$M and a $4\%$ distortion budget, it reaches $1.89\times$ compression and $1.18\times$ GPU inference speedup, compared with $1.14\times$ and $1.01\times$ after standard weight decay. Under fixed-horizon training with $60\%$ label noise, it also improves final mean clean-test accuracy over matched $\ell_2$ regularization by up to $17.8$ points on MNIST and $4.6$ points across four BERT-base tasks. Code is available at this https URL.

---


### 172. [MemTrial: Learning When to Trust Memory in LLM Portfolio Agents](https://arxiv.org/abs/2610.11732)

**<font color=#1a73e8>作者：</font>** Guanghao Wu, Zhuo Cai, Shoujin Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents for portfolio management learn from experience: they credit each experience in their memory with the outcome of the decisions that used it. In financial markets, however, this outcome mostly reflects the market move shared by all decisions on that date, so the credit tracks the market rather than the experience, and these agents often do worse than simply holding the equal-weight (1/$N$) portfolio. We ask how an agent can credit an experience with what it changes, and answer it by putting memory on trial: drafts of the same decision with and without an experience face the same market, so the outcome they share cancels in their difference. Our agent, MemTrial, drafts each decision with eight combinations of its retrieved experiences, chosen by a fractional factorial design, and credits each experience with its Banzhaf value, the average of these differences. As each date occurs once and each draft is a noisy LLM sample, these credits are noisy and may not hold on new dates. MemTrial therefore pools them across dates and similar experiences with a hierarchical Bayesian model, acts on them only after they have predicted unseen dates, and otherwise stays anchored at a conservative reference such as 1/$N$. On four benchmarks, MemTrial not only benefits from experiences that matter (the best of 15 methods on a semi-synthetic benchmark with known experience quality) but also limits its losses when its values do not hold (at most 2.2\% below 1/$N$ on PortBench and InvestorBench, against 15--38\% for the best experience-learning agent). Averaged over five settings, it improves the utility of the best experience-learning agent by 21.2\%, and with eight LLMs it beats every LLM-based baseline on InvestorBench.

---


### 173. [RAGenome: Scaling Retrieval-Based Genomic Language Models to Long Contexts](https://arxiv.org/abs/2610.11761)

**<font color=#1a73e8>作者：</font>** Frederikke Isa Marin, Panagiotis Antoniadis, Dionysia Danai Brilli 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The genome holds the blueprint that governs the biological properties of the cell. Consequently, advancing our knowledge of genomic function is crucial both for a broader understanding of biology and for continued biomedical advances. The success of large language models on natural language and protein sequences has motivated similar efforts on genomic data. However, standard genomic language models (gLMs) often require extremely large computational resources and still fall behind traditional methods on some downstream tasks. Recently, MSA-based pretraining has been proposed as an efficient alternative, but existing models are limited to short input contexts, restricting their use to short-range tasks, such as variant effect prediction. In this work, we present RAGenome, the first retrieval-based gLM that scales pretraining to longer contexts (100$\times$ longer than existing MSA-based gLMs), allowing it to capture both across-species evolutionary relationships and within-species longer-range interactions. Trained on whole-genome alignments from 100 vertebrates, RAGenome substantially improves the long-range capabilities of MSA-based gLMs, raising gene finding performance from 0.45 to 0.60, while remaining competitive on purely evolutionary-based tasks like prioritizing pathogenic variants. RAGenome provides competitive gLM performance at a fraction of the training cost, unifying evolutionary modeling and long-range capabilities within a single, flexible, scalable framework. Code is available at this https URL.

---


### 174. [Thinking Inertia: LLMs Keep Thinking When Told Not To](https://arxiv.org/abs/2610.11765)

**<font color=#1a73e8>作者：</font>** Dianqiao Lei, Kevin Qinghong Lin, Pan Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) increasingly ship with explicit "thinking modes", yet their counterpart, "no-thinking", has received far less attention. We study LLMs' no-thinking behavior along two axes. a. How to measure no-thinking? Prior work typically defines no-thinking through proxies such as a disabled thinking mode or the absence of long traces. These proxies are unreliable: disabled thinking modes may still emit reasoning, while long traces may contain filler rather than genuine inference. We instead normalize each response into a pre-answer trace and final answer, and evaluate it at three levels: (i) Empty-Thinking Rate for strict answer-only compliance; (ii) instruction-aware Question-Pre-answer Relevance for similarity between the question and pre-answer trace; and (iii) LLM-as-judge Explicit Inference Rate for visible explicit inference. Together, these metrics distinguish answer-only output, relevant but non-inferential text, and explicit inference. b. How does no-thinking vary across tasks and models? We evaluate six prompting interventions on six LLMs across Boolean, multiple-choice, and open-ended questions. We find that explicit no-think controls cannot reliably eliminate visible inference. Models instead exhibit "Thinking Inertia": explicit inference persists even under strict controls and becomes more prevalent as the answer space opens. Accuracy remains stable on Boolean and multiple-choice tasks, whereas open-ended tasks reveal a trade-off between answer-only compliance and task accuracy. Rewriting the same questions across answer spaces shows that supplying candidate answers makes answer-only responses easier to produce. These findings establish no-thinking as a non-trivial capability: stopping explicit reasoning cannot be assumed from model settings or instructions alone and deserves systematic evaluation alongside reasoning ability.

---


### 175. [From Video Clips to Creation Trajectory: Sora100K for AI-Native Video Creation](https://arxiv.org/abs/2610.11770)

**<font color=#1a73e8>作者：</font>** Sicong Yang, Ruihuan Yang, Jian Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-Native video creation is shifting from isolated video clips toward iterative video creation workflows. However, existing datasets remain largely video clips, representing video generation and editing as separate tasks rather than connected stages of a video creation workflow. In this paper, we introduce Sora100K, a dataset that represents the AI-Native video creation workflow as a structured video creation trajectory. Specifically, we first identify video creation trajectories and decompose them into three subsets according to their structural roles: text-to-video generation records as roots, single-turn video editing records as editing edges, and multi-turn video editing records as complete trajectories. Then, we use a VLM to assign semantic annotations for generation roots and editing-operation annotations for editing edges. A strict construction pipeline further reconstructs source-to-edit lineage, editing order, and intermediate video states while ensuring data quality. Finally, we perform lightweight adaptation on LTX-2 models to assess the supervision value of Sora100K. The results show improvements in visual quality, multi-shot generation, and cross-shot consistency, while successive-turn evaluation reveals that following multi-turn editing instructions remains challenging. Sora100K establishes a new data foundation for AI-Native video creation beyond isolated video clips and toward structured video creation trajectory. The dataset and supplementary materials are publicly available at this https URL.

---


### 176. [Safe Actions Alone Do Not Ensure Safe Agents: Identifying Unfulfilled Obligations with Guard Models](https://arxiv.org/abs/2610.11773)

**<font color=#1a73e8>作者：</font>** Youwei Feng, Yitong Zhang, Yuetong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Guard models are increasingly used to safeguard LLM-based agents, primarily by identifying actions that agents are forbidden to perform. However, identifying forbidden actions alone is insufficient to ensure agent safety. In this paper, we argue that agent safety also depends on identifying required yet unperformed safety-critical actions, which we call obligations. Our preliminary study on a popular benchmark for evaluating safety shows that 56.92% of GLM-5.3 trajectories contain unfulfilled obligations, compared with only 30.00% containing forbidden actions. This finding reveals unfulfilled obligations as a major and previously overlooked source of safety risk. However, to our knowledge, no existing benchmark evaluates whether guard models can identify these obligations. To close this gap, we introduce ObligationBench, the first benchmark for evaluating the capability of obligation identification, comprising 240 expert-validated trajectories covering issue resolution, feature development, and terminal operations. Our evaluation of 14 representative models reveals substantial limitations: the highest recall and exact-match rate are only 48.97% and 10.00%, respectively. To address these limitations, we develop ObligationGuard using 40,000 synthetic training examples. ObligationGuard achieves 57.52% recall and an exact-match rate of 21.67%, surpassing all evaluated models on both metrics. We call on the community to incorporate obligation identification into the design and evaluation of future guard models to improve agent safety.

---


### 177. [RouterInterp: Understanding Superposed Specialisation in Mixture of Experts Routing](https://arxiv.org/abs/2610.11775)

**<font color=#1a73e8>作者：</font>** Ilya Lasy, Nora Yinuo Cai, Kola Ayonrinde  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture of Experts (MoE) models scale more efficiently than dense models by routing tokens to modular expert networks that are only active for processing a fraction of tokens. A leading hypothesis for the performance of MoE models is that each expert specialises in a single, coherent domain. However, interpretability efforts that assume this hypothesis have generally been unsuccessful. We propose and present evidence for an alternative account that we call the Superposed Specialisation Hypothesis (SSH): experts specialise in a disjoint union of fine-grained features rather than one broad domain. Leveraging the SSH, we introduce RouterInterp, a method for interpreting expert routing that identifies Sparse Autoencoder features most predictive of routing decisions and produces unified natural language explanations. On gpt-oss-20b, RouterInterp explains expert routing with ${\sim}65\%$ higher detection accuracy than prior token statistics based methods. This work provides a scalable method for generating more accurate explanations of expert routing and increases our understanding of a previously uninterpretable component of foundation models.

---


### 178. [DPPM: Dual-Path Parametric Memory for Personalized Language Models](https://arxiv.org/abs/2610.11776)

**<font color=#1a73e8>作者：</font>** Yuhao Chen, Shuochen Liu, Jiayao Shi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term personalization requires language models to use interaction history to track users' preferences across sessions. Parametric memory encodes this interaction history into model parameters or adapters, reducing the need to include it in the inference context. However, independent context compilation leaves cross-session integration unspecified, while recurrent updates can attenuate earlier evidence. To address these challenges, we propose Dual-Path Parametric Memory (DPPM). Its Evidence path directly pools representations of the interaction history to preserve earlier evidence, while its Delta path sequentially updates an associative state to capture changes. Fusing both outputs produces history-conditioned LoRA adapters that combine evidence accumulation with ordered revision. Across multiple backbones, DPPM outperforms the evaluated baselines, achieving 54.22% on PersonaMem-v2 and 86.79% on PrefEval. These results suggest that DPPM provides a simple and effective design choice for cross-session personalized parametric memory.

---


### 179. [Compile the Table: Query-Calibrated Operator Compression for Tabular In-Context Learning](https://arxiv.org/abs/2610.11784)

**<font color=#1a73e8>作者：</font>** Xu Zhao, Jiaming Zhao, Bin Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular in-context learning (ICL) has emerged as a training-free and accurate paradigm for tabular prediction, but current approaches to compressing its in-context examples face an accuracy-throughput tradeoff: fixed subsets can sacrifice accuracy, while query-specific retrieval limits cache reuse and batching across queries, reducing throughput. We propose QCOC (Query-Calibrated Operator Compression), which exploits the exchangeability and repeated use of in-context examples by compiling their full KV cache once into compact memory shared across subsequent queries. Instead of retaining raw examples, QCOC clusters their states into joint-KV prototypes, preserves per-cluster multiplicities and the original example count, and calibrates prototype values against attention query vectors produced by the in-context examples through an anchored closed-form solution. Prototype compression drives the speedup, while value fitting helps preserve accuracy. On 64 held-out OpenML-CC18 datasets, QCOC achieves the highest mean accuracy among the compared compression and retrieval methods at both retained counts. Across 12 configurations on seven long tables, it ranks first among compressed methods in ten and averages 0.23 percentage points below full context. Compressing 8,192 in-context examples to 512 memory slots yields a 10.5x cache compression ratio; excluding one-time compilation, in a single-core CPU online-serving comparison over 1,000 queries, QCOC is up to 508x faster than dynamic retrieval baselines and 1.98x faster than full-context inference. These results show that QCOC enables compact-memory reuse and efficient inference across queries while retaining accuracy close to full context.

---


### 180. [Easy to anticipate, hard to compute: boundary dependence finds the computed outputs that entropy patching misses](https://arxiv.org/abs/2610.11790)

**<font color=#1a73e8>作者：</font>** Nicolás Vera Zúñiga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Byte-level language models such as the Byte Latent Transformer (BLT) group bytes into patches and run their large global model once per patch. BLT starts a patch where a small model's next-byte entropy is high, so global compute goes where the next byte is hard to predict. We show that this rule has a systematic blind spot: positions whose type is predictable but whose value must be computed, such as the number after "=" in a worked math solution. Under tight patch budgets, entropy-triggered layouts skip these positions, and accuracy on them collapses. In Meta's BLT-1B with patch starts on 10% of bytes, the entropy rule puts a patch start at 16% of the computed results in GSM8K solutions and gets 19.0% of them exactly right; a boundary after each "=" at the same patch count gets 51.8%, and entropy combined with a label-free boundary-dependence signal gets 67.1% (default layout at 26% of bytes: 76.8%). The gap survives adapting BLT-1B to the budget with low-rank fine-tuning (32.9% vs 72.7%, three runs per rule, paired p < 1e-200) and grows with model size in byte models trained from scratch at a 10% budget: at 1M, 12M and 50M parameters, boundary dependence beats entropy on final answers by -1.6, +10.1 and +19.8 points, and at 50M it gets 35.9% of computed results against 13.9% (3 seeds each). BLT's entropy-jump rule helps neither target at 50M. The entropy trigger of Scratchpad Patching is likewise indistinguishable from random scratchpads on final answers (5.6% vs 5.9%, 5 seeds), while answer-start scratchpads give 38.1%. The effect is specific to computed values: copies and lookups gain little, and values the model cannot compute gain nothing. Boundary dependence, the rise in the model's own loss when a patch start is removed, measured per two-byte context, finds these positions without labels: combined with entropy it beats the hand-written rule on computed results.

---


### 181. [Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks](https://arxiv.org/abs/2610.11794)

**<font color=#1a73e8>作者：</font>** Haoyu Zhao, Zhengxu Yu, Zhiyuan He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning to act in unfamiliar environments requires agents to infer how the world works and revise that understanding as new evidence arrives. Yet limited observations can support multiple world models that explain past interactions but predict different outcomes in unseen states. We introduce Memento 3, building on the Memento series to enable frozen LLM agents to continually learn explicit world models through external memory. The agent maintains a natural-language rulebook as persistent semantic memory, recording revisable hypotheses about environment dynamics while leaving unknown aspects underspecified. It compiles this rulebook into executable code for prediction and planning. Through a continual loop of observation, reflection, rule revision, compilation, and verification, the agent uses prediction errors to refine both the rulebook and its code. Updated code is accepted only when the LLM judges it faithful to the rulebook and cell-exact replay reproduces the observed transitions. We investigate this process as a model-based route to recursive self-improvement (RSI): the agent autonomously explores the environment, revises its world model, and uses verified updates to guide subsequent interaction and learning, while the underlying LLM remains fixed. A population extension maintains multiple world models in parallel, sharing interaction evidence and using their predictions to guide exploration. On ARC-AGI-3, the single-model agent clears every level of all 25 public games, achieves a mean Relative Human Action Efficiency (RHAE) of 100.0, and uses 44% of the human action count. In an Atari Pong case study, a learned feedback controller wins 21:0 in each of three evaluated episodes with different openings, without further LLM calls.

---


### 182. [Seek-and-View Reasoning for Multi-View Spatial Understanding](https://arxiv.org/abs/2610.11810)

**<font color=#1a73e8>作者：</font>** Qixiang Chen, Cheng Zhang, Fucai Ke 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing approaches to multi-view spatial reasoning operate largely on sparse input views. Vision-language models (VLMs) are thus restricted to understand a scene and infer spatial relations within these fixed views, leading to fragile cross-view alignment and geometry-to-language bottleneck. To address these issues, we formulate a novel Seek-and-View reasoning approach to find implicit cross-view spatial evidence by locating a question-relevant view to support the spatial reasoning. To realize this approach, we propose Vantage, a training-free model-agnostic reasoning framework that pairs a VLM with a 3D foundation model: a viewpoint-grounded reasoning stage for question analysis and view planning, followed by a geometry-grounded evidence augmentation stage to effectively synthesize and incorporate visual evidence into the final reasoning. Comprehensive experiments on six VLMs demonstrate consistent improvements on five benchmarks without fine-tuning. Overall, by revealing spatial evidence through view-grounded reasoning, Vantage can largely reduce reliance on language-based cross-view alignment and improve multi-view spatial understanding. Our code is available at this https URL.

---


### 183. [From Pixels to Structure: Lightweight Vision-Language Models for Document OCR and Structured JSON Extraction](https://arxiv.org/abs/2610.11818)

**<font color=#1a73e8>作者：</font>** Uddipan Basu Bir, Vincent Christlein, Andreas Maier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While massive, closed-source Vision-Language Models (VLMs) set strong benchmarks for document understanding, their dependence on commercial APIs limits adoption in institutional archives due to data autonomy concerns, recurring costs, and the environmental footprint of hyperscale computing. This is especially acute in heritage digitization, where documents include historical handwriting, domain-specific terminology (e.g., jewelry, prehistory, architecture), and non-standard layouts requiring high-dimensional structured extraction. We present a comparative study of eight open-source lightweight VLMs (up to 7B parameters) for Optical Character Recognition (OCR)-to-structure across three university heritage collections. Given a document image, models must extract text and generate schema-compliant JSON, enabling automatic validation and downstream use. We evaluate models under a constraint-aware protocol across zero-shot, few-shot, and fine-tuning settings, measuring extraction fidelity and structured-output quality using Character Error Rate (CER), Approximate Normalized Levenshtein Similarity (ANLS*), and mean Average Precision F1 (mAP-F1). Against a fine-tuning baseline, we further test the independent impact of (i) hyperparameter optimization, (ii) classical image preprocessing (illumination flattening, denoising, and CLAHE), and (iii) multi-stage training. Finally, we analyze the trade-off between dataset-specific fine-tuning and a single multi-dataset checkpoint, where joint training enables one model to operate across collections but can shift performance between datasets. Overall, we show that carefully adapted VLMs with up to 7B parameters can provide a sustainable, private, high-performing alternative to manual transcription or commercial black-box systems, and we offer actionable guidance for heritage institutions seeking institution-controlled OCR-to-JSON extraction.

---


### 184. [From Suppression to Repair: Mitigating Object Hallucination in Large Vision-Language Models via Localized Distribution Alignment](https://arxiv.org/abs/2610.11826)

**<font color=#1a73e8>作者：</font>** Chen Zhao, Xingping Dong, Jiachun Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object hallucination remains a major obstacle for large vision-language models (LVLMs) to generate reliable content. An intuitive mitigation strategy is to suppress hallucination-related components in hidden representations. However, these components may also contain useful information, and suppressing them can weaken the model's multimodal capabilities. In this paper, we propose ResOT, a training-free method that repairs representations at inference time through localized distribution alignment. Specifically, ResOT projects dominant hallucinated directions away from the faithful subspace, forming a low-dimensional residual subspace for intervention. Within this subspace, ResOT uses Gaussian optimal transport (OT) to align the hallucinated distribution with the faithful one. The resulting map defines repair targets with minimal changes to the original representations. At inference, ResOT adaptively controls how far each token state moves toward its OT target. Experiments on three representative LVLMs show that ResOT substantially reduces object hallucination while improving image caption quality and multimodal performance across multiple benchmarks. Code will be released.

---


### 185. [Anytime-valid detection of LLM weight exfiltration](https://arxiv.org/abs/2610.11843)

**<font color=#1a73e8>作者：</font>** Ines Ortega-Fernandez, Mateusz Kowalczyk, Keri Warr  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A compromised LLM inference server can leak model weights by encoding payload bits in otherwise plausible token choices. A replay of the same prompt in a trusted server can expose such deviations, but benign numerical nondeterminism also causes token mismatches. Patient attackers can therefore hide within normal variation unless evidence is combined across responses. We introduce a prompt-level e-process that calibrates whole-response mismatch events on trusted benign traffic and accumulates evidence sequentially while, under a calibration-transfer assumption, controlling the probability of any false alarm over an unbounded monitoring horizon. We evaluate it on four models against a seed-blind attack and a stronger seed-aware attack that hides payload bits only in near-ties to remain stealthy, analyzing the channel capacity vs detectability trade-off. Compared with a hard per-token alarm, the e-process combines weak evidence across responses while providing explicit anytime false-alarm control.

---


### 186. [Detecting Spin in Clinical Trials with Large Language Models](https://arxiv.org/abs/2610.11845)

**<font color=#1a73e8>作者：</font>** Tjaš Ajdovec, Marko Robnik-Šikonja, Simon Šuster  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spin in clinical trials includes reporting practices that distort the presentation of results. This is particularly critical in medicine, where spin is present in more than 50% of randomized controlled trials that fail to reach statistical significance. The comparison of primary and reported outcomes is crucial for detecting several types of spin, including outcome switching. We used 300 pairs of outcomes labeled with semantic similarity to develop a system for automatic detection of outcome switching. We evaluated baseline text similarity models and open-source LLMs using generated similarity scores and the Youden index to determine the classification threshold. The proposed approach involves prompt engineering, classification based on token probabilities, and majority voting for the final decision. The results on the test set of 2,496 examples with an F1 score of 0.78 and an accuracy of 0.90 outperform baseline text similarity models but trail behind fine-tuned versions of BERT. We used LLMs to generate natural language explanations for the classified instances and manually assessed their quality.

---


### 187. [SemField: A Simple, Linear, Continuous, yet Robust Semantic Watermark](https://arxiv.org/abs/2610.11848)

**<font color=#1a73e8>作者：</font>** Varun Gumma, Navonil Majumdar, Soujanya Poria  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of Large Language Models (LLMs) necessitates reliable watermarking techniques to identify AI-generated text and ensure appropriate attribution. While token-based watermarks are vulnerable to paraphrasing, a central challenge for semantic watermarking is to turn sentence meanings into a stable, well-calibrated document-level signal. To this end, we introduce SemField, a simple, training-free semantic watermark that embeds a continuous, linear signal directly into the sentence embedding space. Using a shared secret key to define a specific Gaussian direction, SemField iteratively evaluates candidate sentences and selects those that maximize the alignment of the cumulative document aggregate with this targeted direction. We also propose SemField-PL, a polarity-locked variant that first determines the optimal orientation from the initial sentence and continuously reinforces it throughout the generation process. The document-level aggregated formulation guarantees exact invariance to sentence reordering and provides theoretical bounds against structural tampering, such as sentence insertion and deletion. Lastly, with extensive evaluations across three models, we demonstrate that both variants outperform 12 recent baselines. Across clean detection and four paraphrasing attacks, both variants achieve a mean True Positive Rate (TPR) of 88.2% to 90.4% at a 1% False Positive Rate (FPR), all while maintaining comparable perplexity and naturalness as human-generated content. We open-source our implementation at this https URL

---


### 188. [GRPODropout: Less is More for Online Reinforcement Learning Rollouts](https://arxiv.org/abs/2610.11854)

**<font color=#1a73e8>作者：</font>** Hexuan Deng, Zihao Yan, Xuebo Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) methods such as GRPO substantially improve large language model reasoning but often suffer from policy entropy collapse: the loss of sampling diversity weakens exploration and limits further improvement. Existing methods address this issue either through algorithm-level interventions, such as reward modification and entropy/KL regularization, or through token-level reweighting. We investigate a complementary perspective: entropy collapse can also be mitigated by changing which generated rollouts contribute to policy updates. Under the same sampling budget, not all rollouts contribute positively to an update, and selectively excluding some can improve learning. To address this, we propose GRPODropout: before the standard update, we use a simple strategy that selectively removes a small number of high-probability positive-advantage rollouts and recenters the retained advantages. To motivate this design, we develop a rollout-level theoretical analysis that guides method design and threshold selection. The method changes only rollout usage, and adds negligible computational overhead. Experiments show higher accuracy than original GRPO and higher actor entropy while using fewer rollout samples for updates, illustrating "less is more." This work provides insight into RL rollout usage: removing some rollouts can improve performance. Code is available at this https URL.

---


### 189. [LEVER: Adaptive Cost-Aware Proof Search Over AND/OR Graphs](https://arxiv.org/abs/2610.11862)

**<font color=#1a73e8>作者：</font>** Nihal Jain, Shuangjie Yao, Begum Cicekdag 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematicians value proofs for more than correctness: among correct proofs, simplicity, purity and the computational cost of finding them vary widely. Yet LLM-powered theorem provers largely search for any correct proof, and improve its quality only after it is found. We propose LEVER, a proof search algorithm that makes the objective over correct proofs programmable and optimizes it during search. LEVER scores partial proofs over an AND/OR proof graph, combining realized objective values with predictions for open subgoals, so the objective guides search before a proof is complete. The same mechanism optimizes computational cost, proof length, topical impurity, and even their weighted combinations, while the Lean kernel enforces correctness. On PutnamBench in Lean 4, under matched budgets, LEVER costs 34% less than a strong single-conversation agent while raising the solve rate from 80% to 96%. On reducing topical impurity, i.e., how far a proof strays from its theorem's subject, it improves over post-hoc refactoring (42% reduction against 33%) at two-thirds of the cost and more reliably; on proof length, the metric refactoring is built for, it approaches refactoring. Varying the objective's weights traces a quality-cost trade-off curve, so the user can choose how much a better proof is worth. Overall, LEVER is a performant, cost-efficient and tunable proof search algorithm for navigating the space of correct proofs.

---


### 190. [A Security Meta-Model for Retrieval-Augmented Generation Systems](https://arxiv.org/abs/2610.11893)

**<font color=#1a73e8>作者：</font>** Steve Nouyep, Sébastien Salva, Maxime Puys  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems extend large language models (LLMs) with external knowledge through a multi-stage pipeline. While this architecture can improve the factual grounding of generated answers, it introduces structural attack surfaces that extend beyond those of standalone LLMs. In this paper, we introduce a security meta-model that captures explicit causal relationships between RAG surfaces, attacks, weaknesses, risks, and CIA impact (Confidentiality, Integrity, Availability). Its purpose is to provide security engineers with a structured and user-friendly framework for gathering and assessing the risks, weaknesses, and mitigations relevant to their RAG deployment. We designed the meta-model through an iterative, structured analysis of 43~publications (2023--2026) and instantiated it as a catalog populated with the security threats and remediations reported in the literature. Filtering the catalog according to a deployment configuration produces a risk profile containing the risks applicable to that deployment. An interactive web visualizer lets users navigate the catalog as a graph, follow causal chains, and explore stakeholder-specific views. Analysis of the catalog revealed a persistent imbalance between attack-focused and defense-focused research, a concentration of threats at ingestion, and coverage gaps affecting output integrity. Coverage is assessed against the OWASP LLM Top~10, and operational applicability is illustrated across textual, graph-based, and multimodal RAG configurations.

---


### 191. [Automated Assembly Instruction Generation from CAD Models Using Grounded Large Language Models: A Human-in-the-Loop Framework](https://arxiv.org/abs/2610.11896)

**<font color=#1a73e8>作者：</font>** Aaron Dsouza, Mohammed Azeez Khan, Ashutosh Mishra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Assembly documentation is a downstream manufacturing artifact that is still usually authored by interpreting CAD models by hand. Structured product data and large language models are both available, yet studies of CAD interpretation, assembly sequence planning, instruction writing, and human oversight have largely proceeded separately. This paper formulates CAD-grounded assembly instruction generation: the production of natural-language assembly procedures constrained by structured engineering information extracted from CAD models. The proposed framework maps a STEP assembly to a typed ProductGraph intermediate representation, derives a precedence order by deterministic topological sorting, realizes each step as language conditioned only on selected graph context, attaches per-step visual documentation, and applies rule-based and model-assisted checks. PDF export remains disabled until a human reviewer resolves every quality flag. The case study establishes endto-end feasibility on a built-in six-part reference assembly: the pipeline preserves a reported assembly order and carries quantity, material, and torque into an exported manual page. Generalization and geometric validation remain open empirical questions. The contribution is an architecture that separates engineering state, deterministic reasoning, grounded language realization, verification, and human release.

---


### 192. [Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent System](https://arxiv.org/abs/2610.11899)

**<font color=#1a73e8>作者：</font>** Irene Weber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly embedded as components in software systems, marketed under labels such as chatbot, copilot, retrieval-augmented generation, workflow, coding agent and AI agent. Whether these labels denote genuine architectural forms or serve as branding has not been assessed systematically.
In the sources surveyed, labels do carry architectural content, most clearly in vendor usage: copilot denotes a router-worker architecture operating a host application under step-by-step user confirmation, while the more recent shift to the label agent coincides with AI-planned multi-step execution of which the user sees only the outcome. The coding agents of four major providers share one architecture, a reason-and-act loop delegating to subagents.
This survey describes seven recurring forms---LLM chats, custom agents, retrieval-augmented generation (RAG), AI-enhanced workflows, copilots, coding agents, and, in part, agentic RAG---in a common vocabulary of agents and tools. Each is characterized along four structural dimensions (agentic RAG only partially): the architectural pattern, the control of execution and the point of user intervention, the number of agent calls per task, and tool use. An illustrative corpus of 22 systems from research publications and vendor documentation grounds the descriptions and shows where they reach their limit.

---


### 193. [Can Decision Models Understand Stance? Evaluating Jev Against General-Purpose LLMs](https://arxiv.org/abs/2610.11901)

**<font color=#1a73e8>作者：</font>** Xing Li, Jinzhong Ning, Yijia Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stance detection requires identifying an author's attitude toward a given target, sometimes based on conversational context. Jev, a specialized decision model designed for structured decision-making, offers an alternative to general-purpose large language models (LLMs). In this work, we evaluate Jev on two stance detection datasets, VAST (English texts) and ZS-CSD (Chinese conversations), comparing it with four general-purpose LLMs and two fine-tuned models. Results show that Jev achieves competitive performance on VAST, matching GPT-5.6 and outperforming the other general-purpose LLMs. However, it falls behind stronger LLMs on ZS-CSD, particularly in distinguishing favor from against. Further analysis suggests that this limitation may be related to understanding reply relationships and stance direction rather than conversation length alone. These findings highlight both the potential and limitations of Jev for stance detection.

---


### 194. [Beyond Visual Enhancement: Adaptive Multi-Context Steering to Mitigate LVLM Hallucinations](https://arxiv.org/abs/2610.11907)

**<font color=#1a73e8>作者：</font>** Shuran Ma, JiaLe Li, Yuxin Dong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hallucination remains a significant challenge in Large Vision-Language Models (LVLMs). Existing training-free methods generally mitigate hallucinations through contrastive decoding or visual enhancement, often increasing the relative influence of visual evidence during generation. This raises a fundamental question: Can LVLMs dynamically regulate the contributions of different context sources to suppress hallucinations? In this work, we investigate and quantify how LVLMs coordinate multiple context sources during decoding and examine how this intrinsic behavior can guide hallucination mitigation. We find that LVLMs exhibit an intrinsic vision-attending tendency that can guide adaptive visual steering, while textual contexts can also contribute to hallucination mitigation. Motivated by these findings, we propose AIMS (Adaptive Information Multi-source Steering), a lightweight training-free framework that adaptively coordinates visual, prefilled textual, and generated contexts during decoding. Specifically, AIMS constructs compact prototypes for the three context domains and estimates their affinities with the current query to determine head-wise steering weights. The resulting multi-source steering direction is applied to the query representation, enabling adaptive context integration without additional model training or auxiliary forward passes. Extensive experiments across multiple LVLMs and decoding strategies demonstrate that AIMS effectively mitigates object hallucination while maintaining competitive general-purpose multimodal capabilities.

---


### 195. [Not Every Change Is Necessary: Recoverable Drift in Large Language Model Unlearning](https://arxiv.org/abs/2610.11915)

**<font color=#1a73e8>作者：</font>** Xunlei Chen, Qinghui Gong, Jingkun Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning in large language models aims to remove unwanted knowledge while preserving the model's remaining capabilities. Although existing methods use retention objectives or restrict where edits occur, achieving the desired forgetting level can still leave collateral changes that impair non-target behavior. Our recovery comparisons suggest that some of these changes can be reversed while preserving observed forgetting performance. In this work, we present Propose-Then-Project Unlearning (PTP-U), a framework that combines targeted forgetting with the recovery of non-target capabilities. PTP-U first applies local analytic edits to weaken target knowledge associations, then aligns non-target output distributions with those of the original model to recover capabilities while maintaining fixed forgetting constraints. Both stages serve a common goal: satisfying the forgetting requirements while preserving fluent generation and performance on non-target tasks. Across three benchmarks, PTP-U achieves the strongest forgetting-retention trade-off among evaluated methods, reaching 81.22%-91.03% forgetting while preserving 94.20% non-target utility on average. At matched forgetting, PTP-U consistently retains higher non-target utility.

---


### 196. [Event-Centric Memory with Query-Aware Graph Augmentation for Long-Term Conversational Agents](https://arxiv.org/abs/2610.11920)

**<font color=#1a73e8>作者：</font>** Yichen Liu, Chunfeng Yuan, Haowei Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For persistent and personalized conversational agents, memory systems can enable them to remember, update, and reason over long histories by storing past interactions and retrieving relevant information. Existing memory systems typically follow two paradigms: flat-structured memory and graph-based memory. The former is lightweight but leaves event relations and state updates implicit, while the latter explicitly models memory structure but incurs additional construction cost and introduces irrelevant relations over long histories. To address these limitations, we propose QGMem, a novel memory construction and activation framework motivated by human memory, in which experience is organized into events and query-relevant events are modeled by graph as working memory. QGMem converts long dialogue histories into event-indexed atomic memory units that preserve individual experiences and consolidates related units into dynamic memory traces that retain state trajectories and current states. When a query arrives, hybrid memory retrieval gathers complementary candidate memories, and query-aware reranking activates the most relevant units as a compact working memory. To expose relational dependencies in the working memory and support conflict-aware reasoning, QGMem organizes the working memory as a local graph, which is then encoded as a graph token and provided to the LLM together with the textual working memory to improve evidence utilization during answer generation. Experiments across six benchmarks validate the framework and show consistent gains in retrieval, multi-hop evidence composition, conflict resolution, and ultra-long dialogue reasoning with compact contexts and moderate inference cost.

---


### 197. [Revisiting Identity and Spectra Dispersion in Media-Bridged Time Series Forecasting: Linking Multivariate Signals and Narrative Flows](https://arxiv.org/abs/2610.11924)

**<font color=#1a73e8>作者：</font>** Jierui Lei, Wenjian Zhang, Qingyi Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Media-bridged time series forecasting is expanding to encompass traditional "multivariate" and emerging "multimodal" (e.g., through textual assistance). Existing Time Series Forecasting (TSF) models still rely on paradigm-specific relation, fusion, and temporal modules, hindering a common forecasting backbone across numerical and pre-aligned narrative-flow settings. To explore this, we propose the Multimedia Identity-Aware Prism Network (MIDAPN), a unified spatiotemporal forecasting backbone based on media-general graph adaptation and automatic temporal learning: (1) Following media pre-alignment, our Multimedia Identity-Aware Graph (MIDAG) revisits identity through static essence, dynamic behavior, and latent commonality, inducing affinities that extend variable-specific dependencies across media. Contextual Identity Modulation (CIM) further refines discriminative aggregation. (2) We develop Spectral Prism Convolution (SPConv) to automatically perform hierarchical temporal analysis, balancing coarse trends and fine-grained details. Meanwhile, its Adaptive Search Guidance configures a scale-efficient architecture for temporal-dimension reconstruction. These decoupled yet synergistic components jointly address media identity disentanglement and temporal-scale mismatch. Comprehensive evaluations involving 16 SOTA TSF models across 13 "multivariate" and 12 "multimodal" datasets, alongside targeted long-context comparisons against 14 time series foundation models and fused pretrained language models, demonstrate MIDAPN's consistent superiority and broad shared backbone compatibility. The code is available at \href{this https URL}{this https URL}.

---


### 198. [Does Target Alignment Mean Target Recovery? An Evidence-Ladder Study of Adversarial Claims on Contrastive Encoders](https://arxiv.org/abs/2610.11938)

**<font color=#1a73e8>作者：</font>** Tao Yang, Jianying Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks on vision-language models optimize an image toward a text target, then cite the attacked model's similarity score as evidence of success. We ask whether that score - victim-space target alignment (VTS) - predicts recovery of the target by an independent model. We first build a measurement instrument: supervised judges outside the attacked geometry, real-target blend controls, shuffled-target negatives, and a reference level derived from a 50% target-image blend. Two preregistered studies then compare six contrastive encoders under a matched attack at three perturbation budgets. Robustly trained encoders (FARE, TeCoA, PMG, TRADES) transfer substantially more independent evidence than vanilla CLIP or SigLIP; all eight contrasts reject at the bootstrap floor. However, no cell reaches the blend-derived reference level. The three best cells fall within its replication band, leaving practical recovery undecided. Within robust encoders, per-sample alignment gain correlates with evidence gain ($\rho = 0.24-0.51$); within vanilla CLIP the correlation is consistent with zero. Across encoders we find no monotone alignment-evidence relation. VTS is therefore informative only within a fixed robust encoder, and we provide a reporting protocol in its place.

---


### 199. [Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents](https://arxiv.org/abs/2610.11942)

**<font color=#1a73e8>作者：</font>** Jiaming Zhang, Xuan Wang, Fuyao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A login screen that appears after a tap on Sign in is expected; the same screen after a tap on View order is an attack. For GUI agents, safety is therefore a property of the transition rather than of the screen, and a monitor that inspects only screens can be defeated by reusing a legitimate one. Judging a transition requires an expectation of what should have followed the action. Existing GUI world models provide one, but they output it as text, code, or images, so checking it against the observed screen requires a second model to judge the two. We argue that a world model meant for verification should instead predict in the space in which observations are encoded, and present LGWM, a decoder-free, action-conditioned world model that predicts the representation of the next screen directly, trained without semantic annotation on 1.85M real GUI transitions. Verification reduces to a vector comparison, and the same signal reveals whether a mismatch is harmful. We evaluate on RSWT-BENCH, a diagnostic where each credential screen appears under both a legitimate and a hijacked transition, so detectors that see only the screen are at chance by construction. The training-free score reaches 0.987 AUC at 17 ms per decision, on par with the strongest closed-source VLMs and about ten AUC points above generative GUI world models at over three orders of magnitude lower latency. The residual direction reaches 0.953 AUC at separating harmful from benign violations, where prompted VLMs are near chance. Further analyses show that the prediction is a usable future state rather than an anomaly score. World models have mostly served as simulators or planners; our results point to a third role, verification, for which predicting in representation space is the natural design.

---


### 200. [When History Helps and Hurts: Selective History Use across Multimodal Turns](https://arxiv.org/abs/2610.11948)

**<font color=#1a73e8>作者：</font>** Shuoyang Sun, Kerui Gu, Hao Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable multimodal interaction depends on selective use of conversational history: an earlier question may remain relevant while its previous answer is outdated, whereas a current request may depend on historical evidence despite conflicting new observations. Existing multi-turn evaluations rarely separate these history-use demands from underlying question difficulty. To address this gap, we introduce ReTurn, a benchmark of 7,000 base tasks spanning visual and audio evidence for evaluating selective history use. For task-carrying history, Reconfirm/Reground require applying a historical question to current media while varying historical agreement; for evidence-carrying history, Retrieve/Rebind require answering a current question using historical media while varying current-media competition. Each pair preserves the target question, media, and answer. Tasks support open-ended and multiple-choice evaluation, with matched single-turn counterparts serving as answerability references. Across 13 omni-modal, vision-language, and audio-language models, median model-level open-ended accuracy falls from 93.7% with direct input to 72.3% in conversation. Behavioral probes show that high question recall can coexist with weaker task application, while competing media can redirect answers away from historical targets. Supervised adaptation yields only partial gains. ReTurn provides a controlled framework for assessing whether multimodal models select and use the historical information required by each request.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-288](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
