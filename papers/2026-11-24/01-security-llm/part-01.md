# 🔐 大模型安全相关研究 | 2026年11月24日

> 本类共 **7** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Beyond Prompt Heuristics: Assessing Child Safety Alignment in LLMs](https://arxiv.org/abs/2611.26965)

**<font color=#1a73e8>作者：</font>** Anika Misra, Chimaobi Okite, Rada Mihalcea  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Child-safety taxonomies typically characterize safety risks through a predefined set of harm categories, and existing evaluations largely operationalize these categories using prompts that explicitly invoke them. However, child-safety considerations can also arise in seemingly benign requests that lack recognizable harm-category cues. We therefore investigate how child-safety alignment generalizes to such settings. Across six models, we find considerably higher misalignment rates on requests without recognizable harm-category cues than on those containing such cues (80.0, 54.0, and 48.4 percentage-point gaps for Qwen3.5-27B, GPT-5.4-mini, and Claude-Haiku-4.5, respectively). Through controlled behavioral and mechanistic analyses, we find that introducing a single harm-associated word reduces misalignment across most models, with mechanistic evidence suggesting that child-safety reasoning may rely in part on lexical and semantic associations with words in the prompt. Our findings motivate evaluations that treat child safety as context-dependent, and not reducible to a fixed set of harm categories.

---


### 2. [Reward Integrity in Adversarial Reinforcement Learning for LLM Guardrail Red-Teaming](https://arxiv.org/abs/2611.26998)

**<font color=#1a73e8>作者：</font>** Chengming Liu, Leon Viti, Hongxu Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study reward fidelity in an adversarial reinforcement-learning loop for red-teaming financial-services language-model guardrails. Apparent wins can arise when an attack omits prescribed personally identifiable information (PII), or when a reward judge credits a response that did not break the targeted policy. On attacker-generated and public benchmark examples, TypeSafe Jev checks whether the prescribed PII is present. For outcome scoring, we compare the decision models TypeSafe Jev, Laya (pretrained and post-trained), and pretrained CLM-8B with logged Opus 4.8 judgements from a replay corpus. Post-training markedly improves Laya's agreement with the judge. A separate author-reviewed off-target set establishes that Opus can award false wins. The findings motivate specialised decision-model judges for checking prescribed PII in attack inputs and scoring target responses against the intended policy.

---


### 3. [Subverting Tool Arguments: Defense-Evading Metadata Poisoning in LLM Agents](https://arxiv.org/abs/2611.27041)

**<font color=#1a73e8>作者：</font>** Shih-Chieh Dai, Xinyu Sun, Haichuan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Conventional indirect prompt injection (IPI) attacks hijack an LLM agent's workflow through malicious instructions embedded in retrieved external content. The growing adoption of the Model Context Protocol (MCP) exposes another attack surface: tool descriptions supplied by third-party MCP servers. Attackers can manipulate this metadata to induce malicious argument generation during tool calls. The challenge is to ensure that the modified descriptions still appear benign to both LLMs and users. Existing IPI attacks, however, struggle to achieve both high attack success and low detectability in this setting. To address this challenge, we propose GRAFT, an LLM-based optimization method for crafting adversarial tool descriptions. Specifically, GRAFT uses a masking mechanism to identify argument-relevant token positions for targeted injection. It then iteratively refines candidate descriptions using dynamic mutation strategies proposed by an LLM, guided by the agent's tool choices and generated arguments. We evaluate GRAFT on three public datasets against several attack baselines. The results show that GRAFT achieves higher attack success while maintaining low detection rates across five filter-based defenses. It also bypasses several existing IPI defenses. Even under an adaptive defense trained on GRAFT-generated injections, GRAFT remains more effective than the baselines.

---


### 4. [No Perfect Guardrail & No Perfect Guard: On the Decidability of Output Policies for Large Language Models](https://arxiv.org/abs/2611.27260)

**<font color=#1a73e8>作者：</font>** Ahmed Amer, Loren Kinczel, Darrell D. E. Long  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Expecting guardrails to provide a general guarantee of safety fails to recognize the limits of computational enforcement and policy specification. We argue that promising such perfection is an ethical failure of precision, and that invoking it to abdicate responsibility is a moral failure. Guardrails can support responsible action, but cannot relieve researchers, developers, policymakers, or users of their obligations to examine what they claim, permit, and prevent.
We establish a precise computational boundary. If every finite string is a possible output of a language model, a computable guard that blocks every forbidden output and passes every permitted one exists if and only if the policy is decidable. For an undecidable policy, every guard misclassifies infinitely many strings, and every guard that blocks all forbidden outputs excludes infinitely many permitted ones. We apply this characterization to arithmetic truth, program behavior, and harmful instructions to an idealized recipient. We distinguish guards from execution monitors, identify bounded and interceptable cases admitting exact enforcement, and explain why the results establish no positive lower bound on average error.
Exact enforcement does not establish that a policy adequately captures safety. Conservative exclusion may withhold warnings, remedies, or challenges needed to recognize the policy's own defects. Human oversight cannot substitute for judgment: an apparent controller can become an instrument of purposes they have ceased to examine. Responsible governance requires continued critical challenge and the intellectual and moral humility to recognize possible flaws in our machines, rules, policies, and ourselves. The impossibility of a general assurance of perfection is a condition responsible practice must confront, not a responsibility that another guardrail - or another guard - can remove.

---


### 5. [TrojanMaxxing: One-shotting VLM Backdoors with Weight-Space Programming](https://arxiv.org/abs/2611.27425)

**<font color=#1a73e8>作者：</font>** Ahaan Dabholkar, Harshvardhan Patel, Michalis Polychronakis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent work shows that large language models (LLMs) can reason directly about the weights of other neural networks. Given only a natural-language objective, an LLM can inspect a model's weights, understand what they compute, and edit them directly without gradient-based optimization. This capability, termed weight-space programming (WSP), has been used to improve model performance on math reasoning, medical QA and other benchmarks. We propose TrojanMaxxing, a novel strategy to backdoor vision-language models (VLMs), by reframing it as a WSP task. We use Claude Opus 5.5 and Mythos 5.2 agents to backdoor VLMs without any optimization or training methods. The agents inspect the model weights, apply targeted edits, and co-design an imperceptible visual trigger that activates the backdoor. We then study the agents' strategies and present a thorough evaluation of the trojaned models on various benchmark datasets. TrojanMaxxing achieves attack success rates of 93%-100% on content moderation and 78%-100% on OCR while maintaining clean accuracy. Perhaps most consequentially, we show that injecting backdoors in a training-free manner is possible by simply, "asking an agent to do it".

---


### 6. [Cleave: Severing Guardrails and Auditing Spectral Coupling in Open-Weight LLMs](https://arxiv.org/abs/2611.27426)

**<font color=#1a73e8>作者：</font>** Feng Huang, Qiang Huang, Yue Gao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight Large Language Models (LLMs) are widely downloaded for their strong coding and reasoning capabilities and deployed locally beyond the provider's control. To prevent misuse, developers embed safety guardrails into these models before release. However, we find that these guardrails rely on the residual writing weights to trigger refusals. Based on this insight, we propose Cleave, a training-free attack that directly edits these weights to remove safety restrictions while preserving general capabilities. With Cleave, malicious users can either remove all guardrails or selectively lift only cybersecurity restrictions. Because this selective removal retains up to a 99% refusal rate on other harmful requests and avoids weight rank collapse, it evades both behavioral spot-checks and static weight audits. Across five open-weight LLMs from 7B to 320B parameters, Cleave achieves up to a 67.97% attack success rate on seven safety benchmarks, substantially outperforming existing white-box baselines. On 356 cybersecurity tasks and 15 live vulnerable services, it further boosts executable exploit generation by up to 24.0 times and compromises up to 66.7% of the targets. To counter this threat, we propose a dual-stage defense that combines pre-release subspace diagnostics with post-release weight-coupling audits, achieving 100% detection recall at a 1% false-positive rate.

---


### 7. [Autonomous Parameter Surgery: How LLMs Implant Selective Backdoors into Language Models](https://arxiv.org/abs/2611.27920)

**<font color=#1a73e8>作者：</font>** Xuyang Liu, Zhiwei Xu, Zirui Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Neural network weights are usually treated as opaque artifacts of gradient descent. Recent work on weight space programming, however, suggests that large language models can inspect and rewrite another network's parameters directly. In this paper, we ask whether a general language model can turn a natural language backdoor specification into persistent, selective weight edits on its own, without gradient training, layer hints, external corpora, or a prescribed editing formula. Using DeepSeek Flash at low reasoning effort inside a restricted workspace that blocks local CPU simulation, we test three open models (Qwen3.5-0.8B, Llama-3.2-1B, SmolLM3-3B) across two review domains (IMDb and Yelp; 18 independent sessions). Evaluated in fresh processes with the editor removed, the modified checkpoints reach 99.2% mean attack success on the editing domain and 97.6% transfer success on the unseen domain, while preserving clean accuracy, low control drift, and general capabilities within 1.7 points of the base models. Our traces show that the model converges on edits in the final layer in 17 of 18 runs and discovers both dense rank-one orthogonalization and single neuron weight surgery at an average cost of \$1.74 per run.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
